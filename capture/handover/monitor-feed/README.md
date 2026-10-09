# monitor-feed

Cloudflare Worker behind **https://feed.seansooch.dev** that serves the latest
"Monitoring the Situation" briefing for the `/monitor/` page on seansooch.dev.
The page fetches the feed at runtime, so a new briefing goes live without redeploying the site.

- Worker: `monitor-feed` (no workers.dev route, no preview URLs), Workers Custom Domain `feed.seansooch.dev`
- KV: namespace `monitor-feed` (`e86dcd02d9064b5cbd8e70ff06ab8f77`), bound as `FEED`
  - `latest`: current briefing (metadata: `etag`, `generated_at`, `stored_at`)
  - `prev`: the briefing that was `latest` before the last publish
  - `archive:YYYY-MM-DD`: one per day (date from `generated_at`), expires after 30 days
- Secret: `FEED_WRITE_SECRET` (Worker secret; local copy in the agent secrets dir, mode 0600)

## Endpoints

| Method | Path | Notes |
|---|---|---|
| GET/HEAD | `/` | `{"name":"monitor-feed","feed":"/v1/feed.json","version":1}` |
| GET/HEAD | `/v1/feed.json` | Latest briefing. `Cache-Control: public, max-age=60, stale-while-revalidate=600, stale-if-error=86400`, `ETag` (304 on `If-None-Match`), `X-Content-Type-Options: nosniff`. 503 `{"error":"no feed yet"}` if nothing published. |
| OPTIONS | `/`, `/v1/feed.json` | CORS preflight |
| PUT | `/v1/feed` | `Authorization: Bearer <FEED_WRITE_SECRET>`. Body ≤ 256 KB, validated. 204 on success; 401 bad/missing secret, 400 bad JSON/schema, 413 too big. |

Anything else: 404 for unknown paths, 405 for a wrong method on a known path.

CORS: `Access-Control-Allow-Origin` is echoed only for `https://seansooch.dev` and
`https://sean-sooch-portfolio.pages.dev`; every response varies on `Origin`.

### Briefing schema

```json
{
  "version": 1,                       // optional on PUT, added if missing
  "generated_at": "2026-10-08T07:06:47-04:00",   // ISO 8601 with timezone
  "sections": [
    { "name": "Finance/markets",
      "items": [
        { "headline": "…", "summary": "…",
          "links": [ { "label": "CNBC", "url": "https://…" } ],   // https only, 1-20
          "source_type": "x" | "web" | "both" } ] } ]
}
```

Unknown fields are dropped. Limits are in `LIMITS` in `src/index.js`.

## Publish a briefing

```sh
./publish.sh /workspace/briefings/2026-10-08.json
```

Uses only the write secret file (no Cloudflare token). Override with
`FEED_WRITE_SECRET_FILE=…` or `FEED_ENDPOINT=…`. The secret is sent to curl on stdin,
never on the command line. Browsers see the new briefing within ~60 s (KV `cacheTtl`
+ `max-age`).

## Test

```sh
export PATH=/home/box/.local/node22/bin:$PATH
npm install --legacy-peer-deps   # npm 10 trips on vitest peer deps without it
npm test                         # vitest + @cloudflare/vitest-pool-workers (local workerd, no network)
```

## Redeploy

```sh
export PATH=/home/box/.local/node22/bin:$PATH
export CLOUDFLARE_API_TOKEN=…   CLOUDFLARE_ACCOUNT_ID=<account id>
npx wrangler deploy
```

`compatibility_date` is capped by the bundled workerd (2026-08-22 at wrangler 4.148.0).

## Rotate the write secret

```sh
umask 077
openssl rand -hex 32 > "$SECRET_FILE"          # new secret
tr -d '\r\n' < "$SECRET_FILE" | npx wrangler secret put FEED_WRITE_SECRET   # needs CF token
```

The old secret stops working as soon as `secret put` finishes; update any other
publisher that holds a copy.
