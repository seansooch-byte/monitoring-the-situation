s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    assert s.count(start)>=1,start
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_arizona','trend.Arizona'),('trend_persona1','trend.Persona 1'),('trend_furtherado','trend.Further Ado'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_riftbound','trend.#Riftbound1Year'),('trend_tommycarr','trend.Tommy Carr'),('trend_syracuse','trend.Syracuse'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.#Riftbound1Year': return 'gaming'  # 2000Z: Riot's Riftbound trading card game first anniversary\n        if str(_x) in ('trend.Tommy Carr','trend.Syracuse'): return 'sports'  # 2000Z: Michigan QB Tommy Carr at Rutgers; Syracuse upsets No. 19 SMU\n"+s[j:]
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):  # noqa keep")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):\n","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):\n")
L("CTX_REPLIES = CTXR","CTX_REPLIES = CTXR  # 2000Z: replies to NICKIMINAJ 2116564175208018186 in its first 20 minutes (25 returned, the three most liked kept)")
L("CTX_QUOTES = CTXQ","CTX_QUOTES = CTXQ  # 2000Z: quotes in the window (25 returned, the three most liked kept)")
L("CTX_IDS = [","CTX_IDS = ['2116564175208018186'] + CTX_REPLIES + CTX_QUOTES  # 2000Z: the context post itself; 25 replies and 25 quotes returned")
R("if _c.endswith('1909Z.json') and '/31/' in _c: continue","if _c.endswith('2000Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T1802Z'  # 1909Z: news/money/science last read in 1802Z","_last = '2026-10-31T1909Z'  # 2000Z: culture/sports/online last read in 1909Z")
R("not in requests/plan.json for 2026-10-31T19Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T20Z (rotation: news/money/science this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T19Z (day band, allowance 42)","cut by requests/plan.json for 2026-10-31T20Z (day band, allowance 42)")
s=s.replace("not due in requests/plan.json for 2026-10-31T19Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T20Z (desks_not_due)")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T19Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T20Z, in its order and in batches of 100 (692 ids; its left_out slowed flat posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","',\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#Riftbound1Year\", \"Tommy Carr\" and \"Syracuse\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; of the top ten US names, Halloween is a repeat event, Rutgers and Iowa were read in 1802Z, Arizona was read in 1909Z and Navy has posts attached earlier; Tommy Carr is the Michigan at Rutgers game, read by the quarterback\\'s name); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"the\" and \"this\" (1909Z used \"just\" and \"what\"), each quoted so X does not reject a bare stopword: (\"the\" lang:en is:quote -is:retweet), (\"this\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T21:00:00Z, end_time 2026-10-31T20:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T21:00Z to 2026-10-31T19:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-31T16:13:00Z (the post\\'s creation minute) and end_time 2026-10-31T16:33:00Z: (conversation_id:2116564175208018186 is:reply) and (quotes_of_tweet_id:2116564175208018186 -is:retweet); the plan gives context.top two reads, so one post: 2116564175208018186 (NICKIMINAJ quote post saying \"his\" anger at his own parents was projected onto white people, 1.42M views, the biggest new post under 24 hours once a likely-paid iPhone post, already left out in 1602Z, is passed over); 25 replies and 25 quotes in the window, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
a=s.index("            f'Day-band run (2:09 PM CDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Day-band run (3:00 PM CDT Oct 31 / 20:00 UTC Oct 31, the 20Z slot; band allowance 42): requests/plan.json is for 2026-10-31T20Z (written after the 1909Z run) and was followed top to bottom (42 reads listed, screen cut). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1909Z and this run, the counter was 395 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 692 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the slowed flat posts in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#Riftbound1Year" (gaming: Riftbound card game anniversary), "Tommy Carr" (sports: Michigan at Rutgers) and "Syracuse" (sports: Syracuse upsets No. 19 SMU) (3 reads). rising.global: quote stream "the" and repost stream "this" (2 reads). context.top: NICKIMINAJ 2116564175208018186 (2 reads; 25 replies and 25 quotes in the 20-minute window). '
            f'Screen: cut by the plan; unread references left unread. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T19Z',","'plan': '2026-10-31T20Z',")
R("    'context': [{'post_id': '2116289709307469938',","    'context': [{'post_id': '2116564175208018186',")
R("f'{REPO}/capture/2026/10/31/1909Z.json'","f'{REPO}/capture/2026/10/31/2000Z.json'")
open('build_capture.py','w').write(s); print('ok')
