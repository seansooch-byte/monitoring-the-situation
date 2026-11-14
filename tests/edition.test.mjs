// The paper's edition (contract/PAPER.md): one Eastern day of the record, ranked by the numbers.
// The first tests build an edition from a small invented record in which every rule has a case;
// the last builds the real 13 November 2026 edition from this repo.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildEdition } from '../tools/lib/edition.mjs';
import { dayBounds, dayKey, hourET } from '../tools/lib/clock.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const DAY = '2026-11-13';
const M = 1e6;

const desks = {
  groups: [{ id: 'news', name: 'News' }, { id: 'money', name: 'Money' }, { id: 'online', name: 'Life online' }],
  desks: [
    { id: 'politics', name: 'Politics', group: 'news' },
    { id: 'markets', name: 'Markets', group: 'money' },
    { id: 'internet', name: 'The internet', group: 'online' },
    { id: 'life', name: 'Life', group: 'online' },
  ],
};
const paper = { news_sections: ['news', 'money'], briefing: 5, unreported: 5, watched: 8, section_items: 3,
  never_shown: ['private_individual', 'minor', 'nsfw', 'graphic'] };

function post(id, handle, desk, created, flags = []) {
  return { id, created_at: created, author: { handle }, desk, flags };
}
const obs = (id, at, views, state = 'live') => ({ id, at, views, state });

function record() {
  const posts = [
    post('p1', 'a', 'politics', '2026-11-13T15:00:00.000Z'),
    post('p2', 'b', 'politics', '2026-11-13T17:00:00.000Z'),
    post('p3', 'c', 'internet', '2026-11-12T20:00:00.000Z'),
    post('p4', 'd', 'internet', '2026-11-13T12:00:00.000Z'),
    post('p5', 'e', 'internet', '2026-11-13T13:00:00.000Z', ['minor']),
    post('p6', 'f', 'life', '2026-11-13T14:00:00.000Z'),
    post('p7', 'g', 'internet', '2026-11-13T14:30:00.000Z'),
    post('p8', 'g', 'internet', '2026-11-13T15:30:00.000Z'),
    post('p9', 'h', 'markets', '2026-11-13T10:00:00.000Z'),
  ];
  const observations = [
    obs('p1', '2026-11-13T16:00:00Z', 1 * M), obs('p1', '2026-11-14T04:00:00Z', 3 * M), obs('p1', '2026-11-14T06:00:00Z', 9 * M),
    obs('p2', '2026-11-14T04:30:00Z', 2 * M),
    obs('p3', '2026-11-13T04:00:00Z', 5 * M), obs('p3', '2026-11-14T04:00:00Z', 6 * M),
    obs('p4', '2026-11-14T03:00:00Z', 8 * M),
    obs('p5', '2026-11-14T03:00:00Z', 9 * M),
    obs('p6', '2026-11-14T03:00:00Z', 4 * M),
    obs('p7', '2026-11-14T03:00:00Z', 7 * M),
    obs('p8', '2026-11-14T03:00:00Z', 1 * M),
    obs('p9', '2026-11-13T20:00:00Z', 0.5 * M), obs('p9', '2026-11-14T01:00:00Z', 0.5 * M, 'unavailable'),
  ];
  const ledger = Object.fromEntries(['p1', 'p2', 'p3', 'p5', 'p6', 'p7', 'p8', 'p9'].map((id) => [id, { result: 'ok' }]));
  const moments = [
    { id: '2026-11-13-alpha', title: 'Alpha', dek: 'The alpha story.', standing: 'developing', desks: ['politics'], started_at: '2026-11-13T15:30:00Z',
      posts: [{ id: 'p2', role: 'voice' }, { id: 'p1', role: 'origin' }] },
    { id: '2026-11-12-beta', title: 'Beta', dek: 'The beta story.', standing: 'established', desks: ['internet'], started_at: '2026-11-12T21:00:00Z',
      posts: [{ id: 'p3', role: 'origin' }] },
    { id: '2026-11-13-gamma', title: 'Gamma', dek: 'The gamma story.', standing: 'developing', desks: ['politics'], started_at: '2026-11-13T18:00:00Z',
      posts: [{ id: 'p4', role: 'origin' }] },
    { id: '2026-11-10-old', title: 'Old', dek: 'An old story.', standing: 'established', desks: ['politics'], started_at: '2026-11-10T18:00:00Z', posts: [] },
  ];
  const lines = {
    p1: { desk: 'politics', line: 'A line about p1.' },
    p6: { desk: 'politics', line: 'A line about p6, which the editor moved to politics.' },
    p7: { desk: 'internet', line: 'A line about p7.' },
    p8: { desk: 'internet', line: 'A line about p8.' },
  };
  return { day: DAY, desks, paper, posts, observations, ledger, moments, lines, letter: null };
}

test('the Eastern day is midnight to midnight in New York, whatever the season', () => {
  const [start, end] = dayBounds(DAY);
  assert.equal(new Date(start).toISOString(), '2026-11-13T05:00:00.000Z');
  assert.equal(new Date(end).toISOString(), '2026-11-14T05:00:00.000Z');
  const [s2] = dayBounds('2026-07-04');
  assert.equal(new Date(s2).toISOString(), '2026-07-04T04:00:00.000Z', 'summer time is four hours behind');
  assert.equal(dayKey(Date.parse('2026-11-14T04:59:00Z')), DAY);
  assert.equal(dayKey(Date.parse('2026-11-14T05:00:00Z')), '2026-11-14');
  assert.equal(hourET(Date.parse('2026-11-13T15:00:00Z')), 10);
});

test('the largest story leads, ranked by the views its posts gained on the day', () => {
  const e = buildEdition(record());
  assert.equal(e.schema, 'mts.edition/2');
  assert.equal(e.edition.day, DAY);
  assert.deepEqual(e.stories.map((s) => [s.id, s.reach]), [['2026-11-13-alpha', 5 * M], ['2026-11-12-beta', 1 * M], ['2026-11-13-gamma', 0]]);
  assert.equal(e.lead, '2026-11-13-alpha');
  assert.deepEqual(e.briefing, ['2026-11-13-alpha', '2026-11-12-beta', '2026-11-13-gamma']);
  assert.deepEqual(e.stories[0].posts.map((p) => [p.id, p.views, p.role, p.handle]), [['p1', 3 * M, 'origin', 'a'], ['p2', 2 * M, 'voice', 'b']]);
  assert.deepEqual(e.stories[0].sections, ['news']);
  assert.ok(!e.stories.some((s) => s.id === '2026-11-10-old'), 'a story with nothing on the day is not in its edition');
});

test('a story begun earlier counts only what it gained on the day', () => {
  const beta = buildEdition(record()).stories.find((s) => s.id === '2026-11-12-beta');
  assert.equal(beta.reach, 1 * M, 'six million at the end less five million at the start');
});

test('a story begun after the day is not in that day\'s edition, whatever its posts gained that day', () => {
  const r = record();
  r.moments.push({ id: '2026-11-14-later', title: 'Later', dek: 'A story begun the next day.', standing: 'developing', desks: ['internet'],
    started_at: '2026-11-14T15:00:00Z', posts: [{ id: 'p3', role: 'origin' }] });
  const e = buildEdition(r);
  assert.ok(!e.stories.some((s) => s.id === '2026-11-14-later'), 'a front page carries no headline from a later day');
  assert.ok(e.stories.some((s) => s.id === '2026-11-12-beta'), 'CONTROL: the story begun the day before is there');
});

test('a reading after the day ends never changes the edition', () => {
  const a = buildEdition(record());
  const r = record();
  r.observations.push(obs('p2', '2026-11-14T09:00:00Z', 50 * M), obs('p7', '2026-11-15T09:00:00Z', 90 * M));
  assert.equal(JSON.stringify(buildEdition(r)), JSON.stringify(a));
});

test('an unconfirmed, flagged or vanished post never counts and never appears', () => {
  const e = buildEdition(record());
  const text = JSON.stringify(e);
  for (const id of ['p4', 'p5', 'p9']) assert.ok(!text.includes(`"${id}"`), `${id} is not in the edition`);
  assert.equal(e.stories.find((s) => s.id === '2026-11-13-gamma').posts.length, 0);
});

test('posts the editor described and no story cites: news sections are not yet a story, the rest were watched', () => {
  const e = buildEdition(record());
  assert.deepEqual(e.unreported.map((p) => [p.id, p.views, p.section, p.desk, p.line]),
    [['p6', 4 * M, 'news', 'politics', 'A line about p6, which the editor moved to politics.']]);
  assert.deepEqual(e.watched.map((p) => [p.id, p.views, p.handle]), [['p7', 7 * M, 'g']], 'one place per account: p8 is held back');
  assert.ok(!e.unreported.concat(e.watched).some((p) => p.id === 'p1'), 'a post a story cites is in its story, not here');
});

test('the counts and the sections are the day', () => {
  const e = buildEdition(record());
  assert.deepEqual(e.counts, { posts: 5, accounts: 4, desks: 4, stories: 3, views: 18 * M });
  const by = Object.fromEntries(e.sections.map((s) => [s.id, s]));
  assert.deepEqual(e.sections.map((s) => s.id), ['news', 'money', 'online'], 'in the order of contract/desks.json');
  assert.deepEqual([by.news.posts, by.news.views, by.online.posts, by.online.views, by.money.posts, by.money.views], [3, 9 * M, 2, 9 * M, 0, 0]);
  assert.equal(by.news.share, 0.5);
  assert.equal(by.news.hours.length, 24);
  assert.equal(by.news.hours[10], 1, 'p1 was posted at 10 a.m. Eastern');
  assert.equal(by.news.hours.reduce((a, b) => a + b, 0), 3);
  assert.deepEqual(by.news.stories, ['2026-11-13-alpha', '2026-11-13-gamma']);
  assert.deepEqual(by.news.items.map((p) => [p.id, p.line]), [['p6', 'A line about p6, which the editor moved to politics.']]);
  assert.deepEqual(by.online.stories, ['2026-11-12-beta']);
});

test('a post with no desk of its own takes the desk of the story that cites it', () => {
  const r = record();
  r.posts.push(post('p10', 'k', null, '2026-11-13T20:00:00.000Z'));
  r.observations.push(obs('p10', '2026-11-14T03:00:00Z', 6 * M));
  r.ledger.p10 = { result: 'ok' };
  r.moments[0].posts.push({ id: 'p10', role: 'voice' });
  const e = buildEdition(r);
  assert.equal(e.stories[0].reach, 11 * M, 'p10 joins the alpha story');
  assert.equal(e.sections.find((s) => s.id === 'news').posts, 4, 'and the news section, by the story\'s desk');
  r.moments[0].posts.pop();
  assert.ok(!JSON.stringify(buildEdition(r)).includes('"p10"'), 'CONTROL: with no story and no desk it does not count');
});

test('an edition holds no text from a post', () => {
  const r = record();
  r.posts[0].text = 'THE WORDS OF THE POST';
  assert.ok(!JSON.stringify(buildEdition(r)).includes('THE WORDS OF THE POST'));
});

function letter(over = {}) {
  const pad = (t, n) => t + ' More words in the same plain voice.'.repeat(n);
  return {
    schema: 'mts.letter/1', date: DAY, published: '2026-11-14', model: 'Test Model',
    subject: 'The day the alpha story led the record', summary: 'One sentence on what the day was about.',
    lead: { desk: 'politics', head: 'Alpha leads', text: [pad('The alpha story drew {reach} views on the day.', 20)], cites: ['alpha'] },
    notes: [
      { desk: 'internet', head: 'Beta again', text: pad('The beta story moved again.', 6), cites: ['beta'] },
      { desk: 'life', head: 'Alpha, seen again', text: pad('The alpha story, from the other side.', 6), cites: ['alpha'] },
    ],
    read: { text: [pad('What the day adds up to.', 8)], cites: ['alpha'] },
    sources: { alpha: { story: '2026-11-13-alpha' }, beta: { story: '2026-11-12-beta' } },
    figures: { reach: { value: '5M', of: 'views on the day', source: 'alpha' } },
    ...over,
  };
}

test('a good letter rides in its edition, whole', () => {
  const r = record();
  r.letter = letter();
  const e = buildEdition(r);
  assert.equal(e.letter.subject, 'The day the alpha story led the record');
  assert.deepEqual(e.letter.read, r.letter.read);
  assert.equal(buildEdition(record()).letter, null, 'CONTROL: no letter, none in the edition');
});

test('a letter that breaks a rule stops the edition and names its file', () => {
  const em = String.fromCharCode(0x2014);
  for (const [what, change, names] of [
    ['an em dash', (l) => l.read.text.push(`One thing ${em} then another.`), 'dash'],
    ['a typed number', (l) => l.read.text.push('It drew 22.6M views.'), '22.6M'],
    ['a story not in the edition', (l) => { l.sources.beta.story = '2026-11-10-old'; }, 'not in this day'],
    ['a key the format does not name', (l) => { l.mood = 'grim'; }, 'mood'],
  ]) {
    const r = record();
    r.letter = letter();
    change(r.letter);
    assert.throws(() => buildEdition(r), (err) => err.message.includes(`newsletter/${DAY}.json`) && err.message.includes(names), what);
  }
});

test('the real 13 November edition leads with the ground stop and puts Microsoft among the unreported', () => {
  const out = mkdtempSync(join(tmpdir(), 'edition-'));
  try {
    const said = execFileSync('node', ['tools/edition.mjs', '--day', DAY, '--out', out], { cwd: root, encoding: 'utf8' });
    assert.match(said, /^edition 2026-11-13:/m);
    const e = JSON.parse(readFileSync(join(out, `${DAY}.json`), 'utf8'));
    assert.equal(e.lead, '2026-11-13-faa-nationwide-ground-stop');
    assert.ok(e.unreported.some((p) => p.id === '2121282013600907325' && p.desk === 'tech'), 'Microsoft, on the editor\'s tech desk');
    assert.ok(e.counts.posts > 500 && e.counts.stories >= 6, JSON.stringify(e.counts));
    assert.equal(e.sections.length, 6);
    assert.ok(Math.abs(e.sections.reduce((a, s) => a + s.share, 0) - 1) < 1e-9);
    const again = mkdtempSync(join(tmpdir(), 'edition-'));
    execFileSync('node', ['tools/edition.mjs', '--day', DAY, '--out', again], { cwd: root });
    assert.equal(readFileSync(join(again, `${DAY}.json`), 'utf8'), readFileSync(join(out, `${DAY}.json`), 'utf8'), 'built twice, the same bytes');
    rmSync(again, { recursive: true, force: true });
  } finally {
    rmSync(out, { recursive: true, force: true });
  }
});
