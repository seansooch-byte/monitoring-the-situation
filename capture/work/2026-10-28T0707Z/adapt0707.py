p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/0608Z.json from saved','capture/2026/10/28/0707Z.json from saved')
R("work/2026-10-28T0608Z'","work/2026-10-28T0707Z'")
R("RUN_ID = '2026-10-28T0608Z'","RUN_ID = '2026-10-28T0707Z'")
R("STARTED = '2026-10-28T06:08:00Z'","STARTED = '2026-10-28T07:07:00Z'")
R("OBS_AT = '2026-10-28T06:09:00Z'","OBS_AT = '2026-10-28T07:08:00Z'")
R("READS_BEFORE = 845","READS_BEFORE = 827")
R("datetime(2026,10,28,6,9,tzinfo=timezone.utc).timestamp()  # 0608Z (","datetime(2026,10,28,7,8,tzinfo=timezone.utc).timestamp()  # 0707Z (0608Z used 06:09, ")
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',","'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",2)
R("""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'trend_blazers': 'trend_blazers.txt', 'trend_scottfoster': 'trend_scottfoster.txt', 'trend_rays': 'trend_rays.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
R("DUE = ['politics','entertainment','sports','internet']  # 0608Z: the plan (requests/plan.json for 2026-10-28T06Z) lists the four hourly desks; the others are not due (left_out.desks_not_due 6) or cut",
  "DUE = ['politics','entertainment','sports','internet']  # 0707Z: the plan (requests/plan.json for 2026-10-28T07Z) lists the four hourly desks; the others are not due (left_out.desks_not_due 6) or cut")
R("""    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
] + [""","""    ('trend_blazers','trend.Blazers'),('trend_scottfoster','trend.Scott Foster'),('trend_rays','trend.Rays'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
] + [""")
R("        if str(_x) in ('trend.49ers','trend.#WorldSeries'): return 'sports'","        if str(_x) in ('trend.Blazers','trend.Scott Foster'): return 'sports'  # 0707Z: Blazers beat the Lakers (NBA); referee Scott Foster in the same game\n        if str(_x) in ('trend.49ers','trend.#WorldSeries'): return 'sports'")
R("if _c.endswith('0608Z.json') and '/28/' in _c: continue","if _c.endswith('0707Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T06Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T07Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"326 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 238 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 4 reads; fields","{len(watch_unavailable)} unavailable, 3 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("sweeps.append(sweep('rising.global'",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); trend names "Blazers", "Scott Foster" and "Rays" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "Dame" and "Deni" are the same Blazers-Lakers game as "Blazers" and "Scott Foster", "Kessler" was not read for the budget, "Cooper Pratt" and "#WorldSeries" were attached in 0406Z and "Drohan" in 0501Z, and "Rays" is the same Brewers-Rays World Series); hourly desks politics/entertainment/sports/internet; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace',
    24,'ok',None, viral_core))
"""+s[b:]
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T06Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-28T07Z'")
R("        _last = '2026-10-28T0501Z'","        _last = '2026-10-28T0608Z'")
R("f'not in requests/plan.json for 2026-10-28T06Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T07Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = ('cut by requests/plan.json for 2026-10-28T06Z (due, but over the overnight allowance of 20)'","reason = ('cut by requests/plan.json for 2026-10-28T07Z (due, but over the overnight allowance of 20)'")
R("'not due: listed under left_out.desks_not_due in requests/plan.json for 2026-10-28T06Z')","'not due: listed under left_out.desks_not_due in requests/plan.json for 2026-10-28T07Z')")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T08:00:00Z, end_time 2026-10-28T07:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat, never counted before); each series is the 167 full hours 2026-10-21T08:00Z to 2026-10-28T06:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
R("'not read: cut by requests/plan.json for 2026-10-28T06Z',None,'skipped'","'not read: cut by requests/plan.json for 2026-10-28T07Z',None,'skipped'")
a=s.index("            f'Overnight-band run (2:08 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Overnight-band run (3:07 AM ET Oct 28 / 07:07 UTC Oct 28, the 07Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-28T07Z, 19 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 295 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 238 flat posts the plan set aside wait for their sixth run and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads). Volume: sports, internet, life and offbeat (4 reads, never counted before). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). '
            f'viral.global: trend names "Blazers", "Scott Foster" and "Rays" (3 reads; "Dame" and "Deni" are the same Blazers-Lakers game; "Rays" is the Brewers-Rays World Series). '
            f'Cut by the plan and not read: screen, desks offbeat/gaming/music/medicine/tech/ai/markets/justice/world, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0608Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0707Z.json'")
R("        'plan': '2026-10-28T06Z',","        'plan': '2026-10-28T07Z',")
open(p,'w').write(s); print('ok')
