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
R('"""Build capture/2026/10/30/1709Z.json from saved','"""Build capture/2026/10/30/1803Z.json from saved')
R("capture/work/2026-10-30T1709Z'","capture/work/2026-10-30T1803Z'")
R("RUN_ID = '2026-10-30T1709Z'","RUN_ID = '2026-10-30T1803Z'")
L("STARTED = ","STARTED = '2026-10-30T18:03:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T18:04:00Z'")
R("READS_BEFORE = 519","READS_BEFORE = 489")
L("READS_USED = 30","READS_USED = 37  # 1803Z: this run's 37 X calls (watch 4, desks 13, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 489 to 452; no 429 or 503 refusals")
R("datetime(2026,10,30,17,10,tzinfo=timezone.utc).timestamp()  # 1709Z (","datetime(2026,10,30,18,4,tzinfo=timezone.utc).timestamp()  # 1803Z (1709Z used 17:10, ")
R("'watch4': 'watch4.txt', 'watch5': 'watch5.txt',\n","\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("    'quote_what': 'quote_what.txt',\n    'repost_the': 'repost_the.txt',","    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',")
R("    'trend_philo': 'trend_philo.txt', 'trend_binance': 'trend_binance.txt', 'trend_battlefront': 'trend_battlefront.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_bblc': 'trend_bblc.txt', 'trend_nbacup': 'trend_nbacup.txt', 'trend_agbaji': 'trend_agbaji.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1803Z: the thirteen desks requests/plan.json for 2026-10-30T18Z lists")
R("""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_philo','trend.Philo'),('trend_binance','trend.Binance'),('trend_battlefront','trend.Battlefront 3'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_bblc','trend.#BBLC'),('trend_nbacup','trend.NBA Cup'),('trend_agbaji','trend.Ochai Agbaji'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x)=='trend.Philo': return 'sports'  # 1709Z: Florida starts QB Aaron Philo against Georgia\n",
  "        if str(_x)=='trend.Philo': return 'sports'  # 1709Z: Florida starts QB Aaron Philo against Georgia\n        if str(_x) in ('trend.NBA Cup','trend.Ochai Agbaji'): return 'sports'  # 1803Z: NBA Cup opens tonight; Thunder sign Ochai Agbaji\n        if str(_x)=='trend.#BBLC': return 'tech'  # 1803Z: the stream holds old posts on Intel's NVL-BBLC chip samples; no event found\n")
R("CTX_REPLIES = CTXR  # 1709Z: replies to nine 2115927574329057714 in its first 20 minutes (one returned)",
  "CTX_REPLIES = CTXR  # 1803Z: replies to elonmusk 2116047608036888796 in its first 20 minutes (none returned)")
R("CTX_IDS = ['2115927574329057714'] + CTX_REPLIES","CTX_IDS = ['2116047608036888796'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2115927574329057714']+CTXR+CTXQ})  # 1709Z:",
  "DESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2115927574329057714']})\nDESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116047608036888796']+CTXR+CTXQ})  # 1803Z: elonmusk 'game over for America' post is politics  # 1709Z:")
R("if _c.endswith('1709Z.json') and '/30/' in _c: continue","if _c.endswith('1803Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T1608Z'  # 1709Z: news/money/science last read in 1608Z","_last = '2026-10-30T1709Z'  # 1803Z: culture/sports/online last read in 1709Z")
R("not in requests/plan.json for 2026-10-30T17Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T18Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T17Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T18Z (desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T17Z","6 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T18Z, in its order and in batches of 100 (388 ids; the plan\\'s note: \"50 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 13 flat posts wait for their sixth run\"; its left_out counts 13 slowed, 0 over cap and 1 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: the plan\\'s 3 reads by id: 100 unread first-hop references (100 returned), then the last 31 first-hop (30 returned), then 29 second-hop (28 returned); 13 third-hop references left unread for want of reads); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#BBLC\", \"NBA Cup\" and \"Ochai Agbaji\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 1709Z; \"Halloween\" is one event with \"Happy Halloween\", read in 1507Z; \"#BBLC\" returned only 4 old posts on Intel chip samples); desks politics/world/justice/markets/ai/tech/medicine/entertainment/music/gaming/sports/internet/offbeat; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (1709Z used \"what\" and \"the\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T19:00:00Z, end_time 2026-10-30T18:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-23T19:00Z to 2026-10-30T17:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T06:00:00Z (the post\\'s creation minute) and end_time 2026-10-30T06:20:00Z: (conversation_id:2116047608036888796 is:reply) and (quotes_of_tweet_id:2116047608036888796 -is:retweet); the plan gives context.top two reads, so one post: 2116047608036888796 (@elonmusk \"It would be game over for America\", the biggest post new this run under 24 hours old at about 4.1M views); no replies and 17 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (12:09 PM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (1:03 PM CT Oct 30 / 18:03 UTC Oct 30, the 18Z slot; band allowance 42): requests/plan.json is for 2026-10-30T18Z (written 17:17Z after the 1709Z capture), so it was followed (37 reads listed) top to bottom; screen used its 3 reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 388 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 13 slowed flat posts and 1 unavailable in its left_out were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (the thirteen the plan lists; the other 6 not due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#BBLC", "NBA Cup" and "Ochai Agbaji" (3 reads). rising.global: quote stream "the" and repost stream "this" (2 reads). context.top: elonmusk 2116047608036888796 (2 reads). '
            f'Screen: 3 reads by id (100 unread references, then the last 31 first-hop, then 29 second-hop; 13 third-hop references left unread). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T17Z',","'plan': '2026-10-30T18Z',")
R("    'context': [{'post_id': '2115927574329057714',","    'context': [{'post_id': '2116047608036888796',")
R("f'{REPO}/capture/2026/10/30/1709Z.json'","f'{REPO}/capture/2026/10/30/1803Z.json'")
anchor="EXTRA_PRIVATE |= {'2115922312075653504'}  # 1709Z"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+open('skips1803.txt').read()+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
