s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1707Z.json from saved","1802Z.json from saved")
R("capture/work/2026-10-29T1707Z'","capture/work/2026-10-29T1802Z'")
R("RUN_ID = '2026-10-29T1707Z'","RUN_ID = '2026-10-29T1802Z'")
R("STARTED = '2026-10-29T17:07:00Z'","STARTED = '2026-10-29T18:02:00Z'")
R("OBS_AT = '2026-10-29T17:09:00Z'","OBS_AT = '2026-10-29T18:03:00Z'")
R("READS_BEFORE = 509","READS_BEFORE = 478")
SPAN("READS_USED = 31","\n","READS_USED = 37  # 1802Z: this run's 37 X calls (watch 5, desks 13, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2 of the plan's 3); the counter fell 478 to 441; no 429 or 503 refusals\n")
R("datetime(2026,10,29,17,9,tzinfo=timezone.utc).timestamp()  # 1707Z (","datetime(2026,10,29,18,3,tzinfo=timezone.utc).timestamp()  # 1802Z (1707Z used 17:09, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_parsons': 'trend_parsons.txt', 'trend_mack': 'trend_mack.txt', 'trend_titans': 'trend_titans.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'watch4': 'watch4.txt',
    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_wnbafinals': 'trend_wnbafinals.txt', 'trend_larkin': 'trend_larkin.txt', 'trend_burton': 'trend_burton.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
SPAN("DUE = ['politics','entertainment'","\n","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1802Z: the 13 desks requests/plan.json for 2026-10-29T18Z lists\n")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_parsons','trend.Parsons'),('trend_mack','trend.Mack'),('trend_titans','trend.Titans'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_wnbafinals','trend.#WNBAFinals'),('trend_larkin','trend.Larkin'),('trend_burton','trend.Burton'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) in ('trend.Parsons','trend.Mack','trend.Titans'): return 'sports'  # 1707Z""","""        if str(_x) in ('trend.#WNBAFinals','trend.Larkin','trend.Burton'): return 'sports'  # 1802Z: WNBA Finals Game 6 (Veronica Burton fouls) and the Dylan Larkin trade standoff in Detroit
        if str(_x) in ('trend.Parsons','trend.Mack','trend.Titans'): return 'sports'  # 1707Z""")
R("('watch0','watch1','watch2','watch3','watch4','watch5')","('watch0','watch1','watch2','watch3','watch4')",2)
R("if _c.endswith('1707Z.json') and '/29/' in _c: continue","if _c.endswith('1802Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T1607Z'  # 1707Z: news/money/science last read in 1607Z","_last = '2026-10-29T1707Z'  # 1802Z: culture/sports/online last read in 1707Z")
R("not in requests/plan.json for 2026-10-29T17Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-29T18Z (rotation: news/money/science this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T17Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T18Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['politics','sports','internet','life','offbeat']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115798348355539302','2115798531504226583','2115796935843983802']  # 1802Z: the three most liked replies to DiscussingFilm 2115793711032676693 in its first 20 minutes (Nythral_man, ianmsantos, Lanbron); the other 22 have 4 likes or fewer\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115798377937903810','2115798219028664580','2115798460725145939']  # 1802Z: the three most liked quotes in the window after the two sexual jokes (JtheFrog0, 7Spideycomics) are left out: MatasChamorrom2, kutttyyy__, AirmitK; the rest have 5 likes or fewer\n")
R("CTX_IDS = ['2115832586706563176'] + CTX_REPLIES","CTX_IDS = ['2115793711032676693'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T17Z","6 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T18Z (contract/PLAN.md), in its order and in batches of 100 (415 ids; its left_out counts 239 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#WNBAFinals\", \"Larkin\" and \"Burton\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1707Z and not read in the last runs, skipping \"#NationalCatDay\" and \"#IStandWithTaylor\" as read in 1607Z and \"Big Jeff\" as read in 1501Z; \"#WNBAFinals\" and \"Burton\" are one event, WNBA Finals Game 6 (Veronica Burton\\'s fouls); \"Larkin\" is the Dylan Larkin trade standoff with the Red Wings); screen: 2 reads by id (150 unread references; no second-hop left)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"just\" and \"what\" (1707Z used \"it\" and \"that\"), each quoted so X does not reject a bare stopword: (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T19:00:00Z, end_time 2026-10-29T18:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.sports, volume.internet, volume.life, volume.offbeat); each series is the 167 full hours 2026-10-22T19:00Z to 2026-10-29T17:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T13:11:00Z (the post\\'s creation minute) and end_time 2026-10-29T13:31:00Z: (conversation_id:2115793711032676693 is:reply) and (quotes_of_tweet_id:2115793711032676693 -is:retweet); the plan gives context.top two reads, so one post: 2115793711032676693 (@DiscussingFilm first look at the Dune: Part 3 popcorn bucket, the biggest fresh post new this run at about 4.0M views in under 5 hours); 25 replies and 25 quotes in the window, the 3 most liked of each kept (two sexual quote jokes left out)',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (12:07 PM CT","Screen: 3 reads by id (118 unread references, then 25 second-hop). '\n",
 "            f'Day-band run (1:02 PM CT Oct 29 / 18:02 UTC Oct 29, the 18Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-29T18Z; 38 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 415 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 239 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (13 reads). Volume: politics, sports, internet, life and offbeat (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"#WNBAFinals\", \"Larkin\" and \"Burton\" (3 reads). rising.global: quote stream \"just\" and repost stream \"what\" (2 reads). context.top: DiscussingFilm 2115793711032676693 (2 reads). '\n"
 "            f'Screen: 2 reads by id (150 unread references; no second-hop left, so the plan\\'s third screen read was not used). '\n")
R("'plan': '2026-10-29T17Z',","'plan': '2026-10-29T18Z',")
R("    'context': [{'post_id': '2115832586706563176',","    'context': [{'post_id': '2115793711032676693',")
R("capture/2026/10/29/1707Z.json'","capture/2026/10/29/1802Z.json'")
anchor="DESK_OVERRIDE_RUN.update({'2115832586706563176'"
i=s.index(anchor); j=s.index("\n",i)+1
add=("skip_nsfw |= {'2115798282924659177','2115798221050052699'}  # 1802Z: sexual text (JtheFrog0 and 7Spideycomics quote jokes on the Dune popcorn bucket)\n"
"DESK_OVERRIDE_RUN.update({'2115793711032676693':'entertainment','2115798348355539302':'entertainment','2115798531504226583':'entertainment','2115796935843983802':'entertainment','2115798377937903810':'entertainment','2115798219028664580':'entertainment','2115798460725145939':'entertainment'})  # 1802Z: DiscussingFilm Dune popcorn bucket and its context replies and quotes are entertainment\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s); print('ok')
