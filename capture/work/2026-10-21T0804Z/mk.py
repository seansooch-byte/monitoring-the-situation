s=open('build_capture.py').read()
BAND="kept to about 20 reads, the 06:00-11:00 UTC overnight band limit"
R=[
("Build capture/2026/10/21/0705Z.json","Build capture/2026/10/21/0804Z.json"),
("work/2026-10-21T0705Z'","work/2026-10-21T0804Z'"),
("RUN_ID = '2026-10-21T0705Z'","RUN_ID = '2026-10-21T0804Z'"),
("STARTED = '2026-10-21T07:05:00Z'","STARTED = '2026-10-21T08:04:00Z'"),
("OBS_AT = '2026-10-21T07:06:00Z'","OBS_AT = '2026-10-21T08:05:00Z'"),
("READS_BEFORE = 849","READS_BEFORE = 829"),
("datetime(2026,10,21,7,8,tzinfo=timezone.utc).timestamp()  # 0705Z (0559Z used 06:02,","datetime(2026,10,21,8,7,tzinfo=timezone.utc).timestamp()  # 0804Z (0705Z used 07:08, 0559Z used 06:02,"),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_visionquest': 'trend_visionquest.txt', 'trend_sixers': 'trend_sixers.txt', 'trend_spurs': 'trend_spurs.txt',","'trend_chet': 'trend_chet.txt', 'trend_dwts': 'trend_dwts.txt', 'trend_knicks': 'trend_knicks.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_visionquest','trend.#VisionQuest'),('trend_sixers','trend.Sixers'),('trend_spurs','trend.Spurs'),","('trend_chet','trend.Chet'),('trend_dwts','trend.#dwts'),('trend_knicks','trend.Knicks'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0705Z.json') and '/21/' in _c: continue","if _c.endswith('0804Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 07Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 363 long, under the 400 cap, so nothing was left out)","(this 08Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 467 long, so the 400 cap left out the 67 slowest-growing fourth-hour-tier posts and no cited post)"),
('sensors news/money/science (one read each); trend names #VisionQuest, Sixers, Spurs (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0559Z); quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id (96 unread referenced first-hop in one read, then 14 second-hop)',
 'sensors culture/sports/online (one read each); trend names Chet, #dwts, Knicks (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0705Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop in one read, then 23 second-hop and leftover first-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"my\", \"it\" and \"that\": (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T0559Z'","_last = '2026-10-21T0705Z'"),
("but cut for the twenty-fourth run (kept","but cut for the twenty-fifth run (kept"),
("but cut for the twenty-sixth run (kept","but cut for the twenty-seventh run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0705Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0804Z.json'"),
("Overnight run (3:05 AM ET Oct 21 / 07:05 UTC Oct 21, the 07Z slot; 06:00-11:00 UTC band, up to 20 reads)","Overnight run (4:04 AM ET Oct 21 / 08:04 UTC Oct 21, the 08Z slot; 06:00-11:00 UTC band, up to 20 reads)"),
("0559Z ended at 850, so one read went elsewhere in between), parallel batches of up to 13","0705Z ended at 829, so nothing else read in between), parallel batches of up to 13"),
("this 07Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 363 ids, under the 400 cap, so nothing was left out; 4 reads)",
 "this 08Z-slot run is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 467 ids, so the 400 cap left out the 67 slowest-growing fourth-hour-tier posts and no cited post; 4 reads)"),
("f'quote/repost words my/it + that (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0559Z, next in rotation); '",
 "f'quote/repost words just/what + the (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 0705Z, next in rotation); '"),
("cut for the twenty-sixth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-fourth run","cut for the twenty-seventh run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-fifth run"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names #VisionQuest, Sixers, Spurs"):
    lines[i]="            f'trend names Chet, #dwts, Knicks (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0705Z; Wemby, Spurs, Shai, Chet, Mara, #ThunderUp and Jared McCain are one event, the Thunder and Spurs NBA game, Knicks, Sixers, Maxey, Embiid and 76ers are one event, the 76ers at Knicks opener, and #dwts is the Dancing with the Stars episode); '"
  if l.lstrip().startswith("f'two screening reads by id: 96"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop, then 23 second-hop and leftover first-hop referenced, reply-parent and media-source posts (3 of them not returned by X; 8 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
