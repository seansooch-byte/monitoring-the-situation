// Gate 2 as pure functions: how a post's record is compared with what X says about it. No file,
// no ledger, so it runs the same at the command line (tools/verify-posts.mjs) and inside the
// Worker's deletion sweep. X's public embed endpoint needs no account and answers 404 for a post
// that does not exist, 403 for one it will not show without a login.
const ENDPOINT = 'https://publish.x.com/oembed?omit_script=1&dnt=1&url=';

const decode = (s) => s
  .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'")
  .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n))).replace(/&amp;/g, '&');

// The post's text as X renders it in an embed: the first paragraph of the blockquote.
export function textFromEmbed(html) {
  const m = /<blockquote[^>]*>\s*<p[^>]*>([\s\S]*?)<\/p>/.exec(html ?? '');
  if (!m) return null;
  return decode(m[1].replace(/<br\s*\/?>/g, '\n').replace(/<[^>]+>/g, ''));
}

// Compare on the characters of the words only. X's API and its embed differ in ways that are not
// differences in what was said: links (t.co in one, pic.twitter.com in the other), the leading
// @mentions of a reply (kept by the API, dropped by the embed), entities, case, and spacing.
const words = (s) => decode(String(s ?? ''))
  .replace(/https?:\/\/\S+/g, ' ').replace(/pic\.twitter\.com\/\S+/g, ' ')
  .replace(/^(\s*@[A-Za-z0-9_]{1,15})+/, ' ')
  .replace(/[\u2026]/g, ' ').toLowerCase().replace(/\s+/g, '');

export function compareToX(record, embed) {
  if (!embed) return { result: 'missing', detail: 'X returned no post for this id' };
  const handle = (/x\.com\/([A-Za-z0-9_]+)/.exec(embed.author_url ?? '') ?? [])[1] ?? '';
  if (handle.toLowerCase() !== String(record.author?.handle ?? '').toLowerCase()) {
    return { result: 'mismatch', detail: `author: the record says @${record.author?.handle}, X says @${handle}` };
  }
  const theirs = words(textFromEmbed(embed.html)), ours = words(record.text);
  // X shortens long posts in an embed, so a match on the opening is a match.
  const n = Math.min(theirs.length, ours.length, 200);
  if (theirs.slice(0, n) !== ours.slice(0, n) || (n === 0 && theirs.length !== ours.length)) {
    return { result: 'mismatch', detail: `text: the record begins "${ours.slice(0, 70)}", X begins "${theirs.slice(0, 70)}"` };
  }
  return { result: 'ok', detail: null };
}

// null: X has no such post. WITHHELD: X has it but will not show it without a login (sensitive
// media, mostly). Anything else is an error and is not recorded.
export const WITHHELD = Symbol('withheld');
export async function askX(url) {
  const r = await fetch(ENDPOINT + encodeURIComponent(url), { redirect: 'follow' });
  if (r.status === 404) return null;
  if (r.status === 403) return WITHHELD;
  if (!r.ok) throw new Error(`X answered ${r.status}`);
  return r.json();
}

