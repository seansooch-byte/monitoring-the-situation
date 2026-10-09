# Reply to grokbot after the side by side run

Sean pastes the block below to grokbot once. The durable parts are in `GRABBER.md` and `CAPTURE.md`.

---

Good run, and an honest one: you reported the new method losing on the biggest post instead of
tuning the test until it won. That is what makes the table usable. Here is what it says and what
to change.

**Reading your table by yield per read.**

| Source | Reads | Kept | Largest | Median | Median age |
|---|---|---|---|---|---|
| References (quote, reply, media source) | 0 extra | 11 | 39.9M | 994K | 35 h |
| Sensor accounts (one probe, mostly replies) | 1 | 2 | 1.7M | 1.2M | 14 h |
| Trend names, repost stream | 2 | 20 | 2.0M | about 90K | 3 h |
| Global quote stream | 1 | 6 | 463K | 278K | 12 h |
| Story clusters (the old method) | 7 | 28 | 5.3M | 93K | 15 h |
| Desk repost streams | 4 | 44 | 1.6M | 40K to 78K | 9 to 18 h |
| Global repost stream | 1 | 6 | 885K | 81K | 11 h |

Three things follow.

1. **References are the best source and cost nothing.** Following a post to what it quotes,
   replies to, or took its media from found bigger posts than any search did.
2. **The global repost stream was my main bet and it was the weakest.** One page is 25 reposts
   from a single minute, which is too small a sample of all of X. It works where the pool is
   narrow: trend names gave the freshest posts of the night.
3. **Nothing found the top of the distribution among fresh posts**, at 2 AM Eastern. The fastest
   post under three hours old was gaining 60,000 views an hour. That may be the hour and not the
   method, so it gets measured again in the evening before anything else is concluded.

**What changed in the repository.** Pull, then re-read these sections of `contract/GRABBER.md`:
Finding posts (reordered by the table above, with three new rules), Volume, Context on request,
and the daily scoreboard at the end of The read budget. The changes, in order of expected gain:

1. **Follow references further.** For every candidate, not only the posts you keep, and a second
   hop from each origin. Count how often each referenced post turns up across everything a run
   reads, screen the most pointed-at first, and put the count in `lead`.
2. **A pace floor for young posts.** A post under three hours old clears a floor if its views
   divided by its age in hours is at least a quarter of the floor's view count (25,000 an hour
   globally). A floor on totals was discarding the posts worth following before they had their
   views. A young post kept on pace joins the re-read list, which is how its rise gets measured.
3. **Sensors every second run**, with `-is:reply` and reposts left in, each repost followed to
   its origin. Your list in `capture/SENSORS.md` is the right shape. Prune it from results: after
   three days, drop any account that has produced nothing kept, and say what you dropped.
4. **All ten top United States trends**, not two. One repost-stream search per name that had no
   posts attached in the previous run. Attach the three biggest posts whatever their size.
5. **Shift global reads from the repost stream to the quote stream** (three quote, one repost),
   vary the common word between reads, and keep a tally across runs: a post seen in the stream
   in several of the last six runs outranks one seen once. Put the tally in `lead`.
6. **Desk repost streams: keep the five best per desk on pace, not everything.** 44 kept of 44
   says the screen was not screening.
7. **Flag old origins.** When a reference leads to a post more than a week older than its copy,
   capture it and set `old_content`. Your run surfaced a clip more than five months old behind a
   fresh re-upload; the editor has to know that before writing a word.

**Two one-time jobs, this run or the next.**

- **Backfill a week of volume for every desk.** One read returned 167 hours for politics. Nineteen
  more reads give the site a full week of hourly history on all twenty desks. You have the budget
  today (926 left). After that, three or four desks a run in rotation, as written. Leave out the
  partial first and last hours.
- **Save X's story text.** `x_stories` was empty in 0615Z for the right reason (you would not
  retype it). Save each `search_news` result to a file first and fill it from the file.

**Three probes, five reads or fewer, results under "Third probe" in `capture/CAPABILITIES.md`.**

- **A post's own history.** Does `get_posts_counts_recent` accept `retweets_of_tweet_id:<id>`,
  `quotes_of_tweet_id:<id>` and `conversation_id:<id>` as the query? If it does, one read gives a
  post's hour by hour spread since it was written, including the hours before anyone was watching.
  Try it on the pinned post's quoted post and on one post from today. If it works, do it for every
  post in `requests/watch.json` and record the series in `volume` (keys are in `CAPTURE.md`).
- **The best replies are the first ones.** Newest-first and relevancy both gave you replies with
  no likes. Try `conversation_id:<id> is:reply` with `end_time` set twenty minutes after the post
  was created. Do the most liked replies show up there?
- **Clean quote search.** `quotes_of_tweet_id:<id> -is:retweet` with the same early window. Does
  that leave only real quote posts?

**Measure it again where it counts.** Repeat the side by side in one run between 00:00 and 02:00
UTC tonight (United States evening), same table, in `capture/NOTES.md`. And start the daily
scoreboard described in The read budget: one line per day over all of that day's captures. The
gather is judged by the day, not by one run.

**The targets stand**, with two corrections from your run. The trend target is now three posts
attached to each of the top ten names. The media-source target is dropped: X only reports a source
when the account used X's own repost-video feature, so 6 of 26 is what there is. Where a post
credits someone in its text instead ("via", a camera emoji and a handle), put that handle in `lead`.

**Reads.** For the rest of today, up to 45 a run, plus the 19 for the backfill. From tomorrow the
table in `GRABBER.md` applies: up to 42 by day, 20 overnight, under 850 for the day.

**Carry on as you are with:** `not_found` when X has nothing, leaving out sexual and graphic
posts and saying that you did, describing the media on the top 25, and writing down what X
actually returned.

**Report back to Sean in six lines:** the three probes; whether the week of volume is in for all
twenty desks; the evening side by side headline (largest and median, per source); how many posts
under three hours old the pace floor let in and the fastest pace among them; reads used and left;
anything you need from him.
