s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('2206Z.json from saved','2300Z.json from saved')
rep("work/2026-10-27T2206Z'","work/2026-10-27T2300Z'")
rep("RUN_ID = '2026-10-27T2206Z'","RUN_ID = '2026-10-27T2300Z'")
rep("STARTED = '2026-10-27T22:06:00Z'","STARTED = '2026-10-27T23:00:00Z'")
rep("OBS_AT = '2026-10-27T22:07:00Z'","OBS_AT = '2026-10-27T23:01:00Z'")
rep("READS_BEFORE = 548","READS_BEFORE = 530")
rep("datetime(2026,10,27,22,7,tzinfo=timezone.utc).timestamp()  # 2206Z (","datetime(2026,10,27,23,1,tzinfo=timezone.utc).timestamp()  # 2300Z (2206Z used 22:07, ")
rep("""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_cassidy': 'trend_cassidy.txt', 'trend_dowman': 'trend_dowman.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""","""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_arsenal': 'trend_arsenal.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_cassidy','trend.Cassidy Hutchinson'),('trend_dowman','trend.Dowman'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_arsenal','trend.Arsenal'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Cassidy Hutchinson',): return 'politics'""","""        if str(_x) in ('trend.Arsenal',): return 'sports'  # 2300Z: Arsenal's Carabao Cup match against Fleetwood (same event as Dowman, Havertz, Fleetwood and Arteta)
        if str(_x) in ('trend.Cassidy Hutchinson',): return 'politics'""")
rep("if _c.endswith('2206Z.json') and '/27/' in _c: continue","if _c.endswith('2300Z.json') and '/27/' in _c: continue")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
WATCHOLD=s[s.index("(this 22Z run is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 546 long, so the 400 cap left out the 99 last six-hour posts, the 12 slowest-growing still-gaining posts and 35 story-cited posts not on the pulse ("+LEFT+"), because the 324 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend name "Arsenal" ("<name> lang:en is:retweet", newest first, 25; the top-ten US names with no posts attached earlier today: "Arsenal" (first, new), "Havertz" (sixth) and "Arteta" (eighth, new) are the same event as "Dowman" and "Fleetwood", Arsenal\\\'s Carabao Cup match against Fleetwood, attached in 2206Z ("Havertz" and "Arteta" not read, same event); "Colts" (second) and "Buckner" (third) are the Colts trading Quenton Nelson, attached in 1705Z to 1905Z; "Cassidy Hutchinson" (fifth) attached in 2206Z, "#drenchgang" (seventh) in 1905Z and "Cuba" (tenth) in 2106Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); """+TR+"""; quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; one screening read by id: 91 unread referenced, reply-parent and media-source posts, most pointed-at first; no second-hop post left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
    'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)')
rep("_last = '2026-10-27T2106Z'","_last = '2026-10-27T2206Z'")
rep("rotation: news/money/science read this run","rotation: culture/sports/online read this run")
rep("one hundred and eighty-first run","one hundred and eighty-second run")
rep("one hundred and eighty-fourth run","one hundred and eighty-fifth run")
i=s.index("            f'Evening run (6:06 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Evening run (7:00 PM ET Oct 27 / 23:00 UTC Oct 27, the 23Z slot, last run of the UTC day; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2206Z ended at 530, so no reads went elsewhere in between), parallel batches of up to 11, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 546 ids, so the 400 cap left out the 99 last six-hour posts, the 12 slowest-growing still-gaining posts and 35 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (1 read); '
            f'quote/repost words and/my + it (3 reads, each word quoted; 2206Z used this/is + you); sensors culture/sports/online (3 reads; news/money/science read 2206Z, so culture/sports/online were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-fifth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-second run, both for the budget; '
            f'one screening read by id: 91 unread referenced, reply-parent and media-source posts, most pointed-at first (91 returned; 2108062331095908717 Not Found in the expansion); no second-hop post left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T2206Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the twelfth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/2206Z.json'","capture/2026/10/27/2300Z.json'")
open('build_capture.py','w').write(s)
print('ok')
