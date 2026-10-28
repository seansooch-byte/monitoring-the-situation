// The day's budget report: phase 0's done test, as arithmetic over captures. It reads the
// numbers from contract/budget.json and the desks from contract/desks.json, so it moves with
// the contract. Every failure it can name is produced here on an invented day.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { readsOf, readsLeftOf, summarizeDay, formatDay } from '../tools/lib/budget.mjs';

const root = new URL('..', import.meta.url);
const DESKS = JSON.parse(readFileSync(new URL('contract/desks.json', root), 'utf8'));
const BUDGET = JSON.parse(readFileSync(new URL('contract/budget.json', root), 'utf8'));
const H = 3600000;
const DAY = Date.parse('2026-10-27T00:00:00Z');
const iso = (ms) => new Date(ms).toISOString().replace('.000Z', 'Z');
const runId = (ms) => iso(ms).replace(/:(\d\d):00Z$/, '$1Z').replace(/(\d\d)(\d\d)Z$/, '$1$2Z');

const CITED = ['2115000000000000001', '2115000000000000002'];

// One run at `hour` on the invented day. By default it does everything the contract asks.
function cap(hour, over = {}) {
  const start = DAY + hour * H + 5 * 60000;
  const sweeps = [];
  const watchIds = over.watch ?? CITED;
  sweeps.push({ id: 'watch', kind: 'watch', desk: null, method: 'by id', window_hours: null, status: 'ok', reason: null, post_ids: watchIds });
  for (const d of DESKS.desks) {
    const due = hour % d.sweep_every_hours === 0;
    const skip = (over.skipDesks ?? []).includes(d.id);
    if (due) sweeps.push({ id: `desk.${d.id}`, kind: 'desk', desk: d.id, method: 'search', window_hours: 24, status: skip ? 'skipped' : 'ok', reason: skip ? 'non-hourly desk skipped after cut order' : null, post_ids: [] });
  }
  const volumeDesks = over.volume ?? DESKS.desks.filter((_, i) => i % 4 === hour % 4).map((d) => d.id);
  const volume = volumeDesks.map((id) => ({ key: `desk.${id}`, desk: id, query: `${id} lang:en`, granularity: 'hour', points: [{ start: iso(start - H), count: 1000 }] }));
  for (const id of volumeDesks) sweeps.push({ id: `volume.${id}`, kind: 'volume', desk: id, method: 'counts', window_hours: 168, status: 'ok', reason: null, post_ids: [] });
  const run = {
    id: runId(start), started_at: iso(start), finished_at: iso(start + 4 * 60000),
    status: over.status ?? 'ok', reason: over.reason ?? null,
    grabber: { agent: 'test', model: null, method: 'synthetic' },
    requests_rev: null,
    reads: over.reads === undefined ? 30 : over.reads,
    reads_left: over.reads_left === undefined ? 1000 - 30 * (hour + 1) : over.reads_left,
  };
  if (over.noReadsField) { delete run.reads; delete run.reads_left; }
  return { schema: 'mts.capture/1', run, sweeps, trends: [], posts: [], observations: [], context: [], answers: over.answers ?? [], volume };
}

const goodDay = () => Array.from({ length: 24 }, (_, h) => cap(h));
const ledger = Object.fromEntries(CITED.map((id) => [id, { result: 'ok', first_run: '2026-10-20T0005Z' }]));
const summarize = (caps, over = {}) => summarizeDay(caps, { desks: DESKS, budget: BUDGET, cited: CITED, ledger, ...over });

test('reads come from run.reads, and from the reason sentence only when the field is missing', () => {
  assert.equal(readsOf(cap(3)), 30);
  assert.equal(readsLeftOf(cap(3)), 1000 - 120);
  const old = cap(3, { noReadsField: true, status: 'partial', reason: 'Night run: 21 X reads this run (936 to 915 left today), no 429 refusals.' });
  assert.equal(readsOf(old), 21);
  assert.equal(readsLeftOf(old), 915);
  const silent = cap(3, { noReadsField: true, status: 'partial', reason: 'something else entirely' });
  assert.equal(readsOf(silent), null);
  assert.equal(readsLeftOf(silent), null);
});

test('a day that does everything the contract asks passes every check', () => {
  const s = summarize(goodDay());
  assert.equal(s.date, '2026-10-27');
  assert.equal(s.runs.n, 24);
  assert.equal(s.reads.total, 720);
  assert.ok(s.desks.every((d) => d.ok), 'every desk swept at its cadence');
  assert.ok(s.volume.every((v) => v.ok), 'every desk counted within four hours');
  assert.equal(s.watch.max_left_out, 0);
  assert.deepEqual(Object.values(s.checks), [true, true, true, true, true]);
  assert.equal(s.pass, true);
  assert.match(formatDay(s), /PASS/);
});

test('a desk skipped after the cut order fails the desks check, by name, and the run rule', () => {
  const skipDesks = DESKS.desks.filter((d) => d.sweep_every_hours > 1).map((d) => d.id);
  const s = summarize(goodDay().map((c, h) => cap(h, { skipDesks, status: 'partial', reason: 'non-hourly desk skipped after cut order' })));
  const failed = s.desks.filter((d) => !d.ok).map((d) => d.id);
  assert.deepEqual(failed, skipDesks);
  assert.equal(s.checks.desks, false);
  assert.equal(s.checks.runs, false, 'a partial run for our own cut order is a failure');
  assert.equal(s.runs.bad.length, 24);
  assert.equal(s.pass, false);
  assert.match(formatDay(s), /FAIL/);
  for (const id of skipDesks.slice(0, 3)) assert.match(formatDay(s), new RegExp(id));
});

test('a partial run for a reason on X\'s side does not fail the run rule', () => {
  const s = summarize(goodDay().map((c, h) => (h === 5 ? cap(h, { status: 'partial', reason: 'X answered 429 on the quote stream; the rest ran' }) : c)));
  assert.equal(s.checks.runs, true);
  assert.equal(s.runs.partial, 1);
});

test('underspending fails the reads check, and so does overspending or not saying', () => {
  assert.equal(summarize(goodDay().map((c, h) => cap(h, { reads: 20 }))).checks.reads, false);
  assert.equal(summarize(goodDay().map((c, h) => cap(h, { reads: 40 }))).checks.reads, false);
  const unknown = summarize(goodDay().map((c, h) => (h === 2 ? cap(h, { noReadsField: true, status: 'partial', reason: 'no numbers here' }) : c)));
  assert.equal(unknown.checks.reads, false);
  assert.equal(unknown.reads.unknown, 1);
  assert.match(formatDay(unknown), /unknown/);
});

test('a desk whose counts go more than four hours without a reading fails the volume check', () => {
  const s = summarize(goodDay().map((c, h) => cap(h, { volume: h < 12 ? [] : DESKS.desks.filter((_, i) => i % 4 === h % 4).map((d) => d.id) })));
  assert.equal(s.checks.volume, false);
  assert.ok(s.volume.some((v) => !v.ok && v.max_gap_h > 4));
  const none = summarize(goodDay().map((c, h) => cap(h, { volume: [] })));
  assert.ok(none.volume.every((v) => v.readings === 0 && !v.ok));
});

test('a story-cited post left off the re-read list is counted, and only once it was known', () => {
  const s = summarize(goodDay().map((c, h) => (h === 9 ? cap(h, { watch: [CITED[0]] }) : c)));
  assert.equal(s.watch.max_left_out, 1);
  assert.equal(s.watch.worst_run, '2026-10-27T0905Z');
  assert.deepEqual(s.watch.left_out_ids, [CITED[1]]);
  assert.equal(s.checks.watch, false);
  // A post first recorded after the run cannot have been on its list.
  const later = summarize(goodDay().map((c, h) => (h === 9 ? cap(h, { watch: [CITED[0]] }) : c)), { ledger: { ...ledger, [CITED[1]]: { result: 'ok', first_run: '2026-10-27T1105Z' } } });
  assert.equal(later.watch.max_left_out, 0);
});

test('a day still in progress is judged on the hours that have run, not on 24', () => {
  const s = summarize(goodDay().slice(0, 6), { hoursInDay: 6 });
  assert.ok(s.desks.every((d) => d.ok), 'six good hours satisfy every cadence for six hours');
  assert.equal(s.reads.total, 180);
  assert.equal(s.checks.reads, false, 'the reads check is for a whole day');
  assert.equal(s.partial_day, true);
});
