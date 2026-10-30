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
R('"""Build capture/2026/10/30/1507Z.json from saved','"""Build capture/2026/10/30/1608Z.json from saved')
R("capture/work/2026-10-30T1507Z'","capture/work/2026-10-30T1608Z'")
R("RUN_ID = '2026-10-30T1507Z'","RUN_ID = '2026-10-30T1608Z'")
L("STARTED = ","STARTED = '2026-10-30T16:08:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T16:09:00Z'")
R("READS_BEFORE = 589","READS_BEFORE = 561")
L("READS_USED = 28","READS_USED = 42  # 1608Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 561 to 519; no 429 or 503 refusals")
R("datetime(2026,10,30,15,8,tzinfo=timezone.utc).timestamp()  # 1507Z (","datetime(2026,10,30,16,9,tzinfo=timezone.utc).timestamp()  # 1608Z (1507Z used 15:08, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',\n")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
R("    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',\n","")
R("    'quote_my': 'quote_my.txt',\n    'repost_it': 'repost_it.txt',","    'quote_that': 'quote_that.txt',\n    'repost_just': 'repost_just.txt',")
R("    'trend_halloween': 'trend_halloween.txt', 'trend_toddwash': 'trend_toddwash.txt', 'trend_yormark': 'trend_yormark.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_lastfour': 'trend_lastfour.txt', 'trend_goodfriday': 'trend_goodfriday.txt', 'trend_kansasiowa': 'trend_kansasiowa.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 1608Z: all 19 desks, as requests/plan.json for 2026-10-30T16Z lists")
R("""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_halloween','trend.Happy Halloween'),('trend_toddwash','trend.Todd Wash'),('trend_yormark','trend.Brett Yormark'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_lastfour','trend.#LastFourWatched'),('trend_goodfriday','trend.Good Friday'),('trend_kansasiowa','trend.Kansas and Iowa'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x)=='trend.Happy Halloween': return 'life'  # 1507Z: Halloween greeting posts\n",
  "        if str(_x)=='trend.Happy Halloween': return 'life'  # 1507Z: Halloween greeting posts\n        if str(_x)=='trend.Kansas and Iowa': return 'politics'  # 1608Z: Trump reinstates Sunday rallies in Kansas and Iowa\n")
R("CTX_REPLIES = CTXR  # 1507Z: replies to 0xngmi 2115918200013533203 in its first 20 minutes, the three most liked kept",
  "CTX_REPLIES = CTXR  # 1608Z: replies to SMO_VZ 2115940979039404540 in its first 20 minutes; relevancy returned none")
R("CTX_IDS = ['2115918200013533203'] + CTX_REPLIES","CTX_IDS = ['2115940979039404540'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2115918200013533203']+CTXR+CTXQ})  # 1507Z:",
  "DESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2115918200013533203']})\nDESK_OVERRIDE_RUN.update({_x:'world' for _x in ['2115940979039404540']+CTXR+CTXQ})  # 1608Z: SMO_VZ post on the war in Ukraine is world  # 1507Z:")
R("if _c.endswith('1507Z.json') and '/30/' in _c: continue","if _c.endswith('1608Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T1402Z'  # 1507Z: news/money/science last read in 1402Z","_last = '2026-10-30T1507Z'  # 1608Z: culture/sports/online last read in 1507Z")
R("not in requests/plan.json for 2026-10-30T15Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T16Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T15Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T16Z (desks_not_due)'")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T15Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T16Z, in its order and in batches of 100 (661 ids; the plan\\'s note: \"46 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 71 flat posts wait for their sixth run\"; its left_out counts 71 slowed, 0 over cap and 3 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read and a second hop by id","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#LastFourWatched\", \"Good Friday\" and \"Kansas and Iowa\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 1507Z; \"Evero\" is one event with \"Todd Wash\", read in 1507Z); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"that\" and \"just\" (1507Z used \"my\" and \"it\"), each quoted so X does not reject a bare stopword: (\"that\" lang:en is:quote -is:retweet), (\"just\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T17:00:00Z, end_time 2026-10-30T16:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-23T17:00Z to 2026-10-30T15:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T22:56:00Z (the post\\'s creation minute) and end_time 2026-10-29T23:16:00Z: (conversation_id:2115940979039404540 is:reply) and (quotes_of_tweet_id:2115940979039404540 -is:retweet); the plan gives context.top two reads, so one post: 2115940979039404540 (@SMO_VZ post on the war in Ukraine, the biggest post new this run under 24 hours old at about 0.93M views; two bigger new posts were over 24 hours old and one was sexual); no replies and no quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (10:07 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (11:08 AM CT Oct 30 / 16:08 UTC Oct 30, the 16Z slot; band allowance 42): requests/plan.json is for 2026-10-30T16Z (written 15:19Z after the 1507Z capture), so it was followed (42 reads listed, screen cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 661 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 71 slowed flat posts and 3 unavailable in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#LastFourWatched", "Good Friday" and "Kansas and Iowa" (3 reads). rising.global: quote stream "that" and repost stream "just" (2 reads). context.top: SMO_VZ 2115940979039404540 (2 reads, nothing returned in the window). '
            f'Screen: cut by the plan; unread second-hop references left unread. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T15Z',","'plan': '2026-10-30T16Z',")
R("    'context': [{'post_id': '2115918200013533203',","    'context': [{'post_id': '2115940979039404540',")
R("f'{REPO}/capture/2026/10/30/1507Z.json'","f'{REPO}/capture/2026/10/30/1608Z.json'")
open('build_capture.py','w').write(s)
print('ok')
