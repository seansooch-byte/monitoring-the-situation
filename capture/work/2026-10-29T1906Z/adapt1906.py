s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1802Z.json from saved","1906Z.json from saved")
R("capture/work/2026-10-29T1802Z'","capture/work/2026-10-29T1906Z'")
R("RUN_ID = '2026-10-29T1802Z'","RUN_ID = '2026-10-29T1906Z'")
R("STARTED = '2026-10-29T18:02:00Z'","STARTED = '2026-10-29T19:06:00Z'")
R("OBS_AT = '2026-10-29T18:03:00Z'","OBS_AT = '2026-10-29T19:07:00Z'")
R("READS_BEFORE = 478","READS_BEFORE = 441")
SPAN("READS_USED = 37","\n","READS_USED = 26  # 1906Z: this run's 26 X calls (watch 4, desks 4, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of the plan's 3); the counter fell 441 to 415; no 429 or 503 refusals\n")
R("datetime(2026,10,29,18,3,tzinfo=timezone.utc).timestamp()  # 1802Z (","datetime(2026,10,29,19,7,tzinfo=timezone.utc).timestamp()  # 1906Z (1802Z used 18:03, ")
R("""    'watch4': 'watch4.txt',
    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_wnbafinals': 'trend_wnbafinals.txt', 'trend_larkin': 'trend_larkin.txt', 'trend_burton': 'trend_burton.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_game7': 'trend_game7.txt', 'trend_24weeks': 'trend_24weeks.txt', 'trend_allishagray': 'trend_allishagray.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
SPAN("DUE = ['politics','world'","\n","DUE = ['politics','entertainment','sports','internet']  # 1906Z: the 4 desks the plan for 2026-10-29T19Z lists\n")
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_wnbafinals','trend.#WNBAFinals'),('trend_larkin','trend.Larkin'),('trend_burton','trend.Burton'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_game7','trend.Game 7'),('trend_24weeks','trend.2-4 WEEKS'),('trend_allishagray','trend.Allisha Gray'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) in ('trend.#WNBAFinals','trend.Larkin','trend.Burton'): return 'sports'  # 1802Z""","""        if str(_x) in ('trend.Game 7','trend.Allisha Gray'): return 'sports'  # 1906Z: the Dream beat the Valkyries in WNBA Finals Game 6 to force the first Game 7
        if str(_x) in ('trend.2-4 WEEKS',): return 'internet'  # 1906Z: AO3 says the site will be down for 2 to 4 weeks
        if str(_x) in ('trend.#WNBAFinals','trend.Larkin','trend.Burton'): return 'sports'  # 1802Z""")
R("('watch0','watch1','watch2','watch3','watch4')","('watch0','watch1','watch2','watch3')",2)
R("if _c.endswith('1802Z.json') and '/29/' in _c: continue","if _c.endswith('1906Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-29T1707Z'  # 1802Z: culture/sports/online last read in 1707Z","_last = '2026-10-29T1802Z'  # 1906Z: news/money/science last read in 1802Z")
R("not in requests/plan.json for 2026-10-29T18Z (rotation: news/money/science this run)","not in the plan for 2026-10-29T19Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T18Z (listed in its left_out.desks_not_due)'","reason = 'not due in the plan for 2026-10-29T19Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['politics','sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115869728409334267','2115869709115548010','2115869723208405299']  # 1906Z: the three most liked replies to AO3_Status 2115864946093305955 in its first 20 minutes (hansfairytale, alextherobot456, gemsomnia); the rest have 1 like or none\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115869773787508838','2115869772290326919','2115869770822144235']  # 1906Z: the most liked quotes in the window (sxlendipity, shqnhes, bright_fangs); lewdocel (9 likes) passed over for its handle; the rest have 2 likes or fewer\n")
R("CTX_IDS = ['2115793711032676693'] + CTX_REPLIES","CTX_IDS = ['2115864946093305955'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T18Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of the plan for 2026-10-29T19Z (node tools/plan-reads.mjs --at 2026-10-29T18:59:00Z --print, contract/PLAN.md; the committed requests/plan.json was still for 18Z), in its order and in batches of 100 (396 ids; its left_out counts 243 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Game 7\", \"2-4 WEEKS\" and \"Allisha Gray\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1802Z, skipping \"Simmons\", \"Bears\", \"Titans\" and \"#NationalCatDay\" as read in 1501Z to 1707Z and \"#WNBAFinals\" and \"Larkin\" as read in 1802Z; \"Game 7\" and \"Allisha Gray\" are one event, the Atlanta Dream beat the Valkyries 80-69 in Game 6 to force the first Game 7 in WNBA Finals history, the same event as \"Dream in 7\", \"Valkyries\" and \"#WNBAFinals\"; \"2-4 WEEKS\" is AO3 saying the site will be down for two to four weeks); screen: 2 reads by id (76 unread references, then 10 second-hop; 3 third-hop references left unread)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (1802Z used \"just\" and \"what\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T20:00:00Z, end_time 2026-10-29T19:00:00Z, one read per desk for the 4 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster); each series is the 167 full hours 2026-10-22T20:00Z to 2026-10-29T18:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T17:54:00Z (the post\\'s creation minute) and end_time 2026-10-29T18:14:00Z: (conversation_id:2115864946093305955 is:reply) and (quotes_of_tweet_id:2115864946093305955 -is:retweet); the plan gives context.top two reads, so one post: 2115864946093305955 (@AO3_Status saying restoration will take about 2 weeks and up to 4, the biggest fresh post new this run at about 4.9M views in about 1.2 hours); 25 replies and 25 quotes in the window, the 3 most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (1:02 PM CT","no second-hop left, so the plan\\'s third screen read was not used). '\n",
 "            f'Day-band run (2:06 PM CT Oct 29 / 19:06 UTC Oct 29, the 19Z slot; band allowance 42): the committed requests/plan.json was still for 2026-10-29T18Z (already run by 1802Z), so per contract/PLAN.md the plan for this hour was made with node tools/plan-reads.mjs --at 2026-10-29T18:59:00Z --print (for_run 2026-10-29T19Z; 27 reads listed, nothing cut) and followed top to bottom; requests/plan.json not changed; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 396 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 243 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, entertainment, sports and internet (4 reads). Volume: world, defense, justice and disaster (4 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Game 7\", \"2-4 WEEKS\" and \"Allisha Gray\" (3 reads). rising.global: quote stream \"the\" and repost stream \"this\" (2 reads). context.top: AO3_Status 2115864946093305955 (2 reads). '\n"
 "            f'Screen: 2 reads by id (76 unread references, then 10 second-hop; the plan\\'s third screen read was not used). '\n")
R("'plan': '2026-10-29T18Z',","'plan': '2026-10-29T19Z',")
R("    'context': [{'post_id': '2115793711032676693',","    'context': [{'post_id': '2115864946093305955',")
R("capture/2026/10/29/1802Z.json'","capture/2026/10/29/1906Z.json'")
anchor="TREND_OFF.setdefault('Burton'"
i=s.index(anchor); j=s.index("\n",i)+1
add=("DESK_OVERRIDE_RUN.update({'2115864946093305955':'internet','2115869728409334267':'internet','2115869709115548010':'internet','2115869723208405299':'internet','2115869773787508838':'internet','2115869772290326919':'internet','2115869770822144235':'internet'})  # 1906Z: AO3_Status outage post and its context replies and quotes are internet\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s); print('ok')
