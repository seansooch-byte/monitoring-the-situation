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
R('"""Build capture/2026/10/30/2006Z.json from saved','"""Build capture/2026/10/30/2102Z.json from saved')
R("capture/work/2026-10-30T2006Z'","capture/work/2026-10-30T2102Z'")
R("RUN_ID = '2026-10-30T2006Z'","RUN_ID = '2026-10-30T2102Z'")
L("STARTED = ","STARTED = '2026-10-30T21:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T21:03:00Z'")
R("READS_BEFORE = 426","READS_BEFORE = 384")
L("READS_USED = 42","READS_USED = 28  # 2102Z: this run's 28 X calls (watch 5, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, screen 2, context.top 2); the counter fell 384 to 356; no 429 or 503 refusals")
R("datetime(2026,10,30,20,7,tzinfo=timezone.utc).timestamp()  # 2006Z (","datetime(2026,10,30,21,3,tzinfo=timezone.utc).timestamp()  # 2102Z (2006Z used 20:07, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',  # 2102Z: two screen reads\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
R("    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',","    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',")
R("    'trend_demarcus': 'trend_demarcus.txt', 'trend_tusk': 'trend_tusk.txt', 'trend_honda': 'trend_honda.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_sungoddess': 'trend_sungoddess.txt', 'trend_hubbard': 'trend_hubbard.txt', 'trend_nisha': 'trend_nisha.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 2102Z: the four desks requests/plan.json for 2026-10-30T21Z lists")
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_demarcus','trend.Demarcus Henry'),('trend_tusk','trend.Tusk'),('trend_honda','trend.Honda'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_sungoddess','trend.Sun Goddess'),('trend_hubbard','trend.Stephen Hubbard'),('trend_nisha','trend.Nisha'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x)=='trend.Honda': return 'justice'  # 2006Z: workers run from an ICE operation at a Honda plant in Alabama\n",
  "        if str(_x)=='trend.Honda': return 'justice'  # 2006Z: workers run from an ICE operation at a Honda plant in Alabama\n        if str(_x)=='trend.Sun Goddess': return 'sports'  # 2102Z: Sun Goddess wins the Breeders' Cup Juvenile Fillies Turf\n        if str(_x)=='trend.Stephen Hubbard': return 'politics'  # 2102Z: Trump meets freed American Stephen Hubbard in the Oval Office\n        if str(_x)=='trend.Nisha': return 'entertainment'  # 2102Z: Avatar: Seven Havens fans on the character Nisha\n")
R("CTX_REPLIES = CTXR  # 2006Z: replies to surajit_ghosh2 2116025216795312542 in its first 20 minutes (none returned)",
  "CTX_REPLIES = CTXR  # 2102Z: replies to TMZ 2116187240233656429 in its first 20 minutes (19 returned)")
R("CTX_IDS = ['2116025216795312542'] + CTX_REPLIES","CTX_IDS = ['2116187240233656429'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'disaster' for _x in ['2116025216795312542']+CTXR+CTXQ})  # 2006Z:",
  "DESK_OVERRIDE_RUN.update({_x:'disaster' for _x in ['2116025216795312542']})\nDESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2116187240233656429']+CTXR+CTXQ})  # 2102Z: TMZ post on Bryce Hall's Halloween fight and its context replies and quotes are internet  # 2006Z:")
R("if _c.endswith('2006Z.json') and '/30/' in _c: continue","if _c.endswith('2102Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T1906Z'  # 2006Z: culture/sports/online last read in 1906Z","_last = '2026-10-30T2006Z'  # 2102Z: news/money/science last read in 2006Z")
R("not in requests/plan.json for 2026-10-30T20Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T21Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T20Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T21Z (desks_not_due)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T20Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T21Z, in its order and in batches of 100 (465 ids; the plan\\'s note: \"56 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 16 flat posts wait for their sixth run\"; its left_out counts 16 slowed, 0 over cap and 0 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 5 reads;")
SPAN("    'sources: references followed one hop from every post read, including","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 2 of the plan\\'s 3 reads by id: the 101 unread first-hop references, then the 24 unread second-hop references and leftovers; 1 Not Found and 1 not authorized); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Sun Goddess\", \"Stephen Hubbard\" and \"Nisha\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 2006Z not read in the last few runs (Halloween, Sam Altman, Tusk, Honda, Philo and Demarcus Henry were; DRAM is one event with Sam Altman)); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"it\" and \"that\" (2006Z used \"and\" and \"my\"), each quoted so X does not reject a bare stopword: (\"it\" lang:en is:quote -is:retweet), (\"that\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T22:00:00Z, end_time 2026-10-30T21:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-23T22:00Z to 2026-10-30T20:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T15:15:00Z (the post\\'s creation minute) and end_time 2026-10-30T15:35:00Z: (conversation_id:2116187240233656429 is:reply) and (quotes_of_tweet_id:2116187240233656429 -is:retweet); the plan gives context.top two reads, so one post: 2116187240233656429 (@TMZ post on Bryce Hall dressed as an inmate for Halloween and taking a beating, the biggest post new this run under 24 hours old at about 4.5M views); 19 replies and 4 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (3:06 PM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (4:02 PM CT Oct 30 / 21:02 UTC Oct 30, the 21Z slot; band allowance 42): requests/plan.json is for 2026-10-30T21Z (written 20:15Z after the 2006Z capture), so it was followed (29 reads listed) top to bottom; screen needed 2 of its 3 reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 465 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 16 slowed flat posts in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four the plan lists; the other 15 not due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Sun Goddess", "Stephen Hubbard" and "Nisha" (3 reads). rising.global: quote stream "it" and repost stream "that" (2 reads). context.top: TMZ 2116187240233656429 (2 reads). '
            f'Screen: 2 reads by id (101 unread first-hop references, then 24 second-hop and leftover references; 1 Not Found, 1 not authorized). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T20Z',","'plan': '2026-10-30T21Z',")
R("    'context': [{'post_id': '2116025216795312542',","    'context': [{'post_id': '2116187240233656429',")
R("f'{REPO}/capture/2026/10/30/2006Z.json'","f'{REPO}/capture/2026/10/30/2102Z.json'")
anchor="EXTRA_PRIVATE |= {'2116112047607861487'"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+open('skips2102.txt').read()+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
