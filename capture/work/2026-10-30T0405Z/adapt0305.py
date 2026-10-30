s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/30/0208Z.json from saved','"""Build capture/2026/10/30/0305Z.json from saved')
R("capture/work/2026-10-30T0207Z'","capture/work/2026-10-30T0305Z'")
R("RUN_ID = '2026-10-30T0208Z'","RUN_ID = '2026-10-30T0305Z'")
R("STARTED = '2026-10-30T02:08:00Z'","STARTED = '2026-10-30T03:05:00Z'")
R("OBS_AT = '2026-10-30T02:08:00Z'","OBS_AT = '2026-10-30T03:06:00Z'")
R("READS_BEFORE = 960","READS_BEFORE = 933")
SPAN("READS_USED = 27","\n","READS_USED = 36  # 0305Z: this run's 36 X calls (watch 3, desks 13, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 933 to 897; no 429 or 503 refusals\n")
R("datetime(2026,10,30,2,8,tzinfo=timezone.utc).timestamp()  # 0207Z (","datetime(2026,10,30,3,6,tzinfo=timezone.utc).timestamp()  # 0305Z (0207Z used 02:08, ")
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',","'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",2)
R("""    'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_packers': 'trend_packers.txt', 'trend_matthewgolden': 'trend_matthewgolden.txt', 'trend_christianwatson': 'trend_christianwatson.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_panthers': 'trend_panthers.txt', 'trend_bryceyoung': 'trend_bryceyoung.txt', 'trend_binance': 'trend_binance.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
SPAN("DUE = ['politics','entertainment','sports','internet']","\n","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 0305Z: the 13 desks the plan for 2026-10-30T03Z lists\n")
R("""    ('quote_this','quote'),('repost_is','repost'),
    ('trend_packers','trend.Packers'),('trend_matthewgolden','trend.Matthew Golden'),('trend_christianwatson','trend.Christian Watson'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_panthers','trend.Panthers'),('trend_bryceyoung','trend.Bryce Young'),('trend_binance','trend.Binance'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("if _c.endswith('0208Z.json') and '/30/' in _c: continue","if _c.endswith('0305Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T0109Z'  # 0207Z: culture/sports/online last read in 0109Z","_last = '2026-10-30T0208Z'  # 0305Z: news/money/science last read in 0208Z")
R("not in requests/plan.json for 2026-10-30T02Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T03Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-30T02Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-30T03Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['entertainment','music','gaming','ideas','politics']")
R("CTX_REPLIES = CTXR  # 0207Z: replies to redbaronpizza 2115917093182792143","CTX_REPLIES = CTXR  # 0305Z: replies to CreatureonX 2115710979531268106 (none in the window)")
R("CTX_IDS = ['2115917093182792143'] + CTX_REPLIES","CTX_IDS = ['2115710979531268106'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T02Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T03Z, in its order and in batches of 100 (281 ids; its left_out counts 12 slowed flat posts and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, then screened by id (3 screen reads: 131 unread references in two reads, then 30 second-hop); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Panthers\", \"Bryce Young\" and \"Binance\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first three top-ten US names with no posts attached in 0208Z; \"Panthers\" and \"Bryce Young\" are one event with \"Christian Watson\", \"Packers\", \"Jordan Love\", \"Matthew Golden\" and \"#GoPackGo\": Panthers at Packers on Thursday Night Football; \"Binance\" is the suspected Binance hack; \"Red Baron\" (also unattached) left for lack of reads)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"you\" and \"and\" (0208Z used \"this\" and \"is\"), each quoted so X does not reject a bare stopword: (\"you\" lang:en is:quote -is:retweet), (\"and\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T04:00:00Z, end_time 2026-10-30T03:00:00Z, one read per desk for the 5 desks the plan lists (volume.entertainment, volume.music, volume.gaming, volume.ideas, volume.politics); each series is the 167 full hours 2026-10-23T04:00Z to 2026-10-30T02:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T07:43:00Z (the post\\'s creation minute) and end_time 2026-10-29T08:03:00Z: (conversation_id:2115710979531268106 is:reply) and (quotes_of_tweet_id:2115710979531268106 -is:retweet); the plan gives context.top two reads, so one post: 2115710979531268106 (@CreatureonX hamster cheek-pouch video, the biggest post new this run at about 3.06M views); 0 replies and 1 quote in the window, the quote kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (9:08 PM CT","f'Screen: 2 reads by id (99 unread references, then 25 second-hop). '\n",
 "            f'Day-band run (10:05 PM CT Oct 29 / 03:05 UTC Oct 30, the 03Z slot; band allowance 42): requests/plan.json is for 2026-10-30T03Z (written 02:15Z after the 0208Z capture), so it was followed (36 reads listed, nothing cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 281 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 12 slowed flat posts and 2 unavailable in its left_out were not read. '\n"
 "            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet, offbeat (the 13 the plan lists). Volume: entertainment, music, gaming, ideas and politics (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Panthers\", \"Bryce Young\" and \"Binance\" (3 reads). rising.global: quote stream \"you\" and repost stream \"and\" (2 reads). context.top: CreatureonX 2115710979531268106 (2 reads). '\n"
 "            f'Screen: 3 reads by id (131 unread references, then 30 second-hop). '\n")
R("'plan': '2026-10-30T02Z',","'plan': '2026-10-30T03Z',")
R("    'context': [{'post_id': '2115917093182792143',","    'context': [{'post_id': '2115710979531268106',")
R("capture/2026/10/30/0208Z.json'","capture/2026/10/30/0305Z.json'")
anchor="DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2115917093182792143']+CTXR+CTXQ})"
i=s.index(anchor); j=s.index("\n",i)+1
s=s[:j]+"DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2115710979531268106']+CTXR+CTXQ})  # 0305Z: CreatureonX hamster video and its context quote are offbeat (animals)\n"+s[j:]
open('build_capture.py','w').write(s); print('ok')
