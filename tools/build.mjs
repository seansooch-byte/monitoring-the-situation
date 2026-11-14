#!/usr/bin/env node
// Builds the site into dist/.
//
//   node tools/build.mjs            from this repository's capture/ and moments/
//   node tools/build.mjs --demo     from fixtures/demo (invented data, marked on every page)
//
// Words come from moments/ (the editor) and newsletter/ (Soochiebot). Numbers come from capture/ (the
// grabber). The build only joins them: it never writes a sentence about a story and never makes up a
// figure. The front page is an edition (contract/PAPER.md): one Eastern day, ranked by the record.
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { deskTrace, magnitude, placesPerAccount, seriesByPost, storyNumbers } from './lib/metrics.mjs';
import { ZONE_LABEL, clockTime, dateOf, dayOf, dayBounds, dayKey } from './lib/clock.mjs';
import { buildEdition } from './lib/edition.mjs';
import { linesBetween, pulseHistory } from './lib/pulse-history.mjs';
import { walk } from './lib/files.mjs';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const DEMO = process.argv.includes('--demo');
const DATA = DEMO ? join(REPO, 'fixtures', 'demo') : REPO;
const OUT = join(REPO, 'dist');
const HOUR = 3600000;
const BINS = 24; // one for each of the last 24 hours
// One account holds at most this many places on the pulse, however many of its posts are large.
const PULSE_PER_ACCOUNT = 1;

const readJSON = (p) => JSON.parse(readFileSync(p, 'utf8'));
// The site draws the desks watched now. A retired desk has no card, no page and no total.
const DESKS = readJSON(join(REPO, 'contract', 'desks.json'));
const deskById = new Map(DESKS.desks.map((d) => [d.id, d]));
// A count in a sentence is written as a word, and is read from the data, never typed.
const WORDS = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'];
const inWords = (n) => WORDS[n] ?? String(n);
const DESK_COUNT = inWords(DESKS.desks.length);
// site.json holds the site's own words. Where they give the number of desks they say {desks}.
const SITE = JSON.parse(readFileSync(join(REPO, 'site.json'), 'utf8').replaceAll('{desks}', DESK_COUNT));

// ---------- load

const captures = walk(join(DATA, 'capture'), (n) => /^\d{4}Z\.json$/.test(n)).map(readJSON);
const moments = walk(join(DATA, 'moments'), (n) => n.endsWith('.json')).map(readJSON);
const records = new Map();
for (const c of captures) for (const p of c.posts ?? []) records.set(p.id, p);
const series = seriesByPost(captures);
const NOW = captures.length ? Math.max(...captures.map((c) => Date.parse(c.run.finished_at))) : Date.now();
const FROM = NOW - 24 * HOUR;

// Gate 2's ledger: what X answered about each captured post. MTS_LEDGER points the build at another
// copy of it (a test, a dry run); given with --demo it makes the demo build check its posts too.
const LEDGER_FILE = process.env.MTS_LEDGER || join(REPO, 'verified', 'posts.json');
const CHECKED = !DEMO || Boolean(process.env.MTS_LEDGER);
if (process.env.MTS_LEDGER && !existsSync(LEDGER_FILE)) throw new Error(`MTS_LEDGER names ${LEDGER_FILE}, which does not exist`);
const LEDGER = CHECKED && existsSync(LEDGER_FILE) ? readJSON(LEDGER_FILE) : {};

// What X said about a post decides what the build does with it. ok: it is shown. mismatch: X shows
// other words or another author than the record, so the record is wrong and the build stops.
// withheld, missing, or not yet asked: it is not shown and counts for nothing, the build says so
// in its log, and the rest of the site is built.
function withX(id) {
  if (!CHECKED) return 'ok';
  const r = LEDGER[id]?.result;
  return ['ok', 'mismatch', 'withheld', 'missing'].includes(r) ? r : 'unverified';
}
const WHY_UNSHOWN = { withheld: 'withheld by X (no embed without a login)', missing: 'missing on X (no post with this id)', unverified: 'not confirmed by X yet' };
let unshown = 0;
const warn = (s) => { unshown++; console.warn(`warning: ${s}`); };

// ---------- small helpers

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
// X sends a few entities already encoded; decode those, then escape everything for the page.
const fromX = (s) => String(s ?? '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
function postText(p) {
  let t = fromX(p.text);
  // X appends a t.co link for attached media and for a quoted post; they are not part of the words.
  if ((p.media ?? []).length || p.quotes) t = t.replace(/(\s*https:\/\/t\.co\/\w+)+\s*$/, '');
  return esc(t).replace(/\n/g, '<br>');
}
function num(n) {
  if (n == null) return 'n/a';
  if (n >= 1e9) return (n / 1e9).toFixed(1).replace(/\.0$/, '') + 'B';
  if (n >= 1e6) return (n / 1e6).toFixed(1).replace(/\.0$/, '') + 'M';
  if (n >= 1e4) return Math.round(n / 1e3) + 'K';
  if (n >= 1e3) return (n / 1e3).toFixed(1).replace(/\.0$/, '') + 'K';
  return String(n);
}
const mag = (m) => (m == null ? 'n/a' : m.toFixed(1));
// Times on the page are Eastern time (tools/lib/clock.mjs). Stored timestamps stay in UTC.
const hhmm = clockTime;
const day = dayOf;
function ago(ms) {
  const m = Math.max(0, Math.round((NOW - ms) / 60000));
  if (m < 60) return `${m} min ago`;
  const h = Math.round(m / 60);
  if (h < 48) return `${h} h ago`;
  return `${Math.round(h / 24)} days ago`;
}
const STANDING = { established: 'Established', developing: 'Developing', disputed: 'Disputed', false: 'False', satire: 'Satire' };
const ROLE = { origin: 'Origin', voice: 'Voice', reply: 'Reply', quote: 'Quote post', official: 'Official', correction: 'Correction' };
const TREND = { rising: 'rising', fading: 'fading', steady: 'steady', new: 'new', still: 'still' };

// ---------- stories: the editor's words joined to the grabber's numbers

// A post X does not confirm comes back as { id, role, unavailable } and carries nothing from the
// record: no words, no author, no numbers.
function resolvePost(ref, who = 'story') {
  const rec = records.get(ref.id);
  if (!rec) throw new Error(`${who} cites post ${ref.id}, which no capture has recorded`);
  const x = withX(ref.id);
  if (x === 'mismatch') throw new Error(`${who} cites post ${ref.id}, which X shows differently from the record (${LEDGER[ref.id].detail ?? 'mismatch'}); change it, do not work around it`);
  if (x !== 'ok') return { id: ref.id, role: ref.role, unavailable: x };
  const list = series.get(ref.id) ?? [];
  const live = [...list].reverse().find((o) => Number.isFinite(o.views)) ?? list[list.length - 1] ?? null;
  return { ...rec, role: ref.role, now: live, readings: list, created: Date.parse(rec.created_at) };
}

const stories = moments.map((m) => {
  // `cited` is every post the story names, in its order; `posts` only those X confirms, which are
  // the ones shown in full and counted.
  const cited = m.posts.map((ref) => resolvePost(ref, `story ${m.id}`));
  for (const p of cited) if (p.unavailable) warn(`story ${m.id} cites post ${p.id}, ${WHY_UNSHOWN[p.unavailable]}: shown as unavailable, counted for nothing`);
  const posts = cited.filter((p) => !p.unavailable);
  const n = storyNumbers(posts.map((p) => p.id), series, NOW);
  const byId = new Map(cited.map((p) => [p.id, p]));
  return {
    ...m, posts, cited, n,
    started: Date.parse(m.started_at),
    origin: posts.find((p) => p.role === 'origin') ?? posts[0] ?? null,
    worlds: (m.worlds ?? []).map((w) => ({ ...w, post: byId.get(w.post) ?? null })),
    home: deskById.get(m.desks[0]),
  };
}).sort((a, b) => (b.n.magnitude ?? 0) - (a.n.magnitude ?? 0) || b.started - a.started);

// The bulletin holds what began in the last 48 hours. An older story keeps its page and moves to the archive.
const LIVE_FOR = 48 * HOUR;
const live = stories.filter((s) => s.started >= NOW - LIVE_FOR);
const past = stories.filter((s) => s.started < NOW - LIVE_FOR).sort((a, b) => b.started - a.started);

// ---------- the pulse: single posts the editor has passed, each with the editor's line

const NEVER_SHOWN = ['private_individual', 'minor', 'nsfw', 'graphic'];
const pulseFile = join(DATA, 'pulse', 'current.json');
const PULSE = existsSync(pulseFile) ? readJSON(pulseFile) : { items: [] };
const storyOf = new Map();
for (const s of stories) for (const p of s.posts) if (!storyOf.has(p.id)) storyOf.set(p.id, s);

// A post on the pulse: an item, or a related post of the item `parent`.
function pulsePost(id, parent = null) {
  const what = parent ? `related post ${id} of pulse item ${parent}` : `pulse item ${id}`;
  const rec = records.get(id);
  if (!rec) throw new Error(`${what} is not in any capture`);
  const bad = (rec.flags ?? []).filter((f) => NEVER_SHOWN.includes(f));
  // A hard stop in code: whatever the editor wrote, a flagged post is never rendered.
  if (bad.length) throw new Error(`${what} is flagged ${bad.join(', ')} by the grabber and cannot be shown`);
  // A mismatch stops the build in resolvePost; a post X does not confirm is left out (null).
  const post = resolvePost({ id, role: null }, parent ? `pulse item ${parent}` : 'the pulse');
  if (!post.unavailable) return post;
  warn(`${what} is ${WHY_UNSHOWN[post.unavailable]}: left off the pulse`);
  return null;
}

const passed = (PULSE.items ?? []).map((it) => {
  const post = pulsePost(it.id);
  // The related posts are checked even when the item is left out, so a flag or a mismatch still stops the build.
  const also = (it.also ?? []).map((id) => pulsePost(id, it.id)).filter(Boolean);
  if (!post) return null;
  const n = storyNumbers([it.id], series, NOW);
  const ageH = Math.max((NOW - post.created) / HOUR, 0.05);
  return {
    ...it, post, n, ageH,
    pace: n.perHour ?? (n.views != null ? Math.round(n.views / ageH) : null), measured: n.perHour != null,
    also,
    story: storyOf.get(it.id) ?? null,
    deskInfo: deskById.get(it.desk) ?? deskById.get(post.desk),
  };
}).filter((it) => it && it.n.views != null).sort((a, b) => b.n.views - a.n.views);

// The pulse is every corner of the internet, so no one account may fill it. Of the posts the
// editor passed, an account keeps its largest; the build says which others it held back.
// The rule is applied to each list a reader is shown: the front page here, and each desk's
// own list below, so a post held off the front still stands on its desk.
const onePlace = (list) => placesPerAccount(list, PULSE_PER_ACCOUNT, (it) => it.post.author.handle);
const { kept: pulse, held } = onePlace(passed);

// ---------- the desks: 24 hourly figures per desk, from every post the grabber labelled with that desk

// Bar height is views gained per hour on a log scale: 1,000 an hour is the floor, 10 million is full.
const level = (perHour) => Math.max(0, Math.min(1, (Math.log10(Math.max(perHour, 1)) - 3) / 4));

// Only posts X has confirmed feed a trace or a total. A post Gate 2 could not confirm counts for nothing.
const confirmed = (id) => withX(id) === 'ok';

const desks = DESKS.desks.map((d) => {
  const own = [...records.values()].filter((p) => p.desk === d.id && confirmed(p.id)).map((p) => ({ id: p.id, created: Date.parse(p.created_at) }));
  const bins = deskTrace(own, series, { from: FROM, to: NOW, bins: BINS });
  const mine = live.filter((s) => s.home?.id === d.id);
  // The desk's figure for the day counts posts written in the last 24 hours. An old post that a
  // reference led back to still feeds the trace by what it gained, but not the day's total.
  const fresh = own.filter((p) => p.created >= FROM);
  const total = fresh.reduce((sum, p) => { const l = (series.get(p.id) ?? []).filter((o) => Number.isFinite(o.views)).pop(); return sum + (l ? l.views : 0); }, 0);
  return { ...d, pulse: onePlace(passed.filter((it) => it.deskInfo?.id === d.id)).kept, bins, posts: fresh.length, views: total, mag: magnitude(total), stories: mine, also: live.filter((s) => s.home?.id !== d.id && s.desks.includes(d.id)), past: past.filter((s) => s.desks.includes(d.id)) };
});


// ---------- the paper: an edition for each Eastern day (contract/PAPER.md)
//
// Edition 3, "The Broadsheet". The front page is the latest complete day, ranked by the views its
// stories' posts gained that day; every day keeps its own front page under /edition/. The pulse is
// still the record's live instrument, and it is now Internet Pulse, at /pulse/, the middle of the switch under the nameplate.

const PAPER = readJSON(join(REPO, 'contract', 'paper.json'));
// A post is captured again and again; a later capture may carry it with no desk (as a reference), so
// a field is filled once and a blank never overwrites it.
const merged = new Map();
const observations = [];
for (const c of captures) {
  for (const p of c.posts ?? []) {
    const had = merged.get(p.id);
    if (!had) { merged.set(p.id, { ...p }); continue; }
    for (const [k, v] of Object.entries(p)) if (had[k] == null || (Array.isArray(had[k]) && !had[k].length && Array.isArray(v) && v.length)) had[k] = v;
  }
  for (const o of c.observations ?? []) observations.push(o);
}
const allPosts = [...merged.values()];
// The demo checks nothing against X unless it is given a ledger, so there every post counts.
const EDITION_LEDGER = CHECKED ? LEDGER : Object.fromEntries(allPosts.map((p) => [p.id, { result: 'ok' }]));
const HISTORY = DEMO ? [] : pulseHistory(REPO);
const linesFor = (start, end) => (DEMO
  ? Object.fromEntries((PULSE.items ?? []).map((it) => [it.id, { desk: it.desk, line: it.line }]))
  : linesBetween(HISTORY, start, end));
const nextDay = (d) => { const [y, m, dd] = d.split('-').map(Number); return new Date(Date.UTC(y, m - 1, dd + 1)).toISOString().slice(0, 10); };
const TODAY = dayKey(NOW);
const FIRST_DAY = captures.length ? dayKey(Math.min(...captures.map((c) => Date.parse(c.run.finished_at)))) : TODAY;

const editions = [];
for (let d = FIRST_DAY; d <= TODAY; d = nextDay(d)) {
  const [s, e] = dayBounds(d);
  const letterFile = join(DATA, 'newsletter', `${d}.json`);
  const ed = buildEdition({ day: d, desks: DESKS, paper: PAPER, posts: allPosts, observations, ledger: EDITION_LEDGER, moments, lines: linesFor(s, e), letter: existsSync(letterFile) ? readJSON(letterFile) : null });
  if (!ed.stories.length && !ed.counts.posts) continue;
  ed.partial = d === TODAY;
  editions.push(ed);
}
const complete = editions.filter((e) => !e.partial);
const todayEd = editions.find((e) => e.partial) ?? null;
// The front page is the latest complete day with a story. On the record's first day, or after a day
// with none, it is today so far.
const frontEd = [...complete].reverse().find((e) => e.stories.length) ?? todayEd ?? complete.at(-1) ?? null;
const storyById = new Map(stories.map((s) => [s.id, s]));
const inEditions = new Map();
for (const e of editions) for (const s of e.stories) {
  if (!inEditions.has(s.id)) inEditions.set(s.id, []);
  inEditions.get(s.id).push({ day: e.edition.day, label: e.edition.label, rank: s.rank, reach: s.reach, partial: e.partial });
}

// ---------- words and small parts

const groupById = new Map(DESKS.groups.map((g) => [g.id, g]));
const sectionName = (id) => groupById.get(id)?.name ?? id;
const deskName = (id) => deskById.get(id)?.name ?? id;
const groupName = (d) => sectionName(d.group);
const LONG = new Intl.DateTimeFormat('en-GB', { timeZone: 'UTC', weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
const SHORT = new Intl.DateTimeFormat('en-GB', { timeZone: 'UTC', weekday: 'short', day: 'numeric', month: 'short' });
const longDay = (d) => LONG.format(new Date(`${d}T12:00:00Z`)).replace(',', '');
const shortDay = (d) => SHORT.format(new Date(`${d}T12:00:00Z`)).replace(',', '');
const ordinal = (n) => (n === 1 ? 'Lead' : `${n}${n % 10 === 2 && n % 100 !== 12 ? 'nd' : n % 10 === 3 && n % 100 !== 13 ? 'rd' : 'th'}`);
// A link to a post on X, made from its id (digits only) and, where it is a plain account name, its handle.
// Nothing recorded about the post becomes part of the address.
const xUrl = (id) => {
  if (!/^\d{1,25}$/.test(String(id))) return 'https://x.com/';
  const h = merged.get(id)?.author?.handle;
  return /^[A-Za-z0-9_]{1,15}$/.test(h ?? '') ? `https://x.com/${h}/status/${id}` : `https://x.com/i/status/${id}`;
};
const deskLink = (d) => (d ? `<a class="desk" href="/desk/${d.id}/">${esc(d.name)}</a>` : '');
const xLink = (p, text, cls) => `<a${cls ? ` class="${cls}"` : ''} href="${esc(p.url)}" rel="noopener noreferrer" target="_blank">${text}</a>`;
const clock = (p) => `<time datetime="${esc(p.created_at)}">${hhmm(p.created)} ${ZONE_LABEL}</time>`;
const who = (p) => `<b>${esc(fromX(p.author.name))}</b>`;
const quoted = (p) => `“${postText(p)}”`;
const numeral = (m, cls = 'num') => `<span class="${cls}"><span class="vh">Magnitude </span>${mag(m)}</span>`;
const standingTag = (s) => `<span class="stand stand-${esc(s.standing)}">${STANDING[s.standing] ?? esc(s.standing)}</span>`;
const OUTSIDE = 'Outside your worlds';
const ageOf = (h) => (h < 1 ? `${Math.round(h * 60)} min` : h < 48 ? `${Math.round(h)} h` : `${Math.round(h / 24)} days`);
const counts = (o, keys) => (o ? keys.filter((k) => o[k] != null).map((k) => `<span>${num(o[k])} ${k}</span>`).join('') : '');
const kicker = (s) => [STANDING[s.standing] ?? s.standing, ...s.desks.map(deskName)].filter(Boolean).map(esc).join(' · ');
const plural = (n, one, many) => `${n.toLocaleString('en-US')} ${n === 1 ? one : many}`;

function mediaLine(p) {
  const m = (p.media ?? [])[0];
  if (!m) return '';
  const kind = { photo: 'Photo', video: 'Video', gif: 'GIF', link: 'Link', poll: 'Poll' }[m.type] ?? 'Media';
  const len = m.duration_s ? `, ${Math.floor(m.duration_s / 60)}:${String(Math.round(m.duration_s % 60)).padStart(2, '0')}` : '';
  const what = m.description ? esc(m.description) : m.link_title ? esc(m.link_title) : '';
  return `<p class="post-media"><span>${kind}${len}</span>${what}</p>`;
}

// A post on a story page: the words first, then who said them and what they have reached.
function postFigure(p, { compact = false } = {}) {
  return `<figure class="post${compact ? ' post-compact' : ''}">
  <blockquote class="post-q">${quoted(p)}</blockquote>
  ${mediaLine(p)}
  <figcaption class="by">${p.role && !compact ? `<span class="role">${ROLE[p.role] ?? esc(p.role)}</span>` : ''}${who(p)}<span>@${esc(p.author.handle)} · ${clock(p)}</span>${counts(p.now, ['views', 'likes', 'reposts', 'replies'])}${xLink(p, 'Open on X', 'open')}</figcaption>
</figure>`;
}

// A cited post X does not confirm, in its place: the note and the id, and nothing from the record.
// A post X has no answer for gets no link, since there is nothing at the other end.
const UNAVAILABLE = {
  withheld: 'X will not show this post without a login, so it is not shown here and its numbers are not counted.',
  missing: 'X has no post with this id now, so it is not shown here and its numbers are not counted.',
  unverified: 'This post has not been confirmed with X yet, so it is not shown here and its numbers are not counted.',
};
function unavailableFigure(p, { compact = false } = {}) {
  const link = p.unavailable === 'missing' ? `<span>Post ${esc(p.id)}</span>` : `<a class="open" href="https://x.com/i/status/${esc(p.id)}" rel="noopener noreferrer" target="_blank">Post ${esc(p.id)} on X</a>`;
  return `<figure class="post post-gone${compact ? ' post-compact' : ''}" data-unavailable="${esc(p.unavailable)}">
  <p class="post-note"><span class="lab">Unavailable on X</span> ${UNAVAILABLE[p.unavailable]}</p>
  <figcaption class="by">${p.role && !compact ? `<span class="role">${ROLE[p.role] ?? esc(p.role)}</span>` : ''}${link}</figcaption>
</figure>`;
}
const citedFigure = (p, opts) => (p.unavailable ? unavailableFigure(p, opts) : postFigure(p, opts));

// How a related post stands to the one it is shown under, read from the grabber's own links.
function relation(main, p) {
  if (p.reply_to && p.reply_to === main.id) return 'A reply';
  if (main.quotes && main.quotes === p.id) return 'The post it quotes';
  if (p.quotes && p.quotes === main.id) return 'A quote post';
  if (main.reply_to && main.reply_to === p.id) return 'The post it answers';
  return 'Related';
}
function relatedPost(main, p) {
  const views = p.now?.views;
  return `<figure class="rel-it">
  <figcaption class="lab">${relation(main, p)}</figcaption>
  <blockquote class="rel-q">${quoted(p)}</blockquote>
  <p class="rel-by">${who(p)} ${xLink(p, `@${esc(p.author.handle)}`)} · ${clock(p)}${views != null ? ` · ${num(views)} views` : ''}</p>
</figure>`;
}
const storyLink = (it) => (it.story ? `<a class="story-link" href="/story/${esc(it.story.id)}/">The researched story</a>` : '');

// ---------- Internet Pulse (/pulse/): the largest posts right now

function leadBlock(it) {
  const d = it.deskInfo, p = it.post;
  const facts = [['Views', num(it.n.views)]];
  if (it.pace != null) facts.push([it.measured ? 'Views an hour' : 'Views an hour, average', num(it.pace)]);
  facts.push(['Age', ageOf(it.ageH)]);
  return `<section class="lead" id="p-${esc(it.id)}" aria-label="The largest post right now" data-views="${it.n.views}" data-desks="${esc(d?.id ?? '')}">
  <div class="lead-fig">
    <p class="lead-top"><span class="lab">The largest post right now</span>${deskLink(d)}<span class="out">${OUTSIDE}</span></p>
    <p>${numeral(it.n.magnitude, 'big')}</p>
    <p class="lab lab-quiet">Magnitude: the base ten log of views</p>
    <dl class="facts">${facts.map(([k, v]) => `<div><dt class="lab">${k}</dt><dd>${v}</dd></div>`).join('')}</dl>
  </div>
  <div>
    <p class="lead-line">${esc(it.line)}</p>
    <blockquote class="lead-q">${quoted(p)}</blockquote>
    <p class="by">${who(p)}<span>@${esc(p.author.handle)} · ${clock(p)}</span>${counts(p.now, ['likes', 'reposts', 'replies'])}${storyLink(it)}${xLink(p, 'Open on X', 'open')}</p>
    ${it.also.length ? `<div class="rel">${it.also.map((x) => relatedPost(p, x)).join('')}</div>` : ''}
  </div>
</section>`;
}

function pulseItem(it) {
  const d = it.deskInfo, p = it.post;
  const pace = it.pace == null ? '' : ` · ${it.measured ? 'gaining' : 'averaging'} ${num(it.pace)} an hour`;
  const more = it.also.length ? `<details class="more"><summary>+${it.also.length} related ${it.also.length === 1 ? 'post' : 'posts'}</summary><div class="more-list">${it.also.map((x) => relatedPost(p, x)).join('')}</div></details>` : '';
  return `<li class="it" id="p-${esc(it.id)}" data-views="${it.n.views}" data-pace="${Math.round(it.pace ?? 0)}" data-start="${p.created}" data-desks="${esc(d?.id ?? '')}">
  <div class="hd">
    ${numeral(it.n.magnitude)}
    <div class="hd-side"><p class="hd-row">${deskLink(d)}<span class="out">${OUTSIDE}</span></p><p class="meta">${num(it.n.views)} views${pace} · ${ageOf(it.ageH)} old</p></div>
  </div>
  <p class="line">${esc(it.line)}</p>
  <blockquote class="q">${quoted(p)}</blockquote>
  <div class="by">${xLink(p, `${who(p)} <span>@${esc(p.author.handle)} · ${clock(p)}</span>`)}${more}${storyLink(it)}${xLink(p, 'Open on X', 'open')}</div>
</li>`;
}
const pulseList = (list, id) => `<ol class="pg"${id ? ` id="${id}"` : ''}>${list.map(pulseItem).join('')}</ol>`;

// A desk's last 24 hours as 24 bars. Height is the views gained in that hour on a log scale:
// 1,000 an hour is the floor and 10 million is full height. An hour with nothing is a faint tick.
function bars(d, max = 40) {
  return d.bins.map((v, i) => {
    const when = i === BINS - 1 ? 'the last hour' : `${BINS - i} h ago`;
    return `<i style="height:${v > 0 ? Math.round(3 + (max - 3) * level(v)) : 1}px"${v > 0 ? '' : ' class="off"'} title="${esc(d.name)}, ${when}: ${num(Math.round(v))} views an hour"></i>`;
  }).join('');
}
// On the wire a card is a switch (this is one of my worlds); everywhere else it is a link.
function deskCard(d, { link = false } = {}) {
  const quiet = d.posts === 0;
  const inner = `<span class="dk-top"><span class="dk-name">${esc(d.name)}</span><span class="dk-mag${quiet ? ' is-quiet' : ''}">${quiet ? 'quiet' : mag(d.mag)}</span></span>
  <span class="dk-bars" aria-hidden="true">${bars(d)}</span>
  <span class="dk-meta"><span>${d.code} · ${esc(groupName(d))}</span><span>${quiet ? 'no posts' : `${num(d.views)} views`}</span></span>`;
  if (!link) return `<button type="button" class="dk" data-desk="${d.id}" aria-pressed="false">${inner}</button>`;
  const top = d.pulse[0]?.line ?? d.stories[0]?.title ?? d.scope.split(':')[0];
  return `<a class="dk" id="desk-${d.id}" href="/desk/${d.id}/">${inner}<span class="dk-line">${esc(top)}</span></a>`;
}

function spark(s, w = 200, h = 44) {
  if (!s.posts.length) return `<p class="spark-wait">No reading yet.</p>`;
  const pts = [];
  for (const p of s.posts) for (const o of p.readings) if (Number.isFinite(o.views)) pts.push(o.at);
  const born = Math.min(...s.posts.map((p) => p.created));
  const times = [...new Set([born, ...pts])].sort((a, b) => a - b);
  if (times.length < 2) return `<p class="spark-wait">No reading yet.</p>`;
  const total = (t) => s.posts.reduce((sum, p) => { const r = p.readings.filter((o) => o.at <= t && Number.isFinite(o.views)).pop(); return sum + (r ? r.views : 0); }, 0);
  const ys = times.map(total), max = Math.max(...ys, 1), t0 = times[0], span = times[times.length - 1] - t0 || 1;
  const d = times.map((t, i) => `${i ? 'L' : 'M'}${(((t - t0) / span) * w).toFixed(1)} ${(h - 2 - (ys[i] / max) * (h - 6)).toFixed(1)}`).join('');
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" role="img" aria-label="Views over time, from ${num(ys[0])} to ${num(ys[ys.length - 1])}"><path d="${d}"/></svg>`;
}

function worldsBlock(s, open) {
  if (!s.worlds.length) return '';
  const count = ['', 'one world', 'two worlds', 'three worlds', 'four worlds'][s.worlds.length] ?? `${s.worlds.length} worlds`;
  return `<details class="worlds"${open ? ' open' : ''}>
  <summary>Seen from ${count}</summary>
  <div class="worlds-grid">${s.worlds.map((w) => `<div class="world"><h4>${esc(w.name)}</h4><p>${esc(w.sees)}</p>${w.post ? citedFigure(w.post, { compact: true }) : ''}</div>`).join('')}</div>
  ${s.common ? `<div class="common"><h4>On the record</h4><p>${esc(s.common)}</p></div>` : ''}
</details>`;
}

function storyMeta(s) {
  return `<p class="hd-row">${s.desks.map((id) => deskLink(deskById.get(id))).join('')}<span class="meta">began ${hhmm(s.started)} ${ZONE_LABEL}, ${ago(s.started)}</span>${standingTag(s)}<span class="out">${OUTSIDE}</span></p>`;
}
function magBlock(s) {
  const rate = s.n.perHour != null ? `<span class="rate">${num(s.n.perHour)} views an hour</span>` : '';
  return `<div class="story-fig">${numeral(s.n.magnitude)}<span class="lab">magnitude</span><span class="trend">${TREND[s.n.trend]}</span>${rate}</div>`;
}
function storyRow(s, i) {
  return `<li class="story" id="s-${esc(s.id)}" data-mag="${s.n.magnitude ?? 0}" data-rate="${s.n.perHour ?? 0}" data-start="${s.started}" data-desks="${esc(s.desks.join(' '))}">
  ${magBlock(s)}
  <div class="story-body">
    ${storyMeta(s)}
    <h3><a href="/story/${esc(s.id)}/">${esc(s.title)}</a></h3>
    <p class="dek">${esc(s.dek)}</p>
    ${s.origin ? postFigure(s.origin) : ''}
    ${worldsBlock(s, i < 4)}
  </div>
  <aside class="story-side">
    ${spark(s)}
    <dl class="facts"><div><dt class="lab">Views</dt><dd>${num(s.n.views)}</dd></div><div><dt class="lab">Posts tracked</dt><dd>${s.posts.length}</dd></div></dl>
    <a href="/story/${esc(s.id)}/">Full story</a>
  </aside>
</li>`;
}
// A story as one ruled line: its magnitude, its title, where it sits and how it stands.
function storyLine(s, { dek = false } = {}) {
  const where = s.desks.map((id) => deskById.get(id)?.name).filter(Boolean).map(esc).join(' · ');
  return `<li><a class="st" href="/story/${esc(s.id)}/"><span class="st-mag">${mag(s.n.magnitude)}</span><span class="st-title">${esc(s.title)}${dek ? `<span class="st-dek">${esc(s.dek)}</span>` : ''}</span><span class="st-side"><span class="lab lab-quiet">${where}</span>${standingTag(s)}</span></a></li>`;
}
const empty = (title, text = '') => `<div class="empty"><h3>${title}</h3>${text ? `<p>${text}</p>` : ''}</div>`;
const sortBar = (keys) => `<div class="sort" role="group" aria-label="Order">${keys.map(([key, label], i) => `<button type="button" data-sort="${key}" aria-pressed="${i ? 'false' : 'true'}">${label}</button>`).join('')}</div>`;

// ---------- the page shell: ears, nameplate, dateline, sections

const FONTS = 'https://fonts.googleapis.com/css2?family=UnifrakturMaguntia&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Libre+Franklin:wght@400..800&display=swap';
const SECTIONS = [['/', 'Front'], ...DESKS.groups.map((g) => [`/section/${g.id}/`, g.name]), ['/stories/', 'Stories'], ['/desks/', 'Desks'], ['/archive/', 'Back issues'], ['/about/', 'About']];

function page({ title, description, path, body, current, edition = null, front = false, mode = 'paper' }) {
  const modes = [['paper', '/', 'The Paper'], ['pulse', '/pulse/', 'Internet Pulse'], ['newsletter', '/newsletter/', 'The Newsletter']]
    .map(([key, href, label]) => `<a href="${href}"${key === mode ? ' aria-current="page"' : ''}>${label}</a>`).join('');
  const nav = SECTIONS.map(([href, label]) => `<a href="${href}"${current === href ? ' aria-current="page"' : ''}>${esc(label)}</a>`).join('');
  const asof = `<time id="asof" datetime="${new Date(NOW).toISOString()}">${hhmm(NOW)} ${ZONE_LABEL} · ${day(NOW)}</time>`;
  const left = mode === 'newsletter' ? 'The Newsletter<br>A letter a day by Soochiebot' : mode === 'pulse' ? 'Internet Pulse<br>The largest posts on X, read hourly' : edition ? `${edition.partial ? 'Today, so far' : 'Morning edition'}<br>${edition.partial ? longDay(edition.edition.day) : `Published ${longDay(nextDay(edition.edition.day))}`}` : `Monitoring the Situation<br>${esc(SITE.line)}`;
  const plate = front
    ? `<h1 class="plate"><a href="/"><span class="plate-name">Monitoring the Situation</span></a></h1>`
    : `<p class="plate plate-s"><a href="/"><span class="plate-name">Monitoring the Situation</span></a></p>`;
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(description)}">
${DEMO ? '<meta name="robots" content="noindex">' : ''}
${SITE.url ? `<link rel="canonical" href="${esc(SITE.url + path)}">\n<meta property="og:url" content="${esc(SITE.url + path)}">` : ''}
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(description)}">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#f2eee4">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="${FONTS.replaceAll('&', '&amp;')}" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script src="/app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to the paper</a>
${DEMO ? '<p class="demo">Design test. Every story and post below is invented. Only the pinned post is real.</p>' : ''}
<div class="paper">
<header>
  <div class="ears">
    <p class="ear">${left}</p>
    <p class="ear-c">“${esc(SITE.pinned.text)}” <a href="/about/">${esc(SITE.pinned.name)}, pinned: why this paper exists</a></p>
    <p class="ear ear-r">As of ${asof}<br>Read from X every hour</p>
  </div>
  ${plate}
  <nav class="mode" aria-label="Read it as">${modes}</nav>
  <nav class="secnav" aria-label="Sections">${nav}</nav>
</header>
<p class="stale" id="stale" role="status" hidden></p>
<main id="main">
${body}
</main>
<footer class="foot">
  <div class="foot-method"><p class="lab">How this paper is made</p>${SITE.method.map((m) => `<p>${esc(m)}</p>`).join('')}<p>Soochiebot, a program set to sound like Sean Sooch, writes the Newsletter: one letter a day, from this record and nothing else, labelled where it appears.</p></div>
  <p class="foot-links"><a href="/about/">About the paper</a><a href="/archive/">Back issues</a><a href="https://seansooch.dev/">seansooch.dev</a></p>
</footer>
</div>
</body>
</html>
`;
}

const head = ({ label, title, dek = '', extra = '', fig = '' }) => `<section class="head">
  <div><p class="lab">${label}</p><h1>${title}</h1>${dek ? `<p class="dek">${dek}</p>` : ''}${extra}</div>
  ${fig ? `<div class="head-fig">${fig}</div>` : ''}
</section>`;

// ---------- an edition: the front page of one day

function folio(ed) {
  const i = editions.indexOf(ed);
  const prev = editions[i - 1], next = editions[i + 1];
  const turn = [prev ? `<a href="/edition/${prev.edition.day}/">‹ ${esc(shortDay(prev.edition.day))}</a>` : '', next ? `<a href="/edition/${next.edition.day}/">${esc(shortDay(next.edition.day))} ›</a>` : ''].filter(Boolean).join(' · ');
  return `<p class="folio"><span>Covering ${esc(ed.edition.label)}${ed.partial ? `, to ${hhmm(NOW)} ${ZONE_LABEL}` : ''}</span><span>${plural(ed.counts.posts, 'post', 'posts')} confirmed · ${plural(ed.counts.accounts, 'account', 'accounts')} · ${ed.counts.desks} desks</span><span>${plural(ed.counts.stories, 'story', 'stories')} · ${num(ed.counts.views)} views on the day</span>${turn ? `<span>${turn}</span>` : ''}</p>`;
}

function itemBlock(p, { big = true } = {}) {
  return `<div class="item" data-desks="${esc(p.desk)}">
    ${big ? `<span class="big">${num(p.views)}</span>` : ''}
    <p class="line">${esc(p.line)}</p>
    <p class="who">${big ? '' : `${num(p.views)} views · `}<a href="${esc(xUrl(p.id))}" rel="noopener noreferrer" target="_blank">@${esc(p.handle ?? 'post')}</a> · ${esc(deskName(p.desk))}</p>
  </div>`;
}

function leadArticle(ed) {
  const e = ed.stories[0];
  const s = storyById.get(e.id);
  const what = s.what.slice(0, 3);
  const worlds = s.worlds.length ? `<div class="box"><span class="lab">Seen from ${s.worlds.length === 1 ? 'one world' : `${inWords(s.worlds.length)} worlds`}</span><ul>${s.worlds.map((w) => `<li><b>${esc(w.name)}.</b> ${esc(w.sees)}</li>`).join('')}</ul></div>` : '';
  const common = s.common ? `<div class="box"><span class="lab">On the record</span><p>${esc(s.common)}</p></div>` : '';
  return `<article id="lead" data-desks="${esc(s.desks.join(' '))}">
    <p class="kicker">${kicker(s)}</p>
    <h2 class="lead-h"><a href="/story/${esc(s.id)}/">${esc(s.title)}</a></h2>
    <p class="dek">${esc(s.dek)}</p>
    <p class="byline">The day's largest story · ${num(e.reach)} views on the day across ${plural(e.posts.length, 'post', 'posts')} · ${plural((s.sources ?? []).length, 'source', 'sources')} · researched by the editor</p>
    <div class="cols">
      ${what.map((t, i) => `<p${i ? '' : ' class="drop"'}>${esc(t)}</p>`).join('')}
      ${worlds}${common}
      ${s.next ? `<p><b>What to watch.</b> ${esc(s.next)}</p>` : ''}
    </div>
    <p class="more-link"><a href="/story/${esc(s.id)}/">${s.what.length > what.length ? 'The full story, its posts and its sources' : 'Its posts and its sources'}</a></p>
  </article>`;
}

function editionBody(ed, { front = false } = {}) {
  const ranked = ed.stories;
  const story = (e) => storyById.get(e.id);
  const brief = ranked.slice(0, PAPER.briefing);
  const sofar = front && todayEd && todayEd !== ed && todayEd.stories.length
    ? `<section class="sofar" aria-label="Today so far"><span class="lab">Today so far, to ${hhmm(NOW)} ${ZONE_LABEL}</span><ol>${todayEd.stories.slice(0, 3).map((e) => `<li><a href="/story/${esc(e.id)}/">${esc(story(e).title)}</a> <span class="lab lab-quiet">${num(e.reach)}</span></li>`).join('')}</ol><a href="/pulse/">Internet Pulse: the largest posts right now</a></section>` : '';
  const briefing = brief.length ? `<section class="brief" aria-labelledby="brief-h"><h2 class="lab" id="brief-h">The day in sixty seconds</h2><ol>${brief.map((e, i) => `<li><a href="${i ? `/story/${esc(e.id)}/` : '#lead'}"><span class="rank-n">${i + 1}</span><span class="brief-t">${esc(story(e).title)}</span><span class="num">${num(e.reach)} views</span></a></li>`).join('')}</ol></section>` : '';
  const unreported = ed.unreported.length ? `<section class="rail-sec" aria-labelledby="unrep-h">
      <h2 class="lab" id="unrep-h">Big on X, not yet a story</h2>
      ${itemBlock(ed.unreported[0])}
      ${ed.unreported.length > 1 ? `<ul class="small-list">${ed.unreported.slice(1).map((p) => `<li>${itemBlock(p, { big: false })}</li>`).join('')}</ul>` : ''}
    </section>` : '';
  const further = ranked.slice(4, 12);
  const rest = further.length ? `<section class="rail-sec" aria-labelledby="rest-h"><h2 class="lab" id="rest-h">Further down the record</h2><ol class="rank-list">${further.map((e) => `<li><a href="/story/${esc(e.id)}/"><span class="t">${esc(story(e).title)}</span><span class="num">${num(e.reach)}</span><span class="meta">${ordinal(e.rank)} · ${esc(STANDING[e.standing] ?? e.standing)} · ${esc(e.sections.map(sectionName).join(', '))}</span></a></li>`).join('')}</ol></section>` : '';
  const three = ranked.slice(1, 4);
  const row = three.length ? `<section class="part" aria-label="The next stories"><div class="row3">${three.map((e) => `<article data-desks="${esc(story(e).desks.join(' '))}"><p class="kicker">${ordinal(e.rank)} · ${kicker(story(e))}</p><h3><a href="/story/${esc(e.id)}/">${esc(story(e).title)}</a></h3><p class="body">${esc(story(e).dek)}</p><p class="who">${num(e.reach)} views on the day · ${plural(e.posts.length, 'post', 'posts')}</p></article>`).join('')}</div></section>` : '';
  const L = ed.letter;
  const opinion = `<section class="opinion" id="newsletter" aria-labelledby="newsletter-h">
    <div><h2 class="lab" id="newsletter-h">From the Newsletter</h2><p class="opinion-name">The read</p><p class="opinion-about">Soochiebot's letter on the day ends with one call on what it adds up to. A program, labelled as one, and kept apart from the news.</p></div>
    <div class="opinion-body">${L
    ? `<h3 class="opinion-h"><a href="/newsletter/${ed.edition.day}/">${esc(L.subject)}</a></h3>${L.read.text.map((t) => `<p class="op">${letterText(t, L)}</p>`).join('')}<p class="who">Soochiebot (${esc(L.model)}) · <a href="/newsletter/${ed.edition.day}/">Read the whole letter, with its references</a></p>`
    : `<p class="opinion-none">No letter for this day. Soochiebot writes one each morning from the edition; on a day it does not, this space stays empty rather than filled.</p>`}</div>
  </section>`;
  const watched = ed.watched.length ? `<section class="part" aria-labelledby="watched-h"><div class="part-h"><h2 id="watched-h">What the internet watched</h2><p>The largest posts the editor described that no story covers, outside the news sections.</p></div><div class="items">${ed.watched.slice(0, 6).map((p) => itemBlock(p)).join('')}</div></section>` : '';
  const strip = `<section class="part" id="sections" aria-labelledby="sections-h"><div class="part-h"><h2 id="sections-h">The six sections</h2><p>Posts confirmed and views gained on the day, and when each section was posting, by Eastern hour.</p></div><div class="strip">${ed.sections.map((sec) => {
    const peak = Math.max(...sec.hours, 1);
    const top = sec.stories[0] ? `<a href="/story/${esc(sec.stories[0])}/">${esc(storyById.get(sec.stories[0]).title)}</a>` : sec.items[0] ? esc(sec.items[0].line) : 'Quiet: nothing from this section cleared the record.';
    return `<div><h3><a href="/section/${sec.id}/">${esc(sec.name)}</a></h3><p class="meta">${plural(sec.posts, 'post', 'posts')} · ${num(sec.views)} · ${Math.round(sec.share * 100)}%</p><span class="minibars" aria-hidden="true">${sec.hours.map((h) => `<i style="height:${h ? Math.max(8, Math.round((100 * h) / peak)) : 4}%"${h ? '' : ' class="off"'}></i>`).join('')}</span><p>${top}</p></div>`;
  }).join('')}</div></section>`;
  const leadPart = ranked.length
    ? `<div class="front">${leadArticle(ed)}<aside class="rail">${unreported}${rest}${!unreported && !rest ? `<section class="rail-sec">${empty('A short day on the record.')}</section>` : ''}</aside></div>`
    : `<div class="front"><div>${empty('No researched story on this day.', 'The record read the posts below. A day without a story is shown as one, not filled.')}</div><aside class="rail">${unreported}</aside></div>`;
  return `${folio(ed)}${sofar}${briefing}${leadPart}${row}${opinion}${watched}${strip}`;
}

function editionPage(ed, { front = false } = {}) {
  const title = front ? `${SITE.name}: ${SITE.line}` : `${ed.edition.label} · ${SITE.name}`;
  const lead = ed.stories[0] ? storyById.get(ed.stories[0].id) : null;
  const description = lead ? `${ed.edition.label}: ${lead.title}. ${ed.counts.stories} stories, ranked by the views they gained that day, from ${ed.counts.posts} posts confirmed with X.` : `${ed.edition.label} on the record of what the internet paid attention to.`;
  return page({ title, description, path: front ? '/' : `/edition/${ed.edition.day}/`, body: editionBody(ed, { front }), current: front ? '/' : null, edition: ed, front });
}

// ---------- the other pages

function pulsePage() {
  const active = desks.filter((d) => d.posts > 0).length;
  const [lead, ...rest] = pulse;
  const early = captures.length < 4 ? ` <strong>Early days: ${captures.length === 1 ? 'one reading' : captures.length + ' readings'} so far, so each desk's bars show only when its posts began. They sharpen with every hourly reading.</strong>` : '';
  const shown = live.slice(0, 8);
  const body = `${head({ label: 'Internet Pulse · live', title: 'The largest posts right now', dek: `What every corner of the internet is passing around, read from X every hour across all ${desks.length} desks. The sentence above each post is the editor's and says what it is, not whether it is right.` })}
${lead ? leadBlock(lead) : ''}
<section class="part-1" id="desks" aria-labelledby="desks-h">
  <div class="part-h"><h2 id="desks-h">Which worlds do you live in?</h2>
    <p>The last 24 hours on all ${desks.length} desks. Each bar is one hour of views gained. Select the desks you already follow, and the page marks what you are not seeing.${early}</p>
  </div>
  <div class="sec-tools" id="mine-tools" hidden><span class="lab" id="mine-count">None selected</span><button type="button" class="btn" id="mine-clear">Clear</button></div>
  <div class="dk-grid" role="group" aria-label="Desks you follow">${desks.map((d) => deskCard(d)).join('')}</div>
</section>
${lead && !rest.length ? '' : `<section class="part" id="pulse" aria-labelledby="pulse-h">
  <div class="part-h"><h2 id="pulse-h">Every desk, largest first</h2>
    <p>The number is magnitude: 6.0 is a million views, 7.0 is ten million.</p>
    ${rest.length ? sortBar([['views', 'Largest'], ['pace', 'Fastest'], ['start', 'Newest']]) : ''}
  </div>
  ${rest.length ? pulseList(rest, 'pulse-list') : empty('The first pulse is being read.', `The instrument is recording on ${active} of ${desks.length} desks. Posts appear here once each has been confirmed with X and passed by the editor.`)}
</section>`}
<section class="part" id="stories" aria-labelledby="stories-h">
  <div class="part-h"><h2 id="stories-h">Researched stories</h2><p>Slower and deeper: what happened, how each world is describing it, and what is on the record, with sources.</p></div>
  ${shown.length ? `<ul class="st-list">${shown.map((s) => storyLine(s)).join('')}</ul>${live.length > shown.length ? `<p class="note"><a href="/stories/">All ${live.length} current stories</a></p>` : ''}` : empty('No stories written up yet.')}
</section>`;
  return page({ title: `Internet Pulse · ${SITE.name}`, description: `The largest posts on X right now, across ${DESK_COUNT} desks, measured hourly and described by the editor.`, path: '/pulse/', body, mode: 'pulse' });
}

function storiesPage() {
  const body = `${head({ label: `${live.length} current`, title: 'Researched stories', dek: 'For the things worth more than a line: what happened, why it is spreading, how each world is describing it, and what is on the record. Each claim has a source, and each post was confirmed with X.' })}
<section class="part-1" id="bulletin">
  <div class="part-h"><h2>The last 48 hours</h2>${sortBar([['mag', 'Largest'], ['rate', 'Fastest'], ['start', 'Newest']])}</div>
  ${live.length ? `<ol class="stories">${live.map(storyRow).join('')}</ol>` : empty('The first stories are being written.')}
  ${past.length ? `<p class="note"><a href="/archive/#past">${past.length} earlier ${past.length === 1 ? 'story' : 'stories'} in the back issues</a></p>` : ''}
</section>`;
  return page({ title: `Stories · ${SITE.name}`, description: 'Researched write-ups of what the internet is passing around: what happened, how each world sees it, and what is established.', path: '/stories/', body, current: '/stories/' });
}

function storyPage(s) {
  const seen = inEditions.get(s.id) ?? [];
  const inPaper = seen.length ? `<section aria-labelledby="inp-h"><h2 class="lab" id="inp-h">In the paper</h2><ol class="in-paper">${seen.map((x) => `<li><a href="/edition/${x.day}/">${esc(shortDay(x.day))}${x.partial ? ', so far' : ''}</a>: ${ordinal(x.rank)}, ${num(x.reach)} views on the day</li>`).join('')}</ol></section>` : '';
  const body = `<article class="full" data-desks="${esc(s.desks.join(' '))}">
  <header class="full-head">
    ${storyMeta(s)}
    <h1>${esc(s.title)}</h1>
    <p class="dek">${esc(s.dek)}</p>
  </header>
  <div class="full-main">
    <h2>What happened</h2>${s.what.map((t) => `<p>${esc(t)}</p>`).join('')}
    <h2>Why it is spreading</h2><p>${esc(s.why)}</p>
    ${worldsBlock(s, true)}
    ${s.next ? `<h2>What to watch</h2><p>${esc(s.next)}</p>` : ''}
    <h2>The posts</h2>${s.cited.map((p) => citedFigure(p)).join('')}
    ${(s.corrections ?? []).length ? `<h2>Corrections</h2><ul class="sources">${s.corrections.map((c) => `<li><time datetime="${esc(c.at)}">${hhmm(Date.parse(c.at))} ${ZONE_LABEL}, ${day(Date.parse(c.at))}</time> ${esc(c.text)}</li>`).join('')}</ul>` : ''}
    ${(s.sources ?? []).length ? `<h2>Sources</h2><ul class="sources">${s.sources.map((x) => `<li><a href="${esc(x.url)}" rel="noopener noreferrer" target="_blank">${esc(x.label)}</a></li>`).join('')}</ul>` : ''}
  </div>
  <aside class="full-side">
    <p class="updated">Written up ${hhmm(Date.parse(s.updated_at))} ${ZONE_LABEL}, ${day(Date.parse(s.updated_at))}</p>
    ${magBlock(s)}
    ${spark(s, 280, 80)}
    <dl class="facts"><div><dt class="lab">Views</dt><dd>${num(s.n.views)}</dd></div><div><dt class="lab">Last hour</dt><dd>${s.n.perHour == null ? 'n/a' : num(s.n.perHour)}</dd></div><div><dt class="lab">Posts tracked</dt><dd>${s.posts.length}</dd></div><div><dt class="lab">Began</dt><dd>${hhmm(s.started)} ${ZONE_LABEL}</dd></div></dl>
    ${inPaper}
  </aside>
</article>`;
  return page({ title: `${s.title} · ${SITE.name}`, description: s.dek, path: `/story/${s.id}/`, body });
}

function sectionPage(g) {
  const ed = frontEd;
  const sec = ed?.sections.find((x) => x.id === g.id);
  const mine = desks.filter((d) => d.group === g.id);
  const recent = stories.filter((s) => s.desks.some((d) => deskById.get(d)?.group === g.id)).sort((a, b) => b.started - a.started).slice(0, 12);
  const peak = sec ? Math.max(...sec.hours, 1) : 1;
  const fig = sec ? `<dl class="facts"><div><dt class="lab">Posts confirmed</dt><dd>${sec.posts.toLocaleString('en-US')}</dd></div><div><dt class="lab">Views on the day</dt><dd>${num(sec.views)}</dd></div><div><dt class="lab">Share of the day</dt><dd>${Math.round(sec.share * 100)}%</dd></div></dl>` : '';
  const body = `${head({ label: `Section · ${ed ? esc(ed.edition.label) : 'no edition yet'}`, title: esc(g.name), dek: `${inWords(mine.length).replace(/^./, (c) => c.toUpperCase())} desks: ${mine.map((d) => `<a href="/desk/${d.id}/">${esc(d.name)}</a>`).join(', ')}.`, fig })}
${sec ? `<section class="part-1" aria-labelledby="hours-h"><div class="part-h"><h2 id="hours-h">When it was posting</h2><p>Posts confirmed in each Eastern hour of ${esc(ed.edition.label)}.</p></div><span class="dk-bars dk-bars-wide" aria-hidden="true">${sec.hours.map((h) => `<i style="height:${h ? Math.max(4, Math.round((96 * h) / peak)) : 1}px"${h ? '' : ' class="off"'}></i>`).join('')}</span><p class="axis" aria-hidden="true"><span>midnight</span><span>6 a.m.</span><span>noon</span><span>6 p.m.</span><span>11 p.m.</span></p></section>` : ''}
${sec ? `<section class="part" aria-labelledby="ined-h"><div class="part-h"><h2 id="ined-h">In the edition</h2><p>This section's stories on ${esc(ed.edition.label)}, in the order of the whole paper.</p></div>${sec.stories.length ? `<ol class="rank-list">${sec.stories.map((id) => ed.stories.find((e) => e.id === id)).map((e) => `<li><a href="/story/${esc(e.id)}/"><span class="t">${esc(storyById.get(e.id).title)}</span><span class="num">${num(e.reach)}</span><span class="meta">${ordinal(e.rank)} in the paper · ${esc(STANDING[e.standing] ?? e.standing)}</span></a></li>`).join('')}</ol>` : empty('No researched story in this section that day.')}
${sec.items.length ? `<div class="items">${sec.items.map((p) => itemBlock(p)).join('')}</div>` : ''}</section>` : ''}
<section class="part" aria-labelledby="desks-h"><div class="part-h"><h2 id="desks-h">The desks, last 24 hours</h2></div><div class="dk-grid">${mine.map((d) => deskCard(d, { link: true })).join('')}</div></section>
<section class="part" aria-labelledby="recent-h"><div class="part-h"><h2 id="recent-h">Recent stories</h2></div>${recent.length ? `<ul class="st-list">${recent.map((s) => storyLine(s, { dek: true })).join('')}</ul>` : empty('None yet.')}</section>`;
  return page({ title: `${g.name} · ${SITE.name}`, description: `${g.name}: the desks, the day's stories and the posts the record read in this section.`, path: `/section/${g.id}/`, body, current: `/section/${g.id}/` });
}

function deskPage(d) {
  const all = [...d.stories, ...d.also];
  const fig = `<p>${d.posts ? numeral(d.mag, 'big') : '<span class="big is-quiet">quiet</span>'}</p><p class="lab lab-quiet">${d.posts ? 'magnitude, last 24 hours' : 'nothing cleared the floor'}</p>`;
  const body = `${head({ label: `<a href="/section/${d.group}/">${esc(groupName(d))}</a> · ${d.code}`, title: esc(d.name), dek: esc(d.scope), extra: `<p class="beats">${d.beats.map((b) => `<span>${esc(b)}</span>`).join('')}</p>`, fig })}
<section class="part-1">
  <span class="dk-bars dk-bars-wide" role="img" aria-label="Views gained on this desk in each of the last 24 hours">${bars(d, 96)}</span>
  <p class="axis" aria-hidden="true"><span>24 h ago</span><span>18 h</span><span>12 h</span><span>6 h</span><span>now</span></p>
  <p class="note">${d.posts ? `${d.posts} posts written in the last 24 hours are on record for this desk, with ${num(d.views)} views between them. Each bar is one hour of views gained.` : 'Nothing on this desk cleared its floor in the last 24 hours.'}</p>
</section>
<section class="part">
  <div class="part-h"><h2>On this desk now</h2></div>
  ${d.pulse.length ? pulseList(d.pulse) : empty('Nothing from this desk is on the pulse right now.', 'A quiet desk is reported as quiet. Nothing is added to fill it.')}
</section>
<section class="part">
  <div class="part-h"><h2>Researched stories on this desk</h2></div>
  ${all.length ? `<ol class="stories">${all.map(storyRow).join('')}</ol>` : `<p class="note">None in the last 48 hours.</p>`}
  ${d.past.length ? `<p class="note"><a href="/archive/#past">${d.past.length} earlier ${d.past.length === 1 ? 'story' : 'stories'} on this desk in the back issues</a></p>` : ''}
</section>`;
  return page({ title: `${d.name} · ${SITE.name}`, description: d.scope, path: `/desk/${d.id}/`, body, current: '/desks/' });
}

function desksPage() {
  const body = `${head({ label: `${desks.length} desks`, title: 'The desks', dek: `Every part of the internet's attention this paper watches, in ${inWords(DESKS.groups.length)} sections. Each desk is swept on a schedule, and a quiet desk is reported as quiet.` })}
${DESKS.groups.map((g) => `<section class="part-1"><div class="part-h"><h2><a href="/section/${g.id}/">${esc(g.name)}</a></h2></div><div class="dk-grid">${desks.filter((d) => d.group === g.id).map((d) => deskCard(d, { link: true })).join('')}</div></section>`).join('\n')}`;
  return page({ title: `The desks · ${SITE.name}`, description: `The ${DESK_COUNT} desks this paper watches, in ${inWords(DESKS.groups.length)} sections.`, path: '/desks/', body, current: '/desks/' });
}

function archivePage() {
  const issues = [...editions].reverse();
  const days = new Map();
  for (const s of past) { const k = dateOf(s.started); if (!days.has(k)) days.set(k, []); days.get(k).push(s); }
  const list = [...days.values()].map((l) => `<section class="part-1"><div class="part-h"><h2>${day(l[0].started)}</h2></div><ul class="st-list">${l.sort((a, b) => (b.n.magnitude ?? 0) - (a.n.magnitude ?? 0)).map((s) => storyLine(s, { dek: true })).join('')}</ul></section>`).join('\n');
  const body = `${head({ label: `${plural(issues.length, 'edition', 'editions')}`, title: 'Back issues', dek: 'Every day of the record has a front page of its own, kept as the record had it at the end of that day.' })}
<section class="part-1" id="issues" aria-labelledby="issues-h"><div class="part-h"><h2 id="issues-h">Editions</h2></div>
${issues.length ? `<div class="table-wrap"><table class="issues"><thead><tr><th scope="col">Day</th><th scope="col">The lead</th><th scope="col">Stories</th><th scope="col">Views on the day</th></tr></thead><tbody>${issues.map((e) => `<tr><td class="n"><a href="/edition/${e.edition.day}/">${esc(shortDay(e.edition.day))}${e.partial ? ', so far' : ''}</a></td><td class="t">${e.stories[0] ? esc(storyById.get(e.stories[0].id).title) : 'No researched story'}</td><td class="n">${e.counts.stories}</td><td class="n">${num(e.counts.views)}</td></tr>`).join('')}</tbody></table></div>` : empty('No edition yet.')}
</section>
<section class="part" id="past" aria-labelledby="past-h"><div class="part-h"><h2 id="past-h">Past stories</h2><p>A story leaves the current list 48 hours after it began and is kept here, as it was last written up, with the numbers its posts had reached.</p></div>
${list || empty('Nothing here yet.', 'The record began on 9 October 2026. Stories arrive here two days after they start.')}
</section>`;
  return page({ title: `Back issues · ${SITE.name}`, description: 'Every day of the record as a front page, and every past story, by day.', path: '/archive/', body, current: '/archive/' });
}

// ---------- the Newsletter: Soochiebot's letter for a day, set as a letter, referenced in the Harvard style
//
// A letter names its sources by id (contract/NEWSLETTER.md); everything a reference says is looked up here: a
// story's title and the day it began, a post's author and the day it was written. Cite Them Right's Harvard
// forms: Author (Year) Title. Available at: URL (Accessed: date). One author in one year more than once takes a,
// b, c in the order of the list, which is alphabetical by author, then year, then title.

const letters = editions.filter((e) => e.letter);
const MONTH_DAY = new Intl.DateTimeFormat('en-GB', { timeZone: 'UTC', day: 'numeric', month: 'long' });
const FULL = new Intl.DateTimeFormat('en-GB', { timeZone: 'UTC', day: 'numeric', month: 'long', year: 'numeric' });
const ofDay = (d, f = FULL) => f.format(new Date(`${d}T12:00:00Z`));

// A sentence of a letter on a page: escaped, **bold** as the one mark it may carry, each figure in its place.
function letterText(t, L) {
  return esc(t).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\{([a-z][a-z0-9_]*)\}/g, (_, k) => `<b class="fig">${esc(L.figures[k]?.value ?? '')}</b>`);
}

function references(L) {
  const refs = Object.entries(L.sources).map(([key, src]) => {
    if (src.story) {
      const st = storyById.get(src.story);
      return { key, author: SITE.name, year: st.started_at.slice(0, 4), title: st.title, href: `${SITE.url}/story/${st.id}/`, local: `/story/${st.id}/`, kind: 'story' };
    }
    const p = merged.get(src.post);
    const created = p?.created_at ? dayKey(Date.parse(p.created_at)) : null;
    const name = p?.author?.name ? fromX(p.author.name) : `@${src.handle}`;
    return { key, author: name, handle: src.handle, year: created ? created.slice(0, 4) : 'n.d.', title: `Post on X${created ? `, ${ofDay(created, MONTH_DAY)}` : ''}`, href: xUrl(src.post), kind: 'post' };
  });
  refs.sort((a, b) => a.author.localeCompare(b.author, 'en', { sensitivity: 'base' }) || a.year.localeCompare(b.year) || a.title.localeCompare(b.title));
  const many = new Map();
  for (const r of refs) many.set(`${r.author}|${r.year}`, (many.get(`${r.author}|${r.year}`) ?? 0) + 1);
  const next = new Map();
  for (const r of refs) {
    const k = `${r.author}|${r.year}`;
    r.suffix = many.get(k) > 1 ? 'abcdefghijklmnopqrstuvwxyz'[(next.set(k, (next.get(k) ?? -1) + 1), next.get(k))] : '';
    r.cite = `${r.author}, ${r.year}${r.suffix}`;
  }
  return refs;
}

function letterArticle(ed, { full = true } = {}) {
  const L = ed.letter;
  const refs = references(L);
  const byKey = new Map(refs.map((r) => [r.key, r]));
  const n = letters.indexOf(ed) + 1;
  const cite = (keys) => {
    const list = [...new Set(keys)].map((k) => byKey.get(k)).filter(Boolean);
    return list.length ? ` <span class="cite">(${list.map((r) => `<a href="#ref-${esc(r.key)}">${esc(r.cite)}</a>`).join('; ')})</span>` : '';
  };
  const paras = (text, keys) => text.map((t, i) => `<p>${letterText(t, L)}${i === text.length - 1 ? cite(keys) : ''}</p>`).join('');
  const published = ofDay(L.published);
  const i = letters.indexOf(ed);
  const turn = [letters[i - 1] ? `<a href="/newsletter/${letters[i - 1].edition.day}/">Earlier: ${esc(shortDay(letters[i - 1].edition.day))}</a>` : '',
    letters[i + 1] ? `<a href="/newsletter/${letters[i + 1].edition.day}/">Later: ${esc(shortDay(letters[i + 1].edition.day))}</a>` : ''].filter(Boolean).join('');
  return `<article class="letter" aria-labelledby="re-${ed.edition.day}">
  <header class="letterhead">
    <p class="lh-name">Monitoring the Situation</p>
    <p class="lab lh-sub">The Newsletter · No. ${n}</p>
  </header>
  <p class="l-date"><time datetime="${esc(L.published)}">${esc(longDay(L.published))}</time></p>
  <h2 class="l-re" id="re-${ed.edition.day}"><span class="lab">Re:</span> ${esc(L.subject)}</h2>
  <p class="l-dear">Dear reader,</p>
  <p class="l-summary">${esc(L.summary)}</p>
  <section class="l-part"><h3>${esc(L.lead.head)}</h3>${paras(L.lead.text, L.lead.cites)}</section>
  ${L.notes.map((nt) => `<section class="l-part"><p class="lab">${esc(deskName(nt.desk))}</p><h3>${esc(nt.head)}</h3>${paras([nt.text], nt.cites)}</section>`).join('\n  ')}
  <section class="l-part l-read"><h3>The read</h3>${paras(L.read.text, L.read.cites)}</section>
  <div class="l-sign">
    <p>Yours,</p>
    <p class="l-sig">Soochiebot</p>
    <p class="l-sig-note">A program writing in Sean Sooch's voice, from the record of ${esc(SITE.name)} and nothing else (${esc(L.model)}). Written for ${esc(ed.edition.label)}; published ${esc(published)}. The numbers in this letter are the record's, and each is cited to its source.</p>
  </div>
  ${full ? `<section class="refs" aria-labelledby="refs-${ed.edition.day}">
    <h3 id="refs-${ed.edition.day}">References</h3>
    <ol class="ref-list">${refs.map((r) => `<li id="ref-${esc(r.key)}">${esc(r.author)}${r.handle ? ` [@${esc(r.handle)}]` : ''} (${esc(r.year)}${r.suffix}) ${r.kind === 'story' ? `<i>${esc(r.title)}</i>` : esc(r.title)}. Available at: <a href="${esc(r.href)}"${r.kind === 'post' ? ' rel="noopener noreferrer" target="_blank"' : ''}>${esc(r.href)}</a> (Accessed: ${esc(published)}).</li>`).join('')}</ol>
  </section>
  ${Object.keys(L.figures).length ? `<section class="refs" aria-labelledby="figs-${ed.edition.day}"><h3 id="figs-${ed.edition.day}">Figures</h3><dl class="fig-list">${Object.values(L.figures).map((f) => `<div><dt>${esc(f.value)}</dt><dd>${esc(f.of)} <span class="cite">(<a href="#ref-${esc(f.source)}">${esc(byKey.get(f.source)?.cite ?? '')}</a>)</span></dd></div>`).join('')}</dl></section>` : ''}
  <p class="l-paper"><a href="/edition/${ed.edition.day}/">The Paper for ${esc(ed.edition.label)}</a></p>
  ${turn ? `<nav class="l-turn" aria-label="Other letters">${turn}</nav>` : ''}` : ''}
</article>`;
}

function letterPage(ed) {
  const L = ed.letter;
  return page({ title: `${L.subject} · The Newsletter · ${SITE.name}`, description: L.summary, path: `/newsletter/${ed.edition.day}/`, body: letterArticle(ed), mode: 'newsletter' });
}

function newsletterPage() {
  const latest = letters.at(-1);
  const earlier = [...letters].reverse().slice(1);
  const body = latest
    ? `${letterArticle(latest)}
${earlier.length ? `<section class="part letters" aria-labelledby="earlier-h"><div class="part-h"><h2 id="earlier-h">Earlier letters</h2></div><ol class="st-list">${earlier.map((e) => `<li><a class="st" href="/newsletter/${e.edition.day}/"><span class="st-mag">${esc(shortDay(e.edition.day))}</span><span class="st-title">${esc(e.letter.subject)}<span class="st-dek">${esc(e.letter.summary)}</span></span><span class="st-side"><span class="lab lab-quiet">No. ${letters.indexOf(e) + 1}</span></span></a></li>`).join('')}</ol></section>` : ''}`
    : `<article class="letter"><header class="letterhead"><p class="lh-name">Monitoring the Situation</p><p class="lab lh-sub">The Newsletter</p></header>${empty('The first letter has not been written.', 'Soochiebot writes one each morning from the day before. Until it does, this page says so rather than filling it.')}</article>`;
  return page({ title: `The Newsletter · ${SITE.name}`, description: 'A letter a day by Soochiebot on what the internet paid attention to, from the record of Monitoring the Situation, with its references.', path: '/newsletter/', body, mode: 'newsletter' });
}

const pinDate = (p) => `<time datetime="${esc(p.created_at)}">${dateOf(Date.parse(p.created_at))}</time>`;
function aboutPage() {
  const p = SITE.pinned;
  const body = `<section class="about">
  <p class="lab">Pinned</p>
  <blockquote class="pin-big">“${esc(p.text)}”</blockquote>
  <p class="by"><b>${esc(p.name)}</b><span>@${esc(p.handle)} · ${pinDate(p)}</span><a class="open" href="${esc(p.url)}" rel="noopener noreferrer" target="_blank">Open on X</a></p>
  ${p.quotes ? `<p class="pin-quoted">Quoting @${esc(p.quotes.handle)}: “${esc(p.quotes.text)}”</p>` : ''}
  <h2>${esc(SITE.line)}</h2>
  ${SITE.purpose.map((t) => `<p>${esc(t)}</p>`).join('')}
  <h2>How the paper is made</h2>
  <ol class="steps">
    <li><h3>Grok reads X.</h3><p>Every hour it records what is spreading on each of ${DESK_COUNT} desks: the posts exactly as written, and their numbers. It re-reads the posts it is tracking so that speed can be measured. It writes no words of its own.</p></li>
    <li><h3>Each post is checked.</h3><p>A post's id carries the moment it was created, so a record whose date does not match its id is rejected. Before a post appears here, X is asked directly whether it exists and whether its author and text match.</p></li>
    <li><h3>Claude writes the news.</h3><p>It reads each post before it is shown, leaves out what should not be shown, and writes the sentence above it. For the larger things it reads the reporting and writes a story: what happened, why it is spreading, how each world is seeing it, and what is on the record. It supplies no numbers.</p></li>
    <li><h3>The record sets the front page.</h3><p>Each morning the day before becomes an edition. Its stories are ranked by the views their posts gained that day, so the lead is what the most people saw, and nobody chooses the order.</p></li>
    <li><h3>Soochiebot writes the Newsletter.</h3><p>One letter a day on the day before, from that edition and nothing else, labelled as a program's and set apart from the news. Every number in it is one of the record's, cited in the Harvard style to the story or post it came from.</p></li>
  </ol>
  <h2>How to read it</h2>
  <dl class="glossary">
    <div><dt>The Paper and the Newsletter</dt><dd>Two ways to read the same record, switched under the nameplate, with Internet Pulse between them. The Paper is the day as a front page, ranked by the numbers. The Newsletter is Soochiebot's letter on the same day: what moved, what it means, and one call at the end, with its references.</dd></div>
    <div><dt>Views on the day</dt><dd>What a post gained between midnight and midnight, Eastern: its last reading that day less its last reading the day before. A story's reach is the sum over its posts. A story that began earlier counts only what it gained that day, so a story that moves again rises again.</dd></div>
    <div><dt>Big on X, not yet a story</dt><dd>Posts in the news sections that drew more views than most stories and that no story covers yet. The gaps in the reporting are printed, not hidden.</dd></div>
    <div><dt>What the internet watched</dt><dd>The largest posts outside the news sections that no story covers: what people were passing around.</dd></div>
    <div><dt>Internet Pulse</dt><dd>The record's live instrument: single posts from every desk, refreshed each hour. The largest leads, and the larger a post is, the larger it is set. No account holds more than ${inWords(PULSE_PER_ACCOUNT)} ${PULSE_PER_ACCOUNT === 1 ? 'place' : 'places'}, however many of its posts are large: this is every corner of the internet, not the loudest one.</dd></div>
    <div><dt>Magnitude</dt><dd>The base ten log of views. 6.0 is a million views, 7.0 is ten million, 8.0 is a hundred million. Each whole step is ten times larger.</dd></div>
    <div><dt>Sections and desks</dt><dd>Six sections, from News to Life online, made of ${DESK_COUNT} desks. Each desk card has a bar for each of the last 24 hours: the views gained in that hour, on a log scale from a thousand to ten million.</dd></div>
    <div><dt>Worlds</dt><dd>When groups of people are describing the same story differently, each description is set out beside the post that carries it, followed by what is on the record.</dd></div>
    <div><dt>Standing</dt><dd>Established, developing, disputed, false or satire: the editor's reading of the story as a whole, with sources on its page.</dd></div>
    <div><dt>Quiet</dt><dd>Nothing on that desk cleared its floor. Quiet desks are shown, not filled.</dd></div>
  </dl>
  <h2>What is left out</h2>
  <p>Posts that show people who are not public figures, anything involving minors, pornography and gore, and private information of any kind. When one of these is at the centre of something large, the story is told without it.</p>
</section>`;
  return page({ title: `About · ${SITE.name}`, description: 'Why this paper exists and how it is made: Grok reads X, Claude writes the news, the record sets the front page, Soochiebot writes the Newsletter.', path: '/about/', body, current: '/about/' });
}

// ---------- write

rmSync(OUT, { recursive: true, force: true });
const put = (rel, text) => { const p = join(OUT, rel); mkdirSync(dirname(p), { recursive: true }); writeFileSync(p, text); };
put('index.html', frontEd ? editionPage(frontEd, { front: true }) : page({ title: `${SITE.name}: ${SITE.line}`, description: SITE.line, path: '/', body: empty('The first edition is being read.', 'The record has no day yet.'), current: '/', front: true }));
for (const ed of editions) { put(`edition/${ed.edition.day}/index.html`, editionPage(ed)); put(`data/edition/${ed.edition.day}.json`, JSON.stringify({ ...ed, partial: undefined }, null, 1) + '\n'); }
put('pulse/index.html', pulsePage());
put('desks/index.html', desksPage());
put('stories/index.html', storiesPage());
put('newsletter/index.html', newsletterPage());
for (const ed of letters) put(`newsletter/${ed.edition.day}/index.html`, letterPage(ed));
put('about/index.html', aboutPage());
put('archive/index.html', archivePage());
for (const g of DESKS.groups) put(`section/${g.id}/index.html`, sectionPage(g));
for (const d of desks) put(`desk/${d.id}/index.html`, deskPage(d));
for (const s of stories) put(`story/${s.id}/index.html`, storyPage(s));
put('404.html', page({ title: `Not found · ${SITE.name}`, description: 'No such page.', path: '/404', body: head({ label: '404', title: 'Nothing recorded here.', dek: '<a href="/">Back to the front page.</a>' }) }));
for (const f of ['styles.css', 'app.js', 'favicon.svg']) cpSync(join(REPO, 'site', f), join(OUT, f));
// Cloudflare adds its analytics beacon to every page on this zone; it is allowed by name. It also
// adds an inline bot-check script, which stays blocked: no inline script runs here, Cloudflare's included.
const CSP = "default-src 'none'; script-src 'self' https://static.cloudflareinsights.com; style-src 'self' https://fonts.googleapis.com; style-src-attr 'unsafe-inline'; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' https://cloudflareinsights.com; base-uri 'none'; form-action 'none'; frame-ancestors 'none'";
put('_headers', `/*\n  Content-Security-Policy: ${CSP}\n  Strict-Transport-Security: max-age=31536000\n  X-Content-Type-Options: nosniff\n  X-Frame-Options: DENY\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  X-Robots-Tag: noindex\n`);
put('robots.txt', 'User-agent: *\nDisallow: /\n');
put('data/pulse.json', JSON.stringify({ as_of: new Date(NOW).toISOString(), demo: DEMO, desks: desks.map((d) => ({ id: d.id, code: d.code, posts: d.posts, views: d.views, magnitude: d.mag })), pulse: pulse.map((it) => ({ id: it.id, url: it.post.url, desk: it.deskInfo?.id ?? null, line: it.line, views: it.n.views, magnitude: it.n.magnitude, views_per_hour: it.pace })), stories: live.map((s) => ({ id: s.id, title: s.title, desks: s.desks, standing: s.standing, ...s.n })) }, null, 1));
if (DEMO) put('DEMO', 'Built from invented data. Never deploy this folder.\n');
if (held.length) {
  const by = new Map();
  for (const it of held) by.set(it.post.author.handle.toLowerCase(), (by.get(it.post.author.handle.toLowerCase()) ?? 0) + 1);
  console.log(`pulse: held back ${held.length} ${held.length === 1 ? 'post' : 'posts'} over ${inWords(PULSE_PER_ACCOUNT)} to an account (${[...by].map(([h, n]) => `${h} ${n}`).join(', ')})`);
}
if (unshown) console.warn(`warning: ${unshown} ${unshown === 1 ? 'post' : 'posts'} not shown because X has not confirmed ${unshown === 1 ? 'it' : 'them'} (listed above); the rest of the site is built`);
console.log(`built ${DEMO ? 'DEMO ' : ''}site: ${pulse.length} on the pulse, ${stories.length} stories (${live.length} current), ${desks.filter((d) => d.posts).length}/${desks.length} desks active, ${records.size} posts, as of ${new Date(NOW).toISOString()}`);
console.log(`built paper: ${editions.length} editions, front page ${frontEd ? `${frontEd.edition.day}${frontEd.partial ? ' (so far)' : ''}, lead ${frontEd.stories[0]?.id ?? 'none'}` : 'none'}, ${letters.length} with a letter`);
