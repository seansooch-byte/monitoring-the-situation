#!/usr/bin/env node
// Gate 2. Before a post is published, X is asked directly whether it exists and what it says.
// The grabber's record is never taken on its own word.
//
//   node tools/verify-posts.mjs <post id> [more ids]     check these posts
//   node tools/verify-posts.mjs --moments                check every post cited by a story
//   node tools/verify-posts.mjs --captures               check every captured post not yet checked
//   node tools/verify-posts.mjs --recheck                ask again about every post not confirmed
//
// Results are kept in verified/posts.json: ok, mismatch, missing, or withheld (X has the post but
// will not show it without a login), with the time of the check and the run that recorded the post.
// X's public embed endpoint is used; it needs no account and returns 404 for a post that
// does not exist.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { walk } from './lib/files.mjs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const LEDGER = join(REPO, 'verified', 'posts.json');
import { textFromEmbed, compareToX, askX, WITHHELD } from './lib/gate2.mjs';
export { textFromEmbed, compareToX, askX, WITHHELD };
export function loadLedger() { return existsSync(LEDGER) ? JSON.parse(readFileSync(LEDGER, 'utf8')) : {}; }

async function main(argv) {
  // Each post is remembered with the run that first recorded it, so a run's record can be counted.
  const records = new Map(), firstRun = new Map();
  for (const f of walk(join(REPO, 'capture'), (n) => /^\d{4}Z\.json$/.test(n))) {
    const doc = JSON.parse(readFileSync(f, 'utf8'));
    for (const p of doc.posts ?? []) { records.set(p.id, p); if (!firstRun.has(p.id)) firstRun.set(p.id, doc.run?.id ?? null); }
  }
  let ids = argv.filter((a) => /^\d+$/.test(a));
  if (argv.includes('--captures')) { const seen = loadLedger(); for (const id of records.keys()) if (!seen[id]) ids.push(id); }
  if (argv.includes('--moments')) {
    for (const f of walk(join(REPO, 'moments'), (n) => n.endsWith('.json'))) for (const p of JSON.parse(readFileSync(f, 'utf8')).posts ?? []) ids.push(p.id);
  }
  ids = [...new Set(ids)];
  if (!ids.length) { if (argv.includes('--captures') || argv.includes('--recheck')) { console.log('every captured post has already been checked'); return 0; } console.error('usage: node tools/verify-posts.mjs <post id> [more] | --moments | --captures'); return 2; }
  const ledger = loadLedger();
  for (const [id, v] of Object.entries(ledger)) if (v.run == null && firstRun.has(id)) v.run = firstRun.get(id);
  if (argv.includes('--recheck')) for (const [id, v] of Object.entries(ledger)) if (v.result !== 'ok' && records.has(id)) ids.push(id);
  ids = [...new Set(ids)];
  let bad = 0;
  for (const id of ids) {
    const rec = records.get(id);
    if (!rec) { console.log(`UNKNOWN  ${id}  no capture has recorded this post`); bad++; continue; }
    let verdict;
    try {
      const answer = await askX(rec.url);
      verdict = answer === WITHHELD ? { result: 'withheld', detail: 'X will not show this post without a login' } : compareToX(rec, answer);
    }
    catch (e) { console.log(`ERROR    ${id}  ${e.message}; not recorded, try again`); bad++; continue; }
    ledger[id] = { ...verdict, checked_at: new Date().toISOString().replace(/\.\d{3}Z$/, 'Z'), handle: rec.author.handle, run: firstRun.get(id) ?? null };
    if (verdict.result !== 'ok') bad++;
    console.log(`${verdict.result.toUpperCase().padEnd(8)} ${id}  @${rec.author.handle}${verdict.detail ? '  ' + verdict.detail : ''}`);
    await new Promise((r) => setTimeout(r, 250));
  }
  mkdirSync(dirname(LEDGER), { recursive: true });
  writeFileSync(LEDGER, JSON.stringify(Object.fromEntries(Object.entries(ledger).sort()), null, 1) + '\n');
  // What X said about each run's posts: the grabber's record, counted.
  const byRun = {};
  for (const v of Object.values(ledger)) { const r = (byRun[v.run ?? 'unknown'] ??= { ok: 0, missing: 0, mismatch: 0, withheld: 0 }); r[v.result] = (r[v.result] ?? 0) + 1; }
  for (const [run, r] of Object.entries(byRun).sort()) console.log(`run ${run}: ${r.ok} confirmed, ${r.missing} missing, ${r.mismatch} mismatched, ${r.withheld} withheld by X`);
  return bad ? 1 : 0;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exit(await main(process.argv.slice(2)));
}
