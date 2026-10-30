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
R('"""Build capture/2026/10/30/0604Z.json from saved','"""Build capture/2026/10/30/0701Z.json from saved')
R("capture/work/2026-10-30T0604Z'","capture/work/2026-10-30T0701Z'")
R("RUN_ID = '2026-10-30T0604Z'","RUN_ID = '2026-10-30T0701Z'")
R("STARTED = '2026-10-30T06:04:00Z'","STARTED = '2026-10-30T07:01:00Z'")
R("OBS_AT = '2026-10-30T06:06:00Z'","OBS_AT = '2026-10-30T07:02:00Z'")
R("READS_BEFORE = 826","READS_BEFORE = 806")
L("READS_USED = 20","READS_USED = 20  # 0701Z: this run's 20 X calls, the plan's 20 reads (watch 3, trends 2, desks 4, sensors 3, viral.global 3, volume 5; screen, rising.global and context.top cut by the plan); the counter fell 806 to 786; no 429 or 503 refusals")
R("datetime(2026,10,30,6,6,tzinfo=timezone.utc).timestamp()  # 0604Z (","datetime(2026,10,30,7,2,tzinfo=timezone.utc).timestamp()  # 0701Z (0604Z used 06:06, ")
R("    'trend_christianwatson': 'trend_christianwatson.txt', 'trend_redbaron': 'trend_redbaron.txt', 'trend_ahs13': 'trend_ahs13.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_packers': 'trend_packers.txt', 'trend_grizzlies': 'trend_grizzlies.txt', 'trend_camboozer': 'trend_camboozer.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0701Z: the four hourly desks requests/plan.json for 2026-10-30T07Z lists; the other 15 are cut or in its left_out.desks_not_due")
R("""    ('trend_christianwatson','trend.Christian Watson'),('trend_redbaron','trend.Red Baron'),('trend_ahs13','trend.#AHS13'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('trend_packers','trend.Packers'),('trend_grizzlies','trend.Grizzlies'),('trend_camboozer','trend.Cam Boozer'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x) == 'trend.#AHS13': return 'entertainment'","        if str(_x) == 'trend.Cam Boozer': return 'sports'  # 0701Z: Grizzlies beat the Blazers to go 5-0; rookie Cam Boozer's triple-double (same event as Grizzlies)\n        if str(_x) == 'trend.#AHS13': return 'entertainment'")
R("if _c.endswith('0604Z.json') and '/30/' in _c: continue","if _c.endswith('0701Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T0505Z'  # 0604Z: culture/sports/online last read in 0505Z","_last = '2026-10-30T0604Z'  # 0701Z: news/money/science last read in 0604Z")
R("not in requests/plan.json for 2026-10-30T06Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T07Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-30T06Z (listed in its left_out.desks_not_due)'","reason = 'not read: requests/plan.json for 2026-10-30T07Z cut it (overnight band, allowance 20) or lists it in left_out.desks_not_due'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T06Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T07Z, in its order and in batches of 100 (289 ids; the plan\\'s note: \"54 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 12 flat posts wait for their sixth run\"; its left_out counts 12 slowed flat posts and 3 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); trend names \"Packers\", \"Grizzlies\" and \"Cam Boozer\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, \"Panthers\", \"Packers\", \"Bryce Young\", \"Grizzlies\", \"Cam Boozer\" and \"Josh Jacobs\" had no posts attached in 0604Z; \"Panthers\", \"Bryce Young\" and \"Josh Jacobs\" were not read because they are the same event as \"Packers\": Panthers at Packers on Thursday Night Football; \"Grizzlies\" and \"Cam Boozer\" are one event: the Grizzlies beat the Blazers 124-103 to go 5-0, rookie Cam Boozer with a triple-double); hourly desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T06Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T07Z'")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T08:00:00Z, end_time 2026-10-30T07:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-23T08:00Z to 2026-10-30T06:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-30T07Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (1:04 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Overnight-band run (2:01 AM CT Oct 30 / 07:01 UTC Oct 30, the 07Z slot; band allowance 20): requests/plan.json is for 2026-10-30T07Z (written 06:10Z after the 0604Z capture), so it was followed (20 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 289 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 12 slowed flat posts and 3 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut or not due). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Packers", "Grizzlies" and "Cam Boozer" (3 reads; Grizzlies and Cam Boozer are one event). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T06Z',","'plan': '2026-10-30T07Z',")
R("f'{REPO}/capture/2026/10/30/0604Z.json'","f'{REPO}/capture/2026/10/30/0701Z.json'")
open('build_capture.py','w').write(s)
print('ok')
