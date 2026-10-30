s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/30/0305Z.json from saved','"""Build capture/2026/10/30/0405Z.json from saved')
R("capture/work/2026-10-30T0305Z'","capture/work/2026-10-30T0405Z'")
R("RUN_ID = '2026-10-30T0305Z'","RUN_ID = '2026-10-30T0405Z'")
R("STARTED = '2026-10-30T03:05:00Z'","STARTED = '2026-10-30T04:05:00Z'")
R("OBS_AT = '2026-10-30T03:06:00Z'","OBS_AT = '2026-10-30T04:06:00Z'")
R("READS_BEFORE = 933","READS_BEFORE = 897")
SPAN("READS_USED = 36","\n","READS_USED = 30  # 0405Z: this run's 30 X calls (watch 7, desks 4, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 897 to 867; no 429 or 503 refusals\n")
R("datetime(2026,10,30,3,6,tzinfo=timezone.utc).timestamp()  # 0305Z (","datetime(2026,10,30,4,6,tzinfo=timezone.utc).timestamp()  # 0405Z (0305Z used 03:06, ")
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',","'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
R("""    'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_panthers': 'trend_panthers.txt', 'trend_bryceyoung': 'trend_bryceyoung.txt', 'trend_binance': 'trend_binance.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""","""    'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_redbaron': 'trend_redbaron.txt', 'trend_joshjacobs': 'trend_joshjacobs.txt', 'trend_gopackgo': 'trend_gopackgo.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
SPAN("DUE = ['politics','world'","\n","DUE = ['politics','entertainment','sports','internet']  # 0405Z: the 4 desks the plan for 2026-10-30T04Z lists\n")
R("""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_panthers','trend.Panthers'),('trend_bryceyoung','trend.Bryce Young'),('trend_binance','trend.Binance'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_redbaron','trend.Red Baron'),('trend_joshjacobs','trend.Josh Jacobs'),('trend_gopackgo','trend.#GoPackGo'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("if _c.endswith('0305Z.json') and '/30/' in _c: continue","if _c.endswith('0405Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T0208Z'  # 0305Z: news/money/science last read in 0208Z","_last = '2026-10-30T0305Z'  # 0405Z: culture/sports/online last read in 0305Z")
R("not in requests/plan.json for 2026-10-30T03Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T04Z (rotation: news/money/science this run)")
R("reason = 'not due in requests/plan.json for 2026-10-30T03Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-30T04Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['entertainment','music','gaming','ideas','politics']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("CTX_REPLIES = CTXR  # 0305Z","\n","CTX_REPLIES = CTXR  # 0405Z: replies to MarioNawfal 2115674710381883569 in its first 20 minutes; relevancy returned 9, the three most liked kept\n")
R("CTX_IDS = ['2115710979531268106'] + CTX_REPLIES","CTX_IDS = ['2115674710381883569'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2115710979531268106']+CTXR+CTXQ})","DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2115710979531268106']})\nDESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2115674710381883569']+CTXR+CTXQ})  # 0405Z: MarioNawfal post on the Red Baron worker fundraiser and its context replies are internet\n#")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T03Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T04Z, in its order and in batches of 100 (638 ids; its left_out counts 67 slowed flat posts and 3 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, then screened by id (3 screen reads: 114 unread references in two reads, then 31 second-hop); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Red Baron\", \"Josh Jacobs\" and \"#GoPackGo\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the three top-ten US names with no posts attached in 0305Z; \"Josh Jacobs\" and \"#GoPackGo\" are one event with \"Panthers\", \"Packers\", \"Christian Watson\", \"Bryce Young\" and \"Jordan Love\": Panthers at Packers on Thursday Night Football; \"Red Baron\" is the fundraiser for the Red Baron worker harassed by pranksters)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"my\" and \"it\" (0305Z used \"you\" and \"and\"), each quoted so X does not reject a bare stopword: (\"my\" lang:en is:quote -is:retweet), (\"it\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T05:00:00Z, end_time 2026-10-30T04:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat); each series is the 167 full hours 2026-10-23T05:00Z to 2026-10-30T03:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T05:18:00Z (the post\\'s creation minute) and end_time 2026-10-29T05:38:00Z: (conversation_id:2115674710381883569 is:reply) and (quotes_of_tweet_id:2115674710381883569 -is:retweet); the plan gives context.top two reads, so one post: 2115674710381883569 (@MarioNawfal on the fundraiser for the Red Baron worker, the biggest post new this run under 24 hours old at about 1.82M views); 9 replies and 0 quotes in the window, the three most liked replies kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (10:05 PM CT","f'Screen: 3 reads by id (131 unread references, then 30 second-hop). '\n",
 "            f'Day-band run (11:05 PM CT Oct 29 / 04:05 UTC Oct 30, the 04Z slot; band allowance 42): requests/plan.json is for 2026-10-30T04Z (written 03:13Z after the 0305Z capture), so it was followed (30 reads listed, nothing cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 638 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 67 slowed flat posts and 3 unavailable in its left_out were not read. '\n"
 "            f'Desks: politics, entertainment, sports, internet (the 4 the plan lists). Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Red Baron\", \"Josh Jacobs\" and \"#GoPackGo\" (3 reads). rising.global: quote stream \"my\" and repost stream \"it\" (2 reads). context.top: MarioNawfal 2115674710381883569 (2 reads). '\n"
 "            f'Screen: 3 reads by id (114 unread references, then 31 second-hop). '\n")
R("'plan': '2026-10-30T03Z',","'plan': '2026-10-30T04Z',")
R("'context': [{'post_id': '2115710979531268106',","'context': [{'post_id': '2115674710381883569',")
R("f'{REPO}/capture/2026/10/30/0305Z.json'","f'{REPO}/capture/2026/10/30/0405Z.json'")
open('build_capture.py','w').write(s)
print('ok')
s=open('build_capture.py').read()
_a="EXTRA_PRIVATE |= {'2113983193174962294'}  # 0207Z"
assert s.count(_a)==1
s=s.replace(_a,"EXTRA_PRIVATE |= {'2115674710381883569'} | set(CTXR) | set(CTXQ)  # 0405Z: MarioNawfal post on the Red Baron worker (a private man; it describes him and his 4 kids) and its context replies, as with the redbaronpizza post and its replies in 0207Z\n"+_a)
open('build_capture.py','w').write(s)
print('ok2')
