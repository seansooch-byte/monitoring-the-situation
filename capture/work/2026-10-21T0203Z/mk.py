s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0059Z.json","Build capture/2026/10/21/0203Z.json"),
("work/2026-10-21T0059Z'","work/2026-10-21T0203Z'"),
("RUN_ID = '2026-10-21T0059Z'","RUN_ID = '2026-10-21T0203Z'"),
("STARTED = '2026-10-21T00:59:00Z'","STARTED = '2026-10-21T02:03:00Z'"),
("OBS_AT = '2026-10-21T01:00:00Z'","OBS_AT = '2026-10-21T02:04:00Z'"),
("READS_BEFORE = 978","READS_BEFORE = 957"),
("datetime(2026,10,21,1,3,tzinfo=timezone.utc).timestamp()  # 0059Z (0006Z used 00:09,","datetime(2026,10,21,2,6,tzinfo=timezone.utc).timestamp()  # 0203Z (0059Z used 01:03, 0006Z used 00:09,"),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_dwts': 'trend_dwts.txt', 'trend_ezra': 'trend_ezra.txt', 'trend_knicks': 'trend_knicks.txt',","'trend_lebron': 'trend_lebron.txt', 'trend_brunson': 'trend_brunson.txt', 'trend_76ers': 'trend_76ers.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_dwts','trend.#dwts'),('trend_ezra','trend.Ezra'),('trend_knicks','trend.Knicks'),","('trend_lebron','trend.LeBron'),('trend_brunson','trend.Brunson'),('trend_76ers','trend.76ers'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) == 'trend.76ers': return 'sports'  # 1600Z: NBA opening week, 76ers\n","        if str(_x) == 'trend.76ers': return 'sports'  # 1600Z: NBA opening week, 76ers\n        if str(_x) in ('trend.LeBron','trend.Brunson'): return 'sports'  # 0203Z: NBA opening week (LeBron; Brunson is the Knicks opener)\n"),
("if _c.endswith('0059Z.json') and '/21/' in _c: continue","if _c.endswith('0203Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 01Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 398 long, under the 400 cap, so nothing was left out)","(this 02Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 374 long, under the 400 cap, so nothing was left out)"),
('sensors news/money/science (one read each); trend names #dwts, Ezra, Knicks (each "<name> lang:en is:retweet", newest first, 25 each; three of the six current top-ten US names with no posts attached in 0006Z); quote/repost words that/just + what; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (118 first-hop in two reads, then 22 second-hop)',
 'sensors culture/sports/online (one read each); trend names LeBron, Brunson, 76ers (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0059Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (102 first-hop in two reads, then 16 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"that\", \"just\" and \"what\": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"the\", \"this\" and \"is\": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T0006Z'","_last = '2026-10-21T0059Z'"),
("cut for the eighteenth run (kept","cut for the nineteenth run (kept"),
("but cut for the twentieth run (kept","but cut for the twenty-first run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0059Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0203Z.json'"),
("Evening run (8:59 PM ET Oct 20 / 00:59 UTC Oct 21, an early fire of the 01Z slot;","Evening run (10:03 PM ET Oct 20 / 02:03 UTC Oct 21, the 02Z slot;"),
("0006Z ended at 978, so no read went elsewhere in between), parallel batches of up to 13","0059Z ended at 957, so no read went elsewhere in between), parallel batches of up to 13"),
("this 01Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 398 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); ",
 "this 02Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 374 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("sensors news/money/science (3 reads; culture/sports/online last read 0006Z, next in rotation)","sensors culture/sports/online (3 reads; news/money/science last read 0059Z, next in rotation)"),
("quote/repost words that/just + what (3 reads)","quote/repost words the/this + is (3 reads)"),
("cut for the twentieth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the eighteenth run","cut for the twenty-first run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the nineteenth run"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names #dwts, Ezra, Knicks"):
    lines[i]="            f'trend names LeBron, Brunson, 76ers (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0059Z; Sixers, Embiid, Maxey, Drummond and 76ers are one event, the 76ers NBA opener (Embiid and Drummond read in 0006Z), so 76ers stands for it; Brunson is one event with the Knicks opener read in 0059Z; LeBron is new this run; #dwts, Tatyana and Ezra had posts attached in 0059Z); '"
  if l.lstrip().startswith("f'three screening reads by id: 118"):
    lines[i]="            f'three screening reads by id: 102 unread first-hop (two reads) and 16 second-hop referenced, reply-parent and media-source posts; story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
