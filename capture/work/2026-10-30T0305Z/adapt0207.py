s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/30/0109Z.json from saved','"""Build capture/2026/10/30/0207Z.json from saved')
R("capture/work/2026-10-30T0109Z'","capture/work/2026-10-30T0207Z'")
R("RUN_ID = '2026-10-30T0109Z'","RUN_ID = '2026-10-30T0207Z'")
R("STARTED = '2026-10-30T01:09:00Z'","STARTED = '2026-10-30T02:08:00Z'")
R("OBS_AT = '2026-10-30T01:10:00Z'","OBS_AT = '2026-10-30T02:08:00Z'")
R("READS_BEFORE = 1000","READS_BEFORE = 960")
SPAN("READS_USED = 40","\n","READS_USED = 27  # 0207Z: this run's 27 X calls (watch 4, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2); the counter fell 960 to 933; no 429 or 503 refusals\n")
R("datetime(2026,10,30,1,10,tzinfo=timezone.utc).timestamp()  # 0109Z (","datetime(2026,10,30,2,8,tzinfo=timezone.utc).timestamp()  # 0207Z (0109Z used 01:10, ")
R("""    'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_treysmack': 'trend_treysmack.txt', 'trend_redbaron': 'trend_redbaron.txt', 'trend_911onabc': 'trend_911onabc.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""","""    'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_packers': 'trend_packers.txt', 'trend_matthewgolden': 'trend_matthewgolden.txt', 'trend_christianwatson': 'trend_christianwatson.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
SPAN("DUE = ['politics','world'","\n","DUE = ['politics','entertainment','sports','internet']  # 0207Z: the four hourly desks the plan for 2026-10-30T02Z lists\n")
R("""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_treysmack','trend.Trey Smack'),('trend_redbaron','trend.Red Baron'),('trend_911onabc','trend.#911onABC'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_this','quote'),('repost_is','repost'),
    ('trend_packers','trend.Packers'),('trend_matthewgolden','trend.Matthew Golden'),('trend_christianwatson','trend.Christian Watson'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) in ('trend.Trey Smack','trend.Panthers',""","""        if str(_x) in ('trend.Matthew Golden','trend.Jordan Love','trend.Bryce','trend.Bryce Young'): return 'sports'  # 0207Z: Panthers at Packers, Thursday Night Football
        if str(_x) in ('trend.Trey Smack','trend.Panthers',""")
R("if _c.endswith('0109Z.json') and '/30/' in _c: continue","if _c.endswith('0207Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T2203Z'  # 0109Z: news/money/science last read in 2203Z","_last = '2026-10-30T0109Z'  # 0207Z: culture/sports/online last read in 0109Z")
R("not in the plan for 2026-10-30T01Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T02Z (rotation: news/money/science this run)")
R("reason = 'not due in the plan for 2026-10-30T01Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-30T02Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
R("CTX_REPLIES = CTXR  # 0109Z: replies to MarvelStudios 2115896865803870592","CTX_REPLIES = CTXR  # 0207Z: replies to redbaronpizza 2115917093182792143")
R("CTX_IDS = ['2115896865803870592'] + CTX_REPLIES","CTX_IDS = ['2115917093182792143'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of the plan for 2026-10-30T01Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T02Z, in its order and in batches of 100 (344 ids; its left_out counts 10 slowed flat posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, then screened by id (2 screen reads: 99 unread references, then 25 second-hop); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Packers\", \"Matthew Golden\" and \"Christian Watson\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first three top-ten US names with no posts attached in 0109Z; all three, with \"Bryce\" and \"Jordan Love\", are one event: Panthers at Packers on Thursday Night Football, where Christian Watson was taken to hospital with a chest injury; skipping \"Panthers\", \"Patrick Stewart\", \"Binance\", \"Red Baron\" and \"Trey Smack\" (attached in 0109Z))',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"this\" and \"is\" (0109Z used \"what\" and \"the\"), each quoted so X does not reject a bare stopword: (\"this\" lang:en is:quote -is:retweet), (\"is\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T03:00:00Z, end_time 2026-10-30T02:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine); each series is the 167 full hours 2026-10-23T03:00Z to 2026-10-30T01:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T21:22:00Z (the post\\'s creation minute) and end_time 2026-10-29T21:42:00Z: (conversation_id:2115917093182792143 is:reply) and (quotes_of_tweet_id:2115917093182792143 -is:retweet); the plan gives context.top two reads, so one post: 2115917093182792143 (@redbaronpizza on the Red Baron worker, \"He\\'s still here. He\\'s got a fan club.\", the biggest post new this run at about 3.14M views); 25 replies and 25 quotes in the window, the 3 most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (8:09 PM CT","f'Screen: cut by the plan; unread second-hop references left unread. '\n",
 "            f'Day-band run (9:08 PM CT Oct 29 / 02:08 UTC Oct 30, the 02Z slot; band allowance 42): requests/plan.json is for 2026-10-30T02Z (written 01:18Z after the 0109Z capture), so it was followed (28 reads listed, nothing cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 344 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable (2115634869154005285 authorization error, 2115228889907855391 not found; neither on the pulse, in a story or on watch.json); nothing added or dropped; the 10 slowed flat posts in its left_out were not read. '\n"
 "            f'Desks: politics, entertainment, sports, internet (the four the plan lists). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Packers\", \"Matthew Golden\" and \"Christian Watson\" (3 reads; one event, Panthers at Packers on Thursday Night Football). rising.global: quote stream \"this\" and repost stream \"is\" (2 reads). context.top: redbaronpizza 2115917093182792143 (2 reads). '\n"
 "            f'Screen: 2 reads by id (99 unread references, then 25 second-hop). '\n")
R("'plan': '2026-10-30T01Z',","'plan': '2026-10-30T02Z',")
R("    'context': [{'post_id': '2115896865803870592',","    'context': [{'post_id': '2115917093182792143',")
R("capture/2026/10/30/0109Z.json'","capture/2026/10/30/0207Z.json'")
anchor="DESK_OVERRIDE_RUN.update({_x:'entertainment' for _x in ['2115896865803870592']+CTXR+CTXQ})"
i=s.index(anchor); j=s.index("\n",i)+1
s=s[:j]+"DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2115917093182792143']+CTXR+CTXQ})  # 0207Z: redbaronpizza post on the Red Baron worker and its context replies and quotes are internet\n"+s[j:]
open('build_capture.py','w').write(s); print('ok')
