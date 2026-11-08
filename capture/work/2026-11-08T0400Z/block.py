DESK_Q = {
 "politics": '(Trump OR "White House" OR Congress OR Senate OR Democrats OR Republicans OR GOP OR "Supreme Court" OR election OR governor)',
 "world": '(Ukraine OR Russia OR Israel OR Gaza OR Iran OR China OR "prime minister" OR president OR protesters OR protest OR migrants OR refugees OR ceasefire OR NATO OR "United Nations")',
 "justice": '(arrested OR police OR cops OR trial OR verdict OR sentenced OR lawsuit OR sued OR shooting OR murder OR jail OR prison)',
 "markets": '(stocks OR "stock market" OR Nasdaq OR "Dow Jones" OR "S&P 500" OR yields OR Treasury OR "the Fed" OR inflation OR "oil prices" OR mortgage OR "interest rates")',
 "business": '(CEO OR company OR layoffs OR "laid off" OR merger OR acquisition OR startup OR boycott OR retail OR earnings OR brand)',
 "ai": '(AI OR "artificial intelligence" OR OpenAI OR ChatGPT OR Anthropic OR Claude OR Gemini OR Grok OR LLM OR "AI model")',
 "tech": '(Apple OR iPhone OR Google OR Microsoft OR Android OR software OR hackers OR hacked OR "data breach" OR outage OR Tesla OR robot)',
 "science": '(NASA OR SpaceX OR rocket OR launch OR astronomers OR telescope OR physics OR scientists OR "new study" OR species OR climate)',
 "medicine": '(doctor OR doctors OR nurse OR nurses OR hospital OR FDA OR CDC OR NIH OR vaccine OR outbreak OR measles OR "mental health" OR patients OR Medicare OR medication)',
 "entertainment": '(movie OR film OR trailer OR "box office" OR Netflix OR "TV show" OR episode OR season OR anime OR actor OR actress OR celebrity)',
 "music": '(album OR song OR tour OR concert OR rapper OR singer OR Billboard OR Spotify OR Grammy OR kpop OR "music video")',
 "gaming": '(game OR gaming OR gamers OR PlayStation OR PS5 OR Xbox OR Nintendo OR Steam OR esports OR "video game" OR patch OR DLC)',
 "sports": '(NFL OR NBA OR MLB OR NHL OR WNBA OR UFC OR "Premier League" OR soccer OR touchdown OR playoffs OR "home run" OR F1 OR golf OR tennis)',
 "internet": '(meme OR memes OR streamer OR stream OR Twitch OR Kick OR YouTuber OR TikTok OR influencer OR podcast OR fandom OR "main character")',
 "offbeat": '(dog OR cat OR puppy OR kitten OR animal OR wildlife OR bird OR satisfying OR wholesome OR "wait for it")',
 "defense": '(military OR Pentagon OR Army OR Navy OR "Air Force" OR Marines OR soldiers OR troops OR veterans OR missile OR drone OR "fighter jet")',
 "disaster": '(hurricane OR tornado OR earthquake OR wildfire OR flood OR flooding OR storm OR "power outage" OR crash OR explosion OR evacuation)',
}
DUE = ["politics", "world", "defense", "justice", "disaster", "markets", "business", "ai", "tech", "science", "medicine", "entertainment", "music", "gaming", "sports", "internet", "offbeat"]
VOL_DESKS = ["business", "ai", "tech", "science", "medicine"]
volume = []
vol_sums = {}
for desk in VOL_DESKS:
    data = load(WD / f"vol_{desk}.json")
    pts = [{"start": iso_hour(row["start"]), "count": row["tweet_count"]} for row in data["data"]]
    sm = sum(p["count"] for p in pts)
    meta = (data.get("meta") or {}).get("total_tweet_count")
    vol_sums[desk] = (len(pts), sm, meta)
    volume.append({"key": f"desk.{desk}", "desk": desk, "query": DESK_Q[desk] + " lang:en", "granularity": "hour", "points": pts})

# ---------- sweeps ----------
def sweep(sid, kind, desk, method, window, status, reason, pids):
    return {
        "id": sid, "kind": kind, "desk": desk, "method": method,
        "window_hours": window, "status": status, "reason": reason,
        "post_ids": pids,
    }

watch_method = (
    "get_posts_by_ids of the re-read list in requests/plan.json for 2026-11-08T04Z "
    "(written at 2026-11-08T03:12:40.232Z), in its order and in batches of 100 "
    f"(800 ids, the day-band cap); {800-len(unavailable)} of 800 returned, {len(unavailable)} unavailable"
    + (f" ({', '.join(unavailable)})" if unavailable else "")
    + (f". {len(omitted)} watch.json ids omitted from that plan list were not re-read this run (the plan's re-read rules left them out)."
       if omitted else ".")
)

SENS_Q = {
 "news": "(from:atrupar OR from:EricLDaugh OR from:LeadingReport OR from:visegrad24 OR from:Osint613 OR from:sethharpesq OR from:nfergus OR from:rawsalerts OR from:streetmediatv OR from:WFLA OR from:JimCantore OR from:BrandonCopicWx OR from:BBCBreaking OR from:SkyNews OR from:Reuters OR from:MeidasTouch OR from:CollinRugg OR from:Gerashchenko_en) -is:reply",
 "money": "(from:unusual_whales OR from:TheStalwart OR from:biancoresearch OR from:markgurman OR from:MacRumors OR from:Variety OR from:DiscussingFilm OR from:WatcherGuru OR from:BitcoinMagazine OR from:Cointelegraph OR from:cryptorover OR from:AshCrypto OR from:BullTheoryio OR from:scottmelker OR from:BitcoinArchive OR from:GrantCardone) -is:reply",
 "science": "(from:AndrewCurran_ OR from:kimmonismus OR from:jukan05 OR from:Hesamation OR from:marclou OR from:ryancarson OR from:NASAAdmin OR from:NASA OR from:SpaceX OR from:elonmusk OR from:sciencegirl OR from:ChildrensHD OR from:SecKennedy OR from:CDCgov) -is:reply",
}
trend_counts = {n: len(source_results[f"trend.{n}"]["result_ids"]) for n in ("Michigan", "Miami", "Beck")}
sweeps = [
    sweep("watch", "watch", None, watch_method, None, "ok", None, list(watch_ids)),
    sweep("trends.us", "trends", None, "get_trends_by_woeid 23424977 max 20", None, "ok", None,
          [pid for t in trends if t["region"] == "US" for pid in t["post_ids"]]),
    sweep("trends.ww", "trends", None, "get_trends_by_woeid 1 max 20", None, "ok", None,
          [pid for t in trends if t["region"] == "WW" for pid in t["post_ids"]]),
    sweep("viral.global", "discovery", None,
          'trend-name repost streams "Michigan" lang:en is:retweet, "Miami" lang:en is:retweet and "Beck" lang:en is:retweet, newest first, 25 each (3 reads; the first three US top-ten names with no posts attached in 0300Z: Michigan rank 4, Miami rank 5 and Beck rank 7, all new this run; Whittingham rank 9 and Lofton rank 10 were also new and left unread after the three-read budget; result counts %s). Ole Miss/Notre Dame/Ohio State/Kentucky/Mensah/Michigan/Miami/Beck/Whittingham/Lofton look like Saturday college football; #UFCVegas124/Dana White one UFC event' % json.dumps(trend_counts),
          24, "ok", None, kept["viral.global"]),
    sweep("rising.global", "discovery", None,
          'quote streams "the lang:en is:quote -is:retweet" and "this lang:en is:quote -is:retweet", newest first, 25 each (2 reads); words the and this, next in the rotation after just/what',
          6, "ok", None, kept["rising.global"]),
]
for g in ("news", "money", "science"):
    sweeps.append(sweep(f"sensors.{g}", "discovery", None,
          f"search_posts_all {SENS_Q[g]}, newest first, 25; sensor posts and the origins they point at, screened by floor/pace",
          None, "ok", None, kept[f"sensors.{g}"]))
for g in ("culture", "sports", "online"):
    sweeps.append(sweep(f"sensors.{g}", "discovery", None,
          "not read this run (rotation: news/money/science this run); last read in 2026-11-08T0300Z",
          None, "skipped", "rotation: news/money/science this run", []))
for d in DUE:
    sweeps.append(sweep(
        f"desk.{d}", "desk", d,
        f"search_posts_all {DESK_Q[d]} lang:en is:retweet -is:reply, newest first, 25; reposted origins screened by desk floor/pace; keep at most five best",
        24, "ok", None, kept[f"desk.{d}"]))

sweeps.append(sweep(
    "volume.desks", "volume", None,
    "get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-11-01T05:00:00Z, end_time 2026-11-08T04:00:00Z, one read per desk for the 5 desks the plan gives (volume.business, volume.ai, volume.tech, volume.science, volume.medicine); each series is the 167 full hours, sums match meta.total_tweet_count",
    None, "ok", None, []))

N_REP = len([x for x in (ctx_replies.get("data") or []) if isinstance(x, dict)])
N_QUO = len([x for x in (ctx_quotes.get("data") or []) if isinstance(x, dict)])
sweeps.append(sweep(
    "context.top", "context", None,
    f"conversation_id:{CONTEXT_ID} is:reply and quotes_of_tweet_id:{CONTEXT_ID} -is:retweet, relevancy, start_time 2026-11-07T15:36:24.000Z end_time 2026-11-07T15:56:24.000Z (post time plus 20 minutes); five most liked of each kept ({len(ctx_reply_ids)} replies, {len(ctx_quote_ids)} quotes kept from {N_REP}/{N_QUO} returned)",
    None, "ok", None, [CONTEXT_ID] + ctx_reply_ids + ctx_quote_ids))

