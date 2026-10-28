// How a capture becomes rows in the store, and how a post X no longer returns is purged from
// the record. Pure functions, used by the Worker (worker/index.mjs) and pinned by
// tests/store-rows.test.mjs.
//
// A purge keeps what X's rules allow us to keep about a deleted post, its id, its handle, its
// desk, its flags and its numbers, and empties what we may not keep: the words, the display
// name, the media descriptions, the link, the note and the lead.

export const PURGED_FIELDS = ['text', 'url', 'media', 'note', 'lead'];

export function purgedRecord(post, at) {
  const p = JSON.parse(JSON.stringify(post));
  p.text = '';
  p.url = '';
  p.media = [];
  p.note = null;
  p.lead = null;
  p.author = { ...(p.author ?? {}), name: '' };
  p.purged_at = post.purged_at ?? at;
  return p;
}

// The same capture with the named records purged. Observations are numbers and stay.
export function stripCapture(doc, ids, at) {
  return { ...doc, posts: (doc.posts ?? []).map((p) => (ids.has(p.id) ? purgedRecord(p, at) : p)) };
}

const J = (v) => JSON.stringify(v ?? null);
const int = (v) => (Number.isInteger(v) ? v : null);

export function rowsOf(doc, receivedAt, source = 'x') {
  const run = doc.run;
  const id = run.id;
  const posts = doc.posts ?? [];
  const observations = doc.observations ?? [];
  const points = new Map();
  for (const v of doc.volume ?? []) for (const pt of v.points ?? []) points.set(`${v.key}|${pt.start}`, { key: v.key, desk: v.desk ?? null, query: v.query ?? null, start: pt.start, count: int(pt.count), run_id: id });
  return {
    run: {
      id, source,
      started_at: run.started_at, finished_at: run.finished_at ?? null, status: run.status, reason: run.reason ?? null,
      agent: run.grabber?.agent ?? null, model: run.grabber?.model ?? null, method: run.grabber?.method ?? null,
      requests_rev: run.requests_rev ?? null, reads: int(run.reads), reads_left: int(run.reads_left), plan: run.plan ?? null,
      received_at: receivedAt, posts: posts.length, observations: observations.length,
    },
    posts: posts.map((p) => ({
      id: p.id, source, url: p.url, created_at: p.created_at, lang: p.lang ?? null, text: p.text ?? '',
      author_handle: p.author?.handle ?? null, author_name: p.author?.name ?? null, author_followers: int(p.author?.followers),
      author_verified: p.author?.verified ?? null, author_kind: p.author?.kind ?? null,
      media: J(p.media ?? []), reply_to: p.reply_to ?? null, quotes: p.quotes ?? null, media_source: p.media_source ?? null,
      note: J(p.note), flags: J(p.flags ?? []), desk: p.desk ?? null, beat: p.beat ?? null, topic: p.topic ?? null, lead: p.lead ?? null,
      first_run: id, last_run: id,
    })),
    post_runs: posts.map((p) => ({ post_id: p.id, run_id: id })),
    observations: observations.map((o) => ({
      post_id: o.id, at: o.at, run_id: id, state: o.state,
      views: int(o.views), likes: int(o.likes), reposts: int(o.reposts), quotes: int(o.quotes), replies: int(o.replies), bookmarks: int(o.bookmarks),
      approx: o.approx ? 1 : 0,
    })),
    sweeps: (doc.sweeps ?? []).map((s) => ({ run_id: id, sweep_id: s.id, kind: s.kind, desk: s.desk ?? null, method: s.method ?? null, window_hours: int(s.window_hours), status: s.status, reason: s.reason ?? null, post_ids: J(s.post_ids ?? []) })),
    volume_points: [...points.values()],
    trends: (doc.trends ?? []).map((t) => ({ run_id: id, region: t.region, rank: int(t.rank), name: t.name, post_count: int(t.post_count), story: J(t.story), post_ids: J(t.post_ids ?? []) })),
    context: (doc.context ?? []).map((c) => ({ run_id: id, post_id: c.post_id, replies: J(c.replies ?? []), quotes: J(c.quotes ?? []) })),
    answers: (doc.answers ?? []).map((a) => ({ run_id: id, request_id: a.request_id, status: a.status, post_ids: J(a.post_ids ?? []), note: a.note ?? null })),
  };
}

// A post row back into the capture's record shape, for readers that consume capture documents.
export function recordOf(row) {
  const parse = (s, fallback) => { try { return s == null ? fallback : JSON.parse(s); } catch { return fallback; } };
  const r = {
    id: row.id, url: row.url, created_at: row.created_at, lang: row.lang, text: row.text,
    author: { handle: row.author_handle, name: row.author_name, followers: row.author_followers, verified: row.author_verified, kind: row.author_kind },
    media: parse(row.media, []), reply_to: row.reply_to, quotes: row.quotes, note: parse(row.note, null),
    flags: parse(row.flags, []), desk: row.desk, beat: row.beat, topic: row.topic, lead: row.lead,
    first_run: row.first_run, last_run: row.last_run,
  };
  if (row.media_source != null) r.media_source = row.media_source;
  if (row.purged_at) r.purged_at = row.purged_at;
  return r;
}
