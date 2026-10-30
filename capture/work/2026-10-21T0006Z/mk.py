s=open('build_capture.py').read()
R=[
("Build capture/2026/10/20/2258Z.json","Build capture/2026/10/21/0006Z.json"),
("work/2026-10-20T2258Z'","work/2026-10-21T0006Z'"),
("RUN_ID = '2026-10-20T2258Z'","RUN_ID = '2026-10-21T0006Z'"),
("STARTED = '2026-10-20T22:58:00Z'","STARTED = '2026-10-21T00:06:00Z'"),
("OBS_AT = '2026-10-20T23:00:00Z'","OBS_AT = '2026-10-21T00:07:00Z'"),
("READS_BEFORE = 476","READS_BEFORE = 1000"),
("datetime(2026,10,20,23,2,tzinfo=timezone.utc).timestamp()  # 2258Z (2207Z used 22:11, 2059Z","datetime(2026,10,21,0,9,tzinfo=timezone.utc).timestamp()  # 0006Z (2258Z used 23:02, 2207Z used 22:11, 2059Z"),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_my': 'quote_my.txt',"),
("'repost_is': 'repost_is.txt',","'repost_it': 'repost_it.txt',"),
("'trend_paulgeorge': 'trend_paulgeorge.txt', 'trend_knicks': 'trend_knicks.txt', 'trend_jaylenbrown': 'trend_jaylenbrown.txt',","'trend_embiid': 'trend_embiid.txt', 'trend_eagle4': 'trend_eagle4.txt', 'trend_drummond': 'trend_drummond.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',"),
("'trends_us': 'trends_us.txt',","'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',"),
("trends = parse_trends(raw['trends_us'], 'US')","trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')"),
("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-20T2207Z',[]))","sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_paulgeorge','trend.Paul George'),('trend_knicks','trend.Knicks'),('trend_jaylenbrown','trend.Jaylen Brown'),","('trend_embiid','trend.Embiid'),('trend_eagle4','trend.EAGLE-4'),('trend_drummond','trend.Drummond'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2258Z.json') and '/20/' in _c: continue","if _c.endswith('0006Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 23Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 427 long, so the 400 cap left out the 27 slowest-growing still-gaining posts, and no cited post)","(this 00Z-slot run is a fourth hour, so the rest of the last 24 hours was added, fastest growing first; with every pulse- and story-cited post placed right after the watch.json ids the list was 484 long, so the 400 cap left out the 84 slowest-growing posts (the fourth-hour tier), and no cited post)"),
('sensors news/money/science (one read each); trend names "Paul George", Knicks, "Jaylen Brown" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; three of the five current top-ten US names with no posts attached in 2207Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (91 first-hop in one read, then 19 second-hop)',
 'sensors culture/sports/online (one read each); trend names Embiid, "EAGLE-4", Drummond (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space or a hyphen; three of the six current top-ten US names with no posts attached in 2258Z); quote/repost words you/my + it; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (121 first-hop in two reads, then 25 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"the\", \"this\" and \"is\": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"you\", \"my\" and \"it\": (you lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-20T2207Z'","_last = '2026-10-20T2258Z'"),
("cut for the sixteenth run (kept","cut for the seventeenth run (kept"),
("but cut for the eighteenth run (kept","but cut for the nineteenth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2258Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0006Z.json'"),
("Evening run (6:58 PM ET Oct 20 / 22:58 UTC, an early fire of the 23Z slot;","Evening run (8:06 PM ET Oct 20 / 00:06 UTC Oct 21, the 00Z slot and the first run of the new UTC day;"),
("2207Z ended at 476, so no read went elsewhere in between), parallel batches of up to 10","the X day reset at 00:00 UTC, so no read went elsewhere in between), parallel batches of up to 13"),
("this 23Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 427 ids, so the 400 cap left out the 27 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 2207Z); ",
 "this 00Z-slot run is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the fourth-hour tier fastest growing first; 484 ids, so the 400 cap left out the 84 slowest-growing posts (all of the fourth-hour tier) and no cited post; 4 reads); trends US+WW (2 reads); "),
("sensors news/money/science (3 reads; culture/sports/online last read 2207Z, next in rotation)","sensors culture/sports/online (3 reads; news/money/science last read 2258Z, next in rotation)"),
("quote/repost words the/this + is (3 reads)","quote/repost words you/my + it (3 reads)"),
("the two-hour desks (last ok 0400Z, due 06:00Z) cut for the eighteenth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the sixteenth run","the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the nineteenth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the seventeenth run"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names \"Paul George\", Knicks"):
    lines[i]="            f'trend names Embiid, \"EAGLE-4\", Drummond (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space or a hyphen; three of the six top-ten US names with no posts attached in 2258Z; Drummond, Sixers, Embiid, Maxey and 76ers are one event, the 76ers NBA opener, so Embiid and Drummond stand for it and Maxey, Sixers and 76ers were not read; Celtics not read, the Celtics v Pistons opener read in 2207Z and 2258Z); '"
  if l.lstrip().startswith("f'two screening reads by id: 91"):
    lines[i]="            f'three screening reads by id: 121 unread first-hop (two reads) and 25 second-hop referenced, reply-parent and media-source posts; story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
