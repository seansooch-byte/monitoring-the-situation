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
R('"""Build capture/2026/10/31/0202Z.json from saved','"""Build capture/2026/10/31/0300Z.json from saved')
R("capture/work/2026-10-31T0202Z'","capture/work/2026-10-31T0300Z'")
R("RUN_ID = '2026-10-31T0202Z'","RUN_ID = '2026-10-31T0300Z'")
L("STARTED = ","STARTED = '2026-10-31T03:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T03:02:00Z'")
R("READS_BEFORE = 930","READS_BEFORE = 893")
L("READS_USED = 37","READS_USED = 28  # 0300Z: this run's 28 X calls (watch 4, trends 2, desks 4, sensors 3, viral.global 3, rising.global 2, volume 5, context.top 2, screen 3); the counter fell 893 to 865; no 429 or 503 refusals")
R("datetime(2026,10,31,2,4,tzinfo=timezone.utc).timestamp()  # 0202Z (","datetime(2026,10,31,3,2,tzinfo=timezone.utc).timestamp()  # 0300Z (0202Z used 02:04, ")
R("  # 0202Z: four watch reads\n","  # 0300Z: four watch reads\n")
R("  # 0202Z: three screen reads; no request asked\n","  # 0300Z: three screen reads; no request asked\n")
R("    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',","    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',")
R("    'trend_simons': 'trend_simons.txt', 'trend_bona': 'trend_bona.txt', 'trend_elvis': 'trend_elvis.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_brunson': 'trend_brunson.txt', 'trend_yaxel': 'trend_yaxel.txt', 'trend_kyrie': 'trend_kyrie.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 0300Z: the 4 desks the plan for 2026-10-31T03Z lists")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_simons','trend.Simons'),('trend_bona','trend.Bona'),('trend_elvis','trend.ELVIS'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_brunson','trend.Brunson'),('trend_yaxel','trend.Yaxel'),('trend_kyrie','trend.Kyrie'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x) in ('trend.Simons','trend.Bona'): return 'sports'  # 0202Z:",
  "        if str(_x) in ('trend.Brunson','trend.Yaxel','trend.Kyrie'): return 'sports'  # 0300Z: Jalen Brunson (Knicks), Yaxel Lendeborg (Warriors rookie v Lakers) and Kyrie Irving (Mavericks) in tonight's NBA games\n        if str(_x) in ('trend.Simons','trend.Bona'): return 'sports'  # 0202Z:")
L("REQ_PICKS = {}","REQ_PICKS = {}  # 0300Z: no request asked (none open and unanswered)")
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 0300Z: replies to itsszema 2116183370468127167 in its first 20 minutes (4 returned, the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['2116183370468127167'] + CTX_REPLIES + CTX_QUOTES  # 0300Z: the context post itself; the quote read returned nothing")
R("DESK_OVERRIDE_RUN.update({_x:'entertainment' for _x in ['2116059923759133013']+CTXR+CTXQ})  # 0202Z: Mangaaposts anime clip is entertainment",
  "DESK_OVERRIDE_RUN.update({_x:'entertainment' for _x in ['2116059923759133013']})  # 0202Z: Mangaaposts anime clip is entertainment\nDESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116183370468127167']+CTXR+CTXQ})  # 0300Z: itsszema beetle-bite photo and its replies are offbeat")
R("if _c.endswith('0202Z.json') and '/31/' in _c: continue","if _c.endswith('0300Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T0102Z'  # 0202Z: culture/sports/online last read in 0102Z","_last = '2026-10-31T0202Z'  # 0300Z: news/money/science last read in 0202Z")
R("not in requests/plan.json for 2026-10-31T02Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T03Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-31T02Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-31T03Z (desks_not_due)'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T02Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T03Z, in its order and in batches of 100 (333 ids; its left_out counts 25 slowed, 0 over cap and 1 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 98 unread first-hop references, then 22 second-hop and 10 third-hop references); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Brunson\", \"Yaxel\" and \"Kyrie\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0202Z; Halloween and Simons had posts attached in 0202Z, #SmackDown was read in 0102Z, Kucherov earlier, Poland/Tusk are the Constitutional Tribunal event already attached, and #OPLive is a police reality show left unread); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"just\" and \"what\" (0202Z used \"it\" and \"that\"), each quoted so X does not reject a bare stopword: (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T04:00:00Z, end_time 2026-10-31T03:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T04:00Z to 2026-10-31T02:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T15:00:00Z (the post\\'s creation minute) and end_time 2026-10-30T15:20:00Z: (conversation_id:2116183370468127167 is:reply) and (quotes_of_tweet_id:2116183370468127167 -is:retweet); the plan gives context.top two reads, so one post: 2116183370468127167 (@itsszema beetle-bite photo, the biggest post new this run under 24 hours old at about 3.18M views); the reply read returned 4 replies, the quote read none',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (10:02 PM EDT","media descriptions. '\n",
"""            f'Day-band run (11:00 PM EDT Oct 30 / 03:00 UTC Oct 31, the 03Z slot; band allowance 42): requests/plan.json is for 2026-10-31T03Z (written 02:10Z after the 0202Z run) and was followed top to bottom (28 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 333 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 25 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Brunson", "Yaxel" and "Kyrie" (3 reads). rising.global: quote stream "just" and repost stream "what" (2 reads). context.top: itsszema 2116183370468127167 (2 reads; 4 replies and no quotes in the 20-minute window). '
            f'Screen: 3 reads by id (98 unread first-hop references, then 22 second-hop, then 10 third-hop). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T02Z',","'plan': '2026-10-31T03Z',")
R("    'context': [{'post_id': '2116059923759133013',","    'context': [{'post_id': '2116183370468127167',")
R("f'{REPO}/capture/2026/10/31/0202Z.json'","f'{REPO}/capture/2026/10/31/0300Z.json'")
open('build_capture.py','w').write(s)
print('ok')
