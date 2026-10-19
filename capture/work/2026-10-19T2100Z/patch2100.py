s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:120]
    s=s.replace(a,b,count)
rep("capture/2026/10/19/2000Z.json from","capture/2026/10/19/2100Z.json from")
rep("work/2026-10-19T2000Z'","work/2026-10-19T2100Z'")
rep("RUN_ID = '2026-10-19T2000Z'","RUN_ID = '2026-10-19T2100Z'")
rep("STARTED = '2026-10-19T20:00:00Z'","STARTED = '2026-10-19T21:00:00Z'")
rep("OBS_AT = '2026-10-19T20:01:00Z'","OBS_AT = '2026-10-19T21:03:00Z'")
rep("READS_BEFORE = 438","READS_BEFORE = 412")
rep("datetime(2026,10,19,20,4,tzinfo=timezone.utc)","datetime(2026,10,19,21,4,tzinfo=timezone.utc)")
rep("""    'quote_the': 'quote_the.txt', 'quote_what': 'quote_what.txt', 'quote_it': 'quote_it.txt',
    'repost_my': 'repost_my.txt',
    'trend_newamerica': 'trend_newamerica.txt', 'trend_howie': 'trend_howie.txt', 'trend_bungie': 'trend_bungie.txt', 'trend_maddison': 'trend_maddison.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_this': 'quote_this.txt',
    'repost_just': 'repost_just.txt',
    'trend_bronny': 'trend_bronny.txt', 'trend_newmexico': 'trend_newmexico.txt', 'trend_daltonknecht': 'trend_daltonknecht.txt', 'trend_kimjongun': 'trend_kimjongun.txt', 'trend_coys': 'trend_coys.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_the','quote'),('quote_what','quote'),('quote_it','quote'),('repost_my','repost'),
    ('trend_newamerica','trend.New America'),('trend_howie','trend.Howie'),('trend_bungie','trend.Bungie'),('trend_maddison','trend.Maddison'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('quote_you','quote'),('quote_this','quote'),('repost_just','repost'),
    ('trend_bronny','trend.Bronny'),('trend_newmexico','trend.New Mexico'),('trend_daltonknecht','trend.Dalton Knecht'),('trend_kimjongun','trend.Kim Jong Un'),('trend_coys','trend.#COYS'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x) in ('trend.New America',): return 'politics'  # 2000Z",
    "        if str(_x) in ('trend.New Mexico',): return 'politics'  # 2100Z: the New America renaming call\n        if str(_x) in ('trend.Bronny','trend.Dalton Knecht','trend.#COYS'): return 'sports'  # 2100Z: Lakers waive Dalton Knecht; Tottenham win\n        if str(_x) in ('trend.New America',): return 'politics'  # 2000Z")
rep("if _c.endswith('2000Z.json') and '/19/' in _c: continue","if _c.endswith('2100Z.json') and '/19/' in _c: continue")
rep("then (20Z is a fourth hour) the rest of the last 24 hours, slowest growing last; 479 ids before the 400 cap, the 79 slowest-growing fourth-hour ids left out (cited posts were placed ahead of the fourth-hour tier, as in 1620Z);",
    "(21Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;")
rep("""trend names "New America", Howie, Bungie, Maddison (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 1909Z; #Fallout76Giveaway not read, a giveaway); quote/repost words the/what/it + my; sensors news/money/science;""",
    """trend names Bronny, "New Mexico", "Dalton Knecht", "Kim Jong Un", #COYS (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2000Z); quote/repost words is/you/this + just; sensors culture/sports/online;""")
rep("""'3 quote pages + 1 repost page, common words "the", "what", "it" and "my": (the lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each; a fourth quote read with the bare word and was rejected by X (ambiguous use of and as a keyword, as recorded in CAPABILITIES.md on 2026-10-15) and replaced with it'""",
    """'3 quote pages + 1 repost page, common words "is", "you", "this" and "just": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
rep("""        _last = '2026-10-19T1909Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T2000Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("reason = 'not due this run (two-hour desk, last ok 2026-10-19T1909Z, due 21:09Z)'","reason = 'not due this run (two-hour desk, last ok 2026-10-19T1909Z, due 21:09Z; this run started 21:00Z)'")
rep("reason = 'not due this run (four-hour desk, last ok 2026-10-19T1710Z, due 21:10Z)'","reason = 'not due this run (four-hour desk, last ok 2026-10-19T1710Z, due 21:10Z; this run started 21:00Z)'")
i=s.index("            f'Afternoon run (4:00 PM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Afternoon run (5:00 PM ET / 21:00 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 2000Z run ended at 412), parallel batches of up to 17, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; nothing left out by the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names Bronny, "New Mexico", "Dalton Knecht", "Kim Jong Un", #COYS (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2000Z; Bronny and Dalton Knecht are one event, the Lakers waiving Dalton Knecht; New Mexico is the New America renaming call, one event with the New America trend; Kim Jong Un is unconfirmed rumours of his death; #COYS is a Tottenham win, one event with the Tottenham and Maddison trends); '
            f'quote/repost words is/you/this + just (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 2000Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; two-hour desks last ok 1909Z, due 21:09Z; four-hour desks last ok 1710Z, due 21:10Z (this run started 21:00Z); '
"""+s[j:]
rep("(a 99-id read and a 21-id read)","(a 100-id read and a 26-id read)")
rep("out_path = f'{REPO}/capture/2026/10/19/2000Z.json'","out_path = f'{REPO}/capture/2026/10/19/2100Z.json'")
open('build_capture.py','w').write(s)
print('ok')
