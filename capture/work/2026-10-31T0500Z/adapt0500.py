s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/31/0400Z.json from saved','"""Build capture/2026/10/31/0500Z.json from saved')
R("capture/work/2026-10-31T0400Z'","capture/work/2026-10-31T0500Z'")
R("RUN_ID = '2026-10-31T0400Z'","RUN_ID = '2026-10-31T0500Z'")
L("STARTED = ","STARTED = '2026-10-31T05:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T05:01:00Z'")
R("READS_BEFORE = 865","READS_BEFORE = 823")
L("READS_USED = 42","READS_USED = 28  # 0500Z: this run's 28 X calls (watch 4, trends 2, desks 4, volume 5, sensors 3, viral.global 3, rising.global 2, screen 3, context.top 2); the counter fell 823 to 795; no 429 or 503 refusals")
R("datetime(2026,10,31,4,1,tzinfo=timezone.utc).timestamp()  # 0400Z (","datetime(2026,10,31,5,1,tzinfo=timezone.utc).timestamp()  # 0500Z (0400Z used 04:01, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 0400Z: seven watch reads; screen cut by the plan; no request asked\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',  # 0500Z: four watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 0500Z: three screen reads; no request asked\n")
R("    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',","    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',")
R("    'trend_luka': 'trend_luka.txt', 'trend_curry': 'trend_curry.txt', 'trend_reaves': 'trend_reaves.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_podz': 'trend_podz.txt', 'trend_grimes': 'trend_grimes.txt', 'trend_lakers': 'trend_lakers.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 0500Z: the 4 desks the plan for 2026-10-31T05Z lists")
R("""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_luka','trend.Luka'),('trend_curry','trend.Curry'),('trend_reaves','trend.Reaves'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_podz','trend.Podz'),('trend_grimes','trend.Grimes'),('trend_lakers','trend.Lakers'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x) in ('trend.Luka','trend.Curry','trend.Reaves'): return 'sports'  # 0400Z:",
  "        if str(_x) in ('trend.Podz','trend.Lakers'): return 'sports'  # 0500Z: Brandin Podziemski (Warriors) and the Lakers in Lakers v Warriors, one event with Luka/Steph\n        if str(_x) in ('trend.Luka','trend.Curry','trend.Reaves'): return 'sports'  # 0400Z:")
L("REQ_PICKS = {}","REQ_PICKS = {}  # 0500Z: no request asked (none open and unanswered)")
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 0500Z: replies to AstonVilla 2116293295278285299 in its first 20 minutes (24 returned, the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['2116293295278285299'] + CTX_REPLIES + CTX_QUOTES  # 0500Z: the context post itself; 24 replies and 25 quotes returned")
R("DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116222771000963266']+CTXR+CTXQ})  # 0400Z: the context post and its context replies and quotes share its desk",
  "DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116222771000963266']})  # 0400Z: the tiyora__ post is offbeat\nDESK_OVERRIDE_RUN.update({_x:'sports' for _x in ['2116293295278285299']+CTXR+CTXQ})  # 0500Z: Aston Villa legal action against Jamie Carragher and its context replies and quotes are sports")
R("if _c.endswith('0400Z.json') and '/31/' in _c: continue","if _c.endswith('0500Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T0300Z'  # 0400Z: culture/sports/online last read in 0300Z","_last = '2026-10-31T0400Z'  # 0500Z: news/money/science last read in 0400Z")
R("not in requests/plan.json for 2026-10-31T04Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T05Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-31T04Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-31T05Z (desks_not_due)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T04Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T05Z, in its order and in batches of 100 (367 ids; its left_out counts 25 slowed, 0 over cap and 2 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 97 unread first-hop references, then 21 second-hop and 8 third-hop references); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Podz\", \"Grimes\" and \"Lakers\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0400Z; Podz (Brandin Podziemski) and Lakers are the Lakers v Warriors game already attached through Luka, Steph, Warriors and Reaves; Poland is the Constitutional Tribunal event already attached); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"is\" and \"you\" (0400Z used \"the\" and \"this\"), each quoted so X does not reject a bare stopword: (\"is\" lang:en is:quote -is:retweet), (\"you\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T06:00:00Z, end_time 2026-10-31T05:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-24T06:00Z to 2026-10-31T04:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T22:16:00Z (the post\\'s creation minute) and end_time 2026-10-30T22:36:00Z: (conversation_id:2116293295278285299 is:reply) and (quotes_of_tweet_id:2116293295278285299 -is:retweet); the plan gives context.top two reads, so one post: 2116293295278285299 (@AstonVilla statement on legal action against Jamie Carragher, the biggest post new this run under 24 hours old at about 4.5M views); 24 replies and 25 quotes returned, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (12:00 AM EDT","media descriptions. '\n",
"""            f'Day-band run (1:00 AM EDT Oct 31 / 05:00 UTC Oct 31, the 05Z slot; band allowance 42): requests/plan.json is for 2026-10-31T05Z (written 04:07Z after the 0400Z run) and was followed top to bottom (28 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 367 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 25 slowed flat posts and 2 unavailable posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Podz", "Grimes" and "Lakers" (3 reads). rising.global: quote stream "is" and repost stream "you" (2 reads). context.top: AstonVilla 2116293295278285299 (2 reads; 24 replies and 25 quotes in the 20-minute window). '
            f'Screen: 3 reads by id (97 unread first-hop references, then 21 second-hop, then 8 third-hop). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T04Z',","'plan': '2026-10-31T05Z',")
R("    'context': [{'post_id': '2116222771000963266',","    'context': [{'post_id': '2116293295278285299',")
R("f'{REPO}/capture/2026/10/31/0400Z.json'","f'{REPO}/capture/2026/10/31/0500Z.json'")
open('build_capture.py','w').write(s)
print('ok')
