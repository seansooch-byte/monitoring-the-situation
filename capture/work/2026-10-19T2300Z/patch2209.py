s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:120]
    s=s.replace(a,b,count)
rep("capture/2026/10/19/2100Z.json from","capture/2026/10/19/2209Z.json from")
rep("work/2026-10-19T2100Z'","work/2026-10-19T2209Z'")
rep("RUN_ID = '2026-10-19T2100Z'","RUN_ID = '2026-10-19T2209Z'")
rep("STARTED = '2026-10-19T21:00:00Z'","STARTED = '2026-10-19T22:09:00Z'")
rep("OBS_AT = '2026-10-19T21:03:00Z'","OBS_AT = '2026-10-19T22:10:00Z'")
rep("READS_BEFORE = 412","READS_BEFORE = 386")
rep("datetime(2026,10,19,21,4,tzinfo=timezone.utc)","datetime(2026,10,19,22,12,tzinfo=timezone.utc)")
rep("""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_this': 'quote_this.txt',
    'repost_just': 'repost_just.txt',
    'trend_bronny': 'trend_bronny.txt', 'trend_newmexico': 'trend_newmexico.txt', 'trend_daltonknecht': 'trend_daltonknecht.txt', 'trend_kimjongun': 'trend_kimjongun.txt', 'trend_coys': 'trend_coys.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_my': 'quote_my.txt', 'quote_the': 'quote_the.txt',
    'repost_what': 'repost_what.txt',
    'trend_howie': 'trend_howie.txt', 'trend_davanteadams': 'trend_davanteadams.txt', 'trend_brandonmiller': 'trend_brandonmiller.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_is','quote'),('quote_you','quote'),('quote_this','quote'),('repost_just','repost'),
    ('trend_bronny','trend.Bronny'),('trend_newmexico','trend.New Mexico'),('trend_daltonknecht','trend.Dalton Knecht'),('trend_kimjongun','trend.Kim Jong Un'),('trend_coys','trend.#COYS'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_that','quote'),('quote_my','quote'),('quote_the','quote'),('repost_what','repost'),
    ('trend_howie','trend.Howie'),('trend_davanteadams','trend.Davante Adams'),('trend_brandonmiller','trend.Brandon Miller'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) in ('trend.New Mexico',): return 'politics'  # 2100Z",
    "        if str(_x) in ('trend.Davante Adams','trend.Brandon Miller'): return 'sports'  # 2209Z: Davante Adams hamstring injury; Brandon Miller Hornets extension\n        if str(_x) in ('trend.New Mexico',): return 'politics'  # 2100Z")
rep("if _c.endswith('2100Z.json') and '/19/' in _c: continue","if _c.endswith('2209Z.json') and '/19/' in _c: continue")
rep("if d['id'] in ('politics','entertainment','sports','internet')]","if d['id'] in ('politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat')]")
rep("(21Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;",
    "(22Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;")
rep("""trend names Bronny, "New Mexico", "Dalton Knecht", "Kim Jong Un", #COYS (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2000Z); quote/repost words is/you/this + just; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet;""",
    """trend names Howie, "Davante Adams", "Brandon Miller" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these and #CODEPP had no posts attached in 2100Z; #CODEPP was read but is a Stake gambling giveaway, so nothing from it was used); quote/repost words that/my/the + what; sensors news/money/science; all 19 desks (hourly, two-hour and four-hour desks were all due);""")
rep("""'3 quote pages + 1 repost page, common words "is", "you", "this" and "just": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "that", "my", "the" and "what": (that lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
rep("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
rep("""        _last = '2026-10-19T2000Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T2100Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""")
i=s.index("            f'Afternoon run (5:00 PM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Evening run (6:09 PM ET / 22:09 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 2100Z run ended at 386), parallel batches of up to 25, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; nothing left out by the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names #CODEPP, Howie, "Davante Adams", "Brandon Miller" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2100Z; #CODEPP is a Stake gambling giveaway, so its stream was not used and no posts were attached; Howie is the Eagles front office and the Nick Sirianni press conference on Jalen Hurts, one event with the Jalen and Eagles trends; Davante Adams is the Rams receiver hamstring injury, one event with the Kobie Turner and Poona Ford trends; Brandon Miller is his Hornets contract extension); '
            f'quote/repost words that/my/the + what (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 2100Z); '
            f'19 desk reads: hourly politics, entertainment, sports, internet; the nine two-hour desks (last ok 1909Z, due 21:09Z) and the six four-hour desks (last ok 1710Z, due 21:10Z), all due this run; '
"""+s[j:]
rep("(a 100-id read and a 26-id read)","(a 100-id read and an 81-id read)")
rep("out_path = f'{REPO}/capture/2026/10/19/2100Z.json'","out_path = f'{REPO}/capture/2026/10/19/2209Z.json'")
open('build_capture.py','w').write(s)
print('ok')
