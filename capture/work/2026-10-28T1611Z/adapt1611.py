p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1511Z.json from saved','capture/2026/10/28/1611Z.json from saved')
R("work/2026-10-28T1511Z'","work/2026-10-28T1611Z'")
R("RUN_ID = '2026-10-28T1511Z'","RUN_ID = '2026-10-28T1611Z'")
R("STARTED = '2026-10-28T15:11:00Z'","STARTED = '2026-10-28T16:11:00Z'")
R("OBS_AT = '2026-10-28T15:12:00Z'","OBS_AT = '2026-10-28T16:12:00Z'")
R("READS_BEFORE = 596","READS_BEFORE = 569")
a=s.index("READS_USED = 27  # 1511Z"); b=s.index("\n",a)
s=s[:a]+"READS_USED = 42  # 1611Z: this run's 42 X calls (the plan's 42 reads; screen was cut by the plan); the counter fell 569 to 527; no 429 or 503 refusals"+s[b:]
R("datetime(2026,10,28,15,12,tzinfo=timezone.utc).timestamp()  # 1511Z (1406Z used 14:07, ","datetime(2026,10,28,16,12,tzinfo=timezone.utc).timestamp()  # 1611Z (1511Z used 15:12, 1406Z used 14:07, ")
R("""    'watch4': 'watch4.txt',
    'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_toledo': 'trend_toledo.txt', 'trend_jlaw': 'trend_jlaw.txt', 'trend_robin': 'trend_robin.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',
    'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_huerta': 'trend_huerta.txt', 'trend_fomc': 'trend_fomc.txt', 'trend_tucker': 'trend_tucker.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7'):",2)
a=s.index("DUE = ['politics','entertainment'"); b=s.index("\n",a)
s=s[:a]+"DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1611Z: the 17 desks requests/plan.json for 2026-10-28T16Z lists (ideas and life not due)"+s[b:]
R("""    ('quote_this','quote'),('repost_you','repost'),
    ('trend_toledo','trend.Toledo'),('trend_jlaw','trend.Jennifer Lawrence'),('trend_robin','trend.Nico Robin'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_huerta','trend.Dolores Huerta'),('trend_fomc','trend.FOMC'),('trend_tucker','trend.Justin Tucker'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("""        if str(_x) == 'trend.Toledo': return 'disaster'  # 1511Z""","""        if str(_x) == 'trend.Dolores Huerta': return 'politics'  # 1611Z: labor and civil rights leader Dolores Huerta, United Farm Workers co-founder, died at 96 ("United Farm Workers" on the US list is the same event)
        if str(_x) == 'trend.Toledo': return 'disaster'  # 1511Z""")
R("if _c.endswith('1511Z.json') and '/28/' in _c: continue","if _c.endswith('1611Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T15Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T16Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"325 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 286 flat posts wait for their sixth run\"; its left_out also counts 5 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 5 reads; fields","{len(watch_unavailable)} unavailable, 8 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Dolores Huerta", "FOMC" and "Justin Tucker" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names without posts in 1511Z, "Dolores Huerta" and "United Farm Workers" are one event (Huerta, UFW co-founder, died at 96), "Justin Tucker" and "Butker" are one event (the Chiefs practice-squad signing), "FOMC" is the Fed decision due 2 PM ET today, and "Good Wednesday", "Hump Day" and "#NationalFirstRespondersDay" are greetings or a day of observance); all 17 due desks; no screening reads by id (the plan cut screen), so candidates were screened with the numbers the discovery reads returned and referenced posts not returned in includes were not captured; story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "and" and "my", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1406Z'","        _last = '2026-10-28T1511Z'")
R("f'not in requests/plan.json for 2026-10-28T15Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T16Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T15Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-28T16Z (only screen was cut)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['politics','world','defense','justice','disaster']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T17:00:00Z, end_time 2026-10-28T16:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.world, volume.defense, volume.justice, volume.disaster; counts 4 h old); each series is the 167 full hours 2026-10-21T17:00Z to 2026-10-28T15:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-27T22:43:00Z (the post\\'s creation, 22:43:05) and end_time 2026-10-27T23:03:00Z: (conversation_id:2115212717938078027 is:reply) and (quotes_of_tweet_id:2115212717938078027 -is:retweet); the plan gives context.top two reads, so one post: 2115212717938078027 (@DiscussingFilm, Thing 1 and Thing 3 searching for Thing 2 ahead of THE CAT IN THE HAT, 1.35M views), the most viewed post new this run that is not old content; 25 replies and 25 quote posts came back; the five most liked of each kind kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))"+s[b:]
a=s.index("            f'Day-band run (11:11 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (12:11 PM ET Oct 28 / 16:11 UTC Oct 28, the 16Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T16Z, 42 reads listed, screen cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 706 ids in its order, 8 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 286 flat posts the plan set aside and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, defense, justice, disaster, markets, business, ai, tech, science, medicine, entertainment, music, gaming, sports, internet and offbeat (17 reads; ideas and life not due). Volume: politics, world, defense, justice and disaster (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Dolores Huerta", "FOMC" and "Justin Tucker" (3 reads). rising.global: quote word "and" and repost word "my" (2 reads). context.top: 2 reads for 2115212717938078027 (25 replies and 25 quotes in the window; 5 of each kept). Screen: none (cut by the plan). '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1511Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1611Z.json'")
R("        'plan': '2026-10-28T15Z',","        'plan': '2026-10-28T16Z',")
R("    'context': [{'post_id': '2115116782046372003',","    'context': [{'post_id': '2115212717938078027',")
a=s.index("CTX_REPLIES = ['2115118185217147012'"); b=s.index("CTX_IDS = CTX_REPLIES + CTX_QUOTES",a)
s=s[:a]+"CTX_REPLIES = ['2115214886766776367','2115213449160757290','2115215393568833712','2115217194745463048','2115215152815509553']  # 1611Z: five most liked replies to DiscussingFilm 2115212717938078027 in its first 20 minutes\nCTX_QUOTES = ['2115213260689678677','2115213180834390145','2115215698901254177','2115215748432113856','2115214143221616895']  # 1611Z: five most liked quote posts in the window\n"+s[b:]
R("# 4b) context picks (1511Z)","# 4b) context picks (1511Z, 1611Z)")
open(p,'w').write(s); print('ok')
