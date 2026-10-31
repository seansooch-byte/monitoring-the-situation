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
R('"""Build capture/2026/10/31/0959Z.json from saved','"""Build capture/2026/10/31/1105Z.json from saved')
R("capture/work/2026-10-31T0959Z'","capture/work/2026-10-31T1105Z'")
R("RUN_ID = '2026-10-31T0959Z'","RUN_ID = '2026-10-31T1105Z'")
L("STARTED = ","STARTED = '2026-10-31T11:05:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T11:06:00Z'")
R("READS_BEFORE = 721","READS_BEFORE = 692")
L("READS_USED = 20","READS_USED = 21  # 1105Z: this run's 21 X calls: the plan's 20 reads (watch 3, desks 4, volume 5, trends 2, sensors 3, viral.global trend names 3; screen, rising.global and context.top cut by the plan) plus 1 wasted get_posts_by_ids call sent with a placeholder id (Invalid Request, counted); the counter fell 692 to 671; no 429 or 503 refusals")
R("datetime(2026,10,31,10,1,tzinfo=timezone.utc).timestamp()  # 1000Z (","datetime(2026,10,31,11,6,tzinfo=timezone.utc).timestamp()  # 1105Z (1000Z used 10:01, ")
R("    'trend_halloween': 'trend_halloween.txt', 'trend_nunew': 'trend_nunew.txt', 'trend_maniac': 'trend_maniac.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n",
  "    'trend_poland': 'trend_poland.txt', 'trend_goodsat': 'trend_goodsat.txt', 'trend_lakers': 'trend_lakers.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n")
R("    ('trend_halloween','trend.Happy Halloween'),('trend_nunew','trend.#BornToBeNuNewConcertD1'),('trend_maniac','trend.#YouManiacSeriesFinalEP'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),",
  "    ('trend_poland','trend.Poland'),('trend_goodsat','trend.Good Saturday'),('trend_lakers','trend.Lakers'),\n    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 1105Z: the 4 desks the plan for 2026-10-31T11Z lists")
R("if _c.endswith('0959Z.json') and '/31/' in _c: continue","if _c.endswith('1105Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-31T0900Z'  # 1000Z: culture/sports/online last read in 0900Z","_last = '2026-10-31T0959Z'  # 1105Z: news/money/science last read in 0959Z")
R("not in requests/plan.json for 2026-10-31T10Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-31T11Z (rotation: culture/sports/online this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T10Z (overnight band, allowance 20)","cut by requests/plan.json for 2026-10-31T11Z (overnight band, allowance 20)")
s=s.replace("not due in requests/plan.json for 2026-10-31T10Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T11Z (desks_not_due)")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T10Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T11Z, in its order and in batches of 100 (262 ids; its left_out counts 18 slowed, 0 over cap and 1 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); trend names \"Poland\", \"Good Saturday\" and \"Lakers\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0959Z and not read there; Poland and Tusk are one event, the Polish Constitutional Tribunal standoff; Happy Halloween, #BornToBeNuNewConcertD1 and #YouManiacSeriesFinalEP/MANIAC FINAL MOMENT were read in 0959Z; Luka and Steph already had posts); desks politics/entertainment/sports/internet; quote and repost streams and story clusters not read (rising.global cut by the plan, overnight band allowance 20); global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T10Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T11Z'")
R("start_time 2026-10-24T11:00:00Z, end_time 2026-10-31T10:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T11:00Z to 2026-10-31T09:00Z",
  "start_time 2026-10-24T12:00:00Z, end_time 2026-10-31T11:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T12:00Z to 2026-10-31T10:00Z")
s=s.replace("'not read: cut by requests/plan.json for 2026-10-31T10Z'","'not read: cut by requests/plan.json for 2026-10-31T11Z'")
a=s.index("            f'Overnight-band run (6:00 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Overnight-band run (7:05 AM EDT Oct 31 / 11:05 UTC Oct 31, the 11Z slot; band allowance 20): requests/plan.json is for 2026-10-31T11Z (written 10:05Z after the 0959Z run) and was followed top to bottom (20 reads listed). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 7:03 AM ET briefing used 9 between 0959Z and this run; 1 of the 21 was a wasted call sent with a placeholder id that X refused as an invalid request), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 262 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 18 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 the plan lists; the others cut by the plan). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Poland", "Good Saturday" and "Lakers" (3 reads). Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T10Z',","'plan': '2026-10-31T11Z',")
R("f'{REPO}/capture/2026/10/31/0959Z.json'","f'{REPO}/capture/2026/10/31/1105Z.json'")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.Poland': return 'world'  # 1105Z: the Polish Constitutional Tribunal standoff (Tusk), one event with Tusk/Polish\n"+s[j:]
open('build_capture.py','w').write(s); print('ok')
