s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1604Z.json","Build capture/2026/10/21/1709Z.json"),
("work/2026-10-21T1604Z'","work/2026-10-21T1709Z'"),
("RUN_ID = '2026-10-21T1604Z'","RUN_ID = '2026-10-21T1709Z'"),
("STARTED = '2026-10-21T16:04:00Z'","STARTED = '2026-10-21T17:09:00Z'"),
("OBS_AT = '2026-10-21T16:04:00Z'","OBS_AT = '2026-10-21T17:09:00Z'"),
("READS_BEFORE = 670","READS_BEFORE = 651"),
("datetime(2026,10,21,16,8,tzinfo=timezone.utc).timestamp()  # 1604Z (","datetime(2026,10,21,17,14,tzinfo=timezone.utc).timestamp()  # 1709Z (1604Z used 16:08, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_locksley': 'trend_locksley.txt', 'trend_cashman': 'trend_cashman.txt',","'trend_nicopaz': 'trend_nicopaz.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_locksley','trend.Mike Locksley'),('trend_cashman','trend.Cashman'),","('trend_nicopaz','trend.Nico Paz'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1604Z.json') and '/21/' in _c: continue","if _c.endswith('1709Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
('sensors culture/sports/online (one read each); trend names Mike Locksley, Cashman (each "<name> lang:en is:retweet", newest first, 25 each, "Mike Locksley" in quotes; two current top-ten US names with no posts attached in 1500Z); quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id (93 unread referenced first-hop, then 16 second-hop and leftover)',
 'sensors news/money/science (one read each); trend name Nico Paz ("\\"Nico Paz\\" lang:en is:retweet", newest first, 25; the one current top-ten US name with no posts attached in 1604Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (99 unread referenced first-hop, then 25 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"my\", \"it\" and \"that\": (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each (\"and\" skipped in the rotation; X refused it in 1007Z)'",
 "'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T1500Z'","_last = '2026-10-21T1604Z'"),
("cut for the thirty-third run","cut for the thirty-fourth run"),
("cut for the thirty-fifth run","cut for the thirty-sixth run"),
("(this 16Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 528 long, so the 400 cap left out the 128 slowest-growing fourth-hour posts and no cited post)",
 "(this 17Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 447 long, so the 400 cap left out the 47 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1604Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1709Z.json'"),
("Midday run (12:04 PM ET Oct 21 / 16:04 UTC Oct 21, the 16Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)","Afternoon run (1:09 PM ET Oct 21 / 17:09 UTC Oct 21, the 17Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)"),
("1500Z ended at 670, so no read went elsewhere in between), parallel batches of up to 12","1604Z ended at 651, so no read went elsewhere in between), parallel batches of up to 12"),
("16Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 528 ids, so the 400 cap left out the 128 slowest-growing fourth-hour posts and no cited post; 4 reads)",
 "17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 447 ids, so the 400 cap left out the 47 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words my/it + that (3 reads; \"and\" skipped, X refused it in 1007Z); sensors culture/sports/online (3 reads; news/money/science last read 1500Z, next in rotation); '",
 "f'quote/repost words just/what + the (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 1604Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
("        if str(_x) == 'trend.Mike Locksley': return 'sports'  # 1604Z: college football coach",
 "        if str(_x) == 'trend.Nico Paz': return 'sports'  # 1709Z: Como footballer, Champions League goal against Manchester United\n        if str(_x) == 'trend.Mike Locksley': return 'sports'  # 1604Z: college football coach"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names \"Mike Locksley\", Cashman"):
    lines[i]="            f'trend name \"Nico Paz\" (1 read; \"\\\\\"Nico Paz\\\\\" lang:en is:retweet\", newest first, 25; the one top-ten US name with no posts attached in 1604Z; the others were read in 1604Z or earlier (Mike Locksley and Cashman in 1604Z, Glee in 1500Z, Abolish in 1402Z, Witkoff in 1302Z) or are fan campaigns (#RespectMyanmarCulture, We Demand Action, #pilotstwtselfieday) or likely paid promotion (#DreaminaOnly29Cents); Nico Paz is his early goal for Como against Manchester United); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 93"):
    lines[i]="            f'two screening reads by id: 99 unread first-hop referenced, reply-parent and media-source posts (all 99 returned), then 25 unread second-hop and leftover posts (1 Not Found: 2108062331095908717 again); 14 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
