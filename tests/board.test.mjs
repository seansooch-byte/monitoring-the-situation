// The board (contract/BOARD.md): the agents' shared thread and the state derived from it.
// Pure functions in tools/lib/board.mjs; the Worker stores, these decide.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { checkMessage, openItems, stateOf, BOARD } from '../tools/lib/board.mjs';

const msg = (over = {}) => ({ from: 'claude', to: 'grokbot', channel: 'situation', kind: 'ask', subject: 'Why were 3 watch ids left out?', body: 'Six runs since 06Z say so.', ...over });

test('a well formed message passes, and every rule in contract/board.json is enforced', () => {
  assert.deepEqual(checkMessage(msg()), []);
  assert.deepEqual(checkMessage(msg({ to: 'all' })), [], 'all is a recipient');
  const bad = [
    [{ from: 'nobody' }, /from/], [{ from: 'all' }, /from/], [{ to: 'someone' }, /to/],
    [{ channel: 'crypto' }, /channel/], [{ kind: 'chat' }, /kind/],
    [{ subject: '' }, /subject/], [{ subject: 'two\nlines' }, /subject/], [{ subject: 'x'.repeat(BOARD.limits.subject + 1) }, /subject/],
    [{ body: 'x'.repeat(BOARD.limits.body + 1) }, /body/],
    [{ kind: 'answer', re: undefined }, /re/], [{ re: 0 }, /re/],
    [{ refs: Array(BOARD.limits.refs + 1).fill('a') }, /refs/],
    [{ status: { a: 1 } }, /status/],
    [{ kind: 'report', status: { big: 'x'.repeat(BOARD.limits.status_bytes) } }, /status/],
    [{ to: 'claude' }, /itself/],
    [{ extra: 1 }, /extra/],
  ];
  for (const [over, re] of bad) {
    const errs = checkMessage(msg(over));
    assert.ok(errs.some((e) => re.test(e)), `${JSON.stringify(over).slice(0, 60)} is refused (${errs.join('; ')})`);
  }
  assert.deepEqual(checkMessage(msg({ kind: 'report', to: 'all', status: { run: '2026-11-14T1900Z', reads_left: 396 } })), []);
  assert.ok(checkMessage(null).length, 'not an object');
});

const at = (h) => new Date(Date.UTC(2026, 10, 14, h)).toISOString().replace(/\.\d{3}Z$/, 'Z');
const thread = [
  { id: 1, at: at(10), ...msg() },                                                             // ask claude -> grokbot
  { id: 2, at: at(11), ...msg({ from: 'grokbot', to: 'claude', kind: 'answer', re: 1, subject: 'watch.json changed after the plan' }) },
  { id: 3, at: at(12), ...msg({ kind: 'notice', to: 'grokbot', subject: 'GRABBER.md: read the board each run' }) },
  { id: 4, at: at(13), ...msg({ from: 'grokbot', to: 'claude', kind: 'alert', subject: 'X returned 429 all run' }) },
  { id: 5, at: at(13), ...msg({ from: 'grokbot', to: 'claude', kind: 'answer', re: 4, subject: 'replying to my own alert' }) },
  { id: 6, at: at(14), ...msg({ from: 'editor', to: 'all', kind: 'ask', subject: 'Anyone know the FAA source?' }) },
  { id: 7, at: at(14), ...msg({ from: 'editor', to: 'all', kind: 'report', subject: 'pulse pass 1400Z', status: { pass: 'pulse', items: 29 } }) },
  { id: 8, at: at(15), ...msg({ from: 'grokbot', to: 'all', kind: 'report', subject: 'capture 1500Z', status: { run: '2026-11-14T1500Z', reads_left: 478 } }) },
  { id: 9, at: at(16), ...msg({ from: 'grokbot', to: 'all', kind: 'report', subject: 'capture 1600Z', status: { run: '2026-11-14T1600Z', reads_left: 442 } }) },
];

test('an ask, notice or alert is open until its addressee replies; a reply from anyone else does not close it', () => {
  const open = openItems(thread, at(17));
  assert.deepEqual(open.map((o) => o.id), [3, 4, 6], 'the answered ask (1) is closed; reports and answers are never open');
  const alert = open.find((o) => o.id === 4);
  assert.equal(alert.age_hours, 4);
  assert.equal(alert.overdue, true, `an alert is overdue after ${BOARD.kinds.alert.overdue_hours} hours`);
  assert.equal(open.find((o) => o.id === 3).overdue, false);
  const closed = openItems([...thread, { id: 10, at: at(17), ...msg({ from: 'grokbot', to: 'editor', kind: 'answer', re: 6, subject: 'CBS' }) }], at(17));
  assert.ok(!closed.some((o) => o.id === 6), 'an ask to all is closed by a reply from anyone but its sender');
});

test('the state is derived from the thread: who was seen when, each agent\'s latest report, and what waits on whom', () => {
  const cursors = [{ agent: 'grokbot', last_id: 9, seen_at: at(16) }, { agent: 'claude', last_id: 2, seen_at: at(11) }];
  const s = stateOf({ messages: thread, cursors, now: at(17), store: { last_run: { id: '2026-11-14T1600Z' } } });
  assert.equal(s.now, at(17));
  assert.deepEqual(Object.keys(s.agents).sort(), Object.keys(BOARD.agents).sort(), 'every agent appears, even one that never posted');
  assert.equal(s.agents.grokbot.last_report.status.reads_left, 442, 'the latest report wins');
  assert.equal(s.agents.grokbot.last_seen, at(16));
  assert.equal(s.agents.claude.unread, 6, 'claude has read up to 2; 3 is its own, so 4 to 9 are unread');
  assert.equal(s.agents.sean.last_seen, null);
  assert.equal(s.agents.editor.last_report.subject, 'pulse pass 1400Z');
  assert.deepEqual(s.waiting.grokbot.map((o) => o.id), [3, 6], 'what waits on grokbot: its notice and the open ask to all');
  assert.deepEqual(s.waiting.claude.map((o) => o.id), [4, 6]);
  assert.deepEqual(s.overdue.map((o) => o.id), [4]);
  assert.equal(s.last_id, 9);
  assert.equal(s.store.last_run.id, '2026-11-14T1600Z', 'the store\'s own facts ride along');
});
