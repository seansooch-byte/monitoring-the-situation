s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('2300Z.json from saved','0011Z.json from saved')
rep("work/2026-10-27T2300Z'","work/2026-10-28T0011Z'")
rep("RUN_ID = '2026-10-27T2300Z'","RUN_ID = '2026-10-28T0011Z'")
rep("STARTED = '2026-10-27T23:00:00Z'","STARTED = '2026-10-28T00:11:00Z'")
rep("OBS_AT = '2026-10-27T23:01:00Z'","OBS_AT = '2026-10-28T00:12:00Z'")
rep("READS_BEFORE = 530","READS_BEFORE = 1000")
rep("datetime(2026,10,27,23,1,tzinfo=timezone.utc).timestamp()  # 2300Z (","datetime(2026,10,28,0,12,tzinfo=timezone.utc).timestamp()  # 0011Z (2300Z used 23:01, ")
rep("""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_arsenal': 'trend_arsenal.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt',""","""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_julianne': 'trend_julianne.txt', 'trend_coachjackie': 'trend_coachjackie.txt', 'trend_wwenxt': 'trend_wwenxt.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_arsenal','trend.Arsenal'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_julianne','trend.Julianne'),('trend_coachjackie','trend.COACH JACKIE'),('trend_wwenxt','trend.#WWENXT'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.Arsenal',): return 'sports'""","""        if str(_x) in ('trend.Julianne','trend.COACH JACKIE'): return 'entertainment'  # 0011Z: Dancing with the Stars (judge Julianne Hough; Coach Jackie with Derek Hough), one event
        if str(_x) in ('trend.#WWENXT',): return 'sports'  # 0011Z: WWE NXT on The CW, the last NXT before Halloween Havoc
        if str(_x) in ('trend.Arsenal',): return 'sports'""")
rep("if _c.endswith('2300Z.json') and '/27/' in _c: continue","if _c.endswith('0011Z.json') and '/28/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
WATCHOLD=s[s.index("(this 23Z run is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 00Z run is a fourth hour, so posts first captured 6 to 24 hours ago that gained less than 2 percent were due too; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and fourth-hour tiers, the list was 671 long, so the 400 cap left out the 73 last six-hour posts, the 13 slowest-growing still-gaining posts, 147 of 158 fourth-hour posts and 38 story-cited posts not on the pulse ("+LEFT+"), because the 327 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "Julianne", "COACH JACKIE" and "#WWENXT" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached in the previous run: "Julianne" (sixth, new) and "COACH JACKIE" (tenth, new) are one event, Dancing with the Stars (Julianne Hough judging; Coach Jackie in the ballroom with Derek Hough); "#WWENXT" (seventh, new) is WWE NXT on The CW; "Arsenal" (first) attached in 2300Z, "Fleetwood" (fourth) and "Havertz" (eighth) are the same match, attached in 2206Z and 2300Z; "Cassidy Hutchinson" (second) attached in 2206Z, "Colts" (third) and "Buckner" (fifth) are the Colts trading Quenton Nelson, attached in 1705Z to 1905Z; "Cuba" (ninth) attached in 2106Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); """+TR+"""; quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 90 unread referenced, reply-parent and media-source posts, most pointed-at first, then 16 second-hop posts; 8 third-hop posts left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
    'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)')
rep("_last = '2026-10-27T2206Z'","_last = '2026-10-27T2300Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and eighty-second run","one hundred and eighty-third run")
rep("one hundred and eighty-fifth run","one hundred and eighty-sixth run")
i=s.index("            f'Evening run (7:00 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Evening run (8:11 PM ET Oct 27 / 00:11 UTC Oct 28, the 00Z slot, first run of the UTC day; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today after the 00:00 UTC reset; 2300Z ended at 512 on 2026-10-27), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 671 ids, so the 400 cap left out the 73 last six-hour posts, the 13 slowest-growing still-gaining posts, 147 of 158 fourth-hour posts and 38 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (3 reads); '
            f'quote/repost words that/just + what (3 reads, each word quoted; 2300Z used and/my + it); sensors news/money/science (3 reads; culture/sports/online read 2300Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-sixth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-third run, both for the budget; '
            f'two screening reads by id: 90 unread referenced, reply-parent and media-source posts, most pointed-at first (89 returned; 2108062331095908717 Not Found), then 16 second-hop posts (16 returned); 8 third-hop posts left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T2300Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the thirteenth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/2300Z.json'","capture/2026/10/28/0011Z.json'")
open('build_capture.py','w').write(s)
print('ok')
