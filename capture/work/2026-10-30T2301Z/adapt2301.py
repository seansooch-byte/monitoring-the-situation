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
R('"""Build capture/2026/10/30/2202Z.json from saved','"""Build capture/2026/10/30/2301Z.json from saved')
R("capture/work/2026-10-30T2202Z'","capture/work/2026-10-30T2301Z'")
R("RUN_ID = '2026-10-30T2202Z'","RUN_ID = '2026-10-30T2301Z'")
L("STARTED = ","STARTED = '2026-10-30T23:01:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T23:02:00Z'")
R("READS_BEFORE = 356","READS_BEFORE = 317")
L("READS_USED = 39","READS_USED = 29  # 2301Z: this run's 29 X calls (watch 4, desks 4, volume 5, request 1, trends 2, sensors 3, viral.global 3, rising.global 2, screen 3, context.top 2); the counter fell 317 to 288; no 429 or 503 refusals")
R("datetime(2026,10,30,22,3,tzinfo=timezone.utc).timestamp()  # 2202Z (","datetime(2026,10,30,23,2,tzinfo=timezone.utc).timestamp()  # 2301Z (2202Z used 22:03, ")
R("    'req_r01': 'req_r01_picks.txt',  # 2202Z: the six request picks re-read by id with full fields\n","    'req_r01': 'req_r01.txt',  # 2301Z: the request search\n")
R("    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 2202Z: three screen reads\n","    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 2301Z: three screen reads\n")
R("    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',","    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',")
R("    'trend_tribunal': 'trend_tribunal.txt', 'trend_usyk': 'trend_usyk.txt', 'trend_altman': 'trend_altman.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_kucherov': 'trend_kucherov.txt', 'trend_yeon': 'trend_yeon.txt', 'trend_polish': 'trend_polish.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 2301Z: the four desks requests/plan.json for 2026-10-30T23Z lists")
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_tribunal','trend.Constitutional Tribunal'),('trend_usyk','trend.Usyk'),('trend_altman','trend.Sam Altman'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_kucherov','trend.Kucherov'),('trend_yeon','trend.Yeon'),('trend_polish','trend.Polish'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x)=='trend.Usyk': return 'sports'  # 2202Z: Oleksandr Usyk boxing\n",
  "        if str(_x)=='trend.Usyk': return 'sports'  # 2202Z: Oleksandr Usyk boxing\n        if str(_x)=='trend.Kucherov': return 'sports'  # 2301Z: Nikita Kucherov, NHL\n        if str(_x)=='trend.Yeon': return 'gaming'  # 2301Z: the League of Legends player Yeon at Worlds\n        if str(_x)=='trend.Polish': return 'world'  # 2301Z: the Polish Constitutional Tribunal standoff\n")
R("CTX_REPLIES = CTXR  # 2202Z: replies to ScrambledFaz 2116054436178964783 in its first 20 minutes (13 returned)",
  "CTX_REPLIES = CTXR  # 2301Z: replies to elonmusk 2116165938525741496 in its first 20 minutes (25 returned)")
R("CTX_IDS = ['2116054436178964783'] + CTX_REPLIES","CTX_IDS = ['2116165938525741496'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116054436178964783']+CTXR+CTXQ})  # 2202Z:",
  "DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116054436178964783']})\nDESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116165938525741496']+CTXR+CTXQ})  # 2301Z: elonmusk post on Democrats and one-party rule and its context replies and quotes are politics  # 2202Z:")
R("if _c.endswith('2202Z.json') and '/30/' in _c: continue","if _c.endswith('2301Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T2102Z'  # 2202Z: culture/sports/online last read in 2102Z","_last = '2026-10-30T2202Z'  # 2301Z: news/money/science last read in 2202Z")
R("not in requests/plan.json for 2026-10-30T22Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T23Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T22Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T23Z (desks_not_due)'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T22Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T23Z, in its order and in batches of 100 (334 ids; the plan\\'s note: \"61 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 20 flat posts wait for their sixth run\"; its left_out counts 20 slowed, 0 over cap and 0 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second and third hop by id, including attachments.media_source_tweet_id (screen: the plan\\'s 3 reads by id: the 93 unread first-hop references (1 Not Found), then the 21 unread second-hop references, then the 13 third-hop references); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Kucherov\", \"Yeon\" and \"Polish\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; none of the three had posts attached in 2202Z: Kucherov is the NHL player, Yeon the League of Legends player at Worlds (with some unrelated matches), and Polish is the Constitutional Tribunal standoff (with Poland, Tusk and Nawrocki); Constitutional Tribunal, Usyk and Sam Altman were read in 2202Z); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (2202Z used \"just\" and \"what\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T00:00:00Z, end_time 2026-10-30T23:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T00:00Z to 2026-10-30T22:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T13:50:00Z (the post\\'s creation minute) and end_time 2026-10-30T14:10:00Z: (conversation_id:2116165938525741496 is:reply) and (quotes_of_tweet_id:2116165938525741496 -is:retweet); the plan gives context.top two reads, so one post: 2116165938525741496 (@elonmusk post saying Democrats intend to cement one-party rule, the biggest post new this run under 24 hours old at about 3.55M views); 25 replies and 25 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (5:02 PM CT","media descriptions. '\n",
"""            f'Day-band run (7:01 PM EDT Oct 30 / 23:01 UTC Oct 30, the 23Z slot, the last run of the UTC day; band allowance 42): requests/plan.json is for 2026-10-30T23Z (written 22:12Z after the 2202Z capture), so it was followed (29 reads listed) top to bottom; screen used all 3 of its reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 334 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 20 slowed flat posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four the plan lists; the other fifteen not due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Kucherov", "Yeon" and "Polish" (3 reads). rising.global: quote stream "the" and repost stream "this" (2 reads). context.top: elonmusk 2116165938525741496 (2 reads). '
            f'Screen: 3 reads by id (93 unread first-hop references, 1 Not Found; then 21 second-hop and 13 third-hop references). '
            f'Request r-2026-10-30-01 (Polish government and president on the police at the Constitutional Tribunal): 2202Z read it but wrote no answers entry, so the plan listed it again; one search this run for Judge Anna Korwin-Piotrowska by name and the President\\'s office account KPRP since 00:00Z Oct 30 returned only third-party commentary, none from her or KPRP; the six official posts found in 2202Z (Donald Tusk, President Nawrocki, Justice Minister and Prosecutor General Waldemar Zurek, two Justice Ministry videos and the PM office video) were re-read in watch this run and are the answer. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T22Z',","'plan': '2026-10-30T23Z',")
R("    'context': [{'post_id': '2116054436178964783',","    'context': [{'post_id': '2116165938525741496',")
R("f'{REPO}/capture/2026/10/30/2202Z.json'","f'{REPO}/capture/2026/10/30/2301Z.json'")
R("REQ_PICKS = {'r-2026-10-30-01': [","REQ_PICKS = {'r-2026-10-30-01': [")
L("    'r-2026-10-30-01': 'search_posts_all (from:donaldtusk","    'r-2026-10-30-01': 'search_posts_all (\"Korwin-Piotrowska\" OR from:KPRP) -is:retweet, start_time 2026-10-30T00:00:00Z, relevancy, 25 results (only third-party commentary returned, none from Judge Korwin-Piotrowska or KPRP); the six official posts on the Tribunal first found in 2202Z by searching from:donaldtusk, PremierRP, KPRP, NawrockiKn, MS_GOV_PL, PK_GOV_PL and Zurek_Waldemar were re-read in watch this run',")
R("ANSWERS = []","ANSWERS = [{'request_id': 'r-2026-10-30-01', 'status': 'ok', 'post_ids': [i for i in REQ_PICKS['r-2026-10-30-01'] if i in posts_by_sel], 'note': 'Posts from Donald Tusk, his office (PremierRP video), President Nawrocki, and Justice Minister and Prosecutor General Waldemar Zurek and the Justice Ministry, all re-read this run. A search for Judge Anna Korwin-Piotrowska by name and for the President\\'s office account KPRP since 00:00 UTC Oct 30 found no posts from either, only commentary by others.'}]")
anchor="EXTRA_PRIVATE |= {'1844016316593971494'"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+open('skips2301.txt').read()+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
