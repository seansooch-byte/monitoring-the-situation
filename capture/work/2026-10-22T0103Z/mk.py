s=open('build_capture.py').read()
TN=open('trend_note.txt').read().strip()
R=[
("Build capture/2026/10/22/0001Z.json","Build capture/2026/10/22/0103Z.json"),
("work/2026-10-22T0001Z'","work/2026-10-22T0103Z'"),
("RUN_ID = '2026-10-22T0001Z'","RUN_ID = '2026-10-22T0103Z'"),
("STARTED = '2026-10-22T00:01:00Z'","STARTED = '2026-10-22T01:03:00Z'"),
("OBS_AT = '2026-10-22T00:02:00Z'","OBS_AT = '2026-10-22T01:04:00Z'"),
("READS_BEFORE = 1000","READS_BEFORE = 979"),
("datetime(2026,10,22,0,4,tzinfo=timezone.utc).timestamp()  # 0001Z (","datetime(2026,10,22,1,5,tzinfo=timezone.utc).timestamp()  # 0103Z (0001Z used 00:04, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_you': 'quote_you.txt', 'quote_is': 'quote_is.txt',"),
("'repost_this': 'repost_this.txt',","'repost_my': 'repost_my.txt',"),
("'trend_giannis': 'trend_giannis.txt', 'trend_lamelo': 'trend_lamelo.txt', 'trend_anthonydavis': 'trend_anthonydavis.txt',","'trend_aewdynamite': 'trend_aewdynamite.txt', 'trend_survivor51': 'trend_survivor51.txt', 'trend_tyjerome': 'trend_tyjerome.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',","'trends_us': 'trends_us.txt',"),
("trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')","trends = parse_trends(raw['trends_us'], 'US')"),
("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))","sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-22T0001Z',[]))"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_you','quote'),('quote_is','quote'),('repost_my','repost'),"),
("('trend_giannis','trend.Giannis'),('trend_lamelo','trend.Lamelo'),('trend_anthonydavis','trend.Anthony Davis'),","('trend_aewdynamite','trend.#AEWDynamite'),('trend_survivor51','trend.#Survivor51'),('trend_tyjerome','trend.Ty Jerome'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0001Z.json') and '/22/' in _c: continue","if _c.endswith('0103Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T2301Z'","_last = '2026-10-22T0001Z'"),
("cut for the forty-first run","cut for the forty-second run"),
("cut for the forty-third run","cut for the forty-fourth run"),
("(this 00Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 493 long, so the 400 cap left out the 93 slowest-growing posts (the 70 of the fourth-hour tier and the 23 slowest still-gaining posts) and no cited post)",
 "(this 01Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 416 long, so the 400 cap left out the 16 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0001Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0103Z.json'"),
("Evening run (8:01 PM ET Oct 21 / 00:01 UTC Oct 22, the 00Z slot and the first run of the new UTC day;","Evening run (9:03 PM ET Oct 21 / 01:03 UTC Oct 22, the 01Z slot;"),
("the X day reset at 00:00 UTC, so no read went elsewhere in between)","0001Z ended at 979, so no read went elsewhere in between)"),
("parallel batches of up to 13,","parallel batches of up to 13,"),
("00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the fourth-hour tier; 493 ids, so the 400 cap left out the 93 slowest-growing posts (all 70 of the fourth-hour tier and the 23 slowest still-gaining posts) and no cited post; 4 reads); trends US+WW (2 reads); ",
 "01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 416 ids, so the 400 cap left out the 16 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); "),
("f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2301Z, next in rotation); '",
 "f'quote/repost words you/is + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0001Z, next in rotation); '"),
("Not read: news/money/science sensors,","Not read: culture/sports/online sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "you", "is" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Giannis','trend.Lamelo','trend.Anthony Davis'): return 'sports'  # 0001Z: NBA opening-week games",
 "        if str(_x) in ('trend.#AEWDynamite','trend.Ty Jerome'): return 'sports'  # 0103Z: AEW Dynamite (wrestling beat); Ty Jerome NBA opening week\n        if str(_x) == 'trend.#Survivor51': return 'entertainment'  # 0103Z: CBS Survivor season 51\n        if str(_x) in ('trend.Giannis','trend.Lamelo','trend.Anthony Davis'): return 'sports'  # 0001Z: NBA opening-week games"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names #AEWDynamite, #Survivor51 and \"Ty Jerome\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words you/is + my (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 18 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names Giannis, Lamelo"):
    lines[i]="            f'trend names #AEWDynamite, #Survivor51 and \"Ty Jerome\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (100 returned, plus a Not Found error for the expansion 2108062331095908717, Not Found in earlier runs), then 18 unread second-hop and leftover posts (18 returned; 2108062331095908717 not asked again); 4 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
