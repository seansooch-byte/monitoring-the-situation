// One directory walk for every tool. It returns the regular files whose names the test accepts,
// in name order, and never follows a symlink. The grabber's scratch (capture/work/) has held
// links whose names differ from their targets only by case; on a case-insensitive disk such a
// link points at itself and stat() loops, so a walk that followed links could not build the site.
import { existsSync, lstatSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

export function walk(dir, test, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    const s = lstatSync(p);
    if (s.isSymbolicLink()) continue;
    if (s.isDirectory()) walk(p, test, out);
    else if (s.isFile() && test(name)) out.push(p);
  }
  return out;
}
