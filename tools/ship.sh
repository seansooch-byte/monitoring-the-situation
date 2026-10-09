#!/bin/sh
# Ship the site. Refuses anything that is not a tested build of a committed tree.
#
#   tools/ship.sh            test, build, deploy, check what is live
#   tools/ship.sh --check    everything except the deploy
set -eu
cd "$(dirname "$0")/.."
export PATH="/usr/local/bin:$PATH"
HOST="situation.seansooch.dev"

if [ -n "$(git status --porcelain)" ]; then echo "refusing: the tree has uncommitted changes"; git status --short; exit 1; fi
npm test >/dev/null 2>&1 || { echo "refusing: tests fail (run npm test)"; exit 1; }
node tools/verify-posts.mjs --captures >/dev/null 2>&1 || true   # ask X about anything new; the build decides what counts
if [ -n "$(git status --porcelain)" ]; then echo "refusing: checking new posts changed verified/posts.json; commit it first"; exit 1; fi
node tools/build.mjs
[ ! -e dist/DEMO ] || { echo "refusing: dist/ was built from invented data"; exit 1; }
[ ! -e dist/.wrangler ] || { echo "refusing: wrangler files inside dist/"; exit 1; }
STAMP=$(grep -o 'id="asof" datetime="[^"]*"' dist/index.html | head -1)
[ -n "$STAMP" ] || { echo "refusing: the build has no as-of time"; exit 1; }
echo "built $(find dist -type f | wc -l | tr -d ' ') files, $STAMP, commit $(git rev-parse --short HEAD)"

if [ "${1:-}" = "--check" ]; then echo "check only: not deployed"; exit 0; fi

npx --yes wrangler@latest deploy

# A status code proves nothing; compare what is live with what was built, file by file.
# A release takes some seconds to reach every edge, so look up to four times before calling it a failure.
ok=no
for wait in 8 12 15 20; do
  sleep "$wait"
  if node tools/audit-live.mjs "https://$HOST" > /tmp/mts-audit.txt 2>&1; then ok=yes; break; fi
done
tail -3 /tmp/mts-audit.txt
[ "$ok" = yes ] || { echo "NOT VERIFIED: the live site still differs from this build after a minute; run node tools/audit-live.mjs"; exit 1; }
echo "live: https://$HOST serves commit $(git rev-parse --short HEAD)"
