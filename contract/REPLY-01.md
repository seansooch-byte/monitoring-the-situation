# Reply to grokbot after the first capture

Sean pastes the block below to grokbot once. The durable parts are in `GRABBER.md` and `CAPTURE.md`.

---

The first capture did its job, and it showed exactly where the next gain is. This message is about
making the gather five to ten times better. The site build does not need to finish first.

**What you got right, and should keep doing.** Exact numbers on every post. A capture that passed
the checker on the first push. All twenty desks attempted. Twenty posts flagged for showing private
people and five for minors. A capabilities report written from what happened, not from
documentation. And `not_found` on request r-02: that post does not exist, and saying so was the
right answer. Some lookups will go on being for posts that do not exist.

**The gap, in numbers from your own file.**

- The 153 posts you discovered add up to 38.2 million views. The site's pinned post has 39.4
  million by itself. The capture missed the top of the distribution completely.
- The biggest post had 3.35 million views. None reached 5 million. The median was 95,000, and 79
  of the 153 were under 100,000.
- The median post was 12 hours old. Only 12 were under 6 hours old, and `rising.global` found nothing.
- 40 trends were listed and none had a post attached.
- 34 posts came from aggregator accounts, 17 of them video, and none was traced to its origin.
- 2 of 116 media items were described. The editor cannot see media.

**The cause is one thing.** Every candidate came from X's story clusters. Those find what X has
already filed as news, hours after it started. This site is about what people are passing around
right now. You said so yourself in the capabilities report; this is the fix.

**What changed in the repository.** Pull, then read these sections of `contract/GRABBER.md`, which
are new or rewritten: Finding posts, Volume, Media and links, Context on request, The read budget,
Re-reads. In short:

1. **Sample the repost stream.** Search for reposts, newest first. Each result carries the post
   being reposted, so one read returns up to 25 posts weighted by how fast they are spreading this
   minute. That is the "sort by engagement" that search does not offer. The same with quote posts
   finds what is being argued about.
2. **Follow every reference.** The post being quoted or replied to, and the post a clip was first
   attached to (`attachments.media_source_tweet_id`, recorded in the new `media_source` field).
   That is how an aggregator's copy leads to the origin.
3. **Attach posts to trends.** One repost-stream search per top ten United States trend.
4. **Sensor accounts.** One search can name many accounts. Keep a list per desk group and read
   each group in one call.
5. **Story clusters stay**, as one source of five, and X's own story text goes in the new
   `x_stories` array.

Also new: `volume` (hourly post counts per desk from `get_posts_counts_recent`, which will drive
the site's main chart), media descriptions for the top 25 posts of every capture, link cards
recorded as `link` media, replies and quotes fetched on request instead of by default, and a read
budget that spends more during United States waking hours and less overnight.
`contract/CAPTURE.md` documents the three additions (`media_source`, `x_stories`, `volume`); all
are optional and the checker accepts them now.

**Do these in order.**

1. **Probe, once, in 15 reads or fewer.** Try each of these and write what X actually returned
   into `capture/CAPABILITIES.md` under a new heading, "Second probe":
   - A repost-stream search (a common word, `lang:en is:retweet`, newest first). Does the post
     being reposted come back with its full numbers? How many distinct originals in one page?
   - The same with `is:quote`.
   - `attachments.media_source_tweet_id` on three aggregator video posts from your first capture.
     Does it name a source post?
   - One search naming ten or more accounts with `from:`. How long can the query be?
   - `get_posts_counts_recent` for one desk query, hourly. How many hours come back, and does it
     cost one read?
   - Replies to one big post in `relevancy` order against newest first. Which page has more likes
     in it? Does a quote operator on the post id (`quotes_of_tweet_id:`) work?
   If X rejects something, write down its exact words and move on. Do not build on anything the
   probe did not confirm.

2. **Run both methods side by side for one run.** In the same hour, gather with the old method
   (story clusters only) and with the new sources. In `capture/NOTES.md`, one line per source:
   reads spent, candidates found, posts kept, the largest and the median views among those kept,
   and their median age in hours. That table is how the improvement is measured, so report it
   even where the new method loses.

3. **Write `capture/SENSORS.md`.** Up to twenty accounts for each of the six desk groups, chosen
   from accounts that showed up in your own captures and others you can justify. For each: the
   handle, the desks it serves, whether it mostly posts its own material or reposts other
   people's, and one line on why it is there. The editor will edit this list through requests.

4. **Fix the standing query for the weak desks.** World, gaming, ideas, life, medicine and
   internet returned little. Rebuild their terms from the beats in `contract/desks.json` and list
   every desk's standing query in the capabilities report. These queries also feed `volume`, so
   once set they should not drift.

5. **Carry on hourly with the new method.** One file per run, always. The re-read list is bounded
   (see Re-reads) so it fits in four reads.

**What a good daytime run looks like.** These are targets for a United States daytime or evening
hour, not floors to be met by padding:

- the biggest post is over 10 million views, and at least ten are over 1 million;
- the median kept post is over 300,000 views;
- at least fifteen posts are under three hours old;
- each of the top ten United States trends has at least one post attached;
- at least half of the aggregator video posts have a `media_source`, and that source post is captured;
- the 25 most viewed posts have their media described;
- three or four desks have a fresh `volume` series.

When a run misses one, say which and why in `run.reason`. A short, true capture is still better
than a padded one, and every honesty rule in `GRABBER.md` stands unchanged: only what X returned
in this run, `null` over a guess, verbatim text, failure recorded as data.

**Answers to what you asked.**

- One file per run, always. The bounded re-read list is what keeps it within the caps.
- `npm test` now runs on older Node. Pull and it will pass.
- The hourly schedule should keep running. Pushing commits that touch only `capture/` to this
  repository's main branch is the job you were given; Sean approves that as a standing matter.
- The four beats you asked for are in `contract/desks.json` (`world`: protests, migration;
  `internet`: fandom; `life`: habits).
- The pinned post is in `requests/watch.json` and has a lookup open (r-2026-10-09-05).

**Report back to Sean in six lines:** which probes worked and which X rejected; the side by side
table's headline (largest and median views, old method against new); the reads the new run used;
which targets the run met; where `SENSORS.md` is; anything you need from him.
