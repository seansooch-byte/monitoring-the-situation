s=open('build_capture.py').read()
TN=open('trend_note.txt').read().strip()
R=[
("Build capture/2026/10/21/2203Z.json","Build capture/2026/10/21/2301Z.json"),
("work/2026-10-21T2203Z'","work/2026-10-21T2301Z'"),
("RUN_ID = '2026-10-21T2203Z'","RUN_ID = '2026-10-21T2301Z'"),
("STARTED = '2026-10-21T22:03:00Z'","STARTED = '2026-10-21T23:01:00Z'"),
("OBS_AT = '2026-10-21T22:03:00Z'","OBS_AT = '2026-10-21T23:01:00Z'"),
("READS_BEFORE = 557","READS_BEFORE = 538"),
("datetime(2026,10,21,22,6,tzinfo=timezone.utc).timestamp()  # 2203Z (","datetime(2026,10,21,23,4,tzinfo=timezone.utc).timestamp()  # 2301Z (2203Z used 22:06, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_kenan': 'trend_kenan.txt', 'trend_claudeduet': 'trend_claudeduet.txt',","'trend_haiti': 'trend_haiti.txt', 'trend_ilhannur': 'trend_ilhannur.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_kenan','trend.Kenan'),('trend_claudeduet','trend.Claude Duet'),","('trend_haiti','trend.Haiti'),('trend_ilhannur','trend.Ilhan Nur'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2203Z.json') and '/21/' in _c: continue","if _c.endswith('2301Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T2107Z'","_last = '2026-10-21T2203Z'"),
("cut for the thirty-ninth run","cut for the fortieth run"),
("cut for the forty-first run","cut for the forty-second run"),
("(this 22Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 435 long, so the 400 cap left out the 35 slowest-growing still-gaining posts and no cited post)",
 "(this 23Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 431 long, so the 400 cap left out the 31 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2203Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2301Z.json'"),
("Evening run (6:03 PM ET Oct 21 / 22:03 UTC Oct 21, the 22Z slot;","Evening run (7:01 PM ET Oct 21 / 23:01 UTC Oct 21, the 23Z slot, the last run of the UTC day;"),
("2107Z ended at 557, so no read went elsewhere in between)","2203Z ended at 538, so no read went elsewhere in between)"),
("22Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 435 ids, so the 400 cap left out the 35 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "23Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 431 ids, so the 400 cap left out the 31 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2107Z, next in rotation); '",
 "f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2203Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) == 'trend.Kenan': return 'entertainment'",
 "        if str(_x) == 'trend.Haiti': return 'world'  # 2301Z: Bukele military operation in Haiti\n        if str(_x) == 'trend.Ilhan Nur': return 'politics'  # 2301Z: DOJ warrant filing names Ilhan Omar as Ilhan Nur Said Elmi\n        if str(_x) == 'trend.Kenan': return 'entertainment'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names Haiti and Ilhan Nur (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN+"); quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (98 unread referenced first-hop, then 19 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names Kenan and Claude Duet"):
    lines[i]="            f'trend names Haiti and Ilhan Nur (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 97"):
    lines[i]="            f'two screening reads by id: 98 unread first-hop referenced, reply-parent and media-source posts (98 returned), then 19 unread second-hop and leftover posts (19 returned; 2108062331095908717, Not Found in earlier runs, not re-read); 9 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
