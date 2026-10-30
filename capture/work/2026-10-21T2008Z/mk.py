s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1900Z.json","Build capture/2026/10/21/2008Z.json"),
("work/2026-10-21T1900Z'","work/2026-10-21T2008Z'"),
("RUN_ID = '2026-10-21T1900Z'","RUN_ID = '2026-10-21T2008Z'"),
("STARTED = '2026-10-21T19:00:00Z'","STARTED = '2026-10-21T20:08:00Z'"),
("OBS_AT = '2026-10-21T19:00:00Z'","OBS_AT = '2026-10-21T20:08:00Z'"),
("READS_BEFORE = 614","READS_BEFORE = 594"),
("datetime(2026,10,21,19,3,tzinfo=timezone.utc).timestamp()  # 1900Z (","datetime(2026,10,21,20,11,tzinfo=timezone.utc).timestamp()  # 2008Z (1900Z used 19:03, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_nicopaz': 'trend_nicopaz.txt', 'trend_glee': 'trend_glee.txt',","'trend_bioware': 'trend_bioware.txt', 'trend_harrykane': 'trend_harrykane.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_nicopaz','trend.Nico Paz'),('trend_glee','trend.Glee'),","('trend_bioware','trend.BioWare'),('trend_harrykane','trend.Harry Kane'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1900Z.json') and '/21/' in _c: continue","if _c.endswith('2008Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
('sensors news/money/science (one read each); trend names Nico Paz and Glee (each "<name> lang:en is:retweet", newest first, 25; the two current top-ten US names with no posts attached in 1808Z that are not part of an event already read then: Anthem is the BioWare event, Man U and #MUFC the Carrick event, and #DreaminaOnly29Cents is likely paid promotion); quote/repost words and/my + it; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 26 second-hop and leftover)',
 'sensors culture/sports/online (one read each); trend names BioWare and Harry Kane (BioWare as "<name> lang:en is:retweet", Harry Kane quoted, newest first, 25 each; the top-ten US names with no posts attached in 1900Z: BioWare stands for BioWare, Mass Effect, Anthem and KOTOR, one event; Carrick and Man U are the Manchester United event, which had a post attached in 1900Z; #DreaminaOnly29Cents is likely paid promotion; Harry Kane is his Bayern Munich Champions League match); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 27 second-hop and leftover)'),
("'2 quote pages + 1 repost page (budget), common words \"and\", \"my\" and \"it\": (\"and\" lang:en is:quote -is:retweet; the bare word was rejected by X as an ambiguous keyword, one read spent, and re-run quoted), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"that\", \"just\" and \"what\", each quoted so X does not reject a bare stopword: (\"that\" lang:en is:quote -is:retweet), (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T1808Z'","_last = '2026-10-21T1900Z'"),
("cut for the thirty-sixth run","cut for the thirty-seventh run"),
("cut for the thirty-eighth run","cut for the thirty-ninth run"),
("(this 19Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 456 long, so the 400 cap left out the 56 slowest-growing still-gaining posts and no cited post)",
 "(this 20Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 508 long, so the 400 cap left out the 108 slowest-growing posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1900Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2008Z.json'"),
("Afternoon run (3:00 PM ET Oct 21 / 19:00 UTC Oct 21, the 19Z slot;","Afternoon run (4:08 PM ET Oct 21 / 20:08 UTC Oct 21, the 20Z slot;"),
("1808Z ended at 614, so no read went elsewhere in between; one of the reads was the bare \"and\" quote stream, rejected by X as an ambiguous keyword and re-run quoted), parallel batches of up to 12, no 429 refusals.","1900Z ended at 594, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals."),
("19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 456 ids, so the 400 cap left out the 56 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 508 ids, so the 400 cap left out the 108 slowest-growing posts and no cited post; 4 reads)"),
("f'quote/repost words and/my + it (4 reads, one rejected); sensors news/money/science (3 reads; culture/sports/online last read 1808Z, next in rotation); '",
 "f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1900Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
("        if str(_x) == 'trend.Glee': return 'entertainment'  # 1900Z",
 "        if str(_x) == 'trend.Harry Kane': return 'sports'  # 2008Z: Bayern Munich Champions League match\n        if str(_x) == 'trend.Glee': return 'entertainment'  # 1900Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Nico Paz and Glee"):
    lines[i]="            f'trend names BioWare and Harry Kane (2 reads; \"<name> lang:en is:retweet\", Harry Kane quoted, newest first, 25 each; the top-ten US names with no posts attached in 1900Z; Mass Effect, Anthem and KOTOR are the BioWare event; Carrick and Man U are the Manchester United event, which had a post attached in 1900Z; #DreaminaOnly29Cents is likely paid promotion); '"; hit+=1
  if l.lstrip().startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (all 100 returned), then 27 unread second-hop and leftover posts (all 27 returned; 2108062331095908717 is Not Found again and was not re-read); 10 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
