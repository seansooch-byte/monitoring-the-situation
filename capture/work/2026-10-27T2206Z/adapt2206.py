s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('2106Z.json from saved','2206Z.json from saved')
rep("work/2026-10-27T2106Z'","work/2026-10-27T2206Z'")
rep("RUN_ID = '2026-10-27T2106Z'","RUN_ID = '2026-10-27T2206Z'")
rep("STARTED = '2026-10-27T21:06:00Z'","STARTED = '2026-10-27T22:06:00Z'")
rep("OBS_AT = '2026-10-27T21:07:00Z'","OBS_AT = '2026-10-27T22:07:00Z'")
rep("READS_BEFORE = 568","READS_BEFORE = 548")
rep("datetime(2026,10,27,21,7,tzinfo=timezone.utc).timestamp()  # 2106Z (","datetime(2026,10,27,22,7,tzinfo=timezone.utc).timestamp()  # 2206Z (2106Z used 21:07, ")
rep("""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_ryanpoles': 'trend_ryanpoles.txt', 'trend_cuba': 'trend_cuba.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""","""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_cassidy': 'trend_cassidy.txt', 'trend_dowman': 'trend_dowman.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt',""")
rep("""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_ryanpoles','trend.Ryan Poles'),('trend_cuba','trend.Cuba'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_cassidy','trend.Cassidy Hutchinson'),('trend_dowman','trend.Dowman'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.Cuba',): return 'politics'""","""        if str(_x) in ('trend.Cassidy Hutchinson',): return 'politics'  # 2206Z: a DC grand jury declined to indict former White House aide Cassidy Hutchinson over her January 6 testimony
        if str(_x) in ('trend.Dowman',): return 'sports'  # 2206Z: Arsenal's Max Dowman sent off against Fleetwood in the Carabao Cup (Fleetwood and Havertz are the same match)
        if str(_x) in ('trend.Cuba',): return 'politics'""")
rep("if _c.endswith('2106Z.json') and '/27/' in _c: continue","if _c.endswith('2206Z.json') and '/27/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
WATCHOLD=s[s.index("(this 21Z run is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 22Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 531 long, so the 400 cap left out the 87 last six-hour posts, the 13 slowest-growing still-gaining posts and 31 story-cited posts not on the pulse ("+LEFT+"), because the 320 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "Cassidy Hutchinson" and "Dowman" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached earlier today: "Cassidy Hutchinson" (fifth, new) is a DC grand jury declining to indict the former White House aide over her January 6 testimony; "Dowman" (seventh, new), "Havertz" (eighth, new) and "Fleetwood" (ninth, new) are one event, Arsenal\\\'s Max Dowman sent off against Fleetwood in the Carabao Cup ("Havertz" and "Fleetwood" not read, same event); "Poles" (fourth) is the same event as "Ryan Poles", attached in 2106Z; "Colts" (first), "Buckner" (second) and "Josh Downs" (tenth) are the Colts trading Quenton Nelson, attached in 1705Z to 1905Z; "#drenchgang" (third) attached in 1905Z and "Cuba" (sixth) in 2106Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); """+TR+"""; quote/repost words this/is + you (quoted); hourly desks politics/entertainment/sports/internet; one screening read by id: 92 unread referenced, reply-parent and media-source posts, most pointed-at first; no second-hop post left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
    'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)')
rep("_last = '2026-10-27T2002Z'","_last = '2026-10-27T2106Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and eightieth run","one hundred and eighty-first run")
rep("one hundred and eighty-third run","one hundred and eighty-fourth run")
i=s.index("            f'Afternoon run (5:06 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Evening run (6:06 PM ET Oct 27 / 22:06 UTC Oct 27, the 22Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2106Z ended at 548, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 531 ids, so the 400 cap left out the 87 last six-hour posts, the 13 slowest-growing still-gaining posts and 31 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (2 reads); '
            f'quote/repost words this/is + you (3 reads, each word quoted; 2106Z used just/what + the); sensors news/money/science (3 reads; culture/sports/online read 2106Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-first run, both for the budget; '
            f'one screening read by id: 92 unread referenced, reply-parent and media-source posts, most pointed-at first (92 returned; 2108062331095908717 Not Found in the expansion); no second-hop post left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T2106Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the eleventh run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/2106Z.json'","capture/2026/10/27/2206Z.json'")
open('build_capture.py','w').write(s)
print('ok')
