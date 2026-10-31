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
R('"""Build capture/2026/10/31/1700Z.json from saved','"""Build capture/2026/10/31/1802Z.json from saved')
R("capture/work/2026-10-31T1700Z'","capture/work/2026-10-31T1802Z'")
R("RUN_ID = '2026-10-31T1700Z'","RUN_ID = '2026-10-31T1802Z'")
L("STARTED = ","STARTED = '2026-10-31T18:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T18:03:00Z'")
R("READS_BEFORE = 492","READS_BEFORE = 462")
L("READS_USED = 30","READS_USED = 38  # 1802Z: this run's 38 X calls (watch 5, trends 2, desks 13, volume 5, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 462 to 424; no 429 or 503 refusals")
R("datetime(2026,10,31,17,1,tzinfo=timezone.utc).timestamp()  # 1700Z (","datetime(2026,10,31,18,3,tzinfo=timezone.utc).timestamp()  # 1802Z (1700Z used 17:01, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt',  # 1700Z: six watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1700Z: three screen reads; no request asked\n    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',  # 1802Z: five watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1802Z: three screen reads; no request asked\n    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',\n")
R("    'trend_brighton': 'trend_brighton.txt', 'trend_chrisash': 'trend_chrisash.txt', 'trend_navy': 'trend_navy.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_rutgers': 'trend_rutgers.txt', 'trend_iowa': 'trend_iowa.txt', 'trend_wisconsin': 'trend_wisconsin.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1802Z: the 13 desks the plan for 2026-10-31T18Z lists")
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_brighton','trend.Brighton'),('trend_chrisash','trend.Chris Ash'),('trend_navy','trend.Navy'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_rutgers','trend.Rutgers'),('trend_iowa','trend.Iowa'),('trend_wisconsin','trend.Wisconsin'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.Rutgers': return 'sports'  # 1802Z: Michigan vs Rutgers (Iowa and Wisconsin streams mix college football and Midwest politics, so no default)\n"+s[j:]
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 1802Z: replies to hiitotsu 2116421111433032050 in its first 20 minutes (0 returned)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 1802Z: quotes in the window (0 returned)")
L("CTX_IDS = [","CTX_IDS = ['2116421111433032050'] + CTX_REPLIES + CTX_QUOTES  # 1802Z: the context post itself; 0 replies and 0 quotes returned in the window")
R("DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116406440843780259']+CTXR+CTXQ})  # 1700Z: funny0ver__ aespa giselle lip-sync post (and any context replies and quotes) is music",
  "DESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116406440843780259']})  # 1700Z: funny0ver__ aespa giselle lip-sync post is music\nDESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116421111433032050']+CTXR+CTXQ})  # 1802Z: hiitotsu Music Core stage post (and any context replies and quotes) is music")
R("if _c.endswith('1700Z.json') and '/31/' in _c: continue","if _c.endswith('1802Z.json') and '/31/' in _c: continue")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3','watch4'):  # noqa keep")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):\n","for batch in ('watch0','watch1','watch2','watch3','watch4'):\n")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T1602Z'  # 1700Z: news/money/science last read in 1602Z","_last = '2026-10-31T1700Z'  # 1802Z: culture/sports/online last read in 1700Z")
R("not in requests/plan.json for 2026-10-31T17Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T18Z (rotation: news/money/science this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T17Z (day band, allowance 42)","cut by requests/plan.json for 2026-10-31T18Z (day band, allowance 42)")
s=s.replace("not due in requests/plan.json for 2026-10-31T17Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T18Z (desks_not_due)")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T17Z","6 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T18Z, in its order and in batches of 100 (420 ids; its left_out counts 11 slowed, 0 over cap and 2 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 134 unread first-hop references in two reads, 133 returned and 1 not found, then 24 second-hop references, all returned; 7 third-hop references left unread); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Rutgers\", \"Iowa\" and \"Wisconsin\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1700Z; Halloween and Poland are repeat events, Brighton, Chris Ash and Navy were read in 1700Z, Fickell and Badgers are the Wisconsin game); desks politics/world/justice/markets/ai/tech/medicine/entertainment/music/gaming/sports/internet/offbeat; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"it\" and \"that\" (1700Z used \"and\" and \"my\"), each quoted so X does not reject a bare stopword: (\"it\" lang:en is:quote -is:retweet), (\"that\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T19:00:00Z, end_time 2026-10-31T18:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T19:00Z to 2026-10-31T17:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-31T06:44:00Z (the post\\'s creation minute) and end_time 2026-10-31T07:04:00Z: (conversation_id:2116421111433032050 is:reply) and (quotes_of_tweet_id:2116421111433032050 -is:retweet); the plan gives context.top two reads, so one post: 2116421111433032050 (hiitotsu post on a Music Core stage, 4.32M views; the bigger KP_Aashish Anantapur school chainsaw-attack post, 4.72M views, was passed over and left out as graphic: blood on the classroom floor and identifiable children); both searches returned 0 posts in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
a=s.index("            f'Day-band run (1:00 PM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Day-band run (1:02 PM CDT Oct 31 / 18:02 UTC Oct 31, the 18Z slot; band allowance 42): requests/plan.json is for 2026-10-31T18Z (written 17:08Z after the 1700Z run) and was followed top to bottom (38 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1700Z and this run, the counter was 462 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 420 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 11 slowed flat posts and 2 unavailable posts in its left_out were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (the 13 due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Rutgers" (sports: Michigan vs Rutgers), "Iowa" and "Wisconsin" (college football mixed with Midwest politics) (3 reads). rising.global: quote stream "it" and repost stream "that" (2 reads). context.top: hiitotsu 2116421111433032050 (2 reads; 0 replies and 0 quotes in the 20-minute window). '
            f'Screen: 3 reads by id (134 unread first-hop references in two reads, 1 not found; then 24 second-hop, all returned; 7 third-hop left unread). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T17Z',","'plan': '2026-10-31T18Z',")
R("    'context': [{'post_id': '2116406440843780259',","    'context': [{'post_id': '2116421111433032050',")
R("f'{REPO}/capture/2026/10/31/1700Z.json'","f'{REPO}/capture/2026/10/31/1802Z.json'")
i=s.index("DESK_OVERRIDE_RUN.update({'2116187307506057283':'defense'"); j=s.index("\n",i)+1
s=s[:j]+"""skip_nsfw |= {'2116021496753897681','2116288259722736104','2116527572536504499'}  # 1802Z: sexual (kentotero69 clip; IvoryLux2 possibly_sensitive nurse post; GumMuse AI adult ad, also likely paid)
skip_nsfw |= {'2116548579250905153','2115995256781197686'}  # 1802Z: likely paid (mcpmarkets $CREDIT token promo; Stake Drake win ad, 1,363 likes on 723K views)
skip_nsfw |= {'2116421086980276267'}  # 1802Z: graphic (KP_Aashish Anantapur school chainsaw attack: blood on the classroom floor, bloodied chainsaw, children's faces)
"""+s[j:]
open('build_capture.py','w').write(s); print('ok')
