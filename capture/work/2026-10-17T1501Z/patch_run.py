s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)
rep('"""Build capture/2026/10/17/1403Z.json','"""Build capture/2026/10/17/1501Z.json')
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1403Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1501Z'")
rep("RUN_ID = '2026-10-17T1403Z'","RUN_ID = '2026-10-17T1501Z'")
rep("STARTED = '2026-10-17T14:03:00Z'","STARTED = '2026-10-17T15:01:00Z'")
rep("OBS_AT = '2026-10-17T14:05:00Z'","OBS_AT = '2026-10-17T15:02:00Z'")
rep("READS_BEFORE = 640","READS_BEFORE = 608")
rep("READS_AFTER = 608","READS_AFTER = 581")
rep("datetime(2026,10,17,14,10,tzinfo=timezone.utc)","datetime(2026,10,17,15,8,tzinfo=timezone.utc)")
rep("""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_cortis': 'trend_cortis.txt', 'trend_gameday': 'trend_gameday.txt', 'trend_caturday': 'trend_caturday.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_mrfanboy': 'trend_mrfanboy.txt', 'trend_nokings': 'trend_nokings.txt', 'trend_brentford': 'trend_brentford.txt', 'trend_everton': 'trend_everton.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','medicine','entertainment','sports','internet']",
    "DUE = ['politics','entertainment','music','gaming','sports','internet','offbeat']")
rep("""    ('quote_is','quote'),('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_cortis','trend.#CORTIS_NOLFest2026'),('trend_gameday','trend.GAME DAY'),('trend_caturday','trend.#Caturday'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_mrfanboy','trend.#MrFanboyEP8'),('trend_nokings','trend.No Kings'),('trend_brentford','trend.Brentford'),('trend_everton','trend.Everton'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x)=='trend.Everton': return 'sports'\n",
    "        if str(_x)=='trend.Everton': return 'sports'\n        if str(_x) in ('trend.Brentford','trend.Gameday'): return 'sports'\n        if str(_x)=='trend.No Kings': return 'politics'\n        if str(_x) in ('trend.#MrFanboyEP8','trend.MR FANBOY CHAPTER 8'): return 'entertainment'\n")
rep("# one event aliases\nfor a,b in [","# one event aliases\nfor a,b in [('#MrFanboyEP8','MR FANBOY CHAPTER 8'),('Everton','Pedro Neto'),('Everton','#EVECHE'),")
rep("(14Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "(15Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
i=s.index("sweeps.append(sweep('viral.global','discovery',None,\n")
j=s.index("24,'ok',None, viral_core))",i)
s=s[:i]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #MrFanboyEP8, "No Kings", Brentford, Everton (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 1403Z; #MrFanboyEP8 and "MR FANBOY CHAPTER 8" are one event, episode 8 of the Thai series Mr Fanboy, so the second was not searched; "No Kings" is the No Kings protests today; Brentford is the Brentford v Liverpool match; Everton and Pedro Neto are one event, the Everton v Chelsea match (#EVECHE in 1307Z), so Pedro Neto was not searched; Gameday is one event with "GAME DAY", college football Saturday, which had posts attached in 1403Z; "Good Saturday" and #SaturdayVibes are weekend greetings, searched in 1108Z, not searched again; #Caturday had posts attached in 1403Z); quote/repost words it/that/just + what; sensors culture/sports/online; desks politics/entertainment/music/gaming/sports/internet/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',
    """+s[j:]
rep("""    '3 quote pages + 1 repost page, common words "is", "you", "and" and "my": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each',""",
    """    '3 quote pages + 1 repost page, common words "it", "that", "just" and "what": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("""        _last = '2026-10-17T1307Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 1307Z, next run',[]))""",
"""        _last = '2026-10-17T1403Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 1403Z, next run',[]))""")
i=s.index("        if d in ('science','ideas','life'):\n")
j=s.index("        sweeps.append(sweep(f'desk.{d}','desk',d, DESK_Q.get(d) or d, 24,'skipped', reason, []))",i)
s=s[:i]+"""        if d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1307Z, due 17:07Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1403Z, due 18:03Z)'
        elif d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1403Z, due 16:03Z)'
        else:
            reason = 'not due this run'
"""+s[j:]
i=s.index("            f'Daytime run at 10:03 AM ET")
j=s.index("            f'{EXTRA_NOTE} '",i)
s=s[:i]+"""            f'Daytime run at 11:01 AM ET (15:01 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1403Z run ended at 608). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 3 reads); trends US+WW; '
            f'trend names #MrFanboyEP8, "No Kings", Brentford, Everton (4 reads; top-ten US names with no posts attached in 1403Z; #MrFanboyEP8 and "MR FANBOY CHAPTER 8" are one event, episode 8 of the Thai series Mr Fanboy; "No Kings" is the No Kings protests today; Brentford is the Brentford v Liverpool match; Everton and Pedro Neto are one event, the Everton v Chelsea match; Gameday is one event with "GAME DAY", which had posts attached in 1403Z; "Good Saturday" and #SaturdayVibes are weekend greetings, searched in 1108Z, not searched again); quote/repost words it/that/just + what (3+1); '
            f'sensors culture/sports/online; 7 desk reads: the hourly desks politics, entertainment, sports, internet and the two-hour desks music, gaming, offbeat (last ok 1307Z, swept about 4 minutes before 15:07Z to keep the cadence); '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/17/1403Z.json'","out_path = f'{REPO}/capture/2026/10/17/1501Z.json'")
open('build_capture.py','w').write(s); print('ok')
