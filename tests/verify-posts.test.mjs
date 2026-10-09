// Gate 2: X itself is asked whether a post exists and what it says. These tests pin how
// X's answer is read and compared; the network call is one thin function around them.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { textFromEmbed, compareToX } from '../tools/verify-posts.mjs';

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
