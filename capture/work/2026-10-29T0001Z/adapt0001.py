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
R('capture/2026/10/28/2300Z.json from saved','capture/2026/10/29/0001Z.json from saved')
R("work/2026-10-28T2300Z'","work/2026-10-29T0001Z'")
R("RUN_ID = '2026-10-28T2300Z'","RUN_ID = '2026-10-29T0001Z'")
R("STARTED = '2026-10-28T23:00:00Z'","STARTED = '2026-10-29T00:01:00Z'")
R("OBS_AT = '2026-10-28T23:03:00Z'","OBS_AT = '2026-10-29T00:05:00Z'")
R("READS_BEFORE = 389","READS_BEFORE = 1000")
L("READS_USED = 40  # 2300Z","READS_USED = 34  # 0001Z: this run's 34 X calls (the plan's 35 reads less one screen read: the second hop found nothing unread); the counter reset at 00:00 UTC and fell 1000 to 966; no 429 or 503 refusals")
R("datetime(2026,10,28,23,3,tzinfo=timezone.utc).timestamp()  # 2300Z (","datetime(2026,10,29,0,5,tzinfo=timezone.utc).timestamp()  # 0001Z (2300Z used 23:03, ")
R("""    'watch4': 'watch4.txt',
    'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_fofana': 'trend_fofana.txt', 'trend_sullivan': 'trend_sullivan.txt', 'trend_googl': 'trend_googl.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_ernie': 'trend_ernie.txt', 'trend_mason': 'trend_mason.txt', 'trend_dybantsa': 'trend_dybantsa.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
L("DUE = ['politics','world','justice'","DUE = ['politics','defense','disaster','business','science','entertainment','sports','internet']  # 0001Z: the 8 desks requests/plan.json for 2026-10-29T00Z lists (the other 11 not due)")
R("""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_fofana','trend.Fofana'),('trend_sullivan','trend.Dan Sullivan'),('trend_googl','trend.$GOOGL'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_ernie','trend.Ernie'),('trend_mason','trend.Mason Williams'),('trend_dybantsa','trend.AJ Dybantsa'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("        if str(_x) == 'trend.Fofana': return 'sports'","        if str(_x) in ('trend.Mason Williams','trend.AJ Dybantsa'): return 'sports'  # 0001Z: Kentucky v UCF (Mason Williams); AJ Dybantsa's NBA debut for the Wizards\n        if str(_x) == 'trend.Fofana': return 'sports'")
R("if _c.endswith('2300Z.json') and '/28/' in _c: continue","if _c.endswith('0001Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
SPAN("    f'get_posts_by_ids of the watch item of the 2026-10-28T23Z plan","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T00Z, in its order and in batches of 100 (683 ids; its left_out counts 313 slowed flat posts and 7 unavailable posts not listed); nothing added, dropped or reordered; ")
R("{len(watch_unavailable)} unavailable, 5 reads; fields","{len(watch_unavailable)} unavailable, 7 reads; fields")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Ernie", "Mason Williams" and "AJ Dybantsa" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are three top-ten US names that had no posts attached in 2300Z ("Inside the NBA" is the same event as "Ernie"; "Alaska" and "Peltola" are the same event as 2300Z\\'s "Dan Sullivan", "Estevao", "Gravenberch" and "Liverpool" the same match as 2300Z\\'s "Fofana"); "Ernie" is Ernie Johnson announcing this is his last season on Inside the NBA, "Mason Williams" is Kentucky v UCF, "AJ Dybantsa" is his NBA debut for the Wizards); the 8 due desks; 2 screening reads by id (138 unread referenced posts; the second hop found no unread references, so the third screen read was not used), so every referenced post was read; story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "my" and "it" (2300Z used "you" and "and"), each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-28T2004Z'","        _last = '2026-10-28T2300Z'")
R("f'not in the 2026-10-28T23Z plan (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T00Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: the 2026-10-28T23Z plan (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-29T00Z (nothing cut)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T01:00:00Z, end_time 2026-10-29T00:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas; counts 6 h old); each series is the 167 full hours 2026-10-22T01:00Z to 2026-10-28T23:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T22:20:00Z (the post\\'s creation, 22:20:33) and end_time 2026-10-28T22:40:00Z: (conversation_id:2115569434169364836 is:reply) and (quotes_of_tweet_id:2115569434169364836 -is:retweet); the plan gives context.top two reads, so one post: 2115569434169364836 (@SportsCenter, the Inside the NBA crew reacting to Ernie Johnson announcing his last season, 1.44M views), the most viewed post new this run; a full page of 25 replies and 25 quotes came back; the five most liked of each kind are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
SPAN("            f'Day-band run (6:00 PM CT Oct 28","            f'No open requests.","""            f'Day-band run (7:01 PM CT Oct 28 / 00:01 UTC Oct 29, the 00Z slot, first run of the UTC day; band allowance 42): followed requests/plan.json (for_run 2026-10-29T00Z, 35 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today, after the 00:00 UTC reset), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 683 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 313 slowed flat posts and the 7 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, defense, disaster, business, science, entertainment, sports and internet (8 reads; the other 11 not due). Volume: medicine, entertainment, music, gaming and ideas (5 reads, counts 6 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Ernie", "Mason Williams" and "AJ Dybantsa" (3 reads). rising.global: quote word "my" and repost word "it" (2 reads). context.top: 2 reads for 2115569434169364836 (25 replies and 25 quotes in the window, five of each kept). Screen: 2 reads by id (138 referenced posts; no second-hop references were unread). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/2300Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0001Z.json'")
R("        'plan': '2026-10-28T23Z',","        'plan': '2026-10-29T00Z',")
R("    'context': [{'post_id': '2115482148803412332',","    'context': [{'post_id': '2115569434169364836',")
SPAN("CTX_REPLIES = ['2115483912944361783'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115569667976692036','2115572500109332498','2115569660133540196','2115569740668412142','2115570317188116565']  # 0001Z: the five most liked replies to SportsCenter 2115569434169364836 in its first 20 minutes\nCTX_QUOTES = ['2115571762318471290','2115572116938764468','2115573813740232846','2115572865366196700','2115572897297436830']  # 0001Z: the five most liked quotes in the window\n")
R("2300Z: the context post is tech)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'tech',",
  "2300Z: tech; 0001Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',")
open(p,'w').write(s); print('ok')
