s=open('../2026-10-20T2059Z/build_capture.py').read()
R=[
("Build capture/2026/10/20/2059Z.json","Build capture/2026/10/20/2207Z.json"),
("work/2026-10-20T2059Z'","work/2026-10-20T2207Z'"),
("RUN_ID = '2026-10-20T2059Z'","RUN_ID = '2026-10-20T2207Z'"),
("STARTED = '2026-10-20T20:59:00Z'","STARTED = '2026-10-20T22:07:00Z'"),
("OBS_AT = '2026-10-20T21:00:00Z'","OBS_AT = '2026-10-20T22:09:00Z'"),
("READS_BEFORE = 520","READS_BEFORE = 498"),
("datetime(2026,10,20,21,2,tzinfo=timezone.utc).timestamp()  # 2059Z (2007Z","datetime(2026,10,20,22,11,tzinfo=timezone.utc).timestamp()  # 2207Z (2059Z used 21:02, 2007Z"),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_my': 'repost_my.txt',","'repost_you': 'repost_you.txt',"),
("'trend_paulgeorge': 'trend_paulgeorge.txt', 'trend_celtics': 'trend_celtics.txt', 'trend_barca': 'trend_barca.txt',","'trend_tatum': 'trend_tatum.txt', 'trend_duncanrobinson': 'trend_duncanrobinson.txt', 'trend_nickshirley': 'trend_nickshirley.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_my','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_you','repost'),"),
("('trend_paulgeorge','trend.Paul George'),('trend_celtics','trend.Celtics'),('trend_barca','trend.Barca'),","('trend_tatum','trend.Tatum'),('trend_duncanrobinson','trend.Duncan Robinson'),('trend_nickshirley','trend.Nick Shirley'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2059Z.json') and '/20/' in _c: continue","if _c.endswith('2207Z.json') and '/20/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 21Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 434 long, so the 400 cap left out the 34 slowest-growing still-gaining posts, and no cited post)","(this 22Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 415 long, so the 400 cap left out the 15 slowest-growing still-gaining posts, and no cited post)"),
("sensors news/money/science (one read each); trend names \"Paul George\", Celtics, Barca (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the five current top-ten US names with no posts attached in 2007Z); quote/repost words it/that + my; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (113 first-hop in two reads, then 17 second-hop)",
 "sensors culture/sports/online (one read each); trend names Tatum, \"Duncan Robinson\", \"Nick Shirley\" (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the seven current top-ten US names with no posts attached in 2059Z); quote/repost words just/what + you; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (107 first-hop in two reads, then 26 second-hop)"),
("'2 quote pages + 1 repost page (budget), common words \"it\", \"that\" and \"my\": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"you\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-20T2007Z'","_last = '2026-10-20T2059Z'"),
("cut for the fourteenth run (kept","cut for the fifteenth run (kept"),
("but cut for the sixteenth run (kept","but cut for the seventeenth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2059Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2207Z.json'"),
("Afternoon run (4:59 PM ET Oct 20 / 20:59 UTC, the 21Z slot;","Evening run (6:07 PM ET Oct 20 / 22:07 UTC, a late fire of the 22Z slot;"),
("2007Z ended at 520, so no read went elsewhere in between), parallel batches of up to 7","2059Z ended at 498, so no read went elsewhere in between), parallel batches of up to 13"),
("this 21Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 434 ids, so the 400 cap left out the 34 slowest-growing still-gaining posts and no cited post;",
 "this 22Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 415 ids, so the 400 cap left out the 15 slowest-growing still-gaining posts and no cited post;"),
("sensors news/money/science (3 reads; culture/sports/online last read 2007Z, next in rotation)","sensors culture/sports/online (3 reads; news/money/science last read 2059Z, next in rotation)"),
("quote/repost words it/that + my (3 reads)","quote/repost words just/what + you (3 reads)"),
("the two-hour desks (last ok 0400Z, due 06:00Z) cut for the sixteenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the fourteenth run","the two-hour desks (last ok 0400Z, due 06:00Z) cut for the seventeenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the fifteenth run"),
("Not read: culture/sports/online sensors,","Not read: news/money/science sensors,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
import re
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names \"Paul George\""):
    lines[i]="            f'trend names Tatum, \"Duncan Robinson\", \"Nick Shirley\" (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the seven top-ten US names with no posts attached in 2059Z; Tatum, \"Paul George\", Celtics, Pistons, \"Duncan Robinson\", \"Jaylen Brown\" and \"Javonte Green\" are one event, the Celtics v Pistons NBA opener; Barca and Lamine are PSG v Barcelona; Vivek not read, read in 1502Z and 1705Z); '"
  if l.lstrip().startswith("f'three screening reads by id: 113"):
    lines[i]="            f'three screening reads by id: 107 unread first-hop (100 in the first read, 7 in the second) and 26 second-hop referenced, reply-parent and media-source posts (2112663188147974605 not authorized as a referenced post, left out of the second-hop read); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
