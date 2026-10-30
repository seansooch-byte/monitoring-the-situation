p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
R('capture/2026/10/28/1904Z.json from saved','capture/2026/10/28/2004Z.json from saved')
R("work/2026-10-28T1904Z'","work/2026-10-28T2004Z'")
R("RUN_ID = '2026-10-28T1904Z'","RUN_ID = '2026-10-28T2004Z'")
R("STARTED = '2026-10-28T19:04:00Z'","STARTED = '2026-10-28T20:04:00Z'")
R("OBS_AT = '2026-10-28T19:05:00Z'","OBS_AT = '2026-10-28T20:06:00Z'")
R("READS_BEFORE = 458","READS_BEFORE = 431")
L("READS_USED = 27  # 1904Z","READS_USED = 42  # 2004Z: this run's 42 X calls (the plan's 42 reads; screen was cut by the plan); the counter fell 431 to 389; no 429 or 503 refusals")
R("datetime(2026,10,28,19,5,tzinfo=timezone.utc).timestamp()  # 1904Z (1807Z used 18:08, ","datetime(2026,10,28,20,6,tzinfo=timezone.utc).timestamp()  # 2004Z (1904Z used 19:05, 1807Z used 18:08, ")
R("""    'watch4': 'watch4.txt',
    'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_ernie': 'trend_ernie.txt', 'trend_warsh': 'trend_warsh.txt', 'trend_higby': 'trend_higby.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',
    'quote_the': 'quote_the.txt',
    'repost_is': 'repost_is.txt',
    'trend_huerta': 'trend_huerta.txt', 'trend_gemini': 'trend_gemini.txt', 'trend_macbook': 'trend_macbook.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7'):",2)
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 2004Z: the 17 desks requests/plan.json for 2026-10-28T20Z lists (ideas and life not due)")
R("""    ('quote_this','quote'),('repost_you','repost'),
    ('trend_ernie','trend.Ernie'),('trend_warsh','trend.Warsh'),('trend_higby','trend.Cam Higby'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_the','quote'),('repost_is','repost'),
    ('trend_huerta','trend.Dolores Huerta'),('trend_gemini','trend.Gemini 4 Carbon'),('trend_macbook','trend.MacBook Pro'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("if _c.endswith('1904Z.json') and '/28/' in _c: continue","if _c.endswith('2004Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T19Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T20Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"339 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 280 flat posts wait for their sixth run\"; its left_out also counts 6 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 5 reads; fields","{len(watch_unavailable)} unavailable, 8 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Dolores Huerta", "Gemini 4 Carbon" and "MacBook Pro" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the three top-ten US names that had no posts attached in 1904Z (the other seven, Ernie, Inside the NBA, Dan Sullivan, Peltola, Warsh, The Fed and Cam Higby, all had posts in 1904Z; "Dan Sullivan" and "Peltola" are one event, the Alaska Senate race); "Dolores Huerta" is the death of the United Farm Workers co-founder at 96, "Gemini 4 Carbon" is Google\\'s new frontier model, "MacBook Pro" is Apple\\'s first touchscreen MacBook Pro); the 17 due desks; no screening reads (screen was cut by the plan), so only posts returned with numbers by the reads above were screened; unread referenced posts were not read; story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "the" and "is" (1904Z used "this" and "you"), each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1807Z'","        _last = '2026-10-28T1904Z'")
R("f'not in requests/plan.json for 2026-10-28T19Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T20Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T19Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-28T20Z (only screen was cut)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['politics','world','defense','justice','disaster']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T21:00:00Z, end_time 2026-10-28T20:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.world, volume.defense, volume.justice, volume.disaster; counts 4 h old); each series is the 167 full hours 2026-10-21T21:00Z to 2026-10-28T19:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T10:56:00Z (the post\\'s creation, 10:56:37) and end_time 2026-10-28T11:16:00Z: (conversation_id:2115397320292663758 is:reply) and (quotes_of_tweet_id:2115397320292663758 -is:retweet); the plan gives context.top two reads, so one post: 2115397320292663758 (@ChipGotIt_, Lacy\\'s first Japan stream ends after viewers order 500,000 yen of food through a restaurant QR code shown on stream, 4.28M views), the most viewed post new this run that is not old content; 1 reply and no quotes came back in the window; the reply is kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
a=s.index("            f'Day-band run (2:04 PM CT"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (3:04 PM CT Oct 28 / 20:04 UTC Oct 28, the 20Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T20Z, 42 reads listed, screen cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 761 ids in its order, 8 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 280 flat posts the plan set aside and the 6 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, defense, justice, disaster, markets, business, ai, tech, science, medicine, entertainment, music, gaming, sports, internet and offbeat (17 reads; ideas and life not due). Volume: politics, world, defense, justice and disaster (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Dolores Huerta", "Gemini 4 Carbon" and "MacBook Pro" (3 reads). rising.global: quote word "the" and repost word "is" (2 reads). context.top: 2 reads for 2115397320292663758 (1 reply and no quotes in the window; the reply kept). Screen: cut by the plan, no reads by id. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1904Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/2004Z.json'")
R("        'plan': '2026-10-28T19Z',","        'plan': '2026-10-28T20Z',")
R("    'context': [{'post_id': '2115509418276376791',","    'context': [{'post_id': '2115397320292663758',")
a=s.index("CTX_REPLIES = ['2115514418674954580'"); b=s.index("CTX_IDS = CTX_REPLIES + CTX_QUOTES",a)
s=s[:a]+"CTX_REPLIES = ['2115399226301493746']  # 2004Z: the one reply to ChipGotIt_ 2115397320292663758 in its first 20 minutes\nCTX_QUOTES = []  # 2004Z: no quotes in the window\n"+s[b:]
R("# 4b) context picks (1511Z, 1611Z, 1702Z, 1807Z: entertainment; 1904Z: the context post is sports)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'sports',",
  "# 4b) context picks (1511Z, 1611Z, 1702Z, 1807Z: entertainment; 1904Z: sports; 2004Z: the context post is internet)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'internet',")
open(p,'w').write(s); print('ok')
