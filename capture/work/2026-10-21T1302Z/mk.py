s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1204Z.json","Build capture/2026/10/21/1302Z.json"),
("work/2026-10-21T1204Z'","work/2026-10-21T1302Z'"),
("RUN_ID = '2026-10-21T1204Z'","RUN_ID = '2026-10-21T1302Z'"),
("STARTED = '2026-10-21T12:04:00Z'","STARTED = '2026-10-21T13:02:00Z'"),
("OBS_AT = '2026-10-21T12:04:00Z'","OBS_AT = '2026-10-21T13:02:00Z'"),
("READS_BEFORE = 747","READS_BEFORE = 727"),
("datetime(2026,10,21,12,6,tzinfo=timezone.utc).timestamp()  # 1204Z (","datetime(2026,10,21,13,5,tzinfo=timezone.utc).timestamp()  # 1302Z (1204Z used 12:06, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_you': 'repost_you.txt',","'repost_that': 'repost_that.txt',"),
("'trend_bladerunner': 'trend_bladerunner.txt', 'trend_papergames': 'trend_papergames.txt', 'trend_wedemand': 'trend_wedemand.txt',","'trend_hubbard': 'trend_hubbard.txt', 'trend_witkoff': 'trend_witkoff.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_bladerunner','trend.#BladeRunnerSupportsRacist'),('trend_papergames','trend.#PapergamesIsRacist'),('trend_wedemand','trend.We Demand Action'),","('trend_hubbard','trend.Stephen Hubbard'),('trend_witkoff','trend.Witkoff'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1204Z.json') and '/21/' in _c: continue","if _c.endswith('1302Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
('sensors culture/sports/online (one read each); trend names #BladeRunnerSupportsRacist, #PapergamesIsRacist, We Demand Action (each "<name> lang:en is:retweet", newest first, 25 each, the multi-word name in quotes; three of the current top-ten US names with no posts attached in 1107Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 23 second-hop and leftover)',
 'sensors news/money/science (one read each); trend names Stephen Hubbard, Witkoff (each "<name> lang:en is:retweet", newest first, 25 each, the multi-word name in quotes; the two current top-ten US names with no posts attached in 1204Z, other than greetings); quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id (91 unread referenced first-hop, then 21 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"my\", \"it\" and \"that\": (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each; \"and\" skipped in the rotation because X refused it as a query in 1007Z'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T1107Z'","_last = '2026-10-21T1204Z'"),
("cut for the thirty-first run","cut for the thirty-second run"),
("cut for the twenty-ninth run","cut for the thirtieth run"),
("(this 11Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 383 long, under the 400 cap, so nothing was left out)",
 "(this 13Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 412 long, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1204Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1302Z.json'"),
("Morning run (8:04 AM ET Oct 21 / 12:04 UTC Oct 21, the 12Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)","Morning run (9:02 AM ET Oct 21 / 13:02 UTC Oct 21, the 13Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)"),
("1107Z ended at 747, so no read went elsewhere in between), parallel batches of up to 13","1204Z ended at 727, so no read went elsewhere in between), parallel batches of up to 12"),
("12Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 506 ids, so the 400 cap left out the 106 slowest-growing fourth-hour posts and no cited post; 4 reads)",
 "13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 412 ids, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words this/is + you (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 1107Z, next in rotation); '",
 "f'quote/repost words my/it + that (3 reads; \"and\" skipped in the rotation, X refused it in 1007Z); sensors news/money/science (3 reads; culture/sports/online last read 1204Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
("        if str(_x) == 'trend.Stephen Hubbard': return 'world'  # 1107Z",
 "        if str(_x) == 'trend.Witkoff': return 'world'  # 1302Z: Witkoff meets Putin in St Petersburg; one event with the Stephen Hubbard release\n        if str(_x) == 'trend.Stephen Hubbard': return 'world'  # 1107Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names #BladeRunnerSupportsRacist, #PapergamesIsRacist"):
    lines[i]="            f'trend names \"Stephen Hubbard\", Witkoff (2 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, \"Stephen Hubbard\" in quotes; the two top-ten US names with no posts attached in 1204Z other than the greetings Good Wednesday and Hump Day; they are one event: Steve Witkoff meeting Putin in St Petersburg and the release of Stephen Hubbard; the other top-ten names had posts attached in 1204Z); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 91 unread first-hop referenced, reply-parent and media-source posts (all 91 returned; one referenced post inside them Not Found: 2108062331095908717 again), then 21 unread second-hop and leftover posts (all 21 returned; 2108062331095908717 left out of the read as known Not Found); story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
