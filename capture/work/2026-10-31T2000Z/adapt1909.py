s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    assert s.count(start)>=1,start
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/31/1802Z.json from saved','"""Build capture/2026/10/31/1909Z.json from saved')
R("capture/work/2026-10-31T1802Z'","capture/work/2026-10-31T1909Z'")
R("RUN_ID = '2026-10-31T1802Z'","RUN_ID = '2026-10-31T1909Z'")
L("STARTED = ","STARTED = '2026-10-31T19:09:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T19:10:00Z'")
R("READS_BEFORE = 462","READS_BEFORE = 424")
L("READS_USED = 38","READS_USED = 29  # 1909Z: this run's 29 X calls (watch 5, trends 2, desks 4, volume 5, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 424 to 395; no 429 or 503 refusals")
R("datetime(2026,10,31,18,3,tzinfo=timezone.utc).timestamp()  # 1802Z (","datetime(2026,10,31,19,10,tzinfo=timezone.utc).timestamp()  # 1909Z (1802Z used 18:03, ")
R("  # 1802Z: five watch reads\n","  # 1909Z: five watch reads\n")
R("  # 1802Z: three screen reads; no request asked\n    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',\n",
  "  # 1909Z: three screen reads; no request asked\n    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',\n")
R("    'trend_rutgers': 'trend_rutgers.txt', 'trend_iowa': 'trend_iowa.txt', 'trend_wisconsin': 'trend_wisconsin.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_arizona': 'trend_arizona.txt', 'trend_persona1': 'trend_persona1.txt', 'trend_furtherado': 'trend_furtherado.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1909Z: the 4 desks the plan for 2026-10-31T19Z lists")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_rutgers','trend.Rutgers'),('trend_iowa','trend.Iowa'),('trend_wisconsin','trend.Wisconsin'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_arizona','trend.Arizona'),('trend_persona1','trend.Persona 1'),('trend_furtherado','trend.Further Ado'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.Persona 1': return 'gaming'  # 1909Z: Persona 1 remake footage leak\n        if str(_x)=='trend.Further Ado': return 'sports'  # 1909Z: Further Ado wins the Breeders' Cup Dirt Mile (Arizona mixes the Arizona election and Arizona college football, so no default)\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1909Z: replies to zackdfilms1 2116289709307469938 in its first 20 minutes (0 returned)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1909Z: quotes in the window (0 returned)")
L("CTX_IDS = [","CTX_IDS = ['2116289709307469938'] + CTX_REPLIES + CTX_QUOTES  # 1909Z: the context post itself; 0 replies and 0 quotes returned in the window")
R("DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116421111433032050']+CTXR+CTXQ})  # 1802Z: hiitotsu Music Core stage post (and any context replies and quotes) is music",
  "DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116421111433032050']})  # 1802Z: hiitotsu Music Core stage post is music")
R("if _c.endswith('1802Z.json') and '/31/' in _c: continue","if _c.endswith('1909Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T1700Z'  # 1802Z: culture/sports/online last read in 1700Z","_last = '2026-10-31T1802Z'  # 1909Z: news/money/science last read in 1802Z")
R("not in requests/plan.json for 2026-10-31T18Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T19Z (rotation: culture/sports/online this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T18Z (day band, allowance 42)","cut by requests/plan.json for 2026-10-31T19Z (day band, allowance 42)")
s=s.replace("not due in requests/plan.json for 2026-10-31T18Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T19Z (desks_not_due)")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T18Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T19Z, in its order and in batches of 100 (409 ids; its left_out slowed flat posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 103 unread first-hop references in two reads, 102 returned and 1 not found (2060339087798661321, as in 1802Z), then 19 second-hop references, all returned); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Arizona\", \"Persona 1\" and \"Further Ado\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1802Z; Halloween and Navy are repeat events, Iowa, Rutgers and Wisconsin were read in 1802Z, Fickell is the Wisconsin game and Notre Dame the Navy game); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"just\" and \"what\" (1802Z used \"it\" and \"that\"), each quoted so X does not reject a bare stopword: (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T20:00:00Z, end_time 2026-10-31T19:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T20:00Z to 2026-10-31T18:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T22:02:00Z (the post\\'s creation minute) and end_time 2026-10-30T22:22:00Z: (conversation_id:2116289709307469938 is:reply) and (quotes_of_tweet_id:2116289709307469938 -is:retweet); the plan gives context.top two reads, so one post: 2116289709307469938 (zackdfilms1 animated explainer on why Dobermans have cropped ears, 8.49M views, the biggest new post under 24 h); both searches returned 0 posts in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
a=s.index("            f'Day-band run (1:02 PM CDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Day-band run (2:09 PM CDT Oct 31 / 19:09 UTC Oct 31, the 19Z slot; band allowance 42): requests/plan.json is for 2026-10-31T19Z (written 18:11Z after the 1802Z run) and was followed top to bottom (29 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1802Z and this run, the counter was 424 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 409 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the slowed flat posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Arizona" (Arizona election posts mixed with Arizona college football), "Persona 1" (gaming: Persona 1 remake footage leak) and "Further Ado" (sports: Breeders\\' Cup Dirt Mile winner) (3 reads). rising.global: quote stream "just" and repost stream "what" (2 reads). context.top: zackdfilms1 2116289709307469938 (2 reads; 0 replies and 0 quotes in the 20-minute window). '
            f'Screen: 3 reads by id (103 unread first-hop references in two reads, 1 not found; then 19 second-hop, all returned). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T18Z',","'plan': '2026-10-31T19Z',")
R("    'context': [{'post_id': '2116421111433032050',","    'context': [{'post_id': '2116289709307469938',")
R("f'{REPO}/capture/2026/10/31/1802Z.json'","f'{REPO}/capture/2026/10/31/1909Z.json'")
open('build_capture.py','w').write(s); print('ok')
