#!/usr/bin/env node
// Compare what is live with what was built, file by file. A status code proves nothing.
//
//   node tools/audit-live.mjs [https://situation.seansooch.dev]
//
// Cloudflare adds two scripts to every HTML page on this zone (its bot check and its analytics
// beacon). They are removed before comparing; anything else that differs is a real difference.
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const DIST = join(dirname(fileURLToPath(import.meta.url)), '..', 'dist');
const HOST = (process.argv[2] ?? JSON.parse(readFileSync(join(DIST, '..', 'site.json'), 'utf8')).url).replace(/\/$/, '');

export const stripEdge = (html) => html.replace(/<script\b[^>]*>(?:(?!<\/script>)[\s\S])*?<\/script>/g, (tag) => (/cdn-cgi\/challenge-platform|static\.cloudflareinsights\.com/.test(tag) ? '' : tag));

function files(dir, base = '') {
  return readdirSync(dir).flatMap((name) => {
    const rel = base ? `${base}/${name}` : name;
    return statSync(join(dir, name)).isDirectory() ? files(join(dir, name), rel) : [rel];
  });
}

if (process.argv[1] && process.argv[1].endsWith('audit-live.mjs')) {
  let diff = 0, n = 0;
  for (const rel of files(DIST).filter((f) => f !== '_headers')) {
    const url = `${HOST}/${rel.replace(/(^|\/)index\.html$/, '$1')}?audit=${Date.now()}`;
    const built = readFileSync(join(DIST, rel), 'utf8');
    let live;
    try { const r = await fetch(url, { redirect: 'follow' }); live = r.ok || rel === '404.html' ? await r.text() : `HTTP ${r.status}`; }
    catch (e) { live = `no answer: ${e.message}`; }
    if (rel.endsWith('.html')) live = stripEdge(live);
    n++;
    if (live !== built) { diff++; console.log(`DIFF ${rel}`); }
  }
  const head = await fetch(`${HOST}/`, { method: 'HEAD' });
  for (const h of ['content-security-policy', 'x-robots-tag', 'strict-transport-security']) if (!head.headers.get(h)) { diff++; console.log(`MISSING header ${h}`); }
  const lost = await fetch(`${HOST}/no-such-page-${Date.now()}`);
  if (lost.status !== 404) { diff++; console.log(`an unknown path answered ${lost.status}, not 404`); }
  console.log(`${n} files compared with ${HOST}: ${diff ? diff + ' problems' : 'all match, headers present, unknown paths answer 404'}`);
  process.exit(diff ? 1 : 0);
}
