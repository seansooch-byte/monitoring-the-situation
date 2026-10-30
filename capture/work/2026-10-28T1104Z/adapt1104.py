p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1006Z.json from saved','capture/2026/10/28/1104Z.json from saved')
R("work/2026-10-28T1006Z'","work/2026-10-28T1104Z'")
R("RUN_ID = '2026-10-28T1006Z'","RUN_ID = '2026-10-28T1104Z'")
R("STARTED = '2026-10-28T10:06:00Z'","STARTED = '2026-10-28T11:04:00Z'")
R("OBS_AT = '2026-10-28T10:07:00Z'","OBS_AT = '2026-10-28T11:05:00Z'")
R("READS_BEFORE = 772","READS_BEFORE = 752")
R("READS_USED = READS_BEFORE - READS_AFTER  # this run's X calls; no 429 refusals",
  "READS_USED = 20  # 1104Z: this run's 20 X calls; the counter fell 752 to 727 because the 7:03 AM ET daily briefing spent 5 reads on the shared counter during the run; no 429 refusals")
R("datetime(2026,10,28,10,7,tzinfo=timezone.utc).timestamp()  # 1006Z (","datetime(2026,10,28,11,5,tzinfo=timezone.utc).timestamp()  # 1104Z (1006Z used 10:07, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'trend_blazers': 'trend_blazers.txt', 'trend_worldseries': 'trend_worldseries.txt', 'trend_helluvabossspoilers': 'trend_helluvabossspoilers.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'trend_iryo': 'trend_iryo.txt', 'trend_octavia': 'trend_octavia.txt', 'trend_striker': 'trend_striker.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("DUE = ['politics','entertainment','sports','internet']  # 1006Z: the plan (requests/plan.json for 2026-10-28T10Z)","DUE = ['politics','entertainment','sports','internet']  # 1104Z: the plan (requests/plan.json for 2026-10-28T11Z)")
R("""    ('trend_blazers','trend.Blazers'),('trend_worldseries','trend.#WorldSeries'),('trend_helluvabossspoilers','trend.#HelluvaBossSpoilers'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('trend_iryo','trend.Iryo'),('trend_octavia','trend.Octavia'),('trend_striker','trend.Striker'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("""        if str(_x) in ('trend.Blazers','trend.Scott Foster'): return 'sports'""","""        if str(_x) == 'trend.Iryo': return 'disaster'  # 1104Z: Renfe AVE and Iryo high-speed trains collide near Los Yébenes, Toledo, Spain
        if str(_x) == 'trend.Octavia': return 'entertainment'  # 1104Z: Helluva Boss season 3 episode (Octavia and Stolas)
        if str(_x) in ('trend.Blazers','trend.Scott Foster'): return 'sports'""")
R("if _c.endswith('1006Z.json') and '/28/' in _c: continue","if _c.endswith('1104Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T10Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T11Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"323 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 237 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 3 reads; fields","{len(watch_unavailable)} unavailable, 4 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("sweeps.append(sweep('rising.global'",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); trend names "Iryo", "Octavia" and "Striker" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "Blazers", "Dame" and "#WorldSeries" had posts attached in 1006Z; "Good Wednesday" and "Happy Hump" are greetings; "Lipstick" and "Earrings" were not read for the budget; "Octavia" and "Striker" are both the new Helluva Boss episode (with "#HelluvaBossSpoilers" and "Fizz"), and the "Striker" stream also carries football posts; "Iryo" is the Renfe AVE and Iryo high-speed train collision near Los Yébenes, Toledo, Spain); hourly desks politics/entertainment/sports/internet; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace',
    24,'ok',None, viral_core))
"""+s[b:]
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T10Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T11Z'")
R("        _last = '2026-10-28T0907Z'","        _last = '2026-10-28T1006Z'")
R("f'not in requests/plan.json for 2026-10-28T10Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T11Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = ('cut by requests/plan.json for 2026-10-28T10Z (due, but over the overnight allowance of 20)'","reason = ('cut by requests/plan.json for 2026-10-28T11Z (due, but over the overnight allowance of 20)'")
R("else 'not due: requests/plan.json for 2026-10-28T10Z')","else 'not due: requests/plan.json for 2026-10-28T11Z')")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T12:00:00Z, end_time 2026-10-28T11:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat; counts 4 h old); each series is the 167 full hours 2026-10-21T12:00Z to 2026-10-28T10:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
R("'not read: cut by requests/plan.json for 2026-10-28T10Z',None,'skipped'","'not read: cut by requests/plan.json for 2026-10-28T11Z',None,'skipped'")
a=s.index("            f'Overnight-band run (6:06 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Overnight-band run (7:04 AM ET Oct 28 / 11:04 UTC Oct 28, the 11Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-28T11Z, 20 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the other 5 off the shared counter during the run were the 7:03 AM ET daily briefing), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 309 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 237 flat posts the plan set aside and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads). Volume: sports, internet, life and offbeat (4 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Iryo", "Octavia" and "Striker" (3 reads). '
            f'Cut by the plan and not read: screen, desks life/ideas/science/business/disaster/defense/offbeat/gaming/music/medicine/tech/ai/markets/justice/world, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1006Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1104Z.json'")
R("        'plan': '2026-10-28T10Z',","        'plan': '2026-10-28T11Z',")
open(p,'w').write(s); print('ok')
