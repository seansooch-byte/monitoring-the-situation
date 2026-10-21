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

## Second probe (2026-10-09, run 2026-10-09T0615Z)

Every call below went through the x MCP namespace during run 2026-10-09T0615Z. X rejected none of them.
The only adjustment message was from the tool: "max_results was lowered from 100 to 25, the most
results one call can return." Totals are from the "X reads left" line each call returns.

| Probe | What X returned | Reads |
|---|---|---|
| Repost stream: `search_posts_all "the lang:en is:retweet"`, newest first | 25 retweets from the last minute or so. Each carries the original in `includes.tweets` (expansion `referenced_tweets.id`) with `created_at`, text, author and full `public_metrics`. 25 distinct originals; 6 were under 24 hours and over 100k views or 2k likes (largest 884,660 views). | 1 |
| Quote stream: `search_posts_all "the lang:en is:quote"`, newest first | 23 results, 23 distinct quoted posts with `lang`, entities and metrics. 6 cleared the global floor (largest 462,781 views). | 1 |
| `attachments.media_source_tweet_id` | Works. Put `attachments` in post.fields and `attachments.media_source_tweet_id` in expansions; the source id appears as an array inside `attachments`. On 3 aggregator videos from the first capture: 2108221472980218305 (_papawere) gives 2108078093827031386; 2108150422733009382 (MarioNawfal) gives 2107749380040343905; 2108404380856975503 (barstoolsports) gives 2108397722348716044. Absent on 2108076659010105408 (streetmediatv), 2108125191159132417 (miraghini) and 2108256108624400390 (insanevideos), which look like own uploads. Across the 174 re-read posts, 12 carried a source. | 0 extra (rides on by-id reads) |
| Many accounts in one search | 30 accounts joined by `OR from:` in one 585 character query: accepted, 25 results. I did not find the length limit; nothing was rejected at 585. Results were mostly replies and reposts by miraghini, _papawere and Spazzzie, so sensor queries need `-is:reply` and those accounts are poor sensors. | 1 |
| `get_posts_counts_recent`, granularity hour, politics standing query | 169 buckets for 7 days: a partial first bucket from 2026-10-02T06:16:02Z, 167 full hours from 2026-10-02T07:00Z to 2026-10-09T05:00Z, and a partial bucket 06:00 to 06:16:02Z. Field is `tweet_count` with `start` and `end`; `meta.total_tweet_count` 13,623,797 matched the sum. Cost: 1 read (944 to 943). | 1 |
| Replies, relevancy vs newest: `conversation_id:2108262760153026784 is:reply` | Both orders returned the same 25 replies in the same order, all from the last 30 minutes, with 0 or 1 likes. Neither page has more likes; relevancy order does not surface most liked replies for this post (888 replies). | 2 |
| `quotes_of_tweet_id:2108262760153026784` | Accepted, 25 results: 4 direct quote posts of the target plus 21 reposts of other posts in the same story (likely reposts of quotes). Usable only after filtering to `referenced_tweets` type `quoted` with the target id. | 1 |

Other facts seen: the metric key is `repost_count` in get_posts_by_ids but `retweet_count` in search
results; users can carry `withheld.country_codes`; a 100 id by-id read costs 1 read.

## Standing queries

One query per desk, kept stable so volume series stay comparable. Desk sweeps run
`<query> lang:en is:retweet` newest first and take the reposted originals; volume runs
`<query> lang:en` through `get_posts_counts_recent` at hour granularity. Changed for the weak desks
(world, gaming, ideas, life, medicine, internet) to cover the beats in contract/desks.json,
including the new ones (protests, migration, fandom, habits).

| Desk | Query | Chars |
|---|---|---|
| politics | `(Trump OR "White House" OR Congress OR Senate OR Democrats OR Republicans OR GOP OR "Supreme Court" OR election OR governor)` | 124 |
| world | `(Ukraine OR Russia OR Israel OR Gaza OR Iran OR China OR "prime minister" OR president OR protesters OR protest OR migrants OR refugees OR ceasefire OR NATO OR "United Nations")` | 177 |
| defense | `(military OR Pentagon OR Army OR Navy OR "Air Force" OR Marines OR soldiers OR troops OR veterans OR missile OR drone OR "fighter jet")` | 135 |
| justice | `(arrested OR police OR cops OR trial OR verdict OR sentenced OR lawsuit OR sued OR shooting OR murder OR jail OR prison)` | 120 |
| disaster | `(hurricane OR tornado OR earthquake OR wildfire OR flood OR flooding OR storm OR "power outage" OR crash OR explosion OR evacuation)` | 132 |
| markets | `(stocks OR "stock market" OR Nasdaq OR "Dow Jones" OR "S&P 500" OR yields OR Treasury OR "the Fed" OR inflation OR "oil prices" OR mortgage OR "interest rates")` | 160 |
| business | `(CEO OR company OR layoffs OR "laid off" OR merger OR acquisition OR startup OR boycott OR retail OR earnings OR brand)` | 119 |
| crypto | `(bitcoin OR BTC OR crypto OR ethereum OR ETH OR solana OR memecoin OR Coinbase OR Binance OR altcoin)` | 101 |
| ai | `(AI OR "artificial intelligence" OR OpenAI OR ChatGPT OR Anthropic OR Claude OR Gemini OR Grok OR LLM OR "AI model")` | 116 |
| tech | `(Apple OR iPhone OR Google OR Microsoft OR Android OR software OR hackers OR hacked OR "data breach" OR outage OR Tesla OR robot)` | 129 |
| science | `(NASA OR SpaceX OR rocket OR launch OR astronomers OR telescope OR physics OR scientists OR "new study" OR species OR climate)` | 126 |
| medicine | `(doctor OR doctors OR nurse OR nurses OR hospital OR FDA OR CDC OR NIH OR vaccine OR outbreak OR measles OR "mental health" OR patients OR Medicare OR medication)` | 162 |
| entertainment | `(movie OR film OR trailer OR "box office" OR Netflix OR "TV show" OR episode OR season OR anime OR actor OR actress OR celebrity)` | 129 |
| music | `(album OR song OR tour OR concert OR rapper OR singer OR Billboard OR Spotify OR Grammy OR kpop OR "music video")` | 113 |
| gaming | `(game OR gaming OR gamers OR PlayStation OR PS5 OR Xbox OR Nintendo OR Steam OR esports OR "video game" OR patch OR DLC)` | 120 |
| ideas | `(book OR novel OR author OR museum OR painting OR artist OR architecture OR history OR historian OR philosophy OR religion OR church OR Bible OR essay)` | 151 |
| sports | `(NFL OR NBA OR MLB OR NHL OR WNBA OR UFC OR "Premier League" OR soccer OR touchdown OR playoffs OR "home run" OR F1 OR golf OR tennis)` | 134 |
| internet | `(meme OR memes OR streamer OR stream OR Twitch OR Kick OR YouTuber OR TikTok OR influencer OR podcast OR fandom OR "main character")` | 132 |
| life | `(dating OR boyfriend OR girlfriend OR husband OR wife OR marriage OR parents OR kids OR restaurant OR recipe OR wedding OR rent OR tipping OR college OR habit)` | 159 |
| offbeat | `(dog OR cat OR puppy OR kitten OR animal OR wildlife OR bird OR satisfying OR wholesome OR "wait for it")` | 105 |

## Third probe (2026-10-09, run 2026-10-09T0629Z)

Every call went through the x MCP namespace between 06:29:24 and 06:36:45 UTC. X rejected none of
them, so there is no rejection text to quote. Five reads.

| Probe | What X returned | Reads |
|---|---|---|
| `get_posts_counts_recent "retweets_of_tweet_id:2024898302035067174"`, hour, default window | Accepted. 169 buckets, every one 0, total 0. The post is from February 2026, so a quiet week and an operator that counts nothing look the same. Test again on a post under a day old before trusting it. | 1 |
| `get_posts_counts_recent "quotes_of_tweet_id:2108262760153026784"`, hour | Accepted. Total 1,193. First non-zero hour 2026-10-08 18:00Z (3), peak 23:00Z (152), 129 in 05:00Z, 56 in the partial 06:00Z bucket. | 1 |
| `get_posts_counts_recent "conversation_id:2108262760153026784"`, hour | Accepted. Total 1,097 (replies, since the conversation is one post). First non-zero hour 18:00Z (22), peak 22:00Z (142), 66 in 05:00Z. The window starts at the call time minus 7 days (first bucket from 2026-10-02T06:29:24Z). | 1 |
| Early window replies: `search_posts_all "conversation_id:2108108695876092323 is:reply"`, relevancy, start 08:14:00Z, end 20 minutes after the post | 14 results with real likes: 661 (37,111 views), 279, 235, 94. Without the window, both orders returned only the newest replies with 0 or 1 likes. The window works. | 1 |
| Early window quotes: `search_posts_all "quotes_of_tweet_id:2108108695876092323 -is:retweet"`, same window | 8 results, all real quote posts of the target (no reposts once `-is:retweet` is added). The top one had 9,732 likes and 832,494 views. | 1 |
| Two hour window, both kinds, relevancy (run as the r-2026-10-09-10 context step) | 25 results each, but all from the last 45 minutes of the window with 0 to 156 likes: inside a window, relevancy still returns the newest posts first. Use the 20 minute window for most liked; the two hour window only adds the late part. | 2 |

Other facts seen this run:

- `is:quote` also matches reposts of quote posts: 69 of 75 quote-stream results were reposts. Add
  `-is:retweet` to the quote stream.
- `search_news` output stays inline (under the size at which the tool writes a file), so it cannot
  be saved verbatim; `x_stories` stays empty until it can be. Two attempts this run.
- Per-post series: one read per series, so all three for the 19 watch posts is 57 reads. Planned
  as a rotation in capture/RUNBOOK.md.
- Three ids in a by-id read of 94 returned "Not Found Error"; three posts in search results came
  without their author in `includes.users` and were left out.
- 2026-10-15T0708Z: X rejects the bare common word `and` as a search term ("Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 1)"), and the rejected read still counts. Quote it: `"and" lang:en is:quote -is:retweet`.
- 2026-10-21T1007Z: search_posts_all refused `and lang:en is:quote -is:retweet` with 400 Invalid Request: "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text". The bare word "and" cannot be the rotation word; use `"and"` in quotes or skip it.
