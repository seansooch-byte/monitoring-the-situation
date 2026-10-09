// The site's clock: every time a reader sees is Eastern time. These are fixed instants with the
// answer written out by hand, so the test cannot agree with the code by sharing its arithmetic.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { ZONE_LABEL, clockTime, dateOf, dayOf } from '../tools/lib/clock.mjs';

const at = (iso) => Date.parse(iso);

test('the label is ET, which is right in summer and in winter', () => {
  assert.equal(ZONE_LABEL, 'ET');
});

test('in October the clock is four hours behind UTC', () => {
  assert.equal(clockTime(at('2026-10-09T08:12:00Z')), '04:12');
  assert.equal(dayOf(at('2026-10-09T08:12:00Z')), 'Fri 9 Oct 2026');
});

test('in December it is five hours behind, and an early UTC hour is still the evening before', () => {
  assert.equal(clockTime(at('2026-12-01T03:30:00Z')), '22:30');
  assert.equal(dayOf(at('2026-12-01T03:30:00Z')), 'Mon 30 Nov 2026');
  assert.equal(dateOf(at('2026-12-01T03:30:00Z')), '30 Nov 2026');
});

test('midnight is 00:00, never 24:00, and the date turns over with it', () => {
  assert.equal(clockTime(at('2026-10-09T04:00:00Z')), '00:00');
  assert.equal(dayOf(at('2026-10-09T03:59:00Z')), 'Thu 8 Oct 2026');
  assert.equal(dayOf(at('2026-10-09T04:00:00Z')), 'Fri 9 Oct 2026');
});

test('the hour that repeats when the clocks go back reads the same both times', () => {
  // 1 November 2026: 01:30 happens twice in New York, an hour apart.
  assert.equal(clockTime(at('2026-11-01T05:30:00Z')), '01:30');
  assert.equal(clockTime(at('2026-11-01T06:30:00Z')), '01:30');
  assert.equal(clockTime(at('2026-11-01T07:30:00Z')), '02:30');
});

test('the pinned post keeps its date', () => {
  assert.equal(dateOf(at('2026-02-20T18:41:56Z')), '20 Feb 2026');
});
