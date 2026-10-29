s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1607Z.json from saved","1707Z.json from saved")
R("capture/work/2026-10-29T1607Z'","capture/work/2026-10-29T1707Z'")
R("RUN_ID = '2026-10-29T1607Z'","RUN_ID = '2026-10-29T1707Z'")
R("STARTED = '2026-10-29T16:07:00Z'","STARTED = '2026-10-29T17:07:00Z'")
R("OBS_AT = '2026-10-29T16:08:00Z'","OBS_AT = '2026-10-29T17:09:00Z'")
R("READS_BEFORE = 551","READS_BEFORE = 509")
SPAN("READS_USED = 42","\n","READS_USED = 31  # 1707Z: this run's 31 X calls, the plan's 31 reads (watch 6, desks 5, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 509 to 478; no 429 or 503 refusals\n")
R("datetime(2026,10,29,16,8,tzinfo=timezone.utc).timestamp()  # 1607Z (","datetime(2026,10,29,17,9,tzinfo=timezone.utc).timestamp()  # 1707Z (1607Z used 16:08, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_this': 'quote_this.txt',
    'repost_my': 'repost_my.txt',
    'trend_nationalcatday': 'trend_nationalcatday.txt', 'trend_hyperliquid': 'trend_hyperliquid.txt', 'trend_istandwithtaylor': 'trend_istandwithtaylor.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_parsons': 'trend_parsons.txt', 'trend_mack': 'trend_mack.txt', 'trend_titans': 'trend_titans.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
SPAN("DUE = ['politics','world'","\n","DUE = ['politics','entertainment','sports','internet','life']  # 1707Z: the 5 desks requests/plan.json for 2026-10-29T17Z lists\n")
R("""    ('quote_this','quote'),('repost_my','repost'),
    ('trend_nationalcatday','trend.#NationalCatDay'),('trend_hyperliquid','trend.Hyperliquid'),('trend_istandwithtaylor','trend.#IStandWithTaylor'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_parsons','trend.Parsons'),('trend_mack','trend.Mack'),('trend_titans','trend.Titans'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) == 'trend.#NationalCatDay': return 'offbeat'  # 1607Z""","""        if str(_x) in ('trend.Parsons','trend.Mack','trend.Titans'): return 'sports'  # 1707Z: the Simmons-to-Bears trade and its comparisons (Micah Parsons, Khalil Mack trades); one event
        if str(_x) == 'trend.#NationalCatDay': return 'offbeat'  # 1607Z""")
R("('watch0','watch1','watch2','watch3','watch4','watch5','watch6')","('watch0','watch1','watch2','watch3','watch4','watch5')",2)
R("if _c.endswith('1607Z.json') and '/29/' in _c: continue","if _c.endswith('1707Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-29T1501Z'  # 1607Z: culture/sports/online last read in 1501Z","_last = '2026-10-29T1607Z'  # 1707Z: news/money/science last read in 1607Z")
R("not in requests/plan.json for 2026-10-29T16Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-29T17Z (rotation: culture/sports/online this run)")
R("reason = 'not due in requests/plan.json for 2026-10-29T16Z (listed in its left_out.desks_not_due)'","reason = 'not due in requests/plan.json for 2026-10-29T17Z (listed in its left_out.desks_not_due)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
SPAN("CTX_REPLIES = [","\nCTX_QUOTES = [","CTX_REPLIES = ['2115835473490792866','2115836268051628501','2115834484885246361']  # 1707Z: the three most liked replies to factpostnews 2115832586706563176 in its first 20 minutes (oliver_h3nry, PoliticOhMyGawd, UntetheredMango); the other 22 have 52 likes or fewer\nCTX_QUOTES = [")
SPAN("CTX_QUOTES = [","\n","CTX_QUOTES = ['2115834847344386125','2115835576826093689','2115835680156950931']  # 1707Z: the three most liked quotes in the window (JamieBonkiewicz, AntiToxicPeople, MatthewARein; PoliticOhMyGawd's quoting reply is kept as a reply); the rest have 157 likes or fewer\n")
R("CTX_IDS = ['2115823011399938182'] + CTX_REPLIES","CTX_IDS = ['2115832586706563176'] + CTX_REPLIES")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T16Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T17Z (contract/PLAN.md), in its order and in batches of 100 (520 ids; its left_out counts 235 slowed flat posts and 6 unavailable posts not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 6 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Parsons\", \"Mack\" and \"Titans\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1607Z, skipping \"Simmons\", \"Big Jeff\" and \"Ryan Poles\" as read in 1501Z and \"The Bears\" as the same event; all three are the Jeffery Simmons trade to the Bears and its comparisons with the Micah Parsons and Khalil Mack trades, one event); screen: 3 reads by id (118 unread references, then 25 second-hop)',\n")
SPAN("sweeps.append(sweep('rising.global','discovery',None,","\n    6,'ok'",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"it\" and \"that\" (1607Z used \"this\" and \"my\"), each quoted so X does not reject a bare stopword: (\"it\" lang:en is:quote -is:retweet), (\"that\" lang:en is:retweet), newest first, 25 each',\n    6,'ok'")
SPAN("sweeps.append(sweep('volume.desks','volume',None,","\n",
 "sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T18:00:00Z, end_time 2026-10-29T17:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas); each series is the 167 full hours 2026-10-22T18:00Z to 2026-10-29T16:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))\n")
SPAN("sweeps.append(sweep('context.top','context',None,","\n",
 "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T15:46:00Z (the post\\'s creation minute) and end_time 2026-10-29T16:06:00Z: (conversation_id:2115832586706563176 is:reply) and (quotes_of_tweet_id:2115832586706563176 -is:retweet); the plan gives context.top two reads, so one post: 2115832586706563176 (@factpostnews Fox interview with a Trump rally attendee, the biggest fresh post new this run at about 1.6M views in under 1.5 hours); 25 replies and 25 quotes in the window, the 3 most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))\n")
SPAN("            f'Day-band run (11:07 AM CT","Candidates screened with what the plan reads returned. '\n",
 "            f'Day-band run (12:07 PM CT Oct 29 / 17:07 UTC Oct 29, the 17Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-29T17Z; 31 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '\n"
 "            f'Watch: the plan\\'s 520 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 235 slowed flat posts and the 6 standing unavailable posts are in its left_out and were not read. '\n"
 "            f'Desks: politics, entertainment, sports, internet and life (5 reads). Volume: medicine, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads, the rotation). '\n"
 "            f'viral.global: trend names \"Parsons\", \"Mack\" and \"Titans\" (3 reads, one event: the Simmons trade). rising.global: quote stream \"it\" and repost stream \"that\" (2 reads). context.top: factpostnews 2115832586706563176 (2 reads). '\n"
 "            f'Screen: 3 reads by id (118 unread references, then 25 second-hop). '\n")
R("'plan': '2026-10-29T16Z',","'plan': '2026-10-29T17Z',")
R("    'context': [{'post_id': '2115823011399938182',","    'context': [{'post_id': '2115832586706563176',")
R("capture/2026/10/29/1607Z.json'","capture/2026/10/29/1707Z.json'")
anchor="DESK_OVERRIDE_RUN.update({'2115523333089354033'"
i=s.index(anchor); j=s.index("\n",i)+1
add=("DESK_OVERRIDE_RUN.update({'2115832586706563176':'politics','2115835473490792866':'politics','2115836268051628501':'politics','2115834484885246361':'politics','2115834847344386125':'politics','2115835576826093689':'politics','2115835680156950931':'politics'})  # 1707Z: factpostnews Fox interview with a Trump rally attendee and its context replies and quotes are politics\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s); print('ok')
