s=open('build_capture.py').read()
import re as _r
def rep(a,b,count=1):
    global s
    assert a in s, a[:100]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-19T1803Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-19T1909Z'")
rep("RUN_ID = '2026-10-19T1803Z'","RUN_ID = '2026-10-19T1909Z'")
rep('capture/2026/10/19/1803Z.json from','capture/2026/10/19/1909Z.json from')
rep("STARTED = '2026-10-19T18:03:00Z'","STARTED = '2026-10-19T19:09:00Z'")
rep("OBS_AT = '2026-10-19T18:04:00Z'","OBS_AT = '2026-10-19T19:10:00Z'")
rep("READS_BEFORE = 498","READS_BEFORE = 473")
s=_r.sub(r"READS_USED = 25  #[^\n]*","READS_USED = 35  # this run's X calls (473 to 438 left today); no 429 refusals",s,1)
rep("datetime(2026,10,19,18,6,tzinfo=timezone.utc)","datetime(2026,10,19,19,13,tzinfo=timezone.utc)")
rep("""    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_what': 'repost_what.txt',
    'trend_zuffa': 'trend_zuffa.txt', 'trend_tinydesk': 'trend_tinydesk.txt', 'trend_buckner': 'trend_buckner.txt', 'trend_hardrockbet': 'trend_hardrockbet.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_you': 'quote_you.txt',
    'repost_this': 'repost_this.txt',
    'trend_eagles': 'trend_eagles.txt', 'trend_kimjongun': 'trend_kimjongun.txt', 'trend_chrisbosh': 'trend_chrisbosh.txt', 'trend_leslie': 'trend_leslie.txt', 'trend_london': 'trend_london.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet')]",
    "if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]")
rep("""    ('quote_is','quote'),('quote_my','quote'),('quote_it','quote'),('repost_what','repost'),
    ('trend_zuffa','trend.Zuffa'),('trend_tinydesk','trend.Tiny Desk'),('trend_buckner','trend.Buckner'),('trend_hardrockbet','trend.#HardRockBet'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""","""    ('quote_that','quote'),('quote_just','quote'),('quote_you','quote'),('repost_this','repost'),
    ('trend_eagles','trend.Eagles'),('trend_kimjongun','trend.Kim Jong Un'),('trend_chrisbosh','trend.Chris Bosh'),('trend_leslie','trend.Leslie'),('trend_london','trend.London'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""")
rep("        if str(_x) in ('trend.Zuffa','trend.Buckner'): return 'sports'  # 1803Z",
    "        if str(_x) in ('trend.Eagles',): return 'sports'  # 1909Z: Eagles QB Jalen Hurts out for the season\n        if str(_x) in ('trend.Kim Jong Un',): return 'world'  # 1909Z\n        if str(_x) in ('trend.Zuffa','trend.Buckner'): return 'sports'  # 1803Z")
rep("if _c.endswith('1803Z.json') and '/19/' in _c: continue","if _c.endswith('1909Z.json') and '/19/' in _c: continue")
rep("(18Z is not a fourth hour, so the rest of the last 24 hours was not added)","(19Z is not a fourth hour, so the rest of the last 24 hours was not added)")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Eagles, "Kim Jong Un", "Chris Bosh", Leslie, London (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 1803Z; #Fallout76Giveaway not read, a giveaway); quote/repost words that/just/you + this; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet and two-hour desks world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "that", "just", "you" and "this": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each',"""+s[j:]
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
i=s.index("        _last = '2026-10-19T1710Z'"); j=s.index("\n", s.index("sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read",i))
s=s[:i]+"""        _last = '2026-10-19T1803Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))"""+s[j:]
rep("""            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1620Z, due 18:20Z)'""","""            reason = 'swept this run'""")
i=s.index("            f'Afternoon run at 2:03 PM ET"); j=s.index("            f'No new request:",i)
s=s[:i]+"""            f'Afternoon run (the hourly trigger fired late: 3:09 PM ET / 19:09 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1803Z run ended at 473), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour; the watch.json, six-hour and still-gaining tiers plus the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names Eagles, "Kim Jong Un", "Chris Bosh", Leslie, London (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 1803Z; #Fallout76Giveaway not read: a giveaway; Eagles, Chris Bosh and London are largely the Jalen Hurts blood-clot story); '
            f'quote/repost words that/just/you + this (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 1803Z); '
            f'13 desk reads: hourly politics, entertainment, sports, internet and the nine two-hour desks (last ok 1620Z, due 18:20Z); four-hour desks last ok 1710Z, due 21:10Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop (a 100-id read and a 70-id read) and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1803Z.json'","out_path = f'{REPO}/capture/2026/10/19/1909Z.json'")
open('build_capture.py','w').write(s)
print('ok')
