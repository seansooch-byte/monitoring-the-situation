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
R('"""Build capture/2026/10/31/1303Z.json from saved','"""Build capture/2026/10/31/1400Z.json from saved')
R("capture/work/2026-10-31T1303Z'","capture/work/2026-10-31T1400Z'")
R("RUN_ID = '2026-10-31T1303Z'","RUN_ID = '2026-10-31T1400Z'")
L("STARTED = ","STARTED = '2026-10-31T14:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T14:02:00Z'")
R("READS_BEFORE = 629","READS_BEFORE = 599")
L("READS_USED = 30","READS_USED = 37  # 1400Z: this run's 37 X calls (watch 4, trends 2, desks 13, volume 5, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 599 to 562; no 429 or 503 refusals")
R("datetime(2026,10,31,13,6,tzinfo=timezone.utc).timestamp()  # 1303Z (","datetime(2026,10,31,14,2,tzinfo=timezone.utc).timestamp()  # 1400Z (1303Z used 13:06, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt',  # 1303Z: six watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1303Z: three screen reads; no request asked\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',  # 1400Z: four watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1400Z: three screen reads; no request asked\n")
R("    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',","    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',")
R("    'trend_schrader': 'trend_schrader.txt', 'trend_monterrey': 'trend_monterrey.txt', 'trend_alcon': 'trend_alcon.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_chemun': 'trend_chemun.txt', 'trend_rogers': 'trend_rogers.txt', 'trend_tire': 'trend_tire.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1400Z: the 13 desks the plan for 2026-10-31T14Z lists")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_schrader','trend.Schrader'),('trend_monterrey','trend.Monterrey'),('trend_alcon','trend.#AlconEntBetrayedPublicTrust'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_chemun','trend.#CHEMUN'),('trend_rogers','trend.Morgan Rogers'),('trend_tire','trend.Tire'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x) in ('trend.#CHEMUN','trend.Morgan Rogers'): return 'sports'  # 1400Z: Chelsea 2-0 Manchester United (Rogers goal, Martinez red card, Palmer penalty), one event with Martinez, Fofana, Amad, Chelsea, Lavia, Estevao, Maguire, Licha and Palmer\n        if str(_x)=='trend.Tire': return 'sports'  # 1400Z: Nigerian Pidgin 'I don tire' match-frustration posts\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1400Z: replies to hobifIwr 2116338118802440640 in its first 20 minutes (4 returned, the three most liked kept)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1400Z: quotes in the window (4 returned, the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['2116338118802440640'] + CTX_REPLIES + CTX_QUOTES  # 1400Z: the context post itself; 4 replies and 4 quotes returned")
R("DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2116187515132518624']+CTXR+CTXQ})  # 1303Z: kellytheboss7 influencer-and-cafe story and its context replies are internet",
  "DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2116187515132518624']})  # 1303Z: kellytheboss7 influencer-and-cafe story is internet\nDESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116338118802440640']+CTXR+CTXQ})  # 1400Z: hobifIwr fan video and its context replies and quotes are music")
R("if _c.endswith('1303Z.json') and '/31/' in _c: continue","if _c.endswith('1400Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T1208Z'  # 1303Z: news/money/science last read in 1208Z","_last = '2026-10-31T1303Z'  # 1400Z: culture/sports/online last read in 1303Z")
R("not in requests/plan.json for 2026-10-31T13Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T14Z (rotation: news/money/science this run)")
R("reason = ('not read: cut by requests/plan.json for 2026-10-31T13Z (day band, allowance 42)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T13Z (desks_not_due)')",
  "reason = ('not read: cut by requests/plan.json for 2026-10-31T14Z (day band, allowance 42)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T14Z (desks_not_due)')")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T13Z","6 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T14Z, in its order and in batches of 100 (338 ids; its left_out counts 10 slowed, 0 over cap and 2 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 151 unread first-hop references in two reads, then 25 second-hop references; THIRDHOP third-hop references left unread); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#CHEMUN\", \"Morgan Rogers\" and \"Tire\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1303Z; Happy Halloween was read in 0959Z, Good Saturday in 1105Z, Schrader in 1303Z, and Poland had a post attached in 1303Z; #CHEMUN, Martinez, Fofana, Amad, Chelsea, Morgan Rogers, Maguire, Licha, Lavia and Estevao are one event, Chelsea 2-0 Manchester United); desks politics/world/justice/markets/ai/tech/medicine/entertainment/music/gaming/sports/internet/offbeat; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"just\" and \"what\" (1303Z used \"it\" and \"that\"), each quoted so X does not reject a bare stopword: (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T15:00:00Z, end_time 2026-10-31T14:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T15:00Z to 2026-10-31T13:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-31T01:15:00Z (the post\\'s creation minute) and end_time 2026-10-31T01:35:00Z: (conversation_id:2116338118802440640 is:reply) and (quotes_of_tweet_id:2116338118802440640 -is:retweet); the plan gives context.top two reads, so one post: 2116338118802440640 (hobifIwr \"NAO ACREDITO QUE GRAVEI ESSE VIDEO\" fan video, 5.9M views, the biggest new post under 24 hours); 4 replies and 4 quotes in the window, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (9:03 AM EDT","media descriptions. '\n",
"""            f'Day-band run (10:00 AM EDT Oct 31 / 14:00 UTC Oct 31, the 14Z slot; band allowance 42): requests/plan.json is for 2026-10-31T14Z (written 13:13Z after the 1303Z run) and was followed top to bottom (37 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1303Z and this run, the counter was 599 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 338 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 10 slowed flat posts and 2 unavailable posts in its left_out were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (the 13 due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#CHEMUN" and "Morgan Rogers" (Chelsea 2-0 Manchester United) and "Tire" (Nigerian Pidgin match-frustration posts) (3 reads). rising.global: quote stream "just" and repost stream "what" (2 reads). context.top: hobifIwr 2116338118802440640 (2 reads; 4 replies and 4 quotes in the 20-minute window). '
            f'Screen: 3 reads by id (151 unread first-hop references in two reads, then 25 second-hop; THIRDHOP third-hop left unread). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T13Z',","'plan': '2026-10-31T14Z',")
R("    'context': [{'post_id': '2116187515132518624',","    'context': [{'post_id': '2116338118802440640',")
R("f'{REPO}/capture/2026/10/31/1303Z.json'","f'{REPO}/capture/2026/10/31/1400Z.json'")
s=s.replace("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):","for batch in ('watch0','watch1','watch2','watch3'):")
open('build_capture.py','w').write(s); print('ok')
