import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT='2110692763758940436, 2110693166059851836, 2110715556328579219, 2110717537964953810, 2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
OLDLEFT='2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
rep('1604Z.json from saved','1705Z.json from saved')
rep("work/2026-10-27T1604Z'","work/2026-10-27T1705Z'")
rep("RUN_ID = '2026-10-27T1604Z'","RUN_ID = '2026-10-27T1705Z'")
rep("STARTED = '2026-10-27T16:04:00Z'","STARTED = '2026-10-27T17:05:00Z'")
rep("OBS_AT = '2026-10-27T16:06:00Z'","OBS_AT = '2026-10-27T17:06:00Z'")
rep("READS_BEFORE = 668","READS_BEFORE = 647")
rep("datetime(2026,10,27,16,6,tzinfo=timezone.utc).timestamp()  # 1604Z (","datetime(2026,10,27,17,6,tzinfo=timezone.utc).timestamp()  # 1705Z (1604Z used 16:06, ")
rep("""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_stephencloobeck': 'trend_stephencloobeck.txt', 'trend_kateallie': 'trend_kateallie.txt', 'trend_mcmillan': 'trend_mcmillan.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt',""","""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_nelson': 'trend_nelson.txt', 'trend_bigq': 'trend_bigq.txt', 'trend_buckner': 'trend_buckner.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_stephencloobeck','trend.Stephen Cloobeck'),('trend_kateallie','trend.Kate & Allie'),('trend_mcmillan','trend.McMillan'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_nelson','trend.Nelson'),('trend_bigq','trend.Big Q'),('trend_buckner','trend.Buckner'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Stephen Cloobeck',): return 'justice'""","""        if str(_x) in ('trend.Nelson','trend.Big Q','trend.Buckner'): return 'sports'  # 1705Z: Colts trade Quenton Nelson ("Big Q") to the Seahawks and shop DeForest Buckner (one event)
        if str(_x) in ('trend.Stephen Cloobeck',): return 'justice'""")
rep("if _c.endswith('1604Z.json') and '/27/' in _c: continue","if _c.endswith('1705Z.json') and '/27/' in _c: continue")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("this 16Z run is not a","this 17Z run is not a")
rep("the list was 516 long, so the 400 cap left out the 79 last six-hour posts, the 21 slowest-growing still-gaining posts and 16 story-cited posts not on the pulse ("+OLDLEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 305 watch.json",
    "the list was 515 long, so the 400 cap left out the 75 last six-hour posts, the 20 slowest-growing still-gaining posts and 20 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 309 watch.json")
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
TR='trend names "Nelson", "Big Q" and "Buckner" ("<name> lang:en is:retweet", newest first, 25 each; the top US names with no posts attached earlier today: "Nelson" (first, new), "Big Q" (third, new) and "Buckner" (fourth, new) are one event, the Colts trading guard Quenton Nelson ("Big Q") to the Seahawks and shopping DeForest Buckner; "Swalwell" (second) and "Beverly Hills" (fifth) are the FBI search already attached in 1503Z; "Genie 4" (sixth, new), "John Schneider" (seventh, new; likely the Seahawks general manager, same trade), "Zabel" (eighth, new) and "John Lynch" (ninth, new) not searched for the budget; "Noah Wyle" (tenth) had posts attached earlier today)'
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); """+TR+"""; quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 29 second-hop posts; one third-hop post left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
    'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)')
rep("_last = '2026-10-27T1503Z'","_last = '2026-10-27T1604Z'")
rep("rotation: news/money/science read this run","rotation: culture/sports/online read this run")
rep("one hundred and seventy-fifth run","one hundred and seventy-sixth run")
rep("one hundred and seventy-eighth run","one hundred and seventy-ninth run")
i=s.index("            f'Morning run (12:04 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Afternoon run (1:05 PM ET Oct 27 / 17:05 UTC Oct 27, the 17Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1604Z ended at 649, so 2 reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 515 ids, so the 400 cap left out the 75 last six-hour posts, the 20 slowest-growing still-gaining posts and 20 story-cited posts not on the pulse ("""+LEFT+"""; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR.replace("'","\\\\'")+""" (3 reads); '
            f'quote/repost words it/that + just (3 reads, each word quoted; 1604Z used you/and + my); sensors culture/sports/online (3 reads; news/money/science read 1604Z, so culture/sports/online were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and seventy-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and seventy-sixth run, both for the budget; '
            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned; 2108062331095908717, a post referenced by one of those read, came back Not Found again in the expansion), then 29 second-hop posts (29 returned; 2067280591565766836 and 2112579146836844895, referenced by posts in that read, came back Not Found in the expansion); one third-hop post left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1604Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the sixth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/1604Z.json'","capture/2026/10/27/1705Z.json'")
open('build_capture.py','w').write(s)
print('ok')
