s=open('../2026-10-20T1905Z/build_capture.py').read()
R=[
("Build capture/2026/10/20/1905Z.json","Build capture/2026/10/20/2007Z.json"),
("work/2026-10-20T1905Z'","work/2026-10-20T2007Z'"),
("RUN_ID = '2026-10-20T1905Z'","RUN_ID = '2026-10-20T2007Z'"),
("STARTED = '2026-10-20T19:05:00Z'","STARTED = '2026-10-20T20:07:00Z'"),
("OBS_AT = '2026-10-20T19:06:00Z'","OBS_AT = '2026-10-20T20:08:00Z'"),
("READS_BEFORE = 565","READS_BEFORE = 542"),
("datetime(2026,10,20,19,8,tzinfo=timezone.utc).timestamp()  # 1905Z (1804Z","datetime(2026,10,20,20,10,tzinfo=timezone.utc).timestamp()  # 2007Z (1905Z used 19:08, 1804Z"),
("'quote_what': 'quote_what.txt', 'quote_and': 'quote_and.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_you': 'repost_you.txt',","'repost_is': 'repost_is.txt',"),
("'trend_nickshirley': 'trend_nickshirley.txt', 'trend_bach': 'trend_bach.txt', 'trend_celtics': 'trend_celtics.txt',","'trend_pistons': 'trend_pistons.txt', 'trend_dembele': 'trend_dembele.txt', 'trend_mitchellrobinson': 'trend_mitchellrobinson.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_what','quote'),('quote_and','quote'),('repost_you','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_nickshirley','trend.Nick Shirley'),('trend_bach','trend.Bach'),('trend_celtics','trend.Celtics'),","('trend_pistons','trend.Pistons'),('trend_dembele','trend.Dembele'),('trend_mitchellrobinson','trend.Mitchell Robinson'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1905Z.json') and '/20/' in _c: continue","if _c.endswith('2007Z.json') and '/20/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(19Z is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 424 long, so the 400 cap left out the 24 slowest-growing still-gaining posts, and no cited post)","then, as 20Z is a fourth hour, the rest of the last 24 hours fastest growing first; with every pulse- and story-cited post placed right after the watch.json ids the list was 479 long, so the 400 cap left out the 79 slowest-growing posts (all of the fourth-hour tier and the slowest still-gaining posts), and no cited post"),
("'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Nick Shirley\", Bach, Celtics (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the eight current top-ten US names with no posts attached in 1804Z); quote/repost words what/\"and\" + you; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (92 first-hop in one read, then 17 second-hop); story clusters not read for the budget; screened by id with global floor/pace'",
 "'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names Pistons, Dembele, \"Mitchell Robinson\" (each \"<name> lang:en is:retweet\", newest first, 25 each, names quoted when they have a space; three of the nine current top-ten US names with no posts attached in 1905Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (126 first-hop in two reads, then 29 second-hop); story clusters not read for the budget; screened by id with global floor/pace'"),
("'2 quote pages + 1 repost page (budget), common words \"what\", \"and\" and \"you\": (what lang:en is:quote -is:retweet), (\"and\" lang:en is:quote -is:retweet; \"and\" must be quoted, the unquoted query was refused as invalid and cost one read), (you lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"the\", \"this\" and \"is\": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-20T1804Z'","_last = '2026-10-20T1905Z'"),
("cut for the twelfth run (kept","cut for the thirteenth run (kept"),
("but cut for the fourteenth run (kept","but cut for the fifteenth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/1905Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/20/2007Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:80])
  s=s.replace(a,b)
open('build_capture.py','w').write(s)
