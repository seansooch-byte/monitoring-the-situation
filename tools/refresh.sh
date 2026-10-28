#!/bin/sh
# The hourly refresh. No model runs here: it asks X about any post not yet checked, records the
# answers, writes the next run's read plan, commits both, and ships, so the numbers on the site
# follow the newest capture and the grabber's next run has its list.
#
#   tools/refresh.sh        run after a capture has been pushed
#
# It writes two files: verified/posts.json, only through tools/verify-posts.mjs, and
# requests/plan.json, only through tools/plan-reads.mjs.
set -eu
cd "$(dirname "$0")/.."
export PATH="/usr/local/bin:$PATH"

if [ -n "$(git status --porcelain)" ]; then echo "refusing: the tree has uncommitted changes"; git status --short; exit 1; fi
git pull -q --rebase origin main

node tools/verify-posts.mjs --captures | tail -8 || true   # a post X could not confirm is recorded, not fatal
node tools/plan-reads.mjs || echo "plan: the planner failed; the grabber follows the standing orders this hour"
if [ -n "$(git status --porcelain -- verified/posts.json requests/plan.json)" ]; then
  git add verified/posts.json requests/plan.json
  git -c user.name="${GIT_AUTHOR_NAME:-seansooch-byte}" -c user.email="${GIT_AUTHOR_EMAIL:-seansooch@gmail.com}" \
    commit -q -m "refresh: X's answers for the newest capture, and the next run's plan"
  git push -q origin main || { git pull -q --rebase origin main && git push -q origin main; }
fi

./tools/ship.sh
