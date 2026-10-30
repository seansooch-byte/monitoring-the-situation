s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0203Z.json","Build capture/2026/10/21/0308Z.json"),
("work/2026-10-21T0203Z'","work/2026-10-21T0308Z'"),
("RUN_ID = '2026-10-21T0203Z'","RUN_ID = '2026-10-21T0308Z'"),
("STARTED = '2026-10-21T02:03:00Z'","STARTED = '2026-10-21T03:08:00Z'"),
("OBS_AT = '2026-10-21T02:04:00Z'","OBS_AT = '2026-10-21T03:09:00Z'"),
("READS_BEFORE = 957","READS_BEFORE = 936"),
("datetime(2026,10,21,2,6,tzinfo=timezone.utc).timestamp()  # 0203Z (0059Z used 01:03,","datetime(2026,10,21,3,12,tzinfo=timezone.utc).timestamp()  # 0308Z (0203Z used 02:06, 0059Z used 01:03,"),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_lebron': 'trend_lebron.txt', 'trend_brunson': 'trend_brunson.txt', 'trend_76ers': 'trend_76ers.txt',","'trend_chet': 'trend_chet.txt', 'trend_wemby': 'trend_wemby.txt', 'trend_dwts': 'trend_dwts.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_lebron','trend.LeBron'),('trend_brunson','trend.Brunson'),('trend_76ers','trend.76ers'),","('trend_chet','trend.Chet'),('trend_wemby','trend.Wemby'),('trend_dwts','trend.#dwts'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) in ('trend.LeBron','trend.Brunson'): return 'sports'  # 0203Z: NBA opening week (LeBron; Brunson is the Knicks opener)\n","        if str(_x) in ('trend.LeBron','trend.Brunson'): return 'sports'  # 0203Z: NBA opening week (LeBron; Brunson is the Knicks opener)\n        if str(_x) in ('trend.Chet','trend.Wemby','trend.Spurs','trend.Shai'): return 'sports'  # 0308Z: NBA opening week (Thunder and Spurs)\n"),
("if _c.endswith('0203Z.json') and '/21/' in _c: continue","if _c.endswith('0308Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this 02Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 374 long, under the 400 cap, so nothing was left out)","(this 03Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 371 long, under the 400 cap, so nothing was left out)"),
('sensors culture/sports/online (one read each); trend names LeBron, Brunson, 76ers (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0059Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (102 first-hop in two reads, then 16 second-hop)',
 'sensors news/money/science (one read each); trend names Chet, Wemby, #dwts (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0203Z); quote/repost words you/"and" + my; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (106 first-hop in two reads, then 26 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"the\", \"this\" and \"is\": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"you\", \"and\" and \"my\": (you lang:en is:quote -is:retweet), (\"and\" lang:en is:quote -is:retweet, quoted because X refuses a bare and), (my lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T0059Z'","_last = '2026-10-21T0203Z'"),
("cut for the nineteenth run (kept","cut for the twentieth run (kept"),
("but cut for the twenty-first run (kept","but cut for the twenty-second run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0203Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0308Z.json'"),
("Evening run (10:03 PM ET Oct 20 / 02:03 UTC Oct 21, the 02Z slot;","Evening run (11:08 PM ET Oct 20 / 03:08 UTC Oct 21, the 03Z slot;"),
("0059Z ended at 957, so no read went elsewhere in between), parallel batches of up to 13","0203Z ended at 936, so no read went elsewhere in between), parallel batches of up to 13"),
("this 02Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 374 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); ",
 "this 03Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 371 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("f'quote/repost words the/this + is (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 0059Z, next in rotation); '",
 "f'quote/repost words you/\"and\" + my (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0203Z, next in rotation); '"),
("cut for the twenty-first run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the nineteenth run","cut for the twenty-second run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twentieth run"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names LeBron, Brunson, 76ers"):
    lines[i]="            f'trend names Chet, Wemby, #dwts (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0203Z; Chet, Spurs, Wemby and Shai are one event, the Thunder and Spurs NBA game, so Chet and Wemby stand for it and Spurs and Shai were not read; #dwts is the Dancing with the Stars episode, read in 0059Z, with no posts attached in 0203Z); '"
  if l.lstrip().startswith("f'three screening reads by id: 102"):
    lines[i]="            f'three screening reads by id: 106 unread first-hop (two reads) and 26 second-hop referenced, reply-parent and media-source posts (16 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
