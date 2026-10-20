s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:150]
    s=s.replace(a,b,count)
rep("capture/2026/10/20/0400Z.json from","capture/2026/10/20/0501Z.json from")
rep("work/2026-10-20T0400Z'","work/2026-10-20T0501Z'")
rep("RUN_ID = '2026-10-20T0400Z'","RUN_ID = '2026-10-20T0501Z'")
rep("STARTED = '2026-10-20T04:00:00Z'","STARTED = '2026-10-20T05:01:00Z'")
rep("OBS_AT = '2026-10-20T04:00:00Z'","OBS_AT = '2026-10-20T05:01:00Z'")
rep("READS_BEFORE = 890","READS_BEFORE = 858")
rep("datetime(2026,10,20,4,3,tzinfo=timezone.utc)","datetime(2026,10,20,5,4,tzinfo=timezone.utc)")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_you': 'quote_you.txt',
    'repost_this': 'repost_this.txt',
    'trend_angelreese': 'trend_angelreese.txt', 'trend_danquinn': 'trend_danquinn.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_is': 'quote_is.txt', 'quote_the': 'quote_the.txt', 'quote_it': 'quote_it.txt',
    'repost_my': 'repost_my.txt',
    'trend_49ers': 'trend_49ers.txt', 'trend_rays': 'trend_rays.txt', 'trend_niners': 'trend_niners.txt', 'trend_mikeevans': 'trend_mikeevans.txt', 'trend_worldseries': 'trend_worldseries.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]",
    "if d['id'] in ('politics','entertainment','sports','internet')]")
rep("""    ('quote_that','quote'),('quote_just','quote'),('quote_you','quote'),('repost_this','repost'),
    ('trend_angelreese','trend.Angel Reese'),('trend_danquinn','trend.Dan Quinn'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_is','quote'),('quote_the','quote'),('quote_it','quote'),('repost_my','repost'),
    ('trend_49ers','trend.49ers'),('trend_rays','trend.Rays'),('trend_niners','trend.Niners'),('trend_mikeevans','trend.Mike Evans'),('trend_worldseries','trend.#WorldSeries'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("if _c.endswith('0400Z.json') and '/20/' in _c: continue","if _c.endswith('0501Z.json') and '/20/' in _c: continue")
rep("        if str(_x) in ('trend.Fred Warner','trend.Rays','trend.Niners','trend.Commanders'): return 'sports'",
    "        if str(_x) in ('trend.49ers','trend.#WorldSeries'): return 'sports'  # 0501Z: 49ers (Monday Night Football); Brewers v Rays World Series\n        if str(_x) in ('trend.Fred Warner','trend.Rays','trend.Niners','trend.Commanders'): return 'sports'")
rep("('Rays','Junior Caminero'),","('Rays','Junior Caminero'),('Rays','#WorldSeries'),('#WorldSeries','Rays'),('49ers','Niners'),('Mike Evans','49ers'),")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("then, as 04Z is a fourth hour, the rest of the last 24 hours slowest growing last until the 400 cap (42 of the slowest-growing left out by the cap); {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(05Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap); {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
rep("""trend names "Angel Reese", "Dan Quinn" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the two of""",
    """trend names 49ers, Rays, Niners, "Mike Evans", #WorldSeries (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the five of""")
rep("""the five of the current top-ten US names with no posts attached in 0308Z); quote/repost words that/just/you + this; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet and the two-hour desks world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads""",
    """the five of the current top-ten US names with no posts attached in 0400Z); quote/repost words is/the/it + my; sensors news/money/science; hourly desks politics/entertainment/sports/internet; three screening reads""")
rep("""'3 quote pages + 1 repost page, common words "that", "just", "you" and "this": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "is", "the", "it" and "my": (is lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each; a first try with the bare word and (and lang:en is:quote -is:retweet) was refused by X as Invalid Request (Ambiguous use of and as a keyword), as already noted in CAPABILITIES.md, and was replaced by it'""")
rep("""        _last = '2026-10-20T0308Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next ru""",
"""        _last = '2026-10-20T0400Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next ru""")
rep("""        reason = 'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z)'""",
"""        reason = 'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z)' if d in ('defense','disaster','business','science','ideas','life') else 'not due this run (two-hour desk, last ok 2026-10-20T0400Z, due 06:00Z)'""")
rep("out_path = f'{REPO}/capture/2026/10/20/0400Z.json'","out_path = f'{REPO}/capture/2026/10/20/0501Z.json'")
import re
i=s.index("            f'Midnight run (12:00 AM ET Oct 20")
j=s.index("            f'Not read: volume, context.top")
new = """            f'Late night run (1:01 AM ET Oct 20 / 05:01 UTC; 12:00-05:00 UTC band, its last hour, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0400Z run ended at 858), parallel batches of up to 17, no 429 refusals. One read was lost to the bare common word and (and lang:en is:quote -is:retweet), refused by X as Invalid Request ("Ambiguous use of and as a keyword"), as already noted in CAPABILITIES.md; replaced by it. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names 49ers, Rays, Niners, "Mike Evans", #WorldSeries (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; the five of the current top-ten US names with no posts attached in 0400Z; 49ers, Niners and Mike Evans are one event with Jayden Daniels, Dan Quinn, Fred Warner and Commanders, Commanders at 49ers on Monday Night Football (Mike Evans being a 49ers receiver out injured); Rays and #WorldSeries are one event, the Rays winning the AL pennant to meet the Brewers in the World Series); '
            f'quote/repost words is/the/it + my (4 reads, plus the refused and read); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 0400Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks were read in 0400Z and are due 06:00Z, the four-hour desks were read in 0308Z and are due 07:08Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop (a 100-id read and a 21-id read; 2108062331095908717 Not Found again) and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-20-01 in 2026-10-20T0308Z) and was not read again. '
"""
s=s[:i]+new+s[j:]
open('build_capture.py','w').write(s); print('ok')
