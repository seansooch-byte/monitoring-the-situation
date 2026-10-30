s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1302Z.json","Build capture/2026/10/21/1402Z.json"),
("work/2026-10-21T1302Z'","work/2026-10-21T1402Z'"),
("RUN_ID = '2026-10-21T1302Z'","RUN_ID = '2026-10-21T1402Z'"),
("STARTED = '2026-10-21T13:02:00Z'","STARTED = '2026-10-21T14:02:00Z'"),
("OBS_AT = '2026-10-21T13:02:00Z'","OBS_AT = '2026-10-21T14:02:00Z'"),
("READS_BEFORE = 727","READS_BEFORE = 708"),
("datetime(2026,10,21,13,5,tzinfo=timezone.utc).timestamp()  # 1302Z (","datetime(2026,10,21,14,5,tzinfo=timezone.utc).timestamp()  # 1402Z (1302Z used 13:05, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_hubbard': 'trend_hubbard.txt', 'trend_witkoff': 'trend_witkoff.txt',","'trend_abolish': 'trend_abolish.txt', 'trend_eagle4': 'trend_eagle4.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_hubbard','trend.Stephen Hubbard'),('trend_witkoff','trend.Witkoff'),","('trend_abolish','trend.Abolish'),('trend_eagle4','trend.EAGLE-4'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1302Z.json') and '/21/' in _c: continue","if _c.endswith('1402Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
('sensors news/money/science (one read each); trend names Stephen Hubbard, Witkoff (each "<name> lang:en is:retweet", newest first, 25 each, the multi-word name in quotes; the two current top-ten US names with no posts attached in 1204Z, other than greetings); quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id (91 unread referenced first-hop, then 21 second-hop and leftover)',
 'sensors culture/sports/online (one read each); trend names Abolish, EAGLE-4 (each "<name> lang:en is:retweet", newest first, 25 each, "EAGLE-4" in quotes; two current top-ten US names with no posts attached in 1302Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 24 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"my\", \"it\" and \"that\": (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each; \"and\" skipped in the rotation because X refused it as a query in 1007Z'",
 "'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T1204Z'","_last = '2026-10-21T1302Z'"),
("cut for the thirty-second run","cut for the thirty-third run"),
("cut for the thirtieth run","cut for the thirty-first run"),
("(this 13Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 412 long, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post)",
 "(this 14Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 425 long, so the 400 cap left out the 25 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1302Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1402Z.json'"),
("Morning run (9:02 AM ET Oct 21 / 13:02 UTC Oct 21, the 13Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)","Morning run (10:02 AM ET Oct 21 / 14:02 UTC Oct 21, the 14Z slot; 12:00-05:00 UTC band, up to 42 reads, kept to about 20 reads per the scheduling instruction)"),
("1204Z ended at 727, so no read went elsewhere in between), parallel batches of up to 12","1302Z ended at 708, so no read went elsewhere in between), parallel batches of up to 12"),
("13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 412 ids, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 425 ids, so the 400 cap left out the 25 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words my/it + that (3 reads; \"and\" skipped in the rotation, X refused it in 1007Z); sensors news/money/science (3 reads; culture/sports/online last read 1204Z, next in rotation); '",
 "f'quote/repost words just/what + the (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 1302Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
("        if str(_x) == 'trend.Witkoff': return 'world'  # 1302Z",
 "        if str(_x) == 'trend.Abolish': return 'politics'  # 1402Z: mostly reposts of an 'Abolish ICE.' post, with other 'Abolish ...' slogans\n        if str(_x) == 'trend.Witkoff': return 'world'  # 1302Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names \"Stephen Hubbard\", Witkoff"):
    lines[i]="            f'trend names Abolish, \"EAGLE-4\" (2 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, \"EAGLE-4\" in quotes; two of the top-ten US names with no posts attached in 1302Z; the others were read in 1204Z or earlier (We Demand Action, #BladeRunnerSupportsRacist, #papergamesisracist, #RespectMyanmarCulture, #ScarletHeartTH and the Chinese-language Papergames tag are the same two fan campaigns) or are greetings (Good Wednesday); Abolish is mostly reposts of one \"Abolish ICE.\" post; EAGLE-4 is the speculative-decoding release, with paid promotion in its stream as in 0559Z); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 91"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (2 Not Found: 2112595033022922763 and 2108062331095908717 again), then 24 unread second-hop and leftover posts (all 24 returned; the two Not Found ids left out); 12 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
