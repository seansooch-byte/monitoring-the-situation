s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0308Z.json","Build capture/2026/10/21/0403Z.json"),
("work/2026-10-21T0308Z'","work/2026-10-21T0403Z'"),
("RUN_ID = '2026-10-21T0308Z'","RUN_ID = '2026-10-21T0403Z'"),
("STARTED = '2026-10-21T03:08:00Z'","STARTED = '2026-10-21T04:03:00Z'"),
("OBS_AT = '2026-10-21T03:09:00Z'","OBS_AT = '2026-10-21T04:04:00Z'"),
("READS_BEFORE = 936","READS_BEFORE = 915"),
("datetime(2026,10,21,3,12,tzinfo=timezone.utc).timestamp()  # 0308Z (0203Z used 02:06,","datetime(2026,10,21,4,6,tzinfo=timezone.utc).timestamp()  # 0403Z (0308Z used 03:12, 0203Z used 02:06,"),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_chet': 'trend_chet.txt', 'trend_wemby': 'trend_wemby.txt', 'trend_dwts': 'trend_dwts.txt',","'trend_mara': 'trend_mara.txt', 'trend_spurs': 'trend_spurs.txt', 'trend_sixers': 'trend_sixers.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_chet','trend.Chet'),('trend_wemby','trend.Wemby'),('trend_dwts','trend.#dwts'),","('trend_mara','trend.Mara'),('trend_spurs','trend.Spurs'),('trend_sixers','trend.Sixers'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) in ('trend.Chet','trend.Wemby','trend.Spurs','trend.Shai'): return 'sports'  # 0308Z: NBA opening week (Thunder and Spurs)\n","        if str(_x) in ('trend.Chet','trend.Wemby','trend.Spurs','trend.Shai'): return 'sports'  # 0308Z: NBA opening week (Thunder and Spurs)\n        if str(_x) in ('trend.Mara','trend.Thunder','trend.Sixers'): return 'sports'  # 0403Z: Aday Mara of the Thunder (Thunder and Spurs game); Sixers (76ers at Knicks)\n"),
("if _c.endswith('0308Z.json') and '/21/' in _c: continue","if _c.endswith('0403Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 03Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 371 long, under the 400 cap, so nothing was left out)","(this 04Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 443 long, so the 400 cap left out the 43 slowest-growing posts of the fourth-hour tier and no cited post)"),
('sensors news/money/science (one read each); trend names Chet, Wemby, #dwts (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0203Z); quote/repost words you/"and" + my; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (106 first-hop in two reads, then 26 second-hop)',
 'sensors culture/sports/online (one read each); trend names Mara, Spurs, Sixers (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0308Z); quote/repost words it/that + just; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (103 first-hop in two reads, then 22 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"you\", \"and\" and \"my\": (you lang:en is:quote -is:retweet), (\"and\" lang:en is:quote -is:retweet, quoted because X refuses a bare and), (my lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"it\", \"that\" and \"just\": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T0203Z'","_last = '2026-10-21T0308Z'"),
("cut for the twentieth run (kept","cut for the twenty-first run (kept"),
("but cut for the twenty-second run (kept","but cut for the twenty-third run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0308Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0403Z.json'"),
("Evening run (11:08 PM ET Oct 20 / 03:08 UTC Oct 21, the 03Z slot;","Late-night run (12:03 AM ET Oct 21 / 04:03 UTC Oct 21, the 04Z slot;"),
("0203Z ended at 936, so no read went elsewhere in between), parallel batches of up to 13","0308Z ended at 915, so no read went elsewhere in between), parallel batches of up to 13"),
("this 03Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 371 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); ",
 "this 04Z-slot run is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 443 ids, so the 400 cap left out the 43 slowest-growing posts of the fourth-hour tier and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("f'quote/repost words you/\"and\" + my (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0203Z, next in rotation); '",
 "f'quote/repost words it/that + just (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 0308Z, next in rotation); '"),
("cut for the twenty-second run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twentieth run","cut for the twenty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twenty-first run"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Chet, Wemby, #dwts"):
    lines[i]="            f'trend names Mara, Spurs, Sixers (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0308Z; Wemby, Spurs, Chet, Shai and Mara are one event, the Thunder and Spurs NBA game (Mara is Aday Mara of the Thunder), and Sixers, Knicks, Embiid and Maxey are one event, the 76ers at Knicks game); '"
  if l.lstrip().startswith("f'three screening reads by id: 106"):
    lines[i]="            f'three screening reads by id: 103 unread first-hop (two reads) and 22 second-hop referenced, reply-parent and media-source posts (12 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
