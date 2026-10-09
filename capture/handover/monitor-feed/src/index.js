// monitor-feed: the live "Monitoring the Situation" briefing for seansooch.dev.
//
// Public:  GET|HEAD /              -> tiny JSON pointer to /v1/feed.json
//          GET|HEAD /v1/feed.json  -> latest briefing (ETag/304, CORS allow-list)
//          OPTIONS  (any known path) -> CORS preflight
// Private: PUT /v1/feed            -> Bearer FEED_WRITE_SECRET; validates, rotates latest->prev, writes archive
// Everything else is 404 (unknown path) or 405 (known path, wrong method).

const ALLOWED_ORIGINS = new Set(['https://seansooch.dev', 'https://sean-sooch-portfolio.pages.dev']);
const MAX_BODY = 256 * 1024;
const ARCHIVE_TTL = 30 * 24 * 60 * 60;
const FEED_CACHE = 'public, max-age=60, stale-while-revalidate=600, stale-if-error=86400';
const SOURCE_TYPES = new Set(['x', 'web', 'both']);
const LIMITS = { sections: 20, items: 50, links: 20, name: 120, headline: 500, summary: 4000, label: 200, url: 2048 };

export default {
  async fetch(request, env) {
    try {
      return await route(request, env);
    } catch (err) {
      console.error('unhandled', err && err.stack || err);
      return json({ error: 'internal error' }, 500);
    }
  },
};

async function route(request, env) {
  const url = new URL(request.url);
  const method = request.method;
  const path = url.pathname;

  if (path === '/' || path === '/v1/feed.json') {
    if (method === 'OPTIONS') return preflight(request);
    if (method !== 'GET' && method !== 'HEAD') return methodNotAllowed('GET, HEAD, OPTIONS');
    if (path === '/') {
      return withCors(request, json({ name: 'monitor-feed', feed: '/v1/feed.json', version: 1 }, 200,
        { 'Cache-Control': 'public, max-age=300' }), method);
    }
    return withCors(request, await getFeed(request, env), method);
  }
  if (path === '/v1/feed') {
    if (method !== 'PUT') return methodNotAllowed('PUT');
    return putFeed(request, env);
  }
  return json({ error: 'not found' }, 404);
}

// ---------- read ----------

async function getFeed(request, env) {
  const { value, metadata } = await env.FEED.getWithMetadata('latest', { type: 'text', cacheTtl: 60 });
  if (value === null) {
    return json({ error: 'no feed yet' }, 503, { 'Cache-Control': 'no-store', 'Retry-After': '60' });
  }
  const etag = metadata && metadata.etag ? `"${metadata.etag}"` : `"${await sha256hex(value)}"`;
  const headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': FEED_CACHE,
    'ETag': etag,
    'X-Content-Type-Options': 'nosniff',
  };
  if (metadata && metadata.stored_at) headers['Last-Modified'] = new Date(metadata.stored_at).toUTCString();
  if (etagMatches(request.headers.get('If-None-Match'), etag)) {
    return new Response(null, { status: 304, headers });
  }
  return new Response(value, { status: 200, headers });
}

function etagMatches(header, etag) {
  if (!header) return false;
  const bare = etag.replace(/^W\//, '');
  return header.split(',').map((s) => s.trim()).some((t) => t === '*' || t.replace(/^W\//, '') === bare);
}

// ---------- CORS ----------

function corsHeaders(request) {
  const origin = request.headers.get('Origin');
  const h = { 'Vary': 'Origin' };
  if (origin && ALLOWED_ORIGINS.has(origin)) {
    h['Access-Control-Allow-Origin'] = origin;
    h['Access-Control-Expose-Headers'] = 'ETag, Last-Modified';
  }
  return h;
}

function withCors(request, response, method) {
  const headers = new Headers(response.headers);
  for (const [k, v] of Object.entries(corsHeaders(request))) headers.set(k, v);
  return new Response(method === 'HEAD' ? null : response.body, { status: response.status, headers });
}

function preflight(request) {
  const headers = { ...corsHeaders(request), 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'public, max-age=86400' };
  if (headers['Access-Control-Allow-Origin']) {
    headers['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS';
    headers['Access-Control-Allow-Headers'] = 'If-None-Match';
    headers['Access-Control-Max-Age'] = '86400';
  }
  return new Response(null, { status: 204, headers });
}

// ---------- write ----------

async function putFeed(request, env) {
  if (!env.FEED_WRITE_SECRET) return json({ error: 'writes are not configured' }, 503);
  const auth = request.headers.get('Authorization') || '';
  const m = /^Bearer\s+(\S+)\s*$/.exec(auth);
  if (!m || !(await safeEqual(m[1], env.FEED_WRITE_SECRET))) {
    return json({ error: 'unauthorized' }, 401, { 'WWW-Authenticate': 'Bearer' });
  }

  const declared = Number(request.headers.get('Content-Length'));
  if (Number.isFinite(declared) && declared > MAX_BODY) return json({ error: `body exceeds ${MAX_BODY} bytes` }, 413);
  const text = await readCapped(request);
  if (text === null) return json({ error: `body exceeds ${MAX_BODY} bytes` }, 413);

  let input;
  try { input = JSON.parse(text); } catch { return json({ error: 'body is not valid JSON' }, 400); }
  const result = validate(input);
  if (result.error) return json({ error: result.error }, 400);

  const doc = result.doc;
  const body = JSON.stringify(doc);
  const etag = await sha256hex(body);
  const now = new Date().toISOString();
  const meta = { etag, generated_at: doc.generated_at, stored_at: now };

  const prev = await env.FEED.getWithMetadata('latest', { type: 'text' });
  if (prev.value !== null) await env.FEED.put('prev', prev.value, { metadata: prev.metadata || {} });
  await env.FEED.put('latest', body, { metadata: meta });
  await env.FEED.put(`archive:${doc.generated_at.slice(0, 10)}`, body, { metadata: meta, expirationTtl: ARCHIVE_TTL });

  return new Response(null, { status: 204, headers: { 'ETag': `"${etag}"`, 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' } });
}

async function readCapped(request) {
  if (!request.body) return '';
  const reader = request.body.getReader();
  const chunks = [];
  let size = 0;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    size += value.byteLength;
    if (size > MAX_BODY) { try { await reader.cancel(); } catch {} return null; }
    chunks.push(value);
  }
  const all = new Uint8Array(size);
  let off = 0;
  for (const c of chunks) { all.set(c, off); off += c.byteLength; }
  return new TextDecoder().decode(all);
}

async function safeEqual(a, b) {
  const enc = new TextEncoder();
  const [ha, hb] = await Promise.all([
    crypto.subtle.digest('SHA-256', enc.encode(a)),
    crypto.subtle.digest('SHA-256', enc.encode(b)),
  ]);
  return crypto.subtle.timingSafeEqual(ha, hb);
}

// Returns { doc } (normalised: version first, known fields only) or { error }.
export function validate(input) {
  const isObj = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);
  const str = (v, max, min = 1) => typeof v === 'string' && v.trim().length >= min && v.length <= max;
  if (!isObj(input)) return { error: 'body must be a JSON object' };
  if (input.version !== undefined && input.version !== 1) return { error: 'version must be 1' };
  if (typeof input.generated_at !== 'string' || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:\d{2})$/.test(input.generated_at)
      || Number.isNaN(Date.parse(input.generated_at))) {
    return { error: 'generated_at must be an ISO 8601 timestamp with a timezone' };
  }
  if (!Array.isArray(input.sections) || input.sections.length < 1 || input.sections.length > LIMITS.sections) {
    return { error: `sections must be an array of 1-${LIMITS.sections}` };
  }
  const sections = [];
  for (const [si, s] of input.sections.entries()) {
    const at = `sections[${si}]`;
    if (!isObj(s)) return { error: `${at} must be an object` };
    if (!str(s.name, LIMITS.name)) return { error: `${at}.name must be a non-empty string (max ${LIMITS.name})` };
    if (!Array.isArray(s.items) || s.items.length > LIMITS.items) return { error: `${at}.items must be an array (max ${LIMITS.items})` };
    const items = [];
    for (const [ii, it] of s.items.entries()) {
      const ai = `${at}.items[${ii}]`;
      if (!isObj(it)) return { error: `${ai} must be an object` };
      if (!str(it.headline, LIMITS.headline)) return { error: `${ai}.headline must be a non-empty string (max ${LIMITS.headline})` };
      if (!str(it.summary, LIMITS.summary, 0)) return { error: `${ai}.summary must be a string (max ${LIMITS.summary})` };
      if (!SOURCE_TYPES.has(it.source_type)) return { error: `${ai}.source_type must be one of x, web, both` };
      if (!Array.isArray(it.links) || it.links.length < 1 || it.links.length > LIMITS.links) {
        return { error: `${ai}.links must be an array of 1-${LIMITS.links}` };
      }
      const links = [];
      for (const [li, l] of it.links.entries()) {
        const al = `${ai}.links[${li}]`;
        if (!isObj(l)) return { error: `${al} must be an object` };
        if (!str(l.label, LIMITS.label)) return { error: `${al}.label must be a non-empty string (max ${LIMITS.label})` };
        if (typeof l.url !== 'string' || l.url.length > LIMITS.url) return { error: `${al}.url must be a string (max ${LIMITS.url})` };
        let u;
        try { u = new URL(l.url); } catch { return { error: `${al}.url is not a valid URL` }; }
        if (u.protocol !== 'https:' || u.username || u.password) return { error: `${al}.url must be an https URL without credentials` };
        links.push({ label: l.label, url: u.href });
      }
      items.push({ headline: it.headline, summary: it.summary, links, source_type: it.source_type });
    }
    sections.push({ name: s.name, items });
  }
  return { doc: { version: 1, generated_at: input.generated_at, sections } };
}

// ---------- helpers ----------

function json(obj, status, extra = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff', ...extra },
  });
}

function methodNotAllowed(allow) {
  return json({ error: 'method not allowed' }, 405, { Allow: allow });
}

async function sha256hex(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}
