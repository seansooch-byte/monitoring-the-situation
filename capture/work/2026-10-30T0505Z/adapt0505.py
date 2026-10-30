s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/30/0405Z.json from saved','"""Build capture/2026/10/30/0505Z.json from saved')
R("capture/work/2026-10-30T0405Z'","capture/work/2026-10-30T0505Z'")
R("RUN_ID = '2026-10-30T0405Z'","RUN_ID = '2026-10-30T0505Z'")
R("STARTED = '2026-10-30T04:05:00Z'","STARTED = '2026-10-30T05:05:00Z'")
R("OBS_AT = '2026-10-30T04:06:00Z'","OBS_AT = '2026-10-30T05:06:00Z'")
R("READS_BEFORE = 897","READS_BEFORE = 867")
SPAN("READS_USED = 30","\n","READS_USED = 41  # 0505Z: this run's 41 X calls (watch 5, desks 19, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 867 to 826; no 429 or 503 refusals\n")
R("datetime(2026,10,30,4,6,tzinfo=timezone.utc).timestamp()  # 0405Z (","datetime(2026,10,30,5,6,tzinfo=timezone.utc).timestamp()  # 0505Z (0405Z used 04:06, ")
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',","'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
R("""    'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_redbaron': 'trend_redbaron.txt', 'trend_joshjacobs': 'trend_joshjacobs.txt', 'trend_gopackgo': 'trend_gopackgo.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_panthers': 'trend_panthers.txt', 'trend_bryceyoung': 'trend_bryceyoung.txt', 'trend_grizzlies': 'trend_grizzlies.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
SPAN("DUE = ['politics','entertainment'","\n","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 0505Z: all 19 desks, as requests/plan.json for 2026-10-30T05Z lists\n")
R("""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_redbaron','trend.Red Baron'),('trend_joshjacobs','trend.Josh Jacobs'),('trend_gopackgo','trend.#GoPackGo'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_panthers','trend.Panthers'),('trend_bryceyoung','trend.Bryce Young'),('trend_grizzlies','trend.Grizzlies'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("if _c.endswith('0405Z.json') and '/30/' in _c: continue","if _c.endswith('0505Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T0305Z'  # 0405Z: culture/sports/online last read in 0305Z","_last = '2026-10-30T0405Z'  # 0505Z: news/money/science last read in 0405Z")
R("not in requests/plan.json for 2026-10-30T04Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T05Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-30T04Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-30T05Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("CTX_REPLIES = CTXR  # 0405Z","\n","CTX_REPLIES = CTXR  # 0505Z: replies to USronaldcarter 2115739289250156765 in its first 20 minutes; relevancy returned 2, both kept\n")
R("CTX_IDS = ['2115674710381883569'] + CTX_REPLIES","CTX_IDS = ['2115739289250156765'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2115674710381883569']+CTXR+CTXQ})","DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2115674710381883569']})\nDESK_OVERRIDE_RUN.update({_x:'tech' for _x in ['2115739289250156765']+CTXR+CTXQ})  # 0505Z: USronaldcarter thread on hackers hitting banks and its context replies and quote are tech\n#")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T04Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T05Z, in its order and in batches of 100 (461 ids; its left_out counts 9 slowed flat posts and 3 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Panthers\", \"Bryce Young\" and \"Grizzlies\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the three top-ten US names with no posts attached in 0405Z; \"Panthers\" and \"Bryce Young\" are one event with \"Packers\", \"Christian Watson\", \"Josh Jacobs\", \"Jordan Love\" and \"#GoPackGo\": Panthers at Packers on Thursday Night Football; \"Grizzlies\" is Grizzlies at Blazers)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"that\" and \"just\" (0405Z used \"my\" and \"it\"), each quoted so X does not reject a bare stopword: (\"that\" lang:en is:quote -is:retweet), (\"just\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T06:00:00Z, end_time 2026-10-30T05:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets); each series is the 167 full hours 2026-10-23T06:00Z to 2026-10-30T04:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T09:35:00Z (the post\\'s creation minute) and end_time 2026-10-29T09:55:00Z: (conversation_id:2115739289250156765 is:reply) and (quotes_of_tweet_id:2115739289250156765 -is:retweet); the plan gives context.top two reads, so one post: 2115739289250156765 (@USronaldcarter thread on hackers hitting banks in 7 countries, the biggest post new this run under 24 hours old at about 1.97M views; the larger rotobot_ai Panthers-at-Packers simulation post, about 2.34M views, was left out as likely paid); 2 replies and 1 quote in the window, all kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (11:05 PM CT","f'Screen: 3 reads by id (114 unread references, then 31 second-hop). '\n",
 "            f'Day-band run (12:05 AM CT Oct 30 / 05:05 UTC Oct 30, the 05Z slot; band allowance 42): requests/plan.json is for 2026-10-30T05Z (written 04:12Z after the 0405Z capture), so it was followed (41 reads listed, screen cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 461 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 9 slowed flat posts and 3 unavailable in its left_out were not read. '\n"
 "            f'Desks: all 19 the plan lists. Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Panthers\", \"Bryce Young\" and \"Grizzlies\" (3 reads). rising.global: quote stream \"that\" and repost stream \"just\" (2 reads). context.top: USronaldcarter 2115739289250156765 (2 reads). '\n"
 "            f'Screen: cut by the plan; unread second-hop references left unread. '\n")
R("'plan': '2026-10-30T04Z',","'plan': '2026-10-30T05Z',")
R("'context': [{'post_id': '2115674710381883569',","'context': [{'post_id': '2115739289250156765',")
R("f'{REPO}/capture/2026/10/30/0405Z.json'","f'{REPO}/capture/2026/10/30/0505Z.json'")
_a="EXTRA_PRIVATE |= {'2113983193174962294'}  # 0207Z"
assert s.count(_a)==1
s=s.replace(_a,"skip_nsfw |= {'2115825619766587580'}  # 0505Z: likely paid (rotobot_ai Panthers-at-Packers simulation product post: 4,918 likes, 105 replies and 84 reposts on 2.34M views)\n"+_a)
open('build_capture.py','w').write(s)
print('ok')
