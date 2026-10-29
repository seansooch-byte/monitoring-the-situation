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
R('capture/2026/10/29/0705Z.json from saved','capture/2026/10/29/0759Z.json from saved')
R("work/2026-10-29T0705Z'","work/2026-10-29T0759Z'")
R("RUN_ID = '2026-10-29T0705Z'","RUN_ID = '2026-10-29T0759Z'")
R("STARTED = '2026-10-29T07:05:00Z'","STARTED = '2026-10-29T07:59:00Z'")
R("OBS_AT = '2026-10-29T07:06:00Z'","OBS_AT = '2026-10-29T08:00:00Z'")
R("READS_BEFORE = 789","READS_BEFORE = 769")
L("READS_USED = 20  # 0705Z","READS_USED = 18  # 0759Z: this run's 18 X calls, the plan's 18 reads (screen, viral.global trend names, rising.global and context.top cut by the plan); the counter fell 769 to 751; no 429 or 503 refusals")
R("datetime(2026,10,29,7,6,tzinfo=timezone.utc).timestamp()  # 0705Z (","datetime(2026,10,29,8,0,tzinfo=timezone.utc).timestamp()  # 0759Z (0705Z used 07:06, ")
R("    'trend_bobuecker': 'trend_bobuecker.txt', 'trend_hardy': 'trend_hardy.txt', 'trend_vando': 'trend_vando.txt',\n","")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 0759Z: the four hourly desks requests/plan.json for 2026-10-29T08Z lists; the other 15 are cut by it")
R("    ('trend_bobuecker','trend.Bob Uecker'),('trend_hardy','trend.Hardy'),('trend_vando','trend.Vando'),\n","")
R("if _c.endswith('0705Z.json') and '/29/' in _c: continue","if _c.endswith('0759Z.json') and '/29/' in _c: continue")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T06Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T08Z (contract/PLAN.md), in its order and in batches of 100 (400 ids; the plan\\'s note: \"344 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 300 flat posts wait for their sixth run\"; its left_out also counts 9 unavailable posts not listed); nothing added, dropped or reordered; ")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); hourly desks politics/entertainment/sports/internet; no trend-name reads (viral.global is in the cut list of requests/plan.json for 2026-10-29T08Z); no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T08Z',6,'skipped','cut by the plan (overnight band, allowance 20)',[]))
""")
R("        _last = '2026-10-29T0504Z'","        _last = '2026-10-29T0504Z'  # 0759Z: culture/sports/online last read in 0504Z")
R("f'not in requests/plan.json for 2026-10-29T06Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T08Z (the plan lists news/money/science again this run); last read in {_last}'")
R("reason = 'not due: listed under left_out.desks_not_due in requests/plan.json for 2026-10-29T06Z'","reason = 'cut by requests/plan.json for 2026-10-29T08Z (overnight band, allowance 20)'")
R("VOL_DESKS = ['world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T09:00:00Z, end_time 2026-10-29T08:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science: counts 5 h old); each series is the 167 full hours 2026-10-22T09:00Z to 2026-10-29T07:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-29T08Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (2:05 AM CT Oct 29","            f'{EXTRA_NOTE} '","""            f'Overnight-band run (2:59 AM CT Oct 29 / 07:59 UTC Oct 29, the 08Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-29T08Z, written 07:13Z; 18 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 400 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 300 flat posts the plan set aside wait for their sixth run and the 9 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut by the plan). Volume: markets, business, ai, tech and science (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads; the plan lists the same three groups as 0705Z). '
            f'Cut by the plan and not read: screen, viral.global trend names, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0705Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0759Z.json'")
R("        'plan': '2026-10-29T06Z',","        'plan': '2026-10-29T08Z',")
open(p,'w').write(s); print('ok')
