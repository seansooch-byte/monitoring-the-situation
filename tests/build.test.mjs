// The build, end to end, on the invented fixture: every page is written, nothing invented is
// deployable, and the page carries no em dash.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
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
    assert.ok(home.includes(`data-desk="${d.id}"`), `${d.id} has a card on the front page`);
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
  // The record holds posts filed under a desk that was later retired. They feed no total: the
  // desks the site reports are the desks watched now, and nothing else.
  assert.deepEqual(pulse.desks.map((d) => d.id), desks.map((d) => d.id));
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
  // The largest post leads the page on its own; the rest follow in one list, still largest first.
  const lead = home.match(/<section class="lead"[^>]*data-views="(\d+)"/);
  assert.ok(lead, 'the largest post leads the page');
  const rows = [...home.matchAll(/<li class="it"[^>]*data-views="(\d+)"/g)].map((m) => Number(m[1]));
  assert.ok(rows.length >= 9, `expected at least nine pulse items after the lead, found ${rows.length}`);
  assert.deepEqual([Number(lead[1]), ...rows], [Number(lead[1]), ...rows].sort((a, b) => b - a), 'largest first');
  assert.ok(home.indexOf('class="lead"') < home.indexOf('id="pulse"'), 'the lead comes before the list');
  assert.ok(home.indexOf('id="pulse"') < home.indexOf('id="stories"'), 'the pulse comes before the stories');
  assert.match(home, /class="line"/);
  assert.ok(existsSync(root + 'dist/stories/index.html'), 'the researched stories have their own page');
});

// ---- Edition 2: the page as drawn. These pin what the stylesheet and the page script rely on.

test('every desk has a card on the front page with one bar for each of the last 24 hours', () => {
  run('tools/make-demo.mjs');
  run('tools/build.mjs', '--demo');
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  for (const d of desks) {
    const card = home.match(new RegExp(`<button type="button" class="dk" data-desk="${d.id}"[\\s\\S]*?</button>`));
    assert.ok(card, `${d.id} has a card that can be picked`);
    assert.equal((card[0].match(/<i /g) ?? []).length, 24, `${d.id} shows 24 hourly bars`);
    assert.ok(card[0].includes(d.name.replace(/&/g, '&amp;')), `${d.id} is named in full`);
  }
});

test('the pulse list is tiered by position, so its only children are the items themselves', () => {
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  const list = home.match(/<ol class="pg" id="pulse-list">([\s\S]*?)<\/ol>/);
  assert.ok(list, 'the pulse list exists');
  const kids = list[1].split(/<\/li>\s*/).filter((s) => s.trim());
  assert.ok(kids.length >= 9);
  for (const k of kids) assert.match(k.trimStart(), /^<li class="it" id="p-\d+" data-views="\d+" data-pace="\d+" data-start="\d+" data-desks="[a-z]*">/, 'each child is one sortable item');
});

test('a post on the pulse keeps its related posts and its link to X', () => {
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  const fixture = JSON.parse(readFileSync(root + 'fixtures/demo/pulse/current.json', 'utf8'));
  const withRelated = fixture.items.filter((it) => (it.also ?? []).length).length;
  assert.ok(withRelated > 0, 'the fixture has related posts to show');
  // The lead shows its related posts in the open; every other item keeps them behind a disclosure.
  const shown = (home.match(/<details class="more">/g) ?? []).length + (home.includes('<div class="rel">') ? 1 : 0);
  assert.equal(shown, withRelated);
  for (const it of fixture.items) assert.ok(home.includes(`/status/${it.id}"`), `${it.id} links to the post on X`);
});

test('the page script only reaches for what the pages have, and the stylesheet is whole', () => {
  const pages = readFileSync(root + 'dist/index.html', 'utf8') + readFileSync(root + 'dist/stories/index.html', 'utf8');
  const script = readFileSync(root + 'site/app.js', 'utf8');
  const classes = new Set();
  // The script asks through querySelector or through its own all() helper; both are read here.
  for (const [, sel] of script.matchAll(/(?:querySelector(?:All)?|\ball)\('([^']+)'\)/g)) for (const [, c] of sel.matchAll(/\.([a-z][\w-]*)/g)) classes.add(c);
  assert.ok(classes.size >= 3, 'the script looks things up by class');
  for (const c of classes) assert.match(pages, new RegExp(`class="(?:[^"]* )?${c}(?: [^"]*)?"`), `.${c} exists in the markup`);
  const css = readFileSync(root + 'site/styles.css', 'utf8');
  assert.equal((css.match(/{/g) ?? []).length, (css.match(/}/g) ?? []).length, 'every rule is closed');
  assert.equal((css.match(/\/\*/g) ?? []).length, (css.match(/\*\//g) ?? []).length, 'every comment is closed');
  // One family is loaded, so the stylesheet may name no other web font.
  assert.match(pages, /fonts\.googleapis\.com\/css2\?family=Schibsted\+Grotesk/);
  for (const old of ['B612', 'STIX Two', 'Libre Franklin']) assert.ok(!css.includes(old) && !pages.includes(old.replace(/ /g, '+')), `${old} is gone`);
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

test('every time a reader sees is Eastern time, and the machine-readable stamps stay in UTC', () => {
  run('tools/make-demo.mjs');
  run('tools/build.mjs', '--demo');
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  const story = readFileSync(root + 'dist/story/2026-10-08-dog-walks-onto-forecast/index.html', 'utf8');
  const stories = readFileSync(root + 'dist/stories/index.html', 'utf8');
  // what a reader sees: the text of the pages, with the markup taken out
  const seen = (home + story + stories).replace(/<[^>]*>/g, ' ');
  assert.ok(!/\bUTC\b/.test(seen), 'no time on the page is labelled UTC');
  const asof = home.match(/<time id="asof" datetime="([^"]+)">(\d\d:\d\d) ET · [A-Z][a-z]{2} \d{1,2} [A-Z][a-z]{2} \d{4}<\/time>/);
  assert.ok(asof, 'the as-of time reads HH:MM ET, then the day');
  assert.match(asof[1], /^\d{4}-\d\d-\d\dT[\d:.]+Z$/, 'and its datetime attribute is still the instant in UTC');
  assert.notEqual(asof[2], asof[1].slice(11, 16), 'the words are not the UTC clock');
  assert.match(home, /<time datetime="[^"]+Z">\d\d:\d\d ET<\/time>/, 'a post gives its time in ET');
  assert.match(stories, /began \d\d:\d\d ET, /);
  assert.match(story, /Written up \d\d:\d\d ET, /);
});

test('a pulse of nothing, and a pulse of one, still build a whole front page', () => {
  run('tools/make-demo.mjs');
  const file = root + 'fixtures/demo/pulse/current.json';
  const pulse = JSON.parse(readFileSync(file, 'utf8'));
  // nothing passed yet: no lead, and the list says so instead of standing empty
  writeFileSync(file, JSON.stringify({ ...pulse, items: [] }));
  run('tools/build.mjs', '--demo');
  let home = readFileSync(root + 'dist/index.html', 'utf8');
  assert.ok(!home.includes('class="lead"') && !home.includes('<ol class="pg"'));
  assert.match(home, /The first pulse is being read\./);
  for (const d of desks) assert.ok(home.includes(`data-desk="${d.id}"`), `${d.id} still has its card`);
  // one post: it leads, and no empty list follows it
  writeFileSync(file, JSON.stringify({ ...pulse, items: pulse.items.slice(0, 1) }));
  run('tools/build.mjs', '--demo');
  home = readFileSync(root + 'dist/index.html', 'utf8');
  assert.ok(home.includes('class="lead"') && !home.includes('id="pulse"') && home.includes('id="stories"'));
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

// ---- one account, one place; and the desks the pages count are the desks in the list

const captureFiles = (dir, out = []) => {
  for (const name of readdirSync(dir, { withFileTypes: true })) {
    if (name.isDirectory()) captureFiles(`${dir}/${name.name}`, out);
    else if (/^\d{4}Z\.json$/.test(name.name)) out.push(`${dir}/${name.name}`);
  }
  return out;
};

test('no account holds more than one place in a list: its largest post stays, and a post held off the front still stands on its own desk', () => {
  run('tools/make-demo.mjs');
  run('tools/build.mjs', '--demo');
  const before = JSON.parse(readFileSync(root + 'dist/data/pulse.json', 'utf8')).pulse;
  assert.ok(before.length >= 6, 'the fixture has a pulse to cut');
  assert.deepEqual(before.map((it) => it.views), before.map((it) => it.views).sort((a, b) => b - a), 'and it is ranked largest first');
  // Hand three of its posts to one account, written three ways, as X handles ignore case:
  // its largest, a smaller one on the same desk, and a smaller one on another desk.
  const a = before.find((it, i) => before.slice(i + 1).some((x) => x.desk === it.desk));
  const rest = a ? before.slice(before.indexOf(a) + 1) : [];
  const b = rest.find((it) => it.desk === a.desk);
  const c = rest.find((it) => it.desk !== a.desk);
  assert.ok(a && b && c, 'the fixture has two posts on one desk and a smaller one on another');
  const same = [a, b, c];
  const handles = ['demo_loud', 'Demo_Loud', 'DEMO_LOUD'];
  for (const f of captureFiles(root + 'fixtures/demo/capture')) {
    const doc = JSON.parse(readFileSync(f, 'utf8'));
    let changed = false;
    for (const p of doc.posts) {
      const i = same.findIndex((it) => it.id === p.id);
      if (i < 0) continue;
      p.author.handle = handles[i]; p.url = `https://x.com/${handles[i]}/status/${p.id}`; changed = true;
    }
    if (changed) writeFileSync(f, JSON.stringify(doc));
  }
  const out = run('tools/build.mjs', '--demo');
  const after = JSON.parse(readFileSync(root + 'dist/data/pulse.json', 'utf8')).pulse.map((it) => it.id);
  const gone = [b.id, c.id];
  assert.deepEqual(after, before.map((it) => it.id).filter((id) => !gone.includes(id)), 'only that account\'s two smaller posts are gone, and everything else holds its order');
  const home = readFileSync(root + 'dist/index.html', 'utf8');
  assert.ok(home.includes(`id="p-${a.id}"`), 'its largest post is on the front page');
  for (const id of gone) assert.ok(!home.includes(`id="p-${id}"`) && !home.includes(`/status/${id}"`), `${id} is not on the front page`);
  assert.match(out, /held back 2 posts.*demo_loud/i, 'and the build names the account and the count');
  // Each desk's own list is cut the same way, from everything passed for that desk.
  const own = readFileSync(`${root}dist/desk/${a.desk}/index.html`, 'utf8');
  assert.ok(own.includes(`id="p-${a.id}"`) && !own.includes(`id="p-${b.id}"`), 'on its own desk the account still holds one place');
  const other = readFileSync(`${root}dist/desk/${c.desk}/index.html`, 'utf8');
  assert.ok(other.includes(`id="p-${c.id}"`), 'the post held off the front is the account\'s one place on its own desk');
  assert.ok(!other.includes('Nothing from this desk is on the pulse') , 'so that desk is not reported empty');
  assert.match(readFileSync(root + 'dist/about/index.html', 'utf8'), /No account holds more than one place/, 'the about page states the rule');
  run('tools/make-demo.mjs');
});

test('a page that says how many desks there are takes the number from the list', () => {
  run('tools/make-demo.mjs');
  run('tools/build.mjs', '--demo');
  const WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'];
  const right = [WORDS[desks.length] ?? String(desks.length), String(desks.length)];
  const said = [];
  for (const f of ['index.html', 'desks/index.html', 'about/index.html']) {
    for (const [, n] of readFileSync(root + 'dist/' + f, 'utf8').matchAll(new RegExp(`\\b(${WORDS.join('|')}|\\d+) desks\\b`, 'gi'))) said.push(n.toLowerCase());
  }
  assert.ok(said.length >= 5, `the pages state the number of desks in at least five places, found ${said.length}`);
  for (const n of said) assert.ok(right.includes(n), `a page says "${n} desks" but the list has ${desks.length}`);
  // site.json writes the number as {desks}: the site's own words carry it, and no page shows the placeholder.
  assert.ok(readFileSync(root + 'dist/about/index.html', 'utf8').includes(`${right[0]} desks from politics`), 'the purpose gives the number in words');
  for (const f of readdirSync(root + 'dist', { recursive: true }).filter((f) => f.endsWith('.html'))) assert.ok(!readFileSync(root + 'dist/' + f, 'utf8').includes('{desks}'), `${f} shows no placeholder`);
  assert.ok(!existsSync(root + 'dist/desk/crypto/index.html'), 'a retired desk has no page');
  assert.ok(!readFileSync(root + 'dist/index.html', 'utf8').includes('data-desk="crypto"'), 'and no card');
});

// ---- what X said decides what is shown, and only a mismatch stops the build
//
// The demo build checks nothing against X unless it is given a ledger (MTS_LEDGER). These tests
// give it one in which every fixture post is confirmed, then change one answer at a time.

const fixtureRecords = () => {
  const out = new Map();
  for (const f of captureFiles(root + 'fixtures/demo/capture')) for (const p of JSON.parse(readFileSync(f, 'utf8')).posts) out.set(p.id, p);
  return out;
};
const story = (id) => JSON.parse(readFileSync(`${root}fixtures/demo/moments/${id}.json`, 'utf8'));
// Build the demo against a ledger: every fixture post ok, then `over` (a result, or null to leave
// the post out of the ledger). `edit` may change the fixture first.
function buildWith(over, edit = () => {}) {
  run('tools/make-demo.mjs');
  edit();
  const ledger = {};
  for (const id of fixtureRecords().keys()) ledger[id] = { result: 'ok', detail: null };
  for (const [id, result] of Object.entries(over)) {
    if (result == null) delete ledger[id];
    else ledger[id] = { result, detail: result === 'mismatch' ? 'text: the record begins "a", X begins "b"' : null };
  }
  const dir = mkdtempSync(join(tmpdir(), 'mts-ledger-'));
  writeFileSync(join(dir, 'posts.json'), JSON.stringify(ledger));
  const r = spawnSync('node', ['tools/build.mjs', '--demo'], { cwd: root, encoding: 'utf8', env: { ...process.env, MTS_LEDGER: join(dir, 'posts.json') } });
  rmSync(dir, { recursive: true, force: true });
  return r;
}
const read = (rel) => readFileSync(root + 'dist/' + rel, 'utf8');
const escHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
// Nothing the grabber recorded about a post reaches the page: not its words, its link or its author.
function assertNothingOf(page, rec) {
  assert.ok(!page.includes(rec.url), `${rec.id}: its link from the record is not on the page`);
  assert.ok(!page.includes(escHtml(rec.text.split('\n')[0].slice(0, 40))), `${rec.id}: its words are not on the page`);
  assert.ok(!new RegExp(`@${rec.author.handle}[ <]`).test(page), `${rec.id}: its author is not on the page`);
}

const S = '2026-10-08-calendar-typo-moves-yields'; // three posts; worlds on the first two; its origin is on the pulse

test('a cited post X withholds is shown as unavailable, the build says so, and the rest of the site is built', () => {
  const pid = story(S).posts[0].id, rec = fixtureRecords().get(pid);
  const r = buildWith({ [pid]: 'withheld' });
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stdout, /built DEMO site: \d+ on the pulse, 17 stories/);
  assert.ok(r.stderr.includes(`warning: story ${S} cites post ${pid}, withheld by X`), r.stderr);
  const page = read(`story/${S}/index.html`);
  assert.match(page, /data-unavailable="withheld">\s*<p class="post-note"><span class="lab">Unavailable on X<\/span> X will not show this post without a login/);
  assert.ok(page.includes(`href="https://x.com/i/status/${pid}"`), 'a withheld post keeps a link by its id');
  assertNothingOf(page, rec);
  // The world it carried keeps its description, with the note in place of the post.
  const world = page.match(/<div class="world">[\s\S]*?<\/figure><\/div>/)[0];
  assert.ok(world.includes(escHtml(story(S).worlds[0].sees)) && world.includes('data-unavailable="withheld"'));
  assert.match(page, /<dt class="lab">Posts tracked<\/dt><dd>2<\/dd>/, 'and it counts for nothing');
  assertNothingOf(read('index.html'), rec);
  assertNothingOf(read('stories/index.html'), rec);
});

test('a cited post X has no answer for is shown as unavailable, with no link', () => {
  const pid = story(S).posts[2].id;
  const r = buildWith({ [pid]: 'missing' });
  assert.equal(r.status, 0, r.stderr);
  assert.ok(r.stderr.includes(`warning: story ${S} cites post ${pid}, missing on X`), r.stderr);
  const page = read(`story/${S}/index.html`);
  assert.match(page, /data-unavailable="missing"[\s\S]*?X has no post with this id now/);
  assert.ok(!page.includes(`/status/${pid}"`), 'no link to a post that is not there');
  assertNothingOf(page, fixtureRecords().get(pid));
});

test('a cited post X has not been asked about yet is shown as unavailable until it is confirmed', () => {
  const pid = story(S).posts[1].id;
  const r = buildWith({ [pid]: null });
  assert.equal(r.status, 0, r.stderr);
  assert.ok(r.stderr.includes(`warning: story ${S} cites post ${pid}, not confirmed by X yet`), r.stderr);
  assert.match(read(`story/${S}/index.html`), /data-unavailable="unverified"[\s\S]*?has not been confirmed with X yet/);
  assertNothingOf(read(`story/${S}/index.html`), fixtureRecords().get(pid));
});

test('a story that loses every post it cites still builds: its words, its worlds\' descriptions, and the notes', () => {
  const s = story('2026-10-08-cold-plunge-vagus');
  const r = buildWith(Object.fromEntries(s.posts.map((p) => [p.id, 'withheld'])));
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stderr, /posts not shown because X has not confirmed them/);
  const page = read(`story/${s.id}/index.html`);
  assert.equal((page.match(/data-unavailable="withheld"/g) ?? []).length, 4, 'two in the worlds and two in the list of posts');
  for (const w of s.worlds) assert.ok(page.includes(escHtml(w.sees)));
  assert.match(page, /<dt class="lab">Posts tracked<\/dt><dd>0<\/dd>/);
  for (const p of s.posts) assertNothingOf(page, fixtureRecords().get(p.id));
  assert.ok(read('stories/index.html').includes(`id="s-${s.id}"`), 'it stays on the list of stories');
});

test('a cited post whose words on X differ from the record still stops the build', () => {
  const pid = story(S).posts[1].id;
  const r = buildWith({ [pid]: 'mismatch' });
  assert.notEqual(r.status, 0);
  assert.ok(r.stderr.includes(`cites post ${pid}, which X shows differently from the record`), r.stderr);
});

test('on the pulse, a post X does not confirm is left out with a warning, and a mismatch still stops the build', () => {
  run('tools/make-demo.mjs');
  const pulse = JSON.parse(readFileSync(root + 'fixtures/demo/pulse/current.json', 'utf8'));
  const [gone, keeps] = pulse.items.filter((it) => (it.also ?? []).length).slice(-2);
  const r = buildWith({ [gone.id]: 'withheld', [keeps.also[0]]: 'missing' });
  assert.equal(r.status, 0, r.stderr);
  assert.ok(r.stderr.includes(`warning: pulse item ${gone.id} is withheld by X`), r.stderr);
  assert.ok(r.stderr.includes(`warning: related post ${keeps.also[0]} of pulse item ${keeps.id} is missing on X`), r.stderr);
  const data = JSON.parse(read('data/pulse.json')).pulse.map((it) => it.id);
  assert.ok(!data.includes(gone.id) && data.includes(keeps.id), 'the withheld item is off the pulse, the other stays');
  assert.ok(!read('index.html').includes(`id="p-${gone.id}"`) && !read(`desk/${gone.desk}/index.html`).includes(`id="p-${gone.id}"`));
  assert.ok(!read('index.html').includes(`/status/${keeps.also[0]}"`), 'and a related post X has no answer for is dropped');
  // With no story citing them, so that the stop comes from the pulse itself.
  const noStories = () => { for (const f of readdirSync(root + 'fixtures/demo/moments')) rmSync(root + 'fixtures/demo/moments/' + f); };
  const bad = buildWith({ [keeps.also[0]]: 'mismatch' }, noStories);
  assert.notEqual(bad.status, 0);
  assert.ok(bad.stderr.includes(`pulse item ${keeps.id} cites post ${keeps.also[0]}, which X shows differently from the record`), bad.stderr);
  const worse = buildWith({ [gone.id]: 'mismatch' }, noStories);
  assert.notEqual(worse.status, 0, 'a mismatched pulse item stops the build');
  assert.ok(worse.stderr.includes(`the pulse cites post ${gone.id}, which X shows differently`), worse.stderr);
  run('tools/make-demo.mjs');
});

test('with every post confirmed by the ledger, a flagged post on the pulse still stops the build', () => {
  const file = root + 'fixtures/demo/pulse/current.json';
  const r = buildWith({}, () => {
    const pulse = JSON.parse(readFileSync(file, 'utf8'));
    const flagged = JSON.parse(readFileSync(root + 'fixtures/demo/FLAGGED_POST', 'utf8'));
    pulse.items.push({ id: flagged.id, desk: 'life', line: 'This post must never be shown.' });
    writeFileSync(file, JSON.stringify(pulse));
  });
  assert.notEqual(r.status, 0);
  assert.match(r.stderr, /flagged/);
  run('tools/make-demo.mjs');
});
