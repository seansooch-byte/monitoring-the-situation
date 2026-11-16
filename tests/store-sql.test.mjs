// The store's SQL, run for real: the statements the Worker sends to D1 (tools/lib/store-sql.mjs), against
// worker/schema.sql in SQLite. Written after 15 November 2026, when the store spent the account's free
// 100,000 rows written a day by 17:10Z and every write failed until midnight UTC, the agents' board's
// included: each capture rewrote a week of hourly counts that had not changed, and nothing kept the store
// to a share. The same day showed the deletion sweep had never finished a run: it bound 150 ids to one
// statement (D1 allows 100) after reading every post, every hour.
//
// node:sqlite arrived in node 22.5; on an older node these tests are skipped, not failed, because
// tools/ship.sh refuses to ship on a failing suite and the grabber's machine ships every hour.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { rowsOf } from '../tools/lib/store-rows.mjs';
import {
  BTREES, MAX_BOUND, ingestStatements, writeCost, heldBy, resetsAt, secondsUntil, chunks,
  PICK_OWED, PICK_GONE, PICK_ROUND, sweepAsks, checksStatement, SPEND_ADD, ROUND_SET,
} from '../tools/lib/store-sql.mjs';

let DatabaseSync = null;
try { ({ DatabaseSync } = await import('node:sqlite')); } catch { /* node before 22.5 */ }
const skip = DatabaseSync ? false : 'node:sqlite needs node 22.5 or later';

const root = new URL('..', import.meta.url);
const SCHEMA = readFileSync(new URL('worker/schema.sql', root), 'utf8');
const BUDGET = JSON.parse(readFileSync(new URL('contract/budget.json', root), 'utf8'));
const open = () => { const db = new DatabaseSync(':memory:'); db.exec(SCHEMA); return db; };
const run = (db, statements) => statements.reduce((n, s) => n + Number(db.prepare(s.sql).run(...s.params).changes), 0);
const all = (db, sql, ...params) => db.prepare(sql).all(...params);
const plan = (db, sql, ...params) => all(db, `EXPLAIN QUERY PLAN ${sql}`, ...params).map((r) => r.detail).join(' | ');

const hours = (from, n) => Array.from({ length: n }, (_, i) => new Date(Date.parse(from) + i * 3600000).toISOString().replace('.000Z', 'Z'));
function capture(id, { counts = {}, posts = [], observations = [] } = {}) {
  return {
    run: { id, started_at: `${id.slice(0, 13)}:${id.slice(13, 15)}:00Z`, status: 'ok' },
    posts, observations,
    volume: Object.entries(counts).map(([key, points]) => ({ key, desk: key.split('.')[1], query: 'q', points })),
  };
}
const deliver = (db, doc, at = '2026-11-16T06:00:00Z') => run(db, ingestStatements(rowsOf(doc, at)));

test('a week of hourly counts delivered again writes only the hours that are new or changed', { skip }, () => {
  const db = open();
  const week = hours('2026-11-09T06:00:00Z', 6);
  const first = capture('2026-11-16T0505Z', { counts: { 'desk.politics': week.map((start, i) => ({ start, count: 100 + i })) } });
  deliver(db, first);
  assert.equal(all(db, 'SELECT count(*) AS n FROM volume_points')[0].n, 6);

  // Four hours later: the same six hours, one of them recounted by X, and one new hour.
  const next = [...week.map((start, i) => ({ start, count: i === 2 ? 999 : 100 + i })), { start: '2026-11-09T12:00:00Z', count: 7 }];
  const second = rowsOf(capture('2026-11-16T0905Z', { counts: { 'desk.politics': next } }), '2026-11-16T09:10:00Z');
  const volume = ingestStatements(second).filter((s) => s.table === 'volume_points');
  assert.equal(run(db, volume), 2, 'two rows change: the recount and the new hour; five identical hours are not written again');

  const rows = Object.fromEntries(all(db, 'SELECT start, count, run_id FROM volume_points').map((r) => [r.start, r]));
  assert.equal(rows[week[2]].count, 999, "a later run's count replaces an earlier one");
  assert.equal(rows[week[2]].run_id, '2026-11-16T0905Z');
  assert.equal(rows[week[0]].run_id, '2026-11-16T0505Z', 'an unchanged hour keeps the run that last changed it');
  assert.equal(rows['2026-11-09T12:00:00Z'].count, 7);
});

test('a count X withdrew or first gave is a change too', { skip }, () => {
  const db = open();
  deliver(db, capture('2026-11-16T0505Z', { counts: { 'desk.ai': [{ start: '2026-11-09T06:00:00Z', count: null }] } }));
  const again = rowsOf(capture('2026-11-16T0905Z', { counts: { 'desk.ai': [{ start: '2026-11-09T06:00:00Z', count: 12 }] } }), 'x');
  assert.equal(run(db, ingestStatements(again).filter((s) => s.table === 'volume_points')), 1);
  const same = rowsOf(capture('2026-11-16T1305Z', { counts: { 'desk.ai': [{ start: '2026-11-09T06:00:00Z', count: 12 }] } }), 'x');
  assert.equal(run(db, ingestStatements(same).filter((s) => s.table === 'volume_points')), 0);
});

test('the cost counted for a table is one row per B-tree the schema gives it', { skip }, () => {
  const db = open();
  for (const [table, n] of Object.entries(BTREES)) {
    const indexes = all(db, `PRAGMA index_list(${table})`).filter((i) => !i.partial).length;   // a partial index takes only the rows it names
    assert.equal(n, 1 + indexes, `${table}: ${indexes} indexes in worker/schema.sql, so ${1 + indexes} rows written per row (D1 counts each index a row enters)`);
  }
});

test('the cost of a capture is known before it is written, and is never under what it changes', { skip }, () => {
  const post = (id) => ({ id, url: `https://x.com/a/status/${id}`, created_at: '2026-11-16T05:00:00Z', text: 't', author: { handle: 'a' }, desk: 'ai' });
  const obs = (id, at) => ({ id, at, state: 'live', views: 1 });
  const doc = capture('2026-11-16T0505Z', {
    posts: [post('1'.repeat(19)), post('2'.repeat(19))],
    observations: [obs('1'.repeat(19), '2026-11-16T05:05:00Z'), obs('2'.repeat(19), '2026-11-16T05:05:00Z'), obs('2'.repeat(19), '2026-11-16T05:06:00Z')],
    counts: { 'desk.ai': hours('2026-11-09T06:00:00Z', 4).map((start) => ({ start, count: 1 })) },
  });
  const rows = rowsOf(doc, '2026-11-16T05:10:00Z');
  const cost = writeCost(rows);
  assert.equal(cost, BTREES.runs + BTREES.captures + 2 * BTREES.posts + 2 * BTREES.post_runs + 3 * BTREES.observations + 4 * BTREES.volume_points);
  assert.ok(cost >= run(open(), ingestStatements(rows)));
});

test('the store stops at its share of the day, and says when the day turns', () => {
  const allowance = BUDGET.store.writes_per_day;
  assert.ok(allowance < BUDGET.store.account_writes_per_day, 'the share leaves room for the board');
  assert.equal(heldBy({ spent: allowance - 5000, cost: 5000, allowance }), false, 'a capture that fits exactly is taken');
  assert.equal(heldBy({ spent: allowance - 4999, cost: 5000, allowance }), true);
  assert.equal(heldBy({ spent: 0, cost: 5000, allowance }), false);
  assert.equal(resetsAt('2026-11-16T17:10:09Z'), '2026-11-17T00:00:00Z');
  assert.equal(resetsAt('2026-12-31T23:59:59Z'), '2027-01-01T00:00:00Z');
  assert.equal(secondsUntil('2026-11-17T00:00:00Z', '2026-11-16T23:59:00Z'), 60);
});

test('the spend of a day adds up in one row', { skip }, () => {
  const db = open();
  db.prepare(SPEND_ADD).run('2026-11-16', 300);
  db.prepare(SPEND_ADD).run('2026-11-16', 45);
  db.prepare(SPEND_ADD).run('2026-11-17', 1);
  assert.deepEqual(all(db, 'SELECT day, written FROM spend ORDER BY day').map((r) => [r.day, r.written]), [['2026-11-16', 345], ['2026-11-17', 1]]);
});

test('no statement binds more values than D1 allows', () => {
  assert.ok(MAX_BOUND <= 100, 'D1 refuses a statement with more than 100 bound values');
  const ids = Array.from({ length: 205 }, (_, i) => String(i));
  const parts = chunks(ids);
  assert.ok(parts.every((p) => p.length <= MAX_BOUND));
  assert.deepEqual(parts.flat(), ids);
  assert.ok(BUDGET.store.sweep_asks <= 45, 'a free Worker may make 50 requests to other sites per run; each ask is one');
});

function seeded() {
  const db = open();
  const post = db.prepare("INSERT INTO posts (id, text, author_handle, first_run, last_run, purged_at) VALUES (?1, 'words', 'a', 'r', 'r', ?2)");
  for (const [id, purged] of [['p1', null], ['p2', null], ['p3', '2026-11-01T00:00:00Z'], ['p4', null], ['p5', null], ['p6', null]]) post.run(id, purged);
  const obs = db.prepare('INSERT INTO observations (post_id, at, run_id, state) VALUES (?1, ?2, ?3, ?4)');
  obs.run('p1', '2026-11-16T05:00:00Z', 'r', 'live');
  obs.run('p2', '2026-11-16T04:00:00Z', 'r', 'unavailable');
  obs.run('p2', '2026-11-16T05:00:00Z', 'r', 'unavailable');
  obs.run('p3', '2026-11-16T05:00:00Z', 'r', 'unavailable');   // gone, and already purged
  obs.run('p4', '2026-11-16T05:00:00Z', 'r', 'unavailable');   // gone, and asked an hour ago
  const check = db.prepare('INSERT INTO checks (post_id, result, checked_at, purged_at) VALUES (?1, ?2, ?3, ?4)');
  check.run('p4', 'ok', '2026-11-16T05:30:00Z', null);
  check.run('p5', 'missing', '2026-11-16T05:30:00Z', null);    // found missing, purge not finished
  check.run('p3', 'missing', '2026-11-01T00:00:00Z', '2026-11-01T00:00:00Z');
  return db;
}
const DAY_AGO = '2026-11-15T06:00:00Z';

test('the sweep finishes a purge it owes before anything else', { skip }, () => {
  const db = seeded();
  assert.deepEqual(all(db, PICK_OWED, 5).map((r) => r.id), ['p5']);
  assert.match(plan(db, PICK_OWED, 5), /checks_owed/, 'read from the index of owed purges, not the whole table');
});

test('the sweep asks first about posts X stopped returning, once a day each, never a purged one', { skip }, () => {
  const db = seeded();
  assert.deepEqual(all(db, PICK_GONE, DAY_AGO, 8).map((r) => r.id), ['p2'], 'one row for p2 though it was seen gone twice; p3 is purged; p4 was asked an hour ago');
  assert.deepEqual(all(db, PICK_GONE, '2026-11-16T05:45:00Z', 8).map((r) => r.id), ['p2', 'p4'], 'p4 is due again once its check is a day old');
  const p = plan(db, PICK_GONE, DAY_AGO, 8);
  assert.match(p, /observations_gone/, 'read from the index of unavailable readings');
  assert.doesNotMatch(p, /SCAN (p|posts)\b/, 'never a pass over every post');
});

test('the rest of the sweep is a round of every post, taken up where the last sweep stopped', { skip }, () => {
  const db = seeded();
  const first = all(db, PICK_ROUND, 0, 3);
  assert.deepEqual(first.map((r) => r.id), ['p1', 'p2', 'p4'], 'in the order they arrived, skipping the purged one');
  const next = all(db, PICK_ROUND, first.at(-1).n, 3);
  assert.deepEqual(next.map((r) => r.id), ['p5', 'p6']);
  assert.match(plan(db, PICK_ROUND, 0, 3), /SEARCH posts USING INTEGER PRIMARY KEY \(rowid>\?\)/, 'a short walk from the mark, not a pass over every post');
});

test('one sweep asks about the gone first, then the round, no post twice, and marks where the round stopped', () => {
  const round = [{ n: 11, id: 'a' }, { n: 12, id: 'g1' }, { n: 13, id: 'b' }, { n: 14, id: 'c' }];
  const s = sweepAsks({ gone: [{ id: 'g1' }, { id: 'g2' }], round, limit: 4, asked: 4 });
  assert.deepEqual(s.ids, ['g1', 'g2', 'a', 'b'], 'g1 is on the round too and is asked once');
  assert.equal(s.mark, 13, 'the round resumes after the last post it reached');
  assert.equal(s.wrapped, false);

  const full = sweepAsks({ gone: Array.from({ length: 6 }, (_, i) => ({ id: `g${i}` })), round, limit: 4, asked: 4 });
  assert.equal(full.ids.length, 4);
  assert.equal(full.mark, null, 'a sweep the gone filled leaves the round where it was');

  const end = sweepAsks({ gone: [], round: round.slice(0, 2), limit: 4, asked: 4 });
  assert.deepEqual(end.ids, ['a', 'g1']);
  assert.equal(end.wrapped, true, 'fewer posts than asked for: the round reached the newest post and starts again');
  assert.equal(end.mark, 0);
});

test('the mark of the round is one row, and a lap is counted when it wraps', { skip }, () => {
  const db = open();
  db.prepare(ROUND_SET).run(40, 0, 'x');
  db.prepare(ROUND_SET).run(0, 1, 'y');
  db.prepare(ROUND_SET).run(8, 0, 'z');
  assert.deepEqual(all(db, 'SELECT last_rowid, laps, updated_at FROM sweep_round').map((r) => [r.last_rowid, r.laps, r.updated_at]), [[8, 1, 'z']]);
});

test('what X said is recorded in one statement, and a later answer replaces the earlier one', { skip }, () => {
  const db = seeded();
  const answers = [
    { post_id: 'p1', result: 'ok', detail: 'same words', checked_at: '2026-11-16T06:00:00Z', handle: 'a', run: 'r' },
    { post_id: 'p4', result: 'missing', detail: 'X has no such post', checked_at: '2026-11-16T06:00:01Z', handle: 'a', run: 'r' },
  ];
  const s = checksStatement(answers);
  db.prepare(s.sql).run(...s.params);
  const rows = Object.fromEntries(all(db, 'SELECT post_id, result, checked_at FROM checks').map((r) => [r.post_id, r]));
  assert.equal(rows.p1.result, 'ok');
  assert.equal(rows.p4.result, 'missing');
  assert.equal(rows.p4.checked_at, '2026-11-16T06:00:01Z');
  assert.deepEqual(all(db, PICK_OWED, 5).map((r) => r.id).sort(), ['p4', 'p5'], 'a post just found missing is owed a purge until the purge is recorded');
});

test('the timer of the Worker is the sweep interval the budget names', () => {
  const config = readFileSync(new URL('wrangler.jsonc', root), 'utf8');
  const crons = /"crons":\s*\[([^\]]*)\]/.exec(config)[1];
  assert.equal(crons.trim(), `"*/${BUDGET.store.sweep_every_minutes} * * * *"`);
});
