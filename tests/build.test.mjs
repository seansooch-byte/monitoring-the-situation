// The build, end to end, on the invented fixture: every page is written, nothing invented is
// deployable, and the page carries no em dash.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { stripEdge } from '../tools/audit-live.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const run = (...args) => execFileSync('node', args, { cwd: root, encoding: 'utf8' });
const desks = JSON.parse(readFileSync(root + 'contract/desks.json', 'utf8')).desks;

test('the demo build writes the pulse page, a page per desk and a page per story, and marks itself', () => {
  run('tools/make-demo.mjs');
  const out = run('tools/build.mjs', '--demo');
  assert.match(out, /built DEMO site: \d+ on the pulse, 17 stories \(16 current\)/);
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  assert.ok(existsSync(root + 'dist/DEMO'), 'a demo build leaves a DEMO marker so it is never deployed');
  assert.match(home, /class="demo"/);
  assert.match(home, /name="robots" content="noindex"/);
  assert.match(home, /People live in different worlds/);
  for (const d of desks) {
    assert.ok(home.includes(`data-desk="${d.id}"`), `${d.id} has a line on the record`);
    assert.ok(existsSync(`${root}dist/desk/${d.id}/index.html`), `${d.id} has a page`);
  }
  // one invented story is more than 48 hours old: it keeps its page, leaves the bulletin, and is in the archive
  assert.equal(readdirSync(root + 'dist/story').length, 17);
  const all = readFileSync(root + 'dist/stories/index.html', 'utf8');
  assert.equal((all.match(/<li class="story"/g) ?? []).length, 16);
  assert.ok(!all.includes('lighthouse webcam') || all.includes('archive'), 'a story older than 48 hours is off the list of current stories');
  assert.equal((all.match(/<li class="story"[^>]*lighthouse/g) ?? []).length, 0);
  const archive = readFileSync(root + 'dist/archive/index.html', 'utf8');
  assert.ok(archive.includes('lighthouse webcam'), 'and listed in the archive');
  assert.ok(!archive.includes('A dog walks onto a live weather forecast'), 'which does not repeat the bulletin');
  assert.ok(!home.includes(String.fromCharCode(0x2014)), 'no em dash on the page');
  // every element the page script looks up by id exists in the markup
  const script = readFileSync(root + 'site/app.js', 'utf8');
  for (const [, id] of script.matchAll(/getElementById\('([^']+)'\)/g)) assert.ok(home.includes(`id="${id}"`), `#${id} exists`);
});

test('post text from X is escaped, never trusted as markup', () => {
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  assert.ok(!/<script(?![^>]*src="\/app\.js")/.test(home), 'the only script is the page script');
  // one invented reply carries "<3 &": it must reach the page escaped
  const story = readFileSync(root + 'dist/story/2026-10-08-dog-walks-onto-forecast/index.html', 'utf8');
  assert.ok(story.includes('rain &lt;3 &amp; he is right'), 'angle bracket and ampersand are escaped');
  assert.ok(!story.includes('rain <3 & he'), 'and never written raw');
});

test('the real build leaves no DEMO marker, and counts only posts X has confirmed', () => {
  const out = run('tools/build.mjs');
  assert.match(out, /^built site:/m);
  assert.ok(!existsSync(root + 'dist/DEMO'));
  assert.ok(!readFileSync(root + 'dist/index.html', 'utf8').includes('class="demo"'));
  const ledger = existsSync(root + 'verified/posts.json') ? JSON.parse(readFileSync(root + 'verified/posts.json', 'utf8')) : {};
  const ok = Object.values(ledger).filter((v) => v.result === 'ok').length;
  const pulse = JSON.parse(readFileSync(root + 'dist/data/pulse.json', 'utf8'));
  const counted = pulse.desks.reduce((n, d) => n + d.posts, 0);
  assert.ok(counted <= ok, `desks count ${counted} posts but X has confirmed only ${ok}`);
  const headers = readFileSync(root + 'dist/_headers', 'utf8');
  assert.match(headers, /Content-Security-Policy: default-src 'none'/);
  assert.match(headers, /X-Robots-Tag: noindex/);
});

test('the live audit removes only what Cloudflare adds, so a real difference still shows', () => {
  const page = '<body><p>x</p><script src="/app.js" defer></script></body>';
  const edge = '<script>(function(){var a;a.src=\'/cdn-cgi/challenge-platform/scripts/jsd/main.js\';})();</script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v4" data-cf-beacon=\'{}\'></script>';
  assert.equal(stripEdge(page.replace('</body>', edge + '</body>')), page);
  assert.notEqual(stripEdge(page.replace('<p>x</p>', '<p>y</p>')), page);
  assert.notEqual(stripEdge(page.replace('</body>', '<script>alert(1)</script></body>')), page);
});

// ---- Internet Pulse: the viral posts themselves, each passed and described by the editor

test('the demo build shows the pulse above the stories: one row per item, ranked by views, with the editor\'s line', () => {
  run('tools/make-demo.mjs');
  run('tools/build.mjs', '--demo');
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  const rows = [...home.matchAll(/<li class="pulse-item"[^>]*data-views="(\d+)"/g)].map((m) => Number(m[1]));
  assert.ok(rows.length >= 10, `expected at least ten pulse items, found ${rows.length}`);
  assert.deepEqual(rows, [...rows].sort((a, b) => b - a), 'largest first');
  assert.ok(home.indexOf('id="pulse"') < home.indexOf('id="stories"'), 'the pulse comes before the stories');
  assert.match(home, /class="pulse-line"/);
  assert.ok(existsSync(root + 'dist/stories/index.html'), 'the researched stories have their own page');
});

test('the build refuses a pulse item whose post is flagged as showing a private person or a minor', () => {
  run('tools/make-demo.mjs');
  const file = root + 'fixtures/demo/pulse/current.json';
  const pulse = JSON.parse(readFileSync(file, 'utf8'));
  const flagged = JSON.parse(readFileSync(root + 'fixtures/demo/FLAGGED_POST', 'utf8'));
  pulse.items.push({ id: flagged.id, desk: 'life', line: 'This post must never be shown.' });
  writeFileSync(file, JSON.stringify(pulse));
  assert.throws(() => run('tools/build.mjs', '--demo'), /flagged/);
  run('tools/make-demo.mjs');
});

test('the real pulse file is well formed: unique posts, a known desk and a line for each, no em dash', () => {
  const file = root + 'pulse/current.json';
  if (!existsSync(file)) return;
  const pulse = JSON.parse(readFileSync(file, 'utf8'));
  assert.equal(pulse.schema, 'mts.pulse/1');
  const ids = new Set();
  for (const it of pulse.items) {
    assert.match(it.id, /^\d{15,20}$/);
    assert.ok(!ids.has(it.id), `${it.id} is listed twice`); ids.add(it.id);
    assert.ok(desks.some((d) => d.id === it.desk), `${it.id}: unknown desk ${it.desk}`);
    assert.ok(typeof it.line === 'string' && it.line.length >= 20 && it.line.length <= 320, `${it.id}: a line of 20 to 320 characters`);
    assert.ok(!it.line.includes(String.fromCharCode(0x2014)), `${it.id}: no em dash`);
    for (const a of it.also ?? []) assert.match(a, /^\d{15,20}$/);
  }
});
