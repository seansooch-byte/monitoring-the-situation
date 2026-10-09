#!/usr/bin/env node
// Writes fixtures/demo/: a day of invented captures and stories, in the real file formats,
// so the site can be designed before the grabber's first run. See tools/demo-stories.mjs.
//
//   node tools/make-demo.mjs
import { mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { snowflakeFor, runIdFor } from './check-capture.mjs';
import { STORIES } from './demo-stories.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', 'fixtures', 'demo');
const NOW = Date.parse('2026-10-08T22:00:00Z');
const HOUR = 3600000, MIN = 60000;
const iso = (ms) => new Date(ms).toISOString().replace(/\.\d{3}Z$/, 'Z');

// Small seeded generator so the fixture is the same every time.
let seed = 20261008;
const rnd = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };

const posts = [];
const moments = [];
STORIES.forEach((s, si) => {
  const started = NOW - s.start * HOUR;
  const ids = s.posts.map((p, pi) => {
    const created = Math.floor((started + p.at * MIN) / 1000) * 1000;
    const id = snowflakeFor(created, si * 16 + pi + 1);
    posts.push({
      created, v: p.v, tau: p.tau * HOUR, likeRate: 0.018 + rnd() * 0.03,
      record: {
        id, url: `https://x.com/${p.handle}/status/${id}`, created_at: iso(created), lang: 'en', text: p.text,
        author: { handle: p.handle, name: p.name, followers: p.followers, verified: p.followers > 100000 ? 'blue' : 'none', kind: p.kind },
        media: (p.media ?? []).map((m) => ({ type: m.type, description: m.description, alt: null, duration_s: m.duration_s ?? null, link_url: null, link_title: null })),
        reply_to: null, quotes: null, note: null, flags: s.private ? ['private_individual'] : [],
        desk: s.desks[0], beat: s.beat ?? null, topic: s.slug.replaceAll('-', ' '), lead: null,
      },
    });
    return id;
  });
  moments.push({
    schema: 'mts.moment/1',
    id: `${iso(started).slice(0, 10)}-${s.slug}`,
    title: s.title, dek: s.dek, desks: s.desks, standing: s.standing,
    started_at: iso(started), updated_at: iso(NOW),
    what: s.what, why: s.why,
    worlds: (s.worlds ?? []).map((w) => ({ name: w.name, sees: w.sees, post: ids[w.post] })),
    common: s.common ?? null, next: s.next ?? null,
    posts: s.posts.map((p, pi) => ({ id: ids[pi], role: p.role })),
    sources: [],
  });
});

rmSync(ROOT, { recursive: true, force: true });
const recorded = new Set();
for (let h = 23; h >= 0; h--) {
  const start = NOW - h * HOUR;
  const fresh = [], observations = [];
  for (const p of posts) {
    if (p.created > start) continue;
    const age = start + 90000 - p.created;
    const views = Math.round(p.v * (1 - Math.exp(-age / p.tau)) * (0.985 + rnd() * 0.03));
    const likes = Math.round(views * p.likeRate);
    observations.push({ id: p.record.id, at: iso(start + 90000), state: 'live', views, likes, reposts: Math.round(likes * 0.13), quotes: Math.round(likes * 0.02), replies: Math.round(likes * 0.035), bookmarks: Math.round(likes * 0.09), approx: false });
    if (!recorded.has(p.record.id)) { recorded.add(p.record.id); fresh.push(p.record); }
  }
  const doc = {
    schema: 'mts.capture/1',
    run: { id: runIdFor(start), started_at: iso(start), finished_at: iso(start + 4 * MIN), status: observations.length ? 'ok' : 'partial', reason: observations.length ? null : 'nothing cleared a floor this hour', grabber: { agent: 'demo', model: null, method: 'invented fixture, not read from X' }, requests_rev: null },
    sweeps: [
      { id: 'watch', kind: 'watch', desk: null, method: 'invented', window_hours: null, status: 'ok', reason: null, post_ids: observations.map((o) => o.id).filter((id) => !fresh.some((f) => f.id === id)) },
      { id: 'viral.global', kind: 'discovery', desk: null, method: 'invented', window_hours: 24, status: 'ok', reason: null, post_ids: fresh.map((f) => f.id) },
    ],
    trends: [], posts: fresh, observations, context: [], answers: [],
  };
  if (!fresh.length && observations.length) doc.run = { ...doc.run, status: 'partial', reason: 'no new posts this hour; re-reads only' };
  const d = new Date(start).toISOString();
  const file = join(ROOT, 'capture', d.slice(0, 4), d.slice(5, 7), d.slice(8, 10), `${d.slice(11, 13)}${d.slice(14, 16)}Z.json`);
  mkdirSync(dirname(file), { recursive: true });
  writeFileSync(file, JSON.stringify(doc, null, 1) + '\n');
}
mkdirSync(join(ROOT, 'moments'), { recursive: true });
for (const m of moments) writeFileSync(join(ROOT, 'moments', `${m.id}.json`), JSON.stringify(m, null, 2) + '\n');
writeFileSync(join(ROOT, 'DEMO'), 'Invented data for design work. Never deploy a site built from this folder.\n');
console.log(`demo: ${moments.length} stories, ${posts.length} posts, 24 captures in fixtures/demo`);
