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
R('"""Build capture/2026/10/31/0900Z.json from saved','"""Build capture/2026/10/31/1000Z.json from saved')
R("capture/work/2026-10-31T0900Z'","capture/work/2026-10-31T1000Z'")
R("RUN_ID = '2026-10-31T0900Z'","RUN_ID = '2026-10-31T1000Z'")
L("STARTED = ","STARTED = '2026-10-31T09:59:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T10:01:00Z'")
R("READS_BEFORE = 739","READS_BEFORE = 721")
L("READS_USED = 18","READS_USED = 20  # 1000Z: this run's 20 X calls, the plan's 20 reads (watch 3, desks 4, volume 5, trends 2, sensors 3, viral.global trend names 3; screen, rising.global and context.top cut by the plan); the counter fell 721 to 701; no 429 or 503 refusals")
R("datetime(2026,10,31,9,1,tzinfo=timezone.utc).timestamp()  # 0900Z (","datetime(2026,10,31,10,1,tzinfo=timezone.utc).timestamp()  # 1000Z (0900Z used 09:01, ")
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',  # 0500Z: four watch reads","'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',  # 1000Z: three watch reads")
R("    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n",
  "    'trend_halloween': 'trend_halloween.txt', 'trend_nunew': 'trend_nunew.txt', 'trend_maniac': 'trend_maniac.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n")
R("    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),",
  "    ('trend_halloween','trend.Happy Halloween'),('trend_nunew','trend.#BornToBeNuNewConcertD1'),('trend_maniac','trend.#YouManiacSeriesFinalEP'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 1000Z: the 4 desks the plan for 2026-10-31T10Z lists")
R("if _c.endswith('0900Z.json') and '/31/' in _c: continue","if _c.endswith('1000Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T0800Z'  # 0900Z: news/money/science last read in 0800Z","_last = '2026-10-31T0900Z'  # 1000Z: culture/sports/online last read in 0900Z")
R("not in requests/plan.json for 2026-10-31T09Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T10Z (rotation: news/money/science this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T09Z (overnight band, allowance 20)","cut by requests/plan.json for 2026-10-31T10Z (overnight band, allowance 20)")
s=s.replace("not due in requests/plan.json for 2026-10-31T09Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T10Z (desks_not_due)")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T09Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T10Z, in its order and in batches of 100 (269 ids; its left_out counts 15 slowed, 0 over cap and 1 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); trend names \"Happy Halloween\", \"#BornToBeNuNewConcertD1\" and \"#YouManiacSeriesFinalEP\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0900Z; #YouManiacSeriesFinalEP and MANIAC FINAL MOMENT are one event, the final episode of the Thai series You Maniac; Lakers was read in 0800Z and is the Lakers v Warriors game already attached through Luka, Steph and Warriors; Tusk is the Polish Constitutional Tribunal event already attached through Poland); desks politics/entertainment/sports/internet; quote and repost streams and story clusters not read (rising.global cut by the plan, overnight band allowance 20); global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T09Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T10Z'")
R("start_time 2026-10-24T10:00:00Z, end_time 2026-10-31T09:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-24T10:00Z to 2026-10-31T08:00Z",
  "start_time 2026-10-24T11:00:00Z, end_time 2026-10-31T10:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T11:00Z to 2026-10-31T09:00Z")
s=s.replace("'not read: cut by requests/plan.json for 2026-10-31T09Z'","'not read: cut by requests/plan.json for 2026-10-31T10Z'")
a=s.index("            f'Overnight-band run (5:00 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Overnight-band run (6:00 AM EDT Oct 31 / 10:00 UTC Oct 31, the 10Z slot; band allowance 20): requests/plan.json is for 2026-10-31T10Z (written 09:04Z after the 0900Z run) and was followed top to bottom (20 reads listed). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 269 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 15 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 the plan lists; the others cut by the plan). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Happy Halloween", "#BornToBeNuNewConcertD1" and "#YouManiacSeriesFinalEP" (3 reads). Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T09Z',","'plan': '2026-10-31T10Z',")
R("f'{REPO}/capture/2026/10/31/0900Z.json'","f'{REPO}/capture/2026/10/31/1000Z.json'")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x) in ('trend.#YouManiacSeriesFinalEP','trend.MANIAC FINAL MOMENT'): return 'entertainment'  # 1000Z: final episode of the Thai series You Maniac, one event\n        if str(_x)=='trend.#BornToBeNuNewConcertD1': return 'music'  # 1000Z: day one of Thai singer NuNew's second concert\n"+s[j:]
# one event: MANIAC FINAL MOMENT shares the You Maniac posts
k=s.index("trend_posts['Raiders'] = ")
s=s[:k]+"for _a,_b in [('#YouManiacSeriesFinalEP','MANIAC FINAL MOMENT')]:\n    if trend_posts.get(_a): trend_posts[_b] = list(dict.fromkeys((trend_posts.get(_b) or []) + trend_posts[_a]))  # 1000Z: one event, the final episode of You Maniac\n"+s[k:]
open('build_capture.py','w').write(s); print('ok')
