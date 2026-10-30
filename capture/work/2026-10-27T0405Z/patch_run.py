s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, ('MISSING', a[:90]); s=s.replace(a,b)
rep('"""Build capture/2026/10/27/0302Z.json','"""Build capture/2026/10/27/0405Z.json')
rep("work/2026-10-27T0302Z'","work/2026-10-27T0405Z'")
rep("RUN_ID = '2026-10-27T0302Z'","RUN_ID = '2026-10-27T0405Z'")
rep("STARTED = '2026-10-27T03:02:00Z'","STARTED = '2026-10-27T04:05:00Z'")
rep("OBS_AT = '2026-10-27T03:04:00Z'","OBS_AT = '2026-10-27T04:06:00Z'")
rep("READS_BEFORE = 934","READS_BEFORE = 912")
rep("datetime(2026,10,27,3,4,tzinfo=timezone.utc).timestamp()  # 0302Z (","datetime(2026,10,27,4,6,tzinfo=timezone.utc).timestamp()  # 0405Z (0302Z used 03:04, ")
rep("""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_jayz': 'trend_jayz.txt', 'trend_giannis': 'trend_giannis.txt', 'trend_eagles': 'trend_eagles.txt', 'trend_rays': 'trend_rays.txt', 'trend_worldseries': 'trend_worldseries.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_wweraw': 'trend_wweraw.txt', 'trend_mckee': 'trend_mckee.txt', 'trend_winourway': 'trend_winourway.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_jayz','trend.Jay-Z'),('trend_giannis','trend.Giannis'),('trend_eagles','trend.Eagles'),('trend_rays','trend.Rays'),('trend_worldseries','trend.#WorldSeries'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""",
"""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_wweraw','trend.#WWERaw'),('trend_mckee','trend.Tanner McKee'),('trend_winourway','trend.#WinOurWay'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) == 'trend.Jay-Z': return 'music'",
 "        if str(_x) in ('trend.#WinOurWay','trend.Tanner McKee','trend.#WWERaw'): return 'sports'  # 0405Z: Brewers World Series Game 3 win (#WinOurWay); Tanner McKee in Cowboys-Eagles Monday Night Football; WWE Raw (wrestling beat)\n        if str(_x) == 'trend.Jay-Z': return 'music'")
rep("if _c.endswith('0302Z.json') and '/27/' in _c: continue","if _c.endswith('0405Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
TN_SHORT='trend names "#WWERaw", "Tanner McKee" and "#WinOurWay"'
EV=('top-ten US names with no posts attached in 0302Z; "#WWERaw" (fourth) is WWE Raw (John Cena announced for next week in Brooklyn; Liv Morgan keeps the Women\'s World Title by DQ); '
    '"Tanner McKee" (seventh) is one event with "Eagles" (second), "Cowboys" (third) and "Saquon" (eighth) (Cowboys beat the Eagles on Monday Night Football); "#WinOurWay" (ninth) is one event with "Brewers" (first), "Rays" (fifth) and "#WorldSeries" (tenth) (the Brewers rout the Rays in World Series Game 3); '
    'the other seven top-ten names had posts attached in 0302Z, so only three names were searched')
rep("(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 546 long, so the 400 cap left out the 92 last six-hour posts, the 51 slowest-growing still-gaining posts and 3 story-cited posts not on the pulse (2113656547834487022, 2114085789139140865, 2114425377338634392), because the 292 watch.json ids plus 113 cited ids came to 405)",
    "(this 04Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 602 long, so the 400 cap left out the 84 last six-hour posts, the 43 slowest-growing still-gaining posts, the 69 rest-of-24-hour posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392), because the 295 watch.json ids plus 113 cited ids came to 408; no pulse-cited post was left out)")
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 99 then 22 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 13 third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)''',
    '''common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)''')
rep("_last = '2026-10-27T0204Z'","_last = '2026-10-27T0302Z'")
rep("(rotation: culture/sports/online read this run;","(rotation: news/money/science read this run;")
rep("Night run (11:02 PM ET Oct 26 / 03:02 UTC Oct 27, the 03Z slot;","Night run (12:05 AM ET Oct 27 / 04:05 UTC Oct 27, the 04Z slot;")
rep("0204Z ended at 934,","0302Z ended at 912,")
rep("03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 546 ids, so the 400 cap left out the 92 last six-hour posts, the 51 slowest-growing still-gaining posts and 3 story-cited posts not on the pulse (2113656547834487022, 2114085789139140865, 2114425377338634392; 292 watch.json ids plus 113 cited ids came to 405); 4 reads)",
    "04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 602 ids, so the 400 cap left out the 84 last six-hour posts, the 43 slowest-growing still-gaining posts, the 69 rest-of-24-hour posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 295 watch.json ids plus 113 cited ids came to 408); no pulse-cited post was left out; 4 reads)")
i=s.index("            f'trend names \"Jay-Z\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (3 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words and/my + it (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0204Z, so culture/sports/online were next in rotation); ",
    "quote/repost words that/just + what (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online read 0302Z, so news/money/science were next in rotation); ")
rep("one hundred and sixty-fifth run","one hundred and sixty-sixth run")
rep("one hundred and sixty-second run","one hundred and sixty-third run")
rep("two screening reads by id: 93 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 2113778211687641178 and 2108062331095908717 came back Not Found as referenced posts), then 18 second-hop posts (all returned but 2113778211687641178 and 2108062331095908717, Not Found); 7 third-hop posts",
    "two screening reads by id: 99 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned but 2108062331095908717, Not Found again), then 22 second-hop posts (all returned but 2108062331095908717, Not Found again); 13 third-hop posts")
rep("as in 2026-10-26T1204Z through 2026-10-27T0204Z;","as in 2026-10-26T1204Z through 2026-10-27T0302Z;")
rep("Not read: news/money/science sensors,","Not read: culture/sports/online sensors,")
rep("capture/2026/10/27/0302Z.json'","capture/2026/10/27/0405Z.json'")
open('build_capture.py','w').write(s); print('ok')
