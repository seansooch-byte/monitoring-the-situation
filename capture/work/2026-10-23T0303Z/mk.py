s=open('build_capture.py').read()
TN='three of the top-ten US names, none with posts attached in 0205Z: "AJ Brown" (new to the top ten; AJ Brown news, likely the same NFL night as the Patriots at Bears game), "Sixers" (Cavaliers v 76ers, the same event as "Cavs", "76ers", "Harden" and "Maxey") and "Drake Maye" (the Patriots at Bears Thursday night game, the same event as "Jaylon Johnson", "Bears", "Patriots", "Luther Burden", "Ben Johnson", "Caleb", "Cairo Santos", "Rome Odunze", "Al Michaels" and "Pats"); the other top-ten names are the same two games and "#VERZUZ" (attached in 0205Z)'
R=[
("Build capture/2026/10/23/0205Z.json","Build capture/2026/10/23/0303Z.json"),
("work/2026-10-23T0205Z'","work/2026-10-23T0303Z'"),
("RUN_ID = '2026-10-23T0205Z'","RUN_ID = '2026-10-23T0303Z'"),
("STARTED = '2026-10-23T02:05:00Z'","STARTED = '2026-10-23T03:03:00Z'"),
("OBS_AT = '2026-10-23T02:05:00Z'","OBS_AT = '2026-10-23T03:03:00Z'"),
("READS_BEFORE = 959","READS_BEFORE = 939"),
("datetime(2026,10,23,2,7,tzinfo=timezone.utc).timestamp()  # 0205Z (","datetime(2026,10,23,3,5,tzinfo=timezone.utc).timestamp()  # 0303Z (0205Z used 02:07, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_jaylon': 'trend_jaylon.txt', 'trend_cavs': 'trend_cavs.txt', 'trend_verzuz': 'trend_verzuz.txt',","'trend_ajbrown': 'trend_ajbrown.txt', 'trend_sixers': 'trend_sixers.txt', 'trend_maye': 'trend_maye.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_jaylon','trend.Jaylon Johnson'),('trend_cavs','trend.Cavs'),('trend_verzuz','trend.#VERZUZ'),","('trend_ajbrown','trend.AJ Brown'),('trend_sixers','trend.Sixers'),('trend_maye','trend.Drake Maye'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0205Z.json') and '/23/' in _c: continue","if _c.endswith('0303Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-23T0059Z'","_last = '2026-10-23T0205Z'"),
('\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Jaylon Johnson',): return 'sports'  # 0205Z: Patriots at Bears TNF",
 "        if str(_x) in ('trend.Drake Maye','trend.Sixers'): return 'sports'  # 0303Z: Patriots at Bears TNF; Cavaliers v 76ers\n        if str(_x) in ('trend.Jaylon Johnson',): return 'sports'  # 0205Z: Patriots at Bears TNF"),
("but cut for the sixty-seventh run","but cut for the sixty-eighth run"),
("cut for the sixty-ninth run (kept","cut for the seventieth run (kept"),
("(this 02Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 510 long, so the 400 cap left out the 103 slowest-growing still-gaining posts and the 7 last six-hour posts in order, and no cited post)",
 "(this 03Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 518 long, so the 400 cap left out the 106 slowest-growing still-gaining posts and the 12 last six-hour posts in order, and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0205Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0303Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"AJ Brown\", \"Sixers\" and \"Drake Maye\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 10 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Evening run (10:05 PM ET"):
    lines[i]="            f'Night run (11:03 PM ET Oct 22 / 03:03 UTC Oct 23, the 03Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0205Z ended at 939, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 518 ids, so the 400 cap left out 106 slowest-growing still-gaining posts and the 12 last six-hour posts in order, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Jaylon Johnson\""):
    lines[i]="            f'trend names \"AJ Brown\", \"Sixers\" and \"Drake Maye\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[i]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0205Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the seventieth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-eighth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 10 more; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
