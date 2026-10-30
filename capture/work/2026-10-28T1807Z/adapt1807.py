p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
R('capture/2026/10/28/1702Z.json from saved','capture/2026/10/28/1807Z.json from saved')
R("work/2026-10-28T1702Z'","work/2026-10-28T1807Z'")
R("RUN_ID = '2026-10-28T1702Z'","RUN_ID = '2026-10-28T1807Z'")
R("STARTED = '2026-10-28T17:02:00Z'","STARTED = '2026-10-28T18:07:00Z'")
R("OBS_AT = '2026-10-28T17:03:00Z'","OBS_AT = '2026-10-28T18:08:00Z'")
R("READS_BEFORE = 527","READS_BEFORE = 496")
L("READS_USED = 31  # 1702Z","READS_USED = 38  # 1807Z: this run's 38 X calls (the plan's 38 reads, all used); the counter fell 496 to 458; no 429 or 503 refusals")
R("datetime(2026,10,28,17,3,tzinfo=timezone.utc).timestamp()  # 1702Z (1611Z used 16:12, ","datetime(2026,10,28,18,8,tzinfo=timezone.utc).timestamp()  # 1807Z (1702Z used 17:03, 1611Z used 16:12, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_selena': 'trend_selena.txt', 'trend_downs': 'trend_downs.txt', 'trend_robinson': 'trend_robinson.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'watch4': 'watch4.txt',
    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_gemini': 'trend_gemini.txt', 'trend_sullivan': 'trend_sullivan.txt', 'trend_macbook': 'trend_macbook.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
L("DUE = ['politics','entertainment'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1807Z: the 13 desks requests/plan.json for 2026-10-28T18Z lists (the four hourly desks plus the nine 2-hourly desks)")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_selena','trend.Selena'),('trend_downs','trend.Josh Downs'),('trend_robinson','trend.Tommy Robinson'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_gemini','trend.Gemini 4 Carbon'),('trend_sullivan','trend.Dan Sullivan'),('trend_macbook','trend.MacBook Pro'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("""        if str(_x) == 'trend.Selena': return 'entertainment'  # 1702Z""","""        if str(_x) == 'trend.Gemini 4 Carbon': return 'ai'  # 1807Z: Google releases its Gemini 4 Carbon model
        if str(_x) == 'trend.Dan Sullivan': return 'politics'  # 1807Z: NYT report that Democrats recruited a second "Dan Sullivan" for the Alaska Senate ballot ("Peltola" on the US list is the same event)
        if str(_x) == 'trend.MacBook Pro': return 'tech'  # 1807Z: Apple unveils a touchscreen MacBook Pro
        if str(_x) == 'trend.Selena': return 'entertainment'  # 1702Z""")
R("if _c.endswith('1702Z.json') and '/28/' in _c: continue","if _c.endswith('1807Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T17Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T18Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"328 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 223 flat posts wait for their sixth run\"; its left_out also counts 6 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 6 reads; fields","{len(watch_unavailable)} unavailable, 5 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Gemini 4 Carbon", "Dan Sullivan" and "MacBook Pro" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the three highest of the top-ten US names that had no posts attached in 1702Z ("Dolores Huerta", "Justin Tucker", "Selena", "Josh Downs" and "FOMC" had posts in earlier runs; "Cam Higby", "Peltola" and "Argon" were left for a later run, "Peltola" being the same event as "Dan Sullivan" and "Argon" the earlier Gemini 4 Argon model); "Gemini 4 Carbon" is Google\\'s new frontier model, "Dan Sullivan" is the NYT report that Democrats recruited a second Dan Sullivan for the Alaska Senate ballot, "MacBook Pro" is Apple\\'s first touchscreen MacBook Pro); all 13 due desks; three screening reads by id (100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 49, then 21 on the second hop; 2111374968177180932 Not Found); story clusters not in the plan; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "just" and "what", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1611Z'","        _last = '2026-10-28T1702Z'")
R("f'not in requests/plan.json for 2026-10-28T17Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T18Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T17Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-28T18Z (nothing cut)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T19:00:00Z, end_time 2026-10-28T18:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas; counts 4 h old); each series is the 167 full hours 2026-10-21T19:00Z to 2026-10-28T17:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-27T18:37:00Z (the post\\'s creation, 18:37:24) and end_time 2026-10-27T18:57:00Z: (conversation_id:2115150889459589289 is:reply) and (quotes_of_tweet_id:2115150889459589289 -is:retweet); the plan gives context.top two reads, so one post: 2115150889459589289 (@1auvender, quote of a clip about Black actresses and hair, 4.70M views), the most viewed post new this run that is not old content; 1 reply (the author\\'s own follow-up) and no quote posts came back in the window',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it; the window held only one reply and no quotes',CTX_IDS))")
a=s.index("            f'Day-band run (1:02 PM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (1:07 PM CT Oct 28 / 18:07 UTC Oct 28, the 18Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T18Z, 38 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 436 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 223 flat posts the plan set aside and the 6 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (13 reads; the other desks are not due). Volume: medicine, entertainment, music, gaming and ideas (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Gemini 4 Carbon", "Dan Sullivan" and "MacBook Pro" (3 reads). rising.global: quote word "just" and repost word "what" (2 reads). context.top: 2 reads for 2115150889459589289 (1 reply and no quotes in the window). Screen: 3 reads by id (100 ids, 49, then 21 on the second hop). '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1702Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1807Z.json'")
R("        'plan': '2026-10-28T17Z',","        'plan': '2026-10-28T18Z',")
R("    'context': [{'post_id': '2115477603469631911',","    'context': [{'post_id': '2115150889459589289',")
a=s.index("CTX_REPLIES = ['2115481945689956820'"); b=s.index("CTX_IDS = CTX_REPLIES + CTX_QUOTES",a)
s=s[:a]+"CTX_REPLIES = ['2115151855663890477']  # 1807Z: the only reply to 1auvender 2115150889459589289 in its first 20 minutes (the author's own follow-up)\nCTX_QUOTES = []  # 1807Z: no quote posts in the window\n"+s[b:]
R("# 4b) context picks (1511Z, 1611Z, 1702Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',",
  "# 4b) context picks (1511Z, 1611Z, 1702Z, 1807Z: the context post is entertainment)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'entertainment',")
open(p,'w').write(s); print('ok')
