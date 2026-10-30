s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)>=1, ('MISSING', a[:80])
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('"""Build capture/2026/10/27/0105Z.json','"""Build capture/2026/10/27/0204Z.json')
rep("work/2026-10-27T0105Z'","work/2026-10-27T0204Z'")
rep("RUN_ID = '2026-10-27T0105Z'","RUN_ID = '2026-10-27T0204Z'")
rep("STARTED = '2026-10-27T01:05:00Z'","STARTED = '2026-10-27T02:04:00Z'")
rep("OBS_AT = '2026-10-27T01:06:00Z'","OBS_AT = '2026-10-27T02:05:00Z'")
rep("READS_BEFORE = 978","READS_BEFORE = 956")
rep("datetime(2026,10,27,1,6,tzinfo=timezone.utc).timestamp()  # 0105Z (","datetime(2026,10,27,2,5,tzinfo=timezone.utc).timestamp()  # 0204Z (0105Z used 01:06, ")
rep("""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_cowboys': 'trend_cowboys.txt', 'trend_wweraw': 'trend_wweraw.txt', 'trend_saquon': 'trend_saquon.txt', 'trend_chandler': 'trend_chandler.txt', 'trend_mckee': 'trend_mckee.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""",
"""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_brewers': 'trend_brewers.txt', 'trend_worldseries': 'trend_worldseries.txt', 'trend_stokes': 'trend_stokes.txt', 'trend_bayley': 'trend_bayley.txt', 'trend_pickens': 'trend_pickens.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_cowboys','trend.Cowboys'),('trend_wweraw','trend.#WWERaw'),('trend_saquon','trend.Saquon'),('trend_chandler','trend.Chandler Simpson'),('trend_mckee','trend.Tanner McKee'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""",
"""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_brewers','trend.The Brewers'),('trend_worldseries','trend.#WorldSeries2026'),('trend_stokes','trend.Kiah Stokes'),('trend_bayley','trend.Bayley'),('trend_pickens','trend.Pickens'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) in ('trend.Cowboys','trend.Saquon','trend.Tanner McKee','trend.Chandler Simpson','trend.#WWERaw'): return 'sports'  # 0105Z",
 "        if str(_x) in ('trend.The Brewers','trend.#WorldSeries2026','trend.Kiah Stokes','trend.Bayley','trend.Pickens'): return 'sports'  # 0204Z: Brewers-Rays World Series Game 3 (#WorldSeries2026); Kiah Stokes in WNBA Finals Game 5; Bayley v Lyra Valkyria No DQ match on WWE Raw (wrestling beat); George Pickens catch on Monday Night Football\n        if str(_x) in ('trend.Cowboys','trend.Saquon','trend.Tanner McKee','trend.Chandler Simpson','trend.#WWERaw'): return 'sports'  # 0105Z")
rep("if _c.endswith('0105Z.json') and '/27/' in _c: continue","if _c.endswith('0204Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
WATCH_OLD="(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 551 long, so the 400 cap left out the 80 last six-hour posts, the 70 slowest-growing still-gaining posts and one story-cited post, 2114425377338634392 (not on the pulse; the watch.json and cited ids alone came to 401))"
WATCH_NEW="(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 549 long, so the 400 cap left out the 95 last six-hour posts and the 54 slowest-growing still-gaining posts, and no cited post)"
rep(WATCH_OLD,WATCH_NEW)
TN_OLD='''trend names "Cowboys", "#WWERaw", "Saquon", "Chandler Simpson" and "Tanner McKee" ("<name> lang:en is:retweet", newest first, 25 each; "Cowboys" (first, new), "#WWERaw" (second, new), "Saquon" (fourth, new), "Chandler Simpson" (fifth, new) and "Tanner McKee" (ninth, new) are top-ten US names with no posts attached in 0011Z; "Cowboys", "Saquon" and "Tanner McKee" are one event with "#FlyEaglesFly" (Cowboys at Eagles on Monday Night Football); "Sami" (tenth) is one event with "#WWERaw" (Sami Zayn on WWE Raw) and was not searched separately; "Comey" (seventh) and "#FlyEaglesFly" (sixth) had posts attached in 0011Z; "Harry Kane" (third) and "#BallonDor" (eighth) had posts attached in 2302Z and were not searched again); quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 93 then 15 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 5 third-hop posts left unread for the budget;'''
TN_NEW='''trend names "The Brewers", "Bayley", "#WorldSeries2026", "Kiah Stokes" and "Pickens" ("<name> lang:en is:retweet", newest first, 25 each; "The Brewers" (fourth, new), "Bayley" (fifth, new), "#WorldSeries2026" (sixth, new), "Kiah Stokes" (ninth, new) and "Pickens" (tenth, new) are top-ten US names with no posts attached in 0105Z; "The Brewers" and "#WorldSeries2026" are one event (Brewers 10, Rays 0 after an eight-run fifth in World Series Game 3); "Bayley" is one event with "#WWERaw" (Bayley v Lyra Valkyria, No DQ match); "Pickens" and "Eagles" (third, not searched separately) are one event with "Cowboys" (Cowboys at Eagles on Monday Night Football); "Kiah Stokes" is WNBA Finals Game 5; "Cowboys" (first), "#WWERaw" (second) and "Tanner McKee" (eighth) had posts attached in 0105Z; "Harry Kane" (seventh) had posts attached in 2302Z and was not searched again); quote/repost words this/is + you (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 95 then 16 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 8 third-hop posts left unread for the budget;'''
rep(TN_OLD,TN_NEW)
rep("sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each);","sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each);")
rep('''common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)''',
 '''common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)''')
rep("_last = '2026-10-27T0011Z'\n        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online read this run;",
 "_last = '2026-10-27T0105Z'\n        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science read this run;")
rep("f'Evening run (9:05 PM ET Oct 26 / 01:05 UTC Oct 27, the 01Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0011Z ended at 978, so no reads went elsewhere in between)",
 "f'Evening run (10:04 PM ET Oct 26 / 02:04 UTC Oct 27, the 02Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0105Z ended at 956, so no reads went elsewhere in between)")
rep("01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 551 ids, so the 400 cap left out the 80 last six-hour posts, the 70 slowest-growing still-gaining posts and one story-cited post not on the pulse (2114425377338634392: the watch.json and cited ids alone came to 401); 4 reads)",
 "02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 549 ids, so the 400 cap left out the 95 last six-hour posts and the 54 slowest-growing still-gaining posts, and no cited post; 4 reads)")
rep('''f'trend names "Cowboys", "#WWERaw", "Saquon", "Chandler Simpson" and "Tanner McKee" (5 reads; "<name> lang:en is:retweet", newest first, 25; top-ten US names with no posts attached in 0011Z; "Cowboys", "Saquon" and "Tanner McKee" are one event with "#FlyEaglesFly" (Cowboys at Eagles on Monday Night Football); "Sami" is one event with "#WWERaw" and was not searched separately; "Chandler Simpson" is a catch in an MLB postseason game; "Comey" and "#FlyEaglesFly" had posts attached in 0011Z, "Harry Kane" and "#BallonDor" in 2302Z); \'''',
 '''f'trend names "The Brewers", "Bayley", "#WorldSeries2026", "Kiah Stokes" and "Pickens" (5 reads; "<name> lang:en is:retweet", newest first, 25; top-ten US names with no posts attached in 0105Z; "The Brewers" and "#WorldSeries2026" are one event (Brewers 10, Rays 0 after an eight-run fifth in World Series Game 3); "Bayley" is one event with "#WWERaw" (Bayley v Lyra Valkyria, No DQ match); "Pickens" and "Eagles" (not searched separately) are one event with "Cowboys" (Monday Night Football); "Kiah Stokes" is WNBA Finals Game 5; "Cowboys", "#WWERaw" and "Tanner McKee" had posts attached in 0105Z, "Harry Kane" in 2302Z); \'''')
rep("f'quote/repost words just/what + the (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0011Z, so culture/sports/online were next in rotation); '",
 "f'quote/repost words this/is + you (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0105Z, so news/money/science were next in rotation); '")
rep("cut for the one hundred and sixty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and sixtieth run",
 "cut for the one hundred and sixty-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and sixty-first run")
rep("f'two screening reads by id: 93 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned but 2108062331095908717, Not Found again, and 2114695684938989568, Not Found), then 15 second-hop posts (all returned); 5 third-hop posts were left unread for the budget",
 "f'two screening reads by id: 95 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned but 2059067645266100350, Authorization Error), then 16 second-hop posts (all returned but 2108062331095908717, Not Found again); 8 third-hop posts were left unread for the budget")
rep("as in 2026-10-26T1204Z through 2026-10-27T0011Z;","as in 2026-10-26T1204Z through 2026-10-27T0105Z;")
rep("f'Not read: news/money/science sensors,","f'Not read: culture/sports/online sensors,")
rep("f'Left out this run: 2114689594507800986 (SaksLikely video of a killing in Cleveland, graphic). Skipped","f'{LEFT_OUT_NOTE}Skipped")
rep("capture/2026/10/27/0105Z.json'","capture/2026/10/27/0204Z.json'")
open('build_capture.py','w').write(s); print('ok')
