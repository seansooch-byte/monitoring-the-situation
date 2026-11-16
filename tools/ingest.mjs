#!/usr/bin/env node
// Deliver captures to the store.
//
//   node tools/ingest.mjs capture/2026/10/28/0406Z.json [more]   deliver these files
//   node tools/ingest.mjs --new      deliver every capture file newer than the store's newest run
//   node tools/ingest.mjs --all      deliver every capture file the store does not have (resumable)
//
// Files go oldest first, because a capture may observe posts first recorded by an earlier one.
// A 5xx or network error is retried with a backoff (Cloudflare answers a passing 503 under load);
// any failure that remains stops the run, since every later file could depend on it. Run again to
// resume. A file the store already holds is reported and skipped; a file Gate 1 refuses is reported
// with its errors. Exits 1 if a delivery failed. Token and address: tools/lib/store.mjs.
//
// HELD is not a failure. The store shares a free database plan with the agents' board and stops at
// its share of the day's writes (contract/budget.json, store), answering 429. The file and every later
// one stay in git, and the first --new after 00:00 UTC delivers them, oldest first. Exit 0.
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { walk } from './lib/files.mjs';
import { storeClient } from './lib/store.mjs';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const store = storeClient();
const runIdOf = (p) => { const m = /(\d{4})\/(\d{2})\/(\d{2})\/(\d{4}Z)\.json$/.exec(p); return m ? `${m[1]}-${m[2]}-${m[3]}T${m[4]}` : null; };

let files;
if (args.includes('--all') || args.includes('--new')) {
  const have = new Set();
  let newest = '';
  for (let page = 0; page < 20; page++) {
    const { runs } = await store.get(`/api/runs?limit=5000&to=${encodeURIComponent(page === 0 ? '9999' : newest)}`);
    for (const r of runs) { have.add(r.id); if (!newest || r.started_at < newest) newest = r.started_at; }
    if (runs.length < 5000) break;
  }
  const latest = [...have].sort().at(-1) ?? '';
  files = walk(join(REPO, 'capture'), (n) => /^\d{4}Z\.json$/.test(n)).filter((p) => { const id = runIdOf(p); return id && !have.has(id) && (args.includes('--all') || id > latest); });
  console.log(`store holds ${have.size} runs${latest ? `, newest ${latest}` : ''}; ${files.length} file${files.length === 1 ? '' : 's'} to deliver`);
} else {
  files = args.filter((a) => !a.startsWith('-'));
  if (!files.length) { console.error('usage: node tools/ingest.mjs <capture file> [more] | --new | --all'); process.exit(2); }
}

files.sort((a, b) => (runIdOf(a) ?? a).localeCompare(runIdOf(b) ?? b));
const RETRIES = [5, 20, 60];   // seconds to wait before each retry of a 5xx or network error
const transient = (e) => !e.status || e.status >= 500;
async function deliver(doc) {
  for (let i = 0; ; i++) {
    try { return await store.post('/ingest', doc); }
    catch (e) {
      if (!transient(e) || i >= RETRIES.length) throw e;
      console.log(`RETRY ${doc.run?.id}  ${e.status ?? 'network'}; waiting ${RETRIES[i]} s`);
      await new Promise((r) => setTimeout(r, RETRIES[i] * 1000));
    }
  }
}

let failed = 0, delivered = 0, held = 0, heldUntil = null;
for (const f of files) {
  let doc;
  try { doc = JSON.parse(readFileSync(f, 'utf8')); } catch (e) { console.log(`FAIL  ${f}  not readable JSON: ${e.message}`); failed++; continue; }
  try {
    const r = await deliver(doc);
    if (r.duplicate) console.log(`HAVE  ${r.run}`);
    else { delivered++; console.log(`OK    ${r.run}  ${r.posts} posts, ${r.observations} observations, ${r.volume_points} counts, ${Math.round(r.bytes / 1024)} KB as ${Math.round(r.gzip / 1024)} KB${r.written ? `, ${r.written} rows written (${r.spent} of ${r.allowance} today)` : ''}${r.warnings?.length ? `, ${r.warnings.length} warning${r.warnings.length === 1 ? '' : 's'}` : ''}`); }
  } catch (e) {
    if (e.status === 429 && e.data?.held) {
      held = files.length - files.indexOf(f);
      heldUntil = e.data.resets_at;
      console.log(`HELD  ${runIdOf(f) ?? f}  the store has written ${e.data.spent} of its ${e.data.allowance} rows for today; ${held} file${held === 1 ? '' : 's'} wait${held === 1 ? 's' : ''} in git until ${heldUntil}`);
      break;
    }
    failed++;
    console.log(`FAIL  ${f}  ${e.status && e.status >= 500 ? `${e.status} from the store` : e.message}`);
    if (e.status === 422 && e.data?.errors) for (const err of e.data.errors.slice(0, 5)) console.log(`        ${err}`);
    console.log(`stopping: later files may depend on this one; run again to resume from ${runIdOf(f) ?? f}`);
    break;
  }
}
console.log(`delivered ${delivered}, failed ${failed}${held ? `, held ${held} until ${heldUntil} (the store's share of the day's writes is spent; not a failure)` : ''}`);
process.exit(failed ? 1 : 0);
