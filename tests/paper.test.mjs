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
    for (const href of ['/', '/newsletter/', '/pulse/', '/archive/', '/about/']) assert.ok(page.includes(`href="${href}"`), `${f} links ${href}`);
    assert.match(page, /<nav class="mode" aria-label="Read it as"><a href="\/"[^>]*>The Paper<\/a><a href="\/pulse\/"[^>]*>Internet Pulse<\/a><a href="\/newsletter\/"[^>]*>The Newsletter<\/a><\/nav>/, `${f} has the switch: the Paper, Internet Pulse, the Newsletter`);
    assert.ok(!/>The Wire</.test(page), `${f} no longer names the old wire`);
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

const pad = (t, n) => t + ' More words in the same plain voice.'.repeat(n);
// A letter for the demo's front day, citing its two largest stories (contract/NEWSLETTER.md).
function writeLetter(day, change = () => {}) {
  const ed = JSON.parse(read(`data/edition/${day}.json`));
  const [a, b] = ed.stories;
  assert.ok(a && b, 'CONTROL: the demo edition has two stories to cite');
  const letter = {
    schema: 'mts.letter/1', date: day, published: '2026-10-08', model: 'Demo Model',
    subject: 'What the invented day adds up to', summary: 'A test of the page, written by the test; nothing in it is true of any real day.',
    lead: { desk: a.desks[0], head: 'The lead', text: [pad('The largest story drew {reach} views on the day.', 20)], cites: ['first'] },
    notes: [
      { desk: 'tech', head: 'A note', text: pad('The second story moved too.', 6), cites: ['second'] },
      { desk: 'music', head: 'Another note', text: pad('And the first again, from elsewhere.', 6), cites: ['first'] },
    ],
    read: { text: [pad('What the day adds up to, in one call.', 8)], cites: ['first'] },
    sources: { first: { story: a.id }, second: { story: b.id } },
    figures: { reach: { value: '1.2M', of: 'views on the day', source: 'first' } },
  };
  if (letter.lead.desk === 'tech' || letter.lead.desk === 'music') letter.lead.desk = 'politics';
  change(letter);
  mkdirSync(root + 'fixtures/demo/newsletter', { recursive: true });
  writeFileSync(`${root}fixtures/demo/newsletter/${day}.json`, JSON.stringify(letter));
  return { ed, a, b };
}

test('the day\'s letter is a page of the Newsletter, with Harvard references, and the Paper prints its read', () => {
  fresh();
  const day = frontDay();
  const { a, b } = writeLetter(day);
  const out = run('tools/build.mjs', '--demo');
  assert.match(out, /1 with a letter/);
  const letter = read(`newsletter/${day}/index.html`);
  assert.match(letter, /<p class="l-dear">Dear reader,<\/p>/);
  assert.match(letter, /<p class="l-sig">Soochiebot<\/p>/, 'it is signed');
  assert.match(letter, /<a href="\/newsletter\/"[^>]*aria-current="page">The Newsletter<\/a>/, 'the switch shows where the reader is');
  // Harvard: one author twice in one year takes a and b, in the order of the list; the text cites by them.
  const refs = [...letter.matchAll(/<li id="ref-(\w+)">Monitoring the Situation \(\d{4}([ab])\) <i>([^<]+)<\/i>\. Available at: <a href="https:\/\/situation\.seansooch\.dev\/story\/([^/]+)\/">/g)];
  assert.equal(refs.length, 2, 'both stories are in the reference list');
  assert.deepEqual(refs.map((m) => m[2]), ['a', 'b']);
  assert.deepEqual(refs.map((m) => m[4]).sort(), [a.id, b.id].sort());
  assert.match(letter, /\(Accessed: 8 October 2026\)/, 'accessed on the day it was published');
  assert.match(letter, /<span class="cite">\(<a href="#ref-first">Monitoring the Situation, \d{4}[ab]<\/a>\)<\/span>/, 'the text cites by author and year');
  assert.match(letter, /<b class="fig">1\.2M<\/b>/, 'a figure is set in its place');
  const band = read(`edition/${day}/index.html`).split('id="newsletter"')[1].split('</section>')[0];
  assert.ok(band.includes('What the invented day adds up to') && band.includes(`href="/newsletter/${day}/"`), 'the Paper prints the read and links the letter');
  assert.ok(read('newsletter/index.html').includes('What the invented day adds up to'), 'the Newsletter opens on the latest letter');
  run('tools/make-demo.mjs');
});

test('a letter that breaks a rule stops the build and says why', () => {
  fresh();
  const day = frontDay();
  writeLetter(day, (l) => l.read.text.push('It drew 22.6M views.'));
  const r = spawnSync('node', ['tools/build.mjs', '--demo'], { cwd: root, encoding: 'utf8' });
  assert.notEqual(r.status, 0);
  assert.match(r.stderr, new RegExp(`newsletter/${day}\\.json does not meet contract/NEWSLETTER\\.md: .*22\\.6M`));
  run('tools/make-demo.mjs');
});

test('a day without a letter says so, and the Newsletter says when there is none yet', () => {
  fresh();
  assert.match(read('index.html'), /No letter for this day\./);
  assert.match(read('newsletter/index.html'), /The first letter has not been written\./);
  assert.ok(!existsSync(root + 'dist/opinion/index.html'), 'the opinion page is gone');
});
