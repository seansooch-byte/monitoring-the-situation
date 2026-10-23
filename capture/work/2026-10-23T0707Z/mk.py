s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0606Z: "Ethan Klein", "Dear JT" and "Jokic" ("Ethan Klein" and "Dear JT" not read before as names; "Hila" at 11 is the same story as "Ethan Klein"; "Jokic" is Nuggets at Thunder, read in 0458Z); "Bears", "Caleb", "Ben Johnson", "Maye", "Jaylon Johnson", "Patriots" and "AJ Brown" are Patriots at Bears TNF (read in 0303Z to 0606Z), and "Shai" is Nuggets at Thunder (read in 0458Z)'
R=[
("Build capture/2026/10/23/0606Z.json","Build capture/2026/10/23/0707Z.json"),
("work/2026-10-23T0606Z'","work/2026-10-23T0707Z'"),
("RUN_ID = '2026-10-23T0606Z'","RUN_ID = '2026-10-23T0707Z'"),
("STARTED = '2026-10-23T06:06:00Z'","STARTED = '2026-10-23T07:07:00Z'"),
("OBS_AT = '2026-10-23T06:06:00Z'","OBS_AT = '2026-10-23T07:07:00Z'"),
("READS_BEFORE = 879","READS_BEFORE = 859"),
("datetime(2026,10,23,6,9,tzinfo=timezone.utc).timestamp()  # 0606Z (","datetime(2026,10,23,7,11,tzinfo=timezone.utc).timestamp()  # 0707Z (0606Z used 06:09, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_bears': 'trend_bears.txt', 'trend_patriots': 'trend_patriots.txt', 'trend_maye': 'trend_maye.txt',","'trend_ethan': 'trend_ethan.txt', 'trend_dearjt': 'trend_dearjt.txt', 'trend_jokic': 'trend_jokic.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_bears','trend.Bears'),('trend_patriots','trend.Patriots'),('trend_maye','trend.Maye'),","('trend_ethan','trend.Ethan Klein'),('trend_dearjt','trend.Dear JT'),('trend_jokic','trend.Jokic'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0606Z.json') and '/23/' in _c: continue","if _c.endswith('0707Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T0458Z'","_last = '2026-10-23T0606Z'"),
('\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Bears','trend.Patriots','trend.Maye'): return 'sports'  # 0606Z",
 "        if str(_x) == 'trend.Ethan Klein': return 'internet'  # 0707Z: h3h3 podcaster\n        if str(_x) == 'trend.Dear JT': return 'music'  # 0707Z\n        if str(_x) in ('trend.Bears','trend.Patriots','trend.Maye'): return 'sports'  # 0606Z"),
("but cut for the seventy-first run","but cut for the seventy-second run"),
("cut for the seventy-third run (kept","cut for the seventy-fourth run (kept"),
("(this 06Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 512 long, so the 400 cap left out the 110 slowest-growing still-gaining posts and the 2 last six-hour posts in order, and no cited post)",
 "(this 07Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 513 long, so the 400 cap left out the 110 slowest-growing still-gaining posts and the 3 last six-hour posts in order, and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0606Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0707Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Ethan Klein\", \"Dear JT\" and \"Jokic\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words is/you + and (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 15 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Night run (2:06 AM ET"):
    lines[i]="            f'Morning run (3:07 AM ET Oct 23 / 07:07 UTC Oct 23, the 07Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0606Z ended at 859, so no read went elsewhere in between), parallel batches of up to 10, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 513 ids, so the 400 cap left out 113 posts in order (the 3 last six-hour posts and 110 slowest-growing still-gaining) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Bears\""):
    lines[i]="            f'trend names \"Ethan Klein\", \"Dear JT\" and \"Jokic\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[i]="            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0606Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the seventy-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the seventy-second run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 15 more (2113143833588613393, left out in 0002Z as minor bait, and 1746547721153241250, left out in 0606Z as likely paid, were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
