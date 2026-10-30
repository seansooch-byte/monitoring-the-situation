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
R('"""Build capture/2026/10/30/1906Z.json from saved','"""Build capture/2026/10/30/2006Z.json from saved')
R("capture/work/2026-10-30T1906Z'","capture/work/2026-10-30T2006Z'")
R("RUN_ID = '2026-10-30T1906Z'","RUN_ID = '2026-10-30T2006Z'")
L("STARTED = ","STARTED = '2026-10-30T20:06:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T20:07:00Z'")
R("READS_BEFORE = 452","READS_BEFORE = 426")
L("READS_USED = 26","READS_USED = 42  # 2006Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 426 to 384; no 429 or 503 refusals")
R("datetime(2026,10,30,19,7,tzinfo=timezone.utc).timestamp()  # 1906Z (","datetime(2026,10,30,20,7,tzinfo=timezone.utc).timestamp()  # 2006Z (1906Z used 19:07, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', \n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',\n")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
R("    'screen0': 'screen0.txt',  # 1906Z: one screen read\n","")
R("    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',","    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',")
R("    'trend_altman': 'trend_altman.txt', 'trend_fairplay': 'trend_fairplay.txt', 'trend_condesa': 'trend_condesa.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_demarcus': 'trend_demarcus.txt', 'trend_tusk': 'trend_tusk.txt', 'trend_honda': 'trend_honda.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 2006Z: all 19 desks, as requests/plan.json for 2026-10-30T20Z lists")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_altman','trend.Sam Altman'),('trend_fairplay','trend.FAIR PLAY MAX'),('trend_condesa','trend.Condesa'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_demarcus','trend.Demarcus Henry'),('trend_tusk','trend.Tusk'),('trend_honda','trend.Honda'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x)=='trend.Condesa': return 'world'  # 1906Z: Mexico City police arrest an alleged dog killer in Condesa\n",
  "        if str(_x)=='trend.Condesa': return 'world'  # 1906Z: Mexico City police arrest an alleged dog killer in Condesa\n        if str(_x)=='trend.Demarcus Henry': return 'sports'  # 2006Z: five-star recruit DeMarcus Henry commits to North Carolina\n        if str(_x)=='trend.Tusk': return 'world'  # 2006Z: Polish police enter the Constitutional Tribunal on Donald Tusk's orders; critics call it a coup\n        if str(_x)=='trend.Honda': return 'justice'  # 2006Z: workers run from an ICE operation at a Honda plant in Alabama\n")
R("CTX_REPLIES = CTXR  # 1906Z: replies to PopBase 2116018757675991243 in its first 20 minutes (25 returned)",
  "CTX_REPLIES = CTXR  # 2006Z: replies to surajit_ghosh2 2116025216795312542 in its first 20 minutes (none returned)")
R("CTX_IDS = ['2116018757675991243'] + CTX_REPLIES","CTX_IDS = ['2116025216795312542'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'life' for _x in ['2116018757675991243']+CTXR+CTXQ})  # 1906Z:",
  "DESK_OVERRIDE_RUN.update({_x:'life' for _x in ['2116018757675991243']})\nDESK_OVERRIDE_RUN.update({_x:'disaster' for _x in ['2116025216795312542']+CTXR+CTXQ})  # 2006Z: surajit_ghosh2 Panama earthquake video is disaster  # 1906Z:")
R("if _c.endswith('1906Z.json') and '/30/' in _c: continue","if _c.endswith('2006Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T1803Z'  # 1906Z: news/money/science last read in 1803Z","_last = '2026-10-30T1906Z'  # 2006Z: culture/sports/online last read in 1906Z")
R("not in requests/plan.json for 2026-10-30T19Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T20Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T19Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T20Z (desks_not_due)'")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T19Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T20Z, in its order and in batches of 100 (646 ids; the plan\\'s note: \"52 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 91 flat posts wait for their sixth run\"; its left_out counts 91 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read and a second hop by id","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Demarcus Henry\", \"Tusk\" and \"Honda\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 1906Z not read in the last few runs (Halloween, Sam Altman and Philo were); \"#BBLC\" was read in 1803Z); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"and\" and \"my\" (1906Z used \"is\" and \"you\"), each quoted so X does not reject a bare stopword: (\"and\" lang:en is:quote -is:retweet), (\"my\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T21:00:00Z, end_time 2026-10-30T20:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-23T21:00Z to 2026-10-30T19:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T04:31:00Z (the post\\'s creation minute) and end_time 2026-10-30T04:51:00Z: (conversation_id:2116025216795312542 is:reply) and (quotes_of_tweet_id:2116025216795312542 -is:retweet); the plan gives context.top two reads, so one post: 2116025216795312542 (@surajit_ghosh2 video of a 7.7 magnitude earthquake in Panama, the biggest post new this run under 24 hours old at about 2.1M views); no replies and no quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (2:06 PM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (3:06 PM CT Oct 30 / 20:06 UTC Oct 30, the 20Z slot; band allowance 42): requests/plan.json is for 2026-10-30T20Z (written 19:12Z after the 1906Z capture), so it was followed (42 reads listed, screen cut) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 646 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 91 slowed flat posts and 2 unavailable in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Demarcus Henry", "Tusk" and "Honda" (3 reads). rising.global: quote stream "and" and repost stream "my" (2 reads). context.top: surajit_ghosh2 2116025216795312542 (2 reads, nothing returned in the window). '
            f'Screen: cut by the plan; unread second-hop references left unread. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T19Z',","'plan': '2026-10-30T20Z',")
R("    'context': [{'post_id': '2116018757675991243',","    'context': [{'post_id': '2116025216795312542',")
R("f'{REPO}/capture/2026/10/30/1906Z.json'","f'{REPO}/capture/2026/10/30/2006Z.json'")
anchor="EXTRA_PRIVATE |= {'2116158076160000085','2116147038777757887'}  # 1906Z"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+open('skips2006.txt').read()+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
