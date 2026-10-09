#!/usr/bin/env bash
# Publish a briefing JSON to the live feed: ./publish.sh path/to/briefing.json
# Needs only the write secret (no Cloudflare token). Override with env vars if needed.
set -euo pipefail

json="${1:?usage: publish.sh <briefing.json>}"
secret_file="${FEED_WRITE_SECRET_FILE:-/path/to/monitor-feed-write-secret}"
endpoint="${FEED_ENDPOINT:-https://feed.seansooch.dev/v1/feed}"

[ -r "$json" ] || { echo "cannot read $json" >&2; exit 1; }
[ -r "$secret_file" ] || { echo "cannot read secret file $secret_file" >&2; exit 1; }
python3 -I -c 'import json,sys; json.load(open(sys.argv[1]))' "$json" || { echo "$json is not valid JSON" >&2; exit 1; }

# Secret goes to curl through a header file on stdin, so it never appears in argv / ps.
resp="$(mktemp)"; trap 'rm -f "$resp"' EXIT
code="$(printf 'Authorization: Bearer %s\n' "$(tr -d '\r\n' < "$secret_file")" |
  curl -sS -o "$resp" -w '%{http_code}' -X PUT \
    -H @- -H 'Content-Type: application/json' \
    --data-binary @"$json" "$endpoint")"

if [ "$code" = 204 ]; then
  echo "published $json -> $endpoint (204)"
else
  echo "publish failed: HTTP $code" >&2; cat "$resp" >&2; echo >&2; exit 1
fi
