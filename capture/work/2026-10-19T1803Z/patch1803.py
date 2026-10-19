s=open('build_capture.py').read()
import re as _r
def rep(a,b,count=1):
    global s
    assert a in s, a[:100]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-19T1710Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-19T1803Z'")
rep("RUN_ID = '2026-10-19T1710Z'","RUN_ID = '2026-10-19T1803Z'")
rep('capture/2026/10/19/1710Z.json from','capture/2026/10/19/1803Z.json from')
rep("STARTED = '2026-10-19T17:10:00Z'","STARTED = '2026-10-19T18:03:00Z'")
rep("OBS_AT = '2026-10-19T17:11:00Z'","OBS_AT = '2026-10-19T18:04:00Z'")
rep("READS_BEFORE = 530","READS_BEFORE = 498")
s=_r.sub(r"READS_USED = 32  #[^\n]*","READS_USED = 25  # this run's X calls (498 to 473 left today); no 429 refusals",s,1)
rep("datetime(2026,10,19,17,15,tzinfo=timezone.utc)","datetime(2026,10,19,18,6,tzinfo=timezone.utc)")
rep("""    'quote_just': 'quote_just.txt', 'quote_you': 'quote_you.txt', 'quote_this': 'quote_this.txt',
    'repost_the': 'repost_the.txt',
    'trend_chrisbosh': 'trend_chrisbosh.txt', 'trend_leslie': 'trend_leslie.txt', 'trend_nelson': 'trend_nelson.txt', 'trend_victorymonday': 'trend_victorymonday.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_what': 'repost_what.txt',
    'trend_zuffa': 'trend_zuffa.txt', 'trend_tinydesk': 'trend_tinydesk.txt', 'trend_buckner': 'trend_buckner.txt', 'trend_hardrockbet': 'trend_hardrockbet.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','defense','disaster','business','science','ideas','life')]",
    "if d['id'] in ('politics','entertainment','sports','internet')]")
rep("""    ('quote_just','quote'),('quote_you','quote'),('quote_this','quote'),('repost_the','repost'),
    ('trend_chrisbosh','trend.Chris Bosh'),('trend_leslie','trend.Leslie'),('trend_nelson','trend.Nelson'),('trend_victorymonday','trend.Victory Monday'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""","""    ('quote_is','quote'),('quote_my','quote'),('quote_it','quote'),('repost_what','repost'),
    ('trend_zuffa','trend.Zuffa'),('trend_tinydesk','trend.Tiny Desk'),('trend_buckner','trend.Buckner'),('trend_hardrockbet','trend.#HardRockBet'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""")
rep("        if str(_x) in ('trend.Leslie',): return 'politics'  # 1710Z",
    "        if str(_x) in ('trend.Zuffa','trend.Buckner'): return 'sports'  # 1803Z\n        if str(_x) in ('trend.Tiny Desk',): return 'music'  # 1803Z: NPR Tiny Desk concerts\n        if str(_x) in ('trend.Leslie',): return 'politics'  # 1710Z")
rep("if _c.endswith('1710Z.json') and '/19/' in _c: continue","if _c.endswith('1803Z.json') and '/19/' in _c: continue")
rep("(17Z is not a fourth hour, so the rest of the last 24 hours was not added)","(18Z is not a fourth hour, so the rest of the last 24 hours was not added)")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Zuffa, "Tiny Desk", Buckner, #HardRockBet (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 1710Z; #Fallout76Giveaway not read, a giveaway); quote/repost words is/my/it + what; sensors news/money/science; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "is", "my", "it" and "what": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',"""+s[j:]
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
rep("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
i=s.index("        _last = '2026-10-19T1620Z'"); j=s.index("\n", s.index("sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read",i))
s=s[:i]+"""        _last = '2026-10-19T1710Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))"""+s[j:]
rep("""            reason = 'not due this run'""","""            reason = 'not due this run (four-hour desk, last ok 2026-10-19T1710Z, due 21:10Z)'""")
i=s.index("            f'Early afternoon run at 1:10 PM ET"); j=s.index("            f'No new request:",i)
s=s[:i]+"""            f'Afternoon run at 2:03 PM ET (18:03 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1710Z run ended at 498), parallel batches of up to 8, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour; the watch.json, six-hour and still-gaining tiers plus the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names Zuffa, "Tiny Desk", Buckner, #HardRockBet (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 1710Z; #Fallout76Giveaway, the fifth, was not read: a giveaway); '
            f'quote/repost words is/my/it + what (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 1710Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; two-hour desks last ok 1620Z, due 18:20Z, next run; four-hour desks last ok 1710Z; '
            f'two screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts (one read each, 104 and 25 ids; the first-hop list fit one 100-id read plus a 4-id read, so three reads in all); search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1710Z.json'","out_path = f'{REPO}/capture/2026/10/19/1803Z.json'")
open('build_capture.py','w').write(s)
print('ok')
