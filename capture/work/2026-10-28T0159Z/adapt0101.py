s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('capture/2026/10/27/0011Z.json from saved','capture/2026/10/28/0101Z.json from saved')
rep("work/2026-10-28T0011Z'","work/2026-10-28T0101Z'")
rep("RUN_ID = '2026-10-28T0011Z'","RUN_ID = '2026-10-28T0101Z'")
rep("STARTED = '2026-10-28T00:11:00Z'","STARTED = '2026-10-28T01:01:00Z'")
rep("OBS_AT = '2026-10-28T00:12:00Z'","OBS_AT = '2026-10-28T01:02:00Z'")
rep("READS_BEFORE = 1000","READS_BEFORE = 980")
rep("datetime(2026,10,28,0,12,tzinfo=timezone.utc).timestamp()  # 0011Z (","datetime(2026,10,28,1,2,tzinfo=timezone.utc).timestamp()  # 0101Z (0011Z used 00:12, ")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_julianne': 'trend_julianne.txt', 'trend_coachjackie': 'trend_coachjackie.txt', 'trend_wwenxt': 'trend_wwenxt.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""","""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_dwts': 'trend_dwts.txt', 'trend_paulreed': 'trend_paulreed.txt', 'trend_tatyana': 'trend_tatyana.txt', 'trend_shirley': 'trend_shirley.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_julianne','trend.Julianne'),('trend_coachjackie','trend.COACH JACKIE'),('trend_wwenxt','trend.#WWENXT'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_dwts','trend.#dwts'),('trend_paulreed','trend.Paul Reed'),('trend_tatyana','trend.Tatyana'),('trend_shirley','trend.Shirley'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Julianne','trend.COACH JACKIE'): return 'entertainment'""","""        if str(_x) in ('trend.#dwts','trend.Tatyana','trend.Shirley'): return 'entertainment'  # 0101Z: Dancing with the Stars (Shirley Ballas guest judging; Tatyana in the ballroom), one event, as Julianne and COACH JACKIE in 0011Z
        if str(_x) in ('trend.Paul Reed',): return 'sports'  # 0101Z: Pistons big man Paul Reed, 13 points in the first quarter against the Knicks
        if str(_x) in ('trend.Julianne','trend.COACH JACKIE'): return 'entertainment'""")
rep("if _c.endswith('0011Z.json') and '/28/' in _c: continue","if _c.endswith('0101Z.json') and '/28/' in _c: continue")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
WATCHOLD=s[s.index("(this 00Z run is a fourth hour,"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 537 long, so the 400 cap left out the 89 last six-hour posts, the 10 slowest-growing still-gaining posts and 38 story-cited posts not on the pulse ("+LEFT+"), because the 327 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "#dwts", "Tatyana", "Shirley" and "Paul Reed" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached in the previous run: "#dwts" (first), "Tatyana" (second) and "Shirley" (third) are one event, Dancing with the Stars (Shirley Ballas guest judging, Tatyana in the ballroom), and "Connor" (fourth), "Jenna" (fifth) and "Julia" (seventh) are names from the same show, not read separately for the budget; "Paul Reed" (sixth) is the Pistons big man against the Knicks; "#WWENXT" (eighth) attached in 0011Z, "Arsenal" (ninth) in 2300Z, "Cassidy Hutchinson" (tenth) in 2206Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); """+TR+"""; quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned), then 1 second-hop post (returned); story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
    'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)')
rep("_last = '2026-10-27T2300Z'","_last = '2026-10-28T0011Z'")
rep("rotation: news/money/science read this run","rotation: culture/sports/online read this run")
rep("one hundred and eighty-third run","one hundred and eighty-fourth run")
rep("one hundred and eighty-sixth run","one hundred and eighty-seventh run")
i=s.index("            f'Evening run (8:11 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Evening run (9:01 PM ET Oct 27 / 01:01 UTC Oct 28, the 01Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0011Z ended at 980, so no reads went elsewhere in between), parallel batches of up to 7, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 537 ids, so the 400 cap left out the 89 last six-hour posts, the 10 slowest-growing still-gaining posts and 38 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR+""" (4 reads); '
            f'quote/repost words the/this + is (3 reads, each word quoted; 0011Z used that/just + what); sensors culture/sports/online (3 reads; news/money/science read 0011Z, so culture/sports/online were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and eighty-seventh run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-fourth run, both for the budget; '
            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned; two referenced posts in its includes came back as errors: 2114555306361463211 Authorization Error, 2108062331095908717 Not Found), then 1 second-hop post (returned); no third-hop post left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-28T0011Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the fourteenth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/28/0011Z.json'","capture/2026/10/28/0101Z.json'")
open('build_capture.py','w').write(s)
print('ok')
s=open('build_capture.py').read()
rep("PRIOR_DESK = {}\n","DESK_OVERRIDE_RUN.update({'2114886660223611334':'politics','2115077994561847635':'entertainment','2115214810992251368':'sports','1878853557111414795':'politics','2115065692751872212':'politics','2114809445213475189':'gaming','2115141843931533807':'gaming','1791139584270815511':'music','1791135489988411890':'music','1624540409060896771':'music','1888699812574540128':'music','2114954785371652333':'sports','2114996886704955609':'entertainment'})  # 0101Z desk fixes: DeepLeaksHQ Bernie Sanders claim (came in on the Shirley trend via Nick Shirley) is politics; Jennifer Lawrence shoot is entertainment; Dunk Central season post is sports; Mamdani and El-Sayed are politics; Kotaku AI piece and John Romero DOOM post are gaming; Little Mix, BRITs and Rebecca Black clips are music; Jokic post is sports; Sukuna anime post is entertainment\nPRIOR_DESK = {}\n")
open('build_capture.py','w').write(s)
print('ok2')
