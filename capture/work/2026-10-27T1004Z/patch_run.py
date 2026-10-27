s=open('build_capture.py').read()
def rep(a,b,cnt=None):
    global s
    assert a in s, ('MISSING', a[:90])
    if cnt: assert s.count(a)==cnt,(a[:60],s.count(a))
    s=s.replace(a,b)
rep('"""Build capture/2026/10/27/0905Z.json','"""Build capture/2026/10/27/1004Z.json')
rep("work/2026-10-27T0905Z'","work/2026-10-27T1004Z'")
rep("RUN_ID = '2026-10-27T0905Z'","RUN_ID = '2026-10-27T1004Z'")
rep("STARTED = '2026-10-27T09:05:00Z'","STARTED = '2026-10-27T10:04:00Z'")
rep("OBS_AT = '2026-10-27T09:06:00Z'","OBS_AT = '2026-10-27T10:05:00Z'")
rep("READS_BEFORE = 813","READS_BEFORE = 794")
rep("datetime(2026,10,27,9,6,tzinfo=timezone.utc).timestamp()  # 0905Z (","datetime(2026,10,27,10,5,tzinfo=timezone.utc).timestamp()  # 1004Z (0905Z used 09:06, ")
rep("""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_is': 'repost_is.txt',
    'trend_cowboys': 'trend_cowboys.txt', 'trend_yaxel': 'trend_yaxel.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_comey': 'trend_comey.txt', 'trend_brewers': 'trend_brewers.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_you','quote'),('quote_and','quote'),('repost_is','repost'),
    ('trend_cowboys','trend.Cowboys'),('trend_yaxel','trend.Yaxel'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_comey','trend.Comey'),('trend_brewers','trend.Brewers'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("if _c.endswith('0905Z.json') and '/27/' in _c: continue","if _c.endswith('1004Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
TN_SHORT='trend names "Brewers" and "Comey"'
EV=('top-ten US names with no posts attached in 0905Z; "Brewers" (second) is the Brewers win over the Rays in the World Series (one event with "Rays" (eighth)); "Comey" (tenth, new to the top ten) is the new federal charges against James Comey; '
    '"Good Tuesday" (first) is a greeting, and "Unite" (fourth), "Jay-Z" (sixth), "Sneako" (seventh), "Rays" (eighth) and "#WWERaw" (ninth) had posts attached in earlier runs today; they were not searched for the budget; "Eagles" (third) and "Yaxel" (fifth) had posts attached in 0905Z')
CAP="the list was 528 long, so the 400 cap left out the 89 last six-hour posts, the 33 slowest-growing still-gaining posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 2113455120692195588 was read in screening as a referenced post), because the 295 watch.json ids plus 113 cited ids came to 408; no pulse-cited post was left out"
i=s.index("(this 09Z run is not a fourth hour;"); j=s.index("); {len(watch_ids)} ids read",i)
s=s[:i]+"(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, "+CAP+")"+s[j+1:]
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words my/it + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 97 then 22 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 7 third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "you", "and" and "is", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)''',
    '''common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)''')
rep("_last = '2026-10-27T0800Z'","_last = '2026-10-27T0905Z'")
rep("(rotation: culture/sports/online read this run;","(rotation: news/money/science read this run;")
i=s.index("            f'Overnight run (5:05 AM ET Oct 27"); j=s.index("\n",i)
s=s[:i]+"            f'Overnight run (6:04 AM ET Oct 27 / 10:04 UTC Oct 27, the 10Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0905Z ended at 794, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"+s[j:]
i=s.index("09Z is not a fourth hour: the watch.json ids"); j=s.index("no pulse-cited post was left out; 4 reads)",i)
s=s[:i]+"10Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 528 ids, so the 400 cap left out the 89 last six-hour posts, the 33 slowest-growing still-gaining posts and 6 story-cited posts not on the pulse (2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 295 watch.json ids plus 113 cited ids came to 408; 2113455120692195588 was read in screening as a referenced post); "+s[j:]
i=s.index("            f'trend names \"Cowboys\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (2 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words you/and + is (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0800Z, so culture/sports/online were next in rotation); ",
    "quote/repost words my/it + that (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online read 0905Z, so news/money/science were next in rotation); ")
rep("one hundred and seventy-first run","one hundred and seventy-second run")
rep("one hundred and sixty-eighth run","one hundred and sixty-ninth run")
i=s.index("two screening reads by id: 100 unread referenced"); j=s.index("(ids left out earlier as likely paid",i)
s=s[:i]+"two screening reads by id: 97 unread referenced, reply-parent and media-source posts, most pointed-at first (94 returned; 2114960347241283996 and 2114507204040548824 came back Authorization Error and 2108062331095908717 Not Found again as referenced posts), then 22 second-hop posts (all returned); 7 third-hop posts were left unread for the budget "+s[j:]
rep("as in 2026-10-26T1204Z through 2026-10-27T0800Z;","as in 2026-10-26T1204Z through 2026-10-27T0905Z;")
rep("Not read: news/money/science sensors,","Not read: culture/sports/online sensors,")
rep("capture/2026/10/27/0905Z.json'","capture/2026/10/27/1004Z.json'")
open('build_capture.py','w').write(s); print('ok')
