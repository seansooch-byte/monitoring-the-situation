#!/usr/bin/env node
// Writes requests/plan.json: the next run's read list, in order, with a budget line each.
//
//   node tools/plan-reads.mjs                 plan the next hour from the repository as it is
//   node tools/plan-reads.mjs --at 2026-10-28T03:40:00Z
//   node tools/plan-reads.mjs --print         print the plan instead of writing it
//
// Deterministic: the same captures, requests, desks, contract/budget.json and clock give the
// same file, so the plan any run was given can be regenerated. The format is contract/PLAN.md.
// A request is asked while it is under three days old and unanswered in the last three days of
// captures; older ones are the editor's to prune and are counted, not asked.
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { walk } from './lib/files.mjs';
import { planReads } from './lib/plan.mjs';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const readJSON = (p) => JSON.parse(readFileSync(p, 'utf8'));
const args = process.argv.slice(2);
const opt = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : fallback; };
const H = 3600000;

const at = Date.parse(opt('--at', new Date().toISOString()));
if (isNaN(at)) { console.error('--at must be a UTC time like 2026-10-28T03:40:00Z'); process.exit(2); }
const REQUEST_AGE_DAYS = 3;
const WINDOW_H = REQUEST_AGE_DAYS * 24;   // long enough to see every answer a live request has had

const DESKS = readJSON(join(REPO, 'contract', 'desks.json'));
const BUDGET = readJSON(join(REPO, 'contract', 'budget.json'));
const watchFile = join(REPO, 'requests', 'watch.json');
const openFile = join(REPO, 'requests', 'open.json');
const watchIds = existsSync(watchFile) ? readJSON(watchFile).post_ids ?? [] : [];
const open = existsSync(openFile) ? readJSON(openFile).requests ?? [] : [];

// Only the capture files whose path dates fall inside the window are parsed.
const days = new Set();
for (let t = at - WINDOW_H * H; t <= at + H; t += 86400000) days.add(new Date(t).toISOString().slice(0, 10));
days.add(new Date(at + H).toISOString().slice(0, 10));
const files = walk(join(REPO, 'capture'), (n) => /^\d{4}Z\.json$/.test(n)).filter((p) => { const m = /(\d{4})\/(\d{2})\/(\d{2})\/\d{4}Z\.json$/.exec(p); return m && days.has(`${m[1]}-${m[2]}-${m[3]}`); });
const captures = files.map(readJSON).filter((c) => { const t = Date.parse(c.run?.started_at ?? ''); return !isNaN(t) && t >= at - WINDOW_H * H && t <= at; });

const answered = new Set();
for (const c of captures) for (const a of c.answers ?? []) answered.add(a.request_id ?? a.id);
const dated = (id) => { const m = /^r-(\d{4}-\d{2}-\d{2})/.exec(id); return m ? Date.parse(`${m[1]}T00:00:00Z`) : null; };
const openRequests = open.filter((r) => { const d = dated(r.id); return d == null || at - d <= REQUEST_AGE_DAYS * 86400000; });
const stale = open.length - openRequests.length;

const plan = planReads({ captures, watchIds, openRequests, answered, desks: DESKS, budget: BUDGET, now: at });
plan.left_out.requests_stale = stale;

const watch = plan.items.find((i) => i.sweep === 'watch');
const count = (prefix) => plan.items.filter((i) => i.sweep.startsWith(prefix)).length;
const line = `plan ${plan.for_run} (${plan.band}): ${plan.total_reads} reads of ${plan.allowance}${plan.over_budget ? ' OVER BUDGET' : ''}; watch ${watch ? `${watch.reads} reads, ${watch.ids.length} ids` : 'none'} (${plan.left_out.rereads.slowed} slowed, ${plan.left_out.rereads.over_cap} over cap); desks ${count('desk.')} due, ${plan.left_out.desks_not_due.length} not; counts ${count('volume.')}; requests ${count('request.')} asked, ${plan.left_out.requests_waiting} waiting, ${stale} stale; cut ${plan.cut.length ? plan.cut.join(' ') : 'nothing'}; day ${plan.day.reads_left_before} left before, ${plan.day.hours_left} runs left${plan.day.short ? ', SHORT' : ''}; from ${plan.inputs.captures} captures (${plan.inputs.first} to ${plan.inputs.last})`;

if (args.includes('--print')) console.log(JSON.stringify(plan, null, 1));
else writeFileSync(join(REPO, 'requests', 'plan.json'), JSON.stringify(plan, null, 1) + '\n');
console.log(line);
