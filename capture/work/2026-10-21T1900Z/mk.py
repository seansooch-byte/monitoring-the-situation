s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1808Z.json","Build capture/2026/10/21/1900Z.json"),
("work/2026-10-21T1808Z'","work/2026-10-21T1900Z'"),
("RUN_ID = '2026-10-21T1808Z'","RUN_ID = '2026-10-21T1900Z'"),
("STARTED = '2026-10-21T18:08:00Z'","STARTED = '2026-10-21T19:00:00Z'"),
("OBS_AT = '2026-10-21T18:08:00Z'","OBS_AT = '2026-10-21T19:00:00Z'"),
("READS_BEFORE = 633","READS_BEFORE = 614"),
("datetime(2026,10,21,18,12,tzinfo=timezone.utc).timestamp()  # 1808Z (","datetime(2026,10,21,19,3,tzinfo=timezone.utc).timestamp()  # 1900Z (1808Z used 18:12, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_bioware': 'trend_bioware.txt', 'trend_carrick': 'trend_carrick.txt',","'trend_nicopaz': 'trend_nicopaz.txt', 'trend_glee': 'trend_glee.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_bioware','trend.BioWare'),('trend_carrick','trend.Carrick'),","('trend_nicopaz','trend.Nico Paz'),('trend_glee','trend.Glee'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1808Z.json') and '/21/' in _c: continue","if _c.endswith('1900Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
('sensors culture/sports/online (one read each); trend names BioWare and Carrick (each "<name> lang:en is:retweet", newest first, 25; BioWare stands for BioWare, Mass Effect, Dragon Age, Anthem and KOTOR, one event; Carrick stands for Carrick, Manchester United and Man U, one event; none had posts attached in 1709Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (87 unread referenced first-hop, then 21 second-hop and leftover)',
 'sensors news/money/science (one read each); trend names Nico Paz and Glee (each "<name> lang:en is:retweet", newest first, 25; the two current top-ten US names with no posts attached in 1808Z that are not part of an event already read then: Anthem is the BioWare event, Man U and #MUFC the Carrick event, and #DreaminaOnly29Cents is likely paid promotion); quote/repost words and/my + it; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 26 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"and\", \"my\" and \"it\": (\"and\" lang:en is:quote -is:retweet; the bare word was rejected by X as an ambiguous keyword, one read spent, and re-run quoted), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T1709Z'","_last = '2026-10-21T1808Z'"),
("cut for the thirty-fifth run","cut for the thirty-sixth run"),
("cut for the thirty-seventh run","cut for the thirty-eighth run"),
("(this 18Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 455 long, so the 400 cap left out the 55 slowest-growing still-gaining posts and no cited post)",
 "(this 19Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 456 long, so the 400 cap left out the 56 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1808Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1900Z.json'"),
("Afternoon run (2:08 PM ET Oct 21 / 18:08 UTC Oct 21, the 18Z slot;","Afternoon run (3:00 PM ET Oct 21 / 19:00 UTC Oct 21, the 19Z slot;"),
("1709Z ended at 633, so no read went elsewhere in between), parallel batches of up to 8, no 429 refusals.","1808Z ended at 614, so no read went elsewhere in between; one of the reads was the bare \"and\" quote stream, rejected by X as an ambiguous keyword and re-run quoted), parallel batches of up to 12, no 429 refusals."),
("18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 455 ids, so the 400 cap left out the 55 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 456 ids, so the 400 cap left out the 56 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words this/is + you (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 1709Z, next in rotation); '",
 "f'quote/repost words and/my + it (4 reads, one rejected); sensors news/money/science (3 reads; culture/sports/online last read 1808Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
("        if str(_x) == 'trend.BioWare': return 'gaming'  # 1808Z",
 "        if str(_x) == 'trend.Glee': return 'entertainment'  # 1900Z: Glee reboot series order at Disney+ and Hulu\n        if str(_x) == 'trend.BioWare': return 'gaming'  # 1808Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names BioWare and Carrick"):
    lines[i]="            f'trend names Nico Paz and Glee (2 reads; \"<name> lang:en is:retweet\", newest first, 25 each; the current top-ten US names with no posts attached in 1808Z; Anthem was read as part of the BioWare event and Man U and #MUFC as part of the Carrick event in 1808Z, and #DreaminaOnly29Cents is likely paid promotion); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 87"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (all 100 returned), then 26 unread second-hop and leftover posts (all 26 returned; 2108062331095908717 is Not Found again and was not re-read); 14 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
