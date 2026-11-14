// Every version of pulse/current.json the repo has committed, oldest first, as { t, items }: the
// commit time in milliseconds and the pulse's items. Two git processes in all, however long the
// history: one log that names each version's blob, one cat-file that hands every blob over at once.
// A version that is not JSON is skipped. Used by the build and tools/edition.mjs to know which line
// the editor had written for a post by a given time (contract/PAPER.md).
import { execFileSync } from 'node:child_process';

export function pulseHistory(repo, file = 'pulse/current.json') {
  let log;
  try {
    log = execFileSync('git', ['log', '--reverse', '--format=@%ct', '--raw', '--no-renames', '--abbrev=40', '--', file], { cwd: repo, encoding: 'utf8', maxBuffer: 256 * 1024 * 1024 });
  } catch {
    return [];
  }
  const versions = [];
  let t = null;
  for (const line of log.split('\n')) {
    if (line.startsWith('@')) t = Number(line.slice(1)) * 1000;
    else if (line.startsWith(':') && t != null) {
      const [meta] = line.split('\t');
      const blob = meta.split(' ')[3];
      if (blob && !/^0+$/.test(blob)) versions.push({ t, blob });
    }
  }
  if (!versions.length) return [];
  const out = execFileSync('git', ['cat-file', '--batch'], { cwd: repo, input: versions.map((v) => v.blob).join('\n') + '\n', maxBuffer: 2 * 1024 * 1024 * 1024 });
  const history = [];
  let at = 0;
  for (const v of versions) {
    const nl = out.indexOf(0x0a, at);
    const header = out.subarray(at, nl).toString('utf8').split(' ');
    const size = Number(header[2]);
    const body = out.subarray(nl + 1, nl + 1 + size).toString('utf8');
    at = nl + 1 + size + 1;
    if (header[1] !== 'blob') continue;
    try {
      const items = JSON.parse(body).items;
      if (Array.isArray(items)) history.push({ t: v.t, items });
    } catch { /* a version that is not JSON says nothing */ }
  }
  return history;
}

// The editor's line for each post, as it stood by `end`, from versions committed in the 36 hours
// before `start` and up to `end`. A later version's line wins.
export function linesBetween(history, start, end) {
  const out = {};
  for (const v of history) {
    if (v.t < start - 36 * 3600000 || v.t > end) continue;
    for (const it of v.items) if (it && typeof it.id === 'string' && typeof it.line === 'string') out[it.id] = { desk: it.desk, line: it.line };
  }
  return out;
}
