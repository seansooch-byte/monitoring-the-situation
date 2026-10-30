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
R('capture/2026/10/29/0102Z.json from saved','capture/2026/10/29/0159Z.json from saved')
R("work/2026-10-29T0102Z'","work/2026-10-29T0159Z'")
R("RUN_ID = '2026-10-29T0102Z'","RUN_ID = '2026-10-29T0159Z'")
R("STARTED = '2026-10-29T01:02:00Z'","STARTED = '2026-10-29T01:59:00Z'")
R("OBS_AT = '2026-10-29T01:05:00Z'","OBS_AT = '2026-10-29T02:01:00Z'")
R("READS_BEFORE = 966","READS_BEFORE = 929")
L("READS_USED = 37  # 0102Z","READS_USED = 26  # 0159Z: this run's 26 X calls of the plan's 27 reads (2 of the 3 screen reads used: 90 unread references, then 13 second-hop references); the counter fell 929 to 903; no 429 or 503 refusals")
R("datetime(2026,10,29,1,5,tzinfo=timezone.utc).timestamp()  # 0102Z (","datetime(2026,10,29,2,1,tzinfo=timezone.utc).timestamp()  # 0159Z (0102Z used 01:05, ")
R("""    'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_aew': 'trend_aew.txt', 'trend_survivor': 'trend_survivor.txt', 'trend_abbott': 'trend_abbott.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_nembhard': 'trend_nembhard.txt', 'trend_maxey': 'trend_maxey.txt', 'trend_reid': 'trend_reid.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
L("DUE = ['politics','world','justice'","DUE = ['politics','entertainment','sports','internet']  # 0159Z: the 4 desks requests/plan.json for 2026-10-29T02Z lists (the other 15 not due)")
R("""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_aew','trend.#AEWDynamite'),('trend_survivor','trend.#Survivor51'),('trend_abbott','trend.#AbbottElementary'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_nembhard','trend.Nembhard'),('trend_maxey','trend.Tyrese Maxey'),('trend_reid','trend.Naz Reid'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("        if str(_x) == 'trend.#AEWDynamite': return 'sports'  # 0102Z","        if str(_x) in ('trend.Nembhard','trend.Tyrese Maxey','trend.Naz Reid'): return 'sports'  # 0159Z: NBA Wednesday night (Pacers, 76ers, Timberwolves)\n        if str(_x) == 'trend.#AEWDynamite': return 'sports'  # 0102Z")
R("if _c.endswith('0102Z.json') and '/29/' in _c: continue","if _c.endswith('0159Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T01Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T02Z, in its order and in batches of 100 (355 ids; its left_out counts 220 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; ")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Nembhard", "Tyrese Maxey" and "Naz Reid" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the first three top-ten US names that had no posts attached in 0102Z: "#AEWDynamite" and "#Survivor51" were attached in 0102Z, "#MitchJones25mGiveway" is a giveaway hashtag, "Claudio" is the same AEW Dynamite show, "Dan Sullivan" and "Alaska" are the same event as 2300Z\\'s "Dan Sullivan", "Ernie" was attached in 0001Z; all three are Wednesday night NBA games); the 4 due desks; 2 screening reads by id (90 unread referenced posts, then 13 unread second-hop references; 5 third-hop references left unread); story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "what" and "the" (0102Z used "that" and "just"), each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-29T0001Z'","        _last = '2026-10-29T0102Z'")
R("f'not in requests/plan.json for 2026-10-29T01Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T02Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-29T01Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-29T02Z (nothing cut)'")
R("VOL_DESKS = ['sports','internet','life','offbeat','politics']","VOL_DESKS = ['world','defense','justice','disaster']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T03:00:00Z, end_time 2026-10-29T02:00:00Z, one read per desk for the 4 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster: counts 6 h old); each series is the 167 full hours 2026-10-22T03:00Z to 2026-10-29T01:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T08:51:00Z (the post\\'s creation, 08:51:03) and end_time 2026-10-28T09:11:00Z: (conversation_id:2115365790660636879 is:reply) and (quotes_of_tweet_id:2115365790660636879 -is:retweet); the plan gives context.top two reads, so one post: 2115365790660636879 (@Nolimitzor_X, Rampage Jackson arguing with his son Raja, 2.81M views), the most viewed post new this run; only 2 replies and no quotes came back in the window; both replies are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it; the 20-minute window held only 2 replies and no quotes',CTX_IDS))")
SPAN("            f'Day-band run (8:02 PM CT Oct 28","            f'No open requests.","""            f'Day-band run (8:59 PM CT Oct 28 / 01:59 UTC Oct 29, the 02Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T02Z, 27 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 355 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 220 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 not due). Volume: world, defense, justice and disaster (4 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Nembhard", "Tyrese Maxey" and "Naz Reid" (3 reads). rising.global: quote word "what" and repost word "the" (2 reads). context.top: 2 reads for 2115365790660636879 (2 replies and no quotes in the window). Screen: 2 reads by id (90 referenced posts, then 13 second-hop references). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0102Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0159Z.json'")
R("        'plan': '2026-10-29T01Z',","        'plan': '2026-10-29T02Z',")
R("    'context': [{'post_id': '2115544562219315474',","    'context': [{'post_id': '2115365790660636879',")
SPAN("CTX_REPLIES = ['2115549402282467446'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115365793806659642','2115370008649904495']  # 0159Z: the only two replies to Nolimitzor_X 2115365790660636879 in its first 20 minutes\nCTX_QUOTES = []  # 0159Z: no quotes in the window\n")
R("0102Z: the context post is world)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'world',",
  "0102Z: world; 0159Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',")
open(p,'w').write(s); print('ok')
