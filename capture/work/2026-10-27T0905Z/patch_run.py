s=open('build_capture.py').read()
def rep(a,b,cnt=None):
    global s
    assert a in s, ('MISSING', a[:90])
    if cnt: assert s.count(a)==cnt,(a[:60],s.count(a))
    s=s.replace(a,b)
rep('"""Build capture/2026/10/27/0708Z.json','"""Build capture/2026/10/27/0800Z.json')
rep("work/2026-10-27T0708Z'","work/2026-10-27T0800Z'")
rep("RUN_ID = '2026-10-27T0708Z'","RUN_ID = '2026-10-27T0800Z'")
rep("STARTED = '2026-10-27T07:08:00Z'","STARTED = '2026-10-27T08:00:00Z'")
rep("OBS_AT = '2026-10-27T07:09:00Z'","OBS_AT = '2026-10-27T08:01:00Z'")
rep("READS_BEFORE = 851","READS_BEFORE = 832")
rep("datetime(2026,10,27,7,9,tzinfo=timezone.utc).timestamp()  # 0708Z (","datetime(2026,10,27,8,2,tzinfo=timezone.utc).timestamp()  # 0800Z (0708Z used 07:09, ")
rep("""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_unite': 'trend_unite.txt', 'trend_nuggets': 'trend_nuggets.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_sneako': 'trend_sneako.txt', 'trend_brewers': 'trend_brewers.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_unite','trend.Unite'),('trend_nuggets','trend.Nuggets'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_sneako','trend.Sneako'),('trend_brewers','trend.Brewers'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) == 'trend.Unite': return 'gaming'  # 0708Z",
    "        if str(_x) == 'trend.Sneako': return 'internet'  # 0800Z: Sneako and DJ Akademiks argument on an Adin Ross stream\n        if str(_x) == 'trend.Unite': return 'gaming'  # 0708Z",2)
rep("if _c.endswith('0708Z.json') and '/27/' in _c: continue","if _c.endswith('0800Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
TN_SHORT='trend names "Brewers" and "Sneako"'
EV=('top-ten US names with no posts attached in 0708Z; "Brewers" (first) is the Brewers win over the Rays in World Series Game 3 (one event with "Rays" (sixth)); "Sneako" (tenth, new) is Sneako and DJ Akademiks arguing on an Adin Ross stream; '
    '"Eagles" (second), "Cowboys" (fourth) and "Jay-Z" (fifth) had posts attached in 0607Z and 0502Z, "Yaxel" (third) is one event with "Nuggets" (posts attached in 0708Z) and "#WWERaw" (eighth) had posts attached in 0405Z; they were not searched for the budget')
CAP="the list was 533 long, so the 400 cap left out the 94 last six-hour posts, the 35 slowest-growing still-gaining posts and 4 story-cited posts not on the pulse (2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392), because the 293 watch.json ids plus 113 cited ids came to 406; no pulse-cited post was left out"
rep("(this 07Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 529 long, so the 400 cap left out the 85 last six-hour posts, the 39 slowest-growing still-gaining posts and 5 story-cited posts not on the pulse (2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392), because the 294 watch.json ids plus 113 cited ids came to 407; no pulse-cited post was left out)",
    "(this 08Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, "+CAP+")")
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words what/the + this (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 93 then 14 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 6 third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)''',
    '''common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)''')
rep("_last = '2026-10-27T0607Z'","_last = '2026-10-27T0708Z'")
rep("(rotation: culture/sports/online read this run;","(rotation: news/money/science read this run;")
i=s.index("            f'Overnight run (3:08 AM ET Oct 27"); j=s.index("\n",i)
s=s[:i]+"            f'Overnight run (4:00 AM ET Oct 27 / 08:00 UTC Oct 27, the 08Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0708Z ended at 832, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"+s[j:]
rep("07Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 529 ids, so the 400 cap left out the 85 last six-hour posts, the 39 slowest-growing still-gaining posts and 5 story-cited posts not on the pulse (2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 294 watch.json ids plus 113 cited ids came to 407); no pulse-cited post was left out; 4 reads)",
    "08Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 533 ids, so the 400 cap left out the 94 last six-hour posts, the 35 slowest-growing still-gaining posts and 4 story-cited posts not on the pulse (2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 293 watch.json ids plus 113 cited ids came to 406); no pulse-cited post was left out; 4 reads)")
i=s.index("            f'trend names \"Unite\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (2 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words it/that + just (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0607Z, so culture/sports/online were next in rotation); ",
    "quote/repost words what/the + this (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online read 0708Z, so news/money/science were next in rotation); ")
rep("one hundred and sixty-ninth run","one hundred and seventieth run")
rep("one hundred and sixty-sixth run","one hundred and sixty-seventh run")
rep("two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 1557072144793731073 came back Authorization Error as a referenced post), then 42 second-hop posts (all returned; 2108062331095908717 came back Not Found again as a referenced post); 16 third-hop posts",
    "two screening reads by id: 93 unread referenced, reply-parent and media-source posts, most pointed-at first (91 returned; 2114436015800848759 came back Authorization Error and 2108062331095908717 Not Found again as referenced posts), then 14 second-hop posts (all returned); 6 third-hop posts")
rep("as in 2026-10-26T1204Z through 2026-10-27T0607Z;","as in 2026-10-26T1204Z through 2026-10-27T0708Z;")
rep("Not read: news/money/science sensors,","Not read: culture/sports/online sensors,")
rep("capture/2026/10/27/0708Z.json'","capture/2026/10/27/0800Z.json'")
open('build_capture.py','w').write(s); print('ok')
