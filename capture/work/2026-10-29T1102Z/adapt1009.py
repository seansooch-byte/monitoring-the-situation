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
R('capture/2026/10/29/0908Z.json from saved','capture/2026/10/29/1009Z.json from saved')
R("work/2026-10-29T0908Z'","work/2026-10-29T1009Z'")
R("RUN_ID = '2026-10-29T0908Z'","RUN_ID = '2026-10-29T1009Z'")
R("STARTED = '2026-10-29T09:08:00Z'","STARTED = '2026-10-29T10:09:00Z'")
R("OBS_AT = '2026-10-29T09:10:00Z'","OBS_AT = '2026-10-29T10:11:00Z'")
R("READS_BEFORE = 751","READS_BEFORE = 733")
L("READS_USED = 18  # 0908Z","READS_USED = 20  # 1009Z: this run's 20 X calls, the plan's 20 reads (screen, rising.global and context.top cut by the plan); the counter fell 733 to 713; no 429 or 503 refusals")
R("datetime(2026,10,29,9,10,tzinfo=timezone.utc).timestamp()  # 0908Z (","datetime(2026,10,29,10,11,tzinfo=timezone.utc).timestamp()  # 1009Z (0908Z used 09:10, ")
R("    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_goodthursday': 'trend_goodthursday.txt', 'trend_ttpchopard': 'trend_ttpchopard.txt', 'trend_12hours': 'trend_12hours.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','entertainment','sports','internet']  # 1009Z: the four hourly desks requests/plan.json for 2026-10-29T10Z lists; the other 15 are cut by it")
R("    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),",
  "    ('trend_goodthursday','trend.Good Thursday'),('trend_ttpchopard','trend.TTP CHOPARD EXQUISITE'),('trend_12hours','trend.12 HOURS'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),")
R("        if str(_x) in ('trend.Bob Uecker','trend.Vando'): return 'sports'",
  "        if str(_x) == 'trend.12 HOURS': return 'internet'  # 1009Z: AO3 (Archive of Our Own) maintenance 'at least 12 hours'\n        if str(_x) == 'trend.TTP CHOPARD EXQUISITE': return 'entertainment'  # 1009Z: Thai actors Teetee and Por at the Chopard ICONSIAM opening (#TeeteePorXChopard on the US list is the same event)\n        if str(_x) == 'trend.Good Thursday': return 'life'  # 1009Z: morning greeting posts\n        if str(_x) in ('trend.Bob Uecker','trend.Vando'): return 'sports'")
R("if _c.endswith('0908Z.json') and '/29/' in _c: continue","if _c.endswith('1009Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
R("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T09Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T10Z (contract/PLAN.md), in its order and in batches of 100 (295 ids; the plan\\'s note: \"346 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 254 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; ")
R("{len(watch_unavailable)} unavailable, 4 reads; fields","{len(watch_unavailable)} unavailable, 3 reads; fields")
SPAN("    'sources: references followed one hop from every post read","',\n    24,'ok',None, viral_core))",
 "    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); trend names \"Good Thursday\", \"TTP CHOPARD EXQUISITE\" and \"12 HOURS\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first three top-ten US names not attached in a recent run, in list order; \"Brewers\", \"#WinOurWay\", \"#ThisIsMyCrew\" and \"Ueck\" are the Brewers World Series title already attached in 0401Z to 0705Z; \"#TeeteePorXChopard\" is the same event as \"TTP CHOPARD EXQUISITE\"; \"12 HOURS\" is the AO3 maintenance notice; \"#CARDCRUSH\" and \"Cubs\" were not read for the budget); hourly desks politics/entertainment/sports/internet; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace")
R("'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T09Z'","'quote and repost streams: not read, cut by requests/plan.json for 2026-10-29T10Z'")
R("        _last = '2026-10-29T0759Z'  # 0908Z: news/money/science last read in 0759Z","        _last = '2026-10-29T0908Z'  # 1009Z: culture/sports/online last read in 0908Z")
R("f'not in requests/plan.json for 2026-10-29T09Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T10Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'cut by requests/plan.json for 2026-10-29T09Z (overnight band, allowance 20)'","reason = 'cut by requests/plan.json for 2026-10-29T10Z (overnight band, allowance 20)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['politics','sports','internet','life','offbeat']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T11:00:00Z, end_time 2026-10-29T10:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.sports, volume.internet, volume.life, volume.offbeat: counts 5 h old); each series is the 167 full hours 2026-10-22T11:00Z to 2026-10-29T09:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-29T10Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Overnight-band run (4:08 AM CT Oct 29","            f'No open requests.","""            f'Overnight-band run (5:09 AM CT Oct 29 / 10:09 UTC Oct 29, the 10Z slot; band allowance 20): executed requests/plan.json (for_run 2026-10-29T10Z, written 09:13Z; 20 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 295 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 254 flat posts the plan set aside wait for their sixth run and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 cut by the plan). Volume: politics, sports, internet, life and offbeat (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Good Thursday", "TTP CHOPARD EXQUISITE" and "12 HOURS" (3 reads; "12 HOURS" is the AO3 maintenance notice, "TTP CHOPARD EXQUISITE" and "#TeeteePorXChopard" are one event). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0908Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/1009Z.json'")
R("        'plan': '2026-10-29T09Z',","        'plan': '2026-10-29T10Z',")
open(p,'w').write(s); print('ok')
