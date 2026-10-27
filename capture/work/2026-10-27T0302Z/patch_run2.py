import re
s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, ('MISSING', a[:90]); s=s.replace(a,b)
TN_SHORT='trend names "Jay-Z", "Giannis", "Eagles", "Rays" and "#WorldSeries"'
EV=('"Jay-Z" (sixth) is Jay-Z named Super Bowl LXI halftime headliner; "Giannis" (ninth) is Giannis Antetokounmpo\'s first Miami triple-double (29 points, 14 rebounds, 11 assists) as the Heat fall to 0-4 against the Mavericks; '
    '"Eagles" (third) is one event with "Cowboys" (Cowboys 31, Eagles 21 late on Monday Night Football); "Rays" (fifth) and "#WorldSeries" (tenth) are one event with "Brewers" (first; the Brewers far ahead of the Rays late in World Series Game 3); '
    '"Brewers" and "#WWERaw" (fourth) had posts attached in 0204Z, and "Cowboys" (second), "Tanner McKee" (seventh) and "Saquon" (eighth) had been searched in earlier runs; two off-topic "Rays" results (a "Rays of sun" photo and a 2025 scripture post) were not attached to the trend')
# watch.json description
rep("(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 549 long, so the 400 cap left out the 95 last six-hour posts and the 54 slowest-growing still-gaining posts, and no cited post)",
    "(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 546 long, so the 400 cap left out the 92 last six-hour posts, the 51 slowest-growing still-gaining posts and 3 story-cited posts not on the pulse (2113656547834487022, 2114085789139140865, 2114425377338634392), because the 292 watch.json ids plus 113 cited ids came to 405)")
i=s.index("'sources: references followed one hop"); j=s.index("story clusters not read for the budget; screened by id with global floor/pace'",i)
s=s[:i]+("'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "
  +TN_SHORT+' ("<name> lang:en is:retweet", newest first, 25 each; '+EV.replace("'","\\'")+'); quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 93 then 18 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 7 third-hop posts left unread for the budget; ')+s[j:]
rep('''common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)''',
    '''common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)''')
rep("_last = '2026-10-27T0105Z'","_last = '2026-10-27T0204Z'")
rep("(rotation: news/money/science read this run;","(rotation: culture/sports/online read this run;")
rep("Evening run (10:04 PM ET Oct 26 / 02:04 UTC Oct 27, the 02Z slot;","Night run (11:02 PM ET Oct 26 / 03:02 UTC Oct 27, the 03Z slot;")
rep("0105Z ended at 956,","0204Z ended at 934,")
rep("02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 549 ids, so the 400 cap left out the 95 last six-hour posts and the 54 slowest-growing still-gaining posts, and no cited post; 4 reads)",
    "03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 546 ids, so the 400 cap left out the 92 last six-hour posts, the 51 slowest-growing still-gaining posts and 3 story-cited posts not on the pulse (2113656547834487022, 2114085789139140865, 2114425377338634392; 292 watch.json ids plus 113 cited ids came to 405); 4 reads)")
i=s.index("            f'trend names \"The Brewers\""); j=s.index("\n",i)
s=s[:i]+"            f'"+(TN_SHORT+' (5 reads; "<name> lang:en is:retweet", newest first, 25; '+EV+'); ').replace("'","\\'")+"'"+s[j:]
rep("quote/repost words this/is + you (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0105Z, so news/money/science were next in rotation); ",
    "quote/repost words and/my + it (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science read 0204Z, so culture/sports/online were next in rotation); ")
rep("one hundred and sixty-fourth run","one hundred and sixty-fifth run")
rep("one hundred and sixty-first run","one hundred and sixty-second run")
rep("two screening reads by id: 95 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned but 2059067645266100350, Authorization Error), then 16 second-hop posts (all returned but 2108062331095908717, Not Found again); 8 third-hop posts",
    "two screening reads by id: 93 unread referenced, reply-parent and media-source posts, most pointed-at first (all returned; 2113778211687641178 and 2108062331095908717 came back Not Found as referenced posts), then 18 second-hop posts (all returned but 2113778211687641178 and 2108062331095908717, Not Found); 7 third-hop posts")
rep("as in 2026-10-26T1204Z through 2026-10-27T0105Z;","as in 2026-10-26T1204Z through 2026-10-27T0204Z;")
rep("Not read: culture/sports/online sensors,","Not read: news/money/science sensors,")
rep("capture/2026/10/27/0204Z.json'","capture/2026/10/27/0302Z.json'")
open('build_capture.py','w').write(s); print('ok')
