s=open('build_capture.py').read()
def rep(a,b,cnt=None):
    global s
    assert a in s, ('MISSING', a[:90])
    if cnt: assert s.count(a)==cnt,(a[:60],s.count(a))
    s=s.replace(a,b)
rep('"""Build capture/2026/10/27/0502Z.json','"""Build capture/2026/10/27/0607Z.json')
rep("work/2026-10-27T0502Z'","work/2026-10-27T0607Z'")
rep("RUN_ID = '2026-10-27T0502Z'","RUN_ID = '2026-10-27T0607Z'")
rep("STARTED = '2026-10-27T05:02:00Z'","STARTED = '2026-10-27T06:07:00Z'")
rep("OBS_AT = '2026-10-27T05:04:00Z'","OBS_AT = '2026-10-27T06:08:00Z'")
rep("READS_BEFORE = 892","READS_BEFORE = 870")
rep("datetime(2026,10,27,5,4,tzinfo=timezone.utc).timestamp()  # 0502Z (","datetime(2026,10,27,6,8,tzinfo=timezone.utc).timestamp()  # 0607Z (0502Z used 05:04, ")
rep("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_yaxel': 'trend_yaxel.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_eagles': 'trend_eagles.txt', 'trend_jayz': 'trend_jayz.txt', 'trend_cowboys': 'trend_cowboys.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""",
"""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_rays': 'trend_rays.txt', 'trend_saquon': 'trend_saquon.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_yaxel','trend.Yaxel'),('trend_brewers','trend.Brewers'),('trend_eagles','trend.Eagles'),('trend_jayz','trend.Jay-Z'),('trend_cowboys','trend.Cowboys'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""",
"""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_rays','trend.Rays'),('trend_saquon','trend.Saquon'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) in ('trend.Yaxel','trend.Brewers','trend.Eagles','trend.Cowboys'): return 'sports'  # 0502Z",
    "        if str(_x) in ('trend.Rays','trend.Saquon'): return 'sports'  # 0607Z: Brewers beat the Rays in World Series Game 3; Saquon Barkley hamstring and back injury in the Cowboys win over the Eagles on Monday Night Football\n        if str(_x) in ('trend.Yaxel','trend.Brewers','trend.Eagles','trend.Cowboys'): return 'sports'  # 0502Z",2)
rep("if _c.endswith('0502Z.json') and '/27/' in _c: continue","if _c.endswith('0607Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
TN_SHORT='trend names "Rays" and "Saquon"'
EV=('top-ten US names with no posts attached in 0502Z; "Rays" (fifth) is one event with "Brewers" (first), "#WinOurWay" (ninth) and "#WorldSeries" (the Brewers beat the Rays 10-1 in World Series Game 3); "Saquon" (tenth) is one event with "Eagles" (second), "Cowboys" (third) and "Tanner McKee" (eighth) (Cowboys beat the Eagles 38-21 on Monday Night Football; Saquon Barkley said he tweaked his hamstring and hurt his back); '
    '"Jay-Z" (sixth) and "#WWERaw" (seventh) had posts attached in 0502Z and 0405Z; "Tanner McKee" and "#WinOurWay" were not searched for the budget (one event with names searched); several "Rays" results are about sun rays or Blu-rays, not the team, and were kept off the trend')
STALE6="6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392"
NEW5="5 story-cited posts not on the pulse (2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392"
rep("(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 537 long, so the 400 cap left out the 88 last six-hour posts, the 43 slowest-growing still-gaining posts and "+STALE6+"), because the 295 watch.json ids plus 113 cited ids came to 408; no pulse-cited post was left out)",
    "(this 06Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 548 long, so the 400 cap left out the 102 last six-hour posts, the 41 slowest-growing still-gaining posts and "+NEW5+"), because the 294 watch.json ids plus 113 cited ids came to 407; no pulse-cited post was left out)")
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 then 31 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 11 third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)''',
    '''common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)''')
rep("_last = '2026-10-27T0405Z'","_last = '2026-10-27T0502Z'")
rep("(rotation: culture/sports/online read this run;","(rotation: news/money/science read this run;")
i=s.index("            f'Night run (1:02 AM ET Oct 27"); j=s.index("\n",i)
s=s[:i]+"            f'Overnight run (2:07 AM ET Oct 27 / 06:07 UTC Oct 27, the 06Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0502Z ended at 870, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"+s[j:]
rep("05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 537 ids, so the 400 cap left out the 88 last six-hour posts, the 43 slowest-growing still-gaining posts and "+STALE6+"; 295 watch.json ids plus 113 cited ids came to 408); no pulse-cited post was left out; 4 reads)",
    "06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 548 ids, so the 400 cap left out the 102 last six-hour posts, the 41 slowest-growing still-gaining posts and "+NEW5+"; 294 watch.json ids plus 113 cited ids came to 407); no pulse-cited post was left out; 4 reads)")
i=s.index("            f'trend names \"Yaxel\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (2 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words the/this + is (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0405Z, so culture/sports/online were next in rotation); ",
    "quote/repost words you/and + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online read 0502Z, so news/money/science were next in rotation); ")
rep("one hundred and sixty-seventh run","one hundred and sixty-eighth run")
rep("one hundred and sixty-fourth run","one hundred and sixty-fifth run")
rep("two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 2042119594282823945 came back Authorization Error as a referenced post), then 30 second-hop posts (all returned; 2108062331095908717 came back Not Found again as a referenced post); 8 third-hop posts",
    "two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 2108062331095908717 came back Not Found again as a referenced post), then 31 second-hop posts (all returned); 11 third-hop posts")
rep("as in 2026-10-26T1204Z through 2026-10-27T0405Z;","as in 2026-10-26T1204Z through 2026-10-27T0502Z;")
rep("Not read: news/money/science sensors,","Not read: culture/sports/online sensors,")
rep("capture/2026/10/27/0502Z.json'","capture/2026/10/27/0607Z.json'")
open('build_capture.py','w').write(s); print('ok')
