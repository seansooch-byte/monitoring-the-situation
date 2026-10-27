s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, ('MISSING', a[:90]); s=s.replace(a,b)
rep('"""Build capture/2026/10/27/0405Z.json','"""Build capture/2026/10/27/0502Z.json')
rep("work/2026-10-27T0405Z'","work/2026-10-27T0502Z'")
rep("RUN_ID = '2026-10-27T0405Z'","RUN_ID = '2026-10-27T0502Z'")
rep("STARTED = '2026-10-27T04:05:00Z'","STARTED = '2026-10-27T05:02:00Z'")
rep("OBS_AT = '2026-10-27T04:06:00Z'","OBS_AT = '2026-10-27T05:04:00Z'")
rep("READS_BEFORE = 912","READS_BEFORE = 892")
rep("datetime(2026,10,27,4,6,tzinfo=timezone.utc).timestamp()  # 0405Z (","datetime(2026,10,27,5,4,tzinfo=timezone.utc).timestamp()  # 0502Z (0405Z used 04:06, ")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_wweraw': 'trend_wweraw.txt', 'trend_mckee': 'trend_mckee.txt', 'trend_winourway': 'trend_winourway.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_yaxel': 'trend_yaxel.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_eagles': 'trend_eagles.txt', 'trend_jayz': 'trend_jayz.txt', 'trend_cowboys': 'trend_cowboys.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""")
rep("""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_wweraw','trend.#WWERaw'),('trend_mckee','trend.Tanner McKee'),('trend_winourway','trend.#WinOurWay'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_yaxel','trend.Yaxel'),('trend_brewers','trend.Brewers'),('trend_eagles','trend.Eagles'),('trend_jayz','trend.Jay-Z'),('trend_cowboys','trend.Cowboys'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""")
rep("        if str(_x) in ('trend.#WinOurWay','trend.Tanner McKee','trend.#WWERaw'): return 'sports'  # 0405Z",
    "        if str(_x) in ('trend.Yaxel','trend.Brewers','trend.Eagles','trend.Cowboys'): return 'sports'  # 0502Z: Yaxel Lendeborg 31 points in Warriors win over the Nuggets; Brewers World Series Game 3 win; Cowboys beat Eagles on Monday Night Football\n        if str(_x) in ('trend.#WinOurWay','trend.Tanner McKee','trend.#WWERaw'): return 'sports'  # 0405Z")
rep("if _c.endswith('0405Z.json') and '/27/' in _c: continue","if _c.endswith('0502Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
TN_SHORT='trend names "Yaxel", "Brewers", "Eagles", "Jay-Z" and "Cowboys"'
EV=('top-ten US names with no posts attached in 0405Z; "Yaxel" (fourth, new) is Warriors rookie Yaxel Lendeborg (31 points, 12 rebounds in the Warriors\' first win of the season, over the Nuggets); '
    '"Brewers" (first) is one event with "Rays" (fifth) (the Brewers beat the Rays 10-1 in World Series Game 3, one win from the title); "Eagles" (second) and "Cowboys" (third) are one event with "Saquon" (tenth) (Cowboys beat the Eagles 38-21 on Monday Night Football); '
    '"Jay-Z" (seventh) is the Super Bowl LXI halftime headliner announcement; "Rays" and "Saquon" were not searched for the budget (one event with names searched); "#WWERaw", "Tanner McKee" and "#WinOurWay" had posts attached in 0405Z')
rep("(this 04Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 602 long, so the 400 cap left out the 84 last six-hour posts, the 43 slowest-growing still-gaining posts, the 69 rest-of-24-hour posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392), because the 295 watch.json ids plus 113 cited ids came to 408; no pulse-cited post was left out)",
    "(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 537 long, so the 400 cap left out the 88 last six-hour posts, the 43 slowest-growing still-gaining posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392), because the 295 watch.json ids plus 113 cited ids came to 408; no pulse-cited post was left out)")
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 then 30 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 8 third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)''',
    '''common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)''')
rep("_last = '2026-10-27T0302Z'","_last = '2026-10-27T0405Z'")
rep("(rotation: news/money/science read this run;","(rotation: culture/sports/online read this run;")
rep("Night run (12:05 AM ET Oct 27 / 04:05 UTC Oct 27, the 04Z slot;","Night run (1:02 AM ET Oct 27 / 05:02 UTC Oct 27, the 05Z slot;")
rep("0302Z ended at 912,","0405Z ended at 892,")
rep("04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 602 ids, so the 400 cap left out the 84 last six-hour posts, the 43 slowest-growing still-gaining posts, the 69 rest-of-24-hour posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 295 watch.json ids plus 113 cited ids came to 408); no pulse-cited post was left out; 4 reads)",
    "05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 537 ids, so the 400 cap left out the 88 last six-hour posts, the 43 slowest-growing still-gaining posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 295 watch.json ids plus 113 cited ids came to 408); no pulse-cited post was left out; 4 reads)")
i=s.index("            f'trend names \"#WWERaw\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (5 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words that/just + what (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online read 0302Z, so news/money/science were next in rotation); ",
    "quote/repost words the/this + is (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0405Z, so culture/sports/online were next in rotation); ")
rep("one hundred and sixty-sixth run","one hundred and sixty-seventh run")
rep("one hundred and sixty-third run","one hundred and sixty-fourth run")
rep("two screening reads by id: 99 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned but 2108062331095908717, Not Found again), then 22 second-hop posts (all returned but 2108062331095908717, Not Found again); 13 third-hop posts",
    "two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 2042119594282823945 came back Authorization Error as a referenced post), then 30 second-hop posts (all returned; 2108062331095908717 came back Not Found again as a referenced post); 8 third-hop posts")
rep("as in 2026-10-26T1204Z through 2026-10-27T0302Z;","as in 2026-10-26T1204Z through 2026-10-27T0405Z;")
rep("Not read: culture/sports/online sensors,","Not read: news/money/science sensors,")
rep("capture/2026/10/27/0405Z.json'","capture/2026/10/27/0502Z.json'")
open('build_capture.py','w').write(s); print('ok')
