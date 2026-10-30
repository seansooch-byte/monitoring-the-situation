s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)>=1, ('MISSING', a[:80])
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('"""Build capture/2026/10/27/0011Z.json','"""Build capture/2026/10/27/0105Z.json')
rep("work/2026-10-27T0011Z'","work/2026-10-27T0105Z'")
rep("RUN_ID = '2026-10-27T0011Z'","RUN_ID = '2026-10-27T0105Z'")
rep("STARTED = '2026-10-27T00:11:00Z'","STARTED = '2026-10-27T01:05:00Z'")
rep("OBS_AT = '2026-10-27T00:12:00Z'","OBS_AT = '2026-10-27T01:06:00Z'")
rep("READS_BEFORE = 1000","READS_BEFORE = 978")
rep("datetime(2026,10,27,0,12,tzinfo=timezone.utc).timestamp()  # 0011Z (","datetime(2026,10,27,1,6,tzinfo=timezone.utc).timestamp()  # 0105Z (0011Z used 00:12, ")
rep("""    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_comey': 'trend_comey.txt', 'trend_meleek': 'trend_meleek.txt', 'trend_donnie': 'trend_donnie.txt', 'trend_reimer': 'trend_reimer.txt', 'trend_eagles': 'trend_eagles.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_cowboys': 'trend_cowboys.txt', 'trend_wweraw': 'trend_wweraw.txt', 'trend_saquon': 'trend_saquon.txt', 'trend_chandler': 'trend_chandler.txt', 'trend_mckee': 'trend_mckee.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""")
rep("""    ('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_comey','trend.Comey'),('trend_meleek','trend.Meleek Thomas'),('trend_donnie','trend.Donnie Iris'),('trend_reimer','trend.Reimer'),('trend_eagles','trend.#FlyEaglesFly'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_cowboys','trend.Cowboys'),('trend_wweraw','trend.#WWERaw'),('trend_saquon','trend.Saquon'),('trend_chandler','trend.Chandler Simpson'),('trend_mckee','trend.Tanner McKee'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""")
rep("        if str(_x) in ('trend.Meleek Thomas','trend.Reimer','trend.#FlyEaglesFly'): return 'sports'  # 0011Z",
 "        if str(_x) in ('trend.Cowboys','trend.Saquon','trend.Tanner McKee','trend.Chandler Simpson','trend.#WWERaw'): return 'sports'  # 0105Z: Cowboys-Eagles Monday Night Football (Saquon Barkley, Tanner McKee); Chandler Simpson catch (MLB postseason); WWE Raw (wrestling beat)\n        if str(_x) in ('trend.Meleek Thomas','trend.Reimer','trend.#FlyEaglesFly'): return 'sports'  # 0011Z")
rep("if _c.endswith('0011Z.json') and '/27/' in _c: continue","if _c.endswith('0105Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
WATCH_OLD="(this 00Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 617 long, so the 400 cap left out the 62 last six-hour posts, the 79 slowest-growing still-gaining posts and the 76 rest-of-24-hour posts, and no cited post)"
WATCH_NEW="(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 551 long, so the 400 cap left out the 80 last six-hour posts, the 70 slowest-growing still-gaining posts and one story-cited post, 2114425377338634392 (not on the pulse; the watch.json and cited ids alone came to 401))"
rep(WATCH_OLD,WATCH_NEW)
TN_OLD='''trend names "Comey", "Meleek Thomas", "Donnie Iris", "Reimer" and "#FlyEaglesFly" ("<name> lang:en is:retweet", newest first, 25 each; "Comey" (third), "Meleek Thomas" (seventh distinct, new), "Donnie Iris" (eighth, new), "Reimer" (ninth, new) and "#FlyEaglesFly" (tenth, new) are top-ten US names with no posts attached in 2302Z; "Comey" is one event with "James Comey" (the new charges against the former FBI director); "World Cup" (fifth) and "Messi" (sixth) are one event with "#BallonDor" (the Ballon d’Or ceremony) and were not searched separately; "Harry Kane" (first), "#BallonDor" (second) and "Mbappe" (fourth, listed twice) had posts attached in 2302Z); quote/repost words my/it + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 then 17 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 7 third-hop posts left unread for the budget;'''
TN_NEW='''trend names "Cowboys", "#WWERaw", "Saquon", "Chandler Simpson" and "Tanner McKee" ("<name> lang:en is:retweet", newest first, 25 each; "Cowboys" (first, new), "#WWERaw" (second, new), "Saquon" (fourth, new), "Chandler Simpson" (fifth, new) and "Tanner McKee" (ninth, new) are top-ten US names with no posts attached in 0011Z; "Cowboys", "Saquon" and "Tanner McKee" are one event with "#FlyEaglesFly" (Cowboys at Eagles on Monday Night Football); "Sami" (tenth) is one event with "#WWERaw" (Sami Zayn on WWE Raw) and was not searched separately; "Comey" (seventh) and "#FlyEaglesFly" (sixth) had posts attached in 0011Z; "Harry Kane" (third) and "#BallonDor" (eighth) had posts attached in 2302Z and were not searched again); quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 93 then 15 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 5 third-hop posts left unread for the budget;'''
rep(TN_OLD,TN_NEW)
rep('''common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)''',
 '''common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)''')
rep("_last = '2026-10-26T2302Z'\n        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science read this run;",
 "_last = '2026-10-27T0011Z'\n        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online read this run;")
rep("f'Evening run (8:11 PM ET Oct 26 / 00:11 UTC Oct 27, the 00Z slot and the first run of the new UTC day; 12:00-05:00 UTC band, up to 42, kept to about 22 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the X day reset at 00:00 UTC)",
 "f'Evening run (9:05 PM ET Oct 26 / 01:05 UTC Oct 27, the 01Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0011Z ended at 978, so no reads went elsewhere in between)")
rep("00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 617 ids, so the 400 cap left out the 62 last six-hour posts, the 79 slowest-growing still-gaining posts and the 76 rest-of-24-hour posts, and no cited post; 4 reads)",
 "01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 551 ids, so the 400 cap left out the 80 last six-hour posts, the 70 slowest-growing still-gaining posts and one story-cited post not on the pulse (2114425377338634392: the watch.json and cited ids alone came to 401); 4 reads)")
rep('''f'trend names "Comey", "Meleek Thomas", "Donnie Iris", "Reimer" and "#FlyEaglesFly" (5 reads; "<name> lang:en is:retweet", newest first, 25; top-ten US names with no posts attached in 2302Z; "Comey" is the new charges against James Comey; "World Cup" and "Messi" are one event with "#BallonDor" (the Ballon d’Or ceremony) and were not searched separately; "Harry Kane", "#BallonDor" and "Mbappe" had posts attached in 2302Z); \'''',
 '''f'trend names "Cowboys", "#WWERaw", "Saquon", "Chandler Simpson" and "Tanner McKee" (5 reads; "<name> lang:en is:retweet", newest first, 25; top-ten US names with no posts attached in 0011Z; "Cowboys", "Saquon" and "Tanner McKee" are one event with "#FlyEaglesFly" (Cowboys at Eagles on Monday Night Football); "Sami" is one event with "#WWERaw" and was not searched separately; "Chandler Simpson" is a catch in an MLB postseason game; "Comey" and "#FlyEaglesFly" had posts attached in 0011Z, "Harry Kane" and "#BallonDor" in 2302Z); \'''')
rep("f'quote/repost words my/it + that (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2302Z, so news/money/science were next in rotation); '",
 "f'quote/repost words just/what + the (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0011Z, so culture/sports/online were next in rotation); '")
rep("cut for the one hundred and sixty-second run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and fifty-ninth run",
 "cut for the one hundred and sixty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and sixtieth run")
rep("f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 17 left over, including the second-hop posts (all returned but 2108062331095908717, Not Found again in both reads); 7 third-hop posts were left unread for the budget",
 "f'two screening reads by id: 93 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned but 2108062331095908717, Not Found again, and 2114695684938989568, Not Found), then 15 second-hop posts (all returned); 5 third-hop posts were left unread for the budget")
rep("as in 2026-10-26T1204Z through 2302Z;","as in 2026-10-26T1204Z through 2026-10-27T0011Z;")
rep("f'Not read: culture/sports/online sensors,","f'Not read: news/money/science sensors,")
rep("capture/2026/10/27/0011Z.json'","capture/2026/10/27/0105Z.json'")
open('build_capture.py','w').write(s); print('ok')
