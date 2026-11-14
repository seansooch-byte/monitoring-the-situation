#!/usr/bin/env node
// Build one edition of the paper from this repo's record (contract/PAPER.md).
//
//   node tools/edition.mjs [--day 2026-11-13] [--out dist/data/edition]
//
// Expected behaviour:
//   - The day defaults to yesterday, Eastern. The edition is written to <out>/<day>.json and a one-line
//     summary is printed. Nothing else is written.
//   - The record is read from files: the captures from three days before the day to one day after
//     (enough to find each post's reading at the day's start), verified/posts.json, moments/,
//     contract/desks.json, contract/paper.json, and newsletter/<day>.json when there is one.
//   - The editor's lines come from the history of pulse/current.json: every version committed from 36
//     hours before the day to its end, the latest line for each post winning. Commits are history, so
//     a past day's edition does not change when the pulse moves on.
//   - All the rules are in tools/lib/edition.mjs. A broken letter stops the build: exit 1, with the
//     reasons, and no file written.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { walk } from './lib/files.mjs';
import { dayBounds, dayKey } from './lib/clock.mjs';
import { buildEdition } from './lib/edition.mjs';
import { linesBetween, pulseHistory } from './lib/pulse-history.mjs';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const HOUR = 3600000;
const readJSON = (p) => JSON.parse(readFileSync(p, 'utf8'));

function arg(name, fallback) {
  const i = process.argv.indexOf(name);
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const day = arg('--day', dayKey(Date.now() - 24 * HOUR));
const out = arg('--out', join(REPO, 'dist', 'data', 'edition'));
const [start, end] = dayBounds(day);

// Captures whose folder date falls from three days before to one day after.
const folders = new Set();
for (let t = start - 3 * 24 * HOUR; t <= end + 24 * HOUR; t += 24 * HOUR) folders.add(new Date(t).toISOString().slice(0, 10).replaceAll('-', '/'));
const posts = new Map();
const observations = [];
for (const f of [...folders].sort()) {
  for (const file of walk(join(REPO, 'capture', f), (n) => n.endsWith('.json'))) {
    let c;
    try { c = readJSON(file); } catch { continue; }
    // A post is captured again and again; a later capture may carry it with no desk (as a reference), so
    // a field is filled once and a blank never overwrites it.
    for (const p of c.posts ?? []) {
      const had = posts.get(p.id);
      if (!had) { posts.set(p.id, { ...p }); continue; }
      for (const [k, v] of Object.entries(p)) if (had[k] == null || (Array.isArray(had[k]) && !had[k].length && Array.isArray(v) && v.length)) had[k] = v;
    }
    for (const o of c.observations ?? []) observations.push(o);
  }
}

// The editor's lines, from the pulse's history.
const lines = linesBetween(pulseHistory(REPO), start, end);

const moments = walk(join(REPO, 'moments'), (n) => n.endsWith('.json')).map(readJSON);
const letterFile = join(REPO, 'newsletter', `${day}.json`);

let edition;
try {
  edition = buildEdition({
    day,
    desks: readJSON(join(REPO, 'contract', 'desks.json')),
    paper: readJSON(join(REPO, 'contract', 'paper.json')),
    posts: [...posts.values()],
    observations,
    ledger: readJSON(join(REPO, 'verified', 'posts.json')),
    moments,
    lines,
    letter: existsSync(letterFile) ? readJSON(letterFile) : null,
  });
} catch (err) {
  console.error(`edition ${day}: refused. ${err.message}`);
  process.exit(1);
}

mkdirSync(out, { recursive: true });
writeFileSync(join(out, `${day}.json`), JSON.stringify(edition, null, 1) + '\n');
const lead = edition.stories[0];
const m = (n) => `${(n / 1e6).toFixed(1)}M`;
console.log(`edition ${day}: ${lead ? `lead ${lead.id} (${m(lead.reach)})` : 'no story'}, ${edition.counts.stories} stories, ` +
  `${edition.unreported.length} not yet a story, ${edition.watched.length} watched, ${edition.counts.posts} posts, ${m(edition.counts.views)} views on the day` +
  `${edition.letter ? ', with the letter' : ', no letter'}`);
