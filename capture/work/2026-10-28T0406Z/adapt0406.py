s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
LEFT=open('left_story.txt').read().strip()
rep('capture/2026/10/28/0305Z.json from saved','capture/2026/10/28/0406Z.json from saved')
rep("work/2026-10-28T0305Z'","work/2026-10-28T0406Z'")
rep("RUN_ID = '2026-10-28T0305Z'","RUN_ID = '2026-10-28T0406Z'")
rep("STARTED = '2026-10-28T03:05:00Z'","STARTED = '2026-10-28T04:06:00Z'")
rep("OBS_AT = '2026-10-28T03:06:00Z'","OBS_AT = '2026-10-28T04:07:00Z'")
rep("READS_BEFORE = 936","READS_BEFORE = 915")
rep("datetime(2026,10,28,3,6,tzinfo=timezone.utc).timestamp()  # 0305Z (","datetime(2026,10,28,4,7,tzinfo=timezone.utc).timestamp()  # 0406Z (0305Z used 03:06, ")
rep("""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_jaysontatum': 'trend_jaysontatum.txt', 'trend_pistons': 'trend_pistons.txt', 'trend_mikelbrown': 'trend_mikelbrown.txt', 'trend_visionquest': 'trend_visionquest.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""","""    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_cooperpratt': 'trend_cooperpratt.txt', 'trend_worldseries': 'trend_worldseries.txt', 'trend_ianseymour': 'trend_ianseymour.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt',""")
rep("""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_jaysontatum','trend.Jayson Tatum'),('trend_pistons','trend.Pistons'),('trend_mikelbrown','trend.Mikel Brown'),('trend_visionquest','trend.#VisionQuest'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_cooperpratt','trend.Cooper Pratt'),('trend_worldseries','trend.#WorldSeries'),('trend_ianseymour','trend.Ian Seymour'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.Jayson Tatum','trend.Mikel Brown','trend.Pistons'): return 'sports'""","""        if str(_x) in ('trend.Cooper Pratt','trend.#WorldSeries','trend.Ian Seymour'): return 'sports'  # 0406Z: Brewers rookie Cooper Pratt's extra-inning home run off the Rays' Ian Seymour in World Series Game 4, one event (Brewers and Ashby the same game; David Hamilton in 0159Z the same game)
        if str(_x) in ('trend.Jayson Tatum','trend.Mikel Brown','trend.Pistons'): return 'sports'""")
rep("if _c.endswith('0305Z.json') and '/28/' in _c: continue","if _c.endswith('0406Z.json') and '/28/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
WATCHOLD=s[s.index("(this 0305Z run, the 03Z slot, is not a fourth hour;"):s.index("); {len(watch_ids)} ids read")]
WATCHNEW="(this 0406Z run, the 04Z slot, is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 531 long, so the 400 cap left out the 81 last six-hour posts, the 7 slowest-growing still-gaining posts and 43 story-cited posts not on the pulse ("+LEFT+"), because the 332 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out"
rep(WATCHOLD,WATCHNEW)
TR='trend names "Cooper Pratt", "#WorldSeries" and "Ian Seymour" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached in the previous run: "Cooper Pratt" (first), "#WorldSeries" (third), "Ian Seymour" (eighth) and "Brewers" (ninth) are one event, Brewers rookie Cooper Pratt’s extra-inning home run off the Rays’ Ian Seymour in World Series Game 4 (one game with "David Hamilton", attached in 0159Z), so "Brewers" was not read for the budget; "Nets" (tenth) is the Celtics-Nets game attached in 0305Z through "Jayson Tatum" and "Mikel Brown"; "#dwts" and "Tatyana" (second, fourth and fifth) were attached in 0101Z)'
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); """+TR+"""; quote/repost words what/the + this (quoted); hourly desks politics/entertainment/sports/internet; one screening read by id: 82 unread referenced, reply-parent and media-source posts, most pointed-at first (82 returned); no further-hop post left unread; story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
    'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)')
rep("_last = '2026-10-28T0159Z'","_last = '2026-10-28T0305Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and eighty-sixth run","one hundred and eighty-seventh run")
rep("one hundred and eighty-ninth run","one hundred and ninetieth run")
i=s.index("            f'Night run (11:05 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Night run (12:06 AM ET Oct 28 / 04:06 UTC Oct 28, the 04Z slot; 12:00-05:00 UTC band, up to 42; kept to about 19 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0305Z ended at 915), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 531 ids, so the 400 cap left out the 81 last six-hour posts, the 7 slowest-growing still-gaining posts and 43 story-cited posts not on the pulse ("""+LEFT+"""); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'"""+TR.replace("'","\\'")+""" (3 reads); '
            f'quote/repost words what/the + this (3 reads, each word quoted; 0305Z used it/that + just); sensors news/money/science (3 reads; culture/sports/online read 0305Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and ninetieth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and eighty-seventh run, both for the budget; '
            f'one screening read by id: 82 unread referenced, reply-parent and media-source posts, most pointed-at first (82 returned; 2108062331095908717 Not Found again in its includes); no further-hop post left unread; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-28T0305Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; not cited on the pulse) came back Not Found for the seventeenth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/28/0305Z.json'","capture/2026/10/28/0406Z.json'")
open('build_capture.py','w').write(s)
print('ok')
