// Phase 1's done test (PROGRAM.md), against the live store. It runs only when asked
// (MTS_LIVE=1, with a token), so the ordinary suite stays offline:
//
//   npm run store-test
//
// Three checks: a post X stopped returning has no words anywhere in the store and was purged
// within 24 hours of the check that found it; the newest run in the store is the newest capture
// in git, byte for byte apart from purged records; and, once the record has left git, no
// capture text is tracked there.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { storeClient, storeToken } from '../tools/lib/store.mjs';

const REPO = fileURLToPath(new URL('..', import.meta.url));
const live = process.env.MTS_LIVE && storeToken() ? storeClient() : null;
const skip = live ? false : 'set MTS_LIVE=1 with a store token to run against the live store';
const chunks = (a, n) => Array.from({ length: Math.ceil(a.length / n) }, (_, i) => a.slice(i * n, i * n + n));
const fileOf = (runId) => join(REPO, 'capture', runId.slice(0, 4), runId.slice(5, 7), runId.slice(8, 10), `${runId.slice(11, 15)}Z.json`);
const H = 3600000;

test('a post X stopped returning has no words anywhere in the store, and was purged within 24 hours of the check', { skip }, async () => {
  const { checks } = await live.get('/api/checks?result=missing&limit=2000');
  const ids = Object.keys(checks);
  for (const batch of chunks(ids, 100)) {
    const { posts } = await live.get(`/api/posts?ids=${batch.join(',')}`);
    assert.equal(posts.length, batch.length);
    for (const p of posts) {
      assert.equal(p.text, '', `${p.id} has no words`);
      assert.equal(p.author.name, '', `${p.id} has no display name`);
      assert.deepEqual(p.media, [], `${p.id} has no media`);
      assert.equal(p.url, '', `${p.id} has no link`);
      assert.ok(p.purged_at, `${p.id} records when it was purged`);
      assert.ok(p.author.handle && p.first_run, `${p.id} keeps its handle and its first run`);
    }
  }
  // The files that hold the record, for the newest few: stripped too.
  for (const id of ids.slice(0, 5)) {
    const one = await live.get(`/api/post/${id}`);
    assert.ok(one.observations.n >= 1, `${id} keeps its numbers`);
    for (const run of one.runs) {
      const doc = await live.get(`/api/capture/${run}`);
      const rec = doc.posts.find((p) => p.id === id);
      assert.ok(rec, `${id} is still a record in ${run}`);
      assert.equal(rec.text, '', `${id} has no words in the file ${run}`);
      assert.ok(rec.purged_at, `${id} is marked purged in the file ${run}`);
    }
    assert.ok(Date.parse(one.check.purged_at) - Date.parse(one.check.checked_at) <= 24 * H, `${id} was purged within 24 hours of the check that found it`);
  }
});

test('the newest run in the store is its capture in git, byte for byte apart from purged records', { skip }, async () => {
  const { runs } = await live.get('/api/runs?limit=1');
  const id = runs[0].id;
  const file = fileOf(id);
  assert.ok(existsSync(file), `git still holds ${id} (until the cutover)`);
  const mine = JSON.parse(readFileSync(file, 'utf8'));
  const theirs = await live.get(`/api/capture/${id}`);
  const purged = new Set(theirs.posts.filter((p) => p.purged_at).map((p) => p.id));
  assert.deepEqual({ ...theirs, posts: theirs.posts.filter((p) => !purged.has(p.id)) }, { ...mine, posts: mine.posts.filter((p) => !purged.has(p.id)) });
  assert.deepEqual(theirs.observations, mine.observations, 'numbers are never purged');
});

test('once the record has left git, no capture text is tracked there', { skip }, () => {
  const tracked = execFileSync('git', ['ls-files', 'capture/2026'], { cwd: REPO, encoding: 'utf8' }).trim();
  if (tracked) { console.log('  (git still tracks capture files; this check applies after the cutover)'); return; }
  const hits = execFileSync('git', ['grep', '-l', '"text":', 'HEAD', '--', 'capture'], { cwd: REPO, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
  assert.equal(hits, '');
});
