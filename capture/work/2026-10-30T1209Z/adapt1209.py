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
R('"""Build capture/2026/10/30/1106Z.json from saved','"""Build capture/2026/10/30/1209Z.json from saved')
R("capture/work/2026-10-30T1106Z'","capture/work/2026-10-30T1209Z'")
R("RUN_ID = '2026-10-30T1106Z'","RUN_ID = '2026-10-30T1209Z'")
R("STARTED = '2026-10-30T11:06:00Z'","STARTED = '2026-10-30T12:09:00Z'")
R("OBS_AT = '2026-10-30T11:07:00Z'","OBS_AT = '2026-10-30T12:10:00Z'")
R("READS_BEFORE = 716","READS_BEFORE = 696")
L("READS_USED = 20","READS_USED = 42  # 1209Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 696 to 654; no 429 or 503 refusals")
R("datetime(2026,10,30,11,7,tzinfo=timezone.utc).timestamp()  # 1106Z (1004Z used 10:05, ","datetime(2026,10,30,12,10,tzinfo=timezone.utc).timestamp()  # 1209Z (1106Z used 11:07, 1004Z used 10:05, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',\n    'quote_what': 'quote_what.txt',\n    'repost_the': 'repost_the.txt',\n    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',\n")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
R("    'trend_goodfriday': 'trend_goodfriday.txt', 'trend_happyfriyay': 'trend_happyfriyay.txt', 'trend_binance': 'trend_binance.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_halloweeneve': 'trend_halloweeneve.txt', 'trend_papergames': 'trend_papergames.txt', 'trend_alconent': 'trend_alconent.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 1209Z: all 19 desks, as requests/plan.json for 2026-10-30T12Z lists")
R("""    ('trend_goodfriday','trend.Good Friday'),('trend_happyfriyay','trend.Happy Friyay'),('trend_binance','trend.Binance'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_halloweeneve','trend.Happy Halloween Eve'),('trend_papergames','trend.#PapergamesRuinsCNCredibility'),('trend_alconent','trend.#AlconEntHasNoDignity'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x) in ('trend.Good Friday','trend.Happy Friyay'): return 'life'  # 1106Z: Friday morning greeting posts\n",
  "        if str(_x) in ('trend.Good Friday','trend.Happy Friyay'): return 'life'  # 1106Z: Friday morning greeting posts\n        if str(_x) in ('trend.#PapergamesRuinsCNCredibility','trend.#AlconEntHasNoDignity'): return 'gaming'  # 1209Z: one fan campaign against Papergames (Infold) and Alcon Entertainment\n")
R("CTXR = []; CTXQ = []  # 0604Z: context.top cut by the plan\nCTX_REPLIES = []\nCTX_QUOTES = []\nCTX_IDS = []",
  "CTXR = _top3('context_replies.txt'); CTXQ = _top3('context_quotes.txt')\nCTX_REPLIES = CTXR  # 1209Z: replies to cz_binance 2116097554882728341 in its first 20 minutes; relevancy returned none (the post is itself a reply to elonmusk, so its conversation_id is Elon's post)\nCTX_QUOTES = CTXQ  # 0109Z: quotes in the window, the three most liked kept\nCTX_IDS = ['2116097554882728341'] + CTX_REPLIES + CTX_QUOTES")
R("take(((metrics(_p)['views'] or 0), _i, 'tech', 'context',","take(((metrics(_p)['views'] or 0), _i, 'markets', 'context',")
R("DESK_OVERRIDE_RUN.update({_x:'tech' for _x in ['2115739289250156765']+CTXR+CTXQ})","DESK_OVERRIDE_RUN.update({_x:'tech' for _x in ['2115739289250156765']})\nDESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2116097554882728341']+CTXR+CTXQ})  # 1209Z: cz_binance reply to Elon on the Binance hack and its context quotes are markets, as the other Binance posts")
R("if _c.endswith('1106Z.json') and '/30/' in _c: continue","if _c.endswith('1209Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T1004Z'  # 1106Z: news/money/science last read in 1004Z","_last = '2026-10-30T1106Z'  # 1209Z: culture/sports/online last read in 1106Z")
R("not in requests/plan.json for 2026-10-30T11Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T12Z (rotation: news/money/science this run)")
R("reason = 'not read: requests/plan.json for 2026-10-30T11Z cut it (overnight band, allowance 20)'","reason = 'not read: requests/plan.json for 2026-10-30T12Z cut it'")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T11Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T12Z, in its order and in batches of 100 (624 ids; the plan\\'s note: \"48 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 90 flat posts wait for their sixth run\"; its left_out counts 90 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Happy Halloween Eve\", \"#PapergamesRuinsCNCredibility\" and \"#AlconEntHasNoDignity\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1106Z; \"#PapergamesRuinsCNCredibility\" and \"#AlconEntHasNoDignity\" are one fan campaign with \"#上海纵容叠纸破坏两岸交流\" against Papergames (Infold) and Alcon Entertainment (16 and 25 reposts, all of low-view origins); the Orm Kornnaphat/Leapmotor B03X names are one Thai fan campaign and #KEONHOxCHANELCoconeige a K-pop fan campaign, not read); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"what\" and \"the\" (0505Z, the last run that read them, used \"that\" and \"just\"), each quoted so X does not reject a bare stopword: (\"what\" lang:en is:quote -is:retweet), (\"the\" lang:en is:retweet), newest first, 25 each',\n    6,'ok',None, rising_ids[:30]))\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T13:00:00Z, end_time 2026-10-30T12:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-23T13:00Z to 2026-10-30T11:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T09:19:00Z (the post\\'s creation minute) and end_time 2026-10-30T09:39:00Z: (conversation_id:2116097554882728341 is:reply) and (quotes_of_tweet_id:2116097554882728341 -is:retweet); the plan gives context.top two reads, so one post: 2116097554882728341 (@cz_binance reply asking Elon Musk to stop trolling during the Binance hack, the biggest post new this run under 24 hours old at about 1.98M views); no replies in the window (the post is itself a reply, so the conversation is Elon\\'s), 25 quotes, the three most liked kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Overnight-band run (6:06 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (7:09 AM CT Oct 30 / 12:09 UTC Oct 30, the 12Z slot; band allowance 42): requests/plan.json is for 2026-10-30T12Z (written 11:12Z after the 1106Z capture), so it was followed (42 reads listed, screen cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 624 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 90 slowed flat posts and 2 unavailable in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Happy Halloween Eve", "#PapergamesRuinsCNCredibility" and "#AlconEntHasNoDignity" (3 reads; the last two are one fan campaign). rising.global: quote stream "what" and repost stream "the" (2 reads). context.top: cz_binance 2116097554882728341 (2 reads). '
            f'Screen: cut by the plan; unread second-hop references left unread. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T11Z',","'plan': '2026-10-30T12Z',")
R("    'context': [],","    'context': [{'post_id': '2116097554882728341', 'replies': [i for i in CTX_REPLIES if i in posts_by_sel], 'quotes': [i for i in CTX_QUOTES if i in posts_by_sel]}],")
R("f'{REPO}/capture/2026/10/30/1106Z.json'","f'{REPO}/capture/2026/10/30/1209Z.json'")
open('build_capture.py','w').write(s)
print('ok')
