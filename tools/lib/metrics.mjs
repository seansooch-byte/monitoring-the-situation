// Numbers derived from captures. Nothing here writes a word or invents a figure:
// every value is arithmetic on readings the grabber recorded.

const HOUR = 3600000;

// Every reading of every post, joined across captures, oldest first.
export function seriesByPost(captures) {
  const out = new Map();
  for (const c of captures) {
    for (const o of c.observations ?? []) {
      const at = Date.parse(o.at);
      if (isNaN(at)) continue;
      if (!out.has(o.id)) out.set(o.id, []);
      out.get(o.id).push({ ...o, at });
    }
  }
  for (const list of out.values()) list.sort((a, b) => a.at - b.at);
  return out;
}

// Magnitude is the base ten log of views, to one decimal. 7.0 is ten million views.
export function magnitude(views) {
  if (!Number.isFinite(views) || views <= 0) return null;
  return Math.round(Math.log10(views) * 10) / 10;
}

// Readings that carry a view count, with any that go backwards dropped (X recounts now and then).
function climbing(list) {
  const pts = [];
  let top = -1;
  for (const o of list ?? []) {
    if (!Number.isFinite(o.views) || o.views < top) continue;
    top = o.views;
    pts.push({ at: o.at, views: o.views });
  }
  return pts;
}

// Views at time t, read off the line between the two nearest readings. Null outside the readings.
function viewsAt(pts, t) {
  if (!pts.length || t < pts[0].at) return null;
  const last = pts[pts.length - 1];
  if (t >= last.at) return last.views;
  for (let i = 1; i < pts.length; i++) {
    if (t <= pts[i].at) {
      const a = pts[i - 1], b = pts[i];
      return a.views + (b.views - a.views) * ((t - a.at) / (b.at - a.at));
    }
  }
  return last.views;
}

export function trend(lastHour, hourBefore) {
  if (lastHour == null || hourBefore == null) return 'new';
  if (lastHour === 0 && hourBefore === 0) return 'still';
  if (lastHour > hourBefore * 1.25) return 'rising';
  if (lastHour < hourBefore * 0.8) return 'fading';
  return 'steady';
}

// A story's numbers: the latest reading of each of its posts, added up.
export function storyNumbers(ids, series, now) {
  let views = 0, measured = 0, unmeasured = 0, gone = 0;
  let perHour = null, prevPerHour = null;
  for (const id of ids) {
    const list = series.get(id) ?? [];
    const pts = climbing(list);
    if (list.length && list[list.length - 1].state !== 'live') gone++;
    if (!pts.length) { unmeasured++; continue; }
    measured++;
    views += pts[pts.length - 1].views;
    const v0 = viewsAt(pts, now), v1 = viewsAt(pts, now - HOUR), v2 = viewsAt(pts, now - 2 * HOUR);
    if (v0 != null && v1 != null) perHour = (perHour ?? 0) + (v0 - v1);
    if (v1 != null && v2 != null) prevPerHour = (prevPerHour ?? 0) + (v1 - v2);
  }
  return {
    views: measured ? views : null,
    magnitude: measured ? magnitude(views) : null,
    unmeasured, gone,
    perHour: perHour == null ? null : Math.round(perHour),
    prevPerHour: prevPerHour == null ? null : Math.round(prevPerHour),
    trend: trend(perHour, prevPerHour),
  };
}

// Views gained per hour in each of `bins` equal slices of [from, to], for a set of posts.
// A gain between two readings is spread evenly over the time between them; before the first
// reading it is spread from the moment the post was created.
export function deskTrace(posts, series, { from, to, bins }) {
  const out = new Array(bins).fill(0);
  const width = (to - from) / bins;
  for (const p of posts) {
    const pts = [{ at: p.created, views: 0 }, ...climbing(series.get(p.id)).filter((o) => o.at > p.created)];
    for (let i = 1; i < pts.length; i++) {
      const a = pts[i - 1], b = pts[i];
      const gain = b.views - a.views;
      if (gain <= 0 || b.at <= a.at) continue;
      const first = Math.max(0, Math.floor((a.at - from) / width));
      const last = Math.min(bins - 1, Math.floor((b.at - from) / width));
      for (let k = first; k <= last; k++) {
        const lo = Math.max(a.at, from + k * width), hi = Math.min(b.at, from + (k + 1) * width);
        if (hi > lo) out[k] += gain * ((hi - lo) / (b.at - a.at));
      }
    }
  }
  return out.map((g) => g / (width / HOUR));
}
