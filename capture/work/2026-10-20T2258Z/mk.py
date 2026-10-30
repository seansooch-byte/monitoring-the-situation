s=open('../2026-10-20T2207Z/build_capture.py').read()
R=[
("Build capture/2026/10/20/2207Z.json","Build capture/2026/10/20/2258Z.json"),
("work/2026-10-20T2207Z'","work/2026-10-20T2258Z'"),
("RUN_ID = '2026-10-20T2207Z'","RUN_ID = '2026-10-20T2258Z'"),
("STARTED = '2026-10-20T22:07:00Z'","STARTED = '2026-10-20T22:58:00Z'"),
("OBS_AT = '2026-10-20T22:09:00Z'","OBS_AT = '2026-10-20T23:00:00Z'"),
("READS_BEFORE = 498","READS_BEFORE = 476"),
("datetime(2026,10,20,22,11,tzinfo=timezone.utc).timestamp()  # 2207Z (2059Z","datetime(2026,10,20,23,2,tzinfo=timezone.utc).timestamp()  # 2258Z (2207Z used 22:11, 2059Z"),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_you': 'repost_you.txt',","'repost_is': 'repost_is.txt',"),
("'trend_tatum': 'trend_tatum.txt', 'trend_duncanrobinson': 'trend_duncanrobinson.txt', 'trend_nickshirley': 'trend_nickshirley.txt',","'trend_paulgeorge': 'trend_paulgeorge.txt', 'trend_knicks': 'trend_knicks.txt', 'trend_jaylenbrown': 'trend_jaylenbrown.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',","'trends_us': 'trends_us.txt',"),
("parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')","parse_trends(raw['trends_us'], 'US')"),
("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))","sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-20T2207Z',[]))"),
("('quote_just','quote'),('quote_what','quote'),('repost_you','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_tatum','trend.Tatum'),('trend_duncanrobinson','trend.Duncan Robinson'),('trend_nickshirley','trend.Nick Shirley'),","('trend_paulgeorge','trend.Paul George'),('trend_knicks','trend.Knicks'),('trend_jaylenbrown','trend.Jaylen Brown'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2207Z.json') and '/20/' in _c: continue","if _c.endswith('2258Z.json') and '/20/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this 22Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 415 long, so the 400 cap left out the 15 slowest-growing still-gaining posts, and no cited post)","(this 23Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 427 long, so the 400 cap left out the 27 slowest-growing still-gaining posts, and no cited post)"),
("sensors culture/sports/online (one read each); trend names Tatum, \"Duncan Robinson\", \"Nick Shirley\" (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the seven current top-ten US names with no posts attached in 2059Z); quote/repost words just/what + you; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (107 first-hop in two reads, then 26 second-hop)",
 "sensors news/money/science (one read each); trend names \"Paul George\", Knicks, \"Jaylen Brown\" (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the five current top-ten US names with no posts attached in 2207Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (91 first-hop in one read, then 19 second-hop)"),
("'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"you\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"the\", \"this\" and \"is\": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-20T2059Z'","_last = '2026-10-20T2207Z'"),
("cut for the fifteenth run (kept","cut for the sixteenth run (kept"),
("but cut for the seventeenth run (kept","but cut for the eighteenth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2207Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2258Z.json'"),
("Evening run (6:07 PM ET Oct 20 / 22:07 UTC, a late fire of the 22Z slot;","Evening run (6:58 PM ET Oct 20 / 22:58 UTC, an early fire of the 23Z slot;"),
("2059Z ended at 498, so no read went elsewhere in between), parallel batches of up to 13","2207Z ended at 476, so no read went elsewhere in between), parallel batches of up to 10"),
("this 22Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 415 ids, so the 400 cap left out the 15 slowest-growing still-gaining posts and no cited post; 4 reads); trends US+WW (2 reads); ",
 "this 23Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 427 ids, so the 400 cap left out the 27 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 2207Z); "),
("sensors culture/sports/online (3 reads; news/money/science last read 2059Z, next in rotation)","sensors news/money/science (3 reads; culture/sports/online last read 2207Z, next in rotation)"),
("quote/repost words just/what + you (3 reads)","quote/repost words the/this + is (3 reads)"),
("the two-hour desks (last ok 0400Z, due 06:00Z) cut for the seventeenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the fifteenth run","the two-hour desks (last ok 0400Z, due 06:00Z) cut for the eighteenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the sixteenth run"),
("Not read: news/money/science sensors,","Not read: culture/sports/online sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Tatum, \"Duncan Robinson\""):
    lines[i]="            f'trend names \"Paul George\", Knicks, \"Jaylen Brown\" (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the five top-ten US names with no posts attached in 2207Z; Tatum, Celtics, \"Paul George\", Pistons, \"Duncan Robinson\", \"Jaylen Brown\" and \"Javonte Green\" are the NBA opening-night games; Barca is PSG v Barcelona; Vivek and Barca not read, read in 1502Z/1705Z and 2059Z); '"
  if l.lstrip().startswith("f'three screening reads by id: 107"):
    lines[i]="            f'two screening reads by id: 91 unread first-hop and 19 second-hop referenced, reply-parent and media-source posts (2108062331095908717 Not Found again; 9 third-hop posts not read); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
