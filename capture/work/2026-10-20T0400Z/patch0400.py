s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:150]
    s=s.replace(a,b,count)
rep("capture/2026/10/20/0308Z.json from","capture/2026/10/20/0400Z.json from")
rep("work/2026-10-20T0308Z'","work/2026-10-20T0400Z'")
rep("RUN_ID = '2026-10-20T0308Z'","RUN_ID = '2026-10-20T0400Z'")
rep("STARTED = '2026-10-20T03:08:00Z'","STARTED = '2026-10-20T04:00:00Z'")
rep("OBS_AT = '2026-10-20T03:09:00Z'","OBS_AT = '2026-10-20T04:00:00Z'")
rep("READS_BEFORE = 923","READS_BEFORE = 890")
rep("datetime(2026,10,20,3,10,tzinfo=timezone.utc)","datetime(2026,10,20,4,3,tzinfo=timezone.utc)")
rep("""    'quote_the': 'quote_the.txt', 'quote_it': 'quote_it.txt', 'quote_my': 'quote_my.txt',
    'repost_what': 'repost_what.txt',
    'trend_fredwarner': 'trend_fredwarner.txt', 'trend_rays': 'trend_rays.txt', 'trend_niners': 'trend_niners.txt', 'trend_commanders': 'trend_commanders.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'req_spacexa': 'req_r-2026-10-20-01a.txt', 'req_spacexb': 'req_r-2026-10-20-01b.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_you': 'quote_you.txt',
    'repost_this': 'repost_this.txt',
    'trend_angelreese': 'trend_angelreese.txt', 'trend_danquinn': 'trend_danquinn.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','defense','disaster','business','science','ideas','life')]",
    "if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]")
rep("""    ('quote_the','quote'),('quote_it','quote'),('quote_my','quote'),('repost_what','repost'),
    ('trend_fredwarner','trend.Fred Warner'),('trend_rays','trend.Rays'),('trend_niners','trend.Niners'),('trend_commanders','trend.Commanders'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_that','quote'),('quote_just','quote'),('quote_you','quote'),('repost_this','repost'),
    ('trend_angelreese','trend.Angel Reese'),('trend_danquinn','trend.Dan Quinn'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("if _c.endswith('0308Z.json') and '/20/' in _c: continue","if _c.endswith('0400Z.json') and '/20/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
rep("""        _last = '2026-10-20T0200Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-20T0308Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("""        reason = 'not due this run (two-hour desk, last ok 2026-10-20T0200Z, due 04:00Z)'""",
"""        reason = 'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z)'""")
rep("(03Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;",
    "then, as 04Z is a fourth hour, the rest of the last 24 hours slowest growing last until the 400 cap (42 of the slowest-growing left out by the cap);")
rep("""trend names "Fred Warner", Rays, Niners, Commanders (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the four of the current top-ten US names with no posts attached in 0200Z); quote/repost words the/it/my + what; sensors news/money/science; hourly desks politics/entertainment/sports/internet and the four-hour desks defense/disaster/business/science/ideas/life; three screening reads by id of unread referenced posts (two first-hop, one second-hop);""",
    """trend names "Angel Reese", "Dan Quinn" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the two of the current top-ten US names with no posts attached in 0308Z); quote/repost words that/just/you + this; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet and the two-hour desks world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop);""")
rep("""'3 quote pages + 1 repost page, common words "the", "it", "my" and "what": (the lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "that", "just", "you" and "this": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each'""")
i=s.index("            f'Late evening run (the hourly trigger"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Midnight run (12:00 AM ET Oct 20 / 04:00 UTC; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0308Z run ended at 890), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list, then the rest of the last 24 hours slowest growing last, with the 42 slowest-growing of those left out by the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names "Angel Reese", "Dan Quinn" (2 reads; each "<name> lang:en is:retweet", newest first, 25 each; the two of the current top-ten US names with no posts attached in 0308Z; 49ers, Jayden Daniels, Dan Quinn, Niners, Fred Warner and Commanders are one event, Commanders at 49ers on Monday Night Football; the two Rays entries are one event); '
            f'quote/repost words that/just/you + this (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 0308Z); '
            f'13 desk reads: hourly politics, entertainment, sports, internet and the two-hour desks world, justice, markets, ai, tech, medicine, music, gaming, offbeat (last ok 0200Z, due 04:00Z); the four-hour desks were read in 0308Z and are due 07:08Z; '
"""+s[j:]
rep("(a 100-id read and a 30-id read)","(a 100-id read and a 49-id read)")
rep("""            f'New request r-2026-10-20-01 answered with two searches (2 reads, relevancy, from 2026-10-19T07:50Z); every other open request was answered in an earlier capture and was not read again. '""",
    """            f'No new request: every open request was answered in an earlier capture (r-2026-10-20-01 in 2026-10-20T0308Z) and was not read again. '""")
rep("out_path = f'{REPO}/capture/2026/10/20/0308Z.json'","out_path = f'{REPO}/capture/2026/10/20/0400Z.json'")
rep("""REQ_PICKS = {'r-2026-10-20-01': ['2112323120380129562','2112286669508694289','2112256359022362891','2112227716183277635','2112211740884975910']}
REQ_FILES = {'r-2026-10-20-01': 'req_spacexa'}
REQ_ONLY = ({t['id'] for t in (raw['req_spacexa'].get('data') or [])} | {t['id'] for t in (raw['req_spacexb'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-20-01']) - {'2112089556615123114'}""","""REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()""")
rep("ANSWERED_EARLIER = {'r-2026-10-18-02'","ANSWERED_EARLIER = {'r-2026-10-20-01':'2026-10-20T0308Z','r-2026-10-18-02'")
i=s.index("ANSWERS = [{\n    'request_id': 'r-2026-10-20-01',"); j=s.index("}]\ncapture = {",i)
s=s[:i]+"ANSWERS = []\ncapture = {"+s[j+len("}]\ncapture = {"):]
rep("# 5) request picks (r-2026-10-20-01)","# 5) request picks (none this run)")
open('build_capture.py','w').write(s)
print('ok')
