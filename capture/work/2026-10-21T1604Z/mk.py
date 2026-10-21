s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1500Z.json","Build capture/2026/10/21/1604Z.json"),
("work/2026-10-21T1500Z'","work/2026-10-21T1604Z'"),
("RUN_ID = '2026-10-21T1500Z'","RUN_ID = '2026-10-21T1604Z'"),
("STARTED = '2026-10-21T15:00:00Z'","STARTED = '2026-10-21T16:04:00Z'"),
("OBS_AT = '2026-10-21T15:00:00Z'","OBS_AT = '2026-10-21T16:04:00Z'"),
("READS_BEFORE = 689","READS_BEFORE = 670"),
("datetime(2026,10,21,15,3,tzinfo=timezone.utc).timestamp()  # 1500Z (","datetime(2026,10,21,16,8,tzinfo=timezone.utc).timestamp()  # 1604Z (1500Z used 15:03, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_you': 'repost_you.txt',","'repost_that': 'repost_that.txt',"),
("'trend_glee': 'trend_glee.txt', 'trend_gmmtv': 'trend_gmmtv.txt',","'trend_locksley': 'trend_locksley.txt', 'trend_cashman': 'trend_cashman.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_glee','trend.Glee'),('trend_gmmtv','trend.GMMTV'),","('trend_locksley','trend.Mike Locksley'),('trend_cashman','trend.Cashman'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1500Z.json') and '/21/' in _c: continue","if _c.endswith('1604Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
('sensors news/money/science (one read each); trend names Glee, GMMTV (each "<name> lang:en is:retweet", newest first, 25 each; two current top-ten US names with no posts attached in 1402Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (98 unread referenced first-hop, then 21 second-hop and leftover)',
 'sensors culture/sports/online (one read each); trend names Mike Locksley, Cashman (each "<name> lang:en is:retweet", newest first, 25 each, "Mike Locksley" in quotes; two current top-ten US names with no posts attached in 1500Z); quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id (93 unread referenced first-hop, then 16 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"my\", \"it\" and \"that\": (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each (\"and\" skipped in the rotation; X refused it in 1007Z)'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T1402Z'","_last = '2026-10-21T1500Z'"),
("cut for the thirty-fourth run","cut for the thirty-fifth run"),
("cut for the thirty-second run","cut for the thirty-third run"),
("(this 15Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 436 long, so the 400 cap left out the 36 slowest-growing still-gaining posts and no cited post)",
 "(this 16Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 528 long, so the 400 cap left out the 128 slowest-growing fourth-hour posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1500Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1604Z.json'"),
("Morning run (11:00 AM ET Oct 21 / 15:00 UTC Oct 21, the 15Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)","Midday run (12:04 PM ET Oct 21 / 16:04 UTC Oct 21, the 16Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)"),
("1402Z ended at 689, so no read went elsewhere in between), parallel batches of up to 12","1500Z ended at 670, so no read went elsewhere in between), parallel batches of up to 12"),
("15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 436 ids, so the 400 cap left out the 36 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "16Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 528 ids, so the 400 cap left out the 128 slowest-growing fourth-hour posts and no cited post; 4 reads)"),
("f'quote/repost words this/is + you (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 1402Z, next in rotation); '",
 "f'quote/repost words my/it + that (3 reads; \"and\" skipped, X refused it in 1007Z); sensors culture/sports/online (3 reads; news/money/science last read 1500Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
("        if str(_x) == 'trend.Glee': return 'entertainment'  # 1500Z",
 "        if str(_x) == 'trend.Mike Locksley': return 'sports'  # 1604Z: college football coach\n        if str(_x) == 'trend.Cashman': return 'sports'  # 1604Z: Yankees general manager Brian Cashman\n        if str(_x) == 'trend.Glee': return 'entertainment'  # 1500Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Glee, GMMTV"):
    lines[i]="            f'trend names \"Mike Locksley\", Cashman (2 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, \"Mike Locksley\" in quotes; two of the top-ten US names with no posts attached in 1500Z; the others were read in 1500Z or earlier (Glee and GMMTV in 1500Z, Abolish in 1402Z, Witkoff in 1302Z) or are fan campaigns (#RespectMyanmarCulture, We Demand Action) or likely paid promotion (#DreaminaOnly29Cents); TRENDNOTE); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 98"):
    lines[i]="            f'two screening reads by id: 93 unread first-hop referenced, reply-parent and media-source posts (1 Not Found: 2108062331095908717 again), then 16 unread second-hop and leftover posts (all 16 returned); 12 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
