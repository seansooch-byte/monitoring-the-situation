# Hourly grabber runbook

Rewritten 2026-10-09 (run 2026-10-09T0629Z) for the source order, pace floor, reference counts,
old_content rule, volume and scoreboard in contract/GRABBER.md at 874ebe0. If this file and the
contract disagree, the contract is right; note the conflict in capture/NOTES.md.

## Budget

- The X day runs 00:00 to 24:00 UTC (8 PM to 8 PM Eastern). 1,000 reads a day, 30 a minute,
  shared with the 7:03 AM Eastern daily briefing. Stay under 850 a day.
- Rest of 2026-10-09 (UTC): up to 45 reads a run, plus 19 once for the desk backfill (done in
  run 2026-10-09T0629Z).
- From 2026-10-10: the table in contract/GRABBER.md: up to 42 a run 12:00 to 05:00 UTC, up to 20 a
  run 06:00 to 11:00 UTC, under 850 a day. Never more than 25 in one minute.
- Every tool output ends with "X reads left ... today". Write the number at the start and end of
  the run into the capture's run.reason or capture/NOTES.md. If fewer than 150 are left, run
  only watch, requests and trends.

## Steps

1. `git pull --rebase origin main`. `requests_rev` is `git log -1 --format=%H -- requests/`.
   `started_at` is the current UTC minute; run id and file name follow from it.
2. **Save everything.** Every X output goes to a file in the work folder before it is used. An
   output that comes back inline (small results) gives ids only: transcribe ids and reference
   edges, then read the records by id (a by-id read of many ids comes back as a file). Never
   retype text, names or numbers. Counts are the exception: transcribe them and check the sum
   against `meta.total_tweet_count`.
3. **Watch** (about 4 reads): `requests/watch.json` plus every post first captured in the last
   6 hours, then the slower re-read tiers in contract/GRABBER.md. `get_posts_by_ids`, 100 a call,
   fields `created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,
   note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive`, expansions
   `author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id`.
4. **Trends** (1 to 2 reads): `get_trends_by_woeid` 23424977 and 1.
5. **Trend names** (up to 5 reads): one `"<name> lang:en is:retweet"` newest first for each of
   the top ten US names that had no posts attached in the previous run. Attach the three biggest
   posts per name (from those streams and from an exact name match in any post read this run),
   whatever their size. When several names are one event, say so in the trends sweep reason.
6. **Sensors** (3 reads a run): every group of capture/SENSORS.md at least every second run, three
   groups a run in rotation (news, money, science; then culture, sports, online). Query
   `(from:a OR from:b ...) -is:reply`, newest first, 25 results; reposts stay in and are followed
   to their origin. Prune per the clock in SENSORS.md.
7. **Global streams** (4 reads): three quote-stream reads and one repost-stream read, newest
   first, 25 each: `<word> lang:en is:quote -is:retweet` and `<word> lang:en is:retweet`. Rotate
   the common word, never the same word twice in a row: the, this, is, you, and, my, it, that,
   just, what. Record the word used in the sweep method.
8. **Tally**: add this run's quoted and reposted originals from step 7 to `capture/TALLY.json`
   (`runs[]` of `{run, origins}`; keep the last 6 runs only). In `lead`, write "seen in the quote
   or repost stream in N of the last 6 runs". A post seen in several of the last six outranks one
   seen once when screening.
9. **Story clusters** (up to 3 reads): `search_news` for the global sweeps and the hourly desks.
   Fill `x_stories` only from a saved file; if the output came back inline, leave `x_stories`
   empty and say so in the stories sweep.
10. **Due desks** (up to 10 reads): `<standing query> lang:en is:retweet -is:reply` from
    CAPABILITIES.md, newest first. Keep at most the five best per desk by the pace rule.
11. **References** (0 to 2 reads): for every post read in steps 3 to 10, follow `quoted`,
    `replied_to`, `retweeted` and `attachments.media_source_tweet_id`, then follow the origins a
    second hop. Count distinct posts pointing at each referenced post. Read the unread ones by id,
    most pointed-at first; a count of 2 or more goes in `lead` ("pointed at by N posts read this
    run").
12. **Screen** (about 3 reads): every candidate by id. Age is measured at the time of the read that
    gave its numbers.
    - Global: under 24 hours and 100,000 views or 2,000 likes; under 3 hours old, views divided
      by age in hours of at least 25,000.
    - Desk: the desk's floor in contract/desks.json; under 3 hours old, a quarter of
      `floor.views` per hour.
    - A young post kept on pace joins the next runs' re-read list, and its lead says the pace.
    - **Old origins**: a referenced post more than 7 days older than the post that led to it is
      captured with the `old_content` flag, whatever its size.
    - **Credits**: a "via @handle" or "📽️ @handle" in the text goes in `lead` as "credits @handle".
13. **Volume** (up to 4 reads):
    - Desks: one `get_posts_counts_recent` a desk every 6 hours, 3 or 4 desks a run in desks.json
      order, `<standing query> lang:en`, granularity hour, `start_time` and `end_time` on whole
      hours so there is no partial first or last hour. Record all 167 full hours (key
      `desk.<desk>`).
    - Trends: the top five US names, `"<name>"`, key `trend.us.<name>`, when the budget allows.
    - Posts: `retweets_of_tweet_id:<id>`, `quotes_of_tweet_id:<id>` and `conversation_id:<id>`,
      keys `post.<id>.reposts|quotes|replies`, `desk` null. Three reads per post, so rotate:
      about 4 posts' series a day, oldest refresh first, each refreshed every 6 hours while on
      the watch list only when the day has more than 300 reads left. Only full hours.
14. **Context and requests** (about 3 reads): `context.top` for the three biggest new posts and
    each `context` request: `conversation_id:<id> is:reply` and
    `quotes_of_tweet_id:<id> -is:retweet`, relevancy, `start_time` at the post and `end_time` 20
    minutes later (the two hour window only returns the newest posts inside it). Keep the five
    most liked of each kind. Then the open requests.
15. **Media**: for the 25 most viewed posts and every watch post, download each image or video
    preview (`?name=small`), look at it, and write one plain sentence in `media[].description`.
    Skip sexual or graphic posts entirely and name the skipped ids in `run.reason`.
16. **Build** `capture/YYYY/MM/DD/HHMMZ.json`, set `finished_at`, run
    `node tools/check-capture.mjs <file>` until PASS.
17. `git pull --rebase origin main`, `git add capture/`, commit
    `capture: <runid> (N posts, M observations)`, `git push origin main`. Only `capture/` paths.
    If the harness blocks the push, stop and report the block text.
18. One dated line in capture/NOTES.md for anything wrong or new.

Cut order when short: 4-hour desks, 2-hour desks, story clusters, trend volume, per-post
volume, context, rising, viral, trends. Never cut watch.

## Daily scoreboard

In the last run before 00:00 UTC, append one line under "Daily scoreboard" in capture/NOTES.md
for the UTC day, counted over all that day's captures with duplicates removed:
reads used (1,000 minus the reads left after the run); posts kept; posts over 1M, 5M and 10M views
at their last reading; largest; median; median age at first capture; largest and median per
source (references, sensors, trend names, quote and repost streams, story clusters, desk streams,
context and requests). Until then keep a running partial line for the day and replace it.

## Evening side-by-side (run once, between 00:00 and 02:00 UTC)

Sean schedules this; the grabber never creates the schedule. It measures the source ranking at a
busy hour (8 to 10 PM Eastern) to compare with the night run 2026-10-09T0615Z.

1. Start from step 1 above. The X day has just reset, so the run may spend up to 42 reads.
2. Read every source once, in this order, and save each output to a file named by source:
   - references (free: they ride on the watch and screening reads),
   - three sensor groups (news, sports, culture),
   - trend names: repost streams for the top five US names,
   - global streams: two quote reads (`the`, `this` with `lang:en is:quote -is:retweet`) and one
     repost read (`the lang:en is:retweet`),
   - story clusters: `search_news "viral"` with `max_age_hours` 24, plus the hourly desks
     (politics, entertainment, sports, internet) by `search_news "<desk>"`,
   - desk repost streams for the same four hourly desks.
3. Screen every candidate in one or two by-id passes (100 a read) with the pace rule, and keep
   by the normal rules; one capture file for the run as usual.
4. For each source, count: reads it cost; candidates (distinct originals under 24 hours after
   spam screening); kept; largest views; median views; median age in hours at first reading.
   A post found by several sources counts for each of them.
5. Append to capture/NOTES.md, under a dated heading "Evening side-by-side <run id>", this table,
   one row per source, then one line comparing it with the night run (overlap of kept ids, which
   source found the biggest fresh post, and whether the ranking in contract/GRABBER.md holds):

   | Source | Reads | Candidates | Kept | Largest | Median | Median age (h) |
   |---|---|---|---|---|---|---|

6. Check, pull with rebase, commit only `capture/`, push.
