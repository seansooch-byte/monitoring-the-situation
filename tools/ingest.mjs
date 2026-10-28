#!/usr/bin/env node
// Deliver captures to the store.
//
//   node tools/ingest.mjs capture/2026/10/28/0406Z.json [more]   deliver these files
//   node tools/ingest.mjs --new      deliver every capture file newer than the store's newest run
//   node tools/ingest.mjs --all      deliver every capture file the store does not have (resumable)
//
// A file the store already holds is reported and skipped; a file Gate 1 refuses is reported with
// its errors. Exits 1 if any delivery failed. Token and address: tools/lib/store.mjs.
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

let failed = 0, delivered = 0;
for (const f of files) {
  let doc;
  try { doc = JSON.parse(readFileSync(f, 'utf8')); } catch (e) { console.log(`FAIL  ${f}  not readable JSON: ${e.message}`); failed++; continue; }
  try {
    const r = await store.post('/ingest', doc);
    if (r.duplicate) console.log(`HAVE  ${r.run}`);
    else { delivered++; console.log(`OK    ${r.run}  ${r.posts} posts, ${r.observations} observations, ${r.volume_points} counts, ${Math.round(r.bytes / 1024)} KB as ${Math.round(r.gzip / 1024)} KB${r.warnings?.length ? `, ${r.warnings.length} warning${r.warnings.length === 1 ? '' : 's'}` : ''}`); }
  } catch (e) {
    failed++;
    console.log(`FAIL  ${f}  ${e.message}`);
    if (e.status === 422 && e.data?.errors) for (const err of e.data.errors.slice(0, 5)) console.log(`        ${err}`);
  }
}
console.log(`delivered ${delivered}, failed ${failed}`);
process.exit(failed ? 1 : 0);
