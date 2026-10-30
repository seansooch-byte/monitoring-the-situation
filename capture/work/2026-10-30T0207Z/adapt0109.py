s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/29/2203Z.json from saved','"""Build capture/2026/10/30/0109Z.json from saved')
R("capture/work/2026-10-29T2203Z'","capture/work/2026-10-30T0109Z'")
R("RUN_ID = '2026-10-29T2203Z'","RUN_ID = '2026-10-30T0109Z'")
R("STARTED = '2026-10-29T22:03:00Z'","STARTED = '2026-10-30T01:09:00Z'")
R("OBS_AT = '2026-10-29T22:04:00Z'","OBS_AT = '2026-10-30T01:10:00Z'")
R("READS_BEFORE = 344","READS_BEFORE = 1000")
SPAN("READS_USED = 37","\n","READS_USED = 40  # 0109Z: this run's 40 X calls (watch 4, desks 19, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 1000 to 960 (new UTC day); no 429 or 503 refusals\n")
R("datetime(2026,10,29,22,4,tzinfo=timezone.utc).timestamp()  # 2203Z (","datetime(2026,10,30,1,10,tzinfo=timezone.utc).timestamp()  # 0109Z (2203Z used 22:04, ")
R("""    'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_binance': 'trend_binance.txt', 'trend_startrek': 'trend_startrek.txt', 'trend_larkin': 'trend_larkin.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_treysmack': 'trend_treysmack.txt', 'trend_redbaron': 'trend_redbaron.txt', 'trend_911onabc': 'trend_911onabc.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
SPAN("DUE = ['politics','world'","\n","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 0109Z: all 19 desks, as the plan for 2026-10-30T01Z lists\n")
R("""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_binance','trend.Binance'),('trend_startrek','trend.Star Trek'),('trend_larkin','trend.Larkin'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_treysmack','trend.Trey Smack'),('trend_redbaron','trend.Red Baron'),('trend_911onabc','trend.#911onABC'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) in ('trend.Binance','trend.SAFU'): return 'markets'  # 2203Z""","""        if str(_x) in ('trend.Trey Smack','trend.Panthers','trend.#GoPackGo','trend.#Packers','trend.Christian Watson','trend.Nick Scott','trend.Lambeau','trend.#KeepPounding','trend.Tucker Kraft','trend.Chuba Hubbard','trend.Josh Jacobs','trend.Packers'): return 'sports'  # 0109Z: Panthers at Packers, Thursday Night Football (Packers rookie kicker Trey Smack's misses)
        if str(_x) == 'trend.Red Baron': return 'internet'  # 0109Z: fundraiser for the Red Baron worker harassed by an influencer
        if str(_x) == 'trend.#911onABC': return 'entertainment'  # 0109Z: 9-1-1 on ABC episode live-tweeting
        if str(_x) in ('trend.Binance','trend.SAFU'): return 'markets'  # 2203Z""")
R("if _c.endswith('2203Z.json') and '/29/' in _c: continue","if _c.endswith('0109Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-29T2109Z'  # 2203Z: culture/sports/online last read in 2109Z","_last = '2026-10-29T2203Z'  # 0109Z: news/money/science last read in 2203Z")
R("not in requests/plan.json for 2026-10-29T22Z (rotation: news/money/science this run)","not in the plan for 2026-10-30T01Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T22Z (listed in its left_out.desks_not_due)'","reason = 'not due in the plan for 2026-10-30T01Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['politics','sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = CTXR  # 0109Z: replies to MarvelStudios 2115896865803870592 in its first 20 minutes; relevancy returned 25, the three most liked kept\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = CTXQ  # 0109Z: quotes in the window, the three most liked kept\n")
R("CTX_IDS = ['2115915423174853077'] + CTX_REPLIES","CTX_IDS = ['2115896865803870592'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T22Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of the plan for 2026-10-30T01Z (printed by tools/plan-reads.mjs --at 2026-10-30T00:59:00Z; requests/plan.json still holds the 23Z plan and was not changed), in its order and in batches of 100 (317 ids; its left_out counts 14 slowed flat posts and 1 unavailable post not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Trey Smack\", \"Red Baron\" and \"#911onABC\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 2203Z; \"Trey Smack\" is the same event as \"Panthers\", \"#GoPackGo\" and \"#Packers\" (Panthers at Packers on Thursday Night Football) and \"Picard\" the same as \"Patrick Stewart\" and \"Star Trek\" (attached in 2203Z); skipping \"Patrick Stewart\", \"Binance\" and \"Star Trek\" (attached in 2203Z))',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"what\" and \"the\" (2203Z used \"that\" and \"just\"), each quoted so X does not reject a bare stopword: (\"what\" lang:en is:quote -is:retweet), (\"the\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T02:00:00Z, end_time 2026-10-30T01:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets); each series is the 167 full hours 2026-10-23T02:00Z to 2026-10-30T00:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T20:01:00Z (the post\\'s creation minute) and end_time 2026-10-29T20:21:00Z: (conversation_id:2115896865803870592 is:reply) and (quotes_of_tweet_id:2115896865803870592 -is:retweet); the plan gives context.top two reads, so one post: 2115896865803870592 (@MarvelStudios on the death of Sir Patrick Stewart, the biggest post new this run at about 5.45M views); 25 replies and 25 quotes in the window, the 3 most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (5:03 PM CT","f'Screen: 3 reads by id (141 unread references in two reads, then 21 second-hop). '\n",
 "            f'Day-band run (8:09 PM CT Oct 29 / 01:09 UTC Oct 30, the 01Z slot; band allowance 42): the 23Z and 00Z runs did not happen (last capture 2026-10-29T2203Z), so requests/plan.json still held the plan for 2026-10-29T23Z; as contract/PLAN.md says, the plan for 2026-10-30T01Z was printed with node tools/plan-reads.mjs --at 2026-10-30T00:59:00Z --print and followed (40 reads, screen cut) top to bottom; requests/plan.json was not changed. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today, new UTC day), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 317 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 14 slowed flat posts and the 1 standing unavailable post are in its left_out and were not read. '\n"
 "            f'Desks: all 19 the plan lists. Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Trey Smack\", \"Red Baron\" and \"#911onABC\" (3 reads: Packers rookie kicker Trey Smack\\'s misses against the Panthers, the fundraiser for the Red Baron worker, and the 9-1-1 episode). rising.global: quote stream \"what\" and repost stream \"the\" (2 reads). context.top: MarvelStudios 2115896865803870592 (2 reads). '\n"
 "            f'Screen: cut by the plan; unread second-hop references left unread. '\n")
R("'plan': '2026-10-29T22Z',","'plan': '2026-10-30T01Z',")
R("    'context': [{'post_id': '2115915423174853077',","    'context': [{'post_id': '2115896865803870592',")
R("capture/2026/10/29/2203Z.json'","capture/2026/10/30/0109Z.json'")
# context ids computed from files
i=s.index("CTX_REPLIES = CTXR")
s=s[:i]+"""def _top3(fn):
    _j = load_raw(fn)
    _d = [t for t in (_j.get('data') or [])]
    _d.sort(key=lambda t: -t['public_metrics']['like_count'])
    return [t['id'] for t in _d[:3]]
CTXR = _top3('context_replies.txt'); CTXQ = _top3('context_quotes.txt')
"""+s[i:]
anchor="DESK_OVERRIDE_RUN.update({'2115922259739349132':'markets'"
i=s.index(anchor); j=s.index("\n",i)+1
s=s[:j]+"DESK_OVERRIDE_RUN.update({_x:'entertainment' for _x in ['2115896865803870592']+CTXR+CTXQ})  # 0109Z: MarvelStudios Patrick Stewart post and its context replies and quotes are entertainment\n"+s[j:]
open('build_capture.py','w').write(s); print('ok')
