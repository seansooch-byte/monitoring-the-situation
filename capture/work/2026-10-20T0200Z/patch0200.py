s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:120]
    s=s.replace(a,b,count)
rep("capture/2026/10/20/0004Z.json from","capture/2026/10/20/0200Z.json from")
rep("work/2026-10-20T0004Z'","work/2026-10-20T0200Z'")
rep("RUN_ID = '2026-10-20T0004Z'","RUN_ID = '2026-10-20T0200Z'")
rep("STARTED = '2026-10-20T00:04:00Z'","STARTED = '2026-10-20T02:00:00Z'")
rep("OBS_AT = '2026-10-20T00:05:00Z'","OBS_AT = '2026-10-20T02:01:00Z'")
rep("READS_BEFORE = 1000","READS_BEFORE = 958")
rep("datetime(2026,10,20,0,6,tzinfo=timezone.utc)","datetime(2026,10,20,2,2,tzinfo=timezone.utc)")
rep("""    'quote_that': 'quote_that.txt', 'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_mondaynightfootball': 'trend_mondaynightfootball.txt', 'trend_tednugent': 'trend_tednugent.txt', 'trend_shawn': 'trend_shawn.txt', 'trend_kittle': 'trend_kittle.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_just': 'repost_just.txt',
    'trend_jaydendaniels': 'trend_jaydendaniels.txt', 'trend_danquinn': 'trend_danquinn.txt', 'trend_wweraw': 'trend_wweraw.txt', 'trend_mikeevans': 'trend_mikeevans.txt', 'trend_angelreese': 'trend_angelreese.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet')]","if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]")
rep("""    ('quote_that','quote'),('quote_my','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_mondaynightfootball','trend.Monday Night Football'),('trend_tednugent','trend.Ted Nugent'),('trend_shawn','trend.Shawn'),('trend_kittle','trend.Kittle'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_just','repost'),
    ('trend_jaydendaniels','trend.Jayden Daniels'),('trend_danquinn','trend.Dan Quinn'),('trend_wweraw','trend.#WWERaw'),('trend_mikeevans','trend.Mike Evans'),('trend_angelreese','trend.Angel Reese'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x) in ('trend.Monday Night Football','trend.Kittle'): return 'sports'  # 0004Z",
    "        if str(_x) in ('trend.Jayden Daniels','trend.Dan Quinn','trend.Mike Evans','trend.Angel Reese','trend.#WWERaw'): return 'sports'  # 0200Z: Commanders at 49ers on Monday Night Football; Mike Evans; Angel Reese; WWE Raw (wrestling beat)\n        if str(_x) in ('trend.Monday Night Football','trend.Kittle'): return 'sports'  # 0004Z")
rep("for a,b in [('Monday Night Football','Kittle'),","for a,b in [('Jayden Daniels','Dan Quinn'),('Dan Quinn','Jayden Daniels'),('Monday Night Football','Kittle'),")
rep("if _c.endswith('0004Z.json') and '/20/' in _c: continue","if _c.endswith('0200Z.json') and '/20/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
rep("""        _last = '2026-10-19T2300Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-20T0004Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('world','justice','markets','music','gaming','offbeat','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-19T2209Z, due 00:09Z; this run started 00:04Z)'
        else:
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T2209Z, due 02:09Z)'""",
"""        reason = 'not due this run (four-hour desk, last ok 2026-10-19T2209Z, due 02:09Z; this run started 02:00Z)'""")
rep("then, as 00Z is a fourth hour, the rest of the last 24 hours slowest growing last until the 400 cap (63 of the slowest-growing left out by the cap);",
    "(02Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;")
rep("""trend names "Monday Night Football", "Ted Nugent", Shawn, Kittle (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these and #CODEPP had no posts attached in 2300Z; #CODEPP, a Stake gambling giveaway, was not read); quote/repost words that/my/what + the; sensors news/money/science; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop);""",
    """trend names "Jayden Daniels", "Dan Quinn", #WWERaw, "Mike Evans", "Angel Reese" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; none of the current top-ten US names had posts attached in 0004Z, the last capture; five read for the budget, Terry, 49ers, Brock Purdy, #RaiseHail and Diggs not read); quote/repost words this/is/you + just; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet and the two-hour desks world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop);""")
rep("""'3 quote pages + 1 repost page, common words "that", "my", "what" and "the": (that lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "this", "is", "you" and "just": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""")
i=s.index("            f'Evening run (8:04 PM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Late evening run (10:00 PM ET Oct 19 / 02:00 UTC Oct 20; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0004Z run ended at 975, and an hourly run started at 01:06Z used 17 reads but wrote no capture, see capture/NOTES.md), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; 4 reads); trends US+WW (2 reads); '
            f'trend names "Jayden Daniels", "Dan Quinn", #WWERaw, "Mike Evans", "Angel Reese" (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; none of the current top-ten US names had posts attached in 0004Z; Jayden Daniels, Dan Quinn, Terry, 49ers, Brock Purdy and Diggs look like one event, Commanders at 49ers on Monday Night Football; Terry, 49ers, Brock Purdy, #RaiseHail and Diggs not read for the budget); '
            f'quote/repost words this/is/you + just (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 0004Z); '
            f'13 desk reads: hourly politics, entertainment, sports, internet and the two-hour desks world, justice, markets, ai, tech, medicine, music, gaming, offbeat (last ok 2209Z, due 00:09Z; not read in 0004Z, which started 00:04Z); the four-hour desks are due 02:09Z, after this run started; '
"""+s[j:]
rep("(a 100-id read and a 13-id read)","(a 100-id read and a 67-id read)")
rep("out_path = f'{REPO}/capture/2026/10/20/0004Z.json'","out_path = f'{REPO}/capture/2026/10/20/0200Z.json'")
open('build_capture.py','w').write(s)
print('ok')
