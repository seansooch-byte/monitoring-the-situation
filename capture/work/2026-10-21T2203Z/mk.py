s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/2107Z.json","Build capture/2026/10/21/2203Z.json"),
("work/2026-10-21T2107Z'","work/2026-10-21T2203Z'"),
("RUN_ID = '2026-10-21T2107Z'","RUN_ID = '2026-10-21T2203Z'"),
("STARTED = '2026-10-21T21:07:00Z'","STARTED = '2026-10-21T22:03:00Z'"),
("OBS_AT = '2026-10-21T21:07:00Z'","OBS_AT = '2026-10-21T22:03:00Z'"),
("READS_BEFORE = 575","READS_BEFORE = 557"),
("datetime(2026,10,21,21,10,tzinfo=timezone.utc).timestamp()  # 2107Z (","datetime(2026,10,21,22,6,tzinfo=timezone.utc).timestamp()  # 2203Z (2107Z used 21:10, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_diomande': 'trend_diomande.txt',","'trend_kenan': 'trend_kenan.txt', 'trend_claudeduet': 'trend_claudeduet.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_diomande','trend.Diomande'),","('trend_kenan','trend.Kenan'),('trend_claudeduet','trend.Claude Duet'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2107Z.json') and '/21/' in _c: continue","if _c.endswith('2203Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T2008Z'","_last = '2026-10-21T2107Z'"),
("cut for the thirty-eighth run","cut for the thirty-ninth run"),
("cut for the fortieth run","cut for the forty-first run"),
("(this 21Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 438 long, so the 400 cap left out the 38 slowest-growing still-gaining posts and no cited post)",
 "(this 22Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 435 long, so the 400 cap left out the 35 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/2203Z.json'"),
("Evening run (5:07 PM ET Oct 21 / 21:07 UTC Oct 21, the 21Z slot;","Evening run (6:03 PM ET Oct 21 / 22:03 UTC Oct 21, the 22Z slot;"),
("2008Z ended at 575, so no read went elsewhere in between)","2107Z ended at 557, so no read went elsewhere in between)"),
("21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 438 ids, so the 400 cap left out the 38 slowest-growing still-gaining posts and no cited post; 4 reads)",
 "22Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 435 ids, so the 400 cap left out the 35 slowest-growing still-gaining posts and no cited post; 4 reads)"),
("f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2008Z, next in rotation); '",
 "f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2107Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) == 'trend.Diomande': return 'sports'  # 2107Z",
 "        if str(_x) == 'trend.Kenan': return 'entertainment'  # 2203Z: Kenan Thompson on the Shane Gillis SNL monologue\n        if str(_x) == 'trend.Claude Duet': return 'ai'  # 2203Z: Anthropic Claude Duet research preview\n        if str(_x) == 'trend.Diomande': return 'sports'  # 2107Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
TN=open('trend_note.txt').read().strip()
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names Kenan and Claude Duet (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN+"); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (97 unread referenced first-hop, then 23 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend name Diomande"):
    lines[i]="            f'trend names Kenan and Claude Duet (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 97 unread first-hop referenced, reply-parent and media-source posts (96 returned; 2108062331095908717 Not Found again), then 23 unread second-hop and leftover posts (23 returned); 7 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
