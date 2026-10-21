s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1709Z.json","Build capture/2026/10/21/1808Z.json"),
("work/2026-10-21T1709Z'","work/2026-10-21T1808Z'"),
("RUN_ID = '2026-10-21T1709Z'","RUN_ID = '2026-10-21T1808Z'"),
("STARTED = '2026-10-21T17:09:00Z'","STARTED = '2026-10-21T18:08:00Z'"),
("OBS_AT = '2026-10-21T17:09:00Z'","OBS_AT = '2026-10-21T18:08:00Z'"),
("READS_BEFORE = 651","READS_BEFORE = 633"),
("datetime(2026,10,21,17,14,tzinfo=timezone.utc).timestamp()  # 1709Z (","datetime(2026,10,21,18,12,tzinfo=timezone.utc).timestamp()  # 1808Z (1709Z used 17:14, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_nicopaz': 'trend_nicopaz.txt',","'trend_bioware': 'trend_bioware.txt', 'trend_carrick': 'trend_carrick.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_nicopaz','trend.Nico Paz'),","('trend_bioware','trend.BioWare'),('trend_carrick','trend.Carrick'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1709Z.json') and '/21/' in _c: continue","if _c.endswith('1808Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
('sensors news/money/science (one read each); trend name Nico Paz ("\\"Nico Paz\\" lang:en is:retweet", newest first, 25; the one current top-ten US name with no posts attached in 1604Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (99 unread referenced first-hop, then 25 second-hop and leftover)',
 'sensors culture/sports/online (one read each); trend names BioWare and Carrick (each "<name> lang:en is:retweet", newest first, 25; BioWare stands for BioWare, Mass Effect, Dragon Age, Anthem and KOTOR, one event; Carrick stands for Carrick, Manchester United and Man U, one event; none had posts attached in 1709Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (87 unread referenced first-hop, then 21 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T1604Z'","_last = '2026-10-21T1709Z'"),
("cut for the thirty-fourth run","cut for the thirty-fifth run"),
("cut for the thirty-sixth run","cut for the thirty-seventh run"),
("(this 17Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 447 long, so the 400 cap left out the 47 slowest-growing still-gaining posts and no cited post)",
 "(this 18Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 455 long, so the 400 cap left out the 55 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1709Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1808Z.json'"),
("Afternoon run (1:09 PM ET Oct 21 / 17:09 UTC Oct 21, the 17Z slot;","Afternoon run (2:08 PM ET Oct 21 / 18:08 UTC Oct 21, the 18Z slot;"),
("1604Z ended at 651, so no read went elsewhere in between), parallel batches of up to 12","1709Z ended at 633, so no read went elsewhere in between), parallel batches of up to 8"),
("17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 447 ids, so the 400 cap left out the 47 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 455 ids, so the 400 cap left out the 55 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words just/what + the (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 1604Z, next in rotation); '",
 "f'quote/repost words this/is + you (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 1709Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
("        if str(_x) == 'trend.Nico Paz': return 'sports'  # 1709Z",
 "        if str(_x) == 'trend.BioWare': return 'gaming'  # 1808Z: BioWare games studio (Mass Effect, Dragon Age, Anthem, KOTOR trend with it)\n        if str(_x) == 'trend.Carrick': return 'sports'  # 1808Z: Manchester United (Man U, Manchester United trend with it)\n        if str(_x) == 'trend.Nico Paz': return 'sports'  # 1709Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend name \"Nico Paz\""):
    lines[i]="            f'trend names BioWare and Carrick (2 reads; \"<name> lang:en is:retweet\", newest first, 25 each; BioWare, Mass Effect, Dragon Age, Anthem and KOTOR are one event and BioWare was read for all five; Carrick, Manchester United and Man U are one event and Carrick was read for all three; Nico Paz was read in 1709Z and #DreaminaOnly29Cents is likely paid promotion); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 99"):
    lines[i]="            f'two screening reads by id: 87 unread first-hop referenced, reply-parent and media-source posts (all 87 returned), then 21 unread second-hop and leftover posts (all 21 returned; 2108062331095908717 is Not Found again and was not re-read); 11 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
