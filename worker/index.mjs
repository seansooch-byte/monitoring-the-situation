// The Worker: the site's static files, and the store.
//
// The store is the record in a place where a deletion can be honoured (PROGRAM.md, phase 1):
//   POST /ingest                 a capture from the grabber; Gate 1 runs here; rows go to D1,
//                                the file itself is kept gzipped beside them
//   GET  /api/runs               the runs, newest first (?from=&to=&limit=)
//   GET  /api/capture/<run id>   the capture as delivered, after any purge
//   GET  /api/posts?ids=         records, in the capture's shape
//   GET  /api/observations?ids=  the numbers, by post. By time: /api/runs for the window, then each
//                                run's /api/capture (the index by time was dropped on 2026-11-16)
//   GET  /api/volume?desk=       X's hourly counts (?since=)
//   GET  /api/checks?ids=        what X said about each post
//   POST /api/verify {ids}       ask X now (Gate 2) and record the answers
//   GET  /api/status             counts and the last sweep (reads every row: for a person, not a routine)
//   GET  /api/spend              rows the store has written today, and its share of the day
// Every route above needs `Authorization: Bearer <STORE_TOKEN>` until phase 2 opens the reads.
// Everything else is served from the built site.
//
// The deletion sweep runs every ten minutes (triggers.crons), a few posts at a time: a purge still
// owed is finished first, then posts X stopped returning are asked about, then the round of every
// other post is taken up where it stopped. A 404 purges the post's words, name, media and link from
// its row and from every capture file that holds it, and keeps its id and its numbers.
//
// The store shares Cloudflare's free database plan with the agents' board, and the plan refuses every
// write on the account past 100,000 rows a day. So the store counts what it writes (table `spend`),
// writes only what changed, and answers 429 to a capture that would take it past its share
// (contract/budget.json, store): the capture stays in git and tools/ingest.mjs delivers it after
// 00:00 UTC. The SQL and its cost are tools/lib/store-sql.mjs.
import desks from '../contract/desks.json';
import budget from '../contract/budget.json';
import { checkCapture, idsToLookUp } from '../tools/lib/capture-check.mjs';
import { askX, compareToX, WITHHELD } from '../tools/lib/gate2.mjs';
import { rowsOf, recordOf, stripCapture } from '../tools/lib/store-rows.mjs';
import {
  ingestStatements, checksStatement, writeCost, heldBy, dayOf, resetsAt, secondsUntil, chunks,
  SPEND_OF, SPEND_ADD, PICK_OWED, PICK_GONE, PICK_ROUND, ROUND_GET, ROUND_SET, sweepAsks,
} from '../tools/lib/store-sql.mjs';

const STORE = budget.store;    // the store's share of the day's writes, and the sweep's size
const VERIFY_MAX = 45;         // posts one request may ask X about: a free Worker may call 50 other sites per run

const stamp = () => new Date().toISOString().replace(/\.\d{3}Z$/, 'Z');
const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', ...headers } });
// Rows D1 says a statement, or a batch of them, wrote.
const wrote = (r) => (Array.isArray(r) ? r : [r]).reduce((n, x) => n + (x?.meta?.rows_written ?? 0), 0);
const spentToday = async (db, now) => (await db.prepare(SPEND_OF).bind(dayOf(now)).first())?.written ?? 0;
// The spend row is itself one row written. A failed count never fails the work it counts.
const spend = (db, now, n) => db.prepare(SPEND_ADD).bind(dayOf(now), n + 1).run().then(() => true, () => false);
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

async function ingest(request, env) {
  let doc;
  try { doc = await request.json(); } catch { return json({ ok: false, errors: ['body: must be the capture as JSON'] }, 400); }
  // Only the ids this capture points at outside its own posts, never the whole table: reading every id per
  // capture spent the account's free D1 reads on 2026-11-14.
  const known = new Set();
  const want = idsToLookUp(doc);
  for (let i = 0; i < want.length; i += 90) {
    const part = want.slice(i, i + 90);
    for (const r of (await env.DB.prepare(`SELECT id FROM posts WHERE id IN (${place(part.length)})`).bind(...part).all()).results) known.add(r.id);
  }
  const { errors, warnings } = checkCapture(doc, { desks, known, now: new Date() });
  if (errors.length) return json({ ok: false, run: doc?.run?.id ?? null, errors, warnings }, 422);
  const text = JSON.stringify(doc);
  const existing = await env.DB.prepare('SELECT bytes FROM captures WHERE run_id = ?1').bind(doc.run.id).first();
  if (existing) return json({ ok: existing.bytes === text.length, duplicate: true, run: doc.run.id, note: existing.bytes === text.length ? 'already in the store' : 'a different file for this run is already in the store; a pushed capture is never rewritten' }, existing.bytes === text.length ? 200 : 409);
  const db = env.DB;
  const now = stamp();
  const rows = rowsOf(doc, now);
  // The store's share of the day: a capture that would pass it waits in git for the day to turn, so the
  // account's other database, the agents' board, is never left unable to write.
  const cost = writeCost(rows);
  const spent = await spentToday(db, now);
  if (heldBy({ spent, cost, allowance: STORE.writes_per_day })) {
    const resets = resetsAt(now);
    return json({ ok: false, held: true, run: doc.run.id, spent, cost, allowance: STORE.writes_per_day, resets_at: resets, error: `the store has written ${spent} of its ${STORE.writes_per_day} rows for today and this capture may need ${cost}; it stays in git and is taken after ${resets}` }, 429, { 'retry-after': String(secondsUntil(resets, now)) });
  }
  const gz = await gzip(text);
  const done = await db.batch([
    ...ingestStatements(rows).map((q) => db.prepare(q.sql).bind(...q.params)),
    db.prepare('INSERT INTO captures (run_id, gz, bytes, updated_at) VALUES (?1, ?2, ?3, ?4)').bind(doc.run.id, gz, text.length, now),
  ]);
  const written = wrote(done) || cost;   // what D1 counted; the estimate stands in if it gave no count
  await spend(db, now, written);
  return json({ ok: true, run: doc.run.id, posts: rows.posts.length, observations: rows.observations.length, volume_points: rows.volume_points.length, bytes: text.length, gzip: gz.length, written, spent: spent + written + 1, allowance: STORE.writes_per_day, warnings });
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
    const results = [];
    for (const part of chunks(want)) results.push(...(await db.prepare(`SELECT * FROM posts WHERE id IN (${place(part.length)})`).bind(...part).all()).results);
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
    // By post only. Reading by time would walk every observation now that nothing indexes them by time.
    if (!want.length) return json({ error: 'give ?ids=; for a window of time, read /api/runs?from=&to= and then /api/capture/<run id> for each run' }, 400);
    const results = [];
    for (const part of chunks(want)) results.push(...(await db.prepare(`SELECT * FROM observations WHERE post_id IN (${place(part.length)}) ORDER BY post_id, at`).bind(...part).all()).results);
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
    const results = [];
    for (const part of chunks(want)) results.push(...(await db.prepare(`SELECT * FROM checks WHERE post_id IN (${place(part.length)})`).bind(...part).all()).results);
    return json({ checks: Object.fromEntries(results.map((r) => [r.post_id, { result: r.result, detail: r.detail, checked_at: r.checked_at, handle: r.handle, run: r.run, purged_at: r.purged_at }])) });
  }
  if (path === '/api/spend') {
    const now = stamp();
    return json({ day: dayOf(now), written: await spentToday(db, now), allowance: STORE.writes_per_day, account_limit: STORE.account_writes_per_day, resets_at: resetsAt(now), last_sweep: (await db.prepare('SELECT * FROM sweep_log ORDER BY at DESC LIMIT 1').first()) ?? null });
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

// Gate 2 for a list of posts, now. Returns what X said and records it, in one statement. `owed` are
// posts already known gone whose purge comes first.
async function verify(env, want, { purge = true, owed = [] } = {}) {
  const db = env.DB;
  const out = { checked: 0, ok: 0, missing: 0, mismatch: 0, withheld: 0, errors: 0, purged: 0, written: 0, results: {} };
  const posts = [];
  for (const part of chunks(want)) posts.push(...(await db.prepare(`SELECT id, url, text, author_handle, first_run, purged_at FROM posts WHERE id IN (${place(part.length)})`).bind(...part).all()).results);
  const answers = [];
  const toPurge = [...owed];
  for (const p of posts) {
    const at = stamp();
    let verdict;
    try {
      const url = p.url || `https://x.com/${p.author_handle}/status/${p.id}`;
      const answer = await askX(url);
      verdict = answer === WITHHELD ? { result: 'withheld', detail: 'X will not show this post without a login' } : compareToX({ text: p.text, author: { handle: p.author_handle } }, answer);
    } catch (e) { out.errors++; out.results[p.id] = { result: 'error', detail: String(e.message) }; continue; }
    out.checked++; out[verdict.result]++;
    out.results[p.id] = verdict;
    answers.push({ post_id: p.id, result: verdict.result, detail: verdict.detail, checked_at: at, handle: p.author_handle, run: p.first_run });
    if (verdict.result === 'missing' && !p.purged_at && !toPurge.includes(p.id)) toPurge.push(p.id);
  }
  if (answers.length) { const q = checksStatement(answers); out.written += wrote(await db.prepare(q.sql).bind(...q.params).run()); }
  if (purge) {
    const r = await purgePosts(env, toPurge.slice(0, STORE.sweep_purges));
    out.purged = r.purged; out.written += r.written;
  }
  return out;
}

// A post X no longer returns loses its words everywhere: its row, and every capture file it is in.
// The row goes first and the check is marked last, so a purge cut short (a free Worker's time is brief)
// is still owed and the next sweep finishes it; a file already stripped is not written again.
async function purgePosts(env, postIds) {
  const db = env.DB;
  const out = { purged: 0, written: 0 };
  for (const id of postIds) {
    const at = (await db.prepare('SELECT purged_at FROM posts WHERE id = ?1').bind(id).first())?.purged_at ?? stamp();
    out.written += wrote(await db.prepare("UPDATE posts SET text = '', url = '', media = '[]', note = 'null', lead = NULL, author_name = '', purged_at = ?2 WHERE id = ?1 AND purged_at IS NULL").bind(id, at).run());
    const { results } = await db.prepare('SELECT run_id FROM post_runs WHERE post_id = ?1').bind(id).all();
    for (const { run_id } of results) {
      const row = await db.prepare('SELECT gz FROM captures WHERE run_id = ?1').bind(run_id).first();
      if (!row) continue;
      const doc = JSON.parse(await gunzip(row.gz));
      const held = (doc.posts ?? []).find((p) => p.id === id);
      if (!held || held.purged_at) continue;
      const stripped = JSON.stringify(stripCapture(doc, new Set([id]), at));
      out.written += wrote(await db.prepare('UPDATE captures SET gz = ?2, bytes = ?3, updated_at = ?4 WHERE run_id = ?1').bind(run_id, await gzip(stripped), stripped.length, at).run());
    }
    out.written += wrote(await db.prepare('UPDATE checks SET purged_at = ?2 WHERE post_id = ?1 AND purged_at IS NULL').bind(id, at).run());
    out.purged++;
  }
  return out;
}

// The deletion sweep: every few minutes, a few posts (tools/lib/store-sql.mjs says how they are picked
// and why none of the picks reads the whole table).
async function sweep(env) {
  const db = env.DB;
  const now = stamp();
  const before = new Date(Date.now() - STORE.recheck_hours * 3600000).toISOString().replace(/\.\d{3}Z$/, 'Z');
  const mark = (await db.prepare(ROUND_GET).first())?.last_rowid ?? 0;
  const [owed, gone, round] = (await db.batch([
    db.prepare(PICK_OWED).bind(STORE.sweep_purges),
    db.prepare(PICK_GONE).bind(before, STORE.sweep_asks),
    db.prepare(PICK_ROUND).bind(mark, STORE.sweep_asks),
  ])).map((r) => r.results);
  const plan = sweepAsks({ gone, round, limit: STORE.sweep_asks });
  const r = await verify(env, plan.ids, { owed: owed.map((o) => o.id) });
  // A sweep X answered nothing to (it is down, or refusing us) leaves the round where it was.
  const moved = plan.mark !== null && (r.checked > 0 || plan.ids.length === 0);
  const note = `${gone.length} gone, ${owed.length} owed a purge, round ${moved ? `to ${plan.mark}${plan.wrapped ? ' (new lap)' : ''}` : `stays at ${mark}`}`;
  const done = await db.batch([
    ...(moved ? [db.prepare(ROUND_SET).bind(plan.mark, plan.wrapped ? 1 : 0, now)] : []),
    db.prepare('INSERT OR REPLACE INTO sweep_log (at, checked, ok, missing, mismatch, withheld, errors, purged, note) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9)')
      .bind(now, r.checked, r.ok, r.missing, r.mismatch, r.withheld, r.errors, r.purged, note),
  ]);
  await spend(db, now, r.written + wrote(done));
  return { ...r, note };
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
          const want = (body.ids ?? []).filter((s) => /^\d{15,20}$/.test(String(s))).slice(0, VERIFY_MAX);
          const now = stamp();
          const r = await verify(env, want, { purge: body.purge !== false });
          await spend(env.DB, now, r.written);
          return json(r);
        }
        if (url.pathname === '/api/sweep' && request.method === 'POST') return json(await sweep(env));
        if (url.pathname.startsWith('/api/board') || url.pathname === '/api/state') return json({ error: 'the board moved to https://agent-board.seansooch.workers.dev (rules: node tools/board.mjs rules)' }, 410);
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
