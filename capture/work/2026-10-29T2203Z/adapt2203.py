s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("2109Z.json from saved","2203Z.json from saved")
R("capture/work/2026-10-29T2109Z'","capture/work/2026-10-29T2203Z'")
R("RUN_ID = '2026-10-29T2109Z'","RUN_ID = '2026-10-29T2203Z'")
R("STARTED = '2026-10-29T21:09:00Z'","STARTED = '2026-10-29T22:03:00Z'")
R("OBS_AT = '2026-10-29T21:10:00Z'","OBS_AT = '2026-10-29T22:04:00Z'")
R("READS_BEFORE = 373","READS_BEFORE = 344")
SPAN("READS_USED = 29","\n","READS_USED = 37  # 2203Z: this run's 37 X calls (watch 4, desks 13, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 344 to 307; no 429 or 503 refusals\n")
R("datetime(2026,10,29,21,10,tzinfo=timezone.utc).timestamp()  # 2109Z (","datetime(2026,10,29,22,4,tzinfo=timezone.utc).timestamp()  # 2203Z (2109Z used 21:10, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',
    'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_doomsday': 'trend_doomsday.txt', 'trend_americandad': 'trend_americandad.txt', 'trend_averybullock': 'trend_averybullock.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_binance': 'trend_binance.txt', 'trend_startrek': 'trend_startrek.txt', 'trend_larkin': 'trend_larkin.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
SPAN("DUE = ['politics','entertainment'","\n","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 2203Z: the 13 desks the plan for 2026-10-29T22Z lists\n")
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_doomsday','trend.Doomsday'),('trend_americandad','trend.American Dad'),('trend_averybullock','trend.Avery Bullock'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_binance','trend.Binance'),('trend_startrek','trend.Star Trek'),('trend_larkin','trend.Larkin'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) in ('trend.Doomsday','trend.American Dad','trend.Avery Bullock'): return 'entertainment'  # 2109Z""","""        if str(_x) in ('trend.Binance','trend.SAFU'): return 'markets'  # 2203Z: Binance hack (CZ: 'It does look like a hack on Binance'; Tether froze USDT; SAFU is the same event)
        if str(_x) == 'trend.Star Trek': return 'entertainment'  # 2203Z: Patrick Stewart's death
        if str(_x) in ('trend.Doomsday','trend.American Dad','trend.Avery Bullock'): return 'entertainment'  # 2109Z""")
R("('watch0','watch1','watch2','watch3','watch4')","('watch0','watch1','watch2','watch3')",2)
R("if _c.endswith('2109Z.json') and '/29/' in _c: continue","if _c.endswith('2203Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T2001Z'  # 2109Z: news/money/science last read in 2001Z","_last = '2026-10-29T2109Z'  # 2203Z: culture/sports/online last read in 2109Z")
R("not in requests/plan.json for 2026-10-29T21Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-29T22Z (rotation: news/money/science this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T21Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T22Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['politics','sports','internet','life','offbeat']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115920284553511137','2115920281151603024','2115920356791734373']  # 2203Z: replies to cz_binance 2115915423174853077 in its first 20 minutes; relevancy returned 25 from 21:34:36Z to 21:34:59Z, the three most liked kept\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115920292547870981','2115920235584962970','2115920340522320203']  # 2203Z: quotes in the window, the three most liked kept\n")
R("CTX_IDS = ['2115907748164759702'] + CTX_REPLIES","CTX_IDS = ['2115915423174853077'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T21Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T22Z, in its order and in batches of 100 (359 ids; its left_out counts 11 slowed flat posts and 1 unavailable post not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 141 unread references then 21 second-hop); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Binance\", \"Star Trek\" and \"Larkin\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; \"Binance\" is new in the top ten (the Binance hack; \"SAFU\" is the same event); \"Star Trek\" and \"Larkin\" had no posts attached in 2109Z; skipping \"Patrick Stewart\" (same event as Star Trek), \"Doomsday\" and \"American Dad\" (attached in 2109Z), \"#VetClaimsAI\" (looks promoted), and \"Game 7\", \"Ian McKellen\" and \"Simmons\" (read in earlier runs today))',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"that\" and \"just\" (2109Z used \"and\" and \"my\"), each quoted so X does not reject a bare stopword: (\"that\" lang:en is:quote -is:retweet), (\"just\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T23:00:00Z, end_time 2026-10-29T22:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.sports, volume.internet, volume.life, volume.offbeat); each series is the 167 full hours 2026-10-22T23:00Z to 2026-10-29T21:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T21:15:00Z (the post\\'s creation minute) and end_time 2026-10-29T21:35:00Z: (conversation_id:2115915423174853077 is:reply) and (quotes_of_tweet_id:2115915423174853077 -is:retweet); the plan gives context.top two reads, so one post: 2115915423174853077 (@cz_binance saying it looks like a hack on Binance, the biggest fresh post new this run at about 1.3M views in about 50 minutes); 25 replies and 25 quotes in the window (all from the last minute of the window), the 3 most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (4:09 PM CT","f'Screen: 2 reads by id (97 unread references, then 20 second-hop; the plan\\'s third screen read was not used). '\n",
 "            f'Day-band run (5:03 PM CT Oct 29 / 22:03 UTC Oct 29, the 22Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T22Z, 37 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 359 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 11 slowed flat posts and the 1 standing unavailable post are in its left_out and were not read. '\n"
 "            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat, the 13 the plan lists (the other 6 not due). Volume: politics, sports, internet, life and offbeat (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Binance\", \"Star Trek\" and \"Larkin\" (3 reads: the Binance hack, Patrick Stewart\\'s death, and the Red Wings suspending Dylan Larkin). rising.global: quote stream \"that\" and repost stream \"just\" (2 reads). context.top: cz_binance 2115915423174853077 (2 reads). '\n"
 "            f'Screen: 3 reads by id (141 unread references in two reads, then 21 second-hop). '\n")
R("'plan': '2026-10-29T21Z',","'plan': '2026-10-29T22Z',")
R("    'context': [{'post_id': '2115907748164759702',","    'context': [{'post_id': '2115915423174853077',")
R("capture/2026/10/29/2109Z.json'","capture/2026/10/29/2203Z.json'")
anchor="DESK_OVERRIDE_RUN.update({'2112984664256241837':'ai'"
i=s.index(anchor); j=s.index("\n",i)+1
ids=['2115915423174853077','2115920284553511137','2115920281151603024','2115920356791734373','2115920292547870981','2115920235584962970','2115920340522320203']
s=s[:j]+"DESK_OVERRIDE_RUN.update({"+",".join(f"'{x}':'markets'" for x in ids)+"})  # 2203Z: cz_binance hack post and its context replies and quotes are markets (crypto)\n"+s[j:]
i=s.index("_u = list(dict.fromkeys(x for _n in ('Doomsday'")
s=s[:i]+"_u = list(dict.fromkeys(x for _n in ('Binance','SAFU') for x in (trend_posts.get(_n) or [])))  # 2203Z: one event, the Binance hack\nif _u:\n    for _n in ('Binance','SAFU'): trend_posts[_n] = list(dict.fromkeys((trend_posts.get(_n) or []) + _u))\n_u = list(dict.fromkeys(x for _n in ('Star Trek',) for x in (trend_posts.get(_n) or [])))  # 2203Z: Star Trek is Patrick Stewart's death\nif _u:\n    for _n in ('Patrick Stewart','Star Trek','Ian McKellen','The Inner Light','Earl Grey','Green Room'): trend_posts[_n] = list(dict.fromkeys((trend_posts.get(_n) or []) + _u))\n"+s[i:]
open('build_capture.py','w').write(s); print('ok')
# second pass
s=open('build_capture.py').read()
R("skip_nsfw = set(json.load(open(f'{W}/exclude_ids.json')))\n","skip_nsfw = set(json.load(open(f'{W}/exclude_ids.json')))\nskip_nsfw |= {'2115743367569281252','2115473657447260249'}  # 2203Z: sexual text (tnhi43274 bestiality claim video; HoopsCrave 'duration of sex in GTA 6')\n")
anchor="DESK_OVERRIDE_RUN.update({'2115915423174853077':'markets'"
i=s.index(anchor); j=s.index("\n",i)+1
s=s[:j]+"DESK_OVERRIDE_RUN.update({'2115922259739349132':'markets','2115904721856651382':'markets','2115761060569342111':'justice','2115650841269207108':'politics'})  # 2203Z: WatcherGuru and spreekaway Binance hack posts are markets; LongTimeHistory police-beating video is justice; vincedmonroy rally protesters supercut is politics\n"+s[j:]
open('build_capture.py','w').write(s); print('ok2')
