s=open('build_capture.py').read()
TN=open('trend_note.txt').read().strip()
R=[
("Build capture/2026/10/22/0300Z.json","Build capture/2026/10/22/0408Z.json"),
("work/2026-10-22T0300Z'","work/2026-10-22T0408Z'"),
("RUN_ID = '2026-10-22T0300Z'","RUN_ID = '2026-10-22T0408Z'"),
("STARTED = '2026-10-22T03:00:00Z'","STARTED = '2026-10-22T04:08:00Z'"),
("OBS_AT = '2026-10-22T03:00:00Z'","OBS_AT = '2026-10-22T04:08:00Z'"),
("READS_BEFORE = 939","READS_BEFORE = 919"),
("datetime(2026,10,22,3,1,tzinfo=timezone.utc).timestamp()  # 0300Z (","datetime(2026,10,22,4,9,tzinfo=timezone.utc).timestamp()  # 0408Z (0300Z used 03:01, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_the': 'quote_the.txt', 'quote_is': 'quote_is.txt',"),
("'repost_this': 'repost_this.txt',","'repost_you': 'repost_you.txt',"),
("'trend_blazers': 'trend_blazers.txt', 'trend_suns': 'trend_suns.txt', 'trend_angelreese': 'trend_angelreese.txt',","'trend_luka': 'trend_luka.txt', 'trend_yaxel': 'trend_yaxel.txt', 'trend_kessler': 'trend_kessler.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_this','repost'),","('quote_the','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_blazers','trend.Blazers'),('trend_suns','trend.Suns'),('trend_angelreese','trend.Angel Reese'),","('trend_luka','trend.Luka'),('trend_yaxel','trend.Yaxel'),('trend_kessler','trend.Kessler'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0300Z.json') and '/22/' in _c: continue","if _c.endswith('0408Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T0206Z'","_last = '2026-10-22T0300Z'"),
("cut for the forty-fourth run","cut for the forty-fifth run"),
("cut for the forty-sixth run","cut for the forty-seventh run"),
("(this 03Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 412 long, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post)",
 "(this 04Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 478 long, so the 400 cap left out the 78 slowest-growing posts (all 72 fourth-hour and the 6 slowest still-gaining) and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0300Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0408Z.json'"),
("Evening run (11:00 PM ET Oct 21 / 03:00 UTC Oct 22, the 03Z slot;","Night run (12:08 AM ET / 04:08 UTC Oct 22, the 04Z slot;"),
("0206Z ended at 939, so no read went elsewhere in between)","0300Z ended at 919, so no read went elsewhere in between)"),
("03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 412 ids, so the 400 cap left out the 12 slowest-growing still-gaining posts and no cited post; 4 reads); ",
 "04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 478 ids, so the 400 cap left out the 78 slowest-growing posts (all 72 fourth-hour and the 6 slowest still-gaining) and no cited post; 4 reads); "),
("f'quote/repost words just/what + this (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0206Z, next in rotation); '",
 "f'quote/repost words the/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0300Z, next in rotation); '"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "just", "what" and "this", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "the", "is" and "you", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Blazers','trend.Suns','trend.Angel Reese'): return 'sports'  # 0300Z",
 "        if str(_x) in ('trend.Luka','trend.Yaxel','trend.Kessler'): return 'sports'  # 0408Z: Warriors at Lakers (NBA opening week)\n        if str(_x) in ('trend.Blazers','trend.Suns','trend.Angel Reese'): return 'sports'  # 0300Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Luka\", \"Yaxel\" and \"Kessler\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words the/is + you (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 27 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names \"Blazers\""):
    lines[i]="            f'trend names \"Luka\", \"Yaxel\" and \"Kessler\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (100 returned, plus a Not Found error for the expansion 2108062331095908717, Not Found in earlier runs), then 27 unread second-hop and leftover posts (27 returned; 2108062331095908717 not asked again); 8 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
