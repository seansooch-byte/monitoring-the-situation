// The paper, Edition 3 "The Broadsheet": the front page is an edition (contract/PAPER.md), every day
// keeps its own, and every page wears the same head. Built from the demo fixture.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const run = (...args) => execFileSync('node', args, { cwd: root, encoding: 'utf8' });
const read = (rel) => readFileSync(root + 'dist/' + rel, 'utf8');
const groups = JSON.parse(readFileSync(root + 'contract/desks.json', 'utf8')).groups;
const html = () => readdirSync(root + 'dist', { recursive: true }).filter((f) => f.endsWith('.html'));

function fresh() {
  run('tools/make-demo.mjs');
  return run('tools/build.mjs', '--demo');
}
function frontDay() {
  const m = read('index.html').match(/<p class="folio"><span>Covering [^<]+<\/span>/);
  assert.ok(m, 'the front page has a dateline');
  const days = readdirSync(root + 'dist/data/edition').map((f) => f.replace('.json', '')).sort();
  return days.find((d) => JSON.parse(read(`data/edition/${d}.json`)).edition.label && m[0].includes(JSON.parse(read(`data/edition/${d}.json`)).edition.label));
}

test('the front page is an edition: its lead, its briefing and its order are the edition\'s', () => {
  const out = fresh();
  assert.match(out, /built paper: \d+ editions, front page \d{4}-\d\d-\d\d/);
  const day = frontDay();
  assert.ok(day, 'the front page is one of the editions');
  const ed = JSON.parse(read(`data/edition/${day}.json`));
  const home = read('index.html');
  assert.ok(ed.lead, 'CONTROL: the demo edition has a lead');
  assert.match(home, new RegExp(`<h2 class="lead-h"><a href="/story/${ed.lead}/">`), 'the lead is the edition\'s');
  const brief = [...home.split('id="brief-h"')[1].split('</section>')[0].matchAll(/<li><a href="([^"]+)">/g)].map((m) => m[1]);
  assert.deepEqual(brief, ed.briefing.map((id, i) => (i ? `/story/${id}/` : '#lead')), 'the day in sixty seconds is the briefing, in order');
  assert.equal((home.match(/<h1[\s>]/g) ?? []).length, 1, 'one h1: the nameplate');
  assert.match(home, /<h1 class="plate">/);
  assert.equal(read(`edition/${day}/index.html`).includes(`href="/story/${ed.lead}/"`), true, 'the day keeps its own front page');
  for (const e of readdirSync(root + 'dist/data/edition')) assert.ok(existsSync(`${root}dist/edition/${e.replace('.json', '')}/index.html`), `${e} has a page`);
});

test('every page wears the same head: the nameplate, the motto, the sections, the as-of time', () => {
  fresh();
  const pinned = JSON.parse(readFileSync(root + 'site.json', 'utf8')).pinned.text;
  for (const f of html()) {
    const page = read(f);
    assert.match(page, /class="plate-name">Monitoring the Situation</, `${f} has the nameplate`);
    assert.ok(page.includes(pinned), `${f} carries the pinned post as its motto`);
    for (const g of groups) assert.ok(page.includes(`href="/section/${g.id}/"`), `${f} links the ${g.name} section`);
    for (const href of ['/', '/opinion/', '/pulse/', '/archive/', '/about/']) assert.ok(page.includes(`href="${href}"`), `${f} links ${href}`);
    assert.match(page, /<time id="asof" datetime="[^"]+Z">/, `${f} says when the record was read`);
    assert.ok(!page.includes(String.fromCharCode(0x2014)), `${f} has no em dash`);
    assert.ok(!/<script(?![^>]*src="\/app\.js")/.test(page), `${f}: the only script is the page script`);
  }
  assert.match(read('section/news/index.html'), /<a href="\/section\/news\/" aria-current="page">/, 'a section page marks itself in the bar');
});

test('six section pages, each with its desks and its share of the day', () => {
  fresh();
  const desks = JSON.parse(readFileSync(root + 'contract/desks.json', 'utf8')).desks;
  for (const g of groups) {
    const page = read(`section/${g.id}/index.html`);
    for (const d of desks.filter((x) => x.group === g.id)) assert.ok(page.includes(`href="/desk/${d.id}/"`), `${g.id} links its desk ${d.id}`);
    assert.match(page, /Share of the day/);
  }
});

const PLAIN = 'The record has one story above the rest, and the rest of the day follows from it. ';
function writeOpinion(day, over = {}) {
  const ed = JSON.parse(read(`data/edition/${day}.json`));
  mkdirSync(root + 'fixtures/demo/opinion', { recursive: true });
  const op = { schema: 'mts.opinion/1', date: day, published: '2026-10-08', model: 'Demo Model', head: 'What the invented day adds up to',
    text: [PLAIN.repeat(8), 'It is a test of the page, written by the test, and it says nothing true about any real day.'], cites: [ed.lead], ...over };
  writeFileSync(`${root}fixtures/demo/opinion/${day}.json`, JSON.stringify(op));
  return ed;
}

test('the day\'s opinion rides in its edition, labelled, with links to what it rests on', () => {
  fresh();
  const day = frontDay();
  const ed = writeOpinion(day);
  const out = run('tools/build.mjs', '--demo');
  assert.match(out, /1 with an opinion/);
  const home = read('index.html');
  const op = home.split('id="opinion"')[1].split('</section>')[0];
  assert.ok(op.includes('What the invented day adds up to'));
  assert.ok(op.includes(`href="/story/${ed.lead}/"`), 'it links the story it cites');
  assert.match(op, /Soochiebot \(Demo Model\)/, 'and says a program wrote it');
  assert.ok(read('opinion/index.html').includes(`href="/edition/${day}/#opinion"`), 'the opinion page lists it');
  run('tools/make-demo.mjs');
});

test('an opinion that breaks a rule stops the build and says why', () => {
  fresh();
  const day = frontDay();
  writeOpinion(day, { text: ['It drew 22.6M views. ' + PLAIN.repeat(8)] });
  const r = spawnSync('node', ['tools/build.mjs', '--demo'], { cwd: root, encoding: 'utf8' });
  assert.notEqual(r.status, 0);
  assert.match(r.stderr, new RegExp(`opinion/${day}\\.json does not meet contract/PAPER\\.md: .*22\\.6M`));
  run('tools/make-demo.mjs');
});

test('a day without an opinion says so, and a day without a story says so', () => {
  fresh();
  assert.match(read('index.html'), /No editorial for this day\./);
  assert.match(read('opinion/index.html'), /The first editorial has not been published\./);
});
