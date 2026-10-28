// The shared directory walk. The grabber's scratch under capture/work/ has held symlinks whose
// names differ from their targets only by case; on a case-insensitive disk such a link points
// at itself and stat() loops (ELOOP). The walk therefore never follows a symlink, and it reads
// only what the caller's test accepts.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { walk } from '../tools/lib/files.mjs';

test('the walk returns the regular files the test accepts, in order, and skips every symlink', () => {
  const dir = mkdtempSync(join(tmpdir(), 'mts-walk-'));
  try {
    mkdirSync(join(dir, '2026', '10', '27'), { recursive: true });
    mkdirSync(join(dir, 'work'), { recursive: true });
    writeFileSync(join(dir, '2026', '10', '27', '1905Z.json'), '{}');
    writeFileSync(join(dir, '2026', '10', '27', '0005Z.json'), '{}');
    writeFileSync(join(dir, 'work', 'trend_Georgia.txt'), 'x');
    writeFileSync(join(dir, 'NOTES.md'), 'x');
    symlinkSync('loop.txt', join(dir, 'work', 'loop.txt'));            // points at itself: stat() would throw ELOOP
    symlinkSync(join(dir, '2026'), join(dir, 'again'));                 // a link to a directory: following it would double the files
    symlinkSync(join(dir, '2026', '10', '27', '1905Z.json'), join(dir, 'alias.json')); // a link to a file: not a file of its own

    const found = walk(dir, (name) => /^\d{4}Z\.json$/.test(name));
    assert.deepEqual(found, [join(dir, '2026', '10', '27', '0005Z.json'), join(dir, '2026', '10', '27', '1905Z.json')]);

    const everything = walk(dir, () => true);
    assert.ok(everything.every((p) => !p.includes('loop.txt') && !p.includes('again') && !p.endsWith('alias.json')), 'no symlink is ever returned or followed');
    assert.ok(everything.includes(join(dir, 'work', 'trend_Georgia.txt')), 'a regular file the test accepts is returned wherever it sits');
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test('a directory that does not exist walks to nothing', () => {
  assert.deepEqual(walk(join(tmpdir(), 'mts-walk-absent-' + process.pid), () => true), []);
});
