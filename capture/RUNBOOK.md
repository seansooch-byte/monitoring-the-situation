# Hourly grabber runbook

Run at minute 05 of every hour (UTC). Read limits: 30 a minute, 1,000 a day from 00:00 UTC, shared
with the 7:03 AM Detroit daily briefing. Keep each run under 35 reads and under 25 in any one minute.
Stop discovery if the day has fewer than 150 reads left; watch and requests still run.

1. `git pull --rebase origin main`. Note `git log -1 --format=%H -- requests/` as `requests_rev`.
   Set `started_at` to the current UTC minute; run id and file name follow from it.
2. watch: ids from `requests/watch.json` plus every post id in captures from the last 24 hours.
   Read them with `get_posts_by_ids` (100 ids per call, full fields, `note_tweet` included). Each
   returned post gets an observation; `Not Found Error` drops the id; `Authorization Error` is an
   `unavailable` observation.
3. trends.us and trends.ww: `get_trends_by_woeid` 23424977 and 1. `post_count` and `story` are `null`.
4. viral.global: `search_news "viral"` and one or two broad queries, `max_age_hours` 24,
   `news.fields name,cluster_posts_results,updated_at`. Collect cluster ids.
5. rising.global: the same with `max_age_hours` 6.
6. Due desks, in desks.json order (`sweep_every_hours` 1: every run; 2: even hours; 4: hours
   divisible by 4): `search_news "<desk terms>"` with the same fields. Terms are in CAPABILITIES.md.
7. Screen every new candidate id with one `get_posts_by_ids` pass (100 per call). Keep posts inside
   the window that clear the floor; top 10 per desk, 40 viral, 20 rising, by exact views.
8. context.top: for the 5 biggest new posts, one page of replies (`conversation_id:<id> is:reply`)
   and one page of quotes (`get_posts_quoted_posts`, exclude retweets); keep the 3 most liked each.
   All 15 posts every third run if the day budget allows.
9. Requests in `requests/open.json` that no capture has answered yet: lookups by
   `get_posts_by_ids`; searches by `search_posts_all` (25 per page).
10. Final read: every kept record and context id in one or two `get_posts_by_ids` calls. Records and
   observations come only from this read; `at` is its time.
11. Build `capture/YYYY/MM/DD/HHMMZ.json`, set `finished_at`, run
    `node tools/check-capture.mjs <file>` until it prints PASS. A sweep that failed is `down` or
    `skipped` with a reason; the file is written anyway.
12. `git add capture/`, `git commit -m "capture: <runid> (N posts, M observations)"`,
    `git push origin main`; on rejection `git pull --rebase origin main` and push again.
13. Problems go to `capture/NOTES.md` as one dated line.

If a run is cut short, cut in this order: 4-hour desks, then 2-hour desks, then rising, context,
viral, trends. Never cut watch.
