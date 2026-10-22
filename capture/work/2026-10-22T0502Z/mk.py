s=open('build_capture.py').read()
TN=open('trend_note.txt').read().strip()
R=[
("Build capture/2026/10/22/0408Z.json","Build capture/2026/10/22/0502Z.json"),
("work/2026-10-22T0408Z'","work/2026-10-22T0502Z'"),
("RUN_ID = '2026-10-22T0408Z'","RUN_ID = '2026-10-22T0502Z'"),
("STARTED = '2026-10-22T04:08:00Z'","STARTED = '2026-10-22T05:02:00Z'"),
("OBS_AT = '2026-10-22T04:08:00Z'","OBS_AT = '2026-10-22T05:02:00Z'"),
("READS_BEFORE = 919","READS_BEFORE = 899"),
("datetime(2026,10,22,4,9,tzinfo=timezone.utc).timestamp()  # 0408Z (","datetime(2026,10,22,5,4,tzinfo=timezone.utc).timestamp()  # 0502Z (0408Z used 04:09, "),
("'quote_the': 'quote_the.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_luka': 'trend_luka.txt', 'trend_yaxel': 'trend_yaxel.txt', 'trend_kessler': 'trend_kessler.txt',","'trend_steph': 'trend_steph.txt', 'trend_tyjerome': 'trend_tyjerome.txt', 'trend_giannis': 'trend_giannis.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_the','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_luka','trend.Luka'),('trend_yaxel','trend.Yaxel'),('trend_kessler','trend.Kessler'),","('trend_steph','trend.Steph'),('trend_tyjerome','trend.Ty Jerome'),('trend_giannis','trend.Giannis'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0408Z.json') and '/22/' in _c: continue","if _c.endswith('0502Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T0300Z'","_last = '2026-10-22T0408Z'"),
("cut for the forty-fifth run","cut for the forty-sixth run"),
("cut for the forty-seventh run","cut for the forty-eighth run"),
("(this 04Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 478 long, so the 400 cap left out the 78 slowest-growing posts (all 72 fourth-hour and the 6 slowest still-gaining) and no cited post)",
 "(this 05Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 429 long, so the 400 cap left out the 29 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0408Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0502Z.json'"),
("Night run (12:08 AM ET / 04:08 UTC Oct 22, the 04Z slot;","Night run (1:02 AM ET / 05:02 UTC Oct 22, the 05Z slot;"),
("0300Z ended at 919, so no read went elsewhere in between)","0408Z ended at 899, so no read went elsewhere in between)"),
("04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 478 ids, so the 400 cap left out the 78 slowest-growing posts (all 72 fourth-hour and the 6 slowest still-gaining) and no cited post; 4 reads); ",
 "05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 429 ids, so the 400 cap left out the 29 slowest-growing still-gaining posts and no cited post; 4 reads); "),
("f'quote/repost words the/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0300Z, next in rotation); '",
 "f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0408Z, next in rotation); '"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
('\'2 quote pages + 1 repost page (budget), common words "the", "is" and "you", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Luka','trend.Yaxel','trend.Kessler'): return 'sports'  # 0408Z",
 "        if str(_x) in ('trend.Steph','trend.Ty Jerome','trend.Giannis'): return 'sports'  # 0502Z: NBA opening week (Warriors at Lakers; Ty Jerome; Giannis/Bucks)\n        if str(_x) in ('trend.Luka','trend.Yaxel','trend.Kessler'): return 'sports'  # 0408Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Steph\", \"Ty Jerome\" and \"Giannis\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 32 second-hop and leftover); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  if st.startswith("f'trend names \"Luka\""):
    lines[i]="            f'trend names \"Steph\", \"Ty Jerome\" and \"Giannis\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  if st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread first-hop referenced, reply-parent and media-source posts (100 returned, plus a Not Found error for the expansion 2108062331095908717, Not Found in earlier runs), then 32 unread second-hop and leftover posts (32 returned; 2108062331095908717 not asked again); 11 third-hop posts left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
