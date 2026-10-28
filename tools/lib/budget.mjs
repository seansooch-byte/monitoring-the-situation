// The day's budget report: phase 0's done test (PROGRAM.md) as arithmetic over one UTC day of
// captures. Nothing here reads X or runs a model. The numbers come from contract/budget.json and
// the desks from contract/desks.json, so the report moves with the contract.
//
// Five checks make a day: every run ok, or short only for a reason on X's side; reads between
// the target and the ceiling; every desk swept at least at its cadence; every desk's counts never
// more than four hours apart; no story-cited post left off a run's re-read list.

const H = 3600000;

// Reads this run spent: the field, else the grabber's own sentence ("21 X reads this run").
export function readsOf(capture) {
  const r = capture?.run?.reads;
  if (Number.isInteger(r)) return r;
  const m = /(\d+) X reads/.exec(capture?.run?.reason ?? '');
  return m ? Number(m[1]) : null;
}

// Reads left in the UTC day after this run: the field, else the sentence ("936 to 915 left today").
export function readsLeftOf(capture) {
  const r = capture?.run?.reads_left;
  if (Number.isInteger(r)) return r;
  const m = /to (\d+) left today/.exec(capture?.run?.reason ?? '');
  return m ? Number(m[1]) : null;
}

export const dayOf = (capture) => (capture?.run?.started_at ?? '').slice(0, 10);

// A run that fell short is excused only when the reason is on X's side. "no 429 refusals" is
// the grabber saying the opposite, so such phrases are removed before looking.
export function xSide(reason, budget) {
  const r = (reason ?? '').toLowerCase().replace(/\bno (429|rate limits?|refusals?)[^.;,]*/g, '');
  if (/cut order/.test(r)) return false;
  return budget.x_side_reasons.some((s) => r.includes(s.toLowerCase()));
}

export function summarizeDay(captures, { desks, budget, cited = [], ledger = {}, hoursInDay = 24 }) {
  const caps = [...captures].filter((c) => c?.run?.started_at).sort((a, b) => (a.run.started_at < b.run.started_at ? -1 : 1));
  const date = dayOf(caps[0]);
  const dayStart = Date.parse(`${date}T00:00:00Z`);
  const partial_day = hoursInDay < 24;

  const runs = { n: caps.length, ok: 0, partial: 0, down: 0, bad: [] };
  for (const c of caps) {
    runs[c.run.status] = (runs[c.run.status] ?? 0) + 1;
    if (c.run.status !== 'ok' && !xSide(c.run.reason, budget)) runs.bad.push({ id: c.run.id, status: c.run.status, reason: String(c.run.reason ?? '').slice(0, 140) });
  }

  const reads = { total: 0, known: 0, unknown: 0, min: null, max: null };
  for (const c of caps) {
    const r = readsOf(c);
    if (r == null) { reads.unknown++; continue; }
    reads.total += r; reads.known++;
    reads.min = reads.min == null ? r : Math.min(reads.min, r);
    reads.max = reads.max == null ? r : Math.max(reads.max, r);
  }

  const sweptOk = (c, id) => (c.sweeps ?? []).some((s) => s.id === id && (s.status === 'ok' || s.status === 'partial'));
  const desksOut = desks.desks.map((d) => {
    const swept = caps.filter((c) => sweptOk(c, `desk.${d.id}`)).length;
    const expected = Math.floor(hoursInDay / d.sweep_every_hours);
    return { id: d.id, every: d.sweep_every_hours, expected, swept, ok: swept >= expected };
  });

  const every = budget.volume.every_hours * H;
  const volumeOut = desks.desks.map((d) => {
    const times = caps
      .filter((c) => (c.volume ?? []).some((v) => v.key === `desk.${d.id}`) || (c.sweeps ?? []).some((s) => s.id === `volume.${d.id}` && s.status === 'ok'))
      .map((c) => Date.parse(c.run.started_at)).sort((a, b) => a - b);
    const edges = [dayStart, ...times, dayStart + hoursInDay * H];
    let maxGap = 0;
    for (let i = 1; i < edges.length; i++) maxGap = Math.max(maxGap, edges[i] - edges[i - 1]);
    return { id: d.id, readings: times.length, max_gap_h: Math.round((maxGap / H) * 10) / 10, ok: times.length > 0 && maxGap <= every };
  });

  const watch = { max_left_out: 0, worst_run: null, left_out_ids: [] };
  for (const c of caps) {
    const w = (c.sweeps ?? []).find((s) => s.id === 'watch');
    if (!w || !Array.isArray(w.post_ids)) continue;
    const have = new Set(w.post_ids);
    const missing = cited.filter((id) => { const first = ledger[id]?.first_run; return first && first < c.run.id && !have.has(id); });
    if (missing.length > watch.max_left_out) Object.assign(watch, { max_left_out: missing.length, worst_run: c.run.id, left_out_ids: missing });
  }

  const answered = new Set();
  for (const c of caps) for (const a of c.answers ?? []) answered.add(a.request_id ?? a.id);

  const checks = {
    runs: runs.bad.length === 0,
    reads: !partial_day && reads.unknown === 0 && reads.total >= budget.target_min && reads.total <= budget.ceiling,
    desks: desksOut.every((d) => d.ok),
    volume: volumeOut.every((v) => v.ok),
    watch: watch.max_left_out === 0,
  };
  return { date, partial_day, hours: hoursInDay, runs, reads, desks: desksOut, volume: volumeOut, watch, requests: { answered_today: answered.size }, checks, pass: Object.values(checks).every(Boolean) };
}

// One day as lines Sean can read. The first line is the verdict; the rest say what fell short.
export function formatDay(s) {
  const verdict = s.partial_day ? 'so far' : s.pass ? 'PASS' : 'FAIL';
  const desksOk = s.desks.filter((d) => d.ok).length;
  const volOk = s.volume.filter((v) => v.ok).length;
  const lines = [
    `${s.date}  ${verdict}  runs ${s.runs.n} (${s.runs.ok ?? 0} ok, ${s.runs.partial ?? 0} partial, ${s.runs.down ?? 0} down)  reads ${s.reads.total}${s.reads.unknown ? ` + ${s.reads.unknown} unknown` : ''} (${s.reads.min ?? '?'} to ${s.reads.max ?? '?'} a run)  desks ${desksOk}/${s.desks.length} at cadence  counts ${volOk}/${s.volume.length} within 4 h  re-read list left out ${s.watch.max_left_out} story-cited`,
  ];
  if (!s.checks.runs) {
    const b = s.runs.bad[0];
    lines.push(`  runs: ${s.runs.bad.length} fell short for our own reasons, e.g. ${b.id} ${b.status}: ${b.reason}`);
  }
  if (!s.partial_day && !s.checks.reads) lines.push(`  reads: ${s.reads.unknown ? `unknown for ${s.reads.unknown} run${s.reads.unknown === 1 ? '' : 's'}; ` : ''}${s.reads.total} against a target of ${'600 to 850'}`);
  if (!s.checks.desks) lines.push(`  desks under cadence: ${s.desks.filter((d) => !d.ok).map((d) => `${d.id} ${d.swept}/${d.expected}`).join(', ')}`);
  if (!s.checks.volume) lines.push(`  counts: ${s.volume.filter((v) => !v.ok).map((v) => `${v.id} ${v.readings === 0 ? 'none' : `${v.readings}, gap ${v.max_gap_h} h`}`).join(', ')}`);
  if (!s.checks.watch) lines.push(`  re-reads: ${s.watch.worst_run} left out ${s.watch.max_left_out} story-cited post${s.watch.max_left_out === 1 ? '' : 's'} (${s.watch.left_out_ids.slice(0, 5).join(', ')}${s.watch.left_out_ids.length > 5 ? ', ...' : ''})`);
  return lines.join('\n');
}
