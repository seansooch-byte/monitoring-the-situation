// Gate 2: X itself is asked whether a post exists and what it says. These tests pin how
// X's answer is read and compared; the network call is one thin function around them.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { textFromEmbed, compareToX, askX, WITHHELD } from '../tools/verify-posts.mjs';
import { ASK_TIMEOUT_MS } from '../tools/lib/gate2.mjs';

// A real answer from publish.x.com/oembed, fetched 2026-10-09 for post 2108047268167274883.
const REUTERS = {
  url: 'https://x.com/Reuters/status/2108047268167274883', author_name: 'Reuters', author_url: 'https://x.com/Reuters',
  html: '<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Wall Street ends lower, off record highs, as Treasury yields climb <a href="https://t.co/cTEVSB1BgE">https://t.co/cTEVSB1BgE</a> <a href="https://t.co/cTEVSB1BgE">https://t.co/cTEVSB1BgE</a></p>&mdash; Reuters (@Reuters) <a href="https://x.com/Reuters/status/2108047268167274883?ref_src=twsrc%5Etfw">October 8, 2026</a></blockquote>\n\n',
};
const record = (over = {}) => ({ id: '2108047268167274883', url: 'https://x.com/Reuters/status/2108047268167274883', text: 'Wall Street ends lower, off record highs, as Treasury yields climb https://t.co/cTEVSB1BgE https://t.co/cTEVSB1BgE', author: { handle: 'Reuters', name: 'Reuters' }, ...over });

test('the post text is read out of X\'s embed markup, links and entities included', () => {
  assert.equal(textFromEmbed(REUTERS.html), 'Wall Street ends lower, off record highs, as Treasury yields climb https://t.co/cTEVSB1BgE https://t.co/cTEVSB1BgE');
  assert.equal(textFromEmbed('<blockquote><p lang="en">a &amp; b<br>c &lt;3 &quot;d&quot; &#39;e&#39;</p>&mdash; X</blockquote>'), 'a & b\nc <3 "d" \'e\'');
  assert.equal(textFromEmbed('<div>no post here</div>'), null);
});

test('a record that matches X is confirmed', () => {
  assert.deepEqual(compareToX(record(), REUTERS), { result: 'ok', detail: null });
});

test('entities in the record, as the API sends them, do not cause a false mismatch', () => {
  const embed = { ...REUTERS, html: '<blockquote><p>An employee inside AT&amp;T Stadium said “embarrassing”</p>&mdash; x</blockquote>' };
  assert.equal(compareToX(record({ text: 'An employee inside AT&amp;T Stadium said “embarrassing”' }), embed).result, 'ok');
});

test('a long post that X shortens in the embed still matches on its opening', () => {
  const long = 'First sentence of a long post that runs well past what the embed shows. '.repeat(8);
  const embed = { ...REUTERS, html: `<blockquote><p>${long.slice(0, 260)}…</p>&mdash; x</blockquote>` };
  assert.equal(compareToX(record({ text: long }), embed).result, 'ok');
});

test('different words are a mismatch, and so is a different author', () => {
  assert.equal(compareToX(record({ text: 'Wall Street ends sharply higher on rate hopes' }), REUTERS).result, 'mismatch');
  const other = compareToX(record({ url: 'https://x.com/SomeoneElse/status/2108047268167274883', author: { handle: 'SomeoneElse', name: 'x' } }), REUTERS);
  assert.equal(other.result, 'mismatch');
  assert.match(other.detail, /author/);
});

test('a post with no text matches an embed with no text', () => {
  const embed = { ...REUTERS, html: '<blockquote><p lang="zxx"><a href="https://t.co/abc">https://t.co/abc</a></p>&mdash; x</blockquote>' };
  assert.equal(compareToX(record({ text: 'https://t.co/abc' }), embed).result, 'ok');
});

test('no answer from X is "missing", never a pass', () => {
  assert.equal(compareToX(record(), null).result, 'missing');
});

// ---- what the first full pass over two real captures showed (2026-10-09): 24 false mismatches

test('a reply matches although the API keeps the leading @mentions and the embed drops them', () => {
  const embed = { ...REUTERS, html: '<blockquote><p lang="en" dir="ltr">are they finding all the mormon planets?</p>&mdash; x</blockquote>' };
  assert.equal(compareToX(record({ text: '@somewheresy are they finding all the mormon planets?' }), embed).result, 'ok');
  assert.equal(compareToX(record({ text: '@a_b @c2 are they finding all the mormon planets?' }), embed).result, 'ok');
});

test('spacing before a hashtag and the embed\'s own media link do not make a mismatch', () => {
  const embed = { ...REUTERS, html: '<blockquote><p lang="en" dir="ltr">Lily : The ultimate cure!!!!<a href="https://x.com/hashtag/Wuwafanart">#Wuwafanart</a> <a href="https://t.co/Ct0xuT9UTn">pic.twitter.com/Ct0xuT9UTn</a></p>&mdash; x</blockquote>' };
  assert.equal(compareToX(record({ text: 'Lily : The ultimate cure!!!!\n#Wuwafanart https://t.co/Ct0xuT9UTn' }), embed).result, 'ok');
});

test('a post that is only media matches an embed that shows only its media link', () => {
  const embed = { ...REUTERS, html: '<blockquote><p lang="zxx" dir="ltr"><a href="https://t.co/SBf83gzkaZ">pic.twitter.com/SBf83gzkaZ</a></p>&mdash; x</blockquote>' };
  assert.equal(compareToX(record({ text: 'https://t.co/SBf83gzkaZ https://t.co/09cZAeeIwn' }), embed).result, 'ok');
  assert.equal(compareToX(record({ text: '' }), embed).result, 'ok');
});

// ---- the question to X is bounded in time: a hang is an error, never a stall (2026-11-03)

test('a question X does not answer in time fails with a clear error, so the pass records nothing and moves on', async () => {
  // A fetch that never answers, and only gives up when it is aborted.
  const hang = (url, { signal }) => new Promise((_, reject) => signal.addEventListener('abort', () => reject(signal.reason)));
  // The abort timer does not hold the process open (a real fetch's socket does), so this one does.
  const alive = setTimeout(() => {}, 5000);
  const started = Date.now();
  await assert.rejects(askX('https://x.com/a/status/1', { timeoutMs: 50, fetchImpl: hang }), /X did not answer within 0\.05 s/);
  clearTimeout(alive);
  assert.ok(Date.now() - started < 2000, 'it gives up at the limit');
  assert.equal(ASK_TIMEOUT_MS, 15000);
});

test('X\'s answers are still read as before: 404 is no post, 403 is withheld, another status is an error', async () => {
  const answer = (status, body = {}) => async () => new Response(JSON.stringify(body), { status });
  assert.equal(await askX('u', { fetchImpl: answer(404) }), null);
  assert.equal(await askX('u', { fetchImpl: answer(403) }), WITHHELD);
  await assert.rejects(askX('u', { fetchImpl: answer(500) }), /X answered 500/);
  assert.deepEqual(await askX('u', { fetchImpl: answer(200, { html: 'x' }) }), { html: 'x' });
});

test('the looser comparison still catches a record whose words are not what X shows', () => {
  const embed = { ...REUTERS, html: '<blockquote><p>are they finding all the mormon planets?</p>&mdash; x</blockquote>' };
  assert.equal(compareToX(record({ text: '@somewheresy they have found every planet already' }), embed).result, 'mismatch');
  assert.equal(compareToX(record({ text: '' }), embed).result, 'mismatch');
});
