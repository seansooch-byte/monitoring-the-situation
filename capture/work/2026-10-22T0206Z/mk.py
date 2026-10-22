s=open('build_capture.py').read()
TN=open('trend_note.txt').read().strip()
R=[
("Build capture/2026/10/22/0103Z.json","Build capture/2026/10/22/0206Z.json"),
("work/2026-10-22T0103Z'","work/2026-10-22T0206Z'"),
("RUN_ID = '2026-10-22T0103Z'","RUN_ID = '2026-10-22T0206Z'"),
("STARTED = '2026-10-22T01:03:00Z'","STARTED = '2026-10-22T02:06:00Z'"),
("OBS_AT = '2026-10-22T01:04:00Z'","OBS_AT = '2026-10-22T02:08:00Z'"),
("READS_BEFORE = 979","READS_BEFORE = 959"),
("datetime(2026,10,22,1,5,tzinfo=timezone.utc).timestamp()  # 0103Z (","datetime(2026,10,22,2,9,tzinfo=timezone.utc).timestamp()  # 0206Z (0103Z used 01:05, "),
("'quote_you': 'quote_you.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_it': 'quote_it.txt',"),
("'repost_my': 'repost_my.txt',","'repost_that': 'repost_that.txt',"),
("'trend_aewdynamite': 'trend_aewdynamite.txt', 'trend_survivor51': 'trend_survivor51.txt', 'trend_tyjerome': 'trend_tyjerome.txt',","'trend_anthonyedwards': 'trend_anthonyedwards.txt', 'trend_mavs': 'trend_mavs.txt', 'trend_kilby': 'trend_kilby.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_you','quote'),('quote_is','quote'),('repost_my','repost'),","('quote_and','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_aewdynamite','trend.#AEWDynamite'),('trend_survivor51','trend.#Survivor51'),('trend_tyjerome','trend.Ty Jerome'),","('trend_anthonyedwards','trend.Anthony Edwards'),('trend_mavs','trend.Mavs'),('trend_kilby','trend.Kilby'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0103Z.json') and '/22/' in _c: continue","if _c.endswith('0206Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T0001Z'","_last = '2026-10-22T0103Z'"),
("cut for the forty-second run","cut for the forty-third run"),
("cut for the forty-fourth run","cut for the forty-fifth run"),
("(this 01Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 416 long, so the 400 cap left out the 16 slowest-growing still-gaining posts and no cited post)",
 "(this 02Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 414 long, so the 400 cap left out the 14 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0103Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0206Z.json'"),
("Evening run (9:03 PM ET Oct 21 / 01:03 UTC Oct 22, the 01Z slot;","Evening run (10:06 PM ET Oct 21 / 02:06 UTC Oct 22, the 02Z slot;"),
("0001Z ended at 979, so no read went elsewhere in between)","0103Z ended at 959, so no read went elsewhere in between)"),
("01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 416 ids, so the 400 cap left out the 16 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); ",
 "02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 414 ids, so the 400 cap left out the 14 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); "),
("f'quote/repost words you/is + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0001Z, next in rotation); '",
 "f'quote/repost words and/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0103Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "you", "is" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "and", "it" and "that", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.#AEWDynamite','trend.Ty Jerome'): return 'sports'  # 0103Z",
 "        if str(_x) in ('trend.Anthony Edwards','trend.Mavs'): return 'sports'  # 0206Z: NBA opening week (Timberwolves v Heat; Mavericks at Rockets)\n        if str(_x) == 'trend.Kilby': return 'entertainment'  # 0206Z: Survivor 51 contestant\n        if str(_x) in ('trend.#AEWDynamite','trend.Ty Jerome'): return 'sports'  # 0103Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Anthony Edwards\", \"Mavs\" and \"Kilby\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words and/it + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 41 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names #AEWDynamite"):
    lines[i]="            f'trend names \"Anthony Edwards\", \"Mavs\" and \"Kilby\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (100 returned, plus a Not Found error for the expansion 2108062331095908717, Not Found in earlier runs), then 41 unread second-hop and leftover posts (41 returned; 2108062331095908717 not asked again); 10 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
