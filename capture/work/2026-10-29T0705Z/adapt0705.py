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
R('capture/2026/10/29/0504Z.json from saved','capture/2026/10/29/0705Z.json from saved')
R("work/2026-10-29T0504Z'","work/2026-10-29T0705Z'")
R("RUN_ID = '2026-10-29T0504Z'","RUN_ID = '2026-10-29T0705Z'")
R("STARTED = '2026-10-29T05:04:00Z'","STARTED = '2026-10-29T07:05:00Z'")
R("OBS_AT = '2026-10-29T05:05:00Z'","OBS_AT = '2026-10-29T07:06:00Z'")
R("READS_BEFORE = 828","READS_BEFORE = 789")
L("READS_USED = 39  # 0504Z","READS_USED = 20  # 0705Z: this run's 20 X calls, the plan's 20 reads (screen, rising.global and context.top cut by the plan); the counter fell 789 to 769; no 429 or 503 refusals")
R("datetime(2026,10,29,5,5,tzinfo=timezone.utc).timestamp()  # 0504Z (","datetime(2026,10,29,7,6,tzinfo=timezone.utc).timestamp()  # 0705Z (0504Z used 05:05, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n")
R("""    'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_winourway': 'trend_winourway.txt', 'trend_contreras': 'trend_contreras.txt', 'trend_clippers': 'trend_clippers.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',
""","""    'trend_bobuecker': 'trend_bobuecker.txt', 'trend_hardy': 'trend_hardy.txt', 'trend_vando': 'trend_vando.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
L("DUE = ['politics','world','justice'","DUE = ['politics','entertainment','sports','internet']  # 0705Z: the four hourly desks requests/plan.json for 2026-10-29T06Z lists; the other 15 are in its left_out.desks_not_due")
R("""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_winourway','trend.#WinOurWay'),('trend_contreras','trend.William Contreras'),('trend_clippers','trend.Clippers'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('trend_bobuecker','trend.Bob Uecker'),('trend_hardy','trend.Hardy'),('trend_vando','trend.Vando'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("        if str(_x) in ('trend.#WinOurWay','trend.William Contreras','trend.Clippers'): return 'sports'  # 0504Z","        if str(_x) in ('trend.Bob Uecker','trend.Vando'): return 'sports'  # 0705Z: Brewers World Series title tributes to Bob Uecker; Lakers' Jarred Vanderbilt (Vando)\n        if str(_x) in ('trend.#WinOurWay','trend.William Contreras','trend.Clippers'): return 'sports'  # 0504Z")
R("if _c.endswith('0504Z.json') and '/29/' in _c: continue","if _c.endswith('0705Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T05Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T06Z (contract/PLAN.md; the newest plan, written 05:14Z for the 06Z slot whose run failed), in its order and in batches of 100 (372 ids; the plan\\'s note: \"345 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 237 flat posts wait for their sixth run\"; its left_out also counts 5 unavailable posts not listed); nothing added, dropped or reordered; ")
R("unavailable, 6 reads; fields","unavailable, 4 reads; fields")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); trend names "Bob Uecker", "Hardy" and "Vando" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "#WinOurWay", "William Contreras" and "Clippers" were attached in 0504Z and "Brewers", "#ThisIsMyCrew" and "#AEWDynamite" in 0401Z, "Cubs" was not read for the budget; "Brewers", "#WinOurWay", "#ThisIsMyCrew", "Bob Uecker" and "William Contreras" are all one event, the Milwaukee Brewers World Series title; "Hardy" mixes several people (Jaden Hardy, Will Hardy, JJ Hardy, Tom Hardy); "Vando" is the Lakers\\' Jarred Vanderbilt); hourly desks politics/entertainment/sports/internet; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T06Z',6,'skipped','cut by the plan (overnight band, allowance 20)',[]))
""")
R("        _last = '2026-10-29T0401Z'","        _last = '2026-10-29T0504Z'")
R("f'not in requests/plan.json for 2026-10-29T05Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T06Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-29T05Z (nothing cut)'","reason = 'not due: listed under left_out.desks_not_due in requests/plan.json for 2026-10-29T06Z'")
R("VOL_DESKS = ['politics','sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T08:00:00Z, end_time 2026-10-29T07:00:00Z, one read per desk for the 4 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster: counts 4 h old); each series is the 167 full hours 2026-10-22T08:00Z to 2026-10-29T06:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-29T06Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Day-band run (12:04 AM CT Oct 29","            f'{EXTRA_NOTE} '","""            f'Overnight-band run (2:05 AM CT Oct 29 / 07:05 UTC Oct 29, the 07Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-29T06Z, the newest plan: it was written for the 06Z slot, whose run failed and left no capture, and no 07Z plan exists; 20 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 372 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 237 flat posts the plan set aside wait for their sixth run and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 not due). Volume: world, defense, justice and disaster (4 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). '
            f'viral.global: trend names "Bob Uecker", "Hardy" and "Vando" (3 reads; "Bob Uecker" is the same Brewers World Series title as "Brewers" and "#WinOurWay"). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0504Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0705Z.json'")
R("        'plan': '2026-10-29T05Z',","        'plan': '2026-10-29T06Z',")
SPAN("    'context': [{'post_id': '2115443563655754171',","    'answers': ANSWERS,","    'context': [],\n")
SPAN("CTX_REPLIES = ['2115446958747971592'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = []  # 0705Z: context.top cut by the plan\nCTX_QUOTES = []\n")
R("('watch0','watch1','watch2','watch3','watch4','watch5')","('watch0','watch1','watch2','watch3')",2)
open(p,'w').write(s); print('ok')
