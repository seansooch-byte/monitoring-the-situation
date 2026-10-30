s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1107Z.json","Build capture/2026/10/21/1204Z.json"),
("work/2026-10-21T1107Z'","work/2026-10-21T1204Z'"),
("RUN_ID = '2026-10-21T1107Z'","RUN_ID = '2026-10-21T1204Z'"),
("STARTED = '2026-10-21T11:07:00Z'","STARTED = '2026-10-21T12:04:00Z'"),
("OBS_AT = '2026-10-21T11:07:00Z'","OBS_AT = '2026-10-21T12:04:00Z'"),
("READS_BEFORE = 767","READS_BEFORE = 747"),
("datetime(2026,10,21,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (","datetime(2026,10,21,12,6,tzinfo=timezone.utc).timestamp()  # 1204Z (1107Z used 11:10, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_hubbard': 'trend_hubbard.txt', 'trend_lngshot': 'trend_lngshot.txt', 'trend_vassago': 'trend_vassago.txt',","'trend_bladerunner': 'trend_bladerunner.txt', 'trend_papergames': 'trend_papergames.txt', 'trend_wedemand': 'trend_wedemand.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_hubbard','trend.Stephen Hubbard'),('trend_lngshot','trend.#LNGSHOT_SWISH'),('trend_vassago','trend.Vassago'),","('trend_bladerunner','trend.#BladeRunnerSupportsRacist'),('trend_papergames','trend.#PapergamesIsRacist'),('trend_wedemand','trend.We Demand Action'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1107Z.json') and '/21/' in _c: continue","if _c.endswith('1204Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
('sensors news/money/science (one read each); trend names Stephen Hubbard, #LNGSHOT_SWISH, Vassago (each "<name> lang:en is:retweet", newest first, 25 each, the multi-word name in quotes; three of the current top-ten US names with no posts attached in 1007Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (88 unread referenced first-hop, then 18 second-hop)',
 'sensors culture/sports/online (one read each); trend names #BladeRunnerSupportsRacist, #PapergamesIsRacist, We Demand Action (each "<name> lang:en is:retweet", newest first, 25 each, the multi-word name in quotes; three of the current top-ten US names with no posts attached in 1107Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 23 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T1007Z'","_last = '2026-10-21T1107Z'"),
("cut for the thirtieth run","cut for the thirty-first run"),
("cut for the twenty-eighth run","cut for the twenty-ninth run"),
("kept to about 20 reads, the 06:00-11:00 UTC overnight band limit","kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1204Z.json'"),
("Overnight run (7:07 AM ET Oct 21 / 11:07 UTC Oct 21, the 11Z slot; 06:00-11:00 UTC band, up to 20 reads)","Morning run (8:04 AM ET Oct 21 / 12:04 UTC Oct 21, the 12Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)"),
("1007Z ended at 769, so 2 reads went elsewhere in between), parallel batches of up to 13","1107Z ended at 747, so no read went elsewhere in between), parallel batches of up to 13"),
("this 11Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 383 ids, under the 400 cap, so nothing was left out; 4 reads)",
 "12Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 506 ids, so the 400 cap left out the 106 slowest-growing fourth-hour posts and no cited post; 4 reads)"),
("f'quote/repost words just/what + the (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 1007Z, next in rotation); '",
 "f'quote/repost words this/is + you (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 1107Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
("        if str(_x) == 'trend.Stephen Hubbard': return 'world'  # 1107Z",
 "        if str(_x) in ('trend.#BladeRunnerSupportsRacist','trend.#PapergamesIsRacist'): return 'gaming'  # 1204Z: fan campaign against Papergames over alleged racism and harassment in its game community, tagging the Blade Runner rights holders\n        if str(_x) == 'trend.We Demand Action': return 'entertainment'  # 1204Z: Myanmar fans' campaign against GMMTV over Burmese dress in Scarlet Heart Thailand\n        if str(_x) == 'trend.Stephen Hubbard': return 'world'  # 1107Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Stephen Hubbard, #LNGSHOT_SWISH, Vassago"):
    lines[i]="            f'trend names #BladeRunnerSupportsRacist, #PapergamesIsRacist, \"We Demand Action\" (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, \"We Demand Action\" in quotes; three of the top-ten US names with no posts attached in 1107Z; #BladeRunnerSupportsRacist, #PapergamesIsRacist and #中国上海停止包庇叠纸 are one event, a fan campaign against Papergames over alleged racism and harassment that tags the Blade Runner rights holders, and We Demand Action, #RespectMyanmarCulture and #ScarletHeartTH are one event, the Myanmar fans campaign against GMMTV over Burmese dress in Scarlet Heart Thailand; both streams are small hashtag campaigns with no post near the floor; Good Wednesday, Hump Day and Happy Hump are greetings and were not read, Stephen Hubbard had posts attached in 1107Z); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 88"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (98 returned; 1551595087410470914 and 2108062331095908717 again Not Found), then 23 unread second-hop and leftover posts (all 23 returned; one referenced post inside them Not Found: 2112698835151798628 again); story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
