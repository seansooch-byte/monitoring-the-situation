s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('capture/2026/10/28/0101Z.json from saved','capture/2026/10/28/0159Z.json from saved')
rep("work/2026-10-28T0101Z'","work/2026-10-28T0159Z'")
rep("RUN_ID = '2026-10-28T0101Z'","RUN_ID = '2026-10-28T0159Z'")
rep("STARTED = '2026-10-28T01:01:00Z'","STARTED = '2026-10-28T01:59:00Z'")
rep("OBS_AT = '2026-10-28T01:02:00Z'","OBS_AT = '2026-10-28T02:00:00Z'")
rep("READS_BEFORE = 980","READS_BEFORE = 959")
rep("datetime(2026,10,28,1,2,tzinfo=timezone.utc).timestamp()  # 0101Z (","datetime(2026,10,28,2,0,tzinfo=timezone.utc).timestamp()  # 0159Z (0101Z used 01:02, ")
rep("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_dwts': 'trend_dwts.txt', 'trend_paulreed': 'trend_paulreed.txt', 'trend_tatyana': 'trend_tatyana.txt', 'trend_shirley': 'trend_shirley.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""","""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_davidhamilton': 'trend_davidhamilton.txt', 'trend_connor': 'trend_connor.txt', 'trend_amber': 'trend_amber.txt', 'trend_maura': 'trend_maura.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""")
rep("""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_dwts','trend.#dwts'),('trend_paulreed','trend.Paul Reed'),('trend_tatyana','trend.Tatyana'),('trend_shirley','trend.Shirley'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_davidhamilton','trend.David Hamilton'),('trend_connor','trend.Connor'),('trend_amber','trend.Amber'),('trend_maura','trend.Maura'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.#dwts','trend.Tatyana','trend.Shirley'): return 'entertainment'""","""        if str(_x) in ('trend.Connor','trend.Amber','trend.Maura'): return 'entertainment'  # 0159Z: Dancing with the Stars scores (Connor Wood's two 10s against Amber Glenn's and Maura Higgins's 9s), one event with #dwts, Tatyana and Shirley in 0101Z
        if str(_x) in ('trend.David Hamilton',): return 'sports'  # 0159Z: Brewers' David Hamilton's game-tying home run in World Series Game 4
        if str(_x) in ('trend.#dwts','trend.Tatyana','trend.Shirley'): return 'entertainment'""")
rep("if _c.endswith('0101Z.json') and '/28/' in _c: continue","if _c.endswith('0159Z.json') and '/28/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
WATCHOLD=s[s.index("(this 01Z run is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 0159Z run, the 02Z slot, is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 535 long, so the 400 cap left out the 90 last six-hour posts, the 7 slowest-growing still-gaining posts and 38 story-cited posts not on the pulse ("+LEFT+"), because the 327 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "David Hamilton", "Connor", "Amber" and "Maura" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached in the previous run: "Connor" (fifth), "Amber" (seventh), "Jenna" (eighth) and "Maura" (eleventh, read in place of Jenna) are Dancing with the Stars contestants, one event with "#dwts", "Tatyana" and "Shirley" (first to fourth, attached in 0101Z), Jenna not read for the budget; "David Hamilton" (sixth) is the Brewers infielder whose game-tying home run came in World Series Game 4; "Paul Reed" (ninth) attached in 0101Z and "#WWENXT" (tenth) in 0011Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); """+TR+"""; quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; three screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned), then 6 second-hop posts (6 returned), then 19 third-hop posts (19 returned); story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
    'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)')
rep("_last = '2026-10-28T0011Z'","_last = '2026-10-28T0101Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and eighty-fourth run","one hundred and eighty-fifth run")
rep("one hundred and eighty-seventh run","one hundred and eighty-eighth run")
i=s.index("            f'Evening run (9:01 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Evening run (9:59 PM ET Oct 27 / 01:59 UTC Oct 28, the 02Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0101Z ended at 959, so no reads went elsewhere in between), parallel batches of up to 14, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 535 ids, so the 400 cap left out the 90 last six-hour posts, the 7 slowest-growing still-gaining posts and 38 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (4 reads); '
            f'quote/repost words you/and + my (3 reads, each word quoted; 0101Z used the/this + is); sensors news/money/science (3 reads; culture/sports/online read 0101Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-eighth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-fifth run, both for the budget; '
            f'three screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned; two referenced posts in its includes came back Not Found: 2081838749109862897, 2114804068011184133), then 6 second-hop posts (6 returned; 2108062331095908717 Not Found again in its includes), then 19 third-hop posts (19 returned); 11 further-hop posts left unread for the budget; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-28T0101Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the fifteenth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/28/0101Z.json'","capture/2026/10/28/0159Z.json'")
open('build_capture.py','w').write(s)
print('ok')
