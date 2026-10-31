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
R('"""Build capture/2026/10/31/0003Z.json from saved','"""Build capture/2026/10/31/0102Z.json from saved')
R("capture/work/2026-10-31T0003Z'","capture/work/2026-10-31T0102Z'")
R("RUN_ID = '2026-10-31T0003Z'","RUN_ID = '2026-10-31T0102Z'")
L("STARTED = ","STARTED = '2026-10-31T01:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T01:03:00Z'")
R("READS_BEFORE = 1000","READS_BEFORE = 958")
L("READS_USED = 42","READS_USED = 28  # 0102Z: this run's 28 X calls (watch 5, trends 2, desks 4, sensors 3, viral.global 3, rising.global 2, volume 5, context.top 2, screen 2); the counter fell 958 to 930; no 429 or 503 refusals")
R("datetime(2026,10,31,0,4,tzinfo=timezone.utc).timestamp()  # 0003Z (","datetime(2026,10,31,1,3,tzinfo=timezone.utc).timestamp()  # 0102Z (0003Z used 00:04, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 0003Z: seven watch reads; screen cut by the plan; no request asked\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',  # 0102Z: five watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',  # 0102Z: two screen reads; no request asked\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
R("    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',","    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',")
R("    'trend_halloween': 'trend_halloween.txt', 'trend_nbacup': 'trend_nbacup.txt', 'trend_stevens': 'trend_stevens.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_smackdown': 'trend_smackdown.txt', 'trend_emmys': 'trend_emmys.txt', 'trend_wade': 'trend_wade.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world','defense'","DUE = ['politics','entertainment','sports','internet']  # 0102Z: the four hourly desks the plan for 2026-10-31T01Z lists")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_halloween','trend.Halloween'),('trend_nbacup','trend.NBA Cup'),('trend_stevens','trend.Stevens'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_smackdown','trend.#SmackDown'),('trend_emmys','trend.#DaytimeEmmys'),('trend_wade','trend.Dean Wade'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x)=='trend.Halloween': return 'life'  # 0003Z: Halloween costume and greeting posts\n",
  "        if str(_x)=='trend.Halloween': return 'life'  # 0003Z: Halloween costume and greeting posts\n        if str(_x)=='trend.#SmackDown': return 'sports'  # 0102Z: WWE SmackDown tonight\n        if str(_x)=='trend.#DaytimeEmmys': return 'entertainment'  # 0102Z: the Daytime Emmy Awards\n        if str(_x)=='trend.Dean Wade': return 'sports'  # 0102Z: Dean Wade on a handshake with LeBron James\n")
L("REQ_PICKS = {}","REQ_PICKS = {}  # 0102Z: no request asked (none open and unanswered)")
R("CTX_REPLIES = CTXR  # 0003Z: replies to pj_sekai 2116165917382255047 in its first 20 minutes (7 returned)",
  "CTX_REPLIES = CTXR  # 0102Z: replies to AarushYadav47 2116198463847408066 in its first 20 minutes (25 returned)")
R("CTX_IDS = ['2116165917382255047'] + CTX_REPLIES","CTX_IDS = ['2116198463847408066'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'gaming' for _x in ['2116165917382255047']+CTXR+CTXQ})  # 0003Z:",
  "DESK_OVERRIDE_RUN.update({_x:'gaming' for _x in ['2116165917382255047']})\nDESK_OVERRIDE_RUN.update({_x:'tech' for _x in ['2116198463847408066']+CTXR+CTXQ})  # 0102Z: AarushYadav47 Subvocal glasses raise post and its context replies and quotes are tech  # 0003Z:")
R("if _c.endswith('0003Z.json') and '/31/' in _c: continue","if _c.endswith('0102Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T2301Z'  # 0003Z: culture/sports/online last read in 2301Z","_last = '2026-10-31T0003Z'  # 0102Z: news/money/science last read in 0003Z")
R("not in the plan for 2026-10-31T00Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T01Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in the plan for 2026-10-31T00Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-31T01Z (desks_not_due)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of the plan for 2026-10-31T00Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T01Z, in its order and in batches of 100 (478 ids; its left_out counts 24 slowed and 0 over cap, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 2 reads by id, 92 unread first-hop references (1 Not Found) then 16 second-hop references (1 Not Found); the plan allows 3); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#SmackDown\", \"#DaytimeEmmys\" and \"Dean Wade\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0003Z; Halloween, Kucherov and Stevens were read in 0003Z/2301Z, Sam Altman in 2202Z, and Poland/Tusk/Polish are the Constitutional Tribunal event already attached); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"and\" and \"my\" (0003Z used \"is\" and \"you\"), each quoted so X does not reject a bare stopword: (\"and\" lang:en is:quote -is:retweet), (\"my\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T02:00:00Z, end_time 2026-10-31T01:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-24T02:00Z to 2026-10-31T00:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T16:00:00Z (the post\\'s creation minute) and end_time 2026-10-30T16:20:00Z: (conversation_id:2116198463847408066 is:reply) and (quotes_of_tweet_id:2116198463847408066 -is:retweet); the plan gives context.top two reads, so one post: 2116198463847408066 (@AarushYadav47 post on a $1.3M raise for Subvocal glasses, the biggest post new this run under 24 hours old at about 6.41M views); 25 replies and 23 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (8:03 PM EDT","media descriptions. '\n",
"""            f'Day-band run (9:02 PM EDT Oct 30 / 01:02 UTC Oct 31, the 01Z slot; band allowance 42): requests/plan.json is for 2026-10-31T01Z (written 00:11Z after the 0003Z run) and was followed top to bottom (29 reads listed; screen used 2 of its 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 478 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 24 slowed flat posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "#SmackDown", "#DaytimeEmmys" and "Dean Wade" (3 reads). rising.global: quote stream "and" and repost stream "my" (2 reads). context.top: AarushYadav47 2116198463847408066 (2 reads). '
            f'Screen: 2 reads by id (92 unread first-hop references, then 16 second-hop; 1 Not Found each). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T00Z',","'plan': '2026-10-31T01Z',")
R("    'context': [{'post_id': '2116165917382255047',","    'context': [{'post_id': '2116198463847408066',")
R("f'{REPO}/capture/2026/10/31/0003Z.json'","f'{REPO}/capture/2026/10/31/0102Z.json'")
open('build_capture.py','w').write(s)
print('ok')
# (applied after first test build) dedupe watch_unavailable
# then: EXTRA_PRIVATE line for 2115965600069452153, 2116022244954771889
# then: context dropped (AarushYadav47 post left out as likely promoted in 1803Z)
