p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1611Z.json from saved','capture/2026/10/28/1702Z.json from saved')
R("work/2026-10-28T1611Z'","work/2026-10-28T1702Z'")
R("RUN_ID = '2026-10-28T1611Z'","RUN_ID = '2026-10-28T1702Z'")
R("STARTED = '2026-10-28T16:11:00Z'","STARTED = '2026-10-28T17:02:00Z'")
R("OBS_AT = '2026-10-28T16:12:00Z'","OBS_AT = '2026-10-28T17:03:00Z'")
R("READS_BEFORE = 569","READS_BEFORE = 527")
a=s.index("READS_USED = 42  # 1611Z"); b=s.index("\n",a)
s=s[:a]+"READS_USED = 31  # 1702Z: this run's 31 X calls (the plan's 32 reads less one unused screening read); the counter fell 527 to 496; no 429 or 503 refusals"+s[b:]
R("datetime(2026,10,28,16,12,tzinfo=timezone.utc).timestamp()  # 1611Z (1511Z used 15:12, ","datetime(2026,10,28,17,3,tzinfo=timezone.utc).timestamp()  # 1702Z (1611Z used 16:12, 1511Z used 15:12, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',
    'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_huerta': 'trend_huerta.txt', 'trend_fomc': 'trend_fomc.txt', 'trend_tucker': 'trend_tucker.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_selena': 'trend_selena.txt', 'trend_downs': 'trend_downs.txt', 'trend_robinson': 'trend_robinson.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):",2)
a=s.index("DUE = ['politics','world'"); b=s.index("\n",a)
s=s[:a]+"DUE = ['politics','entertainment','ideas','sports','internet','life']  # 1702Z: the 6 desks requests/plan.json for 2026-10-28T17Z lists (the four hourly desks plus ideas and life, every 4 h)"+s[b:]
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_huerta','trend.Dolores Huerta'),('trend_fomc','trend.FOMC'),('trend_tucker','trend.Justin Tucker'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_selena','trend.Selena'),('trend_downs','trend.Josh Downs'),('trend_robinson','trend.Tommy Robinson'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("""        if str(_x) == 'trend.Dolores Huerta': return 'politics'  # 1611Z""","""        if str(_x) == 'trend.Selena': return 'entertainment'  # 1702Z: Selena Gomez and Demi Lovato recreating the Princess Protection Program poster ("Princess Protection Program" and "Demi Lovato" on the US list are the same event)
        if str(_x) == 'trend.Josh Downs': return 'sports'  # 1702Z: Colts WR Josh Downs requests a trade
        if str(_x) == 'trend.Tommy Robinson': return 'justice'  # 1702Z: Tommy Robinson found guilty (UK criminal trial)
        if str(_x) == 'trend.Dolores Huerta': return 'politics'  # 1611Z""")
R("if _c.endswith('1611Z.json') and '/28/' in _c: continue","if _c.endswith('1702Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T16Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T17Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"325 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 230 flat posts wait for their sixth run\"; its left_out also counts 5 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 8 reads; fields","{len(watch_unavailable)} unavailable, 6 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Selena", "Josh Downs" and "Tommy Robinson" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the three highest of the top-ten US names that had no posts attached in 1611Z ("Dolores Huerta", "Justin Tucker", "FOMC", "Butker" and "United Farm Workers" had posts in 1611Z, "El Toledo" is the Toledo train collision streamed in 1511Z, "Alvin Hellerstein" was left for a later run); "Selena" is Selena Gomez and Demi Lovato recreating the Princess Protection Program poster ("Princess Protection Program" and "Demi Lovato" are the same event), "Josh Downs" is the Colts receiver requesting a trade, "Tommy Robinson" is his guilty verdict); hourly desks politics/entertainment/sports/internet plus ideas and life; two screening reads by id (99 unread referenced, reply-parent and media-source posts, most pointed-at first, then 30 on the second hop; 2114804068011184133 and 2115173159322189922 Not Found); story clusters not in the plan; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "it" and "that", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1511Z'","        _last = '2026-10-28T1611Z'")
R("f'not in requests/plan.json for 2026-10-28T16Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T17Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T16Z (only screen was cut)'","reason = 'not due: requests/plan.json for 2026-10-28T17Z (nothing cut)'")
R("VOL_DESKS = ['politics','world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T18:00:00Z, end_time 2026-10-28T17:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science; counts 4 h old); each series is the 167 full hours 2026-10-21T18:00Z to 2026-10-28T16:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T16:15:00Z (the post\\'s creation, 16:15:38) and end_time 2026-10-28T16:35:00Z: (conversation_id:2115477603469631911 is:reply) and (quotes_of_tweet_id:2115477603469631911 -is:retweet); the plan gives context.top two reads, so one post: 2115477603469631911 (@JFowlerESPN, Colts WR Josh Downs requesting a trade, 1.19M views), the most viewed post new this run that is not old content; 25 replies and 25 quote posts came back; the five most liked of each kind kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))"+s[b:]
a=s.index("            f'Day-band run (12:11 PM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (1:02 PM ET Oct 28 / 17:02 UTC Oct 28, the 17Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T17Z, 32 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 563 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 230 flat posts the plan set aside and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, ideas, sports, internet and life (6 reads; the other desks are not due). Volume: markets, business, ai, tech and science (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Selena", "Josh Downs" and "Tommy Robinson" (3 reads). rising.global: quote word "it" and repost word "that" (2 reads). context.top: 2 reads for 2115477603469631911 (25 replies and 25 quotes in the window; 5 of each kept). Screen: 2 reads by id (99 ids, then 30 on the second hop; the plan allowed 3). '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1611Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1702Z.json'")
R("        'plan': '2026-10-28T16Z',","        'plan': '2026-10-28T17Z',")
R("    'context': [{'post_id': '2115212717938078027',","    'context': [{'post_id': '2115477603469631911',")
a=s.index("CTX_REPLIES = ['2115214886766776367'"); b=s.index("CTX_IDS = CTX_REPLIES + CTX_QUOTES",a)
s=s[:a]+"CTX_REPLIES = ['2115481945689956820','2115482387022786697','2115482415632093457','2115481930011730009','2115482417628848510']  # 1702Z: five most liked replies to JFowlerESPN 2115477603469631911 in its first 20 minutes\nCTX_QUOTES = ['2115482283163656692','2115482253316989289','2115482273181212679','2115482441733284032','2115482231854579872']  # 1702Z: five most liked quote posts in the window\n"+s[b:]
R("# 4b) context picks (1511Z, 1611Z)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'entertainment',",
  "# 4b) context picks (1511Z, 1611Z, 1702Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',")
open(p,'w').write(s); print('ok')
s=open(p).read()
anchor="DESK_OVERRIDE_RUN.update({'2115400984507597090':'sports'})  # 1611Z: FabrizioRomano Danilo contract at Flamengo\n"
assert s.count(anchor)==1
s=s.replace(anchor, anchor+"EXTRA_PRIVATE |= {'2115138071524241849','2005240144576831992'}  # 1702Z: v1renff video of his mother and aunt arguing (private family); betoniano San Siro kiss-cam clip naming two private fans\nDESK_OVERRIDE_RUN.update({'2115405415618076707':'disaster','2114801674800017755':'sports','2115388205105021291':'sports','2110823066595131768':'markets','2083293160092893412':'politics'})  # 1702Z desk fixes: AZ_Intel_ Toledo train collision aerial is disaster; Schultz trade-market post and nocontextfooty clip are sports; aleabitoreddit GOOGL memory deals is markets; Oxford Union Tommy Robinson clip is politics\n")
open(p,'w').write(s); print('ok2')
