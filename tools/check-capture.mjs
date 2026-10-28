#!/usr/bin/env node
// Gate 1 at the command line. The rules live in tools/lib/capture-check.mjs, a pure function;
// this file reads the desks, the file and the earlier captures, and prints the verdict.
//
//   node tools/check-capture.mjs capture/2026/10/09/0600Z.json
//
// Prints PASS or the list of errors, and exits 1 on any error. Warnings never fail a run.
// No dependencies, Node 18 or later.
import { readFileSync } from 'node:fs';
import { walk } from './lib/files.mjs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { checkCapture as check, isId } from './lib/capture-check.mjs';
export { SCHEMA, snowflakeTime, snowflakeFor, runIdFor } from './lib/capture-check.mjs';

// The desks and their beats are data: contract/desks.json is the one list.
const DESK_FILE = JSON.parse(readFileSync(new URL('../contract/desks.json', import.meta.url), 'utf8'));
export const DESKS = DESK_FILE.desks.map((d) => d.id);
export const RETIRED = Object.fromEntries((DESK_FILE.retired ?? []).map((d) => [d.id, d.retired_at]));
export const BEATS = Object.fromEntries([...DESK_FILE.desks, ...(DESK_FILE.retired ?? [])].map((d) => [d.id, d.beats]));

// The checker with this repository's desks. opts.desks may still be given to check against another list.
export function checkCapture(doc, opts = {}) {
  return check(doc, { desks: DESK_FILE, ...opts, filePath: opts.filePath ? resolve(opts.filePath) : undefined });
}

// Post ids recorded by every capture that sorts before `filePath`, so a later run may
// send observations for a post without repeating its full record.
export function knownIdsBefore(filePath) {
  const target = resolve(filePath);
  let root = dirname(target);
  for (let i = 0; i < 3; i++) root = dirname(root); // capture/YYYY/MM/DD/file -> capture
  const ids = new Set();
  for (const p of walk(root, (name) => /^\d{4}Z\.json$/.test(name))) {
    if (!(p < target)) continue;
    try {
      for (const post of JSON.parse(readFileSync(p, 'utf8')).posts ?? []) if (post && isId(post.id)) ids.add(post.id);
    } catch { /* an unreadable earlier file contributes nothing */ }
  }
  return ids;
}

function main(argv) {
  const files = argv.filter((a) => !a.startsWith('-'));
  if (!files.length) {
    console.error('usage: node tools/check-capture.mjs capture/YYYY/MM/DD/HHMMZ.json [more files]');
    return 2;
  }
  let failed = 0;
  for (const file of files) {
    let doc;
    try { doc = JSON.parse(readFileSync(file, 'utf8')); }
    catch (e) { console.log(`FAIL ${file}\n  not readable JSON: ${e.message}`); failed++; continue; }
    // Only a file at capture/YYYY/MM/DD/HHMMZ.json is held to its path; the example in contract/ is not.
    const placed = /(^|[\\/])capture[\\/]\d{4}[\\/]\d{2}[\\/]\d{2}[\\/]\d{4}Z\.json$/.test(resolve(file));
    if (!placed) console.log(`  note     ${file} is not at capture/YYYY/MM/DD/HHMMZ.json, so its path was not checked`);
    const { errors, warnings } = checkCapture(doc, placed ? { known: knownIdsBefore(file), filePath: file } : {});
    for (const w of warnings) console.log(`  warning  ${w}`);
    if (errors.length) {
      failed++;
      console.log(`FAIL ${file} (${errors.length} error${errors.length === 1 ? '' : 's'})`);
      for (const e of errors) console.log(`  ${e}`);
    } else {
      const n = (doc.posts ?? []).length, o = (doc.observations ?? []).length;
      console.log(`PASS ${file} (${doc.run?.status}, ${n} posts, ${o} observations)`);
    }
  }
  return failed ? 1 : 0;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exit(main(process.argv.slice(2)));
}
