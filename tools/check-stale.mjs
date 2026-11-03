#!/usr/bin/env node
// Is the live site current? Reads the as-of time off the front page and says how old it is. The
// as-of time is the newest capture the build read, so a site that stopped shipping shows here
// however healthy each part looks on its own.
//
//   node tools/check-stale.mjs [url] [--max-minutes N]
//
// The url defaults to MTS_SITE_URL, then https://situation.seansooch.dev/; N defaults to 180.
// Exit 0: FRESH. Exit 1: STALE. Exit 2: UNREACHABLE (no page) or NOASOF (no as-of time on it).
// One line is printed either way, so a scheduler can mail it as it is.
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const DEFAULT_URL = 'https://situation.seansooch.dev/';
export const DEFAULT_MAX_MINUTES = 180;
const FETCH_TIMEOUT_MS = 20000;

// The instant in the page's <time id="asof" datetime="...">, or null.
export function asOfFrom(html) {
  const m = /<time\b[^>]*\bid="asof"[^>]*\bdatetime="([^"]+)"/.exec(html ?? '') ?? /<time\b[^>]*\bdatetime="([^"]+)"[^>]*\bid="asof"/.exec(html ?? '');
  if (!m || !/^\d{4}-\d\d-\d\dT\d\d:\d\d(:\d\d(\.\d+)?)?Z$/.test(m[1])) return null;
  const at = Date.parse(m[1]);
  return Number.isFinite(at) ? at : null;
}

// The verdict on a page fetched at `now`: a pure function of the page, the clock and the limit.
export function staleness(html, now, maxMinutes = DEFAULT_MAX_MINUTES) {
  const at = asOfFrom(html);
  if (at == null) return { code: 2, line: 'NOASOF: the page has no readable as-of time (id="asof" datetime="...")' };
  const age = Math.max(0, Math.round((now - at) / 60000));
  const iso = new Date(at).toISOString().replace(/\.000Z$/, 'Z');
  if (age <= maxMinutes) return { code: 0, age, line: `FRESH: as of ${iso} (${age} min old)` };
  return { code: 1, age, line: `STALE: as of ${iso}, ${age} min old (${(age / 60).toFixed(1)} h), over the ${maxMinutes} min limit` };
}

async function main(argv) {
  const i = argv.indexOf('--max-minutes');
  const max = i >= 0 ? Number(argv[i + 1]) : DEFAULT_MAX_MINUTES;
  if (!Number.isFinite(max) || max <= 0) { console.log('usage: node tools/check-stale.mjs [url] [--max-minutes N]'); return 2; }
  const url = argv.find((a, k) => !a.startsWith('--') && argv[k - 1] !== '--max-minutes') ?? process.env.MTS_SITE_URL ?? DEFAULT_URL;
  let html;
  try {
    const r = await fetch(url, { redirect: 'follow', headers: { 'cache-control': 'no-cache' }, signal: AbortSignal.timeout(FETCH_TIMEOUT_MS) });
    if (!r.ok) throw new Error(`answered ${r.status}`);
    html = await r.text();
  } catch (e) {
    console.log(`UNREACHABLE: ${url} ${e.name === 'TimeoutError' ? `did not answer within ${FETCH_TIMEOUT_MS / 1000} s` : e.message}`);
    return 2;
  }
  const v = staleness(html, Date.now(), max);
  console.log(v.line);
  return v.code;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exit(await main(process.argv.slice(2)));
}
