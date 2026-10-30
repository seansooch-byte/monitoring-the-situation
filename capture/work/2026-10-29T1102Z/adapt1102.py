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
R('capture/2026/10/29/1009Z.json from saved','capture/2026/10/29/1102Z.json from saved')
R("work/2026-10-29T1009Z'","work/2026-10-29T1102Z'")
R("RUN_ID = '2026-10-29T1009Z'","RUN_ID = '2026-10-29T1102Z'")
R("STARTED = '2026-10-29T10:09:00Z'","STARTED = '2026-10-29T11:02:00Z'")
R("OBS_AT = '2026-10-29T10:11:00Z'","OBS_AT = '2026-10-29T11:04:00Z'")
R("READS_BEFORE = 733","READS_BEFORE = 710")
L("READS_USED = 20  # 1009Z","READS_USED = 19  # 1102Z: this run's 19 X calls, the plan's 19 reads (screen, rising.global and context.top cut by the plan); the counter fell 710 to 691 (the plan expected 713 before; 3 reads went elsewhere between runs); no 429 or 503 refusals")
R("datetime(2026,10,29,10,11,tzinfo=timezone.utc).timestamp()  # 1009Z (","datetime(2026,10,29,11,4,tzinfo=timezone.utc).timestamp()  # 1102Z (1009Z used 10:11, ")
R("    'trend_goodthursday': 'trend_goodthursday.txt', 'trend_ttpchopard': 'trend_ttpchopard.txt', 'trend_12hours': 'trend_12hours.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_happyfridayeve': 'trend_happyfridayeve.txt', 'trend_nationalcatday': 'trend_nationalcatday.txt', 'trend_cardcrush': 'trend_cardcrush.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 1102Z: the four hourly desks requests/plan.json for 2026-10-29T11Z lists; the other 15 are cut by it")
R("    ('trend_goodthursday','trend.Good Thursday'),('trend_ttpchopard','trend.TTP CHOPARD EXQUISITE'),('trend_12hours','trend.12 HOURS'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),",
  "    ('trend_happyfridayeve','trend.Happy Friday Eve'),('trend_nationalcatday','trend.National Cat Day'),('trend_cardcrush','trend.#CARDCRUSH'),\n    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),")
R("        if str(_x) == 'trend.12 HOURS': return 'internet'",
  "        if str(_x) == 'trend.National Cat Day': return 'offbeat'  # 1102Z: cat photos and clips for National Cat Day (animals)\n        if str(_x) == 'trend.Happy Friday Eve': return 'life'  # 1102Z: morning greeting posts, like Good Thursday\n        if str(_x) == 'trend.12 HOURS': return 'internet'")
R("if _c.endswith('1009Z.json') and '/29/' in _c: continue","if _c.endswith('1102Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
R("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T10Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T11Z (contract/PLAN.md), in its order and in batches of 100 (300 ids; the plan\\'s note: \"341 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 238 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; ")
SPAN("    'sources: references followed one hop from every post read","',\n    24,'ok',None, viral_core))",
 "    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); trend names \"Happy Friday Eve\", \"National Cat Day\" and \"#CARDCRUSH\" (\"<name> lang:en is:retweet\", newest first, 25 each; \"#CARDCRUSH\" returned one post; the plan gives viral.global three reads; they are the first three top-ten US names not attached in the previous run, in list order; \"Good Thursday\", \"TTP CHOPARD EXQUISITE\" and \"12 HOURS\" were attached in 1009Z; \"#TeeteePorXChopard\" is the same event as \"TTP CHOPARD EXQUISITE\"; \"Brewers\" is the Brewers World Series title already attached in 0401Z to 0705Z; \"Shin Bet\" was not read for the budget); hourly desks politics/entertainment/sports/internet; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T10Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T11Z'")
R("        _last = '2026-10-29T0908Z'  # 1009Z: culture/sports/online last read in 0908Z","        _last = '2026-10-29T1009Z'  # 1102Z: news/money/science last read in 1009Z")
R("f'not in requests/plan.json for 2026-10-29T10Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T11Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'cut by requests/plan.json for 2026-10-29T10Z (overnight band, allowance 20)'","reason = 'cut by requests/plan.json for 2026-10-29T11Z (overnight band, allowance 20)'")
R("VOL_DESKS = ['politics','sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T12:00:00Z, end_time 2026-10-29T11:00:00Z, one read per desk for the 4 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster: counts 4 h old); each series is the 167 full hours 2026-10-22T12:00Z to 2026-10-29T10:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-29T11Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (5:09 AM CT Oct 29","            f'No open requests.","""            f'Overnight-band run (6:02 AM CT Oct 29 / 11:02 UTC Oct 29, the 11Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-29T11Z, written 10:14Z; 19 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 300 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 238 flat posts the plan set aside wait for their sixth run and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut by the plan). Volume: world, defense, justice and disaster (4 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Happy Friday Eve", "National Cat Day" and "#CARDCRUSH" (3 reads; "#CARDCRUSH" returned one post). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/1009Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/1102Z.json'")
R("        'plan': '2026-10-29T10Z',","        'plan': '2026-10-29T11Z',")
open(p,'w').write(s); print('ok')
