// The read planner: the next run's read list, in order, with a budget line each, computed from
// the captures, the editor's requests, the desks and contract/budget.json. The cut order lives
// here now, where Sean can read it, and not in the grabber's judgement.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { planReads } from '../tools/lib/plan.mjs';

const root = new URL('..', import.meta.url);
const DESKS = JSON.parse(readFileSync(new URL('contract/desks.json', root), 'utf8'));
const BUDGET = JSON.parse(readFileSync(new URL('contract/budget.json', root), 'utf8'));
const H = 3600000;
const iso = (ms) => new Date(ms).toISOString().replace('.000Z', 'Z');
const runId = (ms) => iso(ms).replace(/:(\d\d):\d\dZ$/, '$1Z');

let seq = 0;
const newId = () => String(2115000000000000000n + BigInt(++seq));

// A capture at `startMs` whose observations give each post the views listed.
function cap(startMs, { obs = [], sweeps = [], volume = [], answers = [], reads = 30, reads_left = null, reason = null, posts = [] } = {}) {
  return {
    schema: 'mts.capture/1',
    run: { id: runId(startMs), started_at: iso(startMs), finished_at: iso(startMs + 4 * 60000), status: reason ? 'partial' : 'ok', reason, grabber: { agent: 'test', model: null, method: 'synthetic' }, requests_rev: null, reads, ...(reads_left == null ? {} : { reads_left }) },
    sweeps: sweeps.map((s) => (typeof s === 'string' ? { id: s, kind: s.split('.')[0], desk: null, method: 'x', window_hours: null, status: 'ok', reason: null, post_ids: [] } : s)),
    trends: [], posts, context: [],
    observations: obs.map(([id, views, state = 'live']) => ({ id, at: iso(startMs + 60000), state, views, likes: null, reposts: null, quotes: null, replies: null, bookmarks: null, approx: false })),
    answers: answers.map((request_id) => ({ request_id, status: 'ok', post_ids: [], note: null })),
    volume: volume.map((d) => ({ key: `desk.${d}`, desk: d, query: 'q', granularity: 'hour', points: [] })),
  };
}

// A typical night: the last capture ran at 03:05Z; we plan the 04Z run.
const T0 = Date.parse('2026-10-28T00:05:00Z');
const NOW = Date.parse('2026-10-28T03:40:00Z');
const hourlyDesks = DESKS.desks.filter((d) => d.sweep_every_hours === 1).map((d) => d.id);
const twoHour = DESKS.desks.filter((d) => d.sweep_every_hours === 2).map((d) => d.id);
const fourHour = DESKS.desks.filter((d) => d.sweep_every_hours === 4).map((d) => d.id);

function night() {
  seq = 0;                            // the same night every time it is asked for
  const watched = newId();            // in watch.json, old, still moving
  const fresh = newId();              // first seen 03:05, under 6 hours old
  const gaining = newId();            // first seen 12 hours before midnight, gaining 5 percent an hour
  const flat = newId();               // sixteen readings, no change: slowed
  const gone = newId();               // X no longer returns it
  const stale = newId();              // half a percent an hour: not gaining, not flat, so only every fourth hour
  const caps = [];
  for (let h = -20; h <= 3; h++) {
    const t = T0 + h * H;
    const obs = [];
    obs.push([watched, 1_000_000 + (h + 20) * 50_000]);
    if (h >= 3) obs.push([fresh, 200_000]);
    if (h >= -12) obs.push([gaining, Math.round(100_000 * Math.pow(1.05, h + 12))]);
    if (h >= -12) obs.push([flat, 5_000_000]);
    obs.push([gone, 10, h === 3 ? 'unavailable' : 'live']);
    if (h >= -12) obs.push([stale, Math.round(300_000 * (1 + 0.005 * (h + 12)))]);
    const sweeps = ['watch', ...hourlyDesks.map((d) => `desk.${d}`)];
    if ((h + 20) % 2 === 1) sweeps.push(`desk.${twoHour[0]}`);     // one two-hour desk kept to its cadence (last at 03:05); the rest never swept
    caps.push(cap(t, { obs, sweeps, reads: 21, reads_left: h === 3 ? 915 : null, volume: h === 3 ? [DESKS.desks[0].id] : [] }));
  }
  return { caps, ids: { watched, fresh, gaining, flat, gone, stale } };
}

const plan = (over = {}) => {
  const { caps, ids } = night();
  const p = planReads({ captures: caps, watchIds: [ids.watched], openRequests: [{ id: 'r-1', kind: 'search' }, { id: 'r-2', kind: 'lookup' }], answered: new Set(['r-1']), desks: DESKS, budget: BUDGET, now: NOW, ...over });
  return { p, ids };
};

test('the plan is for the next hour, in the day band, with the watch list first and inside the allowance', () => {
  const { p, ids } = plan();
  assert.equal(p.schema, 'mts.plan/1');
  assert.equal(p.for_run, '2026-10-28T04Z');
  assert.equal(p.band, 'day');
  assert.equal(p.allowance, 42);
  assert.ok(p.total_reads <= p.allowance, `${p.total_reads} reads inside ${p.allowance}`);
  assert.equal(p.items[0].sweep, 'watch');
  const watch = p.items[0];
  assert.equal(watch.ids[0], ids.watched, 'watch.json first');
  assert.equal(watch.ids[1], ids.fresh, 'then posts under six hours old');
  assert.equal(watch.ids[2], ids.gaining, 'then posts gaining at least 2 percent');
  assert.ok(!watch.ids.includes(ids.gone), 'a post X no longer returns is not re-read');
  assert.ok(watch.ids.indexOf(ids.stale) > watch.ids.indexOf(ids.gaining), '04Z is a fourth hour: the rest of the day follows the posts that are moving');
  assert.equal(watch.reads, 1);
  assert.equal(p.day.reads_left_before, 915);
  assert.equal(p.day.short, false);
  assert.equal(p.mode, 'normal');
  for (const it of p.items) assert.ok(Number.isInteger(it.reads) && it.reads >= 1, `${it.sweep} has a read count`);
});

test('a flat post is re-read every sixth run, and the plan says how many it slowed', () => {
  const { p, ids } = plan();
  const flatIn = p.items[0].ids.includes(ids.flat);
  assert.equal(p.left_out.rereads.slowed, flatIn ? 0 : 1);
  // Over six consecutive hours the flat post is read exactly once.
  let reads = 0;
  for (let k = 0; k < 6; k++) {
    const { caps } = night();
    const q = planReads({ captures: caps, watchIds: [ids.flat], openRequests: [], answered: new Set(), desks: DESKS, budget: BUDGET, now: NOW + k * H });
    if (q.items[0].ids.includes(ids.flat)) reads++;
  }
  assert.equal(reads, 1);
});

test('only a fourth hour re-reads the rest of the last 24 hours, slowest last', () => {
  const { caps, ids } = night();
  const base = { captures: caps, watchIds: [ids.watched], openRequests: [], answered: new Set(), desks: DESKS, budget: BUDGET };
  const five = planReads({ ...base, now: NOW + H });   // plans the 05Z run
  assert.equal(five.for_run, '2026-10-28T05Z');
  assert.ok(!five.items[0].ids.includes(ids.stale), 'a post neither fresh nor gaining waits for a fourth hour');
  assert.ok(five.items[0].ids.includes(ids.gaining));
  const eight = planReads({ ...base, now: NOW + 4 * H }); // plans the 08Z run
  assert.equal(eight.for_run, '2026-10-28T08Z');
  assert.ok(eight.items[0].ids.includes(ids.stale), 'the stale post is read on a fourth hour');
  assert.ok(eight.items[0].ids.indexOf(ids.stale) > eight.items[0].ids.indexOf(ids.gaining), 'after the posts that are moving');
});

test('desks are due by their cadence; counts go to the five stalest desks; only unanswered requests are asked', () => {
  const { p } = plan();
  const sweeps = p.items.map((i) => i.sweep);
  for (const d of hourlyDesks) assert.ok(sweeps.includes(`desk.${d}`), `${d} is hourly and due`);
  assert.ok(!sweeps.includes(`desk.${twoHour[0]}`), 'a two-hour desk swept an hour ago is not due');
  for (const d of twoHour.slice(1)) assert.ok(sweeps.includes(`desk.${d}`), `${d} was never swept and is due`);
  const vol = p.items.filter((i) => i.sweep.startsWith('volume.'));
  assert.equal(vol.length, BUDGET.volume.desks_per_run);
  assert.ok(!vol.some((i) => i.sweep === `volume.${DESKS.desks[0].id}`), 'the one desk counted an hour ago is not among the stalest five');
  assert.ok(sweeps.includes('request.r-2'));
  assert.ok(!sweeps.includes('request.r-1'), 'answered once, never asked again');
  const order = ['watch', 'desk.', 'volume.', 'request.', 'trends.us', 'trends.ww', 'sensors.', 'viral.global', 'rising.global', 'context.top', 'screen'];
  let last = -1;
  for (const s of sweeps) {
    const k = order.findIndex((o) => s === o || s.startsWith(o));
    assert.ok(k >= last, `${s} is out of order`);
    last = k;
  }
});

test('a short day lowers the allowance and cuts in the contract\'s order, never the watch list or the counts', () => {
  const { caps } = night();
  const base = { captures: caps, watchIds: [], openRequests: [], answered: new Set(), desks: DESKS, budget: BUDGET };
  // 20:00Z with 250 left: 100 may still be spent on 4 runs, under 30 a run, so the day is short.
  const late = caps.map((c) => ({ ...c, run: { ...c.run, reads_left: 250 } }));
  const p = planReads({ ...base, captures: late, now: Date.parse('2026-10-28T19:40:00Z') });
  assert.equal(p.day.short, true);
  assert.equal(p.allowance, 25);
  assert.ok(p.total_reads <= 25);
  const sweeps = p.items.map((i) => i.sweep);
  assert.equal(sweeps[0], 'watch');
  assert.equal(p.items.filter((i) => i.sweep.startsWith('volume.')).length, BUDGET.volume.desks_per_run, 'counts are never cut');
  assert.ok(!sweeps.includes('screen'), 'the screening reserve goes first');
  for (const d of fourHour) assert.ok(!sweeps.includes(`desk.${d}`), `four-hour desk ${d} is cut before any hourly desk`);
  assert.ok(p.cut.length > 0 && p.cut[0] === 'screen');
  // Nothing left for the day: the plan keeps the watch list and the counts and says it is over budget.
  const spent = caps.map((c) => ({ ...c, run: { ...c.run, reads_left: 120 } }));
  const q = planReads({ ...base, captures: spent, now: Date.parse('2026-10-28T19:40:00Z') });
  assert.equal(q.allowance, 0);
  assert.ok(q.items.every((i) => i.sweep === 'watch' || i.sweep.startsWith('volume.')));
  assert.equal(q.over_budget, true);
});

test('overnight the cap is 20 and the re-read list stops at 400', () => {
  const many = Array.from({ length: 450 }, () => newId());
  const extra = cap(T0 + 3 * H, { obs: many.map((id) => [id, 50_000]), reads: 21, reads_left: 900 });
  const p = planReads({ captures: [extra], watchIds: [], openRequests: [], answered: new Set(), desks: DESKS, budget: BUDGET, now: Date.parse('2026-10-28T07:40:00Z') });
  assert.equal(p.band, 'overnight');
  assert.equal(p.allowance, 20);
  assert.equal(p.items[0].ids.length, 400);
  assert.equal(p.items[0].reads, 4);
  assert.equal(p.left_out.rereads.over_cap, 50);
  assert.ok(p.total_reads <= 20);
});

test('reads left come from the field, else from the sentence, and a new UTC day starts from the full budget', () => {
  const { caps } = night();
  const said = caps.map((c) => ({ ...c, run: { ...c.run, reads_left: undefined, status: 'partial', reason: '21 X reads this run (936 to 915 left today), no 429 refusals' } }));
  for (const c of said) delete c.run.reads_left;
  assert.equal(planReads({ captures: said, watchIds: [], openRequests: [], answered: new Set(), desks: DESKS, budget: BUDGET, now: NOW }).day.reads_left_before, 915);
  const yesterday = caps.filter((c) => c.run.started_at < '2026-10-28');
  const p = planReads({ captures: yesterday, watchIds: [], openRequests: [], answered: new Set(), desks: DESKS, budget: BUDGET, now: NOW });
  assert.equal(p.day.reads_left_before, BUDGET.reads_per_day);
  assert.equal(p.day.hours_left, 20);
});

test('the same inputs give the same plan', () => {
  const a = plan().p;
  const b = plan().p;
  delete a.written_at; delete b.written_at;
  assert.deepEqual(a, b);
});
