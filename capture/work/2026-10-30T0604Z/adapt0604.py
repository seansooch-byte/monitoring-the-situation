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
R('"""Build capture/2026/10/30/0505Z.json from saved','"""Build capture/2026/10/30/0604Z.json from saved')
R("capture/work/2026-10-30T0505Z'","capture/work/2026-10-30T0604Z'")
R("RUN_ID = '2026-10-30T0505Z'","RUN_ID = '2026-10-30T0604Z'")
R("STARTED = '2026-10-30T05:05:00Z'","STARTED = '2026-10-30T06:04:00Z'")
R("OBS_AT = '2026-10-30T05:06:00Z'","OBS_AT = '2026-10-30T06:06:00Z'")
R("READS_BEFORE = 867","READS_BEFORE = 826")
L("READS_USED = 41","READS_USED = 20  # 0604Z: this run's 20 X calls, the plan's 20 reads (watch 3, desks 4, volume 5, trends 2, sensors 3, viral.global 3; screen, rising.global and context.top cut by the plan); the counter fell 826 to 806; no 429 or 503 refusals")
R("datetime(2026,10,30,5,6,tzinfo=timezone.utc).timestamp()  # 0505Z (","datetime(2026,10,30,6,6,tzinfo=timezone.utc).timestamp()  # 0604Z (0505Z used 05:06, ")
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',","'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2'):",2)
R("""    'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_panthers': 'trend_panthers.txt', 'trend_bryceyoung': 'trend_bryceyoung.txt', 'trend_grizzlies': 'trend_grizzlies.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',
""","""    'trend_christianwatson': 'trend_christianwatson.txt', 'trend_redbaron': 'trend_redbaron.txt', 'trend_ahs13': 'trend_ahs13.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 0604Z: the four hourly desks requests/plan.json for 2026-10-30T06Z lists; the other 15 are in its left_out.desks_not_due")
R("""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_panthers','trend.Panthers'),('trend_bryceyoung','trend.Bryce Young'),('trend_grizzlies','trend.Grizzlies'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('trend_christianwatson','trend.Christian Watson'),('trend_redbaron','trend.Red Baron'),('trend_ahs13','trend.#AHS13'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x) == 'trend.Red Baron': return 'internet'","        if str(_x) == 'trend.#AHS13': return 'entertainment'  # 0604Z: American Horror Story season 13 finale reactions\n        if str(_x) == 'trend.Red Baron': return 'internet'")
R("if _c.endswith('0505Z.json') and '/30/' in _c: continue","if _c.endswith('0604Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T0405Z'  # 0505Z: news/money/science last read in 0405Z","_last = '2026-10-30T0505Z'  # 0604Z: culture/sports/online last read in 0505Z")
R("not in requests/plan.json for 2026-10-30T05Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T06Z (rotation: news/money/science this run)")
R("reason = 'not due in requests/plan.json for 2026-10-30T05Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-30T06Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("CTXR = _top3('context_replies.txt')","+ CTX_REPLIES + CTX_QUOTES","CTXR = []; CTXQ = []  # 0604Z: context.top cut by the plan\nCTX_REPLIES = []\nCTX_QUOTES = []\nCTX_IDS = []")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T05Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T06Z, in its order and in batches of 100 (279 ids; the plan\\'s note: \"59 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 10 flat posts wait for their sixth run\"; its left_out counts 10 slowed flat posts and 3 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); trend names \"Christian Watson\", \"Red Baron\" and \"#AHS13\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, \"Christian Watson\", \"Red Baron\", \"Josh Jacobs\" and \"#AHS13\" had no posts attached in 0505Z, and \"Josh Jacobs\" was not read because it is the same event as \"Christian Watson\", \"Panthers\", \"Packers\" and \"Bryce Young\": Panthers at Packers on Thursday Night Football, where Watson returned from the hospital to play; \"Red Baron\" is the fundraiser for the Red Baron worker; \"#AHS13\" is the American Horror Story season 13 finale); hourly desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","rising_ids[:30]))",
 "sweeps.append(sweep('rising.global','discovery',None,'quote and repost streams: not read, cut by requests/plan.json for 2026-10-30T06Z',6,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T07:00:00Z, end_time 2026-10-30T06:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-23T07:00Z to 2026-10-30T05:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-30T06Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))")
SPAN("            f'Day-band run (12:05 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Overnight-band run (1:04 AM CT Oct 30 / 06:04 UTC Oct 30, the 06Z slot; band allowance 20): requests/plan.json is for 2026-10-30T06Z (written 05:14Z after the 0505Z capture), so it was followed (20 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 279 ids in its order, 3 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 10 slowed flat posts and 3 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the other 15 not due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Christian Watson", "Red Baron" and "#AHS13" (3 reads). '
            f'Cut by the plan and not read: screen, rising.global, context.top (so no quote or repost reads; the tally is unchanged). Candidates screened with what the plan reads returned. '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T05Z',","'plan': '2026-10-30T06Z',")
SPAN("    'context': [{'post_id': '2115739289250156765',","\n","    'context': [],\n")
R("f'{REPO}/capture/2026/10/30/0505Z.json'","f'{REPO}/capture/2026/10/30/0604Z.json'")
open('build_capture.py','w').write(s)
print('ok')
