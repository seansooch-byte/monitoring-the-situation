// The numbers the site shows, derived from captures. Words come from the editor; these never do.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { seriesByPost, magnitude, storyNumbers, deskTrace, trend, placesPerAccount } from '../tools/lib/metrics.mjs';

const H = 3600000;
const T = Date.parse('2026-10-08T00:00:00Z');
const iso = (ms) => new Date(ms).toISOString().replace('.000Z', 'Z');
const cap = (hour, rows) => ({ run: { finished_at: iso(T + hour * H) }, observations: rows.map(([id, views, state = 'live']) => ({ id, at: iso(T + hour * H), state, views, likes: null, reposts: null, quotes: null, replies: null, bookmarks: null, approx: false })) });

test('magnitude is the base ten log of views, to one decimal: ten million views is 7.0', () => {
  assert.equal(magnitude(10_000_000), 7.0);
  assert.equal(magnitude(1_000_000), 6.0);
  assert.equal(magnitude(39_400_000), 7.6);
  assert.equal(magnitude(0), null);
  assert.equal(magnitude(null), null);
});

test('readings for a post are joined across captures in time order', () => {
  const s = seriesByPost([cap(2, [['a', 300]]), cap(1, [['a', 100], ['b', 5]])]);
  assert.deepEqual(s.get('a').map((o) => o.views), [100, 300]);
  assert.equal(s.get('b').length, 1);
});

test('a story adds up the latest reading of each of its posts and counts the ones with no views', () => {
  const s = seriesByPost([cap(1, [['a', 1000], ['b', 500], ['c', null]]), cap(2, [['a', 4000], ['b', 900]])]);
  const n = storyNumbers(['a', 'b', 'c', 'never-seen'], s, T + 2 * H);
  assert.equal(n.views, 4900);
  assert.equal(n.magnitude, 3.7);
  assert.equal(n.unmeasured, 2);
  assert.equal(n.perHour, 3400); // (4000-1000) + (900-500) over the last hour
});

test('a deleted post keeps its last live reading and is reported as gone', () => {
  const s = seriesByPost([cap(1, [['a', 1000]]), cap(2, [['a', null, 'deleted']])]);
  const n = storyNumbers(['a'], s, T + 2 * H);
  assert.equal(n.views, 1000);
  assert.equal(n.gone, 1);
});

test('trend compares the last hour with the hour before it', () => {
  assert.equal(trend(5000, 1000), 'rising');
  assert.equal(trend(1000, 5000), 'fading');
  assert.equal(trend(1000, 1100), 'steady');
  assert.equal(trend(1000, null), 'new');
  assert.equal(trend(0, 0), 'still');
});

test('a desk trace spreads each gain in views over the time it happened in', () => {
  // one post: created at hour 0, 6000 views by hour 1, 6000 by hour 3 (flat after)
  const s = seriesByPost([cap(1, [['a', 6000]]), cap(3, [['a', 6000]])]);
  const tr = deskTrace([{ id: 'a', created: T }], s, { from: T, to: T + 4 * H, bins: 4 });
  assert.deepEqual(tr.map(Math.round), [6000, 0, 0, 0]); // views per hour in each one hour bin
});

test('a trace ignores a reading that goes backwards instead of drawing negative attention', () => {
  const s = seriesByPost([cap(1, [['a', 6000]]), cap(2, [['a', 5000]])]);
  const tr = deskTrace([{ id: 'a', created: T }], s, { from: T, to: T + 2 * H, bins: 2 });
  assert.deepEqual(tr.map(Math.round), [6000, 0]);
});

// ---- one account, one place: no account may fill a list that is meant to be every corner of the internet

test('an account keeps only its largest places in a ranked list, and the rest keep their order', () => {
  const ranked = [['a', 'loud', 900], ['b', 'quiet', 800], ['c', 'Loud', 700], ['d', 'other', 600], ['e', 'LOUD', 500]].map(([id, handle, views]) => ({ id, handle, views }));
  const one = placesPerAccount(ranked, 1, (it) => it.handle);
  assert.deepEqual(one.kept.map((it) => it.id), ['a', 'b', 'd'], 'the largest post of each account, largest first');
  assert.deepEqual(one.held.map((it) => it.id), ['c', 'e'], 'the rest are handed back, not lost');
  const two = placesPerAccount(ranked, 2, (it) => it.handle);
  assert.deepEqual(two.kept.map((it) => it.id), ['a', 'b', 'c', 'd']);
  assert.deepEqual(two.held.map((it) => it.id), ['e']);
});

test('a handle is one account however it is capitalised, and a list with no repeats is left alone', () => {
  const ranked = [{ id: 'a', handle: 'One' }, { id: 'b', handle: 'two' }];
  const out = placesPerAccount(ranked, 1, (it) => it.handle);
  assert.deepEqual(out.kept, ranked);
  assert.deepEqual(out.held, []);
  assert.deepEqual(placesPerAccount([], 1, (it) => it.handle), { kept: [], held: [] });
});
