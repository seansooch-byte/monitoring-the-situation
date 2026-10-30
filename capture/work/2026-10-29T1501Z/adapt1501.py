s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1406Z.json from saved","1501Z.json from saved")
R("capture/work/2026-10-29T1406Z'","capture/work/2026-10-29T1501Z'")
R("RUN_ID = '2026-10-29T1406Z'","RUN_ID = '2026-10-29T1501Z'")
R("STARTED = '2026-10-29T14:06:00Z'","STARTED = '2026-10-29T15:01:00Z'")
R("OBS_AT = '2026-10-29T14:07:00Z'","OBS_AT = '2026-10-29T15:03:00Z'")
R("READS_BEFORE = 615","READS_BEFORE = 578")
SPAN("READS_USED = 37","\n","READS_USED = 27  # 1501Z: this run's 27 X calls (watch 5, desks 4, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of the plan's 3); the counter fell 578 to 551; no 429 or 503 refusals\n")
R("datetime(2026,10,29,14,7,tzinfo=timezone.utc).timestamp()  # 1406Z (","datetime(2026,10,29,15,3,tzinfo=timezone.utc).timestamp()  # 1501Z (1406Z used 14:07, ")
R("""    'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_jimbrown': 'trend_jimbrown.txt', 'trend_instacart': 'trend_instacart.txt', 'trend_barrysanders': 'trend_barrysanders.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_simmons': 'trend_simmons.txt', 'trend_bigjeff': 'trend_bigjeff.txt', 'trend_ryanpoles': 'trend_ryanpoles.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
SPAN("DUE = ['politics','world',","\n","DUE = ['politics','entertainment','sports','internet']  # 1501Z: the 4 desks requests/plan.json for 2026-10-29T15Z lists\n")
R("""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_jimbrown','trend.Jim Brown'),('trend_instacart','trend.Instacart'),('trend_barrysanders','trend.Barry Sanders'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_simmons','trend.Simmons'),('trend_bigjeff','trend.Big Jeff'),('trend_ryanpoles','trend.Ryan Poles'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) in ('trend.Jim Brown','trend.Barry Sanders'): return 'sports'  # 1406Z""","""        if str(_x) in ('trend.Simmons','trend.Big Jeff','trend.Ryan Poles'): return 'sports'  # 1501Z: Titans trade DT Jeffery Simmons to the Bears for two first-round picks (one event; Ryan Poles is the Bears GM)
        if str(_x) in ('trend.Jim Brown','trend.Barry Sanders'): return 'sports'  # 1406Z""")
R("if _c.endswith('1406Z.json') and '/29/' in _c: continue","if _c.endswith('1501Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-29T1259Z'  # 1406Z: culture/sports/online last read in 1259Z","_last = '2026-10-29T1406Z'  # 1501Z: news/money/science last read in 1406Z")
R("not in requests/plan.json for 2026-10-29T14Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-29T15Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T14Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T15Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['politics','sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115818348244300105']  # 1501Z: the most liked reply to AdamSchefter 2115813435543826449 in its first 20 minutes (j_macgeever, 4 likes); the other 24 have 0 to 4 likes from small accounts and are left out\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115818239641235729','2115818173815783631']  # 1501Z: the two most liked quotes in the window (SwiftyNetwork, creamsleeve); the other 23 have 2 likes or fewer\n")
R("CTX_IDS = ['2115797314434695516'] + CTX_REPLIES","CTX_IDS = ['2115813435543826449'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T14Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T15Z (contract/PLAN.md), in its order and in batches of 100 (402 ids; its left_out counts 237 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id, the unread ones read by id in 2 screen reads (94 ids, then 16 second-hop; 7 third-hop references left unread); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Simmons\", \"Big Jeff\" and \"Ryan Poles\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the top three US names with no posts attached in 1406Z; all three are one event: the Titans trading All-Pro DT Jeffery Simmons to the Bears for two first-round picks, Ryan Poles being the Bears general manager)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"is\" and \"you\" (1406Z used \"the\" and \"this\"), each quoted so X does not reject a bare stopword: (\"is\" lang:en is:quote -is:retweet), (\"you\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T16:00:00Z, end_time 2026-10-29T15:00:00Z, one read per desk for the 4 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster); each series is the 167 full hours 2026-10-22T16:00Z to 2026-10-29T14:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T14:30:00Z (the post\\'s creation minute) and end_time 2026-10-29T14:50:00Z: (conversation_id:2115813435543826449 is:reply) and (quotes_of_tweet_id:2115813435543826449 -is:retweet); the plan gives context.top two reads, so one post: 2115813435543826449 (@AdamSchefter with the full Simmons trade terms, the biggest fresh post new this run at about 1.57M views in 35 minutes); 25 replies and 25 quotes in the window, the most liked reply and 2 most liked quotes kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (9:06 AM CT","Screen: 2 reads by id (155 unread references). '\n",
 "            f'Day-band run (10:01 AM CT Oct 29 / 15:01 UTC Oct 29, the 15Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-29T15Z, written 14:13Z; 25 reads listed plus up to 3 screen reads) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 402 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 237 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 not due per the plan). Volume: world, defense, justice and disaster (4 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Simmons\", \"Big Jeff\" and \"Ryan Poles\" (3 reads; one event, the Jeffery Simmons trade to the Bears). rising.global: quote stream \"is\" and repost stream \"you\" (2 reads). context.top: AdamSchefter 2115813435543826449 (2 reads). Screen: 2 reads by id (94 unread references, then 16 second-hop). '\n")
R("'plan': '2026-10-29T14Z',","'plan': '2026-10-29T15Z',")
R("    'context': [{'post_id': '2115797314434695516',","    'context': [{'post_id': '2115813435543826449',")
R("capture/2026/10/29/1406Z.json'","capture/2026/10/29/1501Z.json'")
open('build_capture.py','w').write(s); print('ok')
