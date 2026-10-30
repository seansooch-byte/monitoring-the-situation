s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('2002Z.json from saved','2106Z.json from saved')
rep("work/2026-10-27T2002Z'","work/2026-10-27T2106Z'")
rep("RUN_ID = '2026-10-27T2002Z'","RUN_ID = '2026-10-27T2106Z'")
rep("STARTED = '2026-10-27T20:02:00Z'","STARTED = '2026-10-27T21:06:00Z'")
rep("OBS_AT = '2026-10-27T20:03:00Z'","OBS_AT = '2026-10-27T21:07:00Z'")
rep("READS_BEFORE = 588","READS_BEFORE = 568")
rep("datetime(2026,10,27,20,3,tzinfo=timezone.utc).timestamp()  # 2002Z (","datetime(2026,10,27,21,7,tzinfo=timezone.utc).timestamp()  # 2106Z (2002Z used 20:03, ")
rep("""    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_mikewaltz': 'trend_mikewaltz.txt', 'trend_bluewave': 'trend_bluewave.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""","""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_ryanpoles': 'trend_ryanpoles.txt', 'trend_cuba': 'trend_cuba.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_mikewaltz','trend.Mike Waltz'),('trend_bluewave','trend.#BlueWaveIn7Days'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_ryanpoles','trend.Ryan Poles'),('trend_cuba','trend.Cuba'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Mike Waltz','trend.#BlueWaveIn7Days'): return 'politics'""","""        if str(_x) in ('trend.Cuba',): return 'politics'  # 2106Z: same event as Mike Waltz, the US-Cuba clash at the UN (Rubio's "private island" post)
        if str(_x) in ('trend.Ryan Poles',): return 'sports'  # 2106Z: Bears fans at GM Ryan Poles after DeForest Buckner went to the 49ers (same trade-deadline event as the Colts trading Quenton Nelson)
        if str(_x) in ('trend.Mike Waltz','trend.#BlueWaveIn7Days'): return 'politics'""")
rep("if _c.endswith('2002Z.json') and '/27/' in _c: continue","if _c.endswith('2106Z.json') and '/27/' in _c: continue")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
WATCHOLD=s[s.index("(this 20Z run is a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 21Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 519 long, so the 400 cap left out the 75 last six-hour posts, the 15 slowest-growing still-gaining posts and 29 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 318 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "Ryan Poles" and "Cuba" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached earlier today: "Ryan Poles" (fifth, new) is Bears fans calling on GM Ryan Poles after DeForest Buckner was traded to the 49ers, the same trade-deadline event as the Colts trading Quenton Nelson; "Cuba" (sixth, new) is the same event as "Mike Waltz", the US-Cuba clash at the UN and Marco Rubio\\\'s "private island" post; "Colts" (first), "Buckner" (second), "Nelson" (third), "Josh Downs" (seventh), "Jonathan Taylor" (ninth) and "Zabel" (tenth) are the Colts trading Quenton Nelson, attached in 1705Z to 1905Z ("Jonathan Taylor" not read, same event); "#drenchgang" (fourth) attached in 1905Z and "Mike Waltz" (eighth) in 2002Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); """+TR+"""; quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 7 more; no second-hop post left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
    'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)')
rep("_last = '2026-10-27T1905Z'","_last = '2026-10-27T2002Z'")
rep("rotation: news/money/science read this run","rotation: culture/sports/online read this run")
rep("one hundred and seventy-ninth run","one hundred and eightieth run")
rep("one hundred and eighty-second run","one hundred and eighty-third run")
i=s.index("            f'Afternoon run (4:02 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Afternoon run (5:06 PM ET Oct 27 / 21:06 UTC Oct 27, the 21Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2002Z ended at 569, so 1 read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 519 ids, so the 400 cap left out the 75 last six-hour posts, the 15 slowest-growing still-gaining posts and 29 story-cited posts not on the pulse ("""+LEFT+"""; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (2 reads); '
            f'quote/repost words just/what + the (3 reads, each word quoted; 2002Z used my/it + that); sensors culture/sports/online (3 reads; news/money/science read 2002Z, so culture/sports/online were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eightieth run, both for the budget; '
            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (99 returned; 2113737233853264245 Not Found, and 2114804068011184133 Not Found in the expansion), then the 7 remaining (7 returned; 2108062331095908717 Not Found in the expansion); no second-hop post left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T2002Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the tenth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/2002Z.json'","capture/2026/10/27/2106Z.json'")
open('build_capture.py','w').write(s)
print('ok')
