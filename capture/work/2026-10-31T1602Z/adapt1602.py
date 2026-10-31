s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    assert s.count(start)>=1,start
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/31/1500Z.json from saved','"""Build capture/2026/10/31/1602Z.json from saved')
R("capture/work/2026-10-31T1500Z'","capture/work/2026-10-31T1602Z'")
R("RUN_ID = '2026-10-31T1500Z'","RUN_ID = '2026-10-31T1602Z'")
L("STARTED = ","STARTED = '2026-10-31T16:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T16:03:00Z'")
R("READS_BEFORE = 562","READS_BEFORE = 534")
L("READS_USED = 28","READS_USED = 42  # 1602Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 534 to 492; no 429 or 503 refusals")
R("datetime(2026,10,31,15,2,tzinfo=timezone.utc).timestamp()  # 1500Z (","datetime(2026,10,31,16,3,tzinfo=timezone.utc).timestamp()  # 1602Z (1500Z used 15:02, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',  # 1500Z: four watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1500Z: three screen reads; no request asked\n    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 1602Z: seven watch reads; screen cut by the plan; no request asked\n    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',\n")
R("    'trend_halloween': 'trend_halloween.txt', 'trend_poland': 'trend_poland.txt', 'trend_manutd': 'trend_manutd.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_mrfanboy': 'trend_mrfanboy.txt', 'trend_pikmin': 'trend_pikmin.txt', 'trend_ocon': 'trend_ocon.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 1602Z: all 19 desks, as the plan for 2026-10-31T16Z lists")
R("""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_halloween','trend.Happy Halloween'),('trend_poland','trend.Poland'),('trend_manutd','trend.Manchester United'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_mrfanboy','trend.#MrFanboyEP10'),('trend_pikmin','trend.Pikmin'),('trend_ocon','trend.Ocon'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x) in ('trend.#MrFanboyEP10','trend.MR FANBOY CHAPTER 10'): return 'entertainment'  # 1602Z: Thai series Mr Fanboy episode 10, one event\n        if str(_x)=='trend.Pikmin': return 'gaming'  # 1602Z: Nintendo's Pikmin\n        if str(_x)=='trend.Ocon': return 'sports'  # 1602Z: Haas replaces Esteban Ocon with Ryo Hirakawa for the Mexico City Grand Prix\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1602Z: replies to elonmusk 2116523818449805452 in its first 20 minutes (25 returned, the three most liked kept)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1602Z: quotes in the window (25 returned, the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['2116523818449805452'] + CTX_REPLIES + CTX_QUOTES  # 1602Z: the context post itself; 25 replies and 25 quotes returned")
R("DESK_OVERRIDE_RUN.update({_x:'sports' for _x in ['2116379133672612201']+CTXR+CTXQ})  # 1500Z: warriors Curry three and its context replies and quotes are sports",
  "DESK_OVERRIDE_RUN.update({_x:'sports' for _x in ['2116379133672612201']})  # 1500Z: warriors Curry three is sports\nDESK_OVERRIDE_RUN.update({_x:'science' for _x in ['2116523818449805452']+CTXR+CTXQ})  # 1602Z: elonmusk SpaceX 700 Falcon 9 flights post and its context replies and quotes are science")
R("if _c.endswith('1500Z.json') and '/31/' in _c: continue","if _c.endswith('1602Z.json') and '/31/' in _c: continue")
R("for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):  # noqa keep")
R("for batch in ('watch0','watch1','watch2','watch3'):\n","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):\n")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T1400Z'  # 1500Z: news/money/science last read in 1400Z","_last = '2026-10-31T1500Z'  # 1602Z: culture/sports/online last read in 1500Z")
R("not in requests/plan.json for 2026-10-31T15Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T16Z (rotation: news/money/science this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T15Z (day band, allowance 42)","cut by requests/plan.json for 2026-10-31T16Z (day band, allowance 42)")
s=s.replace("not due in requests/plan.json for 2026-10-31T15Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T16Z (desks_not_due)")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T15Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T16Z, in its order and in batches of 100 (685 ids; its left_out counts 91 slowed, 0 over cap and 4 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#MrFanboyEP10\", \"Pikmin\" and \"Ocon\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; of the top ten US names, Halloween is one event with Happy Halloween and Martinez, Manchester United, #CHEMUN and Lavia are one event, Chelsea 2-0 Manchester United, both with posts attached in 1500Z; #MrFanboyEP10 and MR FANBOY CHAPTER 10 are one event; Ocon is 11th and was read in place of the repeat events); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"is\" and \"you\" (1500Z used \"the\" and \"this\"), each quoted so X does not reject a bare stopword: (\"is\" lang:en is:quote -is:retweet), (\"you\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T17:00:00Z, end_time 2026-10-31T16:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T17:00Z to 2026-10-31T15:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-31T13:32:00Z (the post\\'s creation minute) and end_time 2026-10-31T13:52:00Z: (conversation_id:2116523818449805452 is:reply) and (quotes_of_tweet_id:2116523818449805452 -is:retweet); the plan gives context.top two reads, so one post: 2116523818449805452 (elonmusk \"Congrats to the @SpaceX team on over 700 Falcon 9 flights!\", 974K views, the biggest new post under 24 hours once a likely-paid iPhone post and a non-English screenshot post about another user are passed over); 25 replies and 25 quotes in the window, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
a=s.index("            f'Day-band run (11:00 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Day-band run (12:02 PM EDT Oct 31 / 16:02 UTC Oct 31, the 16Z slot; band allowance 42): requests/plan.json is for 2026-10-31T16Z (written 15:08Z after the 1500Z run) and was followed top to bottom (42 reads listed, screen cut). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1500Z and this run, the counter was 534 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 685 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 91 slowed flat posts and 4 unavailable posts in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#MrFanboyEP10" (entertainment: Thai series episode, one event with MR FANBOY CHAPTER 10), "Pikmin" (gaming) and "Ocon" (sports: Haas puts Ryo Hirakawa in for Esteban Ocon in Mexico City) (3 reads). rising.global: quote stream "is" and repost stream "you" (2 reads). context.top: elonmusk 2116523818449805452 (2 reads; 25 replies and 25 quotes in the 20-minute window). '
            f'Screen: cut by the plan; unread references left unread. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T15Z',","'plan': '2026-10-31T16Z',")
R("    'context': [{'post_id': '2116379133672612201',","    'context': [{'post_id': '2116523818449805452',")
R("f'{REPO}/capture/2026/10/31/1500Z.json'","f'{REPO}/capture/2026/10/31/1602Z.json'")
open('build_capture.py','w').write(s); print('ok')
s=open('build_capture.py').read()
i=s.index("DESK_OVERRIDE_RUN.update({'2116534734763458792':'sports'"); j=s.index("\n",i)+1
add = """skip_nsfw |= {'2116401780644868516','2116440041966952853','2116452007661678836','2116414720034931015'}  # 1602Z: likely paid (engr_imm iPhone post reusing tophz_'s photo, 2,220 likes on 1.1M views; ImRossyRibon 'find her father' picture bait, 457 likes on 706K; TheLaw3210 photo reply to grok, 1,211 likes on 772K; abdoulllmuhd CEO/resigning story, 902 likes on 580K)
EXTRA_PRIVATE |= {'2116510470408704149','2116373577691705625'}  # 1602Z: matsutakinoko screenshots of a mutual's posts (not a public figure); Chase_Sithole clip of an unnamed young man questioning a president (not a public figure)
DESK_OVERRIDE_RUN.update({'2116517088869192115':'world','2116543047882174662':'world','2116517338451227113':'sports','2116408184634282470':'sports','2116531181785326020':'entertainment','2116255362844389671':'internet','2115974183872270600':'sports','2116379637215367622':'gaming','2116530550831780131':'politics','2116510470408704149':'internet'})  # 1602Z: desk fixes (KemiBadenoch slavery-history post and elonmusk 'Well said' quoting it are UK politics; OfficialFPL Nicolas Jackson transfers and BCCI Jaipur storm clip are sports; Suriya_offl film #Scene; Cjdeck1 laid off in a hotdog costume; HoustonComets relaunch; GenshinImpact Flins birthday; elonmusk on Talarico; matsutakinoko screenshot post)
"""
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s); print('ok2')
