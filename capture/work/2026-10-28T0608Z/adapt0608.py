p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/0501Z.json from saved','capture/2026/10/28/0608Z.json from saved')
R("work/2026-10-28T0501Z'","work/2026-10-28T0608Z'")
R("RUN_ID = '2026-10-28T0501Z'","RUN_ID = '2026-10-28T0608Z'")
R("STARTED = '2026-10-28T05:01:00Z'","STARTED = '2026-10-28T06:08:00Z'")
R("OBS_AT = '2026-10-28T05:02:00Z'","OBS_AT = '2026-10-28T06:09:00Z'")
R("READS_BEFORE = 871","READS_BEFORE = 845")
R("datetime(2026,10,28,5,2,tzinfo=timezone.utc).timestamp()  # 0501Z (","datetime(2026,10,28,6,9,tzinfo=timezone.utc).timestamp()  # 0608Z (0501Z used 05:02, ")
R("""    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_drohan': 'trend_drohan.txt', 'trend_game5': 'trend_game5.txt', 'trend_benwilliamson': 'trend_benwilliamson.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt',
""","""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
R("DUE = ['politics','entertainment','sports','internet']  # 0501Z: the plan (requests/plan.json for 2026-10-28T05Z) lists the four hourly desks; the others were swept in 0406Z and are not due",
  "DUE = ['politics','entertainment','sports','internet']  # 0608Z: the plan (requests/plan.json for 2026-10-28T06Z) lists the four hourly desks; the others are not due (left_out.desks_not_due 6) or cut")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_drohan','trend.Drohan'),('trend_game5','trend.Game 5'),('trend_benwilliamson','trend.Ben Williamson'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("if _c.endswith('0501Z.json') and '/28/' in _c: continue","if _c.endswith('0608Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T05Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T06Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"325 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 228 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("sweeps.append(sweep('rising.global'",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'no reads of its own: cut by requests/plan.json for 2026-10-28T06Z (cut list: screen, desk.offbeat, desk.gaming, desk.music, desk.medicine, desk.tech, desk.ai, desk.markets, desk.justice, desk.world, rising.global, context.top, viral.global); the list holds posts that clear the global floor/pace among those the plan reads returned: sensors news/money/science, hourly desks politics/entertainment/sports/internet and the posts they reference as returned in the includes; no screening read (screen cut), no trend-name reads',
    24,'partial','cut by the plan; only posts returned by the other plan reads were screened', viral_core))
"""+s[b:]
a=s.index("sweeps.append(sweep('rising.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('rising.global','discovery',None,'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T06Z',6,'skipped','cut by the plan (overnight band, allowance 20)',[]))
"""+s[b:]
R("        _last = '2026-10-28T0406Z'","        _last = '2026-10-28T0501Z'")
R("f'not in requests/plan.json for 2026-10-28T05Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T06Z (rotation: news/money/science this run); last read in {_last}'")
R("        reason = 'not due: swept in 2026-10-28T0406Z; listed under left_out.desks_not_due in requests/plan.json for 2026-10-28T05Z'",
  "        reason = ('cut by requests/plan.json for 2026-10-28T06Z (due, but over the overnight allowance of 20)' if d in {'offbeat','gaming','music','medicine','tech','ai','markets','justice','world'} else 'not due: listed under left_out.desks_not_due in requests/plan.json for 2026-10-28T06Z')")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T07:00:00Z, end_time 2026-10-28T06:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas, never counted before); each series is the 167 full hours 2026-10-21T07:00Z to 2026-10-28T05:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-28T06Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))"+s[b:]
a=s.index("            f'Day-band run (1:01 AM ET"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Overnight-band run (2:08 AM ET Oct 28 / 06:08 UTC Oct 28, the 06Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-28T06Z, 18 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 313 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 228 flat posts the plan set aside wait for their sixth run and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads). Volume: medicine, entertainment, music, gaming and ideas (5 reads, never counted before). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). '
            f'Cut by the plan and not read: screen, desks offbeat/gaming/music/medicine/tech/ai/markets/justice/world, rising.global, context.top, viral.global (so no trend-name, quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'context': [{'post_id': '2114929641320497522', 'replies': [], 'quotes': []}],","'context': [],")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0501Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0608Z.json'")
R("        'plan': '2026-10-28T05Z',","        'plan': '2026-10-28T06Z',")
R("new_runs = (tally_runs + [{'run': RUN_ID, 'origins': sorted(stream_origins)}])[-6:]","new_runs = (tally_runs + ([{'run': RUN_ID, 'origins': sorted(stream_origins)}] if stream_origins else []))[-6:]  # 0608Z: no quote/repost stream read, tally unchanged")
open(p,'w').write(s); print('ok')
