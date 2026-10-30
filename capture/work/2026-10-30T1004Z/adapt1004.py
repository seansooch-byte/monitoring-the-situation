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
R('"""Build capture/2026/10/30/0910Z.json from saved','"""Build capture/2026/10/30/1004Z.json from saved')
R("capture/work/2026-10-30T0910Z'","capture/work/2026-10-30T1004Z'")
R("RUN_ID = '2026-10-30T0910Z'","RUN_ID = '2026-10-30T1004Z'")
R("STARTED = '2026-10-30T09:10:00Z'","STARTED = '2026-10-30T10:04:00Z'")
R("OBS_AT = '2026-10-30T09:11:00Z'","OBS_AT = '2026-10-30T10:05:00Z'")
R("READS_BEFORE = 767","READS_BEFORE = 749")
L("READS_USED = 18","READS_USED = 20  # 1004Z: this run's 20 X calls (watch 3, desks 4, volume 5, trends 2, sensors 3, viral.global 3; screen, rising.global and context.top cut by the plan); the counter fell 749 to 729; no 429 or 503 refusals")
R("datetime(2026,10,30,9,11,tzinfo=timezone.utc).timestamp()  # 0910Z (","datetime(2026,10,30,10,5,tzinfo=timezone.utc).timestamp()  # 1004Z (0910Z used 09:11, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n","    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',\n")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",2)
R("    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_redfriday': 'trend_redfriday.txt', 'trend_avatarsevenshavens': 'trend_avatarsevenshavens.txt', 'trend_halloweeneve': 'trend_halloweeneve.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 1004Z: the four hourly desks requests/plan.json for 2026-10-30T10Z lists; the other 15 are cut")
R("""    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('trend_redfriday','trend.RED Friday'),('trend_avatarsevenshavens','trend.#AvatarSevensHavens'),('trend_halloweeneve','trend.Happy Halloween Eve'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x) == 'trend.#AHS13': return 'entertainment'",
  "        if str(_x) in ('trend.#AvatarSevensHavens','trend.#sevenhavens'): return 'entertainment'  # 1004Z: Avatar: Seven Havens episode reactions\n        if str(_x) in ('trend.RED Friday','trend.Happy Halloween Eve'): return 'life'  # 1004Z: Friday morning greeting posts (wear red for deployed troops; Halloween eve)\n        if str(_x) == 'trend.#AHS13': return 'entertainment'")
R("if _c.endswith('0910Z.json') and '/30/' in _c: continue","if _c.endswith('1004Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T0805Z'  # 0910Z: news/money/science last read in 0805Z","_last = '2026-10-30T0910Z'  # 1004Z: culture/sports/online last read in 0910Z")
R("not in requests/plan.json for 2026-10-30T09Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T10Z (rotation: news/money/science this run)")
R("reason = 'not read: requests/plan.json for 2026-10-30T09Z cut it (overnight band, allowance 20)'","reason = 'not read: requests/plan.json for 2026-10-30T10Z cut it (overnight band, allowance 20)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T09Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T10Z, in its order and in batches of 100 (260 ids; the plan\\'s note: \"46 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 22 flat posts wait for their sixth run\"; its left_out counts 22 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); trend names \"RED Friday\", \"#AvatarSevensHavens\" and \"Happy Halloween Eve\" (\"<name> lang:en is:retweet\", newest first, 25 each; top-ten US names with no posts attached in 0910Z; #sevenhavens is the same show as #AvatarSevensHavens; the Orm Kornnaphat/Leapmotor B03X names are one Thai fan campaign and were not read); hourly desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T09Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T10Z'")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T11:00:00Z, end_time 2026-10-30T10:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-23T11:00Z to 2026-10-30T09:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-30T10Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (4:10 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Overnight-band run (5:04 AM CT Oct 30 / 10:04 UTC Oct 30, the 10Z slot; band allowance 20): requests/plan.json is for 2026-10-30T10Z (written 09:14Z after the 0910Z capture), so it was followed (20 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 260 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 22 slowed and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "RED Friday", "#AvatarSevensHavens" and "Happy Halloween Eve" (3 reads; top-ten US names with no posts attached in 0910Z; the Orm Kornnaphat/Leapmotor names are one Thai fan campaign, not read). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T09Z',","'plan': '2026-10-30T10Z',")
R("f'{REPO}/capture/2026/10/30/0910Z.json'","f'{REPO}/capture/2026/10/30/1004Z.json'")
open('build_capture.py','w').write(s)
print('ok')
