s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1906Z.json from saved","2001Z.json from saved")
R("capture/work/2026-10-29T1906Z'","capture/work/2026-10-29T2001Z'")
R("RUN_ID = '2026-10-29T1906Z'","RUN_ID = '2026-10-29T2001Z'")
R("STARTED = '2026-10-29T19:06:00Z'","STARTED = '2026-10-29T20:01:00Z'")
R("OBS_AT = '2026-10-29T19:07:00Z'","OBS_AT = '2026-10-29T20:02:00Z'")
R("READS_BEFORE = 441","READS_BEFORE = 415")
SPAN("READS_USED = 26","\n","READS_USED = 42  # 2001Z: this run's 42 X calls (watch 7, desks 18, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 415 to 373; no 429 or 503 refusals\n")
R("datetime(2026,10,29,19,7,tzinfo=timezone.utc).timestamp()  # 1906Z (","datetime(2026,10,29,20,2,tzinfo=timezone.utc).timestamp()  # 2001Z (1906Z used 19:07, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_game7': 'trend_game7.txt', 'trend_24weeks': 'trend_24weeks.txt', 'trend_allishagray': 'trend_allishagray.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_patrickstewart': 'trend_patrickstewart.txt', 'trend_professorx': 'trend_professorx.txt', 'trend_captainpicard': 'trend_captainpicard.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
SPAN("DUE = ['politics','entertainment'","\n","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','offbeat']  # 2001Z: the 18 desks the plan for 2026-10-29T20Z lists\n")
R("""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_game7','trend.Game 7'),('trend_24weeks','trend.2-4 WEEKS'),('trend_allishagray','trend.Allisha Gray'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_patrickstewart','trend.Patrick Stewart'),('trend_professorx','trend.Professor X'),('trend_captainpicard','trend.Captain Picard'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) in ('trend.Game 7','trend.Allisha Gray'): return 'sports'  # 1906Z""","""        if str(_x) in ('trend.Patrick Stewart','trend.Professor X','trend.Captain Picard'): return 'entertainment'  # 2001Z: Patrick Stewart has died at 86
        if str(_x) in ('trend.Game 7','trend.Allisha Gray'): return 'sports'  # 1906Z""")
R("('watch0','watch1','watch2','watch3')","('watch0','watch1','watch2','watch3','watch4','watch5','watch6')",2)
R("if _c.endswith('1906Z.json') and '/29/' in _c: continue","if _c.endswith('2001Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T1802Z'  # 1906Z: news/money/science last read in 1802Z","_last = '2026-10-29T1906Z'  # 2001Z: culture/sports/online last read in 1906Z")
R("not in the plan for 2026-10-29T19Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-29T20Z (rotation: news/money/science this run)")
R("reason = 'not due in the plan for 2026-10-29T19Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T20Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115897890833097102','2115897890417873186','2115897890124050756']  # 2001Z: replies to DiscussingFilm 2115893413233016885 in its first 20 minutes; relevancy returned only the newest 25, all with 0 likes, so the first three returned\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115897901989978550','2115897900870029665','2115897900006003031']  # 2001Z: quotes in the window, all 0 likes, the first three returned (benjaboyscott passed over for profanity)\n")
R("CTX_IDS = ['2115864946093305955'] + CTX_REPLIES","CTX_IDS = ['2115893413233016885'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of the plan for 2026-10-29T19Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T20Z, in its order and in batches of 100 (676 ids; its left_out counts 304 slowed flat posts and 9 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Patrick Stewart\", \"Professor X\" and \"Captain Picard\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1906Z, skipping \"Game 7\", \"2-4 WEEKS\", \"Simmons\", \"Larkin\", \"Bears\", \"Titans\" and \"#WNBAFinals\" as read in 1501Z to 1906Z; all three are one event, Sir Patrick Stewart has died at 86, the same event as \"Charles Xavier\", \"X-Men\" and \"Ian McKellen\")',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"is\" and \"you\" (1906Z used \"the\" and \"this\"), each quoted so X does not reject a bare stopword: (\"is\" lang:en is:quote -is:retweet), (\"you\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T21:00:00Z, end_time 2026-10-29T20:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science); each series is the 167 full hours 2026-10-22T21:00Z to 2026-10-29T19:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T19:47:00Z (the post\\'s creation minute) and end_time 2026-10-29T20:07:00Z: (conversation_id:2115893413233016885 is:reply) and (quotes_of_tweet_id:2115893413233016885 -is:retweet); the plan gives context.top two reads, so one post: 2115893413233016885 (@DiscussingFilm reporting Patrick Stewart has died at 86, the biggest fresh post new this run at about 486K views in about 17 minutes); 25 replies and 25 quotes in the window, all with 0 likes, the first 3 of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (2:06 PM CT","the plan\\'s third screen read was not used). '\n",
 "            f'Day-band run (3:01 PM CT Oct 29 / 20:01 UTC Oct 29, the 20Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T20Z, 42 reads, screen cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 676 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 304 slowed flat posts and the 9 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: all 18 the plan lists (life not due). Volume: markets, business, ai, tech and science (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Patrick Stewart\", \"Professor X\" and \"Captain Picard\" (3 reads, one event: Patrick Stewart has died at 86). rising.global: quote stream \"is\" and repost stream \"you\" (2 reads). context.top: DiscussingFilm 2115893413233016885 (2 reads). '\n"
 "            f'Screen: cut by the plan; unread second-hop references left unread. '\n")
R("'plan': '2026-10-29T19Z',","'plan': '2026-10-29T20Z',")
R("    'context': [{'post_id': '2115864946093305955',","    'context': [{'post_id': '2115893413233016885',")
R("capture/2026/10/29/1906Z.json'","capture/2026/10/29/2001Z.json'")
anchor="DESK_OVERRIDE_RUN.update({'2115864946093305955':'internet'"
i=s.index(anchor); j=s.index("\n",i)+1
add=("DESK_OVERRIDE_RUN.update({'2115893413233016885':'entertainment','2115897890833097102':'entertainment','2115897890417873186':'entertainment','2115897890124050756':'entertainment','2115897901989978550':'entertainment','2115897900870029665':'entertainment','2115897900006003031':'entertainment'})  # 2001Z: DiscussingFilm Patrick Stewart death post and its context replies and quotes are entertainment\n")
s=s[:j]+add+s[j:]
i=s.index("_G7 = ('Game 7'")
s=s[:i]+"_PS = ('Patrick Stewart','Professor X','Captain Picard','Charles Xavier','X-Men','Ian McKellen')  # 2001Z: one event, Patrick Stewart has died at 86\n_u = list(dict.fromkeys(x for _n in ('Patrick Stewart','Professor X','Captain Picard') for x in (trend_posts.get(_n) or [])))\nif _u:\n    for _n in _PS: trend_posts[_n] = list(dict.fromkeys((trend_posts.get(_n) or []) + _u))\n"+s[i:]
open('build_capture.py','w').write(s); print('ok')
