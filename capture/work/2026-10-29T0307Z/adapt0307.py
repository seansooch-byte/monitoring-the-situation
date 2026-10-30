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
R('capture/2026/10/29/0159Z.json from saved','capture/2026/10/29/0307Z.json from saved')
R("work/2026-10-29T0159Z'","work/2026-10-29T0307Z'")
R("RUN_ID = '2026-10-29T0159Z'","RUN_ID = '2026-10-29T0307Z'")
R("STARTED = '2026-10-29T01:59:00Z'","STARTED = '2026-10-29T03:07:00Z'")
R("OBS_AT = '2026-10-29T02:01:00Z'","OBS_AT = '2026-10-29T03:09:00Z'")
R("READS_BEFORE = 929","READS_BEFORE = 903")
L("READS_USED = 26  # 0159Z","READS_USED = 39  # 0307Z: this run's 39 X calls, the plan's 39 reads (all 3 screen reads used: 100 and 46 unread references, then 18 second-hop references); the counter fell 903 to 864; no 429 or 503 refusals")
R("datetime(2026,10,29,2,1,tzinfo=timezone.utc).timestamp()  # 0159Z (","datetime(2026,10,29,3,9,tzinfo=timezone.utc).timestamp()  # 0307Z (0159Z used 02:01, ")
R("""    'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_nembhard': 'trend_nembhard.txt', 'trend_maxey': 'trend_maxey.txt', 'trend_reid': 'trend_reid.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_aminata': 'trend_aminata.txt', 'trend_clarkson': 'trend_clarkson.txt', 'trend_lee': 'trend_lee.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 0307Z: the 15 desks requests/plan.json for 2026-10-29T03Z lists (defense, disaster, business, science not due)")
R("""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_nembhard','trend.Nembhard'),('trend_maxey','trend.Tyrese Maxey'),('trend_reid','trend.Naz Reid'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_this','quote'),('repost_is','repost'),
    ('trend_aminata','trend.Queen Aminata'),('trend_clarkson','trend.Clarkson'),('trend_lee','trend.Charles Lee'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("        if str(_x) in ('trend.Nembhard','trend.Tyrese Maxey','trend.Naz Reid'): return 'sports'  # 0159Z","        if str(_x) in ('trend.Queen Aminata','trend.Clarkson','trend.Charles Lee'): return 'sports'  # 0307Z: AEW Dynamite TBS title (Queen Aminata), Knicks' Jordan Clarkson, Hornets coach Charles Lee benching Naz Reid\n        if str(_x) in ('trend.Nembhard','trend.Tyrese Maxey','trend.Naz Reid'): return 'sports'  # 0159Z")
R("if _c.endswith('0159Z.json') and '/29/' in _c: continue","if _c.endswith('0307Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T02Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T03Z, in its order and in batches of 100 (341 ids; its left_out counts 235 slowed flat posts and 5 unavailable posts not listed); nothing added, dropped or reordered; ")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Queen Aminata", "Clarkson" and "Charles Lee" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the first three top-ten US names that had no posts attached in 0159Z: "#AEWDynamite" and "#Survivor51" were attached in 0102Z, "#MitchJones25mGiveway" is a giveaway hashtag, "Naz Reid", "Nembhard" and "Tyrese Maxey" were attached in 0159Z; "Queen Aminata" is the same AEW Dynamite show as "#AEWDynamite" and "Claudio", and "Charles Lee" is the same event as 0159Z\\'s "Naz Reid" (the Hornets coach benching him); "Clarkson" is the Knicks\\' Jordan Clarkson (some posts name Kelly Clarkson)); the 15 due desks; 3 screening reads by id (100 and 46 unread referenced posts, then 18 unread second-hop references); story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "this" and "is" (0159Z used "what" and "the"), each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-29T0102Z'","        _last = '2026-10-29T0159Z'")
R("f'not in requests/plan.json for 2026-10-29T02Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T03Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-29T02Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-29T03Z (nothing cut)'")
R("VOL_DESKS = ['world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T04:00:00Z, end_time 2026-10-29T03:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science: counts 4 h old); each series is the 167 full hours 2026-10-22T04:00Z to 2026-10-29T02:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T03:55:00Z (the post\\'s creation, 03:55:43) and end_time 2026-10-28T04:15:00Z: (conversation_id:2115291395733049422 is:reply) and (quotes_of_tweet_id:2115291395733049422 -is:retweet); the plan gives context.top two reads, so one post: 2115291395733049422 (@RahulGandhi on Tata, 5.0M views), the most viewed post new this run; the five most liked replies and five most liked quotes are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
SPAN("            f'Day-band run (8:59 PM CT Oct 28","            f'No open requests.","""            f'Day-band run (10:07 PM CT Oct 28 / 03:07 UTC Oct 29, the 03Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T03Z, 39 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 341 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 235 slowed flat posts and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, ideas, sports, internet, life and offbeat (15 reads; defense, disaster, business and science not due). Volume: markets, business, ai, tech and science (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Queen Aminata", "Clarkson" and "Charles Lee" (3 reads). rising.global: quote word "this" and repost word "is" (2 reads). context.top: 2 reads for 2115291395733049422. Screen: 3 reads by id (100 and 46 referenced posts, then 18 second-hop references). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0159Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0307Z.json'")
R("        'plan': '2026-10-29T02Z',","        'plan': '2026-10-29T03Z',")
R("    'context': [{'post_id': '2115365790660636879',","    'context': [{'post_id': '2115291395733049422',")
SPAN("CTX_REPLIES = ['2115365793806659642'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115296146117874151','2115296140551950483','2115295985048146078','2115296043508310116','2115296081974329779']  # 0307Z: five most liked replies to RahulGandhi 2115291395733049422 in its first 20 minutes\nCTX_QUOTES = ['2115294385982312626','2115296150869680188','2115295045897326655','2115295115984228614','2115295587281322452']  # 0307Z: five most liked quotes in the window\n")
R("0159Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',",
  "0159Z: sports; 0307Z: the context post is business)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'business',")
open(p,'w').write(s); print('ok')
