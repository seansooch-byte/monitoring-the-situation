# Handover

- `monitor-feed/`: source, wrangler config, package.json, README and publish.sh of the Worker behind
  feed.seansooch.dev, copied 2026-10-09. Secrets removed: the write secret file path in publish.sh
  and the Cloudflare account id in the README are placeholders. No secret or token is in these files;
  the Worker reads `FEED_WRITE_SECRET` from its own secret store. Tests (`test/`) are not copied.
- `briefing/PROMPT.md`: the daily briefing routine prompt, verbatim.
- `briefing/build_2026-10-08.py`: the script that built the 2026-10-08 briefing JSON.
- `briefing/SOURCES.md`: what is known about the X queries and accounts behind that briefing.
