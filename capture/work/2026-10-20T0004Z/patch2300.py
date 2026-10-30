s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:120]
    s=s.replace(a,b,count)
rep("capture/2026/10/19/2209Z.json from","capture/2026/10/19/2300Z.json from")
rep("work/2026-10-19T2209Z'","work/2026-10-19T2300Z'")
rep("RUN_ID = '2026-10-19T2209Z'","RUN_ID = '2026-10-19T2300Z'")
rep("STARTED = '2026-10-19T22:09:00Z'","STARTED = '2026-10-19T23:00:00Z'")
rep("OBS_AT = '2026-10-19T22:10:00Z'","OBS_AT = '2026-10-19T23:01:00Z'")
rep("READS_BEFORE = 386","READS_BEFORE = 346")
rep("datetime(2026,10,19,22,12,tzinfo=timezone.utc)","datetime(2026,10,19,23,4,tzinfo=timezone.utc)")
rep("""    'quote_that': 'quote_that.txt', 'quote_my': 'quote_my.txt', 'quote_the': 'quote_the.txt',
    'repost_what': 'repost_what.txt',
    'trend_howie': 'trend_howie.txt', 'trend_davanteadams': 'trend_davanteadams.txt', 'trend_brandonmiller': 'trend_brandonmiller.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_it': 'quote_it.txt', 'quote_just': 'quote_just.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_newamerica': 'trend_newamerica.txt', 'trend_bronny': 'trend_bronny.txt', 'trend_kimjongun': 'trend_kimjongun.txt', 'trend_knecht': 'trend_knecht.txt', 'trend_bungie': 'trend_bungie.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_that','quote'),('quote_my','quote'),('quote_the','quote'),('repost_what','repost'),
    ('trend_howie','trend.Howie'),('trend_davanteadams','trend.Davante Adams'),('trend_brandonmiller','trend.Brandon Miller'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('quote_just','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_newamerica','trend.New America'),('trend_bronny','trend.Bronny'),('trend_kimjongun','trend.Kim Jong Un'),('trend_knecht','trend.Knecht'),('trend_bungie','trend.Bungie'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x) in ('trend.Davante Adams','trend.Brandon Miller'): return 'sports'  # 2209Z",
    "        if str(_x) in ('trend.Knecht',): return 'sports'  # 2300Z: Lakers waive Dalton Knecht, one event with Bronny\n        if str(_x) in ('trend.Davante Adams','trend.Brandon Miller'): return 'sports'  # 2209Z")
rep("for a,b in [('Bronny','Dalton Knecht'),","for a,b in [('Bronny','Knecht'),('Knecht','Bronny'),('Bronny','Dalton Knecht'),")
rep("if _c.endswith('2209Z.json') and '/19/' in _c: continue","if _c.endswith('2300Z.json') and '/19/' in _c: continue")
rep("if d['id'] in ('politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat')]","if d['id'] in ('politics','entertainment','sports','internet')]")
rep("(22Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;",
    "(23Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;")
rep("""trend names Howie, "Davante Adams", "Brandon Miller" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these and #CODEPP had no posts attached in 2100Z; #CODEPP was read but is a Stake gambling giveaway, so nothing from it was used); quote/repost words that/my/the + what; sensors news/money/science; all 19 desks (hourly, two-hour and four-hour desks were all due);""",
    """trend names "New America", Bronny, "Kim Jong Un", Knecht, Bungie (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these and #CODEPP had no posts attached in 2209Z; #CODEPP, a Stake gambling giveaway, was not read); quote/repost words it/just/this + is; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet;""")
rep("""'3 quote pages + 1 repost page, common words "that", "my", "the" and "what": (that lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "it", "just", "this" and "is": (it lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
rep("""        _last = '2026-10-19T2100Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T2209Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("""            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1909Z, due 21:09Z; this run started 21:00Z)'
        else:
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T1710Z, due 21:10Z; this run started 21:00Z)'""",
"""            reason = 'not due this run (two-hour desk, last ok 2026-10-19T2209Z, due 00:09Z)'
        else:
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T2209Z, due 02:09Z)'""")
i=s.index("            f'Evening run (6:09 PM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Evening run (7:00 PM ET / 23:00 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads; the last run of the UTC day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 2209Z run ended at 346), parallel batches of up to 9, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; nothing left out by the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names "New America", Bronny, "Kim Jong Un", Knecht, Bungie (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these and #CODEPP had no posts attached in 2209Z; #CODEPP, a Stake gambling giveaway, was not read; New America is Trump calling for New Mexico to be renamed; Bronny and Knecht are one event, the Lakers waiving Dalton Knecht; Kim Jong Un is the unconfirmed death rumours; Bungie is the Star Wars Battlefront 3 developer rumour); '
            f'quote/repost words it/just/this + is (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 2209Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet (the two-hour desks are due 00:09Z and the four-hour desks 02:09Z, all last swept in 2209Z); '
"""+s[j:]
rep("(a 100-id read and an 81-id read)","(a 100-id read and a 19-id read)")
rep("No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. ","No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2026-10-18T2203Z) and was not read again. ")
rep("out_path = f'{REPO}/capture/2026/10/19/2209Z.json'","out_path = f'{REPO}/capture/2026/10/19/2300Z.json'")
open('build_capture.py','w').write(s)
print('ok')
