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
R('"""Build capture/2026/10/30/1004Z.json from saved','"""Build capture/2026/10/30/1106Z.json from saved')
R("capture/work/2026-10-30T1004Z'","capture/work/2026-10-30T1106Z'")
R("RUN_ID = '2026-10-30T1004Z'","RUN_ID = '2026-10-30T1106Z'")
R("STARTED = '2026-10-30T10:04:00Z'","STARTED = '2026-10-30T11:06:00Z'")
R("OBS_AT = '2026-10-30T10:05:00Z'","OBS_AT = '2026-10-30T11:07:00Z'")
R("READS_BEFORE = 749","READS_BEFORE = 716")
L("READS_USED = 20","READS_USED = 20  # 1106Z: this run's 20 X calls (watch 3, desks 4, volume 5, trends 2, sensors 3, viral.global 3; screen, rising.global and context.top cut by the plan); the counter fell 716 to 696 (it stood at 729 after 1004Z: 13 reads by the 7:03 AM ET briefing in between); no 429 or 503 refusals")
R("datetime(2026,10,30,10,5,tzinfo=timezone.utc).timestamp()  # 1004Z (","datetime(2026,10,30,11,7,tzinfo=timezone.utc).timestamp()  # 1106Z (1004Z used 10:05, ")
R("    'trend_redfriday': 'trend_redfriday.txt', 'trend_avatarsevenshavens': 'trend_avatarsevenshavens.txt', 'trend_halloweeneve': 'trend_halloweeneve.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_goodfriday': 'trend_goodfriday.txt', 'trend_happyfriyay': 'trend_happyfriyay.txt', 'trend_binance': 'trend_binance.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 1106Z: the four hourly desks requests/plan.json for 2026-10-30T11Z lists; the other 15 are cut")
R("""    ('trend_redfriday','trend.RED Friday'),('trend_avatarsevenshavens','trend.#AvatarSevensHavens'),('trend_halloweeneve','trend.Happy Halloween Eve'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('trend_goodfriday','trend.Good Friday'),('trend_happyfriyay','trend.Happy Friyay'),('trend_binance','trend.Binance'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x) == 'trend.#AHS13': return 'entertainment'",
  "        if str(_x) in ('trend.Good Friday','trend.Happy Friyay'): return 'life'  # 1106Z: Friday morning greeting posts\n        if str(_x) == 'trend.#AHS13': return 'entertainment'")
R("if _c.endswith('1004Z.json') and '/30/' in _c: continue","if _c.endswith('1106Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T0910Z'  # 1004Z: culture/sports/online last read in 0910Z","_last = '2026-10-30T1004Z'  # 1106Z: news/money/science last read in 1004Z")
R("not in requests/plan.json for 2026-10-30T10Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T11Z (rotation: culture/sports/online this run)")
R("reason = 'not read: requests/plan.json for 2026-10-30T10Z cut it (overnight band, allowance 20)'","reason = 'not read: requests/plan.json for 2026-10-30T11Z cut it (overnight band, allowance 20)'")
R("VOL_DESKS = ['business','ai','tech','science','medicine']","VOL_DESKS = ['politics','entertainment','music','gaming','ideas']")
R("'get_trends_by_woeid 23424977 max 20'","'get_trends_by_woeid 23424977 max 50'")
R("'get_trends_by_woeid 1 max 20'","'get_trends_by_woeid 1 max 50'")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T10Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T11Z, in its order and in batches of 100 (258 ids; the plan\\'s note: \"47 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 18 flat posts wait for their sixth run\"; its left_out counts 18 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors culture/sports/online (one read each, their own sweeps); trend names \"Good Friday\", \"Happy Friyay\" and \"Binance\" (\"<name> lang:en is:retweet\", newest first, 25 each; Good Friday and Happy Friyay are top-ten US names with no posts attached in 1004Z; Binance had one post attached in 1004Z and was read in place of the Orm Kornnaphat/Leapmotor B03X names, one Thai fan campaign; #Avatarsevenhavens is the same show as #AvatarSevensHavens, attached in 1004Z); hourly desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T10Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T11Z'")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T12:00:00Z, end_time 2026-10-30T11:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-23T12:00Z to 2026-10-30T10:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-30T11Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (5:04 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Overnight-band run (6:06 AM CT Oct 30 / 11:06 UTC Oct 30, the 11Z slot; band allowance 20): requests/plan.json is for 2026-10-30T11Z (written 10:11Z after the 1004Z capture), so it was followed (20 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; 729 were left after 1004Z, the 7:03 AM ET briefing used 13 in between), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 258 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 18 slowed and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut). Volume: politics, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Good Friday", "Happy Friyay" and "Binance" (3 reads; Good Friday and Happy Friyay had no posts attached in 1004Z; Binance had one and was read in place of the Orm Kornnaphat/Leapmotor names, one Thai fan campaign, not read). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T10Z',","'plan': '2026-10-30T11Z',")
R("f'{REPO}/capture/2026/10/30/1004Z.json'","f'{REPO}/capture/2026/10/30/1106Z.json'")
open('build_capture.py','w').write(s)
print('ok')
