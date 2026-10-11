// The capture contract, as tests. A capture is one sweep of X by the grabber.
// Every rule the grabber must meet is pinned here; contract/CAPTURE.md describes the same
// rules in prose, and contract/example.capture.json is checked below so it cannot rot.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { BEATS, DESKS, RETIRED, checkCapture, knownIdsBefore, runIdFor, snowflakeFor, snowflakeTime } from '../tools/check-capture.mjs';

const T0 = Date.parse('2026-10-09T05:00:00.000Z'); // post created
const RUN_START = '2026-10-09T06:00:00Z';
const RUN_END = '2026-10-09T06:04:30Z';
const NOW = new Date('2026-10-09T06:05:00Z');
const EM_DASH = String.fromCharCode(0x2014);

function post(over = {}) {
  const id = over.id ?? snowflakeFor(T0, 7);
  return {
    id,
    url: `https://x.com/example_handle/status/${id}`,
    created_at: '2026-10-09T05:00:00Z',
    lang: 'en',
    text: 'Example post text.',
    author: { handle: 'example_handle', name: 'Example Account', followers: 1200, verified: 'none', kind: 'person' },
    media: [],
    reply_to: null,
    quotes: null,
    note: null,
    flags: [],
    desk: 'internet',
    topic: 'example topic',
    lead: null,
    ...over,
  };
}

function obs(id, over = {}) {
  return {
    id, at: '2026-10-09T06:01:00Z', state: 'live',
    views: 1200000, likes: 41000, reposts: 6100, quotes: 900, replies: 2300, bookmarks: 5100,
    approx: false, ...over,
  };
}

function capture(over = {}) {
  const p = post();
  return {
    schema: 'mts.capture/1',
    run: {
      id: '2026-10-09T0600Z', started_at: RUN_START, finished_at: RUN_END,
      status: 'ok', reason: null,
      grabber: { agent: 'example', model: null, method: 'synthetic fixture' },
      requests_rev: null,
    },
    sweeps: [{ id: 'viral.global', kind: 'discovery', desk: null, method: 'top posts, last 6 hours', window_hours: 6, status: 'ok', reason: null, post_ids: [p.id] }],
    trends: [],
    posts: [p],
    observations: [obs(p.id)],
    context: [],
    answers: [],
    ...over,
  };
}

const errs = (doc, opts = {}) => checkCapture(doc, { now: NOW, ...opts }).errors;
const has = (list, re) => list.some((e) => re.test(e));

test('a well-formed capture passes with no errors', () => {
  assert.deepEqual(errs(capture()), []);
});

test('the example in contract/ passes, so the documented shape is the checked shape', () => {
  const doc = JSON.parse(readFileSync(new URL('../contract/example.capture.json', import.meta.url), 'utf8'));
  assert.deepEqual(checkCapture(doc, { now: new Date(Date.parse(doc.run.finished_at) + 60000) }).errors, []);
});

test('snowflake helpers round-trip a timestamp', () => {
  assert.equal(snowflakeTime(snowflakeFor(T0, 0)), T0);
  // A real post id, checked against X on 2026-10-09: created 2026-10-08T04:10:09Z.
  assert.equal(new Date(snowflakeTime('2108047268167274883')).toISOString().slice(0, 19), '2026-10-08T04:10:09');
});

test('the schema tag is required and exact', () => {
  assert.ok(has(errs(capture({ schema: 'mts.capture/2' })), /schema/));
});

test('a post id must be a string of digits: a JSON number has already lost digits', () => {
  const c = capture();
  c.posts[0].id = Number(c.posts[0].id);
  assert.ok(has(errs(c), /posts\[0\]\.id.*string/));
});

test('created_at must agree with the time inside the id, which is how an invented id is caught', () => {
  const c = capture();
  c.posts[0].created_at = '2026-10-09T05:07:00Z';
  assert.ok(has(errs(c), /created_at.*id/));
});

test('the url must be the canonical x.com status url for the same id and handle', () => {
  const a = capture(); a.posts[0].url = 'https://x.com/example_handle/status/123';
  assert.ok(has(errs(a), /url/));
  const b = capture(); b.posts[0].url = `https://x.com/someone_else/status/${b.posts[0].id}`;
  assert.ok(has(errs(b), /url/));
  const c = capture(); c.posts[0].url = `http://twitter.com/example_handle/status/${c.posts[0].id}`;
  assert.ok(has(errs(c), /url/));
});

test('every full post record carries at least one observation', () => {
  assert.ok(has(errs(capture({ observations: [] })), /no observation/));
});

test('an observation must point at a post in this capture or an earlier one', () => {
  const c = capture();
  const stranger = snowflakeFor(T0 - 3600000, 3);
  c.observations.push(obs(stranger));
  assert.ok(has(errs(c), /observations\[1\].*unknown post/));
  assert.deepEqual(errs(c, { known: new Set([stranger]) }), []);
});

test('metrics are whole numbers or null, never strings like 1.2M and never negative', () => {
  const a = capture(); a.observations[0].views = '1.2M';
  assert.ok(has(errs(a), /views/));
  const b = capture(); b.observations[0].likes = -1;
  assert.ok(has(errs(b), /likes/));
  const c = capture(); c.observations[0].reposts = 10.5;
  assert.ok(has(errs(c), /reposts/));
  const d = capture(); d.observations[0].views = null;
  assert.deepEqual(errs(d), []);
});

test('a live observation with every metric null says nothing and is rejected; a deleted one may be empty', () => {
  const blank = { views: null, likes: null, reposts: null, quotes: null, replies: null, bookmarks: null };
  const a = capture(); Object.assign(a.observations[0], blank);
  assert.ok(has(errs(a), /no metrics/));
  const b = capture(); Object.assign(b.observations[0], blank, { state: 'deleted' });
  assert.deepEqual(errs(b), []);
});

test('an observation cannot predate its post or fall outside the run', () => {
  const a = capture(); a.observations[0].at = '2026-10-09T04:00:00Z';
  assert.ok(has(errs(a), /before the post/));
  const b = capture(); b.observations[0].at = '2026-10-09T09:00:00Z';
  assert.ok(has(errs(b), /outside the run/));
});

test('a run cannot finish in the future or before it started', () => {
  const a = capture(); a.run.finished_at = '2026-10-09T08:00:00Z';
  assert.ok(has(errs(a), /future/));
  const b = capture(); b.run.finished_at = '2026-10-09T05:00:00Z';
  assert.ok(has(errs(b), /before it started/));
});

test('every id referenced anywhere must be a known post', () => {
  const ghost = snowflakeFor(T0 - 60000, 9);
  const a = capture(); a.sweeps[0].post_ids.push(ghost);
  assert.ok(has(errs(a), /sweeps\[0\].*unknown post/));
  const b = capture(); b.trends.push({ region: 'US', rank: 1, name: 'Example', post_count: null, story: null, post_ids: [ghost] });
  assert.ok(has(errs(b), /trends\[0\].*unknown post/));
  const c = capture(); c.context.push({ post_id: c.posts[0].id, replies: [ghost], quotes: [] });
  assert.ok(has(errs(c), /context\[0\].*unknown post/));
  const d = capture(); d.answers.push({ request_id: 'r1', status: 'ok', post_ids: [ghost], note: null });
  assert.ok(has(errs(d), /answers\[0\].*unknown post/));
});

test('an answer of not_found carries no posts', () => {
  const c = capture();
  c.answers.push({ request_id: 'r1', status: 'not_found', post_ids: [c.posts[0].id], note: null });
  assert.ok(has(errs(c), /not_found/));
});

test('enumerations are closed: desk, author kind, flags, media type, state', () => {
  const a = capture(); a.posts[0].desk = 'weather';
  assert.ok(has(errs(a), /desk/));
  const b = capture(); b.posts[0].author.kind = 'celebrity';
  assert.ok(has(errs(b), /author\.kind/));
  const c = capture(); c.posts[0].flags = ['spicy'];
  assert.ok(has(errs(c), /flags/));
  const d = capture(); d.posts[0].media = [{ type: 'hologram', description: null, alt: null, duration_s: null, link_url: null, link_title: null }];
  assert.ok(has(errs(d), /media\[0\]\.type/));
  const e = capture(); e.observations[0].state = 'gone';
  assert.ok(has(errs(e), /state/));
});

test('links are https only', () => {
  const c = capture();
  c.posts[0].media = [{ type: 'link', description: null, alt: null, duration_s: null, link_url: 'javascript:alert(1)', link_title: 'x' }];
  assert.ok(has(errs(c), /link_url/));
});

test('a sweep or run that did not succeed must say why, as data', () => {
  const a = capture(); a.sweeps[0].status = 'down';
  assert.ok(has(errs(a), /sweeps\[0\]\.reason/));
  const b = capture(); b.run.status = 'partial';
  assert.ok(has(errs(b), /run\.reason/));
});

test('a run that was down is a valid ledger entry with no posts at all', () => {
  const stub = {
    schema: 'mts.capture/1',
    run: { id: '2026-10-09T0600Z', started_at: RUN_START, finished_at: RUN_END, status: 'down', reason: 'X search returned errors on every call', grabber: { agent: 'example', model: null, method: 'synthetic fixture' }, requests_rev: null },
    sweeps: [], trends: [], posts: [], observations: [], context: [], answers: [],
  };
  assert.deepEqual(errs(stub), []);
});

test('an ok run with no posts is not ok', () => {
  assert.ok(has(errs(capture({ posts: [], observations: [], sweeps: [] })), /no posts/));
});

test('grabber-written strings carry no em dash; verbatim post text is never policed', () => {
  const a = capture(); a.posts[0].topic = `one thing ${EM_DASH} another`;
  assert.ok(has(errs(a), /topic.*dash/));
  const b = capture(); b.posts[0].text = `as posted ${EM_DASH} untouched`;
  assert.deepEqual(errs(b), []);
});

test('duplicate post records are rejected', () => {
  const c = capture(); c.posts.push(post());
  assert.ok(has(errs(c), /duplicate/));
});

test('the run id must match its file name when one is given', () => {
  assert.ok(has(errs(capture(), { fileName: '0700Z.json', filePath: 'capture/2026/10/09/0700Z.json' }), /file/));
  assert.deepEqual(errs(capture(), { filePath: 'capture/2026/10/09/0600Z.json' }), []);
});

test('implausible numbers are warnings, not errors: the grabber reports what it saw', () => {
  const c = capture(); c.observations[0].views = 10; // fewer views than likes
  const r = checkCapture(c, { now: NOW });
  assert.deepEqual(r.errors, []);
  assert.ok(has(r.warnings, /views/));
});

test('an X story must have an https url and text that is a string or null', () => {
  const p = capture().posts[0].id;
  const trend = (story) => capture({ trends: [{ region: 'US', rank: 1, name: 'Example', post_count: null, story, post_ids: [p] }] });
  assert.deepEqual(errs(trend({ url: 'https://x.com/i/trending/1', title: 'As X wrote it', text: null })), []);
  assert.ok(has(errs(trend({ url: 'http://x.com/i/trending/1', title: 't', text: 't' })), /story/));
  assert.ok(has(errs(trend({ url: 'https://x.com/i/trending/1', title: 7, text: 't' })), /story/));
});

test('a capture over the size caps is rejected', () => {
  const c = capture();
  for (let i = 0; i < 400; i++) {
    const p = post({ id: snowflakeFor(T0 + 1000, i + 100) });
    p.url = `https://x.com/example_handle/status/${p.id}`;
    p.created_at = '2026-10-09T05:00:01Z';
    c.posts.push(p);
    c.observations.push(obs(p.id));
  }
  assert.ok(has(errs(c), /posts: holds 401 records/));
});

test('a later run may send numbers for a post recorded by an earlier file, and only an earlier one', () => {
  const root = mkdtempSync(join(tmpdir(), 'mts-'));
  try {
    const day = join(root, 'capture', '2026', '10', '09');
    mkdirSync(day, { recursive: true });
    const first = capture();
    const id = first.posts[0].id;
    writeFileSync(join(day, '0600Z.json'), JSON.stringify(first));
    writeFileSync(join(day, '0600Z.note.json'), JSON.stringify({ posts: [{ id: '111111111111111111' }] }));
    const later = join(day, '0700Z.json');
    writeFileSync(later, '{}');
    assert.deepEqual([...knownIdsBefore(later)], [id]);
    assert.deepEqual([...knownIdsBefore(join(day, '0600Z.json'))], []);
    const yesterday = join(root, 'capture', '2026', '10', '08');
    mkdirSync(yesterday, { recursive: true });
    assert.deepEqual([...knownIdsBefore(join(yesterday, '2300Z.json'))], []);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

// ---- the desks: contract/desks.json is the one list, read by the checker, the grabber and the site

const desksDoc = JSON.parse(readFileSync(new URL('../contract/desks.json', import.meta.url), 'utf8'));
// Every desk the record has ever used: the ones watched now, then the retired ones.
const everyDesk = [...desksDoc.desks, ...desksDoc.retired];

test('the desk list is well formed: unique ids and codes, a known group, a scope, a cadence, a floor', () => {
  assert.equal(desksDoc.schema, 'mts.desks/1');
  const groups = new Set(desksDoc.groups.map((g) => g.id));
  assert.equal(groups.size, desksDoc.groups.length, 'group ids are unique');
  const ids = new Set(), codes = new Set();
  // A retired desk keeps its id and code for good, so neither can be handed to a new desk.
  for (const d of everyDesk) {
    assert.match(d.id, /^[a-z]+$/, `${d.id}: id is one lowercase word`);
    assert.match(d.code, /^[A-Z]{2,3}$/, `${d.id}: code is two or three capitals`);
    assert.ok(!ids.has(d.id), `${d.id}: duplicate id`); ids.add(d.id);
    assert.ok(!codes.has(d.code), `${d.id}: duplicate code ${d.code}`); codes.add(d.code);
    assert.ok(groups.has(d.group), `${d.id}: unknown group ${d.group}`);
    assert.ok(typeof d.name === 'string' && d.name.length > 0, `${d.id}: name`);
    assert.ok(typeof d.scope === 'string' && d.scope.length > 30, `${d.id}: scope says what belongs`);
    assert.ok([1, 2, 4].includes(d.sweep_every_hours), `${d.id}: sweep_every_hours is 1, 2 or 4`);
    assert.ok(Number.isInteger(d.floor.views) && d.floor.views > 0 && Number.isInteger(d.floor.likes) && d.floor.likes > 0, `${d.id}: floor`);
    assert.ok(Array.isArray(d.beats) && d.beats.length >= 2, `${d.id}: at least two beats`);
    assert.equal(new Set(d.beats).size, d.beats.length, `${d.id}: beats are unique`);
    for (const b of d.beats) assert.match(b, /^[a-z0-9]+(-[a-z0-9]+)*$/, `${d.id}: beat ${b} is lowercase words joined by hyphens`);
    for (const text of [d.name, d.scope, d.not_here ?? '']) assert.ok(!text.includes(EM_DASH), `${d.id}: no em dash`);
  }
  for (const g of desksDoc.groups) assert.ok(desksDoc.desks.some((d) => d.group === g.id), `group ${g.id} has a desk`);
  for (const d of desksDoc.desks) assert.equal(d.retired_at, undefined, `${d.id}: a watched desk has no retirement time`);
  for (const d of desksDoc.retired) {
    assert.match(d.retired_at, /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/, `${d.id}: retired_at is a UTC time`);
    assert.ok(typeof d.instead === 'string' && d.instead.length > 30 && !d.instead.includes(EM_DASH), `${d.id}: says where its subject goes now`);
  }
});

test('the checker reads its desks and beats from that file, not from a list of its own', () => {
  assert.deepEqual(DESKS, desksDoc.desks.map((d) => d.id));
  for (const d of everyDesk) assert.deepEqual(BEATS[d.id], d.beats);
  assert.deepEqual(RETIRED, Object.fromEntries(desksDoc.retired.map((d) => [d.id, d.retired_at])));
});

// ---- retiring a desk: its id stays good in the captures made while it was watched, and in nothing after

// The same capture, run at another time.
function runAt(doc, startMs) {
  const iso = (ms) => new Date(ms).toISOString().replace('.000Z', 'Z');
  Object.assign(doc.run, { id: runIdFor(startMs), started_at: iso(startMs), finished_at: iso(startMs + 270000) });
  for (const o of doc.observations) o.at = iso(startMs + 60000);
  return { doc, opts: { now: new Date(startMs + 300000) } };
}

test('crypto is retired: it is not a watched desk, and the record still knows what it was', () => {
  assert.ok(!DESKS.includes('crypto'), 'crypto is not swept, labelled or drawn');
  assert.ok(RETIRED.crypto, 'and it is listed as retired, with the time it stopped');
  assert.ok(BEATS.crypto.length >= 2, 'with the beats its old captures used');
});

test('a retired desk is accepted in a capture started before it was retired', () => {
  for (const d of desksDoc.retired) {
    const { doc, opts } = runAt(capture(), Date.parse(d.retired_at) - 3600000);
    Object.assign(doc.posts[0], { desk: d.id, beat: d.beats[0] });
    doc.sweeps.push({ id: `desk.${d.id}`, kind: 'desk', desk: d.id, method: 'standing query', window_hours: 24, status: 'ok', reason: null, post_ids: [] });
    doc.volume = [{ key: `desk.${d.id}`, desk: d.id, query: 'standing query', granularity: 'hour', points: [] }];
    assert.deepEqual(errs(doc, opts), [], `${d.id} an hour before it was retired`);
  }
});

test('a retired desk is refused on a post, a sweep and a volume series in any capture started after', () => {
  for (const d of desksDoc.retired) {
    for (const startMs of [Date.parse(d.retired_at), Date.parse(d.retired_at) + 3600000]) {
      const a = runAt(capture(), startMs); a.doc.posts[0].desk = d.id;
      assert.ok(has(errs(a.doc, a.opts), /posts\[0\]\.desk.*retired/), `${d.id} on a post`);
      const b = runAt(capture(), startMs); b.doc.sweeps[0].desk = d.id;
      assert.ok(has(errs(b.doc, b.opts), /sweeps\[0\]\.desk.*retired/), `${d.id} on a sweep`);
      const c = runAt(capture(), startMs); c.doc.volume = [{ key: `desk.${d.id}`, desk: d.id, query: 'standing query', granularity: 'hour', points: [] }];
      assert.ok(has(errs(c.doc, c.opts), /volume\[0\]\.desk.*retired/), `${d.id} on a volume series`);
      // the control: the same capture at the same hour passes once the retired desk is taken off it
      const ok = runAt(capture(), startMs);
      assert.deepEqual(errs(ok.doc, ok.opts), [], 'and the capture is otherwise sound');
    }
  }
});

test('a desk that never existed is still refused whenever the capture was made', () => {
  const a = capture(); a.posts[0].desk = 'finance';
  assert.ok(has(errs(a), /posts\[0\]\.desk.*contract\/desks\.json/));
  assert.ok(!has(errs(a), /retired/), 'and is not mistaken for a retired one');
  // A name every object already has is not a desk, and must be refused like any other, not crash the checker.
  for (const name of ['constructor', 'toString', '__proto__']) {
    const b = capture(); Object.assign(b.posts[0], { desk: name, beat: 'policy' }); b.sweeps[0].desk = name;
    const list = errs(b);
    assert.ok(has(list, /posts\[0\]\.desk.*contract\/desks\.json/) && has(list, /sweeps\[0\]\.desk.*contract\/desks\.json/), `${name} is refused as a desk`);
    assert.ok(has(list, /posts\[0\]\.beat/), `and ${name} has no beats`);
  }
});

test('the six sectors of the old page each still have a home', () => {
  // Finance/markets, Politics, Pop culture, Sports, Tech & AI, Medicine
  for (const id of ['markets', 'politics', 'entertainment', 'sports', 'tech', 'ai', 'medicine']) assert.ok(DESKS.includes(id), id);
});

test('a beat is optional, and when given it must belong to the post\'s desk', () => {
  const desk = desksDoc.desks[0], other = desksDoc.desks.find((d) => !d.beats.includes(desk.beats[0]));
  const a = capture(); Object.assign(a.posts[0], { desk: desk.id, beat: desk.beats[0] });
  assert.deepEqual(errs(a), []);
  const b = capture(); Object.assign(b.posts[0], { desk: desk.id, beat: null });
  assert.deepEqual(errs(b), []);
  const c = capture(); Object.assign(c.posts[0], { desk: other.id, beat: desk.beats[0] });
  assert.ok(has(errs(c), /beat/));
  const d = capture(); Object.assign(d.posts[0], { desk: null, beat: desk.beats[0] });
  assert.ok(has(errs(d), /beat/));
  const e = capture(); Object.assign(e.posts[0], { desk: desk.id, beat: 'made-up-beat' });
  assert.ok(has(errs(e), /beat/));
});

test('a sweep names a desk from the same list', () => {
  const a = capture(); a.sweeps[0].desk = 'finance'; // a sector name from the old page, not a desk
  assert.ok(has(errs(a), /sweeps\[0\]\.desk/));
  const b = capture(); b.sweeps[0].desk = desksDoc.desks.at(-1).id;
  assert.deepEqual(errs(b), []);
});

test('the desk map in GRABBER.md names every desk in the file once, under its own group, and nothing else', () => {
  const doc = readFileSync(new URL('../contract/GRABBER.md', import.meta.url), 'utf8');
  const table = doc.slice(doc.indexOf('| Group | Desks |'), doc.indexOf('(The table is a map for reading.'));
  const rows = table.split('\n').filter((l) => l.startsWith('| ') && !l.startsWith('| Group') && !l.startsWith('|---'));
  const seen = [];
  for (const row of rows) {
    const [, groupName, cells] = row.split('|').map((c) => c.trim());
    const group = desksDoc.groups.find((g) => g.name === groupName);
    assert.ok(group, `GRABBER.md names a group that is not in the file: ${groupName}`);
    for (const id of [...cells.matchAll(/`([a-z]+)`/g)].map((m) => m[1])) {
      const desk = desksDoc.desks.find((d) => d.id === id);
      assert.ok(desk, `GRABBER.md names a desk that is not in the file: ${id}`);
      assert.equal(desk.group, group.id, `${id} is listed under the wrong group`);
      seen.push(id);
    }
  }
  assert.deepEqual(seen, desksDoc.desks.map((d) => d.id));
});

test('ARCHITECTURE.md mentions every desk', () => {
  const doc = readFileSync(new URL('../ARCHITECTURE.md', import.meta.url), 'utf8');
  const section = doc.slice(doc.indexOf('## The desks'), doc.indexOf('## The checks on the grabber'));
  for (const d of desksDoc.desks) assert.match(section, new RegExp(`\\b${d.id}\\b`), `${d.id} is missing from ARCHITECTURE.md`);
});

// ---- additions after the first real capture: all optional, so earlier captures stay valid

test('a capture without the newer arrays is still valid', () => {
  const c = capture();
  assert.equal(c.x_stories, undefined);
  assert.equal(c.volume, undefined);
  assert.deepEqual(errs(c), []);
});

test('media_source names the post a clip or image was first attached to', () => {
  const a = capture(); a.posts[0].media_source = snowflakeFor(T0 - 7200000, 5);
  assert.deepEqual(errs(a), []);
  const b = capture(); b.posts[0].media_source = 12345;
  assert.ok(has(errs(b), /media_source/));
});

test('x_stories carry X\'s own story for a cluster, with posts that have records', () => {
  const c = capture();
  const story = { id: '2107164174623097194', url: 'https://x.com/i/trending/2107164174623097194', name: 'As X wrote it', summary: null, category: null, updated_at: '2026-10-09T05:30:00Z', post_ids: [c.posts[0].id] };
  c.x_stories = [story];
  assert.deepEqual(errs(c), []);
  c.x_stories = [{ ...story, url: 'http://x.com/i/trending/1' }];
  assert.ok(has(errs(c), /x_stories\[0\]\.url/));
  c.x_stories = [{ ...story, post_ids: [snowflakeFor(T0 - 1000, 77)] }];
  assert.ok(has(errs(c), /x_stories\[0\].*unknown post/));
  c.x_stories = [{ ...story, name: '' }];
  assert.ok(has(errs(c), /x_stories\[0\]\.name/));
});

test('volume is posts per hour for a query: whole counts, hours in order, the query written down', () => {
  const series = (over = {}) => ({ key: 'desk.sports', desk: 'sports', query: '(NFL OR NBA) lang:en -is:retweet', granularity: 'hour', points: [{ start: '2026-10-09T03:00:00Z', count: 41200 }, { start: '2026-10-09T04:00:00Z', count: 38900 }], ...over });
  const a = capture(); a.volume = [series()];
  assert.deepEqual(errs(a), []);
  const b = capture(); b.volume = [series({ points: [{ start: '2026-10-09T04:00:00Z', count: 1 }, { start: '2026-10-09T03:00:00Z', count: 2 }] })];
  assert.ok(has(errs(b), /volume\[0\].*order/));
  const c = capture(); c.volume = [series({ points: [{ start: '2026-10-09T03:00:00Z', count: '41K' }] })];
  assert.ok(has(errs(c), /count/));
  const d = capture(); d.volume = [series({ desk: 'finance' })];
  assert.ok(has(errs(d), /volume\[0\]\.desk/));
  const e = capture(); e.volume = [series({ query: '' })];
  assert.ok(has(errs(e), /volume\[0\]\.query/));
  const f = capture(); f.volume = [series(), series()];
  assert.ok(has(errs(f), /duplicate/));
});

test('a volume sweep is a kind of sweep', () => {
  const c = capture();
  c.sweeps.push({ id: 'volume.sports', kind: 'volume', desk: 'sports', method: 'counts for the desk query, hourly', window_hours: 24, status: 'ok', reason: null, post_ids: [] });
  assert.deepEqual(errs(c), []);
});
