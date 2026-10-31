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
R('"""Build capture/2026/10/31/0800Z.json from saved','"""Build capture/2026/10/31/0900Z.json from saved')
R("capture/work/2026-10-31T0800Z'","capture/work/2026-10-31T0900Z'")
R("RUN_ID = '2026-10-31T0800Z'","RUN_ID = '2026-10-31T0900Z'")
L("STARTED = ","STARTED = '2026-10-31T09:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T09:01:00Z'")
R("READS_BEFORE = 759","READS_BEFORE = 739")
L("READS_USED = 20","READS_USED = 18  # 0900Z: this run's 18 X calls, the plan's 18 reads (watch 4, desks 4, volume 5, trends 2, sensors 3; screen, rising.global, context.top and viral.global cut by the plan); the counter fell 739 to 721; no 429 or 503 refusals")
R("datetime(2026,10,31,8,5,tzinfo=timezone.utc).timestamp()  # 0800Z (","datetime(2026,10,31,9,1,tzinfo=timezone.utc).timestamp()  # 0900Z (0800Z used 08:05, ")
R("    'trend_mcrla4': 'trend_mcrla4.txt', 'trend_gerard': 'trend_gerard.txt', 'trend_lakers': 'trend_lakers.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n",
  "    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n")
R("    ('trend_mcrla4','trend.#mcrla4'),('trend_gerard','trend.gerard'),('trend_lakers','trend.Lakers'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),",
  "    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0900Z: the 4 desks the plan for 2026-10-31T09Z lists")
R("if _c.endswith('0800Z.json') and '/31/' in _c: continue","if _c.endswith('0900Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T0700Z'  # 0800Z: culture/sports/online last read in 0700Z","_last = '2026-10-31T0800Z'  # 0900Z: news/money/science last read in 0800Z")
R("not in requests/plan.json for 2026-10-31T08Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T09Z (rotation: culture/sports/online this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T08Z (overnight band, allowance 20)","cut by requests/plan.json for 2026-10-31T09Z (overnight band, allowance 20)")
s=s.replace("not due in requests/plan.json for 2026-10-31T08Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T09Z (desks_not_due)")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T08Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T09Z, in its order and in batches of 100 (354 ids; its left_out counts 14 slowed, 0 over cap and 1 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); desks politics/entertainment/sports/internet; trend names, quote and repost streams and story clusters not read (viral.global and rising.global cut by the plan, overnight band allowance 20); global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T08Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T09Z'")
R("start_time 2026-10-24T09:00:00Z, end_time 2026-10-31T08:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T09:00Z to 2026-10-31T07:00Z",
  "start_time 2026-10-24T10:00:00Z, end_time 2026-10-31T09:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-24T10:00Z to 2026-10-31T08:00Z")
s=s.replace("'not read: cut by requests/plan.json for 2026-10-31T08Z'","'not read: cut by requests/plan.json for 2026-10-31T09Z'")
a=s.index("            f'Overnight-band run (4:00 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Overnight-band run (5:00 AM EDT Oct 31 / 09:00 UTC Oct 31, the 09Z slot; band allowance 20): requests/plan.json is for 2026-10-31T09Z (written 08:09Z after the 0800Z run) and was followed top to bottom (18 reads listed). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 354 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 14 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 the plan lists; the others cut by the plan). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'Cut by the plan and not read: screen, viral.global trend names, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T08Z',","'plan': '2026-10-31T09Z',")
R("f'{REPO}/capture/2026/10/31/0800Z.json'","f'{REPO}/capture/2026/10/31/0900Z.json'")
R("        if str(_x) in ('trend.#mcrla4','trend.gerard'): return 'music'  # 0800Z: My Chemical Romance's fourth Los Angeles show (Gerard Way), one event\n","")
open('build_capture.py','w').write(s); print('ok')
