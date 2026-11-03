// The staleness alarm: the live page's as-of time, against the clock. The verdict is a pure
// function; the command line is tested against a local server, never the real site.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { createServer } from 'node:http';
import { fileURLToPath } from 'node:url';
import { asOfFrom, staleness } from '../tools/check-stale.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const MIN = 60000;
const page = (iso) => `<p class="lab asof">As of <time id="asof" datetime="${iso}">14:15 ET · Tue 3 Nov 2026</time></p>`;
const AT = Date.parse('2026-11-03T18:15:20.000Z');

test('the as-of time is read from the page as the build writes it', () => {
  assert.equal(asOfFrom(page('2026-11-03T18:15:20.000Z')), AT);
  assert.equal(asOfFrom('<time datetime="2026-11-03T18:15:20.000Z" id="asof">x</time>'), AT);
});

test('a page read within the limit is fresh, with its age in minutes', () => {
  const v = staleness(page('2026-11-03T18:15:20.000Z'), AT + 42 * MIN);
  assert.equal(v.code, 0);
  assert.equal(v.line, 'FRESH: as of 2026-11-03T18:15:20Z (42 min old)');
  assert.equal(staleness(page('2026-11-03T18:15:20.000Z'), AT + 180 * MIN).code, 0, 'the limit itself is still fresh');
  assert.equal(staleness(page('2026-11-03T18:15:20.000Z'), AT - 5 * MIN).age, 0, 'a clock behind the page is not a negative age');
});

test('a page older than the limit is stale, on one line that says how old', () => {
  const v = staleness(page('2026-11-03T18:15:20.000Z'), AT + 35 * 60 * MIN);
  assert.equal(v.code, 1);
  assert.match(v.line, /^STALE: as of 2026-11-03T18:15:20Z, 2100 min old \(35\.0 h\), over the 180 min limit$/);
  assert.equal(staleness(page('2026-11-03T18:15:20.000Z'), AT + 61 * MIN, 60).code, 1, 'the limit can be set');
});

test('a page with no as-of time, or a malformed one, is NOASOF and never fresh', () => {
  for (const html of ['', '<html><body>Bad gateway</body></html>', page('yesterday'), page('2026-13-45T99:99:99Z'), page('2026-11-03 18:15'), '<time id="asof">14:15 ET</time>']) {
    const v = staleness(html, AT);
    assert.equal(v.code, 2, html);
    assert.match(v.line, /^NOASOF:/);
  }
});

const cli = (...args) => new Promise((done) => execFile('node', ['tools/check-stale.mjs', ...args], { cwd: root, encoding: 'utf8' }, (e, stdout) => done({ code: e ? e.code : 0, out: stdout.trim() })));

test('the command line exits 0, 1 or 2 with one line, and gives up on a page that will not load', async () => {
  const now = new Date(Date.now() - 10 * MIN).toISOString();
  const old = new Date(Date.now() - 10 * 60 * MIN).toISOString();
  const server = createServer((req, res) => {
    if (req.url === '/fresh') return res.end(page(now));
    if (req.url === '/old') return res.end(page(old));
    if (req.url === '/none') return res.end('<html></html>');
    res.statusCode = 503; res.end('down');
  });
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  try {
    let r = await cli(`${base}/fresh`);
    assert.equal(r.code, 0); assert.match(r.out, /^FRESH: as of \S+ \(10 min old\)$/);
    r = await cli(`${base}/old`);
    assert.equal(r.code, 1); assert.match(r.out, /^STALE: /);
    r = await cli(`${base}/old`, '--max-minutes', '900');
    assert.equal(r.code, 0, 'the limit is taken from --max-minutes');
    r = await cli(`${base}/none`);
    assert.equal(r.code, 2); assert.match(r.out, /^NOASOF: /);
    r = await cli(`${base}/down`);
    assert.equal(r.code, 2); assert.match(r.out, /^UNREACHABLE: .* answered 503$/);
  } finally {
    server.close();
  }
  const r = await cli('http://127.0.0.1:1/');
  assert.equal(r.code, 2); assert.match(r.out, /^UNREACHABLE: /);
});
