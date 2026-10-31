s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
R('"""Build capture/2026/10/31/0600Z.json from saved','"""Build capture/2026/10/31/0700Z.json from saved')
R("capture/work/2026-10-31T0600Z'","capture/work/2026-10-31T0700Z'")
R("RUN_ID = '2026-10-31T0600Z'","RUN_ID = '2026-10-31T0700Z'")
L("STARTED = ","STARTED = '2026-10-31T07:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T07:03:00Z'")
R("READS_BEFORE = 795","READS_BEFORE = 777")
L("READS_USED = 18","READS_USED = 18  # 0700Z: this run's 18 X calls, the plan's 18 reads (watch 4, desks 4, volume 5, trends 2, sensors 3; screen, rising.global, context.top and viral.global cut by the plan); the counter fell 777 to 759; no 429 or 503 refusals")
R("datetime(2026,10,31,6,1,tzinfo=timezone.utc).timestamp()  # 0600Z (","datetime(2026,10,31,7,3,tzinfo=timezone.utc).timestamp()  # 0700Z (0600Z used 06:01, ")
R("    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n",
  "    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n")
R("    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),",
  "    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0700Z: the 4 desks the plan for 2026-10-31T07Z lists")
R("if _c.endswith('0600Z.json') and '/31/' in _c: continue","if _c.endswith('0700Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T0500Z'  # 0600Z: culture/sports/online last read in 0500Z","_last = '2026-10-31T0600Z'  # 0700Z: news/money/science last read in 0600Z")
R("not in requests/plan.json for 2026-10-31T06Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T07Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-31T06Z (desks_not_due)'",
  "reason = ('not read: cut by requests/plan.json for 2026-10-31T07Z (overnight band, allowance 20)' if f'desk.{d}' in PLAN_CUT else 'not read: not due in requests/plan.json for 2026-10-31T07Z (desks_not_due)')")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']\nPLAN_CUT = set(json.load(open(f'{W}/plan.json')).get('cut') or [])" if False else "VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
R("all_desks = [d['id'] for d in desks['desks']]","all_desks = [d['id'] for d in desks['desks']]\nPLAN_CUT = set(json.load(open(f'{W}/plan.json')).get('cut') or [])")
s=s.replace("f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T06Z, in its order and in batches of 100 (329 ids; its left_out counts 20 slowed, 0 over cap and 2 unavailable, not listed)",
 "f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T07Z, in its order and in batches of 100 (312 ids; its left_out counts 21 slowed, 0 over cap and 1 unavailable, not listed)")
assert "2026-10-31T07Z, in its order" in s
R("sensors news/money/science (one read each, their own sweeps)","sensors culture/sports/online (one read each, their own sweeps)")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T06Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T07Z'")
R("start_time 2026-10-24T07:00:00Z, end_time 2026-10-31T06:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T07:00Z to 2026-10-31T05:00Z",
  "start_time 2026-10-24T08:00:00Z, end_time 2026-10-31T07:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T08:00Z to 2026-10-31T06:00Z")
R("'not read: cut by requests/plan.json for 2026-10-31T06Z'","'not read: cut by requests/plan.json for 2026-10-31T07Z'")
a=s.index("            f'Overnight-band run (2:00 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Overnight-band run (3:00 AM EDT Oct 31 / 07:00 UTC Oct 31, the 07Z slot; band allowance 20): requests/plan.json is for 2026-10-31T07Z (written 06:06Z after the 0600Z run) and was followed top to bottom (18 reads listed). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 312 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 21 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 the plan lists; the others not due or cut by the plan). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'Cut by the plan and not read: screen, viral.global trend names, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T06Z',","'plan': '2026-10-31T07Z',")
R("f'{REPO}/capture/2026/10/31/0600Z.json'","f'{REPO}/capture/2026/10/31/0700Z.json'")
open('build_capture.py','w').write(s); print('ok')
