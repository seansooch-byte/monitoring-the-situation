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
import { checkOpinion } from '../tools/lib/opinion.mjs';
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
  return { day: DAY, desks, paper, posts, observations, ledger, moments, lines, opinion: null };
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
  assert.equal(e.schema, 'mts.edition/1');
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

function opinion(over = {}) {
  return {
    schema: 'mts.opinion/1', date: DAY, published: '2026-11-14', model: 'Test Model',
    head: 'The day the planes stood still',
    text: ['The record shows one thing above the rest. ' + 'Plain words that make a case about the day. '.repeat(16),
      'It was 2026, and GPT-5 and the F-35 both made the news in the 1990s sense. ' + 'More words in the same voice. '.repeat(8)],
    cites: ['2026-11-13-alpha', 'p6'],
    ...over,
  };
}

test('a good opinion rides in its edition', () => {
  const r = record();
  r.opinion = opinion();
  const e = buildEdition(r);
  assert.equal(e.opinion.head, 'The day the planes stood still');
  assert.deepEqual(e.opinion.cites, ['2026-11-13-alpha', 'p6']);
});

test('an opinion that breaks a rule stops the edition and names the rule', () => {
  const em = String.fromCharCode(0x2014), en = String.fromCharCode(0x2013);
  const para = (s) => ({ text: [opinion().text[0], s] });
  const broken = {
    'an em dash': [para(`One thing ${em} then another.`), 'dash'],
    'an en dash': [{ head: `The day ${en} the planes stood still` }, 'dash'],
    'a double hyphen': [para('One thing -- then another.'), 'dash'],
    'a quotation mark': [para('He said "never" and left.'), 'quotation'],
    'a curly quotation': [para('He said ' + String.fromCharCode(0x201C) + 'never' + String.fromCharCode(0x201D) + '.'), 'quotation'],
    'a single quotation': [para("He said 'never' and left."), 'quotation'],
    'a typed number': [para('It drew 22.6M views.'), '22.6M'],
    'a typed share': [para('It rose 12% in a day.'), '12%'],
    'a typed count': [para('More than 5,300 flights were canceled.'), '5,300'],
    'a typed sum': [para('He asked for $50 billion.'), '$50'],
    'an address': [para('Read it at example.com/x today.'), 'address'],
    'a scheme': [para('Read it at https://example.com today.'), 'address'],
    'an emoji': [para('Big day ' + String.fromCodePoint(0x1F680)), 'emoji'],
    'a pictograph': [para('Big day ' + String.fromCodePoint(0x2B50)), 'emoji'],
    'markup': [para('A <b>bold</b> claim.'), 'markup'],
    'a dose': [para('They gave five mg at once.'), 'dose'],
    'a key the format does not name': [{ mood: 'grim' }, 'mood'],
    'a cite not in the edition': [{ cites: ['2026-11-13-alpha', 'nowhere'] }, 'nowhere'],
    'no cite': [{ cites: [] }, 'cites'],
    'a cite of an unconfirmed post': [{ cites: ['p4'] }, 'p4'],
    'too few words': [{ text: ['Too short.'] }, '120'],
    'too many words': [{ text: ['Word '.repeat(420)] }, '400'],
    'five paragraphs': [{ text: Array(5).fill('Some words here. '.repeat(8)) }, 'paragraphs'],
    'a short head': [{ head: 'Short' }, 'head'],
    'another day': [{ date: '2026-11-12' }, 'date'],
    'published before its day': [{ published: '2026-11-13' }, 'published'],
    'a day that does not exist': [{ published: '2026-11-31' }, 'published'],
    'another schema': [{ schema: 'mts.opinion/2' }, 'schema'],
    'a paragraph that is not text': [{ text: [{ html: 'x' }] }, 'text'],
  };
  for (const [what, [change, names]] of Object.entries(broken)) {
    const r = record();
    r.opinion = opinion(change);
    assert.throws(() => buildEdition(r), (err) => err.message.includes(`opinion/${DAY}.json`) && err.message.includes(names), what);
  }
  assert.deepEqual(checkOpinion(opinion(), DAY, new Set(['2026-11-13-alpha', 'p6'])), [], 'CONTROL: the unbroken opinion has no problem');
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
