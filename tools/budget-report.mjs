#!/usr/bin/env node
// The day's budget report: phase 0's done test (PROGRAM.md), read from the captures.
//
//   node tools/budget-report.mjs                the last 7 full UTC days
//   node tools/budget-report.mjs --days 3       the last 3
//   node tools/budget-report.mjs --day 2026-10-27
//   node tools/budget-report.mjs --today        today so far, judged on the hours that have run
//
// Prints one verdict line per day and what fell short. Exits 0 when every full day asked for
// passed, 1 otherwise. No model, no X: arithmetic over the record and contract/budget.json.
import { existsSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { walk } from './lib/files.mjs';
import { summarizeDay, formatDay } from './lib/budget.mjs';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const readJSON = (p) => JSON.parse(readFileSync(p, 'utf8'));
const args = process.argv.slice(2);
const opt = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : fallback; };

const DESKS = readJSON(join(REPO, 'contract', 'desks.json'));
const BUDGET = readJSON(join(REPO, 'contract', 'budget.json'));
const ledgerFile = join(REPO, 'verified', 'posts.json');
const raw = existsSync(ledgerFile) ? readJSON(ledgerFile) : {};
const LEDGER = raw.posts ?? raw;

// Story-cited posts: everything a story or the pulse cites. These are never to be left off a re-read list.
const cited = new Set();
for (const f of walk(join(REPO, 'moments'), (n) => n.endsWith('.json'))) for (const p of readJSON(f).posts ?? []) cited.add(p.id);
const pulseFile = join(REPO, 'pulse', 'current.json');
if (existsSync(pulseFile)) for (const it of readJSON(pulseFile).items ?? []) cited.add(it.id);

const todayUTC = new Date().toISOString().slice(0, 10);
const dayBefore = (d, n) => new Date(Date.parse(`${d}T00:00:00Z`) - n * 86400000).toISOString().slice(0, 10);
let days;
if (args.includes('--today')) days = [todayUTC];
else if (opt('--day')) days = [opt('--day')];
else { const n = Number(opt('--days', 7)); days = Array.from({ length: n }, (_, i) => dayBefore(todayUTC, n - i)); }

const wanted = new Set(days);
const files = walk(join(REPO, 'capture'), (n) => /^\d{4}Z\.json$/.test(n)).filter((p) => { const m = /(\d{4})\/(\d{2})\/(\d{2})\/\d{4}Z\.json$/.exec(p); return m && wanted.has(`${m[1]}-${m[2]}-${m[3]}`); });
const byDay = new Map(days.map((d) => [d, []]));
for (const f of files) { const c = readJSON(f); const d = (c.run?.started_at ?? '').slice(0, 10); if (byDay.has(d)) byDay.get(d).push(c); }

let passed = 0, judged = 0;
for (const d of days) {
  const caps = byDay.get(d);
  if (!caps.length) { console.log(`${d}  no captures`); judged++; continue; }
  const today = d === todayUTC;
  const hoursInDay = today ? new Date().getUTCHours() + 1 : 24;
  const s = summarizeDay(caps, { desks: DESKS, budget: BUDGET, cited: [...cited], ledger: LEDGER, hoursInDay });
  console.log(formatDay(s));
  if (!today) { judged++; if (s.pass) passed++; }
}
if (judged) console.log(`${passed} of ${judged} full days PASS`);
process.exit(judged && passed === judged ? 0 : 1);
