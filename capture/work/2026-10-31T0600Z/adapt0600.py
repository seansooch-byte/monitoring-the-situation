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
R('"""Build capture/2026/10/31/0500Z.json from saved','"""Build capture/2026/10/31/0600Z.json from saved')
R("capture/work/2026-10-31T0500Z'","capture/work/2026-10-31T0600Z'")
R("RUN_ID = '2026-10-31T0500Z'","RUN_ID = '2026-10-31T0600Z'")
L("STARTED = ","STARTED = '2026-10-31T06:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T06:01:00Z'")
R("READS_BEFORE = 823","READS_BEFORE = 795")
L("READS_USED = 28","READS_USED = 18  # 0600Z: this run's 18 X calls, the plan's 18 reads (watch 4, desks 4, volume 5, trends 2, sensors 3; screen, rising.global, context.top and viral.global cut by the plan); the counter fell 795 to 777; no 429 or 503 refusals")
R("datetime(2026,10,31,5,1,tzinfo=timezone.utc).timestamp()  # 0500Z (","datetime(2026,10,31,6,1,tzinfo=timezone.utc).timestamp()  # 0600Z (0500Z used 05:01, ")
R("    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 0500Z: three screen reads; no request asked\n","")
R("""    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',
    'trend_podz': 'trend_podz.txt', 'trend_grimes': 'trend_grimes.txt', 'trend_lakers': 'trend_lakers.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""","""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
L("DUE = ['politics','entertainment'","DUE = ['politics','entertainment','sports','internet']  # 0600Z: the 4 desks the plan for 2026-10-31T06Z lists")
R("""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_podz','trend.Podz'),('trend_grimes','trend.Grimes'),('trend_lakers','trend.Lakers'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("if _c.endswith('0500Z.json') and '/31/' in _c: continue","if _c.endswith('0600Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T0400Z'  # 0500Z: news/money/science last read in 0400Z","_last = '2026-10-31T0500Z'  # 0600Z: culture/sports/online last read in 0500Z")
R("not in requests/plan.json for 2026-10-31T05Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T06Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-31T05Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-31T06Z (desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("CTXR = _top3('context_replies.txt')","+ CTX_REPLIES + CTX_QUOTES","CTXR = []; CTXQ = []  # 0600Z: context.top cut by the plan\nCTX_REPLIES = []\nCTX_QUOTES = []\nCTX_IDS = []")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T05Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T06Z, in its order and in batches of 100 (329 ids; its left_out counts 20 slowed, 0 over cap and 2 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); desks politics/entertainment/sports/internet; trend names, quote and repost streams and story clusters not read (viral.global and rising.global cut by the plan, overnight band allowance 20); global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","rising_ids[:30]))",
 "sweeps.append(sweep('rising.global','discovery',None,'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T06Z',6,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T07:00:00Z, end_time 2026-10-31T06:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T07:00Z to 2026-10-31T05:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-31T06Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Day-band run (1:00 AM EDT","media descriptions. '\n",
"""            f'Overnight-band run (2:00 AM EDT Oct 31 / 06:00 UTC Oct 31, the 06Z slot; band allowance 20): requests/plan.json is for 2026-10-31T06Z (written 05:06Z after the 0500Z run) and was followed top to bottom (18 reads listed). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 329 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 20 slowed flat posts and 2 unavailable posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the 4 due; the others not due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'Cut by the plan and not read: screen, viral.global trend names, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T05Z',","'plan': '2026-10-31T06Z',")
SPAN("    'context': [{'post_id': '2116293295278285299',","\n","    'context': [],\n")
R("f'{REPO}/capture/2026/10/31/0500Z.json'","f'{REPO}/capture/2026/10/31/0600Z.json'")
open('build_capture.py','w').write(s)
print('ok')
