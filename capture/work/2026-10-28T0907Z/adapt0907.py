p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/0800Z.json from saved','capture/2026/10/28/0907Z.json from saved')
R("work/2026-10-28T0800Z'","work/2026-10-28T0907Z'")
R("RUN_ID = '2026-10-28T0800Z'","RUN_ID = '2026-10-28T0907Z'")
R("STARTED = '2026-10-28T08:00:00Z'","STARTED = '2026-10-28T09:07:00Z'")
R("OBS_AT = '2026-10-28T08:01:00Z'","OBS_AT = '2026-10-28T09:08:00Z'")
R("READS_BEFORE = 808","READS_BEFORE = 790")
R("datetime(2026,10,28,8,1,tzinfo=timezone.utc).timestamp()  # 0800Z (","datetime(2026,10,28,9,8,tzinfo=timezone.utc).timestamp()  # 0907Z (0800Z used 08:01, ")
R("    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n",
  "    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n")
R("DUE = ['politics','entertainment','sports','internet']  # 0800Z: the plan (requests/plan.json for 2026-10-28T08Z) lists the four hourly desks; every other desk is due but cut",
  "DUE = ['politics','entertainment','sports','internet']  # 0907Z: the plan (requests/plan.json for 2026-10-28T09Z) lists the four hourly desks; every other desk is due but cut")
R("    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),\n",
  "    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),\n")
R("if _c.endswith('0800Z.json') and '/28/' in _c: continue","if _c.endswith('0907Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T08Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T09Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"324 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 228 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 4 reads; fields","{len(watch_unavailable)} unavailable, 4 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("sweeps.append(sweep('rising.global'",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'no reads of its own: cut by requests/plan.json for 2026-10-28T09Z (cut list: screen, desk.life, desk.ideas, desk.science, desk.business, desk.disaster, desk.defense, desk.offbeat, desk.gaming, desk.music, desk.medicine, desk.tech, desk.ai, desk.markets, desk.justice, desk.world, rising.global, context.top, viral.global); the list holds posts that clear the global floor/pace among those the plan reads returned: sensors culture/sports/online, hourly desks politics/entertainment/sports/internet and the posts they reference as returned in the includes; no screening read (screen cut), no trend-name reads',
    24,'partial','cut by the plan; only posts returned by the other plan reads were screened', viral_core))
"""+s[b:]
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T08Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T09Z'")
R("        _last = '2026-10-28T0707Z'","        _last = '2026-10-28T0800Z'")
R("f'not in requests/plan.json for 2026-10-28T08Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T09Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = ('cut by requests/plan.json for 2026-10-28T08Z (due, but over the overnight allowance of 20)'","reason = ('cut by requests/plan.json for 2026-10-28T09Z (due, but over the overnight allowance of 20)'")
R("else 'not due: requests/plan.json for 2026-10-28T08Z')","else 'not due: requests/plan.json for 2026-10-28T09Z')")
R("VOL_DESKS = ['politics','world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T10:00:00Z, end_time 2026-10-28T09:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science; counts 4 h old); each series is the 167 full hours 2026-10-21T10:00Z to 2026-10-28T08:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
R("'not read: cut by requests/plan.json for 2026-10-28T08Z',None,'skipped'","'not read: cut by requests/plan.json for 2026-10-28T09Z',None,'skipped'")
a=s.index("            f'Overnight-band run (4:00 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Overnight-band run (5:07 AM ET Oct 28 / 09:07 UTC Oct 28, the 09Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-28T09Z, 18 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 310 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 228 flat posts the plan set aside and the 4 standing unavailable posts are in its left_out and were not read (so 9 of the 47 pulse posts and 200 of the 225 story-cited posts were not re-read this run). '
            f'Desks: politics, entertainment, sports and internet (4 reads). Volume: markets, business, ai, tech and science (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). '
            f'Cut by the plan and not read: screen, desks life/ideas/science/business/disaster/defense/offbeat/gaming/music/medicine/tech/ai/markets/justice/world, rising.global, context.top, viral.global (so no trend-name, quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0800Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0907Z.json'")
R("        'plan': '2026-10-28T08Z',","        'plan': '2026-10-28T09Z',")
open(p,'w').write(s); print('ok')
