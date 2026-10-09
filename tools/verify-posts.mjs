#!/usr/bin/env node
// Gate 2. Before a post is published, X is asked directly whether it exists and what it says.
// The grabber's record is never taken on its own word.
//
//   node tools/verify-posts.mjs <post id> [more ids]     check these posts
//   node tools/verify-posts.mjs --moments                check every post cited by a story
//
// Results are kept in verified/posts.json: ok, mismatch, or missing, with the time of the check.
// X's public embed endpoint is used; it needs no account and returns 404 for a post that
// does not exist.
import { existsSync, mkdirSync, readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const LEDGER = join(REPO, 'verified', 'posts.json');
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

// Compare on words only: links, entities, case and spacing differ between X's API and its embed.
const words = (s) => decode(String(s ?? '')).replace(/https?:\/\/\S+/g, ' ').replace(/[…]/g, ' ').toLowerCase().replace(/\s+/g, ' ').trim();

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

export async function askX(url) {
  const r = await fetch(ENDPOINT + encodeURIComponent(url), { redirect: 'follow' });
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`X answered ${r.status}`);
  return r.json();
}

function walk(dir, test, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, test, out);
    else if (test(name)) out.push(p);
  }
  return out;
}

export function loadLedger() { return existsSync(LEDGER) ? JSON.parse(readFileSync(LEDGER, 'utf8')) : {}; }

async function main(argv) {
  const records = new Map();
  for (const f of walk(join(REPO, 'capture'), (n) => /^\d{4}Z\.json$/.test(n))) for (const p of JSON.parse(readFileSync(f, 'utf8')).posts ?? []) records.set(p.id, p);
  let ids = argv.filter((a) => /^\d+$/.test(a));
  if (argv.includes('--moments')) {
    for (const f of walk(join(REPO, 'moments'), (n) => n.endsWith('.json'))) for (const p of JSON.parse(readFileSync(f, 'utf8')).posts ?? []) ids.push(p.id);
  }
  ids = [...new Set(ids)];
  if (!ids.length) { console.error('usage: node tools/verify-posts.mjs <post id> [more] | --moments'); return 2; }
  const ledger = loadLedger();
  let bad = 0;
  for (const id of ids) {
    const rec = records.get(id);
    if (!rec) { console.log(`UNKNOWN  ${id}  no capture has recorded this post`); bad++; continue; }
    let verdict;
    try { verdict = compareToX(rec, await askX(rec.url)); }
    catch (e) { console.log(`ERROR    ${id}  ${e.message}; not recorded, try again`); bad++; continue; }
    ledger[id] = { ...verdict, checked_at: new Date().toISOString().replace(/\.\d{3}Z$/, 'Z'), handle: rec.author.handle };
    if (verdict.result !== 'ok') bad++;
    console.log(`${verdict.result.toUpperCase().padEnd(8)} ${id}  @${rec.author.handle}${verdict.detail ? '  ' + verdict.detail : ''}`);
    await new Promise((r) => setTimeout(r, 250));
  }
  mkdirSync(dirname(LEDGER), { recursive: true });
  writeFileSync(LEDGER, JSON.stringify(Object.fromEntries(Object.entries(ledger).sort()), null, 1) + '\n');
  return bad ? 1 : 0;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exit(await main(process.argv.slice(2)));
}
