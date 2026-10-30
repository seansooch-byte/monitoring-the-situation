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
R('"""Build capture/2026/10/30/1209Z.json from saved','"""Build capture/2026/10/30/1305Z.json from saved')
R("capture/work/2026-10-30T1209Z'","capture/work/2026-10-30T1305Z'")
R("RUN_ID = '2026-10-30T1209Z'","RUN_ID = '2026-10-30T1305Z'")
R("STARTED = '2026-10-30T12:09:00Z'","STARTED = '2026-10-30T13:05:00Z'")
R("OBS_AT = '2026-10-30T12:10:00Z'","OBS_AT = '2026-10-30T13:06:00Z'")
R("READS_BEFORE = 696","READS_BEFORE = 654")
L("READS_USED = 42","READS_USED = 28  # 1305Z: this run's 28 X calls (watch 5, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of its 3); the counter fell 654 to 626; no 429 or 503 refusals")
R("datetime(2026,10,30,12,10,tzinfo=timezone.utc).timestamp()  # 1209Z (1106Z used 11:07, ","datetime(2026,10,30,13,6,tzinfo=timezone.utc).timestamp()  # 1305Z (1209Z used 12:10, 1106Z used 11:07, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',\n    'quote_what': 'quote_what.txt',\n    'repost_the': 'repost_the.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',\n    'quote_this': 'quote_this.txt',\n    'repost_is': 'repost_is.txt',\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
R("    'trend_halloweeneve': 'trend_halloweeneve.txt', 'trend_papergames': 'trend_papergames.txt', 'trend_alconent': 'trend_alconent.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_redfriday': 'trend_redfriday.txt', 'trend_cartesia': 'trend_cartesia.txt', 'trend_fridayvibes': 'trend_fridayvibes.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world',","DUE = ['politics','entertainment','sports','internet']  # 1305Z: the four hourly desks requests/plan.json for 2026-10-30T13Z lists")
R("""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_halloweeneve','trend.Happy Halloween Eve'),('trend_papergames','trend.#PapergamesRuinsCNCredibility'),('trend_alconent','trend.#AlconEntHasNoDignity'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_this','quote'),('repost_is','repost'),
    ('trend_redfriday','trend.RED Friday'),('trend_cartesia','trend.Cartesia Managed Agents'),('trend_fridayvibes','trend.#FridayVibes'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x) in ('trend.#PapergamesRuinsCNCredibility','trend.#AlconEntHasNoDignity'): return 'gaming'  # 1209Z: one fan campaign against Papergames (Infold) and Alcon Entertainment\n",
  "        if str(_x) in ('trend.#PapergamesRuinsCNCredibility','trend.#AlconEntHasNoDignity'): return 'gaming'  # 1209Z: one fan campaign against Papergames (Infold) and Alcon Entertainment\n        if str(_x) == 'trend.Cartesia Managed Agents': return 'ai'  # 1305Z: Cartesia launches Managed Agents (voice AI agents)\n")
R("CTX_REPLIES = CTXR  # 1209Z: replies to cz_binance 2116097554882728341 in its first 20 minutes; relevancy returned none (the post is itself a reply to elonmusk, so its conversation_id is Elon's post)",
  "CTX_REPLIES = CTXR  # 1305Z: replies to nayibbukele 2115915319134855447 in its first 20 minutes, the three most liked kept")
R("CTX_IDS = ['2116097554882728341'] + CTX_REPLIES + CTX_QUOTES","CTX_IDS = ['2115915319134855447'] + CTX_REPLIES + CTX_QUOTES")
R("take(((metrics(_p)['views'] or 0), _i, 'markets', 'context',","take(((metrics(_p)['views'] or 0), _i, 'world', 'context',")
R("DESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2116097554882728341']+CTXR+CTXQ})","DESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2116097554882728341']})\nDESK_OVERRIDE_RUN.update({_x:'world' for _x in ['2115915319134855447']+CTXR+CTXQ})  # 1305Z: Bukele post on El Salvador soldiers going to Haiti and its context replies and quotes are world")
R("EXTRA_PRIVATE |= {'2115674710381883569'} | set(CTXR) | set(CTXQ)  # 0405Z","EXTRA_PRIVATE |= {'2115674710381883569'}  # 1305Z: the 0405Z context sets are not re-applied here (this run's context is a different post; 0405Z flags persist through private_ids.txt); 0405Z")
R("if _c.endswith('1209Z.json') and '/30/' in _c: continue","if _c.endswith('1305Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T1106Z'  # 1209Z: culture/sports/online last read in 1106Z","_last = '2026-10-30T1209Z'  # 1305Z: news/money/science last read in 1209Z")
R("not in requests/plan.json for 2026-10-30T12Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T13Z (rotation: culture/sports/online this run)")
R("reason = 'not read: requests/plan.json for 2026-10-30T12Z cut it'","reason = 'not read: not due in requests/plan.json for 2026-10-30T13Z (desks_not_due)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T12Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T13Z, in its order and in batches of 100 (480 ids; the plan\\'s note: \"47 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 15 flat posts wait for their sixth run\"; its left_out counts 15 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 2 reads by id of the plan\\'s 3, 100 unread references then 21 second-hop; nothing left to read); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"RED Friday\", \"Cartesia Managed Agents\" and \"#FridayVibes\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1209Z; \"#KEONHOxCHANELCoconeige\", a fan campaign, was not read)',\n")
SPAN("sweeps.append(sweep('rising.global'","\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"this\" and \"is\" (1209Z used \"what\" and \"the\"), each quoted so X does not reject a bare stopword: (\"this\" lang:en is:quote -is:retweet), (\"is\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T14:00:00Z, end_time 2026-10-30T13:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-23T14:00Z to 2026-10-30T12:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T21:14:00Z (the post\\'s creation minute) and end_time 2026-10-29T21:34:00Z: (conversation_id:2115915319134855447 is:reply) and (quotes_of_tweet_id:2115915319134855447 -is:retweet); the plan gives context.top two reads, so one post: 2115915319134855447 (@nayibbukele post in Haitian Creole on El Salvador sending soldiers to Haiti, the biggest post new this run under 24 hours old at about 5.65M views); 25 replies and 25 quotes, the three most liked of each kept',None,'ok',None,")
SPAN("            f'Day-band run (7:09 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (8:05 AM CT Oct 30 / 13:05 UTC Oct 30, the 13Z slot; band allowance 42): requests/plan.json is for 2026-10-30T13Z (written 12:19Z after the 1209Z capture), so it was followed (29 reads listed) top to bottom; screen needed 2 of its 3 reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 480 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 15 slowed flat posts and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four the plan lists; the other 15 not due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "RED Friday", "Cartesia Managed Agents" and "#FridayVibes" (3 reads). rising.global: quote stream "this" and repost stream "is" (2 reads). context.top: nayibbukele 2115915319134855447 (2 reads). '
            f'Screen: 2 reads by id (100 unread references, then 21 second-hop). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T12Z',","'plan': '2026-10-30T13Z',")
R("    'context': [{'post_id': '2116097554882728341',","    'context': [{'post_id': '2115915319134855447',")
R("f'{REPO}/capture/2026/10/30/1209Z.json'","f'{REPO}/capture/2026/10/30/1305Z.json'")
open('build_capture.py','w').write(s)
print('ok')
