s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
OLDLEFT='2110596961166561470, 2110602585572860213, 2110611239915401570, 2110646408227274753, 2110692763758940436, 2110693166059851836, 2110715556328579219, 2110717537964953810, 2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
rep('1905Z.json from saved','2002Z.json from saved')
rep("work/2026-10-27T1905Z'","work/2026-10-27T2002Z'")
rep("RUN_ID = '2026-10-27T1905Z'","RUN_ID = '2026-10-27T2002Z'")
rep("STARTED = '2026-10-27T19:05:00Z'","STARTED = '2026-10-27T20:02:00Z'")
rep("OBS_AT = '2026-10-27T19:06:00Z'","OBS_AT = '2026-10-27T20:03:00Z'")
rep("READS_BEFORE = 607","READS_BEFORE = 588")
rep("datetime(2026,10,27,19,6,tzinfo=timezone.utc).timestamp()  # 1905Z (","datetime(2026,10,27,20,3,tzinfo=timezone.utc).timestamp()  # 2002Z (1905Z used 19:06, ")
rep("""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_drenchgang': 'trend_drenchgang.txt', 'trend_210gb': 'trend_210gb.txt', 'trend_joshdowns': 'trend_joshdowns.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt',""","""    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_mikewaltz': 'trend_mikewaltz.txt', 'trend_bluewave': 'trend_bluewave.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),
    ('trend_drenchgang','trend.#drenchgang'),('trend_210gb','trend.210 GB'),('trend_joshdowns','trend.Josh Downs'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_mikewaltz','trend.Mike Waltz'),('trend_bluewave','trend.#BlueWaveIn7Days'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.#drenchgang','trend.Josh Downs'): return 'sports'""","""        if str(_x) in ('trend.Mike Waltz','trend.#BlueWaveIn7Days'): return 'politics'  # 2002Z: UN Ambassador Mike Waltz's clash with a Cuban official at the UN; #BlueWaveIn7Days is a Democratic get-out-the-vote tag a week before the midterms
        if str(_x) in ('trend.#drenchgang','trend.Josh Downs'): return 'sports'""")
rep("if _c.endswith('1905Z.json') and '/27/' in _c: continue","if _c.endswith('2002Z.json') and '/27/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
WATCHOLD=s[s.index("(this 19Z run is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 20Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last, the list was 689 long, so the 400 cap left out the 82 last six-hour posts, the 14 slowest-growing still-gaining posts, 166 of the 177 fourth-hour posts and 27 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 316 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "Mike Waltz" and "#BlueWaveIn7Days" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached earlier today: "Mike Waltz" (sixth, new) is the UN Ambassador\\\'s clash with a Cuban official at the UN; "#BlueWaveIn7Days" (tenth, new) is a Democratic get-out-the-vote tag a week before the midterms; "Nelson" (first), "Colts" (second), "Buckner" (fourth), "Zabel" (fifth) and "Josh Downs" (eighth) are the Colts trading Quenton Nelson to the Seahawks, attached in 1705Z to 1905Z; "#drenchgang" (third), "Genie 4" (seventh) and "210 GB" (ninth) attached in 1800Z and 1905Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); """+TR+"""; quote/repost words my/it + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 97 unread referenced, reply-parent and media-source posts, most pointed-at first, then 18 second-hop posts; 12 third-hop posts left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)',
    'common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)')
rep("_last = '2026-10-27T1800Z'","_last = '2026-10-27T1905Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and seventy-eighth run","one hundred and seventy-ninth run")
rep("one hundred and eighty-first run","one hundred and eighty-second run")
i=s.index("            f'Afternoon run (3:05 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Afternoon run (4:02 PM ET Oct 27 / 20:02 UTC Oct 27, the 20Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1905Z ended at 588, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours; 689 ids, so the 400 cap left out the 82 last six-hour posts, the 14 slowest-growing still-gaining posts, 166 of the 177 fourth-hour posts and 27 story-cited posts not on the pulse ("""+LEFT+"""; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (2 reads); '
            f'quote/repost words my/it + that (3 reads, each word quoted; 1905Z used is/you + and); sensors news/money/science (3 reads; culture/sports/online read 1905Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-second run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and seventy-ninth run, both for the budget; '
            f'two screening reads by id: 97 unread referenced, reply-parent and media-source posts, most pointed-at first (97 returned; 2114804068011184133 and 2108062331095908717 Not Found in the expansion), then 18 second-hop posts (18 returned; 2115080819479826566, a post referenced by one of those read, came back Authorization Error); 12 third-hop posts left unread for the budget (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1905Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the ninth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/1905Z.json'","capture/2026/10/27/2002Z.json'")
open('build_capture.py','w').write(s)
print('ok')
