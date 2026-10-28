// The store's client: how the tools talk to the Worker's /ingest and /api routes.
// The token comes from MTS_TOKEN, else from store.local.token at the repository root
// (ignored by git). The store's address comes from MTS_STORE_URL, else the live site.
import { existsSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO = join(dirname(fileURLToPath(import.meta.url)), '..', '..');

export function storeToken() {
  if (process.env.MTS_TOKEN) return process.env.MTS_TOKEN.trim();
  const f = join(REPO, 'store.local.token');
  if (existsSync(f)) return readFileSync(f, 'utf8').trim();
  return null;
}

export function storeClient({ base = process.env.MTS_STORE_URL ?? 'https://situation.seansooch.dev', token = storeToken() } = {}) {
  if (!token) throw new Error('no store token: set MTS_TOKEN or write store.local.token');
  const call = async (method, path, body) => {
    const r = await fetch(base + path, { method, headers: { authorization: `Bearer ${token}`, ...(body ? { 'content-type': 'application/json' } : {}) }, body: body ? JSON.stringify(body) : undefined });
    const text = await r.text();
    let data;
    try { data = JSON.parse(text); } catch { data = { raw: text.slice(0, 300) }; }
    if (!r.ok) {
      const errs = data.errors ? `${data.errors.slice(0, 3).join('; ')}${data.errors.length > 3 ? ` (and ${data.errors.length - 3} more)` : ''}` : null;
      const e = new Error(`${method} ${path}: ${r.status} ${data.error ?? errs ?? data.note ?? data.raw ?? ''}`);
      e.status = r.status; e.data = data; throw e;
    }
    return data;
  };
  return { base, get: (path) => call('GET', path), post: (path, body) => call('POST', path, body) };
}
