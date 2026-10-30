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
R('"""Build capture/2026/10/30/1402Z.json from saved','"""Build capture/2026/10/30/1507Z.json from saved')
R("capture/work/2026-10-30T1402Z'","capture/work/2026-10-30T1507Z'")
R("RUN_ID = '2026-10-30T1402Z'","RUN_ID = '2026-10-30T1507Z'")
L("STARTED = ","STARTED = '2026-10-30T15:07:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T15:08:00Z'")
R("READS_BEFORE = 626","READS_BEFORE = 589")
L("READS_USED = 37","READS_USED = 27  # 1507Z: this run's 27 X calls (watch 4, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of its 3); the counter fell 589 to 562; no 429 or 503 refusals")
R("datetime(2026,10,30,14,3,tzinfo=timezone.utc).timestamp()  # 1402Z (","datetime(2026,10,30,15,8,tzinfo=timezone.utc).timestamp()  # 1507Z (1402Z used 14:03, ")
R("    'quote_you': 'quote_you.txt',\n    'repost_and': 'repost_and.txt',","    'quote_my': 'quote_my.txt',\n    'repost_it': 'repost_it.txt',")
R("    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',","    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',")
R("    'trend_halloweeneve': 'trend_halloweeneve.txt', 'trend_binance': 'trend_binance.txt', 'trend_friyay': 'trend_friyay.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_halloween': 'trend_halloween.txt', 'trend_toddwash': 'trend_toddwash.txt', 'trend_yormark': 'trend_yormark.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world','justice'","DUE = ['politics','entertainment','sports','internet']  # 1507Z: the four hourly desks requests/plan.json for 2026-10-30T15Z lists")
R("""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_halloweeneve','trend.Happy Halloween Eve'),('trend_binance','trend.Binance'),('trend_friyay','trend.Happy Friyay'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_halloween','trend.Happy Halloween'),('trend_toddwash','trend.Todd Wash'),('trend_yormark','trend.Brett Yormark'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x) in ('trend.Good Friday','trend.Happy Friyay'): return 'life'  # 1106Z: Friday morning greeting posts\n",
  "        if str(_x) in ('trend.Good Friday','trend.Happy Friyay'): return 'life'  # 1106Z: Friday morning greeting posts\n        if str(_x)=='trend.Happy Halloween': return 'life'  # 1507Z: Halloween greeting posts\n        if str(_x) in ('trend.Todd Wash','trend.Brett Yormark','trend.Ejiro Evero'): return 'sports'  # 1507Z: Panthers fire DC Ejiro Evero, Todd Wash interim; Big 12 commissioner Yormark leaving\n")
R("CTX_REPLIES = CTXR  # 1402Z: replies to DiscussingFilm 2115821092950684009 in its first 20 minutes, the three most liked kept",
  "CTX_REPLIES = CTXR  # 1507Z: replies to 0xngmi 2115918200013533203 in its first 20 minutes, the three most liked kept")
R("CTX_IDS = ['2115821092950684009'] + CTX_REPLIES","CTX_IDS = ['2115918200013533203'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'gaming' for _x in ['2115821092950684009']+CTXR+CTXQ})  # 1402Z:",
  "DESK_OVERRIDE_RUN.update({_x:'gaming' for _x in ['2115821092950684009']})\nDESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2115918200013533203']+CTXR+CTXQ})  # 1507Z: 0xngmi post on Binance custody and frozen USDT/USDC losses and its context replies and quotes are markets  # 1402Z:")
R("if _c.endswith('1402Z.json') and '/30/' in _c: continue","if _c.endswith('1507Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T1305Z'  # 1402Z: culture/sports/online last read in 1305Z","_last = '2026-10-30T1402Z'  # 1507Z: news/money/science last read in 1402Z")
R("not in requests/plan.json for 2026-10-30T14Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T15Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T14Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T15Z (desks_not_due)'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T14Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T15Z, in its order and in batches of 100 (367 ids; the plan\\'s note: \"48 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 14 flat posts wait for their sixth run\"; its left_out counts 14 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read and a second hop by id","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 2 reads by id of the plan\\'s 3, 84 unread references then 1 second-hop (not found); nothing left to read); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Happy Halloween\", \"Todd Wash\" and \"Brett Yormark\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 1402Z; \"RED Friday\" was read in 1305Z and \"#LastFourWatched\", \"Kansas and Iowa\" and \"Jack Black\" were not read; \"Todd Wash\" and the US name \"Ejiro Evero\" are one event, the Panthers firing defensive coordinator Ejiro Evero and naming Todd Wash interim)',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"my\" and \"it\" (1402Z used \"you\" and \"and\"), each quoted so X does not reject a bare stopword: (\"my\" lang:en is:quote -is:retweet), (\"it\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T16:00:00Z, end_time 2026-10-30T15:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-23T16:00Z to 2026-10-30T14:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T21:26:00Z (the post\\'s creation minute) and end_time 2026-10-29T21:46:00Z: (conversation_id:2115918200013533203 is:reply) and (quotes_of_tweet_id:2115918200013533203 -is:retweet); the plan gives context.top two reads, so one post: 2115918200013533203 (@0xngmi post on Binance assets under custody and the loss with USDT and USDC frozen, the biggest post new this run under 24 hours old at about 2.50M views); 25 replies and 9 quotes, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (9:02 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (10:07 AM CT Oct 30 / 15:07 UTC Oct 30, the 15Z slot; band allowance 42): requests/plan.json is for 2026-10-30T15Z (written 14:10Z after the 1402Z capture), so it was followed (28 reads listed) top to bottom; screen needed 2 of its 3 reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 367 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 14 slowed flat posts and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four the plan lists; the other 15 not due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Happy Halloween", "Todd Wash" and "Brett Yormark" (3 reads). rising.global: quote stream "my" and repost stream "it" (2 reads). context.top: 0xngmi 2115918200013533203 (2 reads). '
            f'Screen: 2 reads by id (84 unread references, then 1 second-hop, not found). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T14Z',","'plan': '2026-10-30T15Z',")
R("    'context': [{'post_id': '2115821092950684009',","    'context': [{'post_id': '2115918200013533203',")
R("f'{REPO}/capture/2026/10/30/1402Z.json'","f'{REPO}/capture/2026/10/30/1507Z.json'")
open('build_capture.py','w').write(s)
print('ok')
