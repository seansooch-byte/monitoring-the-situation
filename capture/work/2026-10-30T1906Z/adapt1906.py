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
R('"""Build capture/2026/10/30/1803Z.json from saved','"""Build capture/2026/10/30/1906Z.json from saved')
R("capture/work/2026-10-30T1803Z'","capture/work/2026-10-30T1906Z'")
R("RUN_ID = '2026-10-30T1803Z'","RUN_ID = '2026-10-30T1906Z'")
L("STARTED = ","STARTED = '2026-10-30T19:06:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T19:07:00Z'")
R("READS_BEFORE = 489","READS_BEFORE = 452")
L("READS_USED = 37","READS_USED = 26  # 1906Z: this run's 26 X calls (watch 4, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 1); the counter fell 452 to 426; no 429 or 503 refusals")
R("datetime(2026,10,30,18,4,tzinfo=timezone.utc).timestamp()  # 1803Z (","datetime(2026,10,30,19,7,tzinfo=timezone.utc).timestamp()  # 1906Z (1803Z used 18:04, ")
R("    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',","    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',")
R("    'trend_bblc': 'trend_bblc.txt', 'trend_nbacup': 'trend_nbacup.txt', 'trend_agbaji': 'trend_agbaji.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_altman': 'trend_altman.txt', 'trend_fairplay': 'trend_fairplay.txt', 'trend_condesa': 'trend_condesa.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1906Z: the four desks requests/plan.json for 2026-10-30T19Z lists")
R("""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_bblc','trend.#BBLC'),('trend_nbacup','trend.NBA Cup'),('trend_agbaji','trend.Ochai Agbaji'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_altman','trend.Sam Altman'),('trend_fairplay','trend.FAIR PLAY MAX'),('trend_condesa','trend.Condesa'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x)=='trend.#BBLC': return 'tech'  # 1803Z: the stream holds old posts on Intel's NVL-BBLC chip samples; no event found\n",
  "        if str(_x)=='trend.#BBLC': return 'tech'  # 1803Z: the stream holds old posts on Intel's NVL-BBLC chip samples; no event found\n        if str(_x)=='trend.Sam Altman': return 'ai'  # 1906Z: Sam Altman says local DRAM is a poor use of scarce memory (one event with DRAM)\n        if str(_x)=='trend.FAIR PLAY MAX': return 'sports'  # 1906Z: Fanatics Fair Play Max player-prop pledge (only 2 old posts returned)\n        if str(_x)=='trend.Condesa': return 'world'  # 1906Z: Mexico City police arrest an alleged dog killer in Condesa\n")
R("CTX_REPLIES = CTXR  # 1803Z: replies to elonmusk 2116047608036888796 in its first 20 minutes (none returned)",
  "CTX_REPLIES = CTXR  # 1906Z: replies to PopBase 2116018757675991243 in its first 20 minutes (25 returned)")
R("CTX_IDS = ['2116047608036888796'] + CTX_REPLIES","CTX_IDS = ['2116018757675991243'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116047608036888796']+CTXR+CTXQ})  # 1803Z:",
  "DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116047608036888796']})\nDESK_OVERRIDE_RUN.update({_x:'life' for _x in ['2116018757675991243']+CTXR+CTXQ})  # 1906Z: PopBase 'National Text Your Ex Day' post and its context replies and quotes are life  # 1803Z:")
R("if _c.endswith('1803Z.json') and '/30/' in _c: continue","if _c.endswith('1906Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T1709Z'  # 1803Z: culture/sports/online last read in 1709Z","_last = '2026-10-30T1803Z'  # 1906Z: news/money/science last read in 1803Z")
R("not in requests/plan.json for 2026-10-30T18Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T19Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T18Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T19Z (desks_not_due)'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T18Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T19Z, in its order and in batches of 100 (353 ids; the plan\\'s note: \"51 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 19 flat posts wait for their sixth run\"; its left_out counts 19 slowed, 0 over cap and 1 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 1 of the plan\\'s 3 reads by id: the 86 unread first-hop references (85 returned, 1 Not Found); they pointed at no unread second-hop posts, so the other 2 screen reads were not used); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Sam Altman\", \"FAIR PLAY MAX\" and \"Condesa\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 1803Z not read in 1709Z (Philo, Binance and Battlefront 3 were); \"Halloween\" is one event with \"Happy Halloween\", read in 1507Z; \"FAIR PLAY MAX\" returned only 2 posts from Oct 19 and 22 on the Fanatics pledge); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"is\" and \"you\" (1803Z used \"the\" and \"this\"), each quoted so X does not reject a bare stopword: (\"is\" lang:en is:quote -is:retweet), (\"you\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T20:00:00Z, end_time 2026-10-30T19:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-23T20:00Z to 2026-10-30T18:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T04:06:00Z (the post\\'s creation minute) and end_time 2026-10-30T04:26:00Z: (conversation_id:2116018757675991243 is:reply) and (quotes_of_tweet_id:2116018757675991243 -is:retweet); the plan gives context.top two reads, so one post: 2116018757675991243 (@PopBase \"Today is National Text Your Ex Day.\", the biggest post new this run under 24 hours old at about 1.6M views, after likely-promoted posts were left out); 25 replies and 25 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (1:03 PM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (2:06 PM CT Oct 30 / 19:06 UTC Oct 30, the 19Z slot; band allowance 42): requests/plan.json is for 2026-10-30T19Z (written 18:11Z after the 1803Z capture), so it was followed (28 reads listed) top to bottom; screen needed 1 of its 3 reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 353 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 19 slowed flat posts and 1 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four the plan lists; the other 15 not due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Sam Altman", "FAIR PLAY MAX" and "Condesa" (3 reads). rising.global: quote stream "is" and repost stream "you" (2 reads). context.top: PopBase 2116018757675991243 (2 reads). '
            f'Screen: 1 read by id (the 86 unread first-hop references, 85 returned, 1 Not Found; no unread second-hop references). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T18Z',","'plan': '2026-10-30T19Z',")
R("    'context': [{'post_id': '2116047608036888796',","    'context': [{'post_id': '2116018757675991243',")
R("f'{REPO}/capture/2026/10/30/1803Z.json'","f'{REPO}/capture/2026/10/30/1906Z.json'")
anchor="EXTRA_PRIVATE |= {'2115974957452992663','2116189296893808825','2115948754100510781'}  # 1803Z"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+open('skips1906.txt').read()+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
