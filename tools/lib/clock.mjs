// The site's clock. Every time a reader sees is Eastern time. Captures, post ids and every stored
// timestamp stay in UTC; only the words on the page are converted, here and nowhere else.
//
// The label is ET, not EST or EDT: it is right all year, and the zone's own rule supplies the
// summer and the winter hour (four behind UTC in October, five in December).
export const ZONE = 'America/New_York';
export const ZONE_LABEL = 'ET';

const format = new Intl.DateTimeFormat('en-US', { timeZone: ZONE, hourCycle: 'h23', hour: '2-digit', minute: '2-digit', weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' });
function parts(ms) {
  const out = {};
  for (const p of format.formatToParts(new Date(ms))) out[p.type] = p.value;
  return out;
}

// 04:12
export function clockTime(ms) { const p = parts(ms); return `${p.hour}:${p.minute}`; }
// 9 Oct 2026. Also the key for "the same day" when stories are grouped by day.
export function dateOf(ms) { const p = parts(ms); return `${p.day} ${p.month} ${p.year}`; }
// Fri 9 Oct 2026
export function dayOf(ms) { return `${parts(ms).weekday} ${dateOf(ms)}`; }

// The paper's day (contract/PAPER.md): an Eastern calendar day, midnight to midnight.
const keyFormat = new Intl.DateTimeFormat('en-CA', { timeZone: ZONE, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hourCycle: 'h23' });
function keyParts(ms) {
  const out = {};
  for (const p of keyFormat.formatToParts(new Date(ms))) out[p.type] = p.value;
  return out;
}
// 2026-11-13: the Eastern day a moment falls in.
export function dayKey(ms) { const p = keyParts(ms); return `${p.year}-${p.month}-${p.day}`; }
// 0 to 23: the Eastern hour a moment falls in.
export function hourET(ms) { return Number(keyParts(ms).hour) % 24; }
// The first millisecond of an Eastern day, in UTC. New York is four or five hours behind.
function dayStart(day) {
  const [y, m, d] = day.split('-').map(Number);
  for (const h of [4, 5, 3, 6]) {
    const ms = Date.UTC(y, m - 1, d, h);
    if (dayKey(ms) === day && hourET(ms) === 0) return ms;
  }
  throw new Error(`${day} is not a day`);
}
// [start, end) of an Eastern day, in UTC milliseconds.
export function dayBounds(day) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(day)) throw new Error(`${day} is not a day: write 2026-11-13`);
  const [y, m, d] = day.split('-').map(Number);
  const next = new Date(Date.UTC(y, m - 1, d + 1)).toISOString().slice(0, 10);
  return [dayStart(day), dayStart(next)];
}
