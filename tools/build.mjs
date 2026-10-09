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
import { deskTrace, magnitude, seriesByPost, storyNumbers } from './lib/metrics.mjs';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..');
const DEMO = process.argv.includes('--demo');
const DATA = DEMO ? join(REPO, 'fixtures', 'demo') : REPO;
const OUT = join(REPO, 'dist');
const HOUR = 3600000;
const BINS = 96; // 15 minutes each over 24 hours

const readJSON = (p) => JSON.parse(readFileSync(p, 'utf8'));
const DESKS = readJSON(join(REPO, 'contract', 'desks.json'));
const SITE = readJSON(join(REPO, 'site.json'));
const deskById = new Map(DESKS.desks.map((d) => [d.id, d]));

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
const hhmm = (ms) => new Date(ms).toISOString().slice(11, 16);
const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
function day(ms) { const d = new Date(ms); return `${DAYS[d.getUTCDay()]} ${d.getUTCDate()} ${MONTHS[d.getUTCMonth()]} ${d.getUTCFullYear()}`; }
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

const pulse = (PULSE.items ?? []).map((it) => {
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

// ---------- the record: one trace per desk, from every post the grabber labelled with that desk

function hash(str) { let h = 2166136261; for (const c of str) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); } return h >>> 0; }

// Trace height is views gained per hour on a log scale: 1,000 an hour is flat, 10 million is full.
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

function tracePath(desk, w = 960, h = 40) {
  let seed = hash(desk.id);
  const rnd = () => { seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed / 4294967296; };
  const per = 5, step = w / (BINS * per), mid = h / 2;
  let d = `M0 ${mid}`;
  for (let i = 0; i < BINS * per; i++) {
    const e = level(desk.bins[Math.floor(i / per)]);
    const swing = e === 0 ? 0 : (i % 2 ? 1 : -1) * (0.35 + rnd() * 0.65) * e * (mid - 2);
    d += `L${((i + 0.5) * step).toFixed(1)} ${(mid + swing).toFixed(1)}`;
  }
  return d + `L${w} ${mid}`;
}

// ---------- components

function chip(id) { const d = deskById.get(id); return d ? `<a class="code" href="/desk/${d.id}/" title="${esc(d.name)}">${d.code}</a>` : ''; }

function mediaLine(p) {
  const m = (p.media ?? [])[0];
  if (!m) return '';
  const kind = { photo: 'Photo', video: 'Video', gif: 'GIF', link: 'Link', poll: 'Poll' }[m.type] ?? 'Media';
  const len = m.duration_s ? `, ${Math.floor(m.duration_s / 60)}:${String(Math.round(m.duration_s % 60)).padStart(2, '0')}` : '';
  const what = m.description ? esc(m.description) : m.link_title ? esc(m.link_title) : '';
  return `<p class="post-media"><span>${kind}${len}</span>${what}</p>`;
}

function postBlock(p, { compact = false } = {}) {
  const o = p.now;
  const nums = o ? [['views', o.views], ['likes', o.likes], ['reposts', o.reposts], ['replies', o.replies]].filter(([, v]) => v != null).map(([k, v]) => `<span><b>${num(v)}</b> ${k}</span>`).join('') : '';
  return `<figure class="post${compact ? ' post-compact' : ''}">
  <figcaption>${p.role && !compact ? `<span class="role">${ROLE[p.role] ?? esc(p.role)}</span>` : ''}<b>${esc(fromX(p.author.name))}</b> <span class="handle">@${esc(p.author.handle)}</span> <time datetime="${esc(p.created_at)}">${hhmm(p.created)} UTC</time></figcaption>
  <blockquote>${postText(p)}</blockquote>
  ${mediaLine(p)}
  <p class="post-nums">${nums}<a href="${esc(p.url)}" rel="noopener noreferrer" target="_blank">Open on X</a></p>
</figure>`;
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
  <div class="worlds-grid">${s.worlds.map((w) => `<div class="world"><h4>${esc(w.name)}</h4><p>${esc(w.sees)}</p>${w.post ? postBlock(w.post, { compact: true }) : ''}</div>`).join('')}</div>
  ${s.common ? `<div class="common"><h4>On the record</h4><p>${esc(s.common)}</p></div>` : ''}
</details>`;
}

function storyMeta(s) {
  return `<p class="story-meta">${s.desks.map(chip).join('')}<span>${esc(s.home?.name ?? '')}</span><span>began ${hhmm(s.started)} UTC, ${ago(s.started)}</span><span class="standing standing-${esc(s.standing)}">${STANDING[s.standing] ?? esc(s.standing)}</span></p>`;
}

function magBlock(s) {
  const big = (s.n.magnitude ?? 0) >= 7;
  const rate = s.n.perHour != null ? `<span class="rate">${num(s.n.perHour)} views/h</span>` : '';
  return `<div class="story-mag"><span class="mag${big ? ' mag-big' : ''}">${mag(s.n.magnitude)}</span><span class="mag-label">magnitude</span><span class="trend trend-${s.n.trend}">${TREND[s.n.trend]}</span>${rate}</div>`;
}

function storyRow(s, i) {
  return `<li class="story" id="s-${esc(s.id)}" data-mag="${s.n.magnitude ?? 0}" data-rate="${s.n.perHour ?? 0}" data-start="${s.started}" data-desks="${esc(s.desks.join(' '))}">
  ${magBlock(s)}
  <div class="story-body">
    ${storyMeta(s)}
    <h3><a href="/story/${esc(s.id)}/">${esc(s.title)}</a></h3>
    <p class="dek">${esc(s.dek)}</p>
    ${postBlock(s.origin)}
    ${worldsBlock(s, i < 4)}
  </div>
  <aside class="story-side">
    ${spark(s)}
    <dl><div><dt>Views</dt><dd>${num(s.n.views)}</dd></div><div><dt>Posts tracked</dt><dd>${s.posts.length}</dd></div></dl>
    <a class="more" href="/story/${esc(s.id)}/">Full story</a>
  </aside>
</li>`;
}

function pulseRow(it) {
  const d = it.deskInfo;
  const big = (it.n.magnitude ?? 0) >= 7;
  const age = it.ageH < 1 ? `${Math.round(it.ageH * 60)} min old` : it.ageH < 48 ? `${Math.round(it.ageH)} h old` : `${Math.round(it.ageH / 24)} days old`;
  const pace = it.pace == null ? '' : `<span>${it.measured ? 'gaining' : 'averaging'} ${num(it.pace)} views/h</span>`;
  return `<li class="pulse-item" id="p-${esc(it.id)}" data-views="${it.n.views}" data-pace="${it.pace ?? 0}" data-start="${it.post.created}" data-desks="${esc(d?.id ?? '')}">
  <div class="pulse-mag"><span class="mag${big ? ' mag-big' : ''}">${mag(it.n.magnitude)}</span></div>
  <div class="pulse-body">
    <p class="story-meta">${d ? chip(d.id) : ''}<span>${esc(d?.name ?? '')}</span><span>${age}</span>${pace}</p>
    <p class="pulse-line">${esc(it.line)}</p>
    ${postBlock(it.post)}
    ${it.also.length ? `<div class="pulse-also">${it.also.map((p) => postBlock(p, { compact: true })).join('')}</div>` : ''}
    ${it.story ? `<p class="pulse-story"><a href="/story/${esc(it.story.id)}/">The researched story: ${esc(it.story.title)}</a></p>` : ''}
  </div>
</li>`;
}

function storyTeaser(s) {
  return `<li><a href="/story/${esc(s.id)}/"><span class="desk-peak">${mag(s.n.magnitude)}</span><b>${esc(s.title)}</b><span class="standing standing-${esc(s.standing)}">${STANDING[s.standing] ?? esc(s.standing)}</span><span class="desk-top">${esc(s.dek)}</span></a></li>`;
}

function recordFigure(list, { labels = true } = {}) {
  const ticks = [];
  const first = Math.ceil(FROM / (3 * HOUR)) * 3 * HOUR;
  for (let t = first; t < NOW - 1.2 * HOUR; t += 3 * HOUR) ticks.push(`<span style="left:${(((t - FROM) / (NOW - FROM)) * 100).toFixed(2)}%">${hhmm(t)}</span>`);
  const row = (d) => {
    const marks = d.stories.filter((s) => s.n.magnitude != null).slice(0, 4).map((s) => {
      const x = Math.max(0, Math.min(100, ((s.started - FROM) / (NOW - FROM)) * 100));
      return `<a class="mark${(s.n.magnitude ?? 0) >= 7 ? ' mark-big' : ''}${x > 90 ? ' mark-flip' : ''}" style="left:${x.toFixed(2)}%" href="/story/${esc(s.id)}/" title="${esc(s.title)}"><span>${mag(s.n.magnitude)}</span></a>`;
    }).join('');
    const quiet = d.posts === 0;
    return `<div class="rec-row${quiet ? ' rec-quiet' : ''}" data-desk="${d.id}">
    <a class="rec-name" href="/desk/${d.id}/"><span class="code">${d.code}</span><span class="rec-full">${esc(d.name)}</span></a>
    <div class="rec-trace"><svg viewBox="0 0 960 40" preserveAspectRatio="none" aria-hidden="true"><path d="${tracePath(d)}"/></svg>${marks}</div>
    <span class="rec-peak">${quiet ? 'quiet' : mag(d.mag)}</span>
  </div>`;
  };
  const groups = DESKS.groups.map((g) => {
    const rows = list.filter((d) => d.group === g.id);
    if (!rows.length) return '';
    return `<div class="rec-group">${labels ? `<p class="rec-group-name">${esc(g.name)}</p>` : ''}${rows.map(row).join('')}</div>`;
  }).join('');
  const off = (((first - FROM) / (NOW - FROM)) * 100).toFixed(2);
  return `<div class="rec" style="--off:${off}%" role="group" aria-label="Activity on each desk over the last 24 hours">
  <div class="rec-axis"><span class="rec-name"></span><div class="rec-ticks">${ticks.join('')}<span class="rec-now" style="left:100%">now</span></div><span class="rec-peak">24 h</span></div>
  ${groups}
</div>`;
}

// ---------- page shell

const FONTS = 'https://fonts.googleapis.com/css2?family=B612:wght@400;700&family=Libre+Franklin:ital,wght@0,400;0,600;0,800;0,900;1,400&family=STIX+Two+Text:ital,wght@0,400;0,600;1,400&display=swap';

function page({ title, description, path, body, current }) {
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
<meta name="theme-color" content="#e8edf2">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="${FONTS}" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script src="/app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to the record</a>
${DEMO ? '<p class="demo">Design test. Every story and post below is invented. Only the pinned post is real.</p>' : ''}
<header class="bar">
  <a class="brand" href="/">Monitoring <span>the</span> Situation</a>
  <nav aria-label="Sections">${nav}</nav>
  <p class="asof">As of <time id="asof" datetime="${new Date(NOW).toISOString()}">${hhmm(NOW)} UTC, ${day(NOW)}</time></p>
</header>
<p class="stale" id="stale" role="status" hidden></p>
<main id="main">
${body}
</main>
<footer class="foot">
  <div class="foot-method">${SITE.method.map((m) => `<p>${esc(m)}</p>`).join('')}</div>
  <p class="foot-links"><a href="/about/">How this is made</a><a href="https://seansooch.dev/">seansooch.dev</a></p>
</footer>
</body>
</html>
`;
}

function pinned() {
  const p = SITE.pinned;
  const d = new Date(p.created_at);
  return `<section class="pin" aria-labelledby="pin-h">
  <figure class="pin-post">
    <figcaption class="label">Pinned</figcaption>
    <blockquote><p>${esc(p.text)}</p></blockquote>
    <p class="pin-by"><b>${esc(p.name)}</b> <span class="handle">@${esc(p.handle)}</span> <time datetime="${esc(p.created_at)}">${d.getUTCDate()} ${MONTHS[d.getUTCMonth()]} ${d.getUTCFullYear()}</time> <a href="${esc(p.url)}" rel="noopener noreferrer" target="_blank">Open on X</a></p>
    ${p.quotes ? `<p class="pin-quoted">Quoting <span class="handle">@${esc(p.quotes.handle)}</span>: “${esc(p.quotes.text)}”</p>` : ''}
  </figure>
  <div class="pin-answer">
    <h1 id="pin-h">${esc(SITE.line)}</h1>
    ${SITE.purpose.map((t) => `<p>${esc(t)}</p>`).join('')}
  </div>
</section>`;
}

// ---------- pages

function pulsePage() {
  const active = desks.filter((d) => d.posts > 0).length;
  const picker = `<section class="yours" id="yours" aria-labelledby="yours-h">
  <header class="sec-head"><h2 id="yours-h">Which worlds do you live in?</h2><p>Pick the desks you already follow. The page will mark what you are not seeing.</p></header>
  <div class="yours-desks" role="group" aria-label="Desks you follow">${DESKS.desks.map((d) => `<button type="button" class="pick" data-desk="${d.id}" aria-pressed="false"><span class="code">${d.code}</span>${esc(d.name)}</button>`).join('')}</div>
  <p class="yours-out" id="yours-out" hidden></p>
</section>`;
  const pulseList = pulse.length
    ? `<ol class="pulse">${pulse.map(pulseRow).join('')}</ol>`
    : `<div class="empty"><h3>The first pulse is being read.</h3><p>The instrument is recording on ${active} of ${desks.length} desks. Posts appear here once each has been confirmed with X and passed by the editor.</p></div>`;
  const body = `${pinned()}
<section class="record" id="record" aria-labelledby="record-h">
  <header class="sec-head"><h2 id="record-h">The record</h2><p>The last 24 hours on all ${desks.length} desks. Each line is one desk; its height is views gained per hour. A flag is a researched story, and its number is the story's magnitude.${captures.length < 4 ? ` <strong>Early days: ${captures.length === 1 ? 'one reading' : captures.length + ' readings'} so far, so each line shows only when its posts began. It sharpens with every hourly reading.</strong>` : ''}</p></header>
  ${recordFigure(desks)}
</section>
${picker}
<section class="pulse-sec" id="pulse" aria-labelledby="pulse-h">
  <header class="sec-head"><h2 id="pulse-h">Internet Pulse</h2>
    <p>The posts the internet is passing around right now, largest first, from every desk. The number is magnitude: 6.0 is a million views, 7.0 is ten million. The sentence above each post is ours and says what it is, not whether it is right.</p>
    <div class="sort" role="group" aria-label="Order"><button type="button" data-sort="views" aria-pressed="true">Largest</button><button type="button" data-sort="pace" aria-pressed="false">Fastest</button><button type="button" data-sort="start" aria-pressed="false">Newest</button></div>
  </header>
  ${pulseList}
</section>
<section class="stories-sec" id="stories" aria-labelledby="stories-h">
  <header class="sec-head"><h2 id="stories-h">Researched stories</h2><p>Slower and deeper: what happened, how each world is describing it, and what is on the record, with sources.</p></header>
  ${live.length ? `<ul class="teasers">${live.slice(0, 6).map(storyTeaser).join('')}</ul><p class="desk-nums"><a href="/stories/">All ${live.length} current stories</a></p>` : `<div class="empty"><h3>No stories written up yet.</h3></div>`}
</section>`;
  return page({ title: `${SITE.name}: ${SITE.line}`, description: 'What every corner of the internet is passing around, on one record: twenty desks, measured hourly, with what each world is seeing and what is established.', path: '/', body, current: '/' });
}

function storiesPage() {
  const body = `<section class="desk-head"><p class="label">${live.length} current</p><h1>Researched stories</h1><p class="dek">For the things worth more than a line: what happened, why it is spreading, how each world is describing it, and what is on the record. Each claim has a source, and each post was confirmed with X.</p></section>
<section class="bulletin" id="bulletin">
  <header class="sec-head"><h2>The last 48 hours</h2>
    <div class="sort" role="group" aria-label="Order"><button type="button" data-sort="mag" aria-pressed="true">Largest</button><button type="button" data-sort="rate" aria-pressed="false">Fastest</button><button type="button" data-sort="start" aria-pressed="false">Newest</button></div>
  </header>
  ${live.length ? `<ol class="stories">${live.map(storyRow).join('')}</ol>` : `<div class="empty"><h3>The first stories are being written.</h3></div>`}
  ${past.length ? `<p class="desk-nums"><a href="/archive/">${past.length} earlier ${past.length === 1 ? 'story' : 'stories'} in the archive</a></p>` : ''}
</section>`;
  return page({ title: `Stories · ${SITE.name}`, description: 'Researched write-ups of what the internet is passing around: what happened, how each world sees it, and what is established.', path: '/stories/', body, current: '/stories/' });
}

function storyPage(s) {
  const body = `<article class="full">
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
      <h2>The posts</h2>${s.posts.map((p) => postBlock(p)).join('')}
      ${(s.corrections ?? []).length ? `<h2>Corrections</h2><ul class="sources">${s.corrections.map((c) => `<li><time datetime="${esc(c.at)}">${hhmm(Date.parse(c.at))} UTC, ${day(Date.parse(c.at))}</time> ${esc(c.text)}</li>`).join('')}</ul>` : ''}
      ${(s.sources ?? []).length ? `<h2>Sources</h2><ul class="sources">${s.sources.map((x) => `<li><a href="${esc(x.url)}" rel="noopener noreferrer" target="_blank">${esc(x.label)}</a></li>`).join('')}</ul>` : ''}
    </div>
    <aside class="full-side">
      <p class="updated">Written up ${hhmm(Date.parse(s.updated_at))} UTC, ${day(Date.parse(s.updated_at))}</p>
      ${magBlock(s)}
      ${spark(s, 280, 80)}
      <dl><div><dt>Views</dt><dd>${num(s.n.views)}</dd></div><div><dt>Last hour</dt><dd>${s.n.perHour == null ? 'n/a' : num(s.n.perHour)}</dd></div><div><dt>Posts tracked</dt><dd>${s.posts.length}</dd></div><div><dt>Began</dt><dd>${hhmm(s.started)} UTC</dd></div></dl>
    </aside>
  </div>
</article>`;
  return page({ title: `${s.title} · ${SITE.name}`, description: s.dek, path: `/story/${s.id}/`, body });
}

function deskPage(d) {
  const all = [...d.stories, ...d.also];
  const body = `<section class="desk-head">
  <p class="label">${esc(DESKS.groups.find((g) => g.id === d.group).name)} · station ${d.code}</p>
  <h1>${esc(d.name)}</h1>
  <p class="dek">${esc(d.scope)}</p>
  <p class="beats">${d.beats.map((b) => `<span>${esc(b)}</span>`).join('')}</p>
</section>
<section class="record">${recordFigure([d], { labels: false })}
  <p class="desk-nums">${d.posts ? `${d.posts} posts written in the last 24 hours are on record for this desk, with ${num(d.views)} views between them.` : 'Nothing on this desk cleared its floor in the last 24 hours.'}</p>
</section>
<section class="pulse-sec">
  <header class="sec-head"><h2>On this desk now</h2></header>
  ${d.pulse.length ? `<ol class="pulse">${d.pulse.map(pulseRow).join('')}</ol>` : `<div class="empty"><h3>Nothing from this desk is on the pulse right now.</h3><p>A quiet desk is reported as quiet. Nothing is added to fill it.</p></div>`}
</section>
<section class="bulletin">
  <header class="sec-head"><h2>Researched stories on this desk</h2></header>
  ${all.length ? `<ol class="stories">${all.map(storyRow).join('')}</ol>` : `<p class="desk-nums">None in the last 48 hours.</p>`}
  ${d.past.length ? `<p class="desk-nums"><a href="/archive/">${d.past.length} earlier ${d.past.length === 1 ? 'story' : 'stories'} on this desk in the archive</a></p>` : ''}
</section>`;
  return page({ title: `${d.name} · ${SITE.name}`, description: d.scope, path: `/desk/${d.id}/`, body, current: '/desks/' });
}

function desksPage() {
  const body = `<section class="desk-head"><p class="label">${desks.length} stations</p><h1>The desks</h1><p class="dek">Every part of the internet's attention this site watches. Each is swept on a schedule, and a quiet desk is reported as quiet.</p></section>
<section class="desk-index">${DESKS.groups.map((g) => `<div class="desk-group"><h2>${esc(g.name)}</h2><ul>${desks.filter((d) => d.group === g.id).map((d) => {
    const top = d.pulse[0]?.line ?? d.stories[0]?.title;
    return `<li><a href="/desk/${d.id}/"><span class="code">${d.code}</span><b>${esc(d.name)}</b><span class="desk-peak">${d.posts ? mag(d.mag) : 'quiet'}</span><span class="desk-top">${top ? esc(top) : esc(d.scope.split(':')[0])}</span></a></li>`;
  }).join('')}</ul></div>`).join('')}</section>`;
  return page({ title: `The desks · ${SITE.name}`, description: 'The twenty desks this site watches, in six groups.', path: '/desks/', body, current: '/desks/' });
}

function archivePage() {
  const days = new Map();
  for (const s of past) { const k = new Date(s.started).toISOString().slice(0, 10); if (!days.has(k)) days.set(k, []); days.get(k).push(s); }
  const list = [...days.entries()].map(([k, list]) => `<div class="desk-group"><h2>${day(Date.parse(k + 'T12:00:00Z'))}</h2><ul>${list.sort((a, b) => (b.n.magnitude ?? 0) - (a.n.magnitude ?? 0)).map((s) => `<li><a href="/story/${esc(s.id)}/"><span class="code">${s.home?.code ?? ''}</span><b>${esc(s.title)}</b><span class="desk-peak">${mag(s.n.magnitude)}</span><span class="desk-top">${esc(s.dek)}</span></a></li>`).join('')}</ul></div>`).join('');
  const body = `<section class="desk-head"><p class="label">${past.length} ${past.length === 1 ? 'story' : 'stories'}</p><h1>The archive</h1><p class="dek">A story leaves the bulletin 48 hours after it began and is kept here, as it was last written up, with the numbers its posts had reached.</p></section>
<section class="desk-index archive">${list || '<div class="empty"><h3>Nothing here yet.</h3><p>The record began on 9 October 2026. Stories arrive here two days after they start.</p></div>'}</section>`;
  return page({ title: `Archive · ${SITE.name}`, description: 'Stories that have left the bulletin, by day.', path: '/archive/', body, current: '/archive/' });
}

function aboutPage() {
  const body = `${pinned()}
<section class="about">
  <h2>How it is made</h2>
  <ol class="steps">
    <li><h3>Grok reads X.</h3><p>Every hour it records what is spreading on each of twenty desks: the posts exactly as written, and their numbers. It re-reads the posts it is tracking so that speed can be measured. It writes no words of its own.</p></li>
    <li><h3>Each post is checked.</h3><p>A post's id carries the moment it was created, so a record whose date does not match its id is rejected. Before a post appears here, X is asked directly whether it exists and whether its author and text match.</p></li>
    <li><h3>Claude writes.</h3><p>It reads each post before it is shown, leaves out what should not be shown, and writes the sentence above it. For the larger things it reads the reporting and writes a story: what happened, why it is spreading, how each world is seeing it, and what is on the record. It supplies no numbers.</p></li>
  </ol>
  <h2>How to read it</h2>
  <dl class="glossary">
    <div><dt>Internet Pulse</dt><dd>The front of the site: single posts, largest first, from every desk, refreshed each hour. The sentence above a post is the editor's and says what the post is, not whether it is right.</dd></div>
    <div><dt>Stories</dt><dd>Slower and deeper. For the things worth more than a line: what happened, why it is spreading, how each world describes it, and what is on the record, with sources.</dd></div>
    <div><dt>Magnitude</dt><dd>The base ten log of views, for one post on the pulse or across a story's tracked posts. 6.0 is a million views, 7.0 is ten million, 8.0 is a hundred million. Each whole step is ten times larger.</dd></div>
    <div><dt>The record</dt><dd>One line per desk over 24 hours. The height of a line is the views gained per hour by the posts recorded on that desk, on a log scale. The wiggle itself carries no information; only its height does.</dd></div>
    <div><dt>Worlds</dt><dd>When groups of people are describing the same story differently, each description is set out beside the post that carries it, followed by what is established.</dd></div>
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
put('404.html', page({ title: `Not found · ${SITE.name}`, description: 'No such page.', path: '/404', body: '<section class="desk-head"><p class="label">404</p><h1>Nothing recorded here.</h1><p class="dek"><a href="/">Back to the record.</a></p></section>' }));
for (const f of ['styles.css', 'app.js', 'favicon.svg']) cpSync(join(REPO, 'site', f), join(OUT, f));
// Cloudflare adds its analytics beacon to every page on this zone; it is allowed by name. It also
// adds an inline bot-check script, which stays blocked: no inline script runs here, Cloudflare's included.
const CSP = "default-src 'none'; script-src 'self' https://static.cloudflareinsights.com; style-src 'self' https://fonts.googleapis.com; style-src-attr 'unsafe-inline'; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' https://cloudflareinsights.com; base-uri 'none'; form-action 'none'; frame-ancestors 'none'";
put('_headers', `/*\n  Content-Security-Policy: ${CSP}\n  Strict-Transport-Security: max-age=31536000\n  X-Content-Type-Options: nosniff\n  X-Frame-Options: DENY\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  X-Robots-Tag: noindex\n`);
put('robots.txt', 'User-agent: *\nDisallow: /\n');
put('data/pulse.json', JSON.stringify({ as_of: new Date(NOW).toISOString(), demo: DEMO, desks: desks.map((d) => ({ id: d.id, code: d.code, posts: d.posts, views: d.views, magnitude: d.mag })), pulse: pulse.map((it) => ({ id: it.id, url: it.post.url, desk: it.deskInfo?.id ?? null, line: it.line, views: it.n.views, magnitude: it.n.magnitude, views_per_hour: it.pace })), stories: live.map((s) => ({ id: s.id, title: s.title, desks: s.desks, standing: s.standing, ...s.n })) }, null, 1));
if (DEMO) put('DEMO', 'Built from invented data. Never deploy this folder.\n');
console.log(`built ${DEMO ? 'DEMO ' : ''}site: ${pulse.length} on the pulse, ${stories.length} stories (${live.length} current), ${desks.filter((d) => d.posts).length}/${desks.length} desks active, ${records.size} posts, as of ${new Date(NOW).toISOString()}`);
