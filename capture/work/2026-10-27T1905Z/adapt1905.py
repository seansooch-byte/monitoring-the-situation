s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
OLDLEFT='2110646408227274753, 2110692763758940436, 2110693166059851836, 2110715556328579219, 2110717537964953810, 2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
rep('1800Z.json from saved','1905Z.json from saved')
rep("work/2026-10-27T1800Z'","work/2026-10-27T1905Z'")
rep("RUN_ID = '2026-10-27T1800Z'","RUN_ID = '2026-10-27T1905Z'")
rep("STARTED = '2026-10-27T18:00:00Z'","STARTED = '2026-10-27T19:05:00Z'")
rep("OBS_AT = '2026-10-27T18:01:00Z'","OBS_AT = '2026-10-27T19:06:00Z'")
rep("READS_BEFORE = 627","READS_BEFORE = 607")
rep("datetime(2026,10,27,18,1,tzinfo=timezone.utc).timestamp()  # 1800Z (","datetime(2026,10,27,19,6,tzinfo=timezone.utc).timestamp()  # 1905Z (1800Z used 18:01, ")
rep("""    'quote_the': 'quote_the.txt', 'quote_what': 'quote_what.txt',
    'repost_this': 'repost_this.txt',
    'trend_colts': 'trend_colts.txt', 'trend_zabel': 'trend_zabel.txt', 'trend_genie4': 'trend_genie4.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""","""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_drenchgang': 'trend_drenchgang.txt', 'trend_210gb': 'trend_210gb.txt', 'trend_joshdowns': 'trend_joshdowns.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt',""")
rep("""    ('quote_the','quote'),('quote_what','quote'),('repost_this','repost'),
    ('trend_colts','trend.Colts'),('trend_zabel','trend.Zabel'),('trend_genie4','trend.Genie 4'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),
    ('trend_drenchgang','trend.#drenchgang'),('trend_210gb','trend.210 GB'),('trend_joshdowns','trend.Josh Downs'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Colts','trend.Zabel'): return 'sports'""","""        if str(_x) in ('trend.#drenchgang','trend.Josh Downs'): return 'sports'  # 1905Z: Indiana Hoosiers football fans' purple "drench out" for Saturday's game against Minnesota; Josh Downs is the Colts receiver named in the Colts fire-sale reports (same event as the Quenton Nelson trade)
        if str(_x) in ('trend.210 GB',): return 'gaming'  # 1905Z: GTA 6's reported 210 GB PS5 download size
        if str(_x) in ('trend.Colts','trend.Zabel'): return 'sports'""")
rep("if _c.endswith('1800Z.json') and '/27/' in _c: continue","if _c.endswith('1905Z.json') and '/27/' in _c: continue")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("this 18Z run is not a","this 19Z run is not a")
rep("the list was 533 long, so the 400 cap left out the 93 last six-hour posts, the 19 slowest-growing still-gaining posts and 21 story-cited posts not on the pulse ("+OLDLEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 310 watch.json",
    "the list was 511 long, so the 400 cap left out the 71 last six-hour posts, the 16 slowest-growing still-gaining posts and 24 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 313 watch.json")
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
TR='trend names "#drenchgang", "210 GB" and "Josh Downs" ("<name> lang:en is:retweet", newest first, 25 each; the top US names with no posts attached earlier today: "#drenchgang" (fifth, new) is Indiana Hoosiers football fans calling a purple \\\'drench out\\\' for Saturday\\\'s game against Minnesota; "210 GB" (eighth, new) is GTA 6\\\'s reported PS5 download size; "Josh Downs" (tenth, new) is the Colts receiver named as a trade candidate, the same event as "Nelson" (first), "Colts" (second), "Buckner" (third) and "Zabel" (fourth), attached in 1705Z and 1800Z: the Colts trading Quenton Nelson to the Seahawks; "Jonathan Taylor" (seventh; same event) not searched for the budget; "Genie 4" (sixth) attached in 1800Z and "Eric Swalwell" (ninth) is the FBI search already attached in 1503Z)'
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); """+TR+"""; quote/repost words is/you + and (quoted); hourly desks politics/entertainment/sports/internet; one screening read by id: 94 unread referenced, reply-parent and media-source posts, most pointed-at first; no second-hop post was left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "the", "what" and "this", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
    'common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)')
rep("_last = '2026-10-27T1705Z'","_last = '2026-10-27T1800Z'")
rep("rotation: news/money/science read this run","rotation: culture/sports/online read this run")
rep("one hundred and seventy-seventh run","one hundred and seventy-eighth run")
rep("one hundred and eightieth run","one hundred and eighty-first run")
i=s.index("            f'Afternoon run (2:00 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Afternoon run (3:05 PM ET Oct 27 / 19:05 UTC Oct 27, the 19Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1800Z ended at 607, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 511 ids, so the 400 cap left out the 71 last six-hour posts, the 16 slowest-growing still-gaining posts and 24 story-cited posts not on the pulse ("""+LEFT+"""; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (3 reads); '
            f'quote/repost words is/you + and (3 reads, each word quoted; 1800Z used the/what + this); sensors culture/sports/online (3 reads; news/money/science read 1800Z, so culture/sports/online were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-first run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and seventy-eighth run, both for the budget; '
            f'one screening read by id: 94 unread referenced, reply-parent and media-source posts, most pointed-at first (94 returned; 2112935455473701201, a post referenced by one of those read, came back Authorization Error and 2108062331095908717 Not Found again in the expansion); no second-hop post was left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1800Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the eighth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/1800Z.json'","capture/2026/10/27/1905Z.json'")
open('build_capture.py','w').write(s)
print('ok')
