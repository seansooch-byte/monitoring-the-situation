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
R('"""Build capture/2026/10/31/1400Z.json from saved','"""Build capture/2026/10/31/1500Z.json from saved')
R("capture/work/2026-10-31T1400Z'","capture/work/2026-10-31T1500Z'")
R("RUN_ID = '2026-10-31T1400Z'","RUN_ID = '2026-10-31T1500Z'")
L("STARTED = ","STARTED = '2026-10-31T15:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T15:02:00Z'")
R("READS_BEFORE = 599","READS_BEFORE = 562")
L("READS_USED = 37","READS_USED = 28  # 1500Z: this run's 28 X calls (watch 4, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 562 to 534; no 429 or 503 refusals")
R("datetime(2026,10,31,14,2,tzinfo=timezone.utc).timestamp()  # 1400Z (","datetime(2026,10,31,15,2,tzinfo=timezone.utc).timestamp()  # 1500Z (1400Z used 14:02, ")
R("  # 1400Z: four watch reads\n","  # 1500Z: four watch reads\n")
R("  # 1400Z: three screen reads; no request asked\n","  # 1500Z: three screen reads; no request asked\n")
R("    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',","    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',")
R("    'trend_chemun': 'trend_chemun.txt', 'trend_rogers': 'trend_rogers.txt', 'trend_tire': 'trend_tire.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_halloween': 'trend_halloween.txt', 'trend_poland': 'trend_poland.txt', 'trend_manutd': 'trend_manutd.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1500Z: the 4 desks the plan for 2026-10-31T15Z lists")
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_chemun','trend.#CHEMUN'),('trend_rogers','trend.Morgan Rogers'),('trend_tire','trend.Tire'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_halloween','trend.Happy Halloween'),('trend_poland','trend.Poland'),('trend_manutd','trend.Manchester United'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.Manchester United': return 'sports'  # 1500Z: Chelsea 2-0 Manchester United aftermath, one event with Martinez, Chelsea, Lavia, Estevao, #CHEMUN, Fofana, Amad and Maguire\n        if str(_x)=='trend.Poland': return 'world'  # 1500Z: the Constitutional Tribunal standoff (one event with Tusk)\n        if str(_x)=='trend.Happy Halloween': return 'life'  # 1500Z: Halloween greetings\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1500Z: replies to warriors 2116379133672612201 in its first 20 minutes (25 returned, the three most liked kept)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1500Z: quotes in the window (25 returned, the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['2116379133672612201'] + CTX_REPLIES + CTX_QUOTES  # 1500Z: the context post itself; 25 replies and 25 quotes returned")
R("DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116338118802440640']+CTXR+CTXQ})  # 1400Z: hobifIwr fan video and its context replies and quotes are music",
  "DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116338118802440640']})  # 1400Z: hobifIwr fan video is music\nDESK_OVERRIDE_RUN.update({_x:'sports' for _x in ['2116379133672612201']+CTXR+CTXQ})  # 1500Z: warriors Curry three and its context replies and quotes are sports")
R("if _c.endswith('1400Z.json') and '/31/' in _c: continue","if _c.endswith('1500Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T1303Z'  # 1400Z: culture/sports/online last read in 1303Z","_last = '2026-10-31T1400Z'  # 1500Z: news/money/science last read in 1400Z")
R("not in requests/plan.json for 2026-10-31T14Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T15Z (rotation: culture/sports/online this run)")
R("reason = ('not read: cut by requests/plan.json for 2026-10-31T14Z (day band, allowance 42)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T14Z (desks_not_due)')",
  "reason = ('not read: cut by requests/plan.json for 2026-10-31T15Z (day band, allowance 42)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T15Z (desks_not_due)')")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T14Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T15Z, in its order and in batches of 100 (367 ids; its left_out counts 8 flat posts waiting for their sixth run, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 110 unread first-hop references in two reads, then 21 second-hop references; 9 third-hop references left unread); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Happy Halloween\", \"Poland\" and \"Manchester United\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1400Z; Happy Halloween was last read in 0959Z and Poland in 1105Z; Martinez, Chelsea, Manchester United, Lavia, Estevao, #CHEMUN, Fofana and Amad are one event, Chelsea 2-0 Manchester United, so one name was read for it); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (1400Z used \"just\" and \"what\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T16:00:00Z, end_time 2026-10-31T15:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T16:00Z to 2026-10-31T14:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-31T03:58:00Z (the post\\'s creation minute) and end_time 2026-10-31T04:18:00Z: (conversation_id:2116379133672612201 is:reply) and (quotes_of_tweet_id:2116379133672612201 -is:retweet); the plan gives context.top two reads, so one post: 2116379133672612201 (warriors \"A 3PT MASTERCLASS FROM STEPHEN\" clip, 8.26M views, the biggest new post under 24 hours once the srkntnyldz street-assault clip of a private woman is passed over); 25 replies and 25 quotes in the window, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (10:00 AM EDT","media descriptions. '\n",
"""            f'Day-band run (11:00 AM EDT Oct 31 / 15:00 UTC Oct 31, the 15Z slot; band allowance 42): requests/plan.json is for 2026-10-31T15Z (written 14:06Z after the 1400Z run) and was followed top to bottom (28 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1400Z and this run, the counter was 562 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 367 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 8 flat posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Happy Halloween" (life), "Poland" (world: the Constitutional Tribunal standoff) and "Manchester United" (sports: Chelsea 2-0 Manchester United) (3 reads). rising.global: quote stream "the" and repost stream "this" (2 reads). context.top: warriors 2116379133672612201 (2 reads; 25 replies and 25 quotes in the 20-minute window). '
            f'Screen: 3 reads by id (110 unread first-hop references in two reads, then 21 second-hop; 9 third-hop left unread). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T14Z',","'plan': '2026-10-31T15Z',")
R("    'context': [{'post_id': '2116338118802440640',","    'context': [{'post_id': '2116379133672612201',")
R("f'{REPO}/capture/2026/10/31/1400Z.json'","f'{REPO}/capture/2026/10/31/1500Z.json'")
open('build_capture.py','w').write(s); print('ok')
