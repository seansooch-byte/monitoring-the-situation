import fs from 'fs';
const R = '/workspace/mts-editor/';
const posts = {}, obs = {};
const files = [];
for (const d of ['29', '30']) {
  const dir = R + 'capture/2026/10/' + d;
  for (const f of fs.readdirSync(dir).sort()) if (f.endsWith('Z.json')) files.push(dir + '/' + f);
}
for (const f of files) {
  const c = JSON.parse(fs.readFileSync(f));
  for (const p of c.posts || []) posts[p.id] = p;
  for (const o of c.observations || []) obs[o.id] = o;
}
const v = JSON.parse(fs.readFileSync(R + 'verified/posts.json'));
const vp = v.posts || v;
const pulse = JSON.parse(fs.readFileSync(R + 'pulse/current.json'));
const inP = new Set(pulse.items.flatMap(i => [i.id, ...(i.also || [])]));
const cut = Date.parse('2026-10-30T12:15:00Z') - 36 * 3600e3;
const rows = Object.values(posts)
  .filter(p => Date.parse(p.created_at) >= cut && obs[p.id])
  .map(p => ({ p, o: obs[p.id], s: (vp[p.id] && (vp[p.id].status || vp[p.id].state)) || '?' }));
rows.sort((a, b) => b.o.views - a.o.views);
for (const { p, o, s } of rows.slice(0, +process.argv[2] || 90))
  console.log(inP.has(p.id) ? '*' : ' ', p.id, p.desk, '@' + p.author.handle, o.views, p.created_at.slice(5, 16), s, (p.flags || []).join(','), o.at.slice(11, 16), '|', p.text.replace(/\n/g, ' ').slice(0, 110));
console.log(rows.length);
