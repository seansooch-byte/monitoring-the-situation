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
R('"""Build capture/2026/10/31/0700Z.json from saved','"""Build capture/2026/10/31/0800Z.json from saved')
R("capture/work/2026-10-31T0700Z'","capture/work/2026-10-31T0800Z'")
R("RUN_ID = '2026-10-31T0700Z'","RUN_ID = '2026-10-31T0800Z'")
L("STARTED = ","STARTED = '2026-10-31T08:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T08:05:00Z'")
R("READS_BEFORE = 777","READS_BEFORE = 759")
L("READS_USED = 18","READS_USED = 20  # 0800Z: this run's 20 X calls, the plan's 20 reads (watch 4, desks 4, volume 4, trends 2, sensors 3, viral.global trend names 3; screen, rising.global and context.top cut by the plan); the counter fell 759 to 739; no 429 or 503 refusals")
R("datetime(2026,10,31,7,3,tzinfo=timezone.utc).timestamp()  # 0700Z (","datetime(2026,10,31,8,5,tzinfo=timezone.utc).timestamp()  # 0800Z (0700Z used 07:03, ")
R("    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n",
  "    'trend_mcrla4': 'trend_mcrla4.txt', 'trend_gerard': 'trend_gerard.txt', 'trend_lakers': 'trend_lakers.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n")
R("    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),",
  "    ('trend_mcrla4','trend.#mcrla4'),('trend_gerard','trend.gerard'),('trend_lakers','trend.Lakers'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0800Z: the 4 desks the plan for 2026-10-31T08Z lists")
R("if _c.endswith('0700Z.json') and '/31/' in _c: continue","if _c.endswith('0800Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T0600Z'  # 0700Z: news/money/science last read in 0600Z","_last = '2026-10-31T0700Z'  # 0800Z: culture/sports/online last read in 0700Z")
R("not in requests/plan.json for 2026-10-31T07Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T08Z (rotation: news/money/science this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T07Z (overnight band, allowance 20)","cut by requests/plan.json for 2026-10-31T08Z (overnight band, allowance 20)")
s=s.replace("not due in requests/plan.json for 2026-10-31T07Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T08Z (desks_not_due)")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T07Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T08Z, in its order and in batches of 100 (400 ids; its left_out counts 105 slowed, 290 over cap and 3 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); trend names \"#mcrla4\", \"gerard\" and \"Lakers\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0700Z; #mcrla4 and gerard are one event, My Chemical Romance\\'s fourth Los Angeles show (Gerard Way); Lakers is the Lakers v Warriors game already attached through Luka, Steph and Warriors; Poland and Tusk are the Constitutional Tribunal event already attached, Reaves, Podz and Yaxel were read in 0300Z to 0500Z); desks politics/entertainment/sports/internet; quote and repost streams and story clusters not read (rising.global cut by the plan, overnight band allowance 20); global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T07Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T08Z'")
R("start_time 2026-10-24T08:00:00Z, end_time 2026-10-31T07:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T08:00Z to 2026-10-31T06:00Z",
  "start_time 2026-10-24T09:00:00Z, end_time 2026-10-31T08:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T09:00Z to 2026-10-31T07:00Z")
s=s.replace("'not read: cut by requests/plan.json for 2026-10-31T07Z'","'not read: cut by requests/plan.json for 2026-10-31T08Z'")
a=s.index("            f'Overnight-band run (3:00 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Overnight-band run (4:00 AM EDT Oct 31 / 08:00 UTC Oct 31, the 08Z slot; band allowance 20): requests/plan.json is for 2026-10-31T08Z (written 07:09Z after the 0700Z run) and was followed top to bottom (20 reads listed). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 400 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 105 slowed flat posts, 290 over-cap posts and 3 unavailable posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 the plan lists; the others cut by the plan). Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#mcrla4", "gerard" and "Lakers" (3 reads). Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T07Z',","'plan': '2026-10-31T08Z',")
R("f'{REPO}/capture/2026/10/31/0700Z.json'","f'{REPO}/capture/2026/10/31/0800Z.json'")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x) in ('trend.#mcrla4','trend.gerard'): return 'music'  # 0800Z: My Chemical Romance's fourth Los Angeles show (Gerard Way), one event\n"+s[j:]
open('build_capture.py','w').write(s); print('ok')
