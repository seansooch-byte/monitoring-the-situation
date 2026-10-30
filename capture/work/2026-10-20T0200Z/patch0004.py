s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:120]
    s=s.replace(a,b,count)
rep("capture/2026/10/19/2300Z.json from","capture/2026/10/20/0004Z.json from")
rep("work/2026-10-19T2300Z'","work/2026-10-20T0004Z'")
rep("RUN_ID = '2026-10-19T2300Z'","RUN_ID = '2026-10-20T0004Z'")
rep("STARTED = '2026-10-19T23:00:00Z'","STARTED = '2026-10-20T00:04:00Z'")
rep("OBS_AT = '2026-10-19T23:01:00Z'","OBS_AT = '2026-10-20T00:05:00Z'")
rep("READS_BEFORE = 346","READS_BEFORE = 1000")
rep("datetime(2026,10,19,23,4,tzinfo=timezone.utc)","datetime(2026,10,20,0,8,tzinfo=timezone.utc)")
rep("""    'quote_it': 'quote_it.txt', 'quote_just': 'quote_just.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_newamerica': 'trend_newamerica.txt', 'trend_bronny': 'trend_bronny.txt', 'trend_kimjongun': 'trend_kimjongun.txt', 'trend_knecht': 'trend_knecht.txt', 'trend_bungie': 'trend_bungie.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_mondaynightfootball': 'trend_mondaynightfootball.txt', 'trend_tednugent': 'trend_tednugent.txt', 'trend_shawn': 'trend_shawn.txt', 'trend_kittle': 'trend_kittle.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_it','quote'),('quote_just','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_newamerica','trend.New America'),('trend_bronny','trend.Bronny'),('trend_kimjongun','trend.Kim Jong Un'),('trend_knecht','trend.Knecht'),('trend_bungie','trend.Bungie'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_that','quote'),('quote_my','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_mondaynightfootball','trend.Monday Night Football'),('trend_tednugent','trend.Ted Nugent'),('trend_shawn','trend.Shawn'),('trend_kittle','trend.Kittle'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) in ('trend.Knecht',): return 'sports'  # 2300Z",
    "        if str(_x) in ('trend.Monday Night Football','trend.Kittle'): return 'sports'  # 0004Z: Commanders at 49ers on Monday Night Football\n        if str(_x) in ('trend.Ted Nugent',): return 'politics'  # 0004Z: Ted Nugent speaking at the Trump rally in Kansas\n        if str(_x) in ('trend.Shawn',): return 'internet'  # 0004Z: mostly the Shawn Ryan Show podcast dispute\n        if str(_x) in ('trend.Knecht',): return 'sports'  # 2300Z")
rep("for a,b in [('Bronny','Knecht'),","for a,b in [('Monday Night Football','Kittle'),('Kittle','Monday Night Football'),('Bronny','Knecht'),")
rep("if _c.endswith('2300Z.json') and '/19/' in _c: continue","if _c.endswith('0004Z.json') and '/20/' in _c: continue")
rep("skip_nsfw |= {'2088853262334152834'}  # 2209Z","skip_nsfw |= {'2112334072492196126','2112332726116462711','2112322316256309442'}  # 0004Z: posts alleging sexual abuse of a minor by Ted Nugent (actingliketommy, KyleKulinski, AllwhichIam); left out under the minors rule\nskip_nsfw |= {'2088853262334152834'}  # 2209Z")
rep("(23Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;",
    "then, as 00Z is a fourth hour, the rest of the last 24 hours slowest growing last until the 400 cap (63 of the slowest-growing left out by the cap);")
rep("""trend names "New America", Bronny, "Kim Jong Un", Knecht, Bungie (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these and #CODEPP had no posts attached in 2209Z; #CODEPP, a Stake gambling giveaway, was not read); quote/repost words it/just/this + is; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet;""",
    """trend names "Monday Night Football", "Ted Nugent", Shawn, Kittle (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these and #CODEPP had no posts attached in 2300Z; #CODEPP, a Stake gambling giveaway, was not read); quote/repost words that/my/what + the; sensors news/money/science; hourly desks politics/entertainment/sports/internet;""")
rep("""'3 quote pages + 1 repost page, common words "it", "just", "this" and "is": (it lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "that", "my", "what" and "the": (that lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
rep("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
rep("""        _last = '2026-10-19T2209Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T2300Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""")
rep("""            reason = 'not due this run (two-hour desk, last ok 2026-10-19T2209Z, due 00:09Z)'
        else:
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T2209Z, due 02:09Z)'""",
"""            reason = 'not due this run (two-hour desk, last ok 2026-10-19T2209Z, due 00:09Z; this run started 00:04Z)'
        else:
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T2209Z, due 02:09Z)'""")
i=s.index("            f'Evening run (7:00 PM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Evening run (8:04 PM ET Oct 19 / 00:04 UTC Oct 20; the first run of the UTC day, the X day reset at 00:00 UTC; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 8, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list, then the rest of the last 24 hours slowest growing last, with the 63 slowest-growing of those left out by the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names "Monday Night Football", "Ted Nugent", Shawn, Kittle (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these and #CODEPP had no posts attached in 2300Z; #CODEPP, a Stake gambling giveaway, was not read; Monday Night Football and Kittle are one event, Commanders at 49ers; Ted Nugent is his speech at the Trump rally in Kansas; Shawn is mostly the Shawn Ryan Show podcast dispute); '
            f'quote/repost words that/my/what + the (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 2300Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet (the two-hour desks are due 00:09Z, after this run started, and the four-hour desks 02:09Z, all last swept in 2209Z); '
"""+s[j:]
rep("(a 100-id read and a 19-id read)","(a 100-id read and a 13-id read)")
rep("out_path = f'{REPO}/capture/2026/10/19/2300Z.json'","out_path = f'{REPO}/capture/2026/10/20/0004Z.json'")
open('build_capture.py','w').write(s)
