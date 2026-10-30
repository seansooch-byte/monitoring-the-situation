s=open('build_capture.py').read()
TN=open('trend_note.txt').read().strip()
R=[
("Build capture/2026/10/22/0206Z.json","Build capture/2026/10/22/0300Z.json"),
("work/2026-10-22T0206Z'","work/2026-10-22T0300Z'"),
("RUN_ID = '2026-10-22T0206Z'","RUN_ID = '2026-10-22T0300Z'"),
("STARTED = '2026-10-22T02:06:00Z'","STARTED = '2026-10-22T03:00:00Z'"),
("OBS_AT = '2026-10-22T02:08:00Z'","OBS_AT = '2026-10-22T03:00:00Z'"),
("READS_BEFORE = 959","READS_BEFORE = 939"),
("datetime(2026,10,22,2,9,tzinfo=timezone.utc).timestamp()  # 0206Z (","datetime(2026,10,22,3,1,tzinfo=timezone.utc).timestamp()  # 0300Z (0206Z used 02:09, "),
("'quote_and': 'quote_and.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_this': 'repost_this.txt',"),
("'trend_anthonyedwards': 'trend_anthonyedwards.txt', 'trend_mavs': 'trend_mavs.txt', 'trend_kilby': 'trend_kilby.txt',","'trend_blazers': 'trend_blazers.txt', 'trend_suns': 'trend_suns.txt', 'trend_angelreese': 'trend_angelreese.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_and','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_this','repost'),"),
("('trend_anthonyedwards','trend.Anthony Edwards'),('trend_mavs','trend.Mavs'),('trend_kilby','trend.Kilby'),","('trend_blazers','trend.Blazers'),('trend_suns','trend.Suns'),('trend_angelreese','trend.Angel Reese'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0206Z.json') and '/22/' in _c: continue","if _c.endswith('0300Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T0103Z'","_last = '2026-10-22T0206Z'"),
("cut for the forty-third run","cut for the forty-fourth run"),
("cut for the forty-fifth run","cut for the forty-sixth run"),
("(this 02Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 414 long, so the 400 cap left out the 14 slowest-growing still-gaining posts and no cited post)",
 "(this 03Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 412 long, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0206Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0300Z.json'"),
("Evening run (10:06 PM ET Oct 21 / 02:06 UTC Oct 22, the 02Z slot;","Evening run (11:00 PM ET Oct 21 / 03:00 UTC Oct 22, the 03Z slot;"),
("0103Z ended at 959, so no read went elsewhere in between)","0206Z ended at 939, so no read went elsewhere in between)"),
("02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 414 ids, so the 400 cap left out the 14 slowest-growing still-gaining posts and no cited post; 4 reads); ",
 "03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 412 ids, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post; 4 reads); "),
("f'quote/repost words and/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0103Z, next in rotation); '",
 "f'quote/repost words just/what + this (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0206Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "and", "it" and "that", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "just", "what" and "this", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Anthony Edwards','trend.Mavs'): return 'sports'  # 0206Z",
 "        if str(_x) in ('trend.Blazers','trend.Suns','trend.Angel Reese'): return 'sports'  # 0300Z: Suns at Trail Blazers (NBA opening week); Angel Reese WNBA Finals\n        if str(_x) in ('trend.Anthony Edwards','trend.Mavs'): return 'sports'  # 0206Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Blazers\", \"Suns\" and \"Angel Reese\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words just/what + this (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 36 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names \"Anthony Edwards\""):
    lines[i]="            f'trend names \"Blazers\", \"Suns\" and \"Angel Reese\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (99 returned, plus a Not Found error for 1696895709092454422 and Not Found errors for the expansions 2112954732289700225 and 2108062331095908717, the last Not Found in earlier runs), then 36 unread second-hop and leftover posts (36 returned; the three Not Found ids not asked again); 4 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
