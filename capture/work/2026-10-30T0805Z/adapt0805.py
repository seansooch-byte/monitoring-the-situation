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
R('"""Build capture/2026/10/30/0701Z.json from saved','"""Build capture/2026/10/30/0805Z.json from saved')
R("capture/work/2026-10-30T0701Z'","capture/work/2026-10-30T0805Z'")
R("RUN_ID = '2026-10-30T0701Z'","RUN_ID = '2026-10-30T0805Z'")
R("STARTED = '2026-10-30T07:01:00Z'","STARTED = '2026-10-30T08:05:00Z'")
R("OBS_AT = '2026-10-30T07:02:00Z'","OBS_AT = '2026-10-30T08:06:00Z'")
R("READS_BEFORE = 806","READS_BEFORE = 786")
L("READS_USED = 20","READS_USED = 19  # 0805Z: this run's 19 X calls (watch 4, trends 2, desks 4, volume 4, sensors 3, viral.global 2 of its 3; screen, rising.global and context.top cut by the plan); the counter fell 786 to 767; no 429 or 503 refusals")
R("datetime(2026,10,30,7,2,tzinfo=timezone.utc).timestamp()  # 0701Z (","datetime(2026,10,30,8,6,tzinfo=timezone.utc).timestamp()  # 0805Z (0701Z used 07:02, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',\n","    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n")
R("    'trend_packers': 'trend_packers.txt', 'trend_grizzlies': 'trend_grizzlies.txt', 'trend_camboozer': 'trend_camboozer.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_binance': 'trend_binance.txt', 'trend_ahs13': 'trend_ahs13.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0805Z: the four hourly desks requests/plan.json for 2026-10-30T08Z lists; the other 15 are cut or in its left_out.desks_not_due")
R("""    ('trend_packers','trend.Packers'),('trend_grizzlies','trend.Grizzlies'),('trend_camboozer','trend.Cam Boozer'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('trend_binance','trend.Binance'),('trend_ahs13','trend.#AHS13'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("if _c.endswith('0701Z.json') and '/30/' in _c: continue","if _c.endswith('0805Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T0604Z'  # 0701Z: news/money/science last read in 0604Z","_last = '2026-10-30T0701Z'  # 0805Z: culture/sports/online last read in 0701Z")
R("not in requests/plan.json for 2026-10-30T07Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T08Z (rotation: news/money/science this run)")
R("reason = 'not read: requests/plan.json for 2026-10-30T07Z cut it (overnight band, allowance 20) or lists it in left_out.desks_not_due'","reason = 'not read: requests/plan.json for 2026-10-30T08Z cut it (overnight band, allowance 20) or lists it in left_out.desks_not_due'")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T07Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T08Z, in its order and in batches of 100 (400 ids; the plan\\'s note: \"53 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 71 flat posts wait for their sixth run\"; its left_out counts 71 slowed, 242 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); trend names \"Binance\" and \"#AHS13\" (\"<name> lang:en is:retweet\", newest first, 25 each; of the top-ten US names only these two had no posts attached in 0701Z, so two of the plan\\'s three viral.global reads were used); hourly desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T07Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T08Z'")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T09:00:00Z, end_time 2026-10-30T08:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-23T09:00Z to 2026-10-30T07:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-30T08Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (2:01 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Overnight-band run (3:05 AM CT Oct 30 / 08:05 UTC Oct 30, the 08Z slot; band allowance 20): requests/plan.json is for 2026-10-30T08Z (written 07:06Z after the 0701Z capture), so it was followed (20 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 400 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 71 slowed, 242 over-cap and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut or not due). Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Binance" and "#AHS13" (2 of 3 reads; the only top-ten US names with no posts attached in 0701Z). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T07Z',","'plan': '2026-10-30T08Z',")
R("f'{REPO}/capture/2026/10/30/0701Z.json'","f'{REPO}/capture/2026/10/30/0805Z.json'")
open('build_capture.py','w').write(s)
print('ok')
