s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)
def repline(start,new):
    global s
    i=s.index(start); j=s.index("\n",i); s=s[:i]+new+s[j:]
rep('"""Build capture/2026/10/17/1706Z.json','"""Build capture/2026/10/17/1807Z.json')
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1706Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1807Z'")
rep("RUN_ID = '2026-10-17T1706Z'","RUN_ID = '2026-10-17T1807Z'")
rep("STARTED = '2026-10-17T17:06:00Z'","STARTED = '2026-10-17T18:07:00Z'")
rep("OBS_AT = '2026-10-17T17:07:00Z'","OBS_AT = '2026-10-17T18:08:00Z'")
rep("READS_BEFORE = 551","READS_BEFORE = 520")
rep("READS_AFTER = 520","READS_AFTER = 486")
rep("datetime(2026,10,17,17,10,tzinfo=timezone.utc)","datetime(2026,10,17,18,11,tzinfo=timezone.utc)")
rep("""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_sayin': 'trend_sayin.txt', 'trend_hoover': 'trend_hoover.txt', 'trend_lamine': 'trend_lamine.txt', 'trend_niblett': 'trend_niblett.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_ryanday': 'trend_ryanday.txt', 'trend_arthursmith': 'trend_arthursmith.txt', 'trend_betis': 'trend_betis.txt', 'trend_gators': 'trend_gators.txt', 'trend_nokings': 'trend_nokings.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("DUE = ['politics','science','entertainment','music','gaming','ideas','sports','internet','life','offbeat']",
    "DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','medicine','entertainment','sports','internet']")
rep("""    ('quote_and','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_sayin','trend.Julian Sayin'),('trend_hoover','trend.Hoover'),('trend_lamine','trend.Lamine'),('trend_niblett','trend.Ryan Niblett'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_just','quote'),('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_ryanday','trend.Ryan Day'),('trend_arthursmith','trend.Arthur Smith'),('trend_betis','trend.Betis'),('trend_gators','trend.Gators'),('trend_nokings','trend.No Kings'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x)=='trend.No Kings': return 'politics'\n",
    "        if str(_x)=='trend.No Kings': return 'politics'\n        if str(_x) in ('trend.Ryan Day','trend.Arthur Smith','trend.Betis','trend.Gators','trend.Indiana'): return 'sports'\n")
rep("for a,b in [('Isak','Munoz'),","for a,b in [('Ryan Day','Ohio State'),('Ryan Day','Indiana'),('Arthur Smith','Ohio State'),('Betis','Lamine'),")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("(17Z is not a fourth hour, so no slow tier)","(18Z is not a fourth hour, so no slow tier)")
TN = 'trend names "Ryan Day", "Arthur Smith", Betis, Gators, "No Kings" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; five of the six top-ten US names with no posts attached in 1706Z; Ryan Day, Arthur Smith and Indiana belong to the Ohio State v Indiana college football game, already covered through Julian Sayin, Hoover and Ohio State, so Indiana was not searched (cap of five); Betis is Real Betis v Barcelona, one event with Lamine; Gators is the Texas v Florida game, one event with Ryan Niblett in 1706Z; No Kings is the planned protest day)'
repline("    'sources: references followed two hops", "    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; "+TN.replace("'","\\'")+"; quote/repost words just/what/the + this; sensors news/money/science; desks politics/world/defense/justice/disaster/markets/business/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',")
repline("    '3 quote pages + 1 repost page, common words", """    '3 quote pages + 1 repost page, common words "just", "what", "the" and "this": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each',""")
rep("""        _last = '2026-10-17T1600Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 1600Z, next run',[]))""",
"""        _last = '2026-10-17T1706Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 1706Z, next run',[]))""")
rep("""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1600Z, due 18:00Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1403Z, due 18:03Z)'""",
"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1706Z, due 19:06Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1706Z, due 21:06Z)'""")
i=s.index("            f'Daytime run at 1:06 PM ET"); j=s.index("            f'{EXTRA_NOTE} '",i)
s=s[:i]+"""            f'Daytime run at 2:07 PM ET (18:07 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1706Z run ended at 520, so nothing else read in between). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 3 reads); trends US+WW; '
            f'"""+TN.replace("'","\\'").replace('{','{{').replace('}','}}')+""" (5 reads); quote/repost words just/what/the + this (3+1); '
            f'sensors news/money/science; 13 desk reads: the hourly desks politics, entertainment, sports, internet, the two-hour desks world, justice, markets, ai, tech, medicine (last ok 1600Z, due 18:00Z) and the four-hour desks defense, disaster, business (last ok 1403Z, due 18:03Z); '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/17/1706Z.json'","out_path = f'{REPO}/capture/2026/10/17/1807Z.json'")
open('build_capture.py','w').write(s); print('ok')
