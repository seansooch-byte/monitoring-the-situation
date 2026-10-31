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
R('"""Build capture/2026/10/31/1602Z.json from saved','"""Build capture/2026/10/31/1700Z.json from saved')
R("capture/work/2026-10-31T1602Z'","capture/work/2026-10-31T1700Z'")
R("RUN_ID = '2026-10-31T1602Z'","RUN_ID = '2026-10-31T1700Z'")
L("STARTED = ","STARTED = '2026-10-31T17:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T17:01:00Z'")
R("READS_BEFORE = 534","READS_BEFORE = 492")
L("READS_USED = 42","READS_USED = 30  # 1700Z: this run's 30 X calls (watch 6, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 492 to 462; no 429 or 503 refusals")
R("datetime(2026,10,31,16,3,tzinfo=timezone.utc).timestamp()  # 1602Z (","datetime(2026,10,31,17,1,tzinfo=timezone.utc).timestamp()  # 1700Z (1602Z used 16:03, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 1602Z: seven watch reads; screen cut by the plan; no request asked\n    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt',  # 1700Z: six watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1700Z: three screen reads; no request asked\n    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',\n")
R("    'trend_mrfanboy': 'trend_mrfanboy.txt', 'trend_pikmin': 'trend_pikmin.txt', 'trend_ocon': 'trend_ocon.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_brighton': 'trend_brighton.txt', 'trend_chrisash': 'trend_chrisash.txt', 'trend_navy': 'trend_navy.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1700Z: the 4 desks the plan for 2026-10-31T17Z lists")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_mrfanboy','trend.#MrFanboyEP10'),('trend_pikmin','trend.Pikmin'),('trend_ocon','trend.Ocon'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_brighton','trend.Brighton'),('trend_chrisash','trend.Chris Ash'),('trend_navy','trend.Navy'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.Brighton': return 'sports'  # 1700Z: Brighton 1-0 Manchester City\n        if str(_x)=='trend.Chris Ash': return 'sports'  # 1700Z: Notre Dame defensive coordinator Chris Ash, Notre Dame vs Navy\n        if str(_x)=='trend.Navy': return 'sports'  # 1700Z: mostly Notre Dame vs Navy (an Iran navy story is in the same stream; per-post fixes below)\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1700Z: replies to funny0ver__ 2116406440843780259 in its first 20 minutes (0 returned)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1700Z: quotes in the window (0 returned)")
L("CTX_IDS = [","CTX_IDS = ['2116406440843780259'] + CTX_REPLIES + CTX_QUOTES  # 1700Z: the context post itself; 0 replies and 0 quotes returned in the window")
R("DESK_OVERRIDE_RUN.update({_x:'science' for _x in ['2116523818449805452']+CTXR+CTXQ})  # 1602Z: elonmusk SpaceX 700 Falcon 9 flights post and its context replies and quotes are science",
  "DESK_OVERRIDE_RUN.update({_x:'science' for _x in ['2116523818449805452']})  # 1602Z: elonmusk SpaceX 700 Falcon 9 flights post is science\nDESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116406440843780259']+CTXR+CTXQ})  # 1700Z: funny0ver__ aespa giselle lip-sync post (and any context replies and quotes) is music")
R("if _c.endswith('1602Z.json') and '/31/' in _c: continue","if _c.endswith('1700Z.json') and '/31/' in _c: continue")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):  # noqa keep")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):\n","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):\n")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T1500Z'  # 1602Z: culture/sports/online last read in 1500Z","_last = '2026-10-31T1602Z'  # 1700Z: news/money/science last read in 1602Z")
R("not in requests/plan.json for 2026-10-31T16Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T17Z (rotation: culture/sports/online this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T16Z (day band, allowance 42)","cut by requests/plan.json for 2026-10-31T17Z (day band, allowance 42)")
s=s.replace("not due in requests/plan.json for 2026-10-31T16Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T17Z (desks_not_due)")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T16Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T17Z, in its order and in batches of 100 (540 ids; its left_out counts 9 slowed, 0 over cap and 2 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 6 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 135 unread first-hop references in two reads, then 3 second-hop references, none returned); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Brighton\", \"Chris Ash\" and \"Navy\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the top US names with no posts attached in 1602Z; Halloween, Poland and Manchester United are repeat events attached in 1500Z, MR FANBOY and Ocon were read in 1602Z); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"and\" and \"my\" (1602Z used \"is\" and \"you\"), each quoted so X does not reject a bare stopword: (\"and\" lang:en is:quote -is:retweet), (\"my\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T18:00:00Z, end_time 2026-10-31T17:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-24T18:00Z to 2026-10-31T16:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-31T05:46:00Z (the post\\'s creation minute) and end_time 2026-10-31T06:06:00Z: (conversation_id:2116406440843780259 is:reply) and (quotes_of_tweet_id:2116406440843780259 -is:retweet); the plan gives context.top two reads, so one post: 2116406440843780259 (funny0ver__ post on aespa giselle lip-syncing, 3.72M views, the biggest new post under 24 hours); both searches returned 0 posts in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
a=s.index("            f'Day-band run (12:02 PM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Day-band run (1:00 PM EDT Oct 31 / 17:00 UTC Oct 31, the 17Z slot; band allowance 42): requests/plan.json is for 2026-10-31T17Z (written 16:10Z after the 1602Z run) and was followed top to bottom (30 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1602Z and this run, the counter was 492 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 540 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 9 slowed flat posts and 2 unavailable posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Brighton" (sports: Brighton 1-0 Manchester City), "Chris Ash" (sports: Notre Dame vs Navy) and "Navy" (mostly the same game) (3 reads). rising.global: quote stream "and" and repost stream "my" (2 reads). context.top: funny0ver__ 2116406440843780259 (2 reads; 0 replies and 0 quotes in the 20-minute window). '
            f'Screen: 3 reads by id (135 unread first-hop references in two reads, then 3 second-hop, none returned). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T16Z',","'plan': '2026-10-31T17Z',")
R("    'context': [{'post_id': '2116523818449805452',","    'context': [{'post_id': '2116406440843780259',")
R("f'{REPO}/capture/2026/10/31/1602Z.json'","f'{REPO}/capture/2026/10/31/1700Z.json'")
i=s.index("DESK_OVERRIDE_RUN.update({'2116517088869192115':'world'"); j=s.index("\n",i)+1
s=s[:j]+"""skip_nsfw |= {'2116523146949906605','2116498026865070250'}  # 1700Z: sexual (hotguystiktok locker-room clip; LoveIndia163 lingerie post)
skip_nsfw |= {'2116209329556922392','2116279098259513364','2116316436209828169'}  # 1700Z: likely paid (Roobet slot ad, 129 likes on 251K views; PlayStation podcast promo, 908 likes on 768K views); graphic (Crime_In_NYC body in a garbage bag in Canarsie, same story as the MarioNawfal clip left out in 1105Z)
"""+s[j:]
open('build_capture.py','w').write(s); print('ok')
