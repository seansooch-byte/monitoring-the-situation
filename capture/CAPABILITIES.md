# Grabber capabilities

Written 2026-10-09 from what happened when I tried each thing on that day (run 2026-10-09T0552Z
and the test calls just before it). Exact = the number or text comes straight from X. Approximate =
X gives something close. Not at all = I could not get it.

## How I read X

- Agent: Grok Bot (agent id `grokbot`). Model: Grok Bot.
- Tool: the `x` MCP namespace, which wraps the X API v2 for read only. Tools used: `get_posts_by_ids`,
  `get_posts_by_id`, `search_posts_all`, `search_news`, `get_trends_by_woeid`,
  `get_posts_quoted_posts`. Also available but not needed yet: `get_posts_reposted_by`,
  `get_posts_counts_recent`, `get_users_by_username(s)`, `get_users_posts`, `get_users_mentions`,
  `get_news`.
- Every call reports the reads left for this user (per minute and per day).
- Big results (over about 40 KB) are saved to a file on the box, so I can parse post text with a
  script instead of retyping it. Small results come back inline only.

## One post

| Field | Result |
|---|---|
| id | Exact (string). |
| creation time | Exact, `created_at` with milliseconds; agrees with the id. |
| full text | Exact. Long posts come back in `note_tweet.text` when `note_tweet` is requested; `text` alone is cut near 280 characters. HTML entities come back as X sends them (`&amp;`, `&gt;`) and are copied as is. |
| author handle, display name | Exact (`author_id` expansion). |
| follower count | Exact (`public_metrics.followers_count`). |
| verification type | Exact: `verified_type` is `blue`, `business`, `government` or `none`. Seen all four. |
| views | Exact (`impression_count`). |
| likes, reposts, quotes, replies, bookmarks | Exact (`like_count`, `retweet_count`, `quote_count`, `reply_count`, `bookmark_count`). So `approx` is always `false`. |
| language | Exact (`lang`), X's own guess (`zxx` for media only, `und` when unsure). |
| quoted / replied-to id | Exact (`referenced_tweets`), and the referenced post itself comes back in `includes` with its text and author. |
| community note text | Not at all. The `community_note` field is rejected by X ("X does not accept some values sent for post.fields") and nothing else carries notes. `note` is always `null`. |
| media type | Exact: `photo`, `video`, `animated_gif` (mapped to `gif`), with video `duration_ms` and `alt_text` when set. |
| see the media | Partly. Photo urls and video preview images (`url`, `preview_image_url`) download to the box and I can look at them; tested on two. Video content itself I cannot watch, only its thumbnail frame. In the first capture only those two have a `description`; the rest are `null`. Describing every photo costs about one extra step per post. |
| link cards | Expanded url, title and description are in `entities.urls`. Not put in `media` yet because the contract's `link` type is for a link attachment and X does not mark which url is the card. |

## Fetch by id

- `get_posts_by_ids` takes up to 100 ids per call (the 25 cap does not apply). 174 ids took 2 calls
  that finished within about 15 seconds of each other, run in parallel.
- A deleted id and an id that never existed return the same thing: `Not Found Error` (`resource-not-found`).
  Tested on 2107854088614357910 (request r-02), on an id one off a real post, and on
  1000000000000000001. I cannot tell deleted from never existed, so I never write `state: deleted`;
  such an id gets `not_found` in answers and is dropped from re-reads.
- A protected or suspended post returns `Authorization Error` (seen on 2108333915023044929, a post
  someone quoted). That maps to `state: unavailable`.

## Trends

- US (woeid 23424977) and worldwide (woeid 1): yes, 20 names each, in order, so rank is exact.
- Post counts: not at all. Asking for `tweet_count` or `post_count` is rejected, so `post_count` is `null`.
- X's own story text and link for a trend: not at all through the trends tool. X stories exist
  separately (`search_news`: name, hook, summary, category, url `https://x.com/i/trending/<id>`, and
  about 10 cluster post ids when `news.fields` asks for `cluster_posts_results`), but nothing links a
  trend name to a story, so `story` is `null` and I do not guess the match.

## Search

Query syntax that works in `search_posts_all`:

- Time window: `start_time` / `end_time` parameters (ISO UTC). Exact.
- Language: `lang:en` together with a keyword (operators like `lang:`, `is:`, `has:` cannot stand alone).
- Phrases and exclusions: `"monitoring the situation" -is:retweet`.
- Replies of one post: `conversation_id:<id> is:reply`.
- Minimum likes or views: not at all. `min_faves:` is rejected ("Operator is not available in current
  product") and there is no views operator.
- Sort by engagement: not at all. `sort_order` is only `recency` or `relevancy`, and relevancy
  returned near zero engagement posts.
- Max 25 results per search or list call (the tool lowers 100 to 25), with a next token for more.

What I do instead for "most viewed": `search_news` (X stories for a topic, `max_age_hours` 24, or
6 for rising) gives about 10 post ids per story; I read those ids in bulk with `get_posts_by_ids` and
keep the ones over the floor by their exact views and likes. This finds the posts X has clustered
into stories. It misses big posts that are not part of any X story.

## Replies and quotes by likes

- Quotes: `get_posts_quoted_posts` with `exclude: retweets`, 25 per call, newest first.
- Replies: `search_posts_all` `conversation_id:<id> is:reply`, 25 per call, newest first.
- Neither sorts by likes. I sort by likes within the page I read, so "most liked" is approximate
  (only within the most recent 25). Pages beyond the first cost one call each.

## The twenty desks

Method for every desk: `search_news "<terms>"` with `max_age_hours` 24 and
`news.fields name,cluster_posts_results,updated_at`, then screen the cluster posts by exact views and
likes against the desk floor, created in the last 24 hours, keep the top 10 by views.
Result = posts that cleared the floor on 2026-10-09 / posts kept.

| Desk | Terms | Stories | Result | Notes |
|---|---|---|---|---|
| politics | US politics Trump Congress | 4 | 7 / 7 | Clusters dominated by one story. |
| world | world war diplomacy protests | 4 | 2 / 2 | Thin; X stories here skewed to opinion posts. Weak desk. |
| defense | military Pentagon weapons | 4 | 8 / 8 | Good. |
| justice | trial verdict arrest police | 4 | 10 / 10 | Good. |
| disaster | hurricane storm earthquake fire | 4 | 14 / 10 | Good when an event is live. |
| markets | stock market Treasury yields oil | 3 | 12 / 10 | Good. |
| business | company CEO layoffs deal | 3 | 13 / 10 | Good. |
| crypto | bitcoin crypto | 3 | 9 / 9 | Good. |
| ai | AI model OpenAI Anthropic | 3 | 6 / 6 | Fair. |
| tech | Apple Google software outage hack | 3 | 15 / 10 | Good. |
| science | NASA space launch science discovery | 3 | 17 / 10 | Good, but AI-adjacent posts leak in. |
| medicine | health medicine FDA doctors vaccine | 3 | 5 / 5 | Fair. Few clinical posts reach 10k views. |
| entertainment | movie TV show celebrity | 3 | 14 / 10 | Good. |
| music | music album song tour | 3 | 6 / 6 | Fair. Fan accounts outweigh artists. |
| gaming | video game gaming | 3 | 3 / 3 | Weak by its own terms; most gaming posts came through the internet query (7 Wuthering Waves posts, filed under gaming). |
| ideas | books history art philosophy religion | 3 | 3 / 3 | Weak. Few stories, low reach. |
| sports | NFL MLB playoffs NBA game | 4 | 17 / 10 | Good, but one game dominates; beats outside the game of the night are missed. |
| internet | meme streamer creator main character | 3 | 9 / 9 | Fair; stories are fandom heavy. |
| life | dating relationships food parenting | 3 | 3 / 3 | Weak. Life posts rarely form X stories. |
| offbeat | animals cute wholesome nature | 3 | 5 / 5 | Fair. |

Desks I cannot sweep well: world, gaming, ideas, life, and medicine below its floor. The global
sweeps (viral, rising) have the same blind spot: no engagement sort means anything outside an X story
is invisible. On the first run rising.global found nothing: every story post that cleared 100k views
or 2k likes was 11 to 20 hours old.

Beats: none look wrong. Missing: `world` has no beat for protests or migration; `life` has no beat for
health habits that are not medicine; `internet` has no beat for fandom, which is where most of its
posts came from.

## Limits

- 30 calls per minute and 1,000 calls per day per user, fixed windows. The minute window resets
  at :00 of each minute; the day resets at 00:00 UTC (8:00 PM Detroit time). Every call counts
  as one read whatever it returns.
- The daily budget is shared with everything else that reads X for Sean, including the 7:03 AM
  daily briefing.
- Cost: no money cost is shown to me; the limit is the read count.
- Max 25 results per search or list call; 100 ids per by-id call.
- Calls are fast (a few seconds); many fit in one minute, so the minute cap is the one I hit first.
  The first run used about 48 reads in total, with 25 in one minute at the peak.
- Re-reading 200 posts: 2 calls, about 15 seconds. 400 posts (the file cap): 4 calls.
- The first run went over the 10 minute target from GRABBER.md only because sweeps were being
  designed while they ran; the timed part (final full read of every record) took under a minute.

## Schedule I can sustain

Hourly, from Grok Bot's scheduler on Sean's box, at about 20 to 35 reads per run:

- watch re-read: 1 to 4 calls (all tracked ids, 100 per call)
- trends US and WW: 2 calls
- viral.global and rising.global: 2 `search_news` calls
- desks due that hour: 4 every hour (politics, entertainment, sports, internet), plus 10 more on even
  hours, plus 6 more every fourth hour: average about 10 calls
- screening of new candidates: 2 to 3 calls
- context: replies and quotes for the top 5 posts, not 15: 10 calls
- requests: 1 to 3 calls

That is about 30 an hour, 720 a day, which leaves room for the daily briefing. Calls must be spread
so no minute passes 25. Context for all 15 top posts (30 calls) every hour does not fit; it fits
every 3 hours.

## What the contract asks for that I cannot fill

- `trends[].post_count` and `trends[].story`: always `null`.
- `posts[].note` (community notes): always `null`.
- `state: deleted`: X does not say deleted, so never used; gone posts are `not_found` or `unavailable`.
- `media[].description` for video content: only a thumbnail frame can be seen.
- "Top posts by views" in any sweep: not available as a search, see above.
- Replies and quotes "ordered by likes": only within a page of 25.

## What I can get that the contract has no place for

- Link card title, description and expanded url (`entities.urls`).
- The text and author of the post being quoted or replied to, even when I do not keep it as a record.
- `possibly_sensitive`, `conversation_id`, edit history ids.
- X stories (`search_news`): name, summary, category and cluster post ids, updated time.
- `get_posts_counts_recent`: post volume per hour for a query, which could stand in for trend counts.
