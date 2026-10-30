s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0403Z.json","Build capture/2026/10/21/0507Z.json"),
("work/2026-10-21T0403Z'","work/2026-10-21T0507Z'"),
("RUN_ID = '2026-10-21T0403Z'","RUN_ID = '2026-10-21T0507Z'"),
("STARTED = '2026-10-21T04:03:00Z'","STARTED = '2026-10-21T05:07:00Z'"),
("OBS_AT = '2026-10-21T04:04:00Z'","OBS_AT = '2026-10-21T05:08:00Z'"),
("READS_BEFORE = 915","READS_BEFORE = 894"),
("datetime(2026,10,21,4,6,tzinfo=timezone.utc).timestamp()  # 0403Z (0308Z used 03:12,","datetime(2026,10,21,5,10,tzinfo=timezone.utc).timestamp()  # 0507Z (0403Z used 04:06, 0308Z used 03:12,"),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_mara': 'trend_mara.txt', 'trend_spurs': 'trend_spurs.txt', 'trend_sixers': 'trend_sixers.txt',","'trend_shai': 'trend_shai.txt', 'trend_thunderup': 'trend_thunderup.txt', 'trend_mccain': 'trend_mccain.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_mara','trend.Mara'),('trend_spurs','trend.Spurs'),('trend_sixers','trend.Sixers'),","('trend_shai','trend.Shai'),('trend_thunderup','trend.#ThunderUp'),('trend_mccain','trend.Jared McCain'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) in ('trend.Mara','trend.Thunder','trend.Sixers'): return 'sports'  # 0403Z: Aday Mara of the Thunder (Thunder and Spurs game); Sixers (76ers at Knicks)\n","        if str(_x) in ('trend.Mara','trend.Thunder','trend.Sixers'): return 'sports'  # 0403Z: Aday Mara of the Thunder (Thunder and Spurs game); Sixers (76ers at Knicks)\n        if str(_x) in ('trend.#ThunderUp','trend.Jared McCain'): return 'sports'  # 0507Z: Thunder fan tag (Thunder and Spurs game); Jared McCain (Thunder)\n"),
("if _c.endswith('0403Z.json') and '/21/' in _c: continue","if _c.endswith('0507Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this 04Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 443 long, so the 400 cap left out the 43 slowest-growing posts of the fourth-hour tier and no cited post)","(this 05Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 392 long, under the 400 cap, so nothing was left out)"),
('sensors culture/sports/online (one read each); trend names Mara, Spurs, Sixers (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0308Z); quote/repost words it/that + just; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (103 first-hop in two reads, then 22 second-hop)',
 'sensors news/money/science (one read each); trend names Shai, #ThunderUp, Jared McCain (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0403Z); quote/repost words what/the + this; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (117 first-hop in two reads, then 21 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"it\", \"that\" and \"just\": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"what\", \"the\" and \"this\": (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T0308Z'","_last = '2026-10-21T0403Z'"),
("cut for the twenty-first run (kept","cut for the twenty-second run (kept"),
("but cut for the twenty-third run (kept","but cut for the twenty-fourth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0403Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0507Z.json'"),
("Late-night run (12:03 AM ET Oct 21 / 04:03 UTC Oct 21, the 04Z slot;","Late-night run (1:07 AM ET Oct 21 / 05:07 UTC Oct 21, the 05Z slot;"),
("0308Z ended at 915, so no read went elsewhere in between), parallel batches of up to 13","0403Z ended at 894, so no read went elsewhere in between), parallel batches of up to 13"),
("this 04Z-slot run is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 443 ids, so the 400 cap left out the 43 slowest-growing posts of the fourth-hour tier and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); ",
 "this 05Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 392 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("f'quote/repost words it/that + just (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 0308Z, next in rotation); '",
 "f'quote/repost words what/the + this (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0403Z, next in rotation); '"),
("cut for the twenty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twenty-first run","cut for the twenty-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twenty-second run"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Mara, Spurs, Sixers"):
    lines[i]="            f'trend names Shai, #ThunderUp, Jared McCain (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0403Z; Wemby, Spurs, Shai, Chet, Mara, #ThunderUp and Jared McCain are one event, the Thunder and Spurs NBA game, and Sixers, Knicks, Maxey, Embiid and 76ers are one event, the 76ers at Knicks game); '"
  if l.lstrip().startswith("f'three screening reads by id: 103"):
    lines[i]="            f'three screening reads by id: 117 unread first-hop (two reads) and 21 second-hop referenced, reply-parent and media-source posts (12 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
