#!/usr/bin/env node
// The capture contract. A capture is one sweep of X written by the grabber.
// This file is the single definition of what a valid capture is: contract/CAPTURE.md
// describes it in prose and tests/check-capture.test.mjs pins every rule.
//
//   node tools/check-capture.mjs capture/2026/10/09/0600Z.json
//
// Prints PASS or the list of errors, and exits 1 on any error. Warnings never fail a run.
// No dependencies, Node 18 or later.
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { basename, dirname, join, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

export const SCHEMA = 'mts.capture/1';
// The desks and their beats are data: contract/desks.json is the one list.
const DESK_FILE = JSON.parse(readFileSync(new URL('../contract/desks.json', import.meta.url), 'utf8'));
export const DESKS = DESK_FILE.desks.map((d) => d.id);
export const BEATS = Object.fromEntries(DESK_FILE.desks.map((d) => [d.id, d.beats]));
const RUN_STATUS = ['ok', 'partial', 'down'];
const SWEEP_STATUS = ['ok', 'partial', 'down', 'skipped'];
const SWEEP_KINDS = ['discovery', 'desk', 'trends', 'watch', 'context', 'request'];
const AUTHOR_KINDS = ['person', 'creator', 'news', 'org', 'brand', 'official', 'parody', 'aggregator', 'unknown'];
const VERIFIED = ['blue', 'business', 'government', 'none'];
const MEDIA_TYPES = ['photo', 'video', 'gif', 'link', 'poll'];
const FLAGS = ['nsfw', 'graphic', 'private_individual', 'minor', 'ad', 'engagement_bait', 'ai_media_suspected', 'old_content', 'non_english'];
const STATES = ['live', 'deleted', 'unavailable'];
const ANSWER_STATUS = ['ok', 'not_found', 'unable'];
const METRICS = ['views', 'likes', 'reposts', 'quotes', 'replies', 'bookmarks'];

const MAX_POSTS = 400;
const MAX_OBSERVATIONS = 1500;
const ID_TIME_TOLERANCE_MS = 2000;
const RUN_SLACK_MS = 5 * 60 * 1000;

// X ids are snowflakes: the top bits are milliseconds since this epoch. A real id therefore
// carries its own creation time, and an invented one almost never matches its claimed date.
const X_EPOCH_MS = 1288834974657n;
const EM_DASH = String.fromCharCode(0x2014);

export function snowflakeTime(id) {
  return Number((BigInt(id) >> 22n) + X_EPOCH_MS);
}

export function snowflakeFor(ms, seq = 0) {
  return (((BigInt(ms) - X_EPOCH_MS) << 22n) | BigInt(seq)).toString();
}

const isObj = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);
const isStr = (v) => typeof v === 'string';
const isId = (v) => isStr(v) && /^\d{15,20}$/.test(v);
const isCount = (v) => Number.isInteger(v) && v >= 0;
const UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,3})?Z$/;

function utc(v) {
  if (!isStr(v) || !UTC.test(v)) return NaN;
  return Date.parse(v);
}

// 2026-10-09T06:00:00Z -> 2026-10-09T0600Z
export function runIdFor(ms) {
  const iso = new Date(ms).toISOString();
  return `${iso.slice(0, 10)}T${iso.slice(11, 13)}${iso.slice(14, 16)}Z`;
}

function httpsUrl(v) {
  if (!isStr(v)) return false;
  try {
    const u = new URL(v);
    return u.protocol === 'https:' && !u.username && !u.password;
  } catch { return false; }
}

export function checkCapture(doc, opts = {}) {
  const errors = [];
  const warnings = [];
  const err = (path, msg) => errors.push(`${path}: ${msg}`);
  const warn = (path, msg) => warnings.push(`${path}: ${msg}`);
  const known = opts.known ?? new Set();
  const now = (opts.now ?? new Date()).getTime();

  // Strings the grabber writes itself. Verbatim fields (post text, names, notes from X) are never policed.
  const own = (path, v, { required = false } = {}) => {
    if (v == null) { if (required) err(path, 'is required'); return; }
    if (!isStr(v) || v.trim() === '') { err(path, 'must be a non-empty string or null'); return; }
    if (v.includes(EM_DASH)) err(path, 'contains an em dash; use a comma, colon or period');
  };
  const oneOf = (path, v, list, { nullable = false } = {}) => {
    if (v == null && nullable) return;
    if (!list.includes(v)) err(path, `must be one of ${list.join(', ')}${nullable ? ' or null' : ''}`);
  };
  const arr = (path, v) => {
    if (!Array.isArray(v)) { err(path, 'must be an array'); return []; }
    return v;
  };

  if (!isObj(doc)) return { errors: ['capture: must be a JSON object'], warnings };
  if (doc.schema !== SCHEMA) err('schema', `must be exactly "${SCHEMA}"`);

  // ---- run
  const run = isObj(doc.run) ? doc.run : (err('run', 'is required'), {});
  if (!isStr(run.id) || !/^\d{4}-\d{2}-\d{2}T\d{4}Z$/.test(run.id)) err('run.id', 'must look like 2026-10-09T0600Z (UTC start, to the minute)');
  const started = utc(run.started_at);
  const finished = utc(run.finished_at);
  if (isNaN(started)) err('run.started_at', 'must be a UTC time like 2026-10-09T06:00:00Z');
  if (isNaN(finished)) err('run.finished_at', 'must be a UTC time like 2026-10-09T06:04:30Z');
  if (finished < started) err('run.finished_at', 'is before it started');
  if (finished > now + RUN_SLACK_MS) err('run.finished_at', 'is in the future');
  if (isStr(run.id) && !isNaN(started) && runIdFor(started) !== run.id) {
    err('run.id', `does not match run.started_at (expected ${runIdFor(started)})`);
  }
  oneOf('run.status', run.status, RUN_STATUS);
  if (run.status !== 'ok') own('run.reason', run.reason, { required: true }); else own('run.reason', run.reason);
  const g = isObj(run.grabber) ? run.grabber : (err('run.grabber', 'is required'), {});
  own('run.grabber.agent', g.agent, { required: true });
  own('run.grabber.model', g.model);
  own('run.grabber.method', g.method, { required: true });
  if (run.requests_rev != null && !isStr(run.requests_rev)) err('run.requests_rev', 'must be a string or null');

  if (opts.filePath && isStr(run.id)) {
    // capture/2026/10/09/0600Z.json  <->  2026-10-09T0600Z
    const parts = resolve(opts.filePath).split(sep);
    const fromPath = `${parts.at(-4)}-${parts.at(-3)}-${parts.at(-2)}T${basename(opts.filePath, '.json')}`;
    if (fromPath !== run.id) err('run.id', `does not match its file path (file says ${fromPath})`);
  }

  // ---- posts
  const posts = arr('posts', doc.posts);
  const here = new Map();
  if (posts.length > MAX_POSTS) err('posts', `holds ${posts.length} records; the cap is ${MAX_POSTS}`);
  posts.forEach((p, i) => {
    const at = `posts[${i}]`;
    if (!isObj(p)) { err(at, 'must be an object'); return; }
    if (!isId(p.id)) { err(`${at}.id`, 'must be a string of digits (a JSON number has already lost digits)'); return; }
    if (here.has(p.id)) err(`${at}.id`, `duplicate of an earlier record for ${p.id}`);
    here.set(p.id, p);

    const created = utc(p.created_at);
    const idTime = snowflakeTime(p.id);
    if (isNaN(created)) err(`${at}.created_at`, 'must be a UTC time like 2026-10-09T05:00:00Z');
    else if (Math.abs(created - idTime) > ID_TIME_TOLERANCE_MS) {
      err(`${at}.created_at`, `disagrees with the time inside the id (${new Date(idTime).toISOString()}); report what X returned, never a guess`);
    }
    if (idTime > now + RUN_SLACK_MS) err(`${at}.id`, 'encodes a time in the future');

    const a = isObj(p.author) ? p.author : (err(`${at}.author`, 'is required'), {});
    if (!isStr(a.handle) || !/^[A-Za-z0-9_]{1,15}$/.test(a.handle)) err(`${at}.author.handle`, 'must be the handle without @');
    if (!isStr(a.name)) err(`${at}.author.name`, 'must be a string (the display name as shown)');
    if (a.followers != null && !isCount(a.followers)) err(`${at}.author.followers`, 'must be a whole number or null');
    oneOf(`${at}.author.verified`, a.verified, VERIFIED, { nullable: true });
    oneOf(`${at}.author.kind`, a.kind, AUTHOR_KINDS);

    const m = isStr(p.url) && /^https:\/\/x\.com\/([A-Za-z0-9_]{1,15})\/status\/(\d+)$/.exec(p.url);
    if (!m) err(`${at}.url`, 'must be https://x.com/<handle>/status/<id>');
    else if (m[2] !== p.id || (isStr(a.handle) && m[1].toLowerCase() !== a.handle.toLowerCase())) {
      err(`${at}.url`, 'must carry the same id and handle as the record');
    }

    if (!isStr(p.text)) err(`${at}.text`, 'must be a string: the post exactly as written, or "" for a post with no text');
    if (p.lang != null && !isStr(p.lang)) err(`${at}.lang`, 'must be a language code or null');

    arr(`${at}.media`, p.media).forEach((md, j) => {
      const mp = `${at}.media[${j}]`;
      if (!isObj(md)) { err(mp, 'must be an object'); return; }
      oneOf(`${mp}.type`, md.type, MEDIA_TYPES);
      own(`${mp}.description`, md.description);
      if (md.alt != null && !isStr(md.alt)) err(`${mp}.alt`, 'must be a string or null');
      if (md.duration_s != null && !(typeof md.duration_s === 'number' && md.duration_s >= 0)) err(`${mp}.duration_s`, 'must be seconds or null');
      if (md.link_url != null && !httpsUrl(md.link_url)) err(`${mp}.link_url`, 'must be an https url or null');
      if (md.link_title != null && !isStr(md.link_title)) err(`${mp}.link_title`, 'must be a string or null');
    });
    if (isStr(p.text) && p.text === '' && Array.isArray(p.media) && p.media.length === 0) warn(at, 'has no text and no media');

    for (const rel of ['reply_to', 'quotes']) {
      if (p[rel] != null && !isId(p[rel])) err(`${at}.${rel}`, 'must be a post id string or null');
    }
    if (p.note != null && !(isObj(p.note) && isStr(p.note.text))) err(`${at}.note`, 'must be { text } or null');
    arr(`${at}.flags`, p.flags).forEach((f) => oneOf(`${at}.flags`, f, FLAGS));
    if (p.desk != null && !DESKS.includes(p.desk)) err(`${at}.desk`, 'must be a desk id from contract/desks.json, or null');
    if (p.beat != null) {
      if (p.desk == null) err(`${at}.beat`, 'needs a desk; a beat is a part of one desk');
      else if (!(BEATS[p.desk] ?? []).includes(p.beat)) err(`${at}.beat`, `is not a beat of ${p.desk} in contract/desks.json; use one of its beats or null`);
    }
    own(`${at}.topic`, p.topic);
    own(`${at}.lead`, p.lead);
  });

  const exists = (id) => here.has(id) || known.has(id);
  const refs = (path, list) => arr(path, list).forEach((id) => {
    if (!isId(id)) err(path, 'holds something that is not a post id string');
    else if (!exists(id)) err(path, `points at unknown post ${id}; include its full record in posts`);
  });

  // ---- observations
  const observations = arr('observations', doc.observations);
  const observed = new Set();
  if (observations.length > MAX_OBSERVATIONS) err('observations', `holds ${observations.length} rows; the cap is ${MAX_OBSERVATIONS}`);
  observations.forEach((o, i) => {
    const at = `observations[${i}]`;
    if (!isObj(o)) { err(at, 'must be an object'); return; }
    if (!isId(o.id)) { err(`${at}.id`, 'must be a post id string'); return; }
    if (!exists(o.id)) err(at, `points at unknown post ${o.id}; include its full record in posts`);
    observed.add(o.id);
    oneOf(`${at}.state`, o.state, STATES);
    const t = utc(o.at);
    if (isNaN(t)) err(`${at}.at`, 'must be a UTC time');
    else {
      if (t < snowflakeTime(o.id)) err(`${at}.at`, 'is before the post existed');
      if (!isNaN(started) && !isNaN(finished) && (t < started - RUN_SLACK_MS || t > finished + RUN_SLACK_MS)) {
        err(`${at}.at`, 'is outside the run; an observation is what you read during this run');
      }
    }
    let any = false;
    for (const k of METRICS) {
      if (o[k] == null) continue;
      if (!isCount(o[k])) err(`${at}.${k}`, 'must be a whole number or null (write 1200000, not "1.2M")');
      else any = true;
    }
    if (o.state === 'live' && !any) err(at, 'has no metrics; drop the row or report the state that explains it');
    if (typeof o.approx !== 'boolean') err(`${at}.approx`, 'must be true (read from an abbreviated display such as 1.2M) or false (exact)');
    if (isCount(o.views) && isCount(o.likes) && o.views < o.likes) warn(at, 'has fewer views than likes');
  });
  posts.forEach((p, i) => {
    if (isObj(p) && isId(p.id) && !observed.has(p.id)) err(`posts[${i}]`, `has no observation in this capture (${p.id})`);
  });

  // ---- sweeps, trends, context, answers
  arr('sweeps', doc.sweeps).forEach((s, i) => {
    const at = `sweeps[${i}]`;
    if (!isObj(s)) { err(at, 'must be an object'); return; }
    own(`${at}.id`, s.id, { required: true });
    oneOf(`${at}.kind`, s.kind, SWEEP_KINDS);
    if (s.desk != null && !DESKS.includes(s.desk)) err(`${at}.desk`, 'must be a desk id from contract/desks.json, or null');
    own(`${at}.method`, s.method, { required: true });
    if (s.window_hours != null && !(typeof s.window_hours === 'number' && s.window_hours > 0)) err(`${at}.window_hours`, 'must be a positive number or null');
    oneOf(`${at}.status`, s.status, SWEEP_STATUS);
    if (s.status !== 'ok') own(`${at}.reason`, s.reason, { required: true }); else own(`${at}.reason`, s.reason);
    refs(`${at}.post_ids`, s.post_ids);
  });

  arr('trends', doc.trends).forEach((t, i) => {
    const at = `trends[${i}]`;
    if (!isObj(t)) { err(at, 'must be an object'); return; }
    if (!isStr(t.region) || t.region === '') err(`${at}.region`, 'must be a region such as US or WW');
    if (!(Number.isInteger(t.rank) && t.rank >= 1)) err(`${at}.rank`, 'must be a whole number from 1');
    if (!isStr(t.name) || t.name === '') err(`${at}.name`, 'must be the trend exactly as X shows it');
    if (t.post_count != null && !isCount(t.post_count)) err(`${at}.post_count`, 'must be a whole number or null');
    if (t.story != null) {
      const st = t.story;
      const text = (v) => v == null || isStr(v);
      if (!isObj(st) || !httpsUrl(st.url) || !text(st.title) || !text(st.text)) {
        err(`${at}.story`, 'must be { url, title, text } with an https url and string or null title and text, or null');
      }
    }
    refs(`${at}.post_ids`, t.post_ids);
  });

  arr('context', doc.context).forEach((c, i) => {
    const at = `context[${i}]`;
    if (!isObj(c)) { err(at, 'must be an object'); return; }
    if (!isId(c.post_id) || !exists(c.post_id)) err(`${at}.post_id`, 'points at unknown post; include its full record in posts');
    refs(`${at}.replies`, c.replies);
    refs(`${at}.quotes`, c.quotes);
  });

  arr('answers', doc.answers).forEach((a, i) => {
    const at = `answers[${i}]`;
    if (!isObj(a)) { err(at, 'must be an object'); return; }
    own(`${at}.request_id`, a.request_id, { required: true });
    oneOf(`${at}.status`, a.status, ANSWER_STATUS);
    refs(`${at}.post_ids`, a.post_ids);
    if (a.status === 'not_found' && Array.isArray(a.post_ids) && a.post_ids.length) err(at, 'is not_found but lists posts');
    own(`${at}.note`, a.note);
  });

  if (run.status === 'ok' && posts.length === 0) err('run.status', 'is ok but the capture has no posts; use partial or down and say why');

  return { errors, warnings };
}

// Post ids recorded by every capture that sorts before `filePath`, so a later run may
// send observations for a post without repeating its full record.
export function knownIdsBefore(filePath) {
  const target = resolve(filePath);
  let root = dirname(target);
  for (let i = 0; i < 3; i++) root = dirname(root); // capture/YYYY/MM/DD/file -> capture
  const ids = new Set();
  const walk = (dir) => {
    for (const name of readdirSync(dir).sort()) {
      const p = join(dir, name);
      if (statSync(p).isDirectory()) walk(p);
      else if (/^\d{4}Z\.json$/.test(name) && p < target) {
        try {
          for (const post of JSON.parse(readFileSync(p, 'utf8')).posts ?? []) if (post && isId(post.id)) ids.add(post.id);
        } catch { /* an unreadable earlier file contributes nothing */ }
      }
    }
  };
  try { walk(root); } catch { /* first capture: nothing earlier */ }
  return ids;
}

function main(argv) {
  const files = argv.filter((a) => !a.startsWith('-'));
  if (!files.length) {
    console.error('usage: node tools/check-capture.mjs capture/YYYY/MM/DD/HHMMZ.json [more files]');
    return 2;
  }
  let failed = 0;
  for (const file of files) {
    let doc;
    try { doc = JSON.parse(readFileSync(file, 'utf8')); }
    catch (e) { console.log(`FAIL ${file}\n  not readable JSON: ${e.message}`); failed++; continue; }
    // Only a file at capture/YYYY/MM/DD/HHMMZ.json is held to its path; the example in contract/ is not.
    const placed = /(^|[\\/])capture[\\/]\d{4}[\\/]\d{2}[\\/]\d{2}[\\/]\d{4}Z\.json$/.test(resolve(file));
    if (!placed) console.log(`  note     ${file} is not at capture/YYYY/MM/DD/HHMMZ.json, so its path was not checked`);
    const { errors, warnings } = checkCapture(doc, placed ? { known: knownIdsBefore(file), filePath: file } : {});
    for (const w of warnings) console.log(`  warning  ${w}`);
    if (errors.length) {
      failed++;
      console.log(`FAIL ${file} (${errors.length} error${errors.length === 1 ? '' : 's'})`);
      for (const e of errors) console.log(`  ${e}`);
    } else {
      const n = (doc.posts ?? []).length, o = (doc.observations ?? []).length;
      console.log(`PASS ${file} (${doc.run?.status}, ${n} posts, ${o} observations)`);
    }
  }
  return failed ? 1 : 0;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exit(main(process.argv.slice(2)));
}
