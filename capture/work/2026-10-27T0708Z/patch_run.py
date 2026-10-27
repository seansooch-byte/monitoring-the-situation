s=open('build_capture.py').read()
def rep(a,b,cnt=None):
    global s
    assert a in s, ('MISSING', a[:90])
    if cnt: assert s.count(a)==cnt,(a[:60],s.count(a))
    s=s.replace(a,b)
rep('"""Build capture/2026/10/27/0607Z.json','"""Build capture/2026/10/27/0708Z.json')
rep("work/2026-10-27T0607Z'","work/2026-10-27T0708Z'")
rep("RUN_ID = '2026-10-27T0607Z'","RUN_ID = '2026-10-27T0708Z'")
rep("STARTED = '2026-10-27T06:07:00Z'","STARTED = '2026-10-27T07:08:00Z'")
rep("OBS_AT = '2026-10-27T06:08:00Z'","OBS_AT = '2026-10-27T07:09:00Z'")
rep("READS_BEFORE = 870","READS_BEFORE = 851")
rep("datetime(2026,10,27,6,8,tzinfo=timezone.utc).timestamp()  # 0607Z (","datetime(2026,10,27,7,9,tzinfo=timezone.utc).timestamp()  # 0708Z (0607Z used 06:08, ")
rep("""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_rays': 'trend_rays.txt', 'trend_saquon': 'trend_saquon.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_unite': 'trend_unite.txt', 'trend_nuggets': 'trend_nuggets.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_rays','trend.Rays'),('trend_saquon','trend.Saquon'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_unite','trend.Unite'),('trend_nuggets','trend.Nuggets'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x) in ('trend.Rays','trend.Saquon'): return 'sports'  # 0607Z",
    "        if str(_x) == 'trend.Unite': return 'gaming'  # 0708Z: Pokémon UNITE end of service announced for March 23, 2027\n        if str(_x) == 'trend.Nuggets': return 'sports'  # 0708Z: Warriors beat the Nuggets 134-114, Yaxel Lendeborg 31 points\n        if str(_x) in ('trend.Rays','trend.Saquon'): return 'sports'  # 0607Z",2)
rep("if _c.endswith('0607Z.json') and '/27/' in _c: continue","if _c.endswith('0708Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
TN_SHORT='trend names "Unite" and "Nuggets"'
EV=('top-ten US names with no posts attached in 0607Z; "Unite" (eighth) is Pokémon UNITE (end of service announced for March 23, 2027); several "unite" results are about other things (political calls to unite, Uganda, Kenya, Iranian rallies) and were kept off the trend; "Nuggets" (ninth) is one event with "Yaxel" (fourth) (the Warriors beat the Nuggets 134-114, rookie Yaxel Lendeborg 31 points and 12 rebounds); a chicken-nuggets joke and two spam posts were kept off the trend; '
    '"Jay-Z" (sixth) and "#WWERaw" (seventh) had posts attached in 0502Z and 0405Z and "Tanner McKee" (tenth) is one event with "Eagles" and "Cowboys" (posts attached in 0607Z); they were not searched for the budget')
NEW5="5 story-cited posts not on the pulse (2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392"
rep("(this 06Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 548 long, so the 400 cap left out the 102 last six-hour posts, the 41 slowest-growing still-gaining posts and "+NEW5+"), because the 294 watch.json ids plus 113 cited ids came to 407; no pulse-cited post was left out)",
    "(this 07Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 529 long, so the 400 cap left out the 85 last six-hour posts, the 39 slowest-growing still-gaining posts and "+NEW5+"), because the 294 watch.json ids plus 113 cited ids came to 407; no pulse-cited post was left out)")
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 then 42 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; THIRDHOP third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)''',
    '''common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)''')
rep("_last = '2026-10-27T0502Z'","_last = '2026-10-27T0607Z'")
rep("(rotation: news/money/science read this run;","(rotation: culture/sports/online read this run;")
i=s.index("            f'Overnight run (2:07 AM ET Oct 27"); j=s.index("\n",i)
s=s[:i]+"            f'Overnight run (3:08 AM ET Oct 27 / 07:08 UTC Oct 27, the 07Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0607Z ended at 851, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"+s[j:]
rep("06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 548 ids, so the 400 cap left out the 102 last six-hour posts, the 41 slowest-growing still-gaining posts and "+NEW5+"; 294 watch.json ids plus 113 cited ids came to 407); no pulse-cited post was left out; 4 reads)",
    "07Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 529 ids, so the 400 cap left out the 85 last six-hour posts, the 39 slowest-growing still-gaining posts and "+NEW5+"; 294 watch.json ids plus 113 cited ids came to 407); no pulse-cited post was left out; 4 reads)")
i=s.index("            f'trend names \"Rays\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (2 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words you/and + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online read 0502Z, so news/money/science were next in rotation); ",
    "quote/repost words it/that + just (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0607Z, so culture/sports/online were next in rotation); ")
rep("one hundred and sixty-eighth run","one hundred and sixty-ninth run")
rep("one hundred and sixty-fifth run","one hundred and sixty-sixth run")
rep("two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 2108062331095908717 came back Not Found again as a referenced post), then 31 second-hop posts (all returned); 11 third-hop posts",
    "two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 1557072144793731073 came back Authorization Error as a referenced post), then 42 second-hop posts (all returned; 2108062331095908717 came back Not Found again as a referenced post); THIRDHOP third-hop posts")
rep("as in 2026-10-26T1204Z through 2026-10-27T0502Z;","as in 2026-10-26T1204Z through 2026-10-27T0607Z;")
rep("Not read: culture/sports/online sensors,","Not read: news/money/science sensors,")
rep("capture/2026/10/27/0607Z.json'","capture/2026/10/27/0708Z.json'")
open('build_capture.py','w').write(s); print('ok')
