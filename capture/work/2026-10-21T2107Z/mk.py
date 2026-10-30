s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/2008Z.json","Build capture/2026/10/21/2107Z.json"),
("work/2026-10-21T2008Z'","work/2026-10-21T2107Z'"),
("RUN_ID = '2026-10-21T2008Z'","RUN_ID = '2026-10-21T2107Z'"),
("STARTED = '2026-10-21T20:08:00Z'","STARTED = '2026-10-21T21:07:00Z'"),
("OBS_AT = '2026-10-21T20:08:00Z'","OBS_AT = '2026-10-21T21:07:00Z'"),
("READS_BEFORE = 594","READS_BEFORE = 575"),
("datetime(2026,10,21,20,11,tzinfo=timezone.utc).timestamp()  # 2008Z (","datetime(2026,10,21,21,10,tzinfo=timezone.utc).timestamp()  # 2107Z (2008Z used 20:11, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_bioware': 'trend_bioware.txt', 'trend_harrykane': 'trend_harrykane.txt',","'trend_diomande': 'trend_diomande.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_bioware','trend.BioWare'),('trend_harrykane','trend.Harry Kane'),","('trend_diomande','trend.Diomande'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2008Z.json') and '/21/' in _c: continue","if _c.endswith('2107Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T1900Z'","_last = '2026-10-21T2008Z'"),
("cut for the thirty-seventh run","cut for the thirty-eighth run"),
("cut for the thirty-ninth run","cut for the fortieth run"),
("(this 20Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 508 long, so the 400 cap left out the 108 slowest-growing posts and no cited post)",
 "(this 21Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 438 long, so the 400 cap left out the 38 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2008Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2107Z.json'"),
("Afternoon run (4:08 PM ET Oct 21 / 20:08 UTC Oct 21, the 20Z slot;","Evening run (5:07 PM ET Oct 21 / 21:07 UTC Oct 21, the 21Z slot;"),
("1900Z ended at 594, so no read went elsewhere in between)","2008Z ended at 575, so no read went elsewhere in between)"),
("20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 508 ids, so the 400 cap left out the 108 slowest-growing posts and no cited post; 4 reads)",
 "21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 438 ids, so the 400 cap left out the 38 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1900Z, next in rotation); '",
 "f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2008Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) == 'trend.Harry Kane': return 'sports'  # 2008Z",
 "        if str(_x) == 'trend.Diomande': return 'sports'  # 2107Z: Yan Diomande goal and assist for Real Madrid\n        if str(_x) == 'trend.Harry Kane': return 'sports'  # 2008Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend name Diomande (\"Diomande lang:en is:retweet\", newest first, 25; the only top-ten US name with no posts attached in 2008Z that is not part of an event already read: Mass Effect, Anthem and KOTOR are the BioWare event; Carrick and Manchester United the Manchester United event; Bayern is the Harry Kane match; #DreaminaOnly29Cents is likely paid promotion; Diomande is Yan Diomande scoring and assisting for Real Madrid); quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 24 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names BioWare and Harry Kane"):
    lines[i]="            f'trend name Diomande (1 read; \"<name> lang:en is:retweet\", newest first, 25; the only top-ten US name with no posts attached in 2008Z outside events already read; Mass Effect, Anthem and KOTOR are the BioWare event, Carrick and Manchester United the Manchester United event, Bayern the Harry Kane match; #DreaminaOnly29Cents is likely paid promotion); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (100 returned; 2108062331095908717 Not Found again), then 24 unread second-hop and leftover posts (24 returned; 1707476764191035402 Not Found); 10 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
