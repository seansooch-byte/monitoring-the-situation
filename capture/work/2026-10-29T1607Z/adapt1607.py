s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1501Z.json from saved","1607Z.json from saved")
R("capture/work/2026-10-29T1501Z'","capture/work/2026-10-29T1607Z'")
R("RUN_ID = '2026-10-29T1501Z'","RUN_ID = '2026-10-29T1607Z'")
R("STARTED = '2026-10-29T15:01:00Z'","STARTED = '2026-10-29T16:07:00Z'")
R("OBS_AT = '2026-10-29T15:03:00Z'","OBS_AT = '2026-10-29T16:08:00Z'")
R("READS_BEFORE = 578","READS_BEFORE = 551")
SPAN("READS_USED = 27","\n","READS_USED = 42  # 1607Z: this run's 42 X calls, the plan's 42 reads (watch 7, desks 18, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen and desk.life left out by the plan); the counter fell 551 to 509; no 429 or 503 refusals\n")
R("datetime(2026,10,29,15,3,tzinfo=timezone.utc).timestamp()  # 1501Z (","datetime(2026,10,29,16,8,tzinfo=timezone.utc).timestamp()  # 1607Z (1501Z used 15:03, ")
R("""    'watch4': 'watch4.txt',
    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_simmons': 'trend_simmons.txt', 'trend_bigjeff': 'trend_bigjeff.txt', 'trend_ryanpoles': 'trend_ryanpoles.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_this': 'quote_this.txt',
    'repost_my': 'repost_my.txt',
    'trend_nationalcatday': 'trend_nationalcatday.txt', 'trend_hyperliquid': 'trend_hyperliquid.txt', 'trend_istandwithtaylor': 'trend_istandwithtaylor.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
SPAN("DUE = ['politics','entertainment','sports','internet']","\n","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','offbeat']  # 1607Z: the 18 desks requests/plan.json for 2026-10-29T16Z lists (desk.life not due)\n")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_simmons','trend.Simmons'),('trend_bigjeff','trend.Big Jeff'),('trend_ryanpoles','trend.Ryan Poles'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_this','quote'),('repost_my','repost'),
    ('trend_nationalcatday','trend.#NationalCatDay'),('trend_hyperliquid','trend.Hyperliquid'),('trend_istandwithtaylor','trend.#IStandWithTaylor'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) == 'trend.National Cat Day': return 'offbeat'""","""        if str(_x) == 'trend.#NationalCatDay': return 'offbeat'  # 1607Z: cat photos and clips for National Cat Day (animals), as in 1102Z
        if str(_x) == 'trend.#IStandWithTaylor': return 'music'  # 1607Z: Swifties' hashtag campaign backing Taylor Swift against what they call a smear campaign
        if str(_x) == 'trend.National Cat Day': return 'offbeat'""")
R("('watch0','watch1','watch2','watch3','watch4')","('watch0','watch1','watch2','watch3','watch4','watch5','watch6')",2)
R("if _c.endswith('1501Z.json') and '/29/' in _c: continue","if _c.endswith('1607Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T1406Z'  # 1501Z: news/money/science last read in 1406Z","_last = '2026-10-29T1501Z'  # 1607Z: culture/sports/online last read in 1501Z")
R("not in requests/plan.json for 2026-10-29T15Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-29T16Z (rotation: news/money/science this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T15Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T16Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115827957386056068']  # 1607Z: the most liked reply to elonmusk 2115823011399938182 in its first 20 minutes (samuraix, 3 likes); the other 24 have 0 to 3 likes from small accounts and are left out\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115827775810445764','2115827789404271054']  # 1607Z: the two most liked quotes in the window (getLanista, AltcoinsFrance); the other 23 have 7 likes or fewer\n")
R("CTX_IDS = ['2115813435543826449'] + CTX_REPLIES","CTX_IDS = ['2115823011399938182'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T15Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T16Z (contract/PLAN.md), in its order and in batches of 100 (657 ids; its left_out counts 335 slowed flat posts and 9 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#NationalCatDay\", \"Hyperliquid\" and \"#IStandWithTaylor\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the top US names not attached in 1406Z or 1501Z, skipping \"Titans\", \"The Bears\" and \"Mack\" as the Simmons trade and NFL news read in 1501Z, and \"Dexter Lawrence\" for the same reason); screen left out by the plan, so candidates are screened with what these reads returned',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"this\" and \"my\" (1501Z used \"is\" and \"you\"), each quoted so X does not reject a bare stopword: (\"this\" lang:en is:quote -is:retweet), (\"my\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T17:00:00Z, end_time 2026-10-29T16:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science); each series is the 167 full hours 2026-10-22T17:00Z to 2026-10-29T15:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T15:08:00Z (the post\\'s creation minute) and end_time 2026-10-29T15:28:00Z: (conversation_id:2115823011399938182 is:reply) and (quotes_of_tweet_id:2115823011399938182 -is:retweet); the plan gives context.top two reads, so one post: 2115823011399938182 (@elonmusk \"Interesting\" quoting Stan Druckenmiller on 24/7 Hyperliquid futures, the biggest fresh post new this run at about 1.35M views in an hour); 25 replies and 25 quotes in the window, the most liked reply and 2 most liked quotes kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (10:01 AM CT","Screen: 2 reads by id (94 unread references, then 16 second-hop). '\n",
 "            f'Day-band run (11:07 AM CT Oct 29 / 16:07 UTC Oct 29, the 16Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-29T16Z, written 15:09Z; 42 reads listed, screen cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 657 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 335 slowed flat posts and the 9 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, world, defense, justice, disaster, markets, business, ai, tech, science, medicine, entertainment, music, gaming, ideas, sports, internet and offbeat (18 reads; desk.life not due per the plan). Volume: markets, business, ai, tech and science (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"#NationalCatDay\", \"Hyperliquid\" and \"#IStandWithTaylor\" (3 reads). rising.global: quote stream \"this\" and repost stream \"my\" (2 reads). context.top: elonmusk 2115823011399938182 (2 reads). '\n"
 "            f'Cut by the plan and not read: screen. Candidates screened with what the plan reads returned. '\n")
R("'plan': '2026-10-29T15Z',","'plan': '2026-10-29T16Z',")
R("    'context': [{'post_id': '2115813435543826449',","    'context': [{'post_id': '2115823011399938182',")
R("capture/2026/10/29/1501Z.json'","capture/2026/10/29/1607Z.json'")
open('build_capture.py','w').write(s); print('ok')
