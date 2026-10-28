p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/0907Z.json from saved','capture/2026/10/28/1006Z.json from saved')
R("work/2026-10-28T0907Z'","work/2026-10-28T1006Z'")
R("RUN_ID = '2026-10-28T0907Z'","RUN_ID = '2026-10-28T1006Z'")
R("STARTED = '2026-10-28T09:07:00Z'","STARTED = '2026-10-28T10:06:00Z'")
R("OBS_AT = '2026-10-28T09:08:00Z'","OBS_AT = '2026-10-28T10:07:00Z'")
R("READS_BEFORE = 790","READS_BEFORE = 772")
R("datetime(2026,10,28,9,8,tzinfo=timezone.utc).timestamp()  # 0907Z (","datetime(2026,10,28,10,7,tzinfo=timezone.utc).timestamp()  # 1006Z (0907Z used 09:08, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'trend_blazers': 'trend_blazers.txt', 'trend_worldseries': 'trend_worldseries.txt', 'trend_helluvabossspoilers': 'trend_helluvabossspoilers.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",2)
R("DUE = ['politics','entertainment','sports','internet']  # 0907Z: the plan (requests/plan.json for 2026-10-28T09Z)","DUE = ['politics','entertainment','sports','internet']  # 1006Z: the plan (requests/plan.json for 2026-10-28T10Z)")
R("""    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
] + [('desk_'""","""    ('trend_blazers','trend.Blazers'),('trend_worldseries','trend.#WorldSeries'),('trend_helluvabossspoilers','trend.#HelluvaBossSpoilers'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
] + [('desk_'""")
R("if _c.endswith('0907Z.json') and '/28/' in _c: continue","if _c.endswith('1006Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T09Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T10Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"323 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 245 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 4 reads; fields","{len(watch_unavailable)} unavailable, 3 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("sweeps.append(sweep('rising.global'",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); trend names "Blazers", "#WorldSeries" and "#HelluvaBossSpoilers" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; none of the top-ten US names had posts attached in 0907Z; "Dame", "Scott Foster" and "Deni" are the same Blazers-Lakers game as "Blazers"; "Drohan" and "Cooper Pratt" are the same Brewers-Rays World Series as "#WorldSeries"; "Good Wednesday" is a greeting and "Striker" was not read for the budget); hourly desks politics/entertainment/sports/internet; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace',
    24,'ok',None, viral_core))
"""+s[b:]
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T09Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T10Z'")
R("        _last = '2026-10-28T0800Z'","        _last = '2026-10-28T0907Z'")
R("f'not in requests/plan.json for 2026-10-28T09Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T10Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = ('cut by requests/plan.json for 2026-10-28T09Z (due, but over the overnight allowance of 20)'","reason = ('cut by requests/plan.json for 2026-10-28T10Z (due, but over the overnight allowance of 20)'")
R("else 'not due: requests/plan.json for 2026-10-28T09Z')","else 'not due: requests/plan.json for 2026-10-28T10Z')")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T11:00:00Z, end_time 2026-10-28T10:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas; counts 4 h old); each series is the 167 full hours 2026-10-21T11:00Z to 2026-10-28T09:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
R("'not read: cut by requests/plan.json for 2026-10-28T09Z',None,'skipped'","'not read: cut by requests/plan.json for 2026-10-28T10Z',None,'skipped'")
a=s.index("            f'Overnight-band run (5:07 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Overnight-band run (6:06 AM ET Oct 28 / 10:06 UTC Oct 28, the 10Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-28T10Z, 20 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 296 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 245 flat posts the plan set aside and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads). Volume: medicine, entertainment, music, gaming and ideas (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Blazers", "#WorldSeries" and "#HelluvaBossSpoilers" (3 reads). '
            f'Cut by the plan and not read: screen, desks life/ideas/science/business/disaster/defense/offbeat/gaming/music/medicine/tech/ai/markets/justice/world, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0907Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1006Z.json'")
R("        'plan': '2026-10-28T09Z',","        'plan': '2026-10-28T10Z',")
open(p,'w').write(s); print('ok')
