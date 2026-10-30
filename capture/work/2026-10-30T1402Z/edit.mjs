import fs from 'fs';
const f = '/workspace/mts-editor/pulse/current.json';
const p = JSON.parse(fs.readFileSync(f));
const drop = new Set(['2115593262799151111', '2115588901196984822', '2115111611652276717']);
p.items = p.items.filter(i => !drop.has(i.id));
p.items.push(
  {
    id: '2115813444083490867',
    desk: 'internet',
    line: 'Dexerto reports that YouTuber ItalianBach wants custom thumbnails removed and replaced with a random frame from the video. The post quotes him saying it would end clickbait and let viewers "know exactly what you’re going to be seeing". Not checked here.'
  },
  {
    id: '2115848262481768576',
    desk: 'entertainment',
    line: 'Actor Chris Pratt posts a long account of how he got his first film role while waiting tables in Hawaii, after a movie star he met there offered him a part. The story is his own. Not checked here.'
  }
);
p.updated_at = '2026-10-30T12:35:00Z';
p.capture = '2026-10-30T1209Z';
fs.writeFileSync(f, JSON.stringify(p, null, 2) + '\n');
console.log(p.items.length);
