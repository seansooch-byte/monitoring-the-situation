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

# A status code proves nothing; compare what is live with what was built.
sleep 5
LIVE=$(curl -fsSL "https://$HOST/?v=$(date +%s)" | grep -o 'id="asof" datetime="[^"]*"' | head -1 || true)
if [ "$LIVE" = "$STAMP" ]; then echo "live: https://$HOST serves this build"; else echo "NOT VERIFIED: live says '$LIVE', build says '$STAMP' (a new hostname can take a few minutes; check again before trusting it)"; exit 1; fi
