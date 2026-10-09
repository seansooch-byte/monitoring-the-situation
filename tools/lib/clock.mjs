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
