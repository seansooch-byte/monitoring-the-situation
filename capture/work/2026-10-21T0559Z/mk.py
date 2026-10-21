s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0507Z.json","Build capture/2026/10/21/0559Z.json"),
("work/2026-10-21T0507Z'","work/2026-10-21T0559Z'"),
("RUN_ID = '2026-10-21T0507Z'","RUN_ID = '2026-10-21T0559Z'"),
("STARTED = '2026-10-21T05:07:00Z'","STARTED = '2026-10-21T05:59:00Z'"),
("OBS_AT = '2026-10-21T05:08:00Z'","OBS_AT = '2026-10-21T06:00:00Z'"),
("READS_BEFORE = 894","READS_BEFORE = 873"),
("datetime(2026,10,21,5,10,tzinfo=timezone.utc).timestamp()  # 0507Z (0403Z used 04:06,","datetime(2026,10,21,6,2,tzinfo=timezone.utc).timestamp()  # 0559Z (0507Z used 05:10, 0403Z used 04:06,"),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_shai': 'trend_shai.txt', 'trend_thunderup': 'trend_thunderup.txt', 'trend_mccain': 'trend_mccain.txt',","'trend_eagle4': 'trend_eagle4.txt', 'trend_dwts': 'trend_dwts.txt', 'trend_wemby': 'trend_wemby.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_shai','trend.Shai'),('trend_thunderup','trend.#ThunderUp'),('trend_mccain','trend.Jared McCain'),","('trend_eagle4','trend.EAGLE-4'),('trend_dwts','trend.#dwts'),('trend_wemby','trend.Wemby'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) in ('trend.#ThunderUp','trend.Jared McCain'): return 'sports'  # 0507Z: Thunder fan tag (Thunder and Spurs game); Jared McCain (Thunder)\n","        if str(_x) in ('trend.#ThunderUp','trend.Jared McCain'): return 'sports'  # 0507Z: Thunder fan tag (Thunder and Spurs game); Jared McCain (Thunder)\n        if str(_x) == 'trend.#dwts': return 'entertainment'  # 0559Z: Dancing with the Stars\n"),
("if _c.endswith('0507Z.json') and '/21/' in _c: continue","if _c.endswith('0559Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 05Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 392 long, under the 400 cap, so nothing was left out)","(this run, started 05:59Z for the 06Z slot, is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 380 long, under the 400 cap, so nothing was left out)"),
('sensors news/money/science (one read each); trend names Shai, #ThunderUp, Jared McCain (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0403Z); quote/repost words what/the + this; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (117 first-hop in two reads, then 21 second-hop)',
 'sensors culture/sports/online (one read each); trend names EAGLE-4, #dwts, Wemby (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0507Z); quote/repost words is/you + "and"; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (107 first-hop in two reads, then 22 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"what\", \"the\" and \"this\": (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"is\", \"you\" and \"and\": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (\"and\" lang:en is:retweet; and unquoted was refused as an ambiguous keyword, one read spent), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T0403Z'","_last = '2026-10-21T0507Z'"),
("cut for the twenty-second run (kept","cut for the twenty-third run (kept"),
("but cut for the twenty-fourth run (kept","but cut for the twenty-fifth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0507Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0559Z.json'"),
("Late-night run (1:07 AM ET Oct 21 / 05:07 UTC Oct 21, the 05Z slot;","Late-night run (1:59 AM ET Oct 21 / 05:59 UTC Oct 21, firing early for the 06Z slot;"),
("0403Z ended at 894, so no read went elsewhere in between), parallel batches of up to 13","0507Z ended at 873, so no read went elsewhere in between; one of them was the refused unquoted \"and\" repost query), parallel batches of up to 9"),
("this 05Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 392 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); ",
 "this run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 380 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("f'quote/repost words what/the + this (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0403Z, next in rotation); '",
 "f'quote/repost words is/you + \"and\" (4 reads, one refused: X rejected the unquoted query \"and lang:en is:retweet\" as an ambiguous use of and as a keyword, so it was rerun quoted); sensors culture/sports/online (3 reads; news/money/science last read 0507Z, next in rotation); '"),
("cut for the twenty-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twenty-second run","cut for the twenty-fifth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twenty-third run"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Shai, #ThunderUp, Jared McCain"):
    lines[i]="            f'trend names EAGLE-4, #dwts, Wemby (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0507Z; Wemby, Spurs, Shai, Chet, Mara, #ThunderUp and Jared McCain are one event, the Thunder and Spurs NBA game, and Sixers, Knicks, Maxey, Embiid and 76ers are one event, the 76ers at Knicks game); '"
  if l.lstrip().startswith("f'three screening reads by id: 117"):
    lines[i]="            f'three screening reads by id: 107 unread first-hop (two reads) and 22 second-hop referenced, reply-parent and media-source posts (2 of them not returned by X; 12 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
