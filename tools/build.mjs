#!/usr/bin/env node
// Builds the site into dist/.
//
//   node tools/build.mjs            from this repository's capture/ and moments/
//   node tools/build.mjs --demo     from fixtures/demo (invented data, marked on every page)
//
// Words come from moments/ (the editor). Numbers come from capture/ (the grabber). The build
// only joins them: it never writes a sentence about a story and never makes up a figure.
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { deskTrace, magnitude, placesPerAccount, seriesByPost, storyNumbers } from './lib/metrics.mjs';
import { ZONE_LABEL, clockTime, dateOf, dayOf } from './lib/clock.mjs';

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

function walk(dir, test, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, test, out);
    else if (test(name)) out.push(p);
  }
  return out;
}

// ---------- load

const captures = walk(join(DATA, 'capture'), (n) => /^\d{4}Z\.json$/.test(n)).map(readJSON);
const moments = walk(join(DATA, 'moments'), (n) => n.endsWith('.json')).map(readJSON);
const records = new Map();
for (const c of captures) for (const p of c.posts ?? []) records.set(p.id, p);
const series = seriesByPost(captures);
const NOW = captures.length ? Math.max(...captures.map((c) => Date.parse(c.run.finished_at))) : Date.now();
const FROM = NOW - 24 * HOUR;

// Gate 2's ledger: what X answered about each captured post.
const LEDGER = !DEMO && existsSync(join(REPO, 'verified', 'posts.json')) ? readJSON(join(REPO, 'verified', 'posts.json')) : {};

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

function resolvePost(ref) {
  const rec = records.get(ref.id);
  if (!rec) throw new Error(`story cites post ${ref.id}, which no capture has recorded`);
  // A real build refuses a story citing a post X has not confirmed.
  if (!DEMO && LEDGER[ref.id]?.result !== 'ok') throw new Error(`story cites post ${ref.id}, which X has not confirmed; run node tools/verify-posts.mjs --moments`);
  const list = series.get(ref.id) ?? [];
  const live = [...list].reverse().find((o) => Number.isFinite(o.views)) ?? list[list.length - 1] ?? null;
  return { ...rec, role: ref.role, now: live, readings: list, created: Date.parse(rec.created_at) };
}

const stories = moments.map((m) => {
  const posts = m.posts.map(resolvePost);
  const n = storyNumbers(posts.map((p) => p.id), series, NOW);
  const byId = new Map(posts.map((p) => [p.id, p]));
  return {
    ...m, posts, n,
    started: Date.parse(m.started_at),
    origin: posts.find((p) => p.role === 'origin') ?? posts[0],
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

function pulsePost(id, what) {
  const rec = records.get(id);
  if (!rec) throw new Error(`pulse ${what} ${id} is not in any capture`);
  const bad = (rec.flags ?? []).filter((f) => NEVER_SHOWN.includes(f));
  // A hard stop in code: whatever the editor wrote, a flagged post is never rendered.
  if (bad.length) throw new Error(`pulse ${what} ${id} is flagged ${bad.join(', ')} by the grabber and cannot be shown`);
  if (!DEMO && LEDGER[id]?.result !== 'ok') throw new Error(`pulse ${what} ${id} has not been confirmed by X; run node tools/verify-posts.mjs --captures`);
  return resolvePost({ id, role: null });
}

const passed = (PULSE.items ?? []).map((it) => {
  const post = pulsePost(it.id, 'item');
  const n = storyNumbers([it.id], series, NOW);
  const ageH = Math.max((NOW - post.created) / HOUR, 0.05);
  return {
    ...it, post, n, ageH,
    pace: n.perHour ?? (n.views != null ? Math.round(n.views / ageH) : null), measured: n.perHour != null,
    also: (it.also ?? []).map((id) => pulsePost(id, 'related post')),
    story: storyOf.get(it.id) ?? null,
    deskInfo: deskById.get(it.desk) ?? deskById.get(post.desk),
  };
}).filter((it) => it.n.views != null).sort((a, b) => b.n.views - a.n.views);

// The pulse is every corner of the internet, so no one account may fill it. Of the posts the
// editor passed, an account keeps its largest; the build says which others it held back.
const { kept: pulse, held } = placesPerAccount(passed, PULSE_PER_ACCOUNT, (it) => it.post.author.handle);

// ---------- the desks: 24 hourly figures per desk, from every post the grabber labelled with that desk

// Bar height is views gained per hour on a log scale: 1,000 an hour is the floor, 10 million is full.
const level = (perHour) => Math.max(0, Math.min(1, (Math.log10(Math.max(perHour, 1)) - 3) / 4));

// Only posts X has confirmed feed a trace or a total. A post Gate 2 could not confirm counts for nothing.
const confirmed = (id) => DEMO || LEDGER[id]?.result === 'ok';

const desks = DESKS.desks.map((d) => {
  const own = [...records.values()].filter((p) => p.desk === d.id && confirmed(p.id)).map((p) => ({ id: p.id, created: Date.parse(p.created_at) }));
  const bins = deskTrace(own, series, { from: FROM, to: NOW, bins: BINS });
  const mine = live.filter((s) => s.home?.id === d.id);
  // The desk's figure for the day counts posts written in the last 24 hours. An old post that a
  // reference led back to still feeds the trace by what it gained, but not the day's total.
  const fresh = own.filter((p) => p.created >= FROM);
  const total = fresh.reduce((sum, p) => { const l = (series.get(p.id) ?? []).filter((o) => Number.isFinite(o.views)).pop(); return sum + (l ? l.views : 0); }, 0);
  return { ...d, pulse: pulse.filter((it) => it.deskInfo?.id === d.id), bins, posts: fresh.length, views: total, mag: magnitude(total), stories: mine, also: live.filter((s) => s.home?.id !== d.id && s.desks.includes(d.id)), past: past.filter((s) => s.desks.includes(d.id)) };
});


// ---------- components
//
// Edition 2. One family, one ink, one flag colour, and size carries magnitude: the largest post
// leads the page, the next three are set large, six more a step down, and the rest take a line
// each. The tiers are positions in one list, decided by the stylesheet, so re-ordering the list
// re-tiers it and the page script never has to redraw an item.

const deskLink = (d) => (d ? `<a class="desk" href="/desk/${d.id}/">${esc(d.name)}</a>` : '');
const groupName = (d) => DESKS.groups.find((g) => g.id === d.group)?.name ?? '';
const xLink = (p, text, cls) => `<a${cls ? ` class="${cls}"` : ''} href="${esc(p.url)}" rel="noopener noreferrer" target="_blank">${text}</a>`;
const clock = (p) => `<time datetime="${esc(p.created_at)}">${hhmm(p.created)} ${ZONE_LABEL}</time>`;
const who = (p) => `<b>${esc(fromX(p.author.name))}</b>`;
const quoted = (p) => `“${postText(p)}”`;
const numeral = (m, cls = 'num') => `<span class="${cls}"><span class="vh">Magnitude </span>${mag(m)}</span>`;
const standingTag = (s) => `<span class="stand stand-${esc(s.standing)}">${STANDING[s.standing] ?? esc(s.standing)}</span>`;
const OUTSIDE = 'Outside your worlds';
const ageOf = (h) => (h < 1 ? `${Math.round(h * 60)} min` : h < 48 ? `${Math.round(h)} h` : `${Math.round(h / 24)} days`);
const counts = (o, keys) => (o ? keys.filter((k) => o[k] != null).map((k) => `<span>${num(o[k])} ${k}</span>`).join('') : '');

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

// The largest post on the pulse, on its own at the head of the page.
function leadBlock(it) {
  const d = it.deskInfo, p = it.post;
  const facts = [['Views', num(it.n.views)]];
  if (it.pace != null) facts.push([it.measured ? 'Views an hour' : 'Views an hour, average', num(it.pace)]);
  facts.push(['Age', ageOf(it.ageH)]);
  return `<section class="lead" id="p-${esc(it.id)}" aria-label="The largest post right now" data-views="${it.n.views}" data-desks="${esc(d?.id ?? '')}">
  <div class="lead-fig">
    <p class="lead-top"><span class="lab">The largest post right now</span><span class="lead-desk"><span class="out">${OUTSIDE}</span>${deskLink(d)}</span></p>
    <p>${numeral(it.n.magnitude, 'big')}</p>
    <dl class="facts"><div><dt class="lab">Magnitude</dt><dd class="facts-note">base ten log of views</dd></div>${facts.map(([k, v]) => `<div><dt class="lab">${k}</dt><dd>${v}</dd></div>`).join('')}</dl>
  </div>
  <div class="lead-body">
    <p class="lead-line">${esc(it.line)}</p>
    <blockquote class="lead-q">${quoted(p)}</blockquote>
    <p class="by">${who(p)}<span>@${esc(p.author.handle)} · ${clock(p)}</span>${counts(p.now, ['likes', 'reposts', 'replies'])}${storyLink(it)}${xLink(p, 'Open on X', 'open')}</p>
    ${it.also.length ? `<div class="rel">${it.also.map((x) => relatedPost(p, x)).join('')}</div>` : ''}
  </div>
</section>`;
}

// One item of the pulse list. It carries everything any tier shows; the stylesheet decides, by the
// item's place in the list, how much of it is set and how large.
function pulseItem(it) {
  const d = it.deskInfo, p = it.post;
  const pace = it.pace == null ? '' : `<span class="meta-pace"> · ${it.measured ? 'gaining' : 'averaging'} ${num(it.pace)} an hour</span>`;
  const more = it.also.length ? `<details class="more"><summary>+${it.also.length} related ${it.also.length === 1 ? 'post' : 'posts'}</summary><div class="more-list">${it.also.map((x) => relatedPost(p, x)).join('')}</div></details>` : '';
  return `<li class="it" id="p-${esc(it.id)}" data-views="${it.n.views}" data-pace="${Math.round(it.pace ?? 0)}" data-start="${p.created}" data-desks="${esc(d?.id ?? '')}">
  <div class="hd">
    ${numeral(it.n.magnitude)}
    <div class="hd-side">
      <p class="hd-row">${deskLink(d)}<span class="out out-hd">${OUTSIDE}</span></p>
      <p class="meta">${num(it.n.views)} views${pace}<span class="meta-age"> · ${ageOf(it.ageH)}<span class="meta-old"> old</span></span></p>
    </div>
  </div>
  <p class="line">${esc(it.line)}</p>
  <blockquote class="q">${quoted(p)}</blockquote>
  <div class="by">${xLink(p, `${who(p)} <span>@${esc(p.author.handle)}<span class="when"> · ${clock(p)}</span></span>`, 'who')}${more}${storyLink(it)}<span class="out out-by">${OUTSIDE}</span>${xLink(p, 'Open on X', 'open')}</div>
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

// On the front page a card is a switch (this is one of my worlds); on the desks page it is a link.
function deskCard(d, { link = false } = {}) {
  const quiet = d.posts === 0;
  const inner = `<span class="dk-top"><span class="dk-name">${esc(d.name)}</span><span class="dk-mag${quiet ? ' is-quiet' : ''}">${quiet ? 'quiet' : mag(d.mag)}</span></span>
  <span class="dk-bars" aria-hidden="true">${bars(d)}</span>
  <span class="dk-meta"><span>${d.code} · ${esc(groupName(d))}</span><span>${quiet ? 'no posts' : `${num(d.views)} views`}</span></span>`;
  if (!link) return `<button type="button" class="dk" data-desk="${d.id}" aria-pressed="false">${inner}</button>`;
  const top = d.pulse[0]?.line ?? d.stories[0]?.title ?? d.scope.split(':')[0];
  return `<a class="dk" href="/desk/${d.id}/">${inner}<span class="dk-line">${esc(top)}</span></a>`;
}

function spark(s, w = 200, h = 44) {
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
  <div class="worlds-grid">${s.worlds.map((w) => `<div class="world"><h4>${esc(w.name)}</h4><p>${esc(w.sees)}</p>${w.post ? postFigure(w.post, { compact: true }) : ''}</div>`).join('')}</div>
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
    ${postFigure(s.origin)}
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
  return `<li><a class="st" href="/story/${esc(s.id)}/"><span class="st-mag">${mag(s.n.magnitude)}</span><span class="st-title">${esc(s.title)}${dek ? `<span class="st-dek">${esc(s.dek)}</span>` : ''}</span><span class="st-side"><span class="lab">${where}</span>${standingTag(s)}</span></a></li>`;
}

// ---------- page shell

const FONTS = 'https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:ital,wght@0,400..900;1,400..900&display=swap';

function page({ title, description, path, body, current, front = '' }) {
  const nav = [['/', 'Pulse'], ['/stories/', 'Stories'], ['/desks/', 'Desks'], ['/archive/', 'Archive'], ['/about/', 'About']].map(([href, label]) => `<a href="${href}"${current === href ? ' aria-current="page"' : ''}>${label}</a>`).join('');
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
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="${FONTS}" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script src="/app.js" defer></script>
</head>
<body${front ? ' class="front"' : ''}>
<a class="skip" href="#main">Skip to the record</a>
${DEMO ? '<p class="demo">Design test. Every story and post below is invented. Only the pinned post is real.</p>' : ''}
<div class="wrap">
<header class="top">
  <div class="top-row">
    <p class="lab asof">As of <time id="asof" datetime="${new Date(NOW).toISOString()}">${hhmm(NOW)} ${ZONE_LABEL} · ${day(NOW)}</time></p>
    <nav aria-label="Sections">${nav}</nav>
  </div>
  <p class="mast-row"><a class="mast" href="/">Monitoring <span class="the">the</span> Situation</a></p>
  ${front}
</header>
<p class="stale" id="stale" role="status" hidden></p>
<main id="main">
${body}
</main>
<footer class="foot">
  <div class="foot-method"><p class="lab">How this is made</p>${SITE.method.map((m) => `<p>${esc(m)}</p>`).join('')}</div>
  <p class="foot-links"><a href="/about/">How this is made</a><a href="https://seansooch.dev/">seansooch.dev</a></p>
</footer>
</div>
</body>
</html>
`;
}

const pinDate = (p) => `<time datetime="${esc(p.created_at)}">${dateOf(Date.parse(p.created_at))}</time>`;

// The front page carries the site's line and the pinned post as one strip under the nameplate.
function pinStrip() {
  const p = SITE.pinned;
  return `<div class="tagline">
    <h1 class="tag">${esc(SITE.line)}</h1>
    <p class="pin"><span class="lab">Pinned</span><span class="pin-q">“${esc(p.text)}”</span><span class="pin-by">${esc(p.name)}, ${pinDate(p)}</span><a href="/about/">Why this site exists</a></p>
  </div>`;
}

// The about page gives the pinned post in full, and the purpose it set.
function pinFull() {
  const p = SITE.pinned;
  return `<section class="page-head pin-full">
  <div class="page-head-main">
    <p class="lab">Pinned</p>
    <blockquote class="pin-big">“${esc(p.text)}”</blockquote>
    <p class="by"><b>${esc(p.name)}</b><span>@${esc(p.handle)} · ${pinDate(p)}</span><a class="open" href="${esc(p.url)}" rel="noopener noreferrer" target="_blank">Open on X</a></p>
    ${p.quotes ? `<p class="pin-quoted">Quoting @${esc(p.quotes.handle)}: “${esc(p.quotes.text)}”</p>` : ''}
  </div>
</section>`;
}

const pageHead = ({ label, title, dek, extra = '', fig = '' }) => `<section class="page-head">
  <div class="page-head-main"><p class="lab">${label}</p><h1>${title}</h1>${dek ? `<p class="dek">${dek}</p>` : ''}${extra}</div>${fig}
</section>`;
const empty = (title, text = '') => `<div class="empty"><h3>${title}</h3>${text ? `<p>${text}</p>` : ''}</div>`;
const sortBar = (keys) => `<div class="sort" role="group" aria-label="Order">${keys.map(([key, label], i) => `<button type="button" data-sort="${key}" aria-pressed="${i ? 'false' : 'true'}">${label}</button>`).join('')}</div>`;

// ---------- pages

function pulsePage() {
  const active = desks.filter((d) => d.posts > 0).length;
  const [lead, ...rest] = pulse;
  const early = captures.length < 4 ? ` <strong>Early days: ${captures.length === 1 ? 'one reading' : captures.length + ' readings'} so far, so each desk's bars show only when its posts began. They sharpen with every hourly reading.</strong>` : '';
  const shown = live.slice(0, 8);
  const body = `${lead ? leadBlock(lead) : ''}
<section class="desks-sec" id="desks" aria-labelledby="desks-h">
  <header class="sec-head"><h2 id="desks-h">Which worlds do you live in?</h2>
    <p>The last 24 hours on all ${desks.length} desks. Each bar is one hour of views gained. Select the desks you already follow, and the page marks what you are not seeing.${early}</p>
    <div class="sec-tools" id="mine-tools" hidden><span class="lab" id="mine-count">None selected</span><button type="button" class="btn" id="mine-clear">Clear</button></div>
  </header>
  <div class="dk-grid" role="group" aria-label="Desks you follow">${desks.map((d) => deskCard(d)).join('')}</div>
</section>
${lead && !rest.length ? '' : `<section class="pulse-sec" id="pulse" aria-labelledby="pulse-h">
  <header class="sec-head"><h2 id="pulse-h">Internet Pulse</h2>
    <p>The posts the internet is passing around right now, from every desk. The number is magnitude: 6.0 is a million views, 7.0 is ten million. The sentence above each post is ours and says what it is, not whether it is right.</p>
    ${rest.length ? sortBar([['views', 'Largest'], ['pace', 'Fastest'], ['start', 'Newest']]) : ''}
  </header>
  ${rest.length ? pulseList(rest, 'pulse-list') : empty('The first pulse is being read.', `The instrument is recording on ${active} of ${desks.length} desks. Posts appear here once each has been confirmed with X and passed by the editor.`)}
</section>`}
<section class="stories-sec" id="stories" aria-labelledby="stories-h">
  <header class="sec-head"><h2 id="stories-h">Researched stories</h2><p>Slower and deeper: what happened, how each world is describing it, and what is on the record, with sources.</p></header>
  ${shown.length ? `<ul class="st-list">${shown.map((s) => storyLine(s)).join('')}</ul>${live.length > shown.length ? `<p class="note"><a href="/stories/">All ${live.length} current stories</a></p>` : ''}` : empty('No stories written up yet.')}
</section>`;
  return page({ title: `${SITE.name}: ${SITE.line}`, description: `What every corner of the internet is passing around, on one record: ${DESK_COUNT} desks, measured hourly, with what each world is seeing and what is established.`, path: '/', body, current: '/', front: pinStrip() });
}

function storiesPage() {
  const body = `${pageHead({ label: `${live.length} current`, title: 'Researched stories', dek: 'For the things worth more than a line: what happened, why it is spreading, how each world is describing it, and what is on the record. Each claim has a source, and each post was confirmed with X.' })}
<section class="bulletin" id="bulletin">
  <header class="sec-head"><h2>The last 48 hours</h2>
    ${sortBar([['mag', 'Largest'], ['rate', 'Fastest'], ['start', 'Newest']])}
  </header>
  ${live.length ? `<ol class="stories">${live.map(storyRow).join('')}</ol>` : empty('The first stories are being written.')}
  ${past.length ? `<p class="note"><a href="/archive/">${past.length} earlier ${past.length === 1 ? 'story' : 'stories'} in the archive</a></p>` : ''}
</section>`;
  return page({ title: `Stories · ${SITE.name}`, description: 'Researched write-ups of what the internet is passing around: what happened, how each world sees it, and what is established.', path: '/stories/', body, current: '/stories/' });
}

function storyPage(s) {
  const body = `<article class="full" data-desks="${esc(s.desks.join(' '))}">
  <header class="full-head">
    ${storyMeta(s)}
    <h1>${esc(s.title)}</h1>
    <p class="dek">${esc(s.dek)}</p>
  </header>
  <div class="full-grid">
    <div class="full-main">
      <h2>What happened</h2>${s.what.map((t) => `<p>${esc(t)}</p>`).join('')}
      <h2>Why it is spreading</h2><p>${esc(s.why)}</p>
      ${worldsBlock(s, true)}
      ${s.next ? `<h2>What to watch</h2><p>${esc(s.next)}</p>` : ''}
      <h2>The posts</h2>${s.posts.map((p) => postFigure(p)).join('')}
      ${(s.corrections ?? []).length ? `<h2>Corrections</h2><ul class="sources">${s.corrections.map((c) => `<li><time datetime="${esc(c.at)}">${hhmm(Date.parse(c.at))} ${ZONE_LABEL}, ${day(Date.parse(c.at))}</time> ${esc(c.text)}</li>`).join('')}</ul>` : ''}
      ${(s.sources ?? []).length ? `<h2>Sources</h2><ul class="sources">${s.sources.map((x) => `<li><a href="${esc(x.url)}" rel="noopener noreferrer" target="_blank">${esc(x.label)}</a></li>`).join('')}</ul>` : ''}
    </div>
    <aside class="full-side">
      <p class="updated">Written up ${hhmm(Date.parse(s.updated_at))} ${ZONE_LABEL}, ${day(Date.parse(s.updated_at))}</p>
      ${magBlock(s)}
      ${spark(s, 280, 80)}
      <dl class="facts"><div><dt class="lab">Views</dt><dd>${num(s.n.views)}</dd></div><div><dt class="lab">Last hour</dt><dd>${s.n.perHour == null ? 'n/a' : num(s.n.perHour)}</dd></div><div><dt class="lab">Posts tracked</dt><dd>${s.posts.length}</dd></div><div><dt class="lab">Began</dt><dd>${hhmm(s.started)} ${ZONE_LABEL}</dd></div></dl>
    </aside>
  </div>
</article>`;
  return page({ title: `${s.title} · ${SITE.name}`, description: s.dek, path: `/story/${s.id}/`, body });
}

function deskPage(d) {
  const all = [...d.stories, ...d.also];
  const fig = `<div class="page-fig"><p>${d.posts ? numeral(d.mag, 'big') : '<span class="big is-quiet">quiet</span>'}</p><p class="lab">${d.posts ? 'magnitude, last 24 hours' : 'nothing cleared the floor'}</p></div>`;
  const body = `${pageHead({ label: `${esc(groupName(d))} · ${d.code}`, title: esc(d.name), dek: esc(d.scope), extra: `<p class="beats">${d.beats.map((b) => `<span>${esc(b)}</span>`).join('')}</p>`, fig })}
<section class="day">
  <div class="dk-bars dk-bars-wide" role="img" aria-label="Views gained on this desk in each of the last 24 hours">${bars(d, 96)}</div>
  <p class="axis" aria-hidden="true"><span>24 h ago</span><span>18 h</span><span>12 h</span><span>6 h</span><span>now</span></p>
  <p class="note">${d.posts ? `${d.posts} posts written in the last 24 hours are on record for this desk, with ${num(d.views)} views between them. Each bar is one hour of views gained.` : 'Nothing on this desk cleared its floor in the last 24 hours.'}</p>
</section>
<section class="pulse-sec">
  <header class="sec-head"><h2>On this desk now</h2></header>
  ${d.pulse.length ? pulseList(d.pulse) : empty('Nothing from this desk is on the pulse right now.', 'A quiet desk is reported as quiet. Nothing is added to fill it.')}
</section>
<section class="bulletin">
  <header class="sec-head"><h2>Researched stories on this desk</h2></header>
  ${all.length ? `<ol class="stories">${all.map(storyRow).join('')}</ol>` : `<p class="note">None in the last 48 hours.</p>`}
  ${d.past.length ? `<p class="note"><a href="/archive/">${d.past.length} earlier ${d.past.length === 1 ? 'story' : 'stories'} on this desk in the archive</a></p>` : ''}
</section>`;
  return page({ title: `${d.name} · ${SITE.name}`, description: d.scope, path: `/desk/${d.id}/`, body, current: '/desks/' });
}

function desksPage() {
  const body = `${pageHead({ label: `${desks.length} desks`, title: 'The desks', dek: `Every part of the internet's attention this site watches. Each is swept on a schedule, and a quiet desk is reported as quiet.` })}
${DESKS.groups.map((g) => `<section class="group"><h2>${esc(g.name)}</h2><div class="dk-grid">${desks.filter((d) => d.group === g.id).map((d) => deskCard(d, { link: true })).join('')}</div></section>`).join('\n')}`;
  return page({ title: `The desks · ${SITE.name}`, description: `The ${DESK_COUNT} desks this site watches, in ${inWords(DESKS.groups.length)} groups.`, path: '/desks/', body, current: '/desks/' });
}

function archivePage() {
  const days = new Map();
  for (const s of past) { const k = dateOf(s.started); if (!days.has(k)) days.set(k, []); days.get(k).push(s); }
  const list = [...days.values()].map((list) => `<section class="group"><h2>${day(list[0].started)}</h2><ul class="st-list">${list.sort((a, b) => (b.n.magnitude ?? 0) - (a.n.magnitude ?? 0)).map((s) => storyLine(s, { dek: true })).join('')}</ul></section>`).join('\n');
  const body = `${pageHead({ label: `${past.length} ${past.length === 1 ? 'story' : 'stories'}`, title: 'The archive', dek: 'A story leaves the bulletin 48 hours after it began and is kept here, as it was last written up, with the numbers its posts had reached.' })}
${list || empty('Nothing here yet.', 'The record began on 9 October 2026. Stories arrive here two days after they start.')}`;
  return page({ title: `Archive · ${SITE.name}`, description: 'Stories that have left the bulletin, by day.', path: '/archive/', body, current: '/archive/' });
}

function aboutPage() {
  const body = `${pinFull()}
<section class="about">
  <h1>${esc(SITE.line)}</h1>
  ${SITE.purpose.map((t) => `<p>${esc(t)}</p>`).join('')}
  <h2>How it is made</h2>
  <ol class="steps">
    <li><h3>Grok reads X.</h3><p>Every hour it records what is spreading on each of ${DESK_COUNT} desks: the posts exactly as written, and their numbers. It re-reads the posts it is tracking so that speed can be measured. It writes no words of its own.</p></li>
    <li><h3>Each post is checked.</h3><p>A post's id carries the moment it was created, so a record whose date does not match its id is rejected. Before a post appears here, X is asked directly whether it exists and whether its author and text match.</p></li>
    <li><h3>Claude writes.</h3><p>It reads each post before it is shown, leaves out what should not be shown, and writes the sentence above it. For the larger things it reads the reporting and writes a story: what happened, why it is spreading, how each world is seeing it, and what is on the record. It supplies no numbers.</p></li>
  </ol>
  <h2>How to read it</h2>
  <dl class="glossary">
    <div><dt>Internet Pulse</dt><dd>The front of the site: single posts from every desk, refreshed each hour. The largest leads the page, and the larger a post is, the larger it is set. No account holds more than ${inWords(PULSE_PER_ACCOUNT)} ${PULSE_PER_ACCOUNT === 1 ? 'place' : 'places'}, however many of its posts are large: this is every corner of the internet, not the loudest one. The sentence above a post is the editor's and says what the post is, not whether it is right.</dd></div>
    <div><dt>Stories</dt><dd>Slower and deeper. For the things worth more than a line: what happened, why it is spreading, how each world describes it, and what is on the record, with sources.</dd></div>
    <div><dt>Magnitude</dt><dd>The base ten log of views, for one post on the pulse or across a story's tracked posts. 6.0 is a million views, 7.0 is ten million, 8.0 is a hundred million. Each whole step is ten times larger.</dd></div>
    <div><dt>The desks</dt><dd>One card per desk, with a bar for each of the last 24 hours. The height of a bar is the views gained in that hour by the posts recorded on that desk, on a log scale: a thousand an hour is the floor and ten million is full height.</dd></div>
    <div><dt>An hour</dt><dd>How fast a post is being seen. It is measured between two readings of the post when there are two, and says gaining. Until then it is the average since the post was written, and says averaging.</dd></div>
    <div><dt>Worlds</dt><dd>When groups of people are describing the same story differently, each description is set out beside the post that carries it, followed by what is established. Pick the desks you follow on the front page and everything from outside them is marked.</dd></div>
    <div><dt>Standing</dt><dd>Established, developing, disputed, false or satire: the editor's reading of the story as a whole, with sources on its page.</dd></div>
    <div><dt>Quiet</dt><dd>Nothing on that desk cleared its floor. Quiet desks are shown, not filled.</dd></div>
  </dl>
  <h2>What is left out</h2>
  <p>Posts that show people who are not public figures, anything involving minors, pornography and gore, and private information of any kind. When one of these is at the centre of something large, the story is told without it.</p>
</section>`;
  return page({ title: `About · ${SITE.name}`, description: 'Why this site exists and how it is made: Grok reads X, Claude writes, and every post is checked.', path: '/about/', body, current: '/about/' });
}

// ---------- write

rmSync(OUT, { recursive: true, force: true });
const put = (rel, text) => { const p = join(OUT, rel); mkdirSync(dirname(p), { recursive: true }); writeFileSync(p, text); };
put('index.html', pulsePage());
put('desks/index.html', desksPage());
put('stories/index.html', storiesPage());
put('about/index.html', aboutPage());
put('archive/index.html', archivePage());
for (const d of desks) put(`desk/${d.id}/index.html`, deskPage(d));
for (const s of stories) put(`story/${s.id}/index.html`, storyPage(s));
put('404.html', page({ title: `Not found · ${SITE.name}`, description: 'No such page.', path: '/404', body: pageHead({ label: '404', title: 'Nothing recorded here.', dek: '<a href="/">Back to the record.</a>' }) }));
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
console.log(`built ${DEMO ? 'DEMO ' : ''}site: ${pulse.length} on the pulse, ${stories.length} stories (${live.length} current), ${desks.filter((d) => d.posts).length}/${desks.length} desks active, ${records.size} posts, as of ${new Date(NOW).toISOString()}`);
