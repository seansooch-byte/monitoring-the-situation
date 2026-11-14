// Gate 1, the capture contract, as a pure function: no file, no path, no clock of its own, so
// it runs the same in the command line (tools/check-capture.mjs), in the tests and inside the
// Worker's ingest route. The desks come in as opts.desks (the contract/desks.json document),
// the ids recorded by earlier captures as opts.known, the clock as opts.now.
// contract/CAPTURE.md describes the rules in prose and tests/check-capture.test.mjs pins them.
export const SCHEMA = 'mts.capture/1';
const RUN_STATUS = ['ok', 'partial', 'down'];
const SWEEP_STATUS = ['ok', 'partial', 'down', 'skipped'];
const SWEEP_KINDS = ['discovery', 'desk', 'trends', 'watch', 'context', 'request', 'volume'];
const AUTHOR_KINDS = ['person', 'creator', 'news', 'org', 'brand', 'official', 'parody', 'aggregator', 'unknown'];
const VERIFIED = ['blue', 'business', 'government', 'none'];
const MEDIA_TYPES = ['photo', 'video', 'gif', 'link', 'poll'];
const FLAGS = ['nsfw', 'graphic', 'private_individual', 'minor', 'ad', 'engagement_bait', 'ai_media_suspected', 'old_content', 'non_english'];
const STATES = ['live', 'deleted', 'unavailable'];
const ANSWER_STATUS = ['ok', 'not_found', 'unable'];
const METRICS = ['views', 'likes', 'reposts', 'quotes', 'replies', 'bookmarks'];

const MAX_POSTS = 400;
const MAX_OBSERVATIONS = 1500;
const MAX_VOLUME_SERIES = 60;
const MAX_VOLUME_POINTS = 200;
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
export const isId = (v) => isStr(v) && /^\d{15,20}$/.test(v);
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

// The post ids a capture points at outside its own posts: the only ids the check needs opts.known to
// answer for. The store looks up these and nothing else (DECISIONS 2026-11-14, the D1 read limit).
export function idsToLookUp(doc) {
  const own = new Set((Array.isArray(doc?.posts) ? doc.posts : []).map((p) => p?.id));
  const out = new Set();
  const walk = (v) => {
    if (isId(v)) { if (!own.has(v)) out.add(v); return; }
    if (Array.isArray(v)) v.forEach(walk);
    else if (v && typeof v === 'object') for (const [k, x] of Object.entries(v)) if (k !== 'run') walk(x);
  };
  for (const [k, v] of Object.entries(doc ?? {})) if (k !== 'posts' && k !== 'run') walk(v);
  return [...out];
}

export function checkCapture(doc, opts = {}) {
  const errors = [];
  const warnings = [];
  const err = (path, msg) => errors.push(`${path}: ${msg}`);
  const warn = (path, msg) => warnings.push(`${path}: ${msg}`);
  const known = opts.known ?? new Set();
  const now = (opts.now ?? new Date()).getTime();
  // The desks and their beats are data: the contract/desks.json document comes in as opts.desks.
  // The desks watched now. A retired desk is not one of them, but the captures made while it was
  // watched still carry its id and its beats, so the record keeps both and the time it stopped.
  const DESK_FILE = opts.desks;
  if (!Array.isArray(DESK_FILE?.desks)) throw new Error('checkCapture needs opts.desks: the contract/desks.json document');
  const DESKS = DESK_FILE.desks.map((d) => d.id);
  const RETIRED = Object.fromEntries((DESK_FILE.retired ?? []).map((d) => [d.id, d.retired_at]));
  const BEATS = Object.fromEntries([...DESK_FILE.desks, ...(DESK_FILE.retired ?? [])].map((d) => [d.id, d.beats]));

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
  // A desk id is good while its desk is watched. A retired desk's id stays good in a capture
  // started before it was retired, and in nothing started after.
  const desk = (path, v) => {
    if (v == null || DESKS.includes(v)) return;
    if (!Object.hasOwn(RETIRED, v)) err(path, 'must be a desk id from contract/desks.json, or null');
    else if (!(utc(doc.run?.started_at) < Date.parse(RETIRED[v]))) err(path, `is ${v}, a desk retired on ${RETIRED[v].slice(0, 10)}: it is no longer swept, labelled or counted; use a desk watched now, or null`);
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
  // The budget is a number in the record, not a sentence: reads this run spent, reads left in the UTC day after it.
  for (const k of ['reads', 'reads_left']) {
    if (run[k] == null) warn(`run.${k}`, 'is missing: record the reads this run spent and the reads left in the day as whole numbers (contract/CAPTURE.md, run)');
    else if (!Number.isInteger(run[k]) || run[k] < 0) err(`run.${k}`, 'must be a whole number of reads');
  }
  if (run.plan != null && !isStr(run.plan)) err('run.plan', 'must be a string or null: the for_run of the requests/plan.json this run executed');

  if (opts.filePath && isStr(run.id)) {
    // capture/2026/10/09/0600Z.json  <->  2026-10-09T0600Z
    const parts = String(opts.filePath).replace(/\\/g, '/').split('/');
    const fromPath = `${parts.at(-4)}-${parts.at(-3)}-${parts.at(-2)}T${parts.at(-1).replace(/\.json$/, '')}`;
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

    for (const rel of ['reply_to', 'quotes', 'media_source']) {
      if (p[rel] != null && !isId(p[rel])) err(`${at}.${rel}`, 'must be a post id string or null');
    }
    if (p.note != null && !(isObj(p.note) && isStr(p.note.text))) err(`${at}.note`, 'must be { text } or null');
    arr(`${at}.flags`, p.flags).forEach((f) => oneOf(`${at}.flags`, f, FLAGS));
    desk(`${at}.desk`, p.desk);
    if (p.beat != null) {
      if (p.desk == null) err(`${at}.beat`, 'needs a desk; a beat is a part of one desk');
      else if (!(Object.hasOwn(BEATS, p.desk) ? BEATS[p.desk] : []).includes(p.beat)) err(`${at}.beat`, `is not a beat of ${p.desk} in contract/desks.json; use one of its beats or null`);
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
    desk(`${at}.desk`, s.desk);
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

  // ---- optional arrays, added after the first real capture. A capture without them is valid.
  if (doc.x_stories != null) arr('x_stories', doc.x_stories).forEach((x, i) => {
    const at = `x_stories[${i}]`;
    if (!isObj(x)) { err(at, 'must be an object'); return; }
    if (!isStr(x.id) || x.id === '') err(`${at}.id`, 'must be the story id as a string');
    if (!httpsUrl(x.url)) err(`${at}.url`, 'must be the https url of the story on X');
    if (!isStr(x.name) || x.name === '') err(`${at}.name`, 'must be the story name exactly as X wrote it');
    for (const k of ['summary', 'category']) if (x[k] != null && !isStr(x[k])) err(`${at}.${k}`, 'must be a string or null');
    if (x.updated_at != null && isNaN(utc(x.updated_at))) err(`${at}.updated_at`, 'must be a UTC time or null');
    refs(`${at}.post_ids`, x.post_ids);
  });

  if (doc.volume != null) {
    const keys = new Set();
    const list = arr('volume', doc.volume);
    if (list.length > MAX_VOLUME_SERIES) err('volume', `holds ${list.length} series; the cap is ${MAX_VOLUME_SERIES}`);
    list.forEach((v, i) => {
      const at = `volume[${i}]`;
      if (!isObj(v)) { err(at, 'must be an object'); return; }
      own(`${at}.key`, v.key, { required: true });
      if (isStr(v.key)) { if (keys.has(v.key)) err(`${at}.key`, `duplicate of an earlier series for ${v.key}`); keys.add(v.key); }
      desk(`${at}.desk`, v.desk);
      if (!isStr(v.query) || v.query.trim() === '') err(`${at}.query`, 'must be the exact query the counts are for');
      oneOf(`${at}.granularity`, v.granularity, ['hour']);
      const pts = arr(`${at}.points`, v.points);
      if (pts.length > MAX_VOLUME_POINTS) err(`${at}.points`, `holds ${pts.length} points; the cap is ${MAX_VOLUME_POINTS}`);
      let prev = -Infinity;
      pts.forEach((pt, j) => {
        const t = isObj(pt) ? utc(pt.start) : NaN;
        if (isNaN(t)) err(`${at}.points[${j}].start`, 'must be the UTC start of the hour');
        else { if (t <= prev) err(`${at}.points[${j}]`, 'is out of order; hours go oldest first with no repeats'); prev = t; }
        if (!isObj(pt) || !isCount(pt.count)) err(`${at}.points[${j}].count`, 'must be a whole number');
      });
    });
  }

  if (run.status === 'ok' && posts.length === 0) err('run.status', 'is ok but the capture has no posts; use partial or down and say why');

  return { errors, warnings };
}
