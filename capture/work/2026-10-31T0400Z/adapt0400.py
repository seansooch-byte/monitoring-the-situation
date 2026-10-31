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
R('"""Build capture/2026/10/31/0300Z.json from saved','"""Build capture/2026/10/31/0400Z.json from saved')
R("capture/work/2026-10-31T0300Z'","capture/work/2026-10-31T0400Z'")
R("RUN_ID = '2026-10-31T0300Z'","RUN_ID = '2026-10-31T0400Z'")
L("STARTED = ","STARTED = '2026-10-31T04:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T04:01:00Z'")
R("READS_BEFORE = 893","READS_BEFORE = 865")
L("READS_USED = 28","READS_USED = 42  # 0400Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 865 to 823; no 429 or 503 refusals")
R("datetime(2026,10,31,3,2,tzinfo=timezone.utc).timestamp()  # 0300Z (","datetime(2026,10,31,4,1,tzinfo=timezone.utc).timestamp()  # 0400Z (0300Z used 03:02, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',  # 0300Z: four watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 0300Z: three screen reads; no request asked\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 0400Z: seven watch reads; screen cut by the plan; no request asked\n")
R("    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',","    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',")
R("    'trend_brunson': 'trend_brunson.txt', 'trend_yaxel': 'trend_yaxel.txt', 'trend_kyrie': 'trend_kyrie.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_luka': 'trend_luka.txt', 'trend_curry': 'trend_curry.txt', 'trend_reaves': 'trend_reaves.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment'","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 0400Z: all 19 desks, as the plan for 2026-10-31T04Z lists")
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_brunson','trend.Brunson'),('trend_yaxel','trend.Yaxel'),('trend_kyrie','trend.Kyrie'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_luka','trend.Luka'),('trend_curry','trend.Curry'),('trend_reaves','trend.Reaves'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x) in ('trend.Brunson','trend.Yaxel','trend.Kyrie'): return 'sports'  # 0300Z:",
  "        if str(_x) in ('trend.Luka','trend.Curry','trend.Reaves'): return 'sports'  # 0400Z: Luka Doncic and Austin Reaves (Lakers) against Steph Curry (Warriors) tonight, one event\n        if str(_x) in ('trend.Brunson','trend.Yaxel','trend.Kyrie'): return 'sports'  # 0300Z:")
L("REQ_PICKS = {}","REQ_PICKS = {}  # 0400Z: no request asked (none open and unanswered)")
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 0400Z: replies to CTXHANDLE CTXID in its first 20 minutes (the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['CTXID'] + CTX_REPLIES + CTX_QUOTES  # 0400Z: the context post itself")
R("DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116183370468127167']+CTXR+CTXQ})  # 0300Z: itsszema beetle-bite photo and its replies are offbeat",
  "DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116183370468127167']})  # 0300Z: itsszema beetle-bite photo is offbeat\nDESK_OVERRIDE_RUN.update({_x:'CTXDESK' for _x in ['CTXID']+CTXR+CTXQ})  # 0400Z: the context post and its context replies and quotes share its desk")
R("if _c.endswith('0300Z.json') and '/31/' in _c: continue","if _c.endswith('0400Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T0202Z'  # 0300Z: news/money/science last read in 0202Z","_last = '2026-10-31T0300Z'  # 0400Z: culture/sports/online last read in 0300Z")
R("not in requests/plan.json for 2026-10-31T03Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T04Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-31T03Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-31T04Z (desks_not_due)'")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T03Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T04Z, in its order and in batches of 100 (697 ids; its left_out counts 101 slowed, 0 over cap and 2 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Luka\", \"Curry\" and \"Reaves\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0300Z and are one event, the Lakers (Luka Doncic, Austin Reaves) against the Warriors (Steph Curry); Warriors and Steph are the same game, Poland/Tusk are the Constitutional Tribunal event already attached, #SmackDown was read in 0102Z, and Halloween, Yaxel and Kyrie had posts attached in 0300Z); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (0300Z used \"just\" and \"what\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T05:00:00Z, end_time 2026-10-31T04:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T05:00Z to 2026-10-31T03:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time CTXSTART (the post\\'s creation minute) and end_time CTXEND: (conversation_id:CTXID is:reply) and (quotes_of_tweet_id:CTXID -is:retweet); the plan gives context.top two reads, so one post: CTXID (CTXWHAT); CTXRESULT',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (11:00 PM EDT","media descriptions. '\n",
"""            f'Day-band run (12:00 AM EDT Oct 31 / 04:00 UTC Oct 31, the 04Z slot; band allowance 42): requests/plan.json is for 2026-10-31T04Z (written 03:07Z after the 0300Z run) and was followed top to bottom (42 reads listed, screen cut). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 697 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 101 slowed flat posts and 2 unavailable posts in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Luka", "Curry" and "Reaves" (3 reads, one event: Lakers v Warriors). rising.global: quote stream "the" and repost stream "this" (2 reads). context.top: CTXHANDLE CTXID (2 reads). '
            f'Screen: cut by the plan; unread references left unread. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T03Z',","'plan': '2026-10-31T04Z',")
R("    'context': [{'post_id': '2116183370468127167',","    'context': [{'post_id': 'CTXID',")
R("f'{REPO}/capture/2026/10/31/0300Z.json'","f'{REPO}/capture/2026/10/31/0400Z.json'")
open('build_capture.py','w').write(s)
print('ok')
