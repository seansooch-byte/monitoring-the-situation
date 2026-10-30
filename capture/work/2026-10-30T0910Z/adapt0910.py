s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/30/0805Z.json from saved','"""Build capture/2026/10/30/0910Z.json from saved')
R("capture/work/2026-10-30T0805Z'","capture/work/2026-10-30T0910Z'")
R("RUN_ID = '2026-10-30T0805Z'","RUN_ID = '2026-10-30T0910Z'")
R("STARTED = '2026-10-30T08:05:00Z'","STARTED = '2026-10-30T09:10:00Z'")
R("OBS_AT = '2026-10-30T08:06:00Z'","OBS_AT = '2026-10-30T09:11:00Z'")
R("READS_BEFORE = 786","READS_BEFORE = 767")
L("READS_USED = 19","READS_USED = 18  # 0910Z: this run's 18 X calls (watch 4, desks 4, volume 5, trends 2, sensors 3; screen, viral.global, rising.global and context.top cut by the plan); the counter fell 767 to 749; no 429 or 503 refusals")
R("datetime(2026,10,30,8,6,tzinfo=timezone.utc).timestamp()  # 0805Z (","datetime(2026,10,30,9,11,tzinfo=timezone.utc).timestamp()  # 0910Z (0805Z used 08:06, ")
R("    'trend_binance': 'trend_binance.txt', 'trend_ahs13': 'trend_ahs13.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0910Z: the four hourly desks requests/plan.json for 2026-10-30T09Z lists; the other 15 are cut")
R("""    ('trend_binance','trend.Binance'),('trend_ahs13','trend.#AHS13'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("if _c.endswith('0805Z.json') and '/30/' in _c: continue","if _c.endswith('0910Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T0701Z'  # 0805Z: culture/sports/online last read in 0701Z","_last = '2026-10-30T0805Z'  # 0910Z: news/money/science last read in 0805Z")
R("not in requests/plan.json for 2026-10-30T08Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T09Z (rotation: culture/sports/online this run)")
R("reason = 'not read: requests/plan.json for 2026-10-30T08Z cut it (overnight band, allowance 20) or lists it in left_out.desks_not_due'","reason = 'not read: requests/plan.json for 2026-10-30T09Z cut it (overnight band, allowance 20)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T08Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T09Z, in its order and in batches of 100 (346 ids; the plan\\'s note: \"51 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 21 flat posts wait for their sixth run\"; its left_out counts 21 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); trend names not read (requests/plan.json for 2026-10-30T09Z cut viral.global); hourly desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T08Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T09Z'")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T10:00:00Z, end_time 2026-10-30T09:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-23T10:00Z to 2026-10-30T08:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-30T09Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (3:05 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Overnight-band run (4:10 AM CT Oct 30 / 09:10 UTC Oct 30, the 09Z slot; band allowance 20): requests/plan.json is for 2026-10-30T09Z (written 08:10Z after the 0805Z capture), so it was followed (18 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 346 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 21 slowed and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '
            f'Cut by the plan and not read: screen, viral.global (no trend-name streams), rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T08Z',","'plan': '2026-10-30T09Z',")
R("f'{REPO}/capture/2026/10/30/0805Z.json'","f'{REPO}/capture/2026/10/30/0910Z.json'")
open('build_capture.py','w').write(s)
print('ok')
