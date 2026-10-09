// The build, end to end, on the invented fixture: every page is written, nothing invented is
// deployable, and the page carries no em dash.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const run = (...args) => execFileSync('node', args, { cwd: root, encoding: 'utf8' });
const desks = JSON.parse(readFileSync(root + 'contract/desks.json', 'utf8')).desks;

test('the demo build writes the pulse page, a page per desk and a page per story, and marks itself', () => {
  run('tools/make-demo.mjs');
  const out = run('tools/build.mjs', '--demo');
  assert.match(out, /built DEMO site: 16 stories/);
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  assert.ok(existsSync(root + 'dist/DEMO'), 'a demo build leaves a DEMO marker so it is never deployed');
  assert.match(home, /class="demo"/);
  assert.match(home, /name="robots" content="noindex"/);
  assert.match(home, /People live in different worlds/);
  for (const d of desks) {
    assert.ok(home.includes(`data-desk="${d.id}"`), `${d.id} has a line on the record`);
    assert.ok(existsSync(`${root}dist/desk/${d.id}/index.html`), `${d.id} has a page`);
  }
  assert.equal(readdirSync(root + 'dist/story').length, 16);
  assert.equal((home.match(/<li class="story"/g) ?? []).length, 16);
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

test('the real build leaves no DEMO marker', () => {
  const out = run('tools/build.mjs');
  assert.match(out, /^built site:/m);
  assert.ok(!existsSync(root + 'dist/DEMO'));
  assert.ok(!readFileSync(root + 'dist/index.html', 'utf8').includes('class="demo"'));
});
