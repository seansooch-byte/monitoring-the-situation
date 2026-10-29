s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("2001Z.json from saved","2109Z.json from saved")
R("capture/work/2026-10-29T2001Z'","capture/work/2026-10-29T2109Z'")
R("RUN_ID = '2026-10-29T2001Z'","RUN_ID = '2026-10-29T2109Z'")
R("STARTED = '2026-10-29T20:01:00Z'","STARTED = '2026-10-29T21:09:00Z'")
R("OBS_AT = '2026-10-29T20:02:00Z'","OBS_AT = '2026-10-29T21:10:00Z'")
R("READS_BEFORE = 415","READS_BEFORE = 373")
SPAN("READS_USED = 42","\n","READS_USED = 29  # 2109Z: this run's 29 X calls (watch 5, desks 5, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 2); the counter fell 373 to 344; no 429 or 503 refusals\n")
R("datetime(2026,10,29,20,2,tzinfo=timezone.utc).timestamp()  # 2001Z (","datetime(2026,10,29,21,10,tzinfo=timezone.utc).timestamp()  # 2109Z (2001Z used 20:02, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_patrickstewart': 'trend_patrickstewart.txt', 'trend_professorx': 'trend_professorx.txt', 'trend_captainpicard': 'trend_captainpicard.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',
    'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_doomsday': 'trend_doomsday.txt', 'trend_americandad': 'trend_americandad.txt', 'trend_averybullock': 'trend_averybullock.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
SPAN("DUE = ['politics','world'","\n","DUE = ['politics','entertainment','sports','internet','life']  # 2109Z: the 5 desks the plan for 2026-10-29T21Z lists\n")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_patrickstewart','trend.Patrick Stewart'),('trend_professorx','trend.Professor X'),('trend_captainpicard','trend.Captain Picard'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_doomsday','trend.Doomsday'),('trend_americandad','trend.American Dad'),('trend_averybullock','trend.Avery Bullock'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) in ('trend.Patrick Stewart','trend.Professor X','trend.Captain Picard'): return 'entertainment'  # 2001Z""","""        if str(_x) in ('trend.Doomsday','trend.American Dad','trend.Avery Bullock'): return 'entertainment'  # 2109Z: Patrick Stewart's death (his Avengers: Doomsday role and Avery Bullock on American Dad)
        if str(_x) in ('trend.Patrick Stewart','trend.Professor X','trend.Captain Picard'): return 'entertainment'  # 2001Z""")
R("('watch0','watch1','watch2','watch3','watch4','watch5','watch6')","('watch0','watch1','watch2','watch3','watch4')",2)
R("if _c.endswith('2001Z.json') and '/29/' in _c: continue","if _c.endswith('2109Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-29T1906Z'  # 2001Z: culture/sports/online last read in 1906Z","_last = '2026-10-29T2001Z'  # 2109Z: news/money/science last read in 2001Z")
R("not in requests/plan.json for 2026-10-29T20Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-29T21Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T20Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T21Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115911674771521628','2115911989083951219','2115912521244873186']  # 2109Z: replies to FabrizioRomano 2115907748164759702 in its first 20 minutes; relevancy returned 25 from 21:00Z to 21:03Z, the three most liked kept\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115911224508756171','2115911853696266462','2115912224443142592']  # 2109Z: quotes in the window, the three most liked kept\n")
R("CTX_IDS = ['2115893413233016885'] + CTX_REPLIES","CTX_IDS = ['2115907748164759702'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T20Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T21Z, in its order and in batches of 100 (500 ids; its left_out counts 241 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 2 reads by id, 97 unread references then 20 second-hop); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Doomsday\", \"American Dad\" and \"Avery Bullock\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 2001Z, skipping \"Patrick Stewart\", \"Star Trek\" and \"Ian McKellen\" (attached in 2001Z), \"#VetClaimsAI\" (looks promoted), and \"Game 7\", \"Larkin\" and \"Simmons\" as read in 1501Z to 1906Z; all three are the same event as Patrick Stewart\\'s death: his final role as Professor X in Avengers: Doomsday and his voice role as Avery Bullock on American Dad)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"and\" and \"my\" (2001Z used \"is\" and \"you\"), each quoted so X does not reject a bare stopword: (\"and\" lang:en is:quote -is:retweet), (\"my\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T22:00:00Z, end_time 2026-10-29T21:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas); each series is the 167 full hours 2026-10-22T22:00Z to 2026-10-29T20:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T20:44:00Z (the post\\'s creation minute) and end_time 2026-10-29T21:04:00Z: (conversation_id:2115907748164759702 is:reply) and (quotes_of_tweet_id:2115907748164759702 -is:retweet); the plan gives context.top two reads, so one post: 2115907748164759702 (@FabrizioRomano on the new Milan stadium naming deal, the biggest fresh post new this run at about 684K views in about 25 minutes); 25 replies and 25 quotes in the window (all from the last minutes of the window), the 3 most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (3:01 PM CT","f'Screen: cut by the plan; unread second-hop references left unread. '\n",
 "            f'Day-band run (4:09 PM CT Oct 29 / 21:09 UTC Oct 29, the 21Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T21Z, 30 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 500 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 241 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, entertainment, sports, internet and life, the 5 the plan lists (the other 14 not due). Volume: medicine, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Doomsday\", \"American Dad\" and \"Avery Bullock\" (3 reads, one event: Patrick Stewart\\'s death). rising.global: quote stream \"and\" and repost stream \"my\" (2 reads). context.top: FabrizioRomano 2115907748164759702 (2 reads). '\n"
 "            f'Screen: 2 reads by id (97 unread references, then 20 second-hop; the plan\\'s third screen read was not used). '\n")
R("'plan': '2026-10-29T20Z',","'plan': '2026-10-29T21Z',")
R("    'context': [{'post_id': '2115893413233016885',","    'context': [{'post_id': '2115907748164759702',")
R("capture/2026/10/29/2001Z.json'","capture/2026/10/29/2109Z.json'")
anchor="DESK_OVERRIDE_RUN.update({'2115893413233016885':'entertainment'"
i=s.index(anchor); j=s.index("\n",i)+1
ids=['2115907748164759702','2115911674771521628','2115911989083951219','2115912521244873186','2115911224508756171','2115911853696266462','2115912224443142592']
s=s[:j]+"DESK_OVERRIDE_RUN.update({"+",".join(f"'{x}':'sports'" for x in ids)+"})  # 2109Z: FabrizioRomano Milan stadium post and its context replies and quotes are sports\n"+s[j:]
i=s.index("_PS = ('Patrick Stewart'")
s=s[:i]+"_u = list(dict.fromkeys(x for _n in ('Doomsday','American Dad','Avery Bullock') for x in (trend_posts.get(_n) or [])))  # 2109Z: one event, Patrick Stewart's death\nif _u:\n    for _n in ('Doomsday','American Dad','Avery Bullock','Patrick Stewart','Star Trek','Ian McKellen','The Inner Light','Earl Grey','Green Room'): trend_posts[_n] = list(dict.fromkeys((trend_posts.get(_n) or []) + _u))\n"+s[i:]
a="skip_nsfw = set(json.load(open(f'{W}/exclude_ids.json')))\n"
R(a,a+"skip_nsfw |= {'2115783276107612331','2115909687597998414','2115419642919518541','2115452638745469206','2115421729648459944','2115376526191665261','2115743204607680907'}  # 2109Z: sexual promo posts from the 'my' repost stream (jessica56kh8, LivvyBaby_B_, AdrianLecblc, hamitburtpda, EAYTAVENi20l, Crueldomination, GoddesssVanuk)\n")
open('build_capture.py','w').write(s); print('ok')
