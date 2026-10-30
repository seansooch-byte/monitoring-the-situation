p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    a=s.index(start); b=s.index(end,a); s=s[:a]+new+s[b:]
R('capture/2026/10/29/0759Z.json from saved','capture/2026/10/29/0908Z.json from saved')
R("work/2026-10-29T0759Z'","work/2026-10-29T0908Z'")
R("RUN_ID = '2026-10-29T0759Z'","RUN_ID = '2026-10-29T0908Z'")
R("STARTED = '2026-10-29T07:59:00Z'","STARTED = '2026-10-29T09:08:00Z'")
R("OBS_AT = '2026-10-29T08:00:00Z'","OBS_AT = '2026-10-29T09:10:00Z'")
R("READS_BEFORE = 769","READS_BEFORE = 751")
L("READS_USED = 18  # 0759Z","READS_USED = 18  # 0908Z: this run's 18 X calls, the plan's 18 reads (screen, viral.global trend names, rising.global and context.top cut by the plan); the counter fell 751 to 733; no 429 or 503 refusals")
R("datetime(2026,10,29,8,0,tzinfo=timezone.utc).timestamp()  # 0759Z (","datetime(2026,10,29,9,10,tzinfo=timezone.utc).timestamp()  # 0908Z (0759Z used 08:00, ")
R("    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0908Z: the four hourly desks requests/plan.json for 2026-10-29T09Z lists; the other 15 are cut by it")
R("    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
R("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
R("if _c.endswith('0759Z.json') and '/29/' in _c: continue","if _c.endswith('0908Z.json') and '/29/' in _c: continue")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T08Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T09Z (contract/PLAN.md), in its order and in batches of 100 (333 ids; the plan\\'s note: \"345 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 235 flat posts wait for their sixth run\"; its left_out also counts 5 unavailable posts not listed); nothing added, dropped or reordered; ")
R("sensors news/money/science (one read each, their own sweeps); hourly desks","sensors culture/sports/online (one read each, their own sweeps); hourly desks")
R("(viral.global is in the cut list of requests/plan.json for 2026-10-29T08Z)","(viral.global is in the cut list of requests/plan.json for 2026-10-29T09Z)")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T08Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T09Z'")
R("        _last = '2026-10-29T0504Z'  # 0759Z: culture/sports/online last read in 0504Z","        _last = '2026-10-29T0759Z'  # 0908Z: news/money/science last read in 0759Z")
R("f'not in requests/plan.json for 2026-10-29T08Z (the plan lists news/money/science again this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T09Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'cut by requests/plan.json for 2026-10-29T08Z (overnight band, allowance 20)'","reason = 'cut by requests/plan.json for 2026-10-29T09Z (overnight band, allowance 20)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T10:00:00Z, end_time 2026-10-29T09:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 5 h old); each series is the 167 full hours 2026-10-22T10:00Z to 2026-10-29T08:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-29T09Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (2:59 AM CT Oct 29","            f'{EXTRA_NOTE} '","""            f'Overnight-band run (4:08 AM CT Oct 29 / 09:08 UTC Oct 29, the 09Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-29T09Z, written 08:04Z; 18 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 333 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 235 flat posts the plan set aside wait for their sixth run and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut by the plan). Volume: medicine, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '
            f'Cut by the plan and not read: screen, viral.global trend names, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0759Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0908Z.json'")
R("        'plan': '2026-10-29T08Z',","        'plan': '2026-10-29T09Z',")
open(p,'w').write(s); print('ok')
