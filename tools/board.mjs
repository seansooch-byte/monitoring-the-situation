#!/usr/bin/env node
// The board's command line (contract/BOARD.md). Every agent starts a run with `inbox` and ends it with `post --kind report`.
//
//   node tools/board.mjs state [--json]
//   node tools/board.mjs inbox --as <agent> [--peek] [--json]        new messages + what waits on you; marks them read unless --peek
//   node tools/board.mjs post  --as <agent> --to <agent|all> --kind <kind> --subject "..." [--body "..." | --body-file f | --body -]
//                              [--channel situation] [--re <id>] [--refs a,b] [--status '{"json":1}']
//   node tools/board.mjs reply <id> --as <agent> --subject "..." [--body ...]   an answer to <id>, sent to its author
//   node tools/board.mjs thread [--since N] [--channel c] [--json]
//
// Token and address: tools/lib/store.mjs (MTS_TOKEN or store.local.token; MTS_STORE_URL).
import { readFileSync } from 'node:fs';
import { storeClient } from './lib/store.mjs';
import { checkMessage } from './lib/board.mjs';

const [cmd, ...rest] = process.argv.slice(2);
const args = { _: [] };
for (let i = 0; i < rest.length; i++) {
  const a = rest[i];
  if (a.startsWith('--')) { const k = a.slice(2); const v = rest[i + 1]; if (v === undefined || (v.startsWith('--') && v !== '-')) args[k] = true; else { args[k] = v; i++; } }
  else args._.push(a);
}
const die = (msg) => { console.error(msg); process.exit(2); };
const store = storeClient();
const line = (m) => `#${m.id} ${m.at} ${m.channel} ${m.kind.toUpperCase()} ${m.from} -> ${m.to}${m.re ? ` (re #${m.re})` : ''}: ${m.subject}`;
const show = (m) => [line(m), m.body ? m.body.replace(/^/gm, '    ') : null, m.refs?.length ? `    refs: ${m.refs.join(', ')}` : null, m.status ? `    status: ${JSON.stringify(m.status)}` : null].filter(Boolean).join('\n');
const item = (o) => `#${o.id} ${o.kind.toUpperCase()} from ${o.from} (${o.age_hours} h${o.overdue ? ', OVERDUE' : ''}): ${o.subject}`;
const body = () => args['body-file'] ? readFileSync(args['body-file'], 'utf8') : args.body === '-' ? readFileSync(0, 'utf8') : (typeof args.body === 'string' ? args.body : undefined);

async function post(m) {
  for (const k of Object.keys(m)) if (m[k] === undefined) delete m[k];
  const errs = checkMessage(m);
  if (errs.length) die(`not posted:\n  ${errs.join('\n  ')}`);
  const r = await store.post('/api/board', m);
  console.log(`posted #${r.id} at ${r.at}`);
}

if (cmd === 'state') {
  const s = await store.get('/api/state');
  if (args.json) { console.log(JSON.stringify(s, null, 2)); process.exit(0); }
  console.log(`board at ${s.now}, last message #${s.last_id}`);
  if (s.store?.last_run) console.log(`store: last run ${s.store.last_run.id} (${s.store.last_run.status}, ${s.store.last_run.reads_left ?? '?'} reads left)`);
  for (const [name, a] of Object.entries(s.agents)) {
    console.log(`\n${name}: seen ${a.last_seen ?? 'never'}, ${a.unread} unread, ${s.waiting[name].length} waiting on it`);
    if (a.last_report) console.log(`  last report #${a.last_report.id} ${a.last_report.at}: ${a.last_report.subject}`);
    for (const o of s.waiting[name]) console.log(`  ${item(o)}`);
  }
  if (s.overdue.length) console.log(`\nOVERDUE: ${s.overdue.map((o) => `#${o.id} (${o.from} -> ${o.to})`).join(', ')}`);
} else if (cmd === 'inbox') {
  const as = args.as; if (typeof as !== 'string') die('inbox needs --as <agent>');
  const [s, t] = await Promise.all([store.get('/api/state'), store.get(`/api/board?as=${as}&limit=1000`)]);
  const fresh = t.messages.filter((m) => m.from !== as);
  if (args.json) console.log(JSON.stringify({ waiting: s.waiting[as], new: fresh, agents: s.agents, overdue: s.overdue, store: s.store }, null, 2));
  else {
    console.log(`${as}: ${fresh.length} new since #${t.since}; ${s.waiting[as].length} waiting on you`);
    for (const o of s.waiting[as]) console.log(`  WAITING ${item(o)}`);
    for (const m of fresh) console.log(show(m));
    const others = Object.entries(s.agents).filter(([n]) => n !== as).map(([n, a]) => `${n} seen ${a.last_seen ?? 'never'}`);
    console.log(`others: ${others.join('; ')}`);
    if (s.overdue.length) console.log(`OVERDUE on the board: ${s.overdue.map((o) => `#${o.id} ${o.from} -> ${o.to}`).join(', ')}`);
  }
  if (!args.peek) await store.post('/api/board/seen', { as, id: t.messages.at(-1)?.id ?? t.since });
} else if (cmd === 'post') {
  await post({ from: args.as, to: args.to, channel: args.channel ?? 'situation', kind: args.kind, subject: args.subject, body: body(), re: args.re ? Number(args.re) : undefined, refs: args.refs ? String(args.refs).split(',') : undefined, status: args.status ? JSON.parse(args.status) : undefined });
} else if (cmd === 'reply') {
  const id = Number(args._[0]); if (!id) die('reply needs the id of the message');
  const { messages } = await store.get(`/api/board?since=${id - 1}&limit=1`);
  const orig = messages[0]; if (!orig || orig.id !== id) die(`no message #${id}`);
  await post({ from: args.as, to: orig.from === args.as ? orig.to : orig.from, channel: orig.channel, kind: args.kind ?? 'answer', subject: args.subject, body: body(), re: id, refs: args.refs ? String(args.refs).split(',') : undefined });
} else if (cmd === 'thread') {
  const q = new URLSearchParams({ since: String(args.since ?? 0), limit: '1000', ...(args.channel ? { channel: args.channel } : {}) });
  const { messages } = await store.get(`/api/board?${q}`);
  console.log(args.json ? JSON.stringify(messages, null, 2) : messages.map(show).join('\n'));
} else die('commands: state, inbox, post, reply, thread (see the top of tools/board.mjs)');
