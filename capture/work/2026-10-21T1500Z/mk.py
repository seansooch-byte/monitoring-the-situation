s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1402Z.json","Build capture/2026/10/21/1500Z.json"),
("work/2026-10-21T1402Z'","work/2026-10-21T1500Z'"),
("RUN_ID = '2026-10-21T1402Z'","RUN_ID = '2026-10-21T1500Z'"),
("STARTED = '2026-10-21T14:02:00Z'","STARTED = '2026-10-21T15:00:00Z'"),
("OBS_AT = '2026-10-21T14:02:00Z'","OBS_AT = '2026-10-21T15:00:00Z'"),
("READS_BEFORE = 708","READS_BEFORE = 689"),
("datetime(2026,10,21,14,5,tzinfo=timezone.utc).timestamp()  # 1402Z (","datetime(2026,10,21,15,3,tzinfo=timezone.utc).timestamp()  # 1500Z (1402Z used 14:05, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_abolish': 'trend_abolish.txt', 'trend_eagle4': 'trend_eagle4.txt',","'trend_glee': 'trend_glee.txt', 'trend_gmmtv': 'trend_gmmtv.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_abolish','trend.Abolish'),('trend_eagle4','trend.EAGLE-4'),","('trend_glee','trend.Glee'),('trend_gmmtv','trend.GMMTV'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1402Z.json') and '/21/' in _c: continue","if _c.endswith('1500Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
('sensors culture/sports/online (one read each); trend names Abolish, EAGLE-4 (each "<name> lang:en is:retweet", newest first, 25 each, "EAGLE-4" in quotes; two current top-ten US names with no posts attached in 1302Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 24 second-hop and leftover)',
 'sensors news/money/science (one read each); trend names Glee, GMMTV (each "<name> lang:en is:retweet", newest first, 25 each; two current top-ten US names with no posts attached in 1402Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (98 unread referenced first-hop, then 21 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T1302Z'","_last = '2026-10-21T1402Z'"),
("cut for the thirty-third run","cut for the thirty-fourth run"),
("cut for the thirty-first run","cut for the thirty-second run"),
("(this 14Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 425 long, so the 400 cap left out the 25 slowest-growing still-gaining posts and no cited post)",
 "(this 15Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 436 long, so the 400 cap left out the 36 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1402Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1500Z.json'"),
("Morning run (10:02 AM ET Oct 21 / 14:02 UTC Oct 21, the 14Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)","Morning run (11:00 AM ET Oct 21 / 15:00 UTC Oct 21, the 15Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)"),
("1302Z ended at 708, so no read went elsewhere in between), parallel batches of up to 12","1402Z ended at 689, so no read went elsewhere in between), parallel batches of up to 12"),
("14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 425 ids, so the 400 cap left out the 25 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 436 ids, so the 400 cap left out the 36 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words just/what + the (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 1302Z, next in rotation); '",
 "f'quote/repost words this/is + you (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 1402Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
("        if str(_x) == 'trend.Abolish': return 'politics'  # 1402Z",
 "        if str(_x) == 'trend.Glee': return 'entertainment'  # 1500Z: the TV show Glee\n        if str(_x) == 'trend.GMMTV': return 'entertainment'  # 1500Z: Thai TV studio GMMTV and its series\n        if str(_x) == 'trend.Abolish': return 'politics'  # 1402Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Abolish, \"EAGLE-4\""):
    lines[i]="            f'trend names Glee, GMMTV (2 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; two of the top-ten US names with no posts attached in 1402Z; the others were read in 1402Z or earlier (Witkoff and Stephen Hubbard in 1302Z; We Demand Action, #BladeRunnerSupportsRacist, #RespectMyanmarCulture and #pilotstwtselfieday are fan campaigns) or are greetings (Good Wednesday); TRENDNOTE); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 98 unread first-hop referenced, reply-parent and media-source posts (1 Not Found: 2108062331095908717 again), then 21 unread second-hop and leftover posts (all 21 returned); 13 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
