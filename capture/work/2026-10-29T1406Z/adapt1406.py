s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1259Z.json from saved","1406Z.json from saved")
R("capture/work/2026-10-29T1259Z'","capture/work/2026-10-29T1406Z'")
R("RUN_ID = '2026-10-29T1259Z'","RUN_ID = '2026-10-29T1406Z'")
R("STARTED = '2026-10-29T12:59:00Z'","STARTED = '2026-10-29T14:06:00Z'")
R("OBS_AT = '2026-10-29T13:01:00Z'","OBS_AT = '2026-10-29T14:07:00Z'")
R("READS_BEFORE = 645","READS_BEFORE = 615")
SPAN("READS_USED = 30","\n","READS_USED = 37  # 1406Z: this run's 37 X calls (watch 5, desks 13, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of the plan's 3); the counter fell 615 to 578; no 429 or 503 refusals\n")
R("datetime(2026,10,29,13,1,tzinfo=timezone.utc).timestamp()  # 1259Z (","datetime(2026,10,29,14,7,tzinfo=timezone.utc).timestamp()  # 1406Z (1259Z used 13:01, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_corepce': 'trend_corepce.txt', 'trend_q3gdp': 'trend_q3gdp.txt', 'trend_hyperliquid': 'trend_hyperliquid.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch4': 'watch4.txt',
    'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_jimbrown': 'trend_jimbrown.txt', 'trend_instacart': 'trend_instacart.txt', 'trend_barrysanders': 'trend_barrysanders.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
SPAN("DUE = ['politics','entertainment',","\n","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1406Z: the 13 desks requests/plan.json for 2026-10-29T14Z lists\n")
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_corepce','trend.Core PCE'),('trend_q3gdp','trend.Q3 GDP'),('trend_hyperliquid','trend.Hyperliquid'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_jimbrown','trend.Jim Brown'),('trend_instacart','trend.Instacart'),('trend_barrysanders','trend.Barry Sanders'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) in ('trend.Core PCE','trend.Q3 GDP'): return 'markets'  # 1259Z""","""        if str(_x) in ('trend.Jim Brown','trend.Barry Sanders'): return 'sports'  # 1406Z: greatest-running-back debate (Jim Brown vs Barry Sanders; one event)
        if str(_x) == 'trend.Instacart': return 'business'  # 1406Z: DoorDash agrees to buy Instacart for about $17 billion
        if str(_x) in ('trend.Core PCE','trend.Q3 GDP'): return 'markets'  # 1259Z""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
R("if _c.endswith('1259Z.json') and '/29/' in _c: continue","if _c.endswith('1406Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T1206Z'  # 1259Z: news/money/science last read in 1206Z","_last = '2026-10-29T1259Z'  # 1406Z: culture/sports/online last read in 1259Z")
R("not in requests/plan.json for 2026-10-29T13Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-29T14Z (rotation: news/money/science this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T13Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T14Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['politics','sports','internet','life','offbeat']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115802311997931713']  # 1406Z: the most liked reply to Cristiano 2115797314434695516 in its first 20 minutes (ModricBdr, 11 likes); the other 24 have 0 to 8 likes from small accounts and are left out\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115802269329375574','2115802315378528356']  # 1406Z: the two most liked quotes in the window (JELHAZARD_01, fcb_lisco); the other 23 have under 10 likes from small accounts\n")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T13Z","6 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T14Z (contract/PLAN.md), in its order and in batches of 100 (401 ids; its left_out counts 227 slowed flat posts and 5 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id, the unread ones read by id in 2 screen reads (155 ids); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Jim Brown\", \"Instacart\" and \"Barry Sanders\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; \"Jim Brown\" and \"Instacart\" are the top-ten US names not attached in the last runs, and \"Barry Sanders\" is the next name down; \"Good Thursday\", \"#NationalCatDay\", \"Happy Friday Eve\", \"#AlconEntLongForCowdung\" and \"#thursdayvibes\" were attached in 1009Z to 1206Z, \"Core PCE\" and \"Q3 GDP\" in 1259Z, and the Chinese-language hashtag \"#叠纸破坏中国两岸文化往来\" is skipped; \"Jim Brown\" and \"Barry Sanders\" are one event, a greatest-running-back debate; \"Instacart\" is DoorDash agreeing to buy Instacart for about $17 billion)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (1259Z used \"just\" and \"what\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T15:00:00Z, end_time 2026-10-29T14:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.sports, volume.internet, volume.life, volume.offbeat); each series is the 167 full hours 2026-10-22T15:00Z to 2026-10-29T13:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T13:26:00Z (the post\\'s creation, 13:26:04) and end_time 2026-10-29T13:46:00Z: (conversation_id:2115797314434695516 is:reply) and (quotes_of_tweet_id:2115797314434695516 -is:retweet); the plan gives context.top two reads, so one post: 2115797314434695516 (@Cristiano thanking fans for a \"Ballon D\\'Or of All Time\", the biggest fresh post new this run at about 1.03M views in 40 minutes); 25 replies and 25 quotes in the window, the most liked reply and 2 most liked quotes kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (7:59 AM CT","Screen: 2 reads by id (108 unread references). '\n",
 "            f'Day-band run (9:06 AM CT Oct 29 / 14:06 UTC Oct 29, the 14Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-29T14Z, written 13:07Z; 35 reads listed plus up to 3 screen reads) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 401 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 227 slowed flat posts and the 5 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (13 reads; the other 6 not due per the plan). Volume: politics, sports, internet, life and offbeat (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Jim Brown\", \"Instacart\" and \"Barry Sanders\" (3 reads). rising.global: quote stream \"the\" and repost stream \"this\" (2 reads). context.top: Cristiano 2115797314434695516 (2 reads). Screen: 2 reads by id (155 unread references). '\n")
R("'plan': '2026-10-29T13Z',","'plan': '2026-10-29T14Z',")
R("    'context': [{'post_id': '2115755854125478285',","    'context': [{'post_id': '2115797314434695516',")
R("capture/2026/10/29/1259Z.json'","capture/2026/10/29/1406Z.json'")
open('build_capture.py','w').write(s); print('ok')
