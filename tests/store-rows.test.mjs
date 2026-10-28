// The store's rows: how a capture becomes rows in D1, and how a post X no longer returns is
// purged from the record. Pure functions; the Worker calls them and so do these tests.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { rowsOf, purgedRecord, stripCapture, PURGED_FIELDS } from '../tools/lib/store-rows.mjs';

const root = new URL('..', import.meta.url);
const example = JSON.parse(readFileSync(new URL('contract/example.capture.json', root), 'utf8'));
const RECEIVED = '2026-10-09T06:10:00Z';

test('every array of a capture becomes rows, keyed so a second delivery of the same run changes nothing', () => {
  const r = rowsOf(example, RECEIVED);
  assert.equal(r.run.id, example.run.id);
  assert.equal(r.run.received_at, RECEIVED);
  assert.equal(r.run.source, 'x');
  assert.equal(r.posts.length, example.posts.length);
  assert.equal(r.observations.length, example.observations.length);
  assert.equal(r.sweeps.length, example.sweeps.length);
  assert.equal(r.answers.length, (example.answers ?? []).length);
  assert.equal(r.post_runs.length, example.posts.length, 'one row per record per run, so a purge can find every file a record is in');
  for (const p of r.posts) {
    assert.equal(typeof p.media, 'string', 'nested fields are stored as JSON text');
    assert.equal(p.first_run, example.run.id);
    assert.equal(p.source, 'x');
  }
  for (const o of r.observations) { assert.equal(o.run_id, example.run.id); assert.ok(o.post_id && o.at); }
  const points = r.volume_points;
  const series = example.volume ?? [];
  assert.equal(points.length, series.reduce((n, v) => n + v.points.length, 0));
  for (const pt of points) assert.ok(pt.key && pt.start && Number.isInteger(pt.count));
  assert.equal(new Set(points.map((pt) => `${pt.key}|${pt.start}`)).size, points.length, 'one point per key and hour');
});

test('a purged record keeps its id, its handle, its desk and its numbers, and loses its words, name, media and link', () => {
  const post = example.posts[0];
  const p = purgedRecord(post, '2026-10-28T05:00:00Z');
  assert.equal(p.id, post.id);
  assert.equal(p.author.handle, post.author.handle);
  assert.equal(p.desk, post.desk);
  assert.equal(p.flags.length, post.flags.length);
  assert.equal(p.text, '');
  assert.equal(p.author.name, '');
  assert.deepEqual(p.media, []);
  assert.equal(p.url, '');
  assert.equal(p.note, null);
  assert.equal(p.lead, null);
  assert.equal(p.purged_at, '2026-10-28T05:00:00Z');
  for (const f of PURGED_FIELDS) assert.ok(f in p, `${f} is still a field, emptied`);
  assert.deepEqual(purgedRecord(p, '2026-10-28T06:00:00Z').purged_at, '2026-10-28T05:00:00Z', 'the first purge time stays');
});

test('stripping a capture purges only the named records and leaves their observations', () => {
  const id = example.posts[0].id;
  const doc = stripCapture(example, new Set([id]), '2026-10-28T05:00:00Z');
  const stripped = doc.posts.find((p) => p.id === id);
  assert.equal(stripped.text, '');
  assert.equal(stripped.purged_at, '2026-10-28T05:00:00Z');
  for (const p of doc.posts) if (p.id !== id) assert.equal(p.text, example.posts.find((q) => q.id === p.id).text);
  assert.equal(doc.observations.length, example.observations.length);
  assert.equal(example.posts.find((p) => p.id === id).text !== '', true, 'the input is not changed');
});
