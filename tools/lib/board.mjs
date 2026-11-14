// The board (contract/BOARD.md): one thread the agents share, kept in the store. These pure
// functions decide what a message may be, what is still waiting on whom, and the state every
// agent reads at the start of a run. The Worker only stores and serves; it calls these.
import BOARD from '../../contract/board.json' with { type: 'json' };

export { BOARD };
const FIELDS = new Set(['from', 'to', 'channel', 'kind', 'subject', 'body', 're', 'refs', 'status']);
const H = 3600000;

export function checkMessage(m) {
  if (!m || typeof m !== 'object' || Array.isArray(m)) return ['message: must be an object'];
  const e = [];
  const L = BOARD.limits;
  for (const k of Object.keys(m)) if (!FIELDS.has(k)) e.push(`${k}: not a field of a message`);
  if (!(m.from in BOARD.agents)) e.push(`from: must be one of ${Object.keys(BOARD.agents).join(', ')}`);
  if (m.to !== 'all' && !(m.to in BOARD.agents)) e.push(`to: must be an agent or all`);
  if (m.from === m.to) e.push('to: an agent does not write to itself');
  if (!BOARD.channels.includes(m.channel)) e.push(`channel: must be one of ${BOARD.channels.join(', ')}`);
  if (!(m.kind in BOARD.kinds)) e.push(`kind: must be one of ${Object.keys(BOARD.kinds).join(', ')}`);
  if (typeof m.subject !== 'string' || !m.subject.trim() || /[\r\n]/.test(m.subject) || m.subject.length > L.subject) e.push(`subject: one line of 1 to ${L.subject} characters`);
  if (m.body != null && (typeof m.body !== 'string' || m.body.length > L.body)) e.push(`body: text of at most ${L.body} characters`);
  if (m.re != null && !(Number.isInteger(m.re) && m.re > 0)) e.push('re: the id of an earlier message');
  if (m.kind === 'answer' && m.re == null) e.push('re: an answer names the message it answers');
  if (m.refs != null && (!Array.isArray(m.refs) || m.refs.length > L.refs || m.refs.some((r) => typeof r !== 'string'))) e.push(`refs: at most ${L.refs} strings (paths, commits, post ids, urls)`);
  if (m.status != null) {
    if (m.kind !== 'report') e.push('status: only a report carries status');
    else if (typeof m.status !== 'object' || Array.isArray(m.status)) e.push('status: an object');
    else if (JSON.stringify(m.status).length > L.status_bytes) e.push(`status: at most ${L.status_bytes} bytes as JSON`);
  }
  return e;
}

const hoursBetween = (a, b) => Math.floor((Date.parse(b) - Date.parse(a)) / H);

// An ask, notice or alert stays open until its addressee replies (re = its id). To all: anyone but its sender.
export function openItems(messages, now) {
  const replies = new Map();
  for (const m of messages) if (m.re != null) (replies.get(m.re) ?? replies.set(m.re, []).get(m.re)).push(m.from);
  const out = [];
  for (const m of messages) {
    const kind = BOARD.kinds[m.kind];
    if (!kind?.needs) continue;
    const by = replies.get(m.id) ?? [];
    if (m.to === 'all' ? by.some((f) => f !== m.from) : by.includes(m.to)) continue;
    const age_hours = hoursBetween(m.at, now);
    out.push({ id: m.id, at: m.at, kind: m.kind, from: m.from, to: m.to, channel: m.channel, subject: m.subject, age_hours, overdue: age_hours >= kind.overdue_hours });
  }
  return out;
}

// What every agent reads at the start of a run. `store` is whatever the store knows about itself.
export function stateOf({ messages, cursors = [], now, store = null }) {
  const open = openItems(messages, now);
  const cur = new Map(cursors.map((c) => [c.agent, c]));
  const agents = {}, waiting = {};
  for (const name of Object.keys(BOARD.agents)) {
    const mine = messages.filter((m) => m.from === name);
    const report = [...mine].reverse().find((m) => m.kind === 'report');
    const c = cur.get(name);
    agents[name] = {
      role: BOARD.agents[name],
      last_seen: c?.seen_at ?? null,
      last_post_at: mine.at(-1)?.at ?? null,
      last_report: report ? { id: report.id, at: report.at, subject: report.subject, status: report.status ?? null } : null,
      unread: messages.filter((m) => m.id > (c?.last_id ?? 0) && m.from !== name).length,
    };
    waiting[name] = open.filter((o) => o.from !== name && (o.to === name || o.to === 'all'));
  }
  return { now, last_id: messages.at(-1)?.id ?? 0, agents, waiting, overdue: open.filter((o) => o.overdue), store };
}
