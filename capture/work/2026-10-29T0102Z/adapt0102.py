p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    a=s.index(start); b=s.index(end,a); s=s[:a]+new+s[b:]
R('capture/2026/10/29/0001Z.json from saved','capture/2026/10/29/0102Z.json from saved')
R("work/2026-10-29T0001Z'","work/2026-10-29T0102Z'")
R("RUN_ID = '2026-10-29T0001Z'","RUN_ID = '2026-10-29T0102Z'")
R("STARTED = '2026-10-29T00:01:00Z'","STARTED = '2026-10-29T01:02:00Z'")
R("OBS_AT = '2026-10-29T00:05:00Z'","OBS_AT = '2026-10-29T01:05:00Z'")
R("READS_BEFORE = 1000","READS_BEFORE = 966")
L("READS_USED = 34  # 0001Z","READS_USED = 37  # 0102Z: this run's 37 X calls, the plan's 37 reads (all 3 screen reads used: the second hop found 30 unread references); the counter fell 966 to 929; no 429 or 503 refusals")
R("datetime(2026,10,29,0,5,tzinfo=timezone.utc).timestamp()  # 0001Z (","datetime(2026,10,29,1,5,tzinfo=timezone.utc).timestamp()  # 0102Z (0001Z used 00:05, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_ernie': 'trend_ernie.txt', 'trend_mason': 'trend_mason.txt', 'trend_dybantsa': 'trend_dybantsa.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_aew': 'trend_aew.txt', 'trend_survivor': 'trend_survivor.txt', 'trend_abbott': 'trend_abbott.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
L("DUE = ['politics','defense','disaster'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 0102Z: the 13 desks requests/plan.json for 2026-10-29T01Z lists (defense, disaster, business, science, ideas and life not due)")
R("""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_ernie','trend.Ernie'),('trend_mason','trend.Mason Williams'),('trend_dybantsa','trend.AJ Dybantsa'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_aew','trend.#AEWDynamite'),('trend_survivor','trend.#Survivor51'),('trend_abbott','trend.#AbbottElementary'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("        if str(_x) in ('trend.Mason Williams','trend.AJ Dybantsa'): return 'sports'  # 0001Z","        if str(_x) == 'trend.#AEWDynamite': return 'sports'  # 0102Z: AEW Dynamite (\"Anarchy in the Arena\", \"Jack Perry\", \"Kyle Fletcher\", \"Bandido\" and \"Full Gear\" on the US list are the same show)\n        if str(_x) in ('trend.#Survivor51','trend.#AbbottElementary'): return 'entertainment'  # 0102Z: Survivor 51 and Abbott Elementary episodes\n        if str(_x) in ('trend.Mason Williams','trend.AJ Dybantsa'): return 'sports'  # 0001Z")
R("if _c.endswith('0001Z.json') and '/29/' in _c: continue","if _c.endswith('0102Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T00Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T01Z, in its order and in batches of 100 (391 ids; its left_out counts 241 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; ")
R("{len(watch_unavailable)} unavailable, 7 reads; fields","{len(watch_unavailable)} unavailable, 4 reads; fields")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "#AEWDynamite", "#Survivor51" and "#AbbottElementary" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are three top-ten US names that had no posts attached in 0001Z ("Anarchy in the Arena", "Jack Perry" and "Kyle Fletcher" are the same AEW Dynamite show; "Ernie" was attached in 0001Z; "Dan Sullivan" and "Alaska" are the same event as 2300Z\\'s "Dan Sullivan"); "#AEWDynamite" is the AEW Dynamite broadcast, "#Survivor51" and "#AbbottElementary" are that night\\'s TV episodes); the 13 due desks; 3 screening reads by id (153 unread referenced posts, then 30 unread second-hop references), so every referenced post was read; story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "that" and "just" (0001Z used "my" and "it"), each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-28T2300Z'","        _last = '2026-10-29T0001Z'")
R("f'not in requests/plan.json for 2026-10-29T00Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T01Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-29T00Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-29T01Z (nothing cut)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat','politics']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T02:00:00Z, end_time 2026-10-29T01:00:00Z, one read per desk for the 5 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 6 h old; volume.politics: counts 5 h old); each series is the 167 full hours 2026-10-22T02:00Z to 2026-10-29T00:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T20:41:00Z (the post\\'s creation, 20:41:43) and end_time 2026-10-28T21:01:00Z: (conversation_id:2115544562219315474 is:reply) and (quotes_of_tweet_id:2115544562219315474 -is:retweet); the plan gives context.top two reads, so one post: 2115544562219315474 (@FlavioBolsonaro, his letter to the nation after the Brazil runoff, 7.06M views), the most viewed post new this run; a full page of 25 replies and 25 quotes came back (relevancy still returned the last minute of the window); the five most liked of each kind are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
SPAN("            f'Day-band run (7:01 PM CT Oct 28","            f'No open requests.","""            f'Day-band run (8:02 PM CT Oct 28 / 01:02 UTC Oct 29, the 01Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T01Z, 37 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 391 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 241 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (13 reads; defense, disaster, business, science, ideas and life not due). Volume: sports, internet, life, offbeat and politics (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "#AEWDynamite", "#Survivor51" and "#AbbottElementary" (3 reads). rising.global: quote word "that" and repost word "just" (2 reads). context.top: 2 reads for 2115544562219315474 (25 replies and 25 quotes in the window, five of each kept). Screen: 3 reads by id (153 referenced posts, then 30 second-hop references). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0001Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0102Z.json'")
R("        'plan': '2026-10-29T00Z',","        'plan': '2026-10-29T01Z',")
R("    'context': [{'post_id': '2115569434169364836',","    'context': [{'post_id': '2115544562219315474',")
SPAN("CTX_REPLIES = ['2115569667976692036'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115549402282467446','2115549384997838904','2115549414031024243','2115549411325702416','2115549411279360053']  # 0102Z: the five most liked replies to FlavioBolsonaro 2115544562219315474 in its first 20 minutes (relevancy returned the window's last minute)\nCTX_QUOTES = ['2115549362625638415','2115549317511754173','2115549319738867814','2115549366832562614','2115549331038044487']  # 0102Z: the five most liked quotes in the window\n")
R("0001Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',",
  "0001Z: sports; 0102Z: the context post is world)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'world',")
open(p,'w').write(s); print('ok')
