s=open('../2026-10-20T2007Z/build_capture.py').read()
R=[
("Build capture/2026/10/20/2007Z.json","Build capture/2026/10/20/2059Z.json"),
("work/2026-10-20T2007Z'","work/2026-10-20T2059Z'"),
("RUN_ID = '2026-10-20T2007Z'","RUN_ID = '2026-10-20T2059Z'"),
("STARTED = '2026-10-20T20:07:00Z'","STARTED = '2026-10-20T20:59:00Z'"),
("OBS_AT = '2026-10-20T20:08:00Z'","OBS_AT = '2026-10-20T21:00:00Z'"),
("READS_BEFORE = 542","READS_BEFORE = 520"),
("datetime(2026,10,20,20,10,tzinfo=timezone.utc).timestamp()  # 2007Z (1905Z","datetime(2026,10,20,21,2,tzinfo=timezone.utc).timestamp()  # 2059Z (2007Z used 20:10, 1905Z"),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_pistons': 'trend_pistons.txt', 'trend_dembele': 'trend_dembele.txt', 'trend_mitchellrobinson': 'trend_mitchellrobinson.txt',","'trend_paulgeorge': 'trend_paulgeorge.txt', 'trend_celtics': 'trend_celtics.txt', 'trend_barca': 'trend_barca.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_my','repost'),"),
("('trend_pistons','trend.Pistons'),('trend_dembele','trend.Dembele'),('trend_mitchellrobinson','trend.Mitchell Robinson'),","('trend_paulgeorge','trend.Paul George'),('trend_celtics','trend.Celtics'),('trend_barca','trend.Barca'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2007Z.json') and '/20/' in _c: continue","if _c.endswith('2059Z.json') and '/20/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("then, as 20Z is a fourth hour, the rest of the last 24 hours fastest growing first; with every pulse- and story-cited post placed right after the watch.json ids the list was 479 long, so the 400 cap left out the 79 slowest-growing posts (all of the fourth-hour tier and the slowest still-gaining posts), and no cited post","(this 21Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 434 long, so the 400 cap left out the 34 slowest-growing still-gaining posts, and no cited post)"),
("sensors culture/sports/online (one read each); trend names Pistons, Dembele, \"Mitchell Robinson\" (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the nine current top-ten US names with no posts attached in 1905Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (126 first-hop in two reads, then 29 second-hop)",
 "sensors news/money/science (one read each); trend names \"Paul George\", Celtics, Barca (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the five current top-ten US names with no posts attached in 2007Z); quote/repost words it/that + my; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (113 first-hop in two reads, then 17 second-hop)"),
("'2 quote pages + 1 repost page (budget), common words \"the\", \"this\" and \"is\": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"it\", \"that\" and \"my\": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-20T1905Z'","_last = '2026-10-20T2007Z'"),
("cut for the thirteenth run (kept","cut for the fourteenth run (kept"),
("but cut for the fifteenth run (kept","but cut for the sixteenth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2007Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2059Z.json'"),
("Afternoon run (4:07 PM ET Oct 20 / 20:07 UTC, fired a few minutes late;","Afternoon run (4:59 PM ET Oct 20 / 20:59 UTC, the 21Z slot;"),
("1905Z ended at 542, so no read went elsewhere","2007Z ended at 520, so no read went elsewhere"),
("20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours fastest growing first; 479 ids, so the 400 cap left out the 79 slowest-growing posts (the whole fourth-hour tier and the slowest still-gaining posts) and no cited post;",
 "this 21Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 434 ids, so the 400 cap left out the 34 slowest-growing still-gaining posts and no cited post;"),
("sensors culture/sports/online (3 reads; news/money/science last read 1905Z, next in rotation)","sensors news/money/science (3 reads; culture/sports/online last read 2007Z, next in rotation)"),
("the two-hour desks (last ok 0400Z, due 06:00Z) cut for the fifteenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the thirteenth run","the two-hour desks (last ok 0400Z, due 06:00Z) cut for the sixteenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the fourteenth run"),
("Not read: news/money/science sensors,","Not read: culture/sports/online sensors,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
open('build_capture.py','w').write(s)
