s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0458Z: "Bears", "Patriots" and "Maye" (all the Patriots at Bears Thursday night game; "Bears" and "Patriots" not read before as names, "Drake Maye" read in 0303Z); "Caleb", "Ben Johnson", "Jaylon Johnson" and "AJ Brown" are the same game (read in 0303Z to 0458Z), "Jokic" and "Shai" are Nuggets at Thunder (read in 0458Z), and "Cavs" is Cavaliers v 76ers (read in 0205Z)'
R=[
("Build capture/2026/10/23/0458Z.json","Build capture/2026/10/23/0606Z.json"),
("work/2026-10-23T0458Z'","work/2026-10-23T0606Z'"),
("RUN_ID = '2026-10-23T0458Z'","RUN_ID = '2026-10-23T0606Z'"),
("STARTED = '2026-10-23T04:58:00Z'","STARTED = '2026-10-23T06:06:00Z'"),
("OBS_AT = '2026-10-23T04:58:00Z'","OBS_AT = '2026-10-23T06:06:00Z'"),
("READS_BEFORE = 899","READS_BEFORE = 879"),
("datetime(2026,10,23,5,1,tzinfo=timezone.utc).timestamp()  # 0458Z (","datetime(2026,10,23,6,9,tzinfo=timezone.utc).timestamp()  # 0606Z (0458Z used 05:01, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_jokic': 'trend_jokic.txt', 'trend_shai': 'trend_shai.txt', 'trend_jaylon': 'trend_jaylon.txt',","'trend_bears': 'trend_bears.txt', 'trend_patriots': 'trend_patriots.txt', 'trend_maye': 'trend_maye.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_jokic','trend.Jokic'),('trend_shai','trend.Shai'),('trend_jaylon','trend.Jaylon Johnson'),","('trend_bears','trend.Bears'),('trend_patriots','trend.Patriots'),('trend_maye','trend.Maye'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0458Z.json') and '/23/' in _c: continue","if _c.endswith('0606Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-23T0403Z'","_last = '2026-10-23T0458Z'"),
('\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Jokic','trend.Shai','trend.Jaylon Johnson'): return 'sports'  # 0458Z",
 "        if str(_x) in ('trend.Bears','trend.Patriots','trend.Maye'): return 'sports'  # 0606Z: Patriots at Bears TNF\n        if str(_x) in ('trend.Jokic','trend.Shai','trend.Jaylon Johnson'): return 'sports'  # 0458Z"),
("but cut for the seventieth run","but cut for the seventy-first run"),
("cut for the seventy-second run (kept","cut for the seventy-third run (kept"),
("although the 12:00-05:00 UTC band allows up to 42","in the 06:00-11:00 UTC band, up to 20"),
("(this 03Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 518 long, so the 400 cap left out the 106 slowest-growing still-gaining posts and the 12 last six-hour posts in order, and no cited post)",
 "(this 06Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 512 long, so the 400 cap left out the 110 slowest-growing still-gaining posts and the 2 last six-hour posts in order, and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0458Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0606Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Bears\", \"Patriots\" and \"Maye\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words what/the + this (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 42 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Night run (12:58 AM ET"):
    lines[i]="            f'Night run (2:06 AM ET Oct 23 / 06:06 UTC Oct 23, the 06Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0458Z ended at 879, so no read went elsewhere in between), parallel batches of up to 10, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 512 ids, so the 400 cap left out 112 posts in order (the 2 last six-hour posts and 110 slowest-growing still-gaining) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Jokic\""):
    lines[i]="            f'trend names \"Bears\", \"Patriots\" and \"Maye\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[i]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0458Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the seventy-third run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the seventy-first run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 42 more (2113143833588613393, left out in 0002Z as minor bait, was not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
