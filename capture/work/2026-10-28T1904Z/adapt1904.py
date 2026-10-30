p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
R('capture/2026/10/28/1807Z.json from saved','capture/2026/10/28/1904Z.json from saved')
R("work/2026-10-28T1807Z'","work/2026-10-28T1904Z'")
R("RUN_ID = '2026-10-28T1807Z'","RUN_ID = '2026-10-28T1904Z'")
R("STARTED = '2026-10-28T18:07:00Z'","STARTED = '2026-10-28T19:04:00Z'")
R("OBS_AT = '2026-10-28T18:08:00Z'","OBS_AT = '2026-10-28T19:05:00Z'")
R("READS_BEFORE = 496","READS_BEFORE = 458")
L("READS_USED = 38  # 1807Z","READS_USED = 27  # 1904Z: this run's 27 X calls (the plan listed 28; the third screening read was not needed); the counter fell 458 to 431; no 429 or 503 refusals")
R("datetime(2026,10,28,18,8,tzinfo=timezone.utc).timestamp()  # 1807Z (1702Z used 17:03, ","datetime(2026,10,28,19,5,tzinfo=timezone.utc).timestamp()  # 1904Z (1807Z used 18:08, 1702Z used 17:03, ")
R("""    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_gemini': 'trend_gemini.txt', 'trend_sullivan': 'trend_sullivan.txt', 'trend_macbook': 'trend_macbook.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_ernie': 'trend_ernie.txt', 'trend_warsh': 'trend_warsh.txt', 'trend_higby': 'trend_higby.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1904Z: the 4 hourly desks requests/plan.json for 2026-10-28T19Z lists (the 2-hourly desks were read in 1807Z)")
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_gemini','trend.Gemini 4 Carbon'),('trend_sullivan','trend.Dan Sullivan'),('trend_macbook','trend.MacBook Pro'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_this','quote'),('repost_you','repost'),
    ('trend_ernie','trend.Ernie'),('trend_warsh','trend.Warsh'),('trend_higby','trend.Cam Higby'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("""        if str(_x) == 'trend.Gemini 4 Carbon': return 'ai'  # 1807Z""","""        if str(_x) == 'trend.Ernie': return 'sports'  # 1904Z: Ernie Johnson says this is his final season on Inside the NBA ("Inside the NBA" on the US list is the same event)
        if str(_x) == 'trend.Warsh': return 'markets'  # 1904Z: Fed Chair Kevin Warsh's FOMC press conference ("The Fed" on the US list is the same event)
        if str(_x) == 'trend.Cam Higby': return 'justice'  # 1904Z: James O'Keefe and Cam Higby charged with felonies in Minnesota
        if str(_x) == 'trend.Gemini 4 Carbon': return 'ai'  # 1807Z""")
R("if _c.endswith('1807Z.json') and '/28/' in _c: continue","if _c.endswith('1904Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T18Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T19Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"332 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 239 flat posts wait for their sixth run\"; its left_out also counts 6 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Ernie", "Warsh" and "Cam Higby" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the three highest of the top-ten US names that had no posts attached in 1807Z ("Dolores Huerta", "Dan Sullivan", "Gemini 4 Carbon", "MacBook Pro" and "Selena" had posts in earlier runs; "Inside the NBA" is the same event as "Ernie" and "The Fed" the same event as "Warsh"); "Ernie" is Ernie Johnson announcing this is his final season on Inside the NBA, "Warsh" is Fed Chair Kevin Warsh\\'s FOMC press conference, "Cam Higby" is James O\\'Keefe and Cam Higby being charged with felonies in Minnesota); the 4 due desks; two screening reads by id (92 unread referenced, reply-parent and media-source posts, most pointed-at first, then 12 on the second hop; none missing); story clusters not in the plan; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "this" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1702Z'","        _last = '2026-10-28T1807Z'")
R("f'not in requests/plan.json for 2026-10-28T18Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T19Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T18Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-28T19Z (nothing cut)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T20:00:00Z, end_time 2026-10-28T19:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat); each series is the 167 full hours 2026-10-21T20:00Z to 2026-10-28T18:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T18:22:00Z (the post\\'s creation, 18:22:04) and end_time 2026-10-28T18:42:00Z: (conversation_id:2115509418276376791 is:reply) and (quotes_of_tweet_id:2115509418276376791 -is:retweet); the plan gives context.top two reads, so one post: 2115509418276376791 (@FabrizioRomano, Ballon d\\'Or names Cristiano Ronaldo\\'s 2008 award the best Ballon d\\'Or, 3.08M views), the most viewed post new this run that is not old content; a full page of 25 replies and 25 quotes came back; the five most liked of each kind are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
a=s.index("            f'Day-band run (1:07 PM CT"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (2:04 PM CT Oct 28 / 19:04 UTC Oct 28, the 19Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T19Z, 28 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the third screening read was not needed), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 430 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 239 flat posts the plan set aside and the 6 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other desks are not due). Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Ernie", "Warsh" and "Cam Higby" (3 reads). rising.global: quote word "this" and repost word "you" (2 reads). context.top: 2 reads for 2115509418276376791 (25 replies and 25 quotes in the window, five of each kept). Screen: 2 reads by id (92 ids, then 12 on the second hop). '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1807Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1904Z.json'")
R("        'plan': '2026-10-28T18Z',","        'plan': '2026-10-28T19Z',")
R("    'context': [{'post_id': '2115150889459589289',","    'context': [{'post_id': '2115509418276376791',")
a=s.index("CTX_REPLIES = ['2115151855663890477'"); b=s.index("CTX_IDS = CTX_REPLIES + CTX_QUOTES",a)
s=s[:a]+"CTX_REPLIES = ['2115514418674954580','2115514420658942301','2115514415265312901','2115514375859531818','2115514372986462718']  # 1904Z: the five most liked replies to FabrizioRomano 2115509418276376791 in its first 20 minutes\nCTX_QUOTES = ['2115514394167881894','2115514406582804876','2115514423184163161','2115514413776011445','2115514432738455832']  # 1904Z: the five most liked quotes in the window\n"+s[b:]
R("# 4b) context picks (1511Z, 1611Z, 1702Z, 1807Z: the context post is entertainment)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'entertainment',",
  "# 4b) context picks (1511Z, 1611Z, 1702Z, 1807Z: entertainment; 1904Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',")
open(p,'w').write(s); print('ok')
