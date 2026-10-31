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
R('"""Build capture/2026/10/31/1208Z.json from saved','"""Build capture/2026/10/31/1303Z.json from saved')
R("capture/work/2026-10-31T1208Z'","capture/work/2026-10-31T1303Z'")
R("RUN_ID = '2026-10-31T1208Z'","RUN_ID = '2026-10-31T1303Z'")
L("STARTED = ","STARTED = '2026-10-31T13:03:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T13:06:00Z'")
R("READS_BEFORE = 671","READS_BEFORE = 629")
L("READS_USED = 42","READS_USED = 30  # 1303Z: this run's 30 X calls (watch 6, trends 2, desks 4, volume 5, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 629 to 599; no 429 or 503 refusals")
R("datetime(2026,10,31,12,9,tzinfo=timezone.utc).timestamp()  # 1208Z (","datetime(2026,10,31,13,6,tzinfo=timezone.utc).timestamp()  # 1303Z (1208Z used 12:09, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 1208Z: seven watch reads; screen cut by the plan; no request asked\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt',  # 1303Z: six watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1303Z: three screen reads; no request asked\n")
R("    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',","    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',")
R("    'trend_angola': 'trend_angola.txt', 'trend_oasis': 'trend_oasis.txt', 'trend_spencer': 'trend_spencer.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_schrader': 'trend_schrader.txt', 'trend_monterrey': 'trend_monterrey.txt', 'trend_alcon': 'trend_alcon.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1303Z: the 4 desks the plan for 2026-10-31T13Z lists")
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_angola','trend.#AngolaWordAblaze'),('trend_oasis','trend.#OASISxJoongDunk'),('trend_spencer','trend.Spencer Lee'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_schrader','trend.Schrader'),('trend_monterrey','trend.Monterrey'),('trend_alcon','trend.#AlconEntBetrayedPublicTrust'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.Schrader': return 'sports'  # 1303Z: Broncos RB Cody Schrader expected to be elevated (the Hank Schrader Breaking Bad post is entertainment by desk rule)\n        if str(_x)=='trend.Monterrey': return 'music'  # 1303Z: Taemin LiMiNaL world tour shows in Monterrey\n        if str(_x)=='trend.#AlconEntBetrayedPublicTrust': return 'gaming'  # 1303Z: Chinese fan campaign against Papergames (#PapergamesTarnishesCNIntegrity), one event with #北京应重视上海叠纸两岸争议\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1303Z: replies to kellytheboss7 2116187515132518624 in its first 20 minutes (4 returned, the three most liked kept)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1303Z: quotes in the window (none returned)")
L("CTX_IDS = [","CTX_IDS = ['2116187515132518624'] + CTX_REPLIES + CTX_QUOTES  # 1303Z: the context post itself; 4 replies and no quotes returned")
R("DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116236558852657655']+CTXR+CTXQ})  # 1208Z: the IsraelMilitaryX Vance rumour post and its context replies and quotes are politics",
  "DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116236558852657655']})  # 1208Z: the IsraelMilitaryX Vance rumour post is politics\nDESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2116187515132518624']+CTXR+CTXQ})  # 1303Z: kellytheboss7 influencer-and-cafe story and its context replies are internet")
R("if _c.endswith('1208Z.json') and '/31/' in _c: continue","if _c.endswith('1303Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T1105Z'  # 1208Z: culture/sports/online last read in 1105Z","_last = '2026-10-31T1208Z'  # 1303Z: news/money/science last read in 1208Z")
R("not in requests/plan.json for 2026-10-31T12Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T13Z (rotation: culture/sports/online this run)")
R("reason = ('not read: cut by requests/plan.json for 2026-10-31T12Z (day band, allowance 42)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T12Z (desks_not_due)')",
  "reason = ('not read: cut by requests/plan.json for 2026-10-31T13Z (day band, allowance 42)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T13Z (desks_not_due)')")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T12Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T13Z, in its order and in batches of 100 (549 ids; its left_out counts 7 slowed, 0 over cap and 1 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 6 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 114 unread first-hop references in two reads, then 17 second-hop references; 9 third-hop references left unread); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Schrader\", \"Monterrey\" and \"#AlconEntBetrayedPublicTrust\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1208Z; Happy Halloween and #YouManiacSeriesFinalEP/MANIAC FINAL MOMENT were read in 0959Z and Good Saturday in 1105Z; #AlconEntBetrayedPublicTrust and #北京应重视上海叠纸两岸争议 are one Papergames fan campaign); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"it\" and \"that\" (1208Z used \"and\" and \"my\"), each quoted so X does not reject a bare stopword: (\"it\" lang:en is:quote -is:retweet), (\"that\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T14:00:00Z, end_time 2026-10-31T13:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-24T14:00Z to 2026-10-31T12:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T15:16:00Z (the post\\'s creation minute) and end_time 2026-10-30T15:36:00Z: (conversation_id:2116187515132518624 is:reply) and (quotes_of_tweet_id:2116187515132518624 -is:retweet); the plan gives context.top two reads, so one post: 2116187515132518624 (kellytheboss7 \"An influencer asked my café for free food\" post, 2.1M views, the biggest new post under 24 hours once the likely-paid Lenovo promo is left out); 4 replies (3 of them the author\\'s own thread) and no quotes in the window, the three most liked replies kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (8:08 AM EDT","media descriptions. '\n",
"""            f'Day-band run (9:03 AM EDT Oct 31 / 13:03 UTC Oct 31, the 13Z slot; band allowance 42): requests/plan.json is for 2026-10-31T13Z (written 12:17Z after the 1208Z run) and was followed top to bottom (30 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1208Z and this run, the counter was 629 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 549 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 7 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Schrader" (Broncos RB Cody Schrader), "Monterrey" (Taemin tour stop) and "#AlconEntBetrayedPublicTrust" (Chinese fan campaign against Papergames) (3 reads). rising.global: quote stream "it" and repost stream "that" (2 reads). context.top: kellytheboss7 2116187515132518624 (2 reads; 4 replies and no quotes in the 20-minute window). '
            f'Screen: 3 reads by id (114 unread first-hop references in two reads, then 17 second-hop; 9 third-hop left unread). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T12Z',","'plan': '2026-10-31T13Z',")
R("    'context': [{'post_id': '2116236558852657655',","    'context': [{'post_id': '2116187515132518624',")
R("f'{REPO}/capture/2026/10/31/1208Z.json'","f'{REPO}/capture/2026/10/31/1303Z.json'")
open('build_capture.py','w').write(s); print('ok')
# applied after first build attempt: watch batch loops cut to six
s=open('build_capture.py').read()
s=s.replace("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):")
open('build_capture.py','w').write(s)
# applied: skip line for 1303Z (Lenovo likely paid; Monterrey #swingers post sexual)
