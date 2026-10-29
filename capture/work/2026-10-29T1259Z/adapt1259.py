s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1206Z.json from saved","1259Z.json from saved")
R("capture/work/2026-10-29T1206Z'","capture/work/2026-10-29T1259Z'")
R("RUN_ID = '2026-10-29T1206Z'","RUN_ID = '2026-10-29T1259Z'")
R("STARTED = '2026-10-29T12:06:00Z'","STARTED = '2026-10-29T12:59:00Z'")
R("OBS_AT = '2026-10-29T12:08:00Z'","OBS_AT = '2026-10-29T13:01:00Z'")
R("READS_BEFORE = 687","READS_BEFORE = 645")
SPAN("READS_USED = 42","\n","READS_USED = 30  # 1259Z: this run's 30 X calls (watch 6, desks 5, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of the plan's 3); the counter fell 645 to 615; no 429 or 503 refusals\n")
R("datetime(2026,10,29,12,8,tzinfo=timezone.utc).timestamp()  # 1206Z (","datetime(2026,10,29,13,1,tzinfo=timezone.utc).timestamp()  # 1259Z (1206Z used 12:08, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_alconent': 'trend_alconent.txt', 'trend_thursdayvibes': 'trend_thursdayvibes.txt', 'trend_thankfulthursday': 'trend_thankfulthursday.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_corepce': 'trend_corepce.txt', 'trend_q3gdp': 'trend_q3gdp.txt', 'trend_hyperliquid': 'trend_hyperliquid.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
SPAN("DUE = ['politics','world',","\n","DUE = ['politics','entertainment','sports','internet','life']  # 1259Z: the 5 desks requests/plan.json for 2026-10-29T13Z lists\n")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_alconent','trend.#AlconEntLongForCowDung'),('trend_thursdayvibes','trend.#thursdayvibes'),('trend_thankfulthursday','trend.Thankful Thursday'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_corepce','trend.Core PCE'),('trend_q3gdp','trend.Q3 GDP'),('trend_hyperliquid','trend.Hyperliquid'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) == 'trend.#AlconEntLongForCowDung': return 'gaming'""","""        if str(_x) in ('trend.Core PCE','trend.Q3 GDP'): return 'markets'  # 1259Z: US September PCE inflation and advance Q3 GDP released 12:30Z (one event)
        if str(_x) == 'trend.Hyperliquid': return 'markets'  # 1259Z: ICE (NYSE owner) and trade[XYZ] to bring Hyperliquid perpetual futures to US markets
        if str(_x) == 'trend.#AlconEntLongForCowDung': return 'gaming'""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):",2)
R("if _c.endswith('1206Z.json') and '/29/' in _c: continue","if _c.endswith('1259Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-29T1102Z'  # 1206Z: culture/sports/online last read in 1102Z","_last = '2026-10-29T1206Z'  # 1259Z: news/money/science last read in 1206Z")
R("not in requests/plan.json for 2026-10-29T12Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-29T13Z (rotation: culture/sports/online this run)")
R("reason = 'cut by requests/plan.json for 2026-10-29T12Z (day band, allowance 42; it cuts desk.life)'","reason = 'not due in requests/plan.json for 2026-10-29T13Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115759358604918939']  # 1259Z: the most liked reply to tradexyz 2115755854125478285 in its first 20 minutes (0xRiver8, 10 likes); the other 24 have 0 to 3 likes from small accounts (one is profanity) and are left out\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115760585271091325','2115760803768885750','2115759944616329305']  # 1259Z: the three most liked quotes in the window (cryppimagic, bull_genius, Alvin0617); the other 22 have under 10 likes from small accounts\n")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T12Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T13Z (contract/PLAN.md), in its order and in batches of 100 (525 ids; its left_out counts 248 slowed flat posts and 4 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 6 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id, the unread ones read by id in 2 screen reads (108 ids); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Core PCE\", \"Q3 GDP\" and \"Hyperliquid\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first three top-ten US names not attached in the previous run, in list order, skipping the Chinese-language hashtag \"#叠纸破坏中国两岸文化往来\" and \"#NationalCatDay\" (National Cat Day attached in 1102Z); \"Core PCE\" and \"Q3 GDP\" are one event, the 8:30 AM ET US PCE and advance Q3 GDP release)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"just\" and \"what\" (1206Z used \"it\" and \"that\"), each quoted so X does not reject a bare stopword: (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each (the quote page returned 24)',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T14:00:00Z, end_time 2026-10-29T13:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas); each series is the 167 full hours 2026-10-22T14:00Z to 2026-10-29T12:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T10:41:00Z (the post\\'s creation, 10:41:19) and end_time 2026-10-29T11:01:00Z: (conversation_id:2115755854125478285 is:reply) and (quotes_of_tweet_id:2115755854125478285 -is:retweet); the plan gives context.top two reads, so one post: 2115755854125478285 (@tradexyz on joining ICE to bring 24/7 Hyperliquid perpetual futures to US markets, the biggest fresh post new this run at about 333K views in 2.3 hours); 25 replies and 25 quotes in the window, the most liked reply and 3 most liked quotes kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (7:06 AM CT","Candidates screened with what the plan reads returned. '\n",
 "            f'Day-band run (7:59 AM CT Oct 29 / 12:59 UTC Oct 29, the 13Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-29T13Z, written 12:14Z; 31 reads listed plus up to 3 screen reads) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 525 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 248 slowed flat posts and the 4 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, entertainment, sports, internet and life (5 reads; the other 14 not due per the plan). Volume: medicine, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Core PCE\", \"Q3 GDP\" and \"Hyperliquid\" (3 reads). rising.global: quote stream \"just\" and repost stream \"what\" (2 reads). context.top: tradexyz 2115755854125478285 (2 reads). Screen: 2 reads by id (108 unread references). '\n")
R("'plan': '2026-10-29T12Z',","'plan': '2026-10-29T13Z',")
R("    'context': [{'post_id': '2115436064458621189',","    'context': [{'post_id': '2115755854125478285',")
R("capture/2026/10/29/1206Z.json'","capture/2026/10/29/1259Z.json'")
open('build_capture.py','w').write(s); print('ok')
