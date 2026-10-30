s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('capture/2026/10/28/0159Z.json from saved','capture/2026/10/28/0305Z.json from saved')
rep("work/2026-10-28T0159Z'","work/2026-10-28T0305Z'")
rep("RUN_ID = '2026-10-28T0159Z'","RUN_ID = '2026-10-28T0305Z'")
rep("STARTED = '2026-10-28T01:59:00Z'","STARTED = '2026-10-28T03:05:00Z'")
rep("OBS_AT = '2026-10-28T02:00:00Z'","OBS_AT = '2026-10-28T03:06:00Z'")
rep("READS_BEFORE = 959","READS_BEFORE = 936")
rep("datetime(2026,10,28,2,0,tzinfo=timezone.utc).timestamp()  # 0159Z (","datetime(2026,10,28,3,6,tzinfo=timezone.utc).timestamp()  # 0305Z (0159Z used 02:00, ")
rep("""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_davidhamilton': 'trend_davidhamilton.txt', 'trend_connor': 'trend_connor.txt', 'trend_amber': 'trend_amber.txt', 'trend_maura': 'trend_maura.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""","""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_jaysontatum': 'trend_jaysontatum.txt', 'trend_pistons': 'trend_pistons.txt', 'trend_mikelbrown': 'trend_mikelbrown.txt', 'trend_visionquest': 'trend_visionquest.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_davidhamilton','trend.David Hamilton'),('trend_connor','trend.Connor'),('trend_amber','trend.Amber'),('trend_maura','trend.Maura'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_jaysontatum','trend.Jayson Tatum'),('trend_pistons','trend.Pistons'),('trend_mikelbrown','trend.Mikel Brown'),('trend_visionquest','trend.#VisionQuest'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Connor','trend.Amber','trend.Maura'): return 'entertainment'""","""        if str(_x) in ('trend.Jayson Tatum','trend.Mikel Brown','trend.Pistons'): return 'sports'  # 0305Z: Jayson Tatum's overtime game-winner for the Celtics against the Nets (Mikel Brown Jr. the Nets rookie, Nets the same event); Pistons lost to the Knicks (one event with Paul Reed in 0101Z and Josh Hart)
        if str(_x) in ('trend.#VisionQuest',): return 'entertainment'  # 0305Z: the Marvel series VisionQuest, new episode
        if str(_x) in ('trend.Connor','trend.Amber','trend.Maura'): return 'entertainment'""")
rep("if _c.endswith('0159Z.json') and '/28/' in _c: continue","if _c.endswith('0305Z.json') and '/28/' in _c: continue")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
WATCHOLD=s[s.index("(this 0159Z run, the 02Z slot, is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 0305Z run, the 03Z slot, is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 532 long, so the 400 cap left out the 88 last six-hour posts, the 6 slowest-growing still-gaining posts and 38 story-cited posts not on the pulse ("+LEFT+"), because the 327 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "Jayson Tatum", "Pistons", "Mikel Brown" and "#VisionQuest" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached in the previous run: "Jayson Tatum" (fourth) and "Mikel Brown" (ninth) are one event, Tatum’s overtime game-winner for the Celtics against the Nets and the Nets rookie Mikel Brown Jr.’s late shots and missed layups, and "Nets" (seventh) is the same event, not read for the budget; "Pistons" (sixth) is the Knicks’ win over the Pistons, one event with "Paul Reed" (attached in 0101Z) and "Josh Hart" (fifteenth); "#VisionQuest" (tenth) is the Marvel series’ new episode; "#dwts", "Tatyana" and "Shirley" (first to third) were attached in 0101Z and "Connor" (fifth) and "David Hamilton" (eighth) in 0159Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); """+TR+"""; quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned), then the other 23 (23 returned); no further-hop post left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
    'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)')
rep("_last = '2026-10-28T0101Z'","_last = '2026-10-28T0159Z'")
rep("rotation: news/money/science read this run","rotation: culture/sports/online read this run")
rep("one hundred and eighty-fifth run","one hundred and eighty-sixth run")
rep("one hundred and eighty-eighth run","one hundred and eighty-ninth run")
i=s.index("            f'Evening run (9:59 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Night run (11:05 PM ET Oct 27 / 03:05 UTC Oct 28, the 03Z slot; 12:00-05:00 UTC band, up to 42; kept to about 21 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0159Z ended at 937, so one read went elsewhere in between), parallel batches of up to 14, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 532 ids, so the 400 cap left out the 88 last six-hour posts, the 6 slowest-growing still-gaining posts and 38 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR.replace("'","\\'")+""" (4 reads); '
            f'quote/repost words it/that + just (3 reads, each word quoted; 0159Z used you/and + my); sensors culture/sports/online (3 reads; news/money/science read 0159Z, so culture/sports/online were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-sixth run, both for the budget; '
            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned), then the other 23 (23 returned; 2108062331095908717 Not Found again in its includes); no further-hop post left unread; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-28T0159Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the sixteenth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/28/0159Z.json'","capture/2026/10/28/0305Z.json'")
open('build_capture.py','w').write(s)
print('ok')
