import re
s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)
rep('"""Build capture/2026/10/17/1307Z.json','"""Build capture/2026/10/17/1403Z.json')
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1307Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1403Z'")
rep("RUN_ID = '2026-10-17T1307Z'","RUN_ID = '2026-10-17T1403Z'")
rep("STARTED = '2026-10-17T13:07:00Z'","STARTED = '2026-10-17T14:03:00Z'")
rep("OBS_AT = '2026-10-17T13:09:00Z'","OBS_AT = '2026-10-17T14:05:00Z'")
rep("READS_BEFORE = 669","READS_BEFORE = 640")
rep("READS_AFTER = 640","READS_AFTER = 608")
rep("datetime(2026,10,17,13,14,tzinfo=timezone.utc)","datetime(2026,10,17,14,10,tzinfo=timezone.utc)")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_eveche': 'trend_eveche.txt', 'trend_emimartinez': 'trend_emimartinez.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_cortis': 'trend_cortis.txt', 'trend_gameday': 'trend_gameday.txt', 'trend_caturday': 'trend_caturday.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("DUE = ['politics','science','entertainment','music','gaming','ideas','sports','internet','life','offbeat']",
    "DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','medicine','entertainment','sports','internet']")
rep("""    ('quote_just','quote'),('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_eveche','trend.#EVECHE'),('trend_emimartinez','trend.Emi Martinez'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_is','quote'),('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_cortis','trend.#CORTIS_NOLFest2026'),('trend_gameday','trend.GAME DAY'),('trend_caturday','trend.#Caturday'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x)=='trend.Everton': return 'sports'\n",
    "        if str(_x)=='trend.Everton': return 'sports'\n        if str(_x)=='trend.GAME DAY': return 'sports'\n        if str(_x) in ('trend.#Caturday','trend.Caturday'): return 'offbeat'\n")
rep("('watch0','watch1','watch2','watch3')","('watch0','watch1','watch2')",2)
rep("# one event aliases\nfor a,b in [","# one event aliases\nfor a,b in [('#CORTIS_NOLFest2026','IDEA BANK'),('#CORTIS_NOLFest2026','JAMES THE ULTIMATE PHENOMENON'),")
rep("(13Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(14Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
i=s.index("sweeps.append(sweep('viral.global','discovery',None,\n")
j=s.index("24,'ok',None, viral_core))",i)
s=s[:i]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #CORTIS_NOLFest2026, "GAME DAY", #Caturday (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 1307Z; #CORTIS_NOLFest2026 is the CORTIS NOL Festival fan campaign, one event with IDEA BANK (rank 9), so IDEA BANK was not searched; "GAME DAY" is college football Saturday posts, no single event; "Good Saturday" and #SaturdayVibes are weekend-greeting posts, searched in 1108Z, not searched again); quote/repost words is/you/"and" + my; sensors news/money/science; desks politics/world/defense/justice/disaster/markets/business/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',
    """+s[j:]
rep("""    '3 quote pages + 1 repost page, common words "just", "what", "the" and "this": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each',""",
    """    '3 quote pages + 1 repost page, common words "is", "you", "and" and "my": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each',""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("""        _last = '2026-10-17T1202Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 1202Z, next run',[]))""",
"""        _last = '2026-10-17T1307Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 1307Z, next run',[]))""")
i=s.index("        if d in ('defense','disaster','business'):\n")
j=s.index("        sweeps.append(sweep(f'desk.{d}','desk',d, DESK_Q.get(d) or d, 24,'skipped', reason, []))",i)
s=s[:i]+"""        if d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1307Z, due 17:07Z)'
        elif d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1307Z, due 15:07Z)'
        else:
            reason = 'not due this run'
"""+s[j:]
i=s.index("            f'Daytime run at 9:07 AM ET")
j=s.index("            f'{EXTRA_NOTE} '",i)
s=s[:i]+"""            f'Daytime run at 10:03 AM ET (14:03 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1307Z run ended at 640). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 3 reads); trends US+WW; '
            f'trend names #CORTIS_NOLFest2026, "GAME DAY", #Caturday (3 reads; top-ten US names with no posts attached in 1307Z; #CORTIS_NOLFest2026 is one event with IDEA BANK, the CORTIS NOL Festival fan campaign; "GAME DAY" is college football Saturday posts, no single event; "Good Saturday" and #SaturdayVibes are weekend greetings, searched in 1108Z, not searched again); quote/repost words is/you/"and" + my (3+1); '
            f'sensors news/money/science; 13 desk reads: the hourly desks politics, entertainment, sports, internet (56 minutes after the 1307Z sweep, kept hourly as in earlier runs), the two-hour desks world, justice, markets, ai, tech, medicine (due since 14:02Z) and the four-hour desks defense, disaster, business (due since 09:06Z, cut by the desk cap for the last four runs, so the desk cap was raised to 13 this run inside the 42-read run budget); '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/17/1307Z.json'","out_path = f'{REPO}/capture/2026/10/17/1403Z.json'")
open('build_capture.py','w').write(s); print('ok')
