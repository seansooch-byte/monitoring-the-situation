#!/bin/sh
# The hourly refresh. No model runs here: it asks X about any post not yet checked, records the
# answers, and ships, so the numbers on the site follow the newest capture.
#
#   tools/refresh.sh        run after a capture has been pushed
#
# It writes one file, verified/posts.json, and only through tools/verify-posts.mjs.
set -eu
cd "$(dirname "$0")/.."
export PATH="/usr/local/bin:$PATH"

if [ -n "$(git status --porcelain)" ]; then echo "refusing: the tree has uncommitted changes"; git status --short; exit 1; fi
git pull -q --rebase origin main

node tools/verify-posts.mjs --captures | tail -8 || true   # a post X could not confirm is recorded, not fatal
if [ -n "$(git status --porcelain -- verified/posts.json)" ]; then
  git add verified/posts.json
  git -c user.name="${GIT_AUTHOR_NAME:-seansooch-byte}" -c user.email="${GIT_AUTHOR_EMAIL:-seansooch@gmail.com}" \
    commit -q -m "verified: X's answers for the newest capture"
  git push -q origin main || { git pull -q --rebase origin main && git push -q origin main; }
fi

./tools/ship.sh
