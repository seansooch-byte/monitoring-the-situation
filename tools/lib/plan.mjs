// The read planner: the next run's read list, in order, with a budget line for each read.
// The grabber executes it and records what it did; the cut order lives here, where Sean can read
// it, and not in the grabber's judgement. Deterministic: the same captures, requests, desks,
// budget and clock give the same plan, so anyone can regenerate the plan a run was given.
//
// Order of reads: the re-read list (never cut), the desks that are due, the five stalest desks'
// counts (never cut), the editor's unanswered requests, then discovery (trends, sensors, the
// global streams, context) and a screening reserve. When the day is short the list is cut from
// the end in contract/budget.json's cut_order.
import { seriesByPost } from './metrics.mjs';
import { readsOf, readsLeftOf } from './budget.mjs';

const H = 3600000;
const iso = (ms) => new Date(ms).toISOString().replace('.000Z', 'Z');
const hourId = (ms) => `${iso(ms).slice(0, 10)}T${iso(ms).slice(11, 13)}Z`;
const idMod = (id, n) => (/^\d+$/.test(id) ? Number(BigInt(id) % BigInt(n)) : 0);

export function planReads({ captures, watchIds = [], openRequests = [], answered = new Set(), desks, budget, now = Date.now() }) {
  const caps = [...captures].filter((c) => c?.run?.started_at).sort((a, b) => (a.run.started_at < b.run.started_at ? -1 : 1));
  const nowMs = now instanceof Date ? now.getTime() : typeof now === 'number' ? now : Date.parse(now);
  const forRunMs = Math.ceil(nowMs / H) * H;
  const hour = new Date(forRunMs).getUTCHours();
  const band = budget.bands.find((b) => b.hours_utc.includes(hour));
  const date = iso(forRunMs).slice(0, 10);
  const hoursLeft = 24 - hour;

  // ---- the day's budget
  const latest = caps.at(-1);
  let readsLeftBefore;
  if (latest && latest.run.started_at.slice(0, 10) === date) {
    readsLeftBefore = readsLeftOf(latest);
    if (readsLeftBefore == null) {
      const spent = caps.filter((c) => c.run.started_at.slice(0, 10) === date).reduce((n, c) => n + (readsOf(c) ?? band.cap), 0);
      readsLeftBefore = Math.max(0, budget.reads_per_day - spent);
    }
  } else {
    readsLeftBefore = budget.reads_per_day;
  }
  const allowedLeft = readsLeftBefore - (budget.reads_per_day - budget.ceiling);
  const short = allowedLeft < budget.underspend_floor * hoursLeft;
  const allowance = short ? Math.max(0, Math.floor(allowedLeft / hoursLeft)) : band.cap;

  // ---- the re-read list
  const series = seriesByPost(caps);
  const withViews = (id) => (series.get(id) ?? []).filter((o) => Number.isFinite(o.views));
  const firstSeen = (id) => series.get(id)?.[0]?.at ?? Infinity;
  const gone = (id) => series.get(id)?.at(-1)?.state === 'unavailable';
  const gain = (id, back) => { const s = withViews(id); if (s.length < back + 1) return null; const a = s.at(-(back + 1)).views; return a > 0 ? (s.at(-1).views - a) / a : null; };
  const flat = (id) => { const g = gain(id, budget.rereads.flat_readings - 1); return g != null && g < budget.rereads.gain_min; };
  const hourIndex = Math.floor(forRunMs / H);
  const turn = (id) => (hourIndex + idMod(id, budget.rereads.flat_every)) % budget.rereads.flat_every === 0;
  const lastViews = (id) => withViews(id).at(-1)?.views ?? 0;
  const byGain = (a, b) => (gain(b, 1) ?? -1) - (gain(a, 1) ?? -1) || (a < b ? -1 : 1);

  // watch.json is read in full, first, every run (GRABBER.md, Re-reads: "never dropped"): no slowing,
  // no cap, not even for a post X stopped returning, since reading it is how the record learns it came
  // back. The band's cap and the flat-post slowing ration only the other re-reads.
  const watchSet = new Set(watchIds);
  const ids = [...watchSet];
  const groups = [];
  const recent = [...series.keys()].filter((id) => forRunMs - firstSeen(id) < 24 * H);
  groups.push(recent.filter((id) => forRunMs - firstSeen(id) < budget.rereads.fresh_hours * H).sort((a, b) => lastViews(b) - lastViews(a) || (a < b ? -1 : 1)));
  groups.push(recent.filter((id) => forRunMs - firstSeen(id) >= budget.rereads.fresh_hours * H && (gain(id, 1) ?? 0) >= budget.rereads.gain_min).sort(byGain));
  if (hour % budget.rereads.rest_every_hours === 0) groups.push(recent.sort(byGain));

  const left = { slowed: 0, over_cap: 0, unavailable: 0 };
  const seen = new Set(watchSet);
  const others = [];
  for (const g of groups) for (const id of g) {
    if (seen.has(id)) continue;
    seen.add(id);
    if (gone(id)) { left.unavailable++; continue; }
    if (flat(id) && !turn(id)) { left.slowed++; continue; }
    others.push(id);
  }
  const room = Math.max(0, band.rereads - ids.length);
  if (others.length > room) left.over_cap = others.length - room;
  ids.push(...others.slice(0, room));

  // ---- what is due
  const lastSweep = (id) => { let t = null; for (const c of caps) if ((c.sweeps ?? []).some((s) => s.id === id && (s.status === 'ok' || s.status === 'partial'))) t = Date.parse(c.run.started_at); return t; };
  const lastCount = (desk) => { let t = null; for (const c of caps) if ((c.volume ?? []).some((v) => v.key === `desk.${desk}`) || (c.sweeps ?? []).some((s) => s.id === `volume.${desk}` && s.status === 'ok')) t = Date.parse(c.run.started_at); return t; };
  const tolerance = 30 * 60000;
  const due = desks.desks.filter((d) => { const t = lastSweep(`desk.${d.id}`); return t == null || forRunMs - t >= d.sweep_every_hours * H - tolerance; });
  const notDue = desks.desks.filter((d) => !due.includes(d)).map((d) => d.id);
  const stale = desks.desks
    .map((d, i) => ({ id: d.id, i, age: lastCount(d.id) == null ? Infinity : forRunMs - lastCount(d.id) }))
    .filter((d) => d.age >= budget.volume.every_hours * H - tolerance)
    .sort((a, b) => b.age - a.age || a.i - b.i)
    .slice(0, budget.volume.desks_per_run);
  const waiting = openRequests.filter((r) => !answered.has(r.id)).map((r) => r.id).sort();
  const groupIds = (desks.groups ?? []).map((g) => g.id);
  const half = Math.ceil(groupIds.length / 2);
  const sensorGroups = (hour % 2 === 0 ? groupIds.slice(0, half) : groupIds.slice(half)).slice(0, budget.sensor_groups_per_run);

  // ---- the list
  const items = [];
  const push = (sweep, reads, extra = {}) => items.push({ sweep, reads, ...extra });
  if (ids.length) push('watch', Math.ceil(ids.length / budget.ids_per_read), { ids, why: `all ${watchSet.size} from watch.json, then posts under ${budget.rereads.fresh_hours} h old, then posts gaining ${Math.round(budget.rereads.gain_min * 100)} percent${hour % budget.rereads.rest_every_hours === 0 ? ', then the rest of the last 24 h (a fourth hour)' : ''}; ${left.slowed} flat posts outside watch.json wait for their sixth run` });
  for (const d of due) { const t = lastSweep(`desk.${d.id}`); push(`desk.${d.id}`, budget.reads.desk, { every: d.sweep_every_hours, why: t == null ? 'never swept' : `due: every ${d.sweep_every_hours} h, last ${iso(t)}` }); }
  for (const d of stale) push(`volume.${d.id}`, budget.reads.volume, { why: d.age === Infinity ? 'never counted' : `counts ${Math.round(d.age / H)} h old` });
  for (const id of waiting.slice(0, budget.requests_per_run)) push(`request.${id}`, budget.reads.request, { why: 'open in requests/open.json, not yet answered' });
  push('trends.us', budget.reads['trends.us']);
  push('trends.ww', budget.reads['trends.ww']);
  for (const g of sensorGroups) push(`sensors.${g}`, budget.reads.sensors);
  push('viral.global', budget.reads['viral.global']);
  push('rising.global', budget.reads['rising.global']);
  push('context.top', budget.reads['context.top']);
  push('screen', budget.reads.screen, { why: 'reads by id to screen candidates; the one line the grabber sizes itself' });

  // ---- cut to the allowance, in the contract's order; never the re-read list, never the counts
  const total = () => items.reduce((n, it) => n + it.reads, 0);
  const cut = [];
  for (const rule of budget.cut_order) {
    if (total() <= allowance) break;
    const matches = (it) => (rule.startsWith('desk:') ? it.sweep.startsWith('desk.') && it.every === Number(rule.slice(5)) : rule === 'sensors' ? it.sweep.startsWith('sensors.') : rule === 'request' ? it.sweep.startsWith('request.') : it.sweep === rule);
    for (let i = items.length - 1; i >= 0 && total() > allowance; i--) if (matches(items[i])) cut.push(items.splice(i, 1)[0].sweep);
  }
  const total_reads = total();

  return {
    schema: 'mts.plan/1',
    written_at: iso(nowMs),
    for_run: hourId(forRunMs),
    band: band.id,
    mode: 'normal',
    day: { date, reads_left_before: readsLeftBefore, hours_left: hoursLeft, short, rule: short ? `short: ${allowedLeft} may still be spent over ${hoursLeft} runs` : `the ${band.id} band's cap` },
    allowance,
    total_reads,
    over_budget: total_reads > allowance,
    items: items.map((it, i) => ({ n: i + 1, ...it })),
    cut,
    left_out: { rereads: left, desks_not_due: notDue, requests_waiting: Math.max(0, waiting.length - budget.requests_per_run) },
    inputs: { captures: caps.length, first: caps[0]?.run.id ?? null, last: latest?.run.id ?? null, watch_ids: watchIds.length, open_requests: openRequests.length },
  };
}
