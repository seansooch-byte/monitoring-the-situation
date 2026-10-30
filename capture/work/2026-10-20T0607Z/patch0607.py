s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('"""Build capture/2026/10/20/0501Z.json','"""Build capture/2026/10/20/0607Z.json')
rep("capture/work/2026-10-20T0501Z'","capture/work/2026-10-20T0607Z'")
rep("RUN_ID = '2026-10-20T0501Z'","RUN_ID = '2026-10-20T0607Z'")
rep("STARTED = '2026-10-20T05:01:00Z'","STARTED = '2026-10-20T06:07:00Z'")
rep("OBS_AT = '2026-10-20T05:01:00Z'","OBS_AT = '2026-10-20T06:07:00Z'")
rep("READS_BEFORE = 858","READS_BEFORE = 831")
rep("datetime(2026,10,20,5,4,tzinfo=timezone.utc)","datetime(2026,10,20,6,12,tzinfo=timezone.utc)")
rep("""    'quote_is': 'quote_is.txt', 'quote_the': 'quote_the.txt', 'quote_it': 'quote_it.txt',
    'repost_my': 'repost_my.txt',
    'trend_49ers': 'trend_49ers.txt', 'trend_rays': 'trend_rays.txt', 'trend_niners': 'trend_niners.txt', 'trend_mikeevans': 'trend_mikeevans.txt', 'trend_worldseries': 'trend_worldseries.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_angelreese': 'trend_angelreese.txt', 'trend_danquinn': 'trend_danquinn.txt', 'trend_fredwarner': 'trend_fredwarner.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_is','quote'),('quote_the','quote'),('quote_it','quote'),('repost_my','repost'),
    ('trend_49ers','trend.49ers'),('trend_rays','trend.Rays'),('trend_niners','trend.Niners'),('trend_mikeevans','trend.Mike Evans'),('trend_worldseries','trend.#WorldSeries'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_angelreese','trend.Angel Reese'),('trend_danquinn','trend.Dan Quinn'),('trend_fredwarner','trend.Fred Warner'),""")
rep("    if _c.endswith('0501Z.json') and '/20/' in _c: continue","    if _c.endswith('0607Z.json') and '/20/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
    "SENSOR_Q = {}\nSENSOR_READ = set()")
rep("(05Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap)","(06Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap)")
rep("""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names 49ers, Rays, Niners, "Mike Evans", #WorldSeries (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the five of the current top-ten US names with no posts attached in 0400Z); quote/repost words is/the/it + my; sensors news/money/science; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',""",
"""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "Angel Reese", "Dan Quinn", "Fred Warner" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the three of the current top-ten US names with no posts attached in 0501Z); quote/repost words that/just + what; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (100 first-hop, then the other 14 first-hop and 17 second-hop); sensors and story clusters not read for the overnight budget; screened by id with global floor/pace',""")
rep("""'3 quote pages + 1 repost page, common words "is", "the", "it" and "my": (is lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each; a first try with the bare word and (and lang:en is:quote -is:retweet) was refused by X as Invalid Request (Ambiguous use of and as a keyword), as already noted in CAPABILITIES.md, and was replaced by it',""",
"""'2 quote pages + 1 repost page (overnight budget), common words "that", "just" and "what": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',""")
rep("""        _last = '2026-10-20T0400Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-20T0501Z' if g in ('news','money','science') else '2026-10-20T0400Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (cut for the overnight budget, 06:00-11:00 UTC band, up to 20 reads); last read in {_last}',6,'skipped',f'cut for the overnight budget (06:00-11:00 UTC, up to 20 reads); last read in {_last}',[]))""")
rep("""        reason = 'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z)' if d in ('defense','disaster','business','science','ideas','life') else 'not due this run (two-hour desk, last ok 2026-10-20T0400Z, due 06:00Z)'""",
"""        reason = 'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z)' if d in ('defense','disaster','business','science','ideas','life') else 'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut for the overnight budget (06:00-11:00 UTC, up to 20 reads)'""")
rep("sweeps.append(sweep('context.top','context',None,'cut for the read budget',None,'skipped','cut for the read budget',[]))",
    "sweeps.append(sweep('context.top','context',None,'cut for the overnight read budget',None,'skipped','cut for the overnight read budget',[]))")
# reason text
i=s.index("            f'Late night run (1:01 AM ET")
j=s.index("            f'No new request:")
s=s[:i]+"""            f'Overnight run (2:07 AM ET Oct 20 / 06:07 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0501Z run ended at 831), parallel batches of up to 10, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names "Angel Reese", "Dan Quinn", "Fred Warner" (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; the three of the current top-ten US names with no posts attached in 0501Z; Dan Quinn and Fred Warner are one event with 49ers, Jayden Daniels, Niners, Commanders and Mike Evans, Commanders at 49ers on Monday Night Football; Angel Reese is the WNBA Finals; Rays and #WorldSeries are one event); '
            f'quote/repost words that/just + what (3 reads, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z) were due 06:00Z but cut for the overnight budget, the four-hour desks were read in 0308Z and are due 07:08Z; '
            f'two screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop (a 100-id read, then the other 14 with the second hop; 2111338411768389946 Not Found) and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; story clusters (search_news) not read for the overnight budget. '
"""+s[j:]
rep("f'No new request: every open request was answered in an earlier capture (r-2026-10-20-01 in 2026-10-20T0308Z) and was not read again. '","f'No new request: every open request was answered in an earlier capture (r-2026-10-20-01 in 2026-10-20T0308Z) and was not read again. '")
rep("f'Not read: volume, context.top, media descriptions (kept to the run time, as in the earlier runs today). '","f'Not read: sensors, story clusters, volume, context.top, media descriptions (overnight budget). '")
rep("out_path = f'{REPO}/capture/2026/10/20/0501Z.json'","out_path = f'{REPO}/capture/2026/10/20/0607Z.json'")
open('build_capture.py','w').write(s); print('ok')
