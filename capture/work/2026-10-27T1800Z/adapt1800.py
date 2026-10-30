s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT='2110646408227274753, 2110692763758940436, 2110693166059851836, 2110715556328579219, 2110717537964953810, 2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
OLDLEFT='2110692763758940436, 2110693166059851836, 2110715556328579219, 2110717537964953810, 2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
rep('1705Z.json from saved','1800Z.json from saved')
rep("work/2026-10-27T1705Z'","work/2026-10-27T1800Z'")
rep("RUN_ID = '2026-10-27T1705Z'","RUN_ID = '2026-10-27T1800Z'")
rep("STARTED = '2026-10-27T17:05:00Z'","STARTED = '2026-10-27T18:00:00Z'")
rep("OBS_AT = '2026-10-27T17:06:00Z'","OBS_AT = '2026-10-27T18:01:00Z'")
rep("READS_BEFORE = 647","READS_BEFORE = 627")
rep("datetime(2026,10,27,17,6,tzinfo=timezone.utc).timestamp()  # 1705Z (","datetime(2026,10,27,18,1,tzinfo=timezone.utc).timestamp()  # 1800Z (1705Z used 17:06, ")
rep("""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_nelson': 'trend_nelson.txt', 'trend_bigq': 'trend_bigq.txt', 'trend_buckner': 'trend_buckner.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""","""    'quote_the': 'quote_the.txt', 'quote_what': 'quote_what.txt',
    'repost_this': 'repost_this.txt',
    'trend_colts': 'trend_colts.txt', 'trend_zabel': 'trend_zabel.txt', 'trend_genie4': 'trend_genie4.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_nelson','trend.Nelson'),('trend_bigq','trend.Big Q'),('trend_buckner','trend.Buckner'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_the','quote'),('quote_what','quote'),('repost_this','repost'),
    ('trend_colts','trend.Colts'),('trend_zabel','trend.Zabel'),('trend_genie4','trend.Genie 4'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.Nelson','trend.Big Q','trend.Buckner'): return 'sports'""","""        if str(_x) in ('trend.Colts','trend.Zabel'): return 'sports'  # 1800Z: same event as 1705Z, the Colts trading Quenton Nelson to the Seahawks (Grey Zabel is the Seahawks guard moving to right guard)
        if str(_x) in ('trend.Genie 4',): return 'ai'  # 1800Z: Google DeepMind releases the Genie 4 world model
        if str(_x) in ('trend.Nelson','trend.Big Q','trend.Buckner'): return 'sports'""")
rep("if _c.endswith('1705Z.json') and '/27/' in _c: continue","if _c.endswith('1800Z.json') and '/27/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("this 17Z run is not a","this 18Z run is not a")
rep("the list was 515 long, so the 400 cap left out the 75 last six-hour posts, the 20 slowest-growing still-gaining posts and 20 story-cited posts not on the pulse ("+OLDLEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 309 watch.json",
    "the list was 533 long, so the 400 cap left out the 93 last six-hour posts, the 19 slowest-growing still-gaining posts and 21 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 310 watch.json")
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
TR='trend names "Colts", "Zabel" and "Genie 4" ("<name> lang:en is:retweet", newest first, 25 each; the top US names with no posts attached earlier today: "Colts" (second, new) and "Zabel" (fourth, new; Seahawks guard Grey Zabel) are the same event as "Nelson" (first), "Buckner" (third) and "Big Q" (eighth), attached in 1705Z: the Colts trading guard Quenton Nelson to the Seahawks; "Genie 4" (fifth, new) is Google DeepMind\\\'s new world model; "Jonathan Taylor" (sixth, new; Colts ownership does not want to trade him, same event), "John Schneider" (ninth) and "Seahawks" (tenth) not searched for the budget; "Swalwell" (seventh) is the FBI search already attached in 1503Z)'
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); """+TR+"""; quote/repost words the/what + this (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 25 second-hop posts; one third-hop post (2108062331095908717, Not Found again) left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
    'common words "the", "what" and "this", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)')
rep("_last = '2026-10-27T1604Z'","_last = '2026-10-27T1705Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and seventy-sixth run","one hundred and seventy-seventh run")
rep("one hundred and seventy-ninth run","one hundred and eightieth run")
i=s.index("            f'Afternoon run (1:05 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Afternoon run (2:00 PM ET Oct 27 / 18:00 UTC Oct 27, the 18Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1705Z ended at 627, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 533 ids, so the 400 cap left out the 93 last six-hour posts, the 19 slowest-growing still-gaining posts and 21 story-cited posts not on the pulse ("""+LEFT+"""; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR.replace("\\\\'","\\\\'")+""" (3 reads); '
            f'quote/repost words the/what + this (3 reads, each word quoted; 1705Z used it/that + just); sensors news/money/science (3 reads; culture/sports/online read 1705Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eightieth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and seventy-seventh run, both for the budget; '
            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned; 2108062331095908717, a post referenced by one of those read, came back Not Found again in the expansion), then 25 second-hop posts (25 returned; 2115012770873897449, referenced by a post in that read, came back Not Found in the expansion); one third-hop post (2108062331095908717) left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1705Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the seventh run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/1705Z.json'","capture/2026/10/27/1800Z.json'")
open('build_capture.py','w').write(s)
print('ok')
