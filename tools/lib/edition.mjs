// The paper's edition: one Eastern day of the record, ranked by the numbers (contract/PAPER.md).
// Pure: it reads only what it is handed and returns plain data, so the same record always gives the
// same edition, byte for byte. tools/edition.mjs gathers the record from the repo and calls this.
//
// Expected behaviour (tests/edition.test.mjs holds it to this):
//   - A post counts only if the ledger has it as ok, it carries no never-shown flag, and its desk
//     (the editor's where the pulse described it, else the grabber's, else that of a story citing it)
//     is a desk in desks.json.
//   - A post's views on the day are what it gained between the day's start and end; readings after
//     the end are ignored, and a post whose last reading is unavailable gained nothing and is dropped.
//   - Stories begun by the day's end with views on the day, or begun that day, ranked by reach (the sum of their posts'
//     views on the day). The first leads; the first five are the briefing.
//   - Posts the editor described that no story cites are split into unreported (news sections) and
//     watched (the rest), largest first, one per account.
//   - No text from a post is ever copied into an edition.
//   - The day's letter (the Newsletter, contract/NEWSLETTER.md) must pass checkLetter against this edition, or
//     the edition is refused with every reason. It rides in the edition whole; the Paper prints its read.
import { dayBounds, dayKey, hourET } from './clock.mjs';
import { checkLetter } from './letter.mjs';

export const EDITION_SCHEMA = 'mts.edition/2';
const DAYNAME = new Intl.DateTimeFormat('en-GB', { timeZone: 'UTC', weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });

export function buildEdition({ day, desks, paper, posts, observations, ledger, moments, lines = {}, letter = null }) {
  const [start, end] = dayBounds(day);
  const groupOf = Object.fromEntries(desks.desks.map((d) => [d.id, d.group]));
  const never = new Set(paper.never_shown);
  const byId = new Map(posts.map((p) => [p.id, p]));

  // Readings per post, in time order, up to the day's end.
  const readings = new Map();
  for (const o of observations) {
    const t = Date.parse(o.at);
    if (!(t < end) || !byId.has(o.id)) continue;
    if (!readings.has(o.id)) readings.set(o.id, []);
    readings.get(o.id).push({ t, views: o.views, state: o.state });
  }
  for (const list of readings.values()) list.sort((a, b) => a.t - b.t);

  // A post's desk: the editor's, else the grabber's, else the first desk of a story that cites it.
  const storyDesk = new Map();
  for (const m of moments) for (const p of m.posts ?? []) if (!storyDesk.has(p.id) && m.desks?.length) storyDesk.set(p.id, m.desks[0]);
  const deskOf = (id) => lines[id]?.desk || byId.get(id)?.desk || storyDesk.get(id);
  function counts(id) {
    const p = byId.get(id);
    if (!p || ledger[id]?.result !== 'ok') return false;
    if ((p.flags ?? []).some((f) => never.has(f))) return false;
    return Boolean(groupOf[deskOf(id)]);
  }
  // Views gained on the day, or null when the post did not count or had vanished by the day's end.
  const gained = new Map();
  function viewsOnDay(id) {
    if (gained.has(id)) return gained.get(id);
    let out = null;
    const list = readings.get(id) ?? [];
    const last = list.at(-1);
    if (counts(id) && last && last.state === 'live' && typeof last.views === 'number') {
      const created = Date.parse(byId.get(id).created_at);
      let base = 0;
      if (created < start) {
        const before = list.filter((r) => r.t <= start && r.state === 'live').at(-1);
        const first = list.find((r) => r.t >= start && r.state === 'live');
        base = before ? before.views : first ? first.views : last.views;
      }
      out = Math.max(0, last.views - base);
    }
    gained.set(id, out);
    return out;
  }

  // Stories: ranked by reach on the day.
  const cited = new Set(moments.flatMap((m) => (m.posts ?? []).map((p) => p.id)));
  const stories = [];
  for (const m of moments) {
    const began = Date.parse(m.started_at);
    const ps = (m.posts ?? []).map((p) => ({ id: p.id, role: p.role, views: viewsOnDay(p.id) }))
      .filter((p) => p.views !== null)
      .map((p) => ({ ...p, handle: byId.get(p.id).author?.handle ?? null }))
      .sort((a, b) => b.views - a.views || a.id.localeCompare(b.id));
    const reach = ps.reduce((n, p) => n + p.views, 0);
    // A story is in the editions from the day it began: a front page never carries a headline from a later day,
    // whatever the story's earlier posts gained.
    if (!(began < end) || !(reach > 0 || began >= start)) continue;
    const sections = [...new Set((m.desks ?? []).map((d) => groupOf[d]).filter(Boolean))];
    stories.push({ id: m.id, title: m.title, dek: m.dek, standing: m.standing, desks: m.desks ?? [], sections, started_at: m.started_at, reach, posts: ps });
  }
  stories.sort((a, b) => b.reach - a.reach || a.started_at.localeCompare(b.started_at) || a.id.localeCompare(b.id));
  stories.forEach((s, i) => { s.rank = i + 1; });

  // Described, uncited posts: one place per account, largest first.
  const described = [];
  const held = new Set();
  const candidates = Object.keys(lines).filter((id) => !cited.has(id))
    .map((id) => ({ id, views: viewsOnDay(id) })).filter((p) => p.views)
    .sort((a, b) => b.views - a.views || a.id.localeCompare(b.id));
  for (const { id, views } of candidates) {
    const handle = byId.get(id).author?.handle ?? null;
    if (handle && held.has(handle)) continue;
    if (handle) held.add(handle);
    const desk = deskOf(id);
    described.push({ id, handle, desk, section: groupOf[desk], views, line: lines[id].line });
  }
  const news = new Set(paper.news_sections);
  const unreported = described.filter((p) => news.has(p.section)).slice(0, paper.unreported);
  const watched = described.filter((p) => !news.has(p.section)).slice(0, paper.watched);

  // The day's posts, the sections and the counts.
  const dayPosts = posts.filter((p) => { const t = Date.parse(p.created_at); return t >= start && t < end && viewsOnDay(p.id) !== null; });
  const all = posts.filter((p) => viewsOnDay(p.id) !== null);
  const total = all.reduce((n, p) => n + viewsOnDay(p.id), 0);
  const sections = desks.groups.map((g) => {
    const mine = (p) => groupOf[deskOf(p.id)] === g.id;
    const hours = Array(24).fill(0);
    for (const p of dayPosts.filter(mine)) hours[hourET(Date.parse(p.created_at))] += 1;
    const views = all.filter(mine).reduce((n, p) => n + viewsOnDay(p.id), 0);
    return {
      id: g.id, name: g.name, posts: dayPosts.filter(mine).length, views, share: total ? views / total : 0, hours,
      stories: stories.filter((s) => s.sections.includes(g.id)).map((s) => s.id),
      items: described.filter((p) => p.section === g.id).slice(0, paper.section_items),
    };
  });

  // The letter, if there is one, must stand on this edition: it may cite only what the edition holds.
  if (letter) {
    // A story must be in this edition; a post must be one X confirmed that the record may show (it counts), which
    // takes in a post the editor described the morning after, as a letter written then will cite.
    const inEdition = new Set(stories.map((s) => s.id));
    const known = { story: (id) => inEdition.has(id), post: (id) => counts(id) };
    const bad = checkLetter(letter, day, new Set(desks.desks.map((d) => d.id)), known);
    if (bad.length) throw new Error(`newsletter/${day}.json does not meet contract/NEWSLETTER.md: ${bad.join('; ')}`);
  }

  return {
    schema: EDITION_SCHEMA,
    edition: { kind: 'day', day, label: DAYNAME.format(new Date(`${day}T12:00:00Z`)), from: new Date(start).toISOString(), to: new Date(end).toISOString() },
    counts: { posts: dayPosts.length, accounts: new Set(dayPosts.map((p) => p.author?.handle)).size, desks: desks.desks.length, stories: stories.length, views: total },
    lead: stories[0]?.id ?? null,
    briefing: stories.slice(0, paper.briefing).map((s) => s.id),
    stories,
    unreported,
    watched,
    sections,
    letter: letter ?? null,
  };
}

export { dayKey };
