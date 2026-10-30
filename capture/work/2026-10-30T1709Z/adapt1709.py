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
R('"""Build capture/2026/10/30/1608Z.json from saved','"""Build capture/2026/10/30/1709Z.json from saved')
R("capture/work/2026-10-30T1608Z'","capture/work/2026-10-30T1709Z'")
R("RUN_ID = '2026-10-30T1608Z'","RUN_ID = '2026-10-30T1709Z'")
L("STARTED = ","STARTED = '2026-10-30T17:09:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T17:10:00Z'")
R("READS_BEFORE = 561","READS_BEFORE = 519")
L("READS_USED = 42","READS_USED = 30  # 1709Z: this run's 30 X calls (watch 6, desks 4, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 519 to 489; no 429 or 503 refusals")
R("datetime(2026,10,30,16,9,tzinfo=timezone.utc).timestamp()  # 1608Z (","datetime(2026,10,30,17,10,tzinfo=timezone.utc).timestamp()  # 1709Z (1608Z used 16:09, ")
R("'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',\n","'watch4': 'watch4.txt', 'watch5': 'watch5.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):",2)
R("    'quote_that': 'quote_that.txt',\n    'repost_just': 'repost_just.txt',","    'quote_what': 'quote_what.txt',\n    'repost_the': 'repost_the.txt',")
R("    'trend_lastfour': 'trend_lastfour.txt', 'trend_goodfriday': 'trend_goodfriday.txt', 'trend_kansasiowa': 'trend_kansasiowa.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',",
  "    'trend_philo': 'trend_philo.txt', 'trend_binance': 'trend_binance.txt', 'trend_battlefront': 'trend_battlefront.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',")
L("DUE = ['politics','world'","DUE = ['politics','entertainment','sports','internet']  # 1709Z: the four desks requests/plan.json for 2026-10-30T17Z lists")
R("""    ('quote_that','quote'),('repost_just','repost'),
    ('trend_lastfour','trend.#LastFourWatched'),('trend_goodfriday','trend.Good Friday'),('trend_kansasiowa','trend.Kansas and Iowa'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_what','quote'),('repost_the','repost'),
    ('trend_philo','trend.Philo'),('trend_binance','trend.Binance'),('trend_battlefront','trend.Battlefront 3'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("        if str(_x)=='trend.Kansas and Iowa': return 'politics'  # 1608Z: Trump reinstates Sunday rallies in Kansas and Iowa\n",
  "        if str(_x)=='trend.Kansas and Iowa': return 'politics'  # 1608Z: Trump reinstates Sunday rallies in Kansas and Iowa\n        if str(_x)=='trend.Philo': return 'sports'  # 1709Z: Florida starts QB Aaron Philo against Georgia\n        if str(_x)=='trend.Battlefront 3': return 'gaming'  # 1709Z: EA chose to invest in Star Wars: Battlefront 3 (BioWare shutdown)\n")
R("CTX_REPLIES = CTXR  # 1608Z: replies to SMO_VZ 2115940979039404540 in its first 20 minutes; relevancy returned none",
  "CTX_REPLIES = CTXR  # 1709Z: replies to nine 2115927574329057714 in its first 20 minutes (one returned)")
R("CTX_IDS = ['2115940979039404540'] + CTX_REPLIES","CTX_IDS = ['2115927574329057714'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'world' for _x in ['2115940979039404540']+CTXR+CTXQ})  # 1608Z:",
  "DESK_OVERRIDE_RUN.update({_x:'world' for _x in ['2115940979039404540']})\nDESK_OVERRIDE_RUN.update({_x:'markets' for _x in ['2115927574329057714']+CTXR+CTXQ})  # 1709Z: nine post on the Binance hacker and Tether's freeze is markets  # 1608Z:")
R("if _c.endswith('1608Z.json') and '/30/' in _c: continue","if _c.endswith('1709Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("_last = '2026-10-30T1507Z'  # 1608Z: culture/sports/online last read in 1507Z","_last = '2026-10-30T1608Z'  # 1709Z: news/money/science last read in 1608Z")
R("not in requests/plan.json for 2026-10-30T16Z (rotation: news/money/science this run)","not in requests/plan.json for 2026-10-30T17Z (rotation: culture/sports/online this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T16Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T17Z (desks_not_due)'")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['world','defense','justice','disaster','markets']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T16Z","7 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T17Z, in its order and in batches of 100 (506 ids; the plan\\'s note: \"49 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 13 flat posts wait for their sixth run\"; its left_out counts 13 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 6 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: the plan\\'s 3 reads by id: 100 unread first-hop references (99 returned), then 24 second-hop (23 returned), then the last 8 unread (7 returned); nothing left to read); sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Philo\", \"Binance\" and \"Battlefront 3\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are the first top-ten US names with no posts attached in 1608Z; \"Halloween\" is one event with \"Happy Halloween\", read in 1507Z, and \"#LastFourWatched\" was read in 1608Z); desks politics/entertainment/sports/internet; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"what\" and \"the\" (1608Z used \"that\" and \"just\"), each quoted so X does not reject a bare stopword: (\"what\" lang:en is:quote -is:retweet), (\"the\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T18:00:00Z, end_time 2026-10-30T17:00:00Z, one read per desk for the 5 desks the plan lists (volume.world, volume.defense, volume.justice, volume.disaster, volume.markets: counts 4 h old); each series is the 167 full hours 2026-10-23T18:00Z to 2026-10-30T16:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T22:03:00Z (the post\\'s creation minute) and end_time 2026-10-29T22:23:00Z: (conversation_id:2115927574329057714 is:reply) and (quotes_of_tweet_id:2115927574329057714 -is:retweet); the plan gives context.top two reads, so one post: 2115927574329057714 (@nine post on the Binance hacker and Tether\\'s freeze, the biggest post new this run under 24 hours old at about 1.78M views; two bigger new posts under 24 hours were sexual and left out); one reply and no quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (11:08 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (12:09 PM CT Oct 30 / 17:09 UTC Oct 30, the 17Z slot; band allowance 42): requests/plan.json is for 2026-10-30T17Z (written 16:16Z after the 1608Z capture), so it was followed (30 reads listed) top to bottom; screen used its 3 reads. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 506 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 13 slowed flat posts and 2 unavailable in its left_out were not read. '
            f'Desks: politics, entertainment, sports and internet (the four the plan lists; the other 15 not due). Volume: world, defense, justice, disaster and markets (5 reads). Trends US and worldwide (2 reads, max 50). Sensors culture/sports/online (3 reads, the rotation). '
            f'viral.global: trend names "Philo", "Binance" and "Battlefront 3" (3 reads). rising.global: quote stream "what" and repost stream "the" (2 reads). context.top: nine 2115927574329057714 (2 reads). '
            f'Screen: 3 reads by id (100 unread references, then 24 second-hop, then the last 8; nothing left to read). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T16Z',","'plan': '2026-10-30T17Z',")
R("    'context': [{'post_id': '2115940979039404540',","    'context': [{'post_id': '2115927574329057714',")
R("f'{REPO}/capture/2026/10/30/1608Z.json'","f'{REPO}/capture/2026/10/30/1709Z.json'")
anchor="EXTRA_PRIVATE |= {'2115952763750203711','2115938524130365898','2115955817794928753'}  # 0604Z"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+"""skip_nsfw |= {'2115971176296337546','2115913183009427780','2115844805896933451','2116142230737965479'}  # 1709Z: sexual: hollywoodfiles9 sexualised photos of Jaime Chapman; plums2pickles 'came-on characters' chart; bigwillySZN 'high body count' innuendo; sexual text (2116142230737965479)
skip_nsfw |= {'2115981380748263497','2116005260955468165','2116033515141660951','2116085557097124238'}  # 1709Z: likely paid link-only clips (pahrduve two posts, 3 and 6 likes on 454K and 343K views; thepercsgotme Citytv clip, 84 likes on 373K; moreauluvrr clip, 3 likes on 143K)
EXTRA_PRIVATE |= {'2115922312075653504'}  # 1709Z: Raindropsmedia1 video of an influencer confronting an unnamed kid at Walmart (a minor, private person)
"""+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
