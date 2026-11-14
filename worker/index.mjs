// The Worker: the site's static files, and the store.
//
// The store is the record in a place where a deletion can be honoured (PROGRAM.md, phase 1):
//   POST /ingest                 a capture from the grabber; Gate 1 runs here; rows go to D1,
//                                the file itself is kept gzipped beside them
//   GET  /api/runs               the runs, newest first (?from=&to=&limit=)
//   GET  /api/capture/<run id>   the capture as delivered, after any purge
//   GET  /api/posts?ids=         records, in the capture's shape
//   GET  /api/observations       ?ids= or ?since= (and ?until=): the numbers
//   GET  /api/volume?desk=       X's hourly counts (?since=)
//   GET  /api/checks?ids=        what X said about each post
//   POST /api/verify {ids}       ask X now (Gate 2) and record the answers
//   GET  /api/status             counts and the last sweep
//   POST /api/board              a message on the agents' board (contract/BOARD.md)
//   GET  /api/board?as=&since=   the thread after `since` (default: that agent's cursor)
//   POST /api/board/seen {as,id} move an agent's cursor
//   GET  /api/state              what every agent reads first: who was seen, latest reports, what waits on whom
// Every route above needs `Authorization: Bearer <STORE_TOKEN>` until phase 2 opens the reads.
// Everything else is served from the built site.
//
// The deletion sweep runs on the hour (triggers.crons): posts X stopped returning are checked
// first, then the posts checked longest ago; a 404 purges the post's words, name, media and link
// from its row and from every capture file that holds it, and keeps its id and its numbers.
import desks from '../contract/desks.json';
import { checkCapture } from '../tools/lib/capture-check.mjs';
import { askX, compareToX, WITHHELD } from '../tools/lib/gate2.mjs';
import { rowsOf, recordOf, stripCapture } from '../tools/lib/store-rows.mjs';
import { BOARD, checkMessage, stateOf } from '../tools/lib/board.mjs';

const SWEEP_CHECKS = 150;      // oEmbed asks per hourly sweep
const SWEEP_PURGES = 5;        // capture files rewritten per sweep; the rest wait an hour
const RECHECK_HOURS = 24;      // a post is asked about again this long after its last check
const ROWS_PER_STATEMENT = 400;

const stamp = () => new Date().toISOString().replace(/\.\d{3}Z$/, 'Z');
const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
const authed = (request, env) => Boolean(env.STORE_TOKEN) && request.headers.get('authorization') === `Bearer ${env.STORE_TOKEN}`;

async function gzip(text) {
  const cs = new CompressionStream('gzip');
  const w = cs.writable.getWriter();
  w.write(new TextEncoder().encode(text));
  w.close();
  return new Uint8Array(await new Response(cs.readable).arrayBuffer());
}
async function gunzip(bytes) {
  const ds = new DecompressionStream('gzip');
  const w = ds.writable.getWriter();
  w.write(bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes));
  w.close();
  return new Response(ds.readable).text();
}

// One INSERT per table from a JSON array, in slices, so a capture of any size is a short batch.
function inserts(db, table, cols, rows, mode = 'INSERT OR IGNORE', onConflict = '') {
  const picks = cols.map((c) => `json_extract(value, '$.${c}')`).join(', ');
  const out = [];
  for (let i = 0; i < rows.length; i += ROWS_PER_STATEMENT) {
    // "WHERE true" is SQLite's documented way to keep an INSERT ... SELECT from reading the upsert clause's ON as a join.
    out.push(db.prepare(`${mode} INTO ${table} (${cols.join(', ')}) SELECT ${picks} FROM json_each(?1) WHERE true ${onConflict}`).bind(JSON.stringify(rows.slice(i, i + ROWS_PER_STATEMENT))));
  }
  return out;
}

const RUN_COLS = ['id', 'source', 'started_at', 'finished_at', 'status', 'reason', 'agent', 'model', 'method', 'requests_rev', 'reads', 'reads_left', 'plan', 'received_at', 'posts', 'observations'];
const POST_COLS = ['id', 'source', 'url', 'created_at', 'lang', 'text', 'author_handle', 'author_name', 'author_followers', 'author_verified', 'author_kind', 'media', 'reply_to', 'quotes', 'media_source', 'note', 'flags', 'desk', 'beat', 'topic', 'lead', 'first_run', 'last_run'];
const OBS_COLS = ['post_id', 'at', 'run_id', 'state', 'views', 'likes', 'reposts', 'quotes', 'replies', 'bookmarks', 'approx'];
const SWEEP_COLS = ['run_id', 'sweep_id', 'kind', 'desk', 'method', 'window_hours', 'status', 'reason', 'post_ids'];
const VOL_COLS = ['key', 'desk', 'query', 'start', 'count', 'run_id'];
const TREND_COLS = ['run_id', 'region', 'rank', 'name', 'post_count', 'story', 'post_ids'];
const CONTEXT_COLS = ['run_id', 'post_id', 'replies', 'quotes'];
const ANSWER_COLS = ['run_id', 'request_id', 'status', 'post_ids', 'note'];
// A record delivered again (the text was edited, a note appeared) replaces the old one, except a purged one.
const POST_UPSERT = `ON CONFLICT(id) DO UPDATE SET ${POST_COLS.filter((c) => !['id', 'source', 'first_run'].includes(c)).map((c) => `${c} = excluded.${c}`).join(', ')} WHERE posts.purged_at IS NULL AND excluded.last_run > posts.last_run`;

async function ingest(request, env) {
  let doc;
  try { doc = await request.json(); } catch { return json({ ok: false, errors: ['body: must be the capture as JSON'] }, 400); }
  const known = new Set((await env.DB.prepare('SELECT id FROM posts').all()).results.map((r) => r.id));
  const { errors, warnings } = checkCapture(doc, { desks, known, now: new Date() });
  if (errors.length) return json({ ok: false, run: doc?.run?.id ?? null, errors, warnings }, 422);
  const text = JSON.stringify(doc);
  const existing = await env.DB.prepare('SELECT bytes FROM captures WHERE run_id = ?1').bind(doc.run.id).first();
  if (existing) return json({ ok: existing.bytes === text.length, duplicate: true, run: doc.run.id, note: existing.bytes === text.length ? 'already in the store' : 'a different file for this run is already in the store; a pushed capture is never rewritten' }, existing.bytes === text.length ? 200 : 409);
  const rows = rowsOf(doc, stamp());
  const gz = await gzip(text);
  const db = env.DB;
  await db.batch([
    ...inserts(db, 'runs', RUN_COLS, [rows.run], 'INSERT'),
    db.prepare('INSERT INTO captures (run_id, gz, bytes, updated_at) VALUES (?1, ?2, ?3, ?4)').bind(doc.run.id, gz, text.length, stamp()),
    ...inserts(db, 'posts', POST_COLS, rows.posts, 'INSERT', POST_UPSERT),
    ...inserts(db, 'post_runs', ['post_id', 'run_id'], rows.post_runs),
    ...inserts(db, 'observations', OBS_COLS, rows.observations),
    ...inserts(db, 'sweeps', SWEEP_COLS, rows.sweeps, 'INSERT OR REPLACE'),
    ...inserts(db, 'volume_points', VOL_COLS, rows.volume_points, 'INSERT OR REPLACE'),
    ...inserts(db, 'trends', TREND_COLS, rows.trends, 'INSERT OR REPLACE'),
    ...inserts(db, 'context', CONTEXT_COLS, rows.context, 'INSERT OR REPLACE'),
    ...inserts(db, 'answers', ANSWER_COLS, rows.answers, 'INSERT OR REPLACE'),
  ]);
  return json({ ok: true, run: doc.run.id, posts: rows.posts.length, observations: rows.observations.length, volume_points: rows.volume_points.length, bytes: text.length, gzip: gz.length, warnings });
}

const ids = (url) => (url.searchParams.get('ids') ?? '').split(',').map((s) => s.trim()).filter((s) => /^\d{15,20}$/.test(s)).slice(0, 200);
const place = (n) => Array.from({ length: n }, (_, i) => `?${i + 1}`).join(', ');

async function read(url, env) {
  const db = env.DB;
  const path = url.pathname;
  if (path === '/api/runs') {
    const from = url.searchParams.get('from') ?? '0000', to = url.searchParams.get('to') ?? '9999';
    const limit = Math.min(Number(url.searchParams.get('limit') ?? 200), 5000);
    const { results } = await db.prepare('SELECT * FROM runs WHERE started_at >= ?1 AND started_at <= ?2 ORDER BY started_at DESC LIMIT ?3').bind(from, to, limit).all();
    return json({ runs: results });
  }
  const cap = /^\/api\/capture\/(\d{4}-\d{2}-\d{2}T\d{4}Z)$/.exec(path);
  if (cap) {
    const row = await db.prepare('SELECT gz FROM captures WHERE run_id = ?1').bind(cap[1]).first();
    if (!row) return json({ error: 'no such run' }, 404);
    return new Response(await gunzip(row.gz), { headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
  }
  if (path === '/api/posts') {
    const want = ids(url);
    if (!want.length) return json({ posts: [] });
    const { results } = await db.prepare(`SELECT * FROM posts WHERE id IN (${place(want.length)})`).bind(...want).all();
    return json({ posts: results.map(recordOf) });
  }
  const one = /^\/api\/post\/(\d{15,20})$/.exec(path);
  if (one) {
    const row = await db.prepare('SELECT * FROM posts WHERE id = ?1').bind(one[1]).first();
    if (!row) return json({ error: 'no such post' }, 404);
    const [runs, obs, check] = await Promise.all([
      db.prepare('SELECT run_id FROM post_runs WHERE post_id = ?1 ORDER BY run_id').bind(one[1]).all(),
      db.prepare('SELECT count(*) AS n, min(at) AS first, max(at) AS last FROM observations WHERE post_id = ?1').bind(one[1]).first(),
      db.prepare('SELECT result, detail, checked_at, run, purged_at FROM checks WHERE post_id = ?1').bind(one[1]).first(),
    ]);
    return json({ post: recordOf(row), runs: runs.results.map((r) => r.run_id), observations: obs, check: check ?? null });
  }
  if (path === '/api/observations') {
    const want = ids(url);
    const since = url.searchParams.get('since'), until = url.searchParams.get('until') ?? '9999';
    let q;
    if (want.length) q = db.prepare(`SELECT * FROM observations WHERE post_id IN (${place(want.length)}) ORDER BY post_id, at`).bind(...want);
    else if (since) q = db.prepare('SELECT * FROM observations WHERE at >= ?1 AND at <= ?2 ORDER BY at LIMIT 50000').bind(since, until);
    else return json({ error: 'give ?ids= or ?since=' }, 400);
    const { results } = await q.all();
    return json({ observations: results.map((o) => ({ id: o.post_id, at: o.at, run_id: o.run_id, state: o.state, views: o.views, likes: o.likes, reposts: o.reposts, quotes: o.quotes, replies: o.replies, bookmarks: o.bookmarks, approx: Boolean(o.approx) })) });
  }
  if (path === '/api/volume') {
    const desk = url.searchParams.get('desk');
    const since = url.searchParams.get('since') ?? '0000';
    const q = desk
      ? db.prepare('SELECT * FROM volume_points WHERE desk = ?1 AND start >= ?2 ORDER BY start').bind(desk, since)
      : db.prepare('SELECT * FROM volume_points WHERE start >= ?1 ORDER BY desk, start LIMIT 50000').bind(since);
    const { results } = await q.all();
    return json({ points: results });
  }
  if (path === '/api/checks') {
    const want = ids(url);
    const result = url.searchParams.get('result');
    if (!want.length && result) {
      const limit = Math.min(Number(url.searchParams.get('limit') ?? 200), 2000);
      const { results } = await db.prepare('SELECT * FROM checks WHERE result = ?1 ORDER BY checked_at DESC LIMIT ?2').bind(result, limit).all();
      return json({ checks: Object.fromEntries(results.map((r) => [r.post_id, { result: r.result, detail: r.detail, checked_at: r.checked_at, handle: r.handle, run: r.run, purged_at: r.purged_at }])) });
    }
    if (!want.length) return json({ checks: {} });
    const { results } = await db.prepare(`SELECT * FROM checks WHERE post_id IN (${place(want.length)})`).bind(...want).all();
    return json({ checks: Object.fromEntries(results.map((r) => [r.post_id, { result: r.result, detail: r.detail, checked_at: r.checked_at, handle: r.handle, run: r.run, purged_at: r.purged_at }])) });
  }
  if (path === '/api/status') {
    const one = async (sql) => (await db.prepare(sql).first())?.n ?? 0;
    const [runs, posts, observations, purged, checks, last, sweep] = await Promise.all([
      one('SELECT count(*) AS n FROM runs'), one('SELECT count(*) AS n FROM posts'), one('SELECT count(*) AS n FROM observations'),
      one('SELECT count(*) AS n FROM posts WHERE purged_at IS NOT NULL'), one('SELECT count(*) AS n FROM checks'),
      db.prepare('SELECT id, started_at, received_at, reads, reads_left FROM runs ORDER BY started_at DESC LIMIT 1').first(),
      db.prepare('SELECT * FROM sweep_log ORDER BY at DESC LIMIT 1').first(),
    ]);
    return json({ runs, posts, observations, purged, checks, last_run: last ?? null, last_sweep: sweep ?? null, now: stamp() });
  }
  return json({ error: 'no such route' }, 404);
}

// Gate 2 for a list of posts, now. Returns what X said and records it.
async function verify(env, want, { purge = true } = {}) {
  const db = env.DB;
  const out = { checked: 0, ok: 0, missing: 0, mismatch: 0, withheld: 0, errors: 0, purged: 0, results: {} };
  if (!want.length) return out;
  const { results } = await db.prepare(`SELECT id, url, text, author_handle, first_run, purged_at FROM posts WHERE id IN (${place(want.length)})`).bind(...want).all();
  const toPurge = [];
  for (const p of results) {
    const at = stamp();
    let verdict;
    try {
      const url = p.url || `https://x.com/${p.author_handle}/status/${p.id}`;
      const answer = await askX(url);
      verdict = answer === WITHHELD ? { result: 'withheld', detail: 'X will not show this post without a login' } : compareToX({ text: p.text, author: { handle: p.author_handle } }, answer);
    } catch (e) { out.errors++; out.results[p.id] = { result: 'error', detail: String(e.message) }; continue; }
    out.checked++; out[verdict.result]++;
    out.results[p.id] = verdict;
    await db.prepare('INSERT INTO checks (post_id, result, detail, checked_at, handle, run) VALUES (?1, ?2, ?3, ?4, ?5, ?6) ON CONFLICT(post_id) DO UPDATE SET result = excluded.result, detail = excluded.detail, checked_at = excluded.checked_at')
      .bind(p.id, verdict.result, verdict.detail, at, p.author_handle, p.first_run).run();
    if (verdict.result === 'missing' && !p.purged_at) toPurge.push(p.id);
  }
  if (purge) out.purged = await purgePosts(env, toPurge.slice(0, SWEEP_PURGES));
  return out;
}

// A post X no longer returns loses its words everywhere: its row, and every capture file it is in.
async function purgePosts(env, postIds) {
  const db = env.DB;
  let n = 0;
  for (const id of postIds) {
    const at = stamp();
    await db.prepare("UPDATE posts SET text = '', url = '', media = '[]', note = 'null', lead = NULL, author_name = '', purged_at = ?2 WHERE id = ?1 AND purged_at IS NULL").bind(id, at).run();
    await db.prepare('UPDATE checks SET purged_at = ?2 WHERE post_id = ?1 AND purged_at IS NULL').bind(id, at).run();
    const { results } = await db.prepare('SELECT run_id FROM post_runs WHERE post_id = ?1').bind(id).all();
    for (const { run_id } of results) {
      const row = await db.prepare('SELECT gz FROM captures WHERE run_id = ?1').bind(run_id).first();
      if (!row) continue;
      const doc = JSON.parse(await gunzip(row.gz));
      const stripped = JSON.stringify(stripCapture(doc, new Set([id]), at));
      await db.prepare('UPDATE captures SET gz = ?2, bytes = ?3, updated_at = ?4 WHERE run_id = ?1').bind(run_id, await gzip(stripped), stripped.length, at).run();
    }
    n++;
  }
  return n;
}

// The hourly sweep: posts X stopped returning first, then the posts checked longest ago.
async function sweep(env) {
  const db = env.DB;
  const before = new Date(Date.now() - RECHECK_HOURS * 3600000).toISOString().replace(/\.\d{3}Z$/, 'Z');
  const { results } = await db.prepare(`
    SELECT p.id,
      (SELECT o.state FROM observations o WHERE o.post_id = p.id ORDER BY o.at DESC LIMIT 1) AS last_state,
      c.checked_at
    FROM posts p LEFT JOIN checks c ON c.post_id = p.id
    WHERE p.purged_at IS NULL AND (c.checked_at IS NULL OR c.checked_at < ?1)
    ORDER BY (last_state = 'unavailable') DESC, c.checked_at IS NOT NULL, c.checked_at ASC
    LIMIT ?2`).bind(before, SWEEP_CHECKS).all();
  const at = stamp();
  const r = await verify(env, results.map((p) => p.id));
  await db.prepare('INSERT OR REPLACE INTO sweep_log (at, checked, ok, missing, mismatch, withheld, errors, purged, note) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9)')
    .bind(at, r.checked, r.ok, r.missing, r.mismatch, r.withheld, r.errors, r.purged, `${results.filter((p) => p.last_state === 'unavailable').length} were unavailable at their last reading`).run();
  return r;
}

// The board. The store keeps the thread; tools/lib/board.mjs decides what a message may be and what is open.
const STATE_WINDOW = 2000;     // messages the state is derived from; older open items are rare and still listed by /api/board
const rowToMessage = (r) => ({ id: r.id, at: r.at, from: r.from_agent, to: r.to_agent, channel: r.channel, kind: r.kind, re: r.re ?? undefined, subject: r.subject, body: r.body ?? undefined, refs: r.refs ? JSON.parse(r.refs) : undefined, status: r.status ? JSON.parse(r.status) : undefined });

async function boardPost(request, env) {
  const m = await request.json().catch(() => null);
  const errors = checkMessage(m);
  if (!errors.length && m.re != null && !(await env.DB.prepare('SELECT id FROM board WHERE id = ?1').bind(m.re).first())) errors.push(`re: no message ${m.re}`);
  if (errors.length) return json({ ok: false, errors }, 422);
  const at = stamp();
  const r = await env.DB.prepare('INSERT INTO board (at, from_agent, to_agent, channel, kind, re, subject, body, refs, status) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10) RETURNING id')
    .bind(at, m.from, m.to, m.channel, m.kind, m.re ?? null, m.subject.trim(), m.body ?? null, m.refs ? JSON.stringify(m.refs) : null, m.status ? JSON.stringify(m.status) : null).first();
  return json({ ok: true, id: r.id, at });
}

async function boardRead(url, env) {
  const as = url.searchParams.get('as');
  if (as && !(as in BOARD.agents)) return json({ error: 'as: not an agent' }, 400);
  let since = Number(url.searchParams.get('since') ?? NaN);
  if (!Number.isFinite(since)) since = as ? ((await env.DB.prepare('SELECT last_id FROM board_cursors WHERE agent = ?1').bind(as).first())?.last_id ?? 0) : 0;
  const limit = Math.min(Number(url.searchParams.get('limit')) || 200, 1000);
  const channel = url.searchParams.get('channel');
  const q = channel
    ? env.DB.prepare('SELECT * FROM board WHERE id > ?1 AND channel = ?2 ORDER BY id LIMIT ?3').bind(since, channel, limit)
    : env.DB.prepare('SELECT * FROM board WHERE id > ?1 ORDER BY id LIMIT ?2').bind(since, limit);
  const { results } = await q.all();
  return json({ since, messages: results.map(rowToMessage) });
}

async function boardSeen(request, env) {
  const b = await request.json().catch(() => ({}));
  if (!(b.as in BOARD.agents) || !Number.isInteger(b.id) || b.id < 0) return json({ ok: false, errors: ['give {as: agent, id: last message read}'] }, 422);
  const at = stamp();
  // A cursor only moves forward; reading again at the same place still counts as being seen.
  await env.DB.prepare('INSERT INTO board_cursors (agent, last_id, seen_at) VALUES (?1, ?2, ?3) ON CONFLICT(agent) DO UPDATE SET last_id = max(last_id, excluded.last_id), seen_at = excluded.seen_at').bind(b.as, b.id, at).run();
  return json({ ok: true, as: b.as, id: b.id, seen_at: at });
}

async function boardState(env) {
  const db = env.DB;
  const [{ results: rows }, { results: cursors }, last_run, last_sweep] = await Promise.all([
    db.prepare('SELECT * FROM (SELECT * FROM board ORDER BY id DESC LIMIT ?1) ORDER BY id').bind(STATE_WINDOW).all(),
    db.prepare('SELECT * FROM board_cursors').all(),
    db.prepare('SELECT id, started_at, received_at, status, reads, reads_left, posts FROM runs ORDER BY started_at DESC LIMIT 1').first(),
    db.prepare('SELECT at, checked, missing, purged FROM sweep_log ORDER BY at DESC LIMIT 1').first(),
  ]);
  return json(stateOf({ messages: rows.map(rowToMessage), cursors, now: stamp(), store: { last_run: last_run ?? null, last_sweep: last_sweep ?? null } }));
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/ingest' || url.pathname.startsWith('/api/')) {
      if (!authed(request, env)) return json({ error: 'a bearer token is required' }, 401);
      try {
        if (url.pathname === '/ingest') return request.method === 'POST' ? await ingest(request, env) : json({ error: 'POST a capture' }, 405);
        if (url.pathname === '/api/verify' && request.method === 'POST') {
          const body = await request.json().catch(() => ({}));
          const want = (body.ids ?? []).filter((s) => /^\d{15,20}$/.test(String(s))).slice(0, 100);
          return json(await verify(env, want, { purge: body.purge !== false }));
        }
        if (url.pathname === '/api/sweep' && request.method === 'POST') return json(await sweep(env));
        if (url.pathname === '/api/board') return request.method === 'POST' ? await boardPost(request, env) : await boardRead(url, env);
        if (url.pathname === '/api/board/seen' && request.method === 'POST') return await boardSeen(request, env);
        if (url.pathname === '/api/state' && request.method === 'GET') return await boardState(env);
        if (request.method === 'GET') return await read(url, env);
        return json({ error: 'no such route' }, 404);
      } catch (e) {
        return json({ error: String(e.message ?? e) }, 500);
      }
    }
    return env.ASSETS.fetch(request);
  },
  async scheduled(event, env, ctx) {
    ctx.waitUntil(sweep(env));
  },
};
