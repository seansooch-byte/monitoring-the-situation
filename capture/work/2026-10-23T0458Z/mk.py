s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0403Z: "Jokic" (Nikola Jokic of the Nuggets), "Shai" (Shai Gilgeous-Alexander of the Thunder) and "Jaylon Johnson" (the Bears cornerback in the Patriots at Bears Thursday night game, last read in 0205Z); "Bears", "Caleb", "Ben Johnson", "AJ Brown", "Drake Maye" and "Patriots" are the same game (read in 0303Z or 0403Z), and "Cavs" is Cavaliers v 76ers (read in 0205Z)'
R=[
("Build capture/2026/10/23/0403Z.json","Build capture/2026/10/23/0458Z.json"),
("work/2026-10-23T0403Z'","work/2026-10-23T0458Z'"),
("RUN_ID = '2026-10-23T0403Z'","RUN_ID = '2026-10-23T0458Z'"),
("STARTED = '2026-10-23T04:03:00Z'","STARTED = '2026-10-23T04:58:00Z'"),
("OBS_AT = '2026-10-23T04:03:00Z'","OBS_AT = '2026-10-23T04:58:00Z'"),
("READS_BEFORE = 919","READS_BEFORE = 899"),
("datetime(2026,10,23,4,6,tzinfo=timezone.utc).timestamp()  # 0403Z (","datetime(2026,10,23,5,1,tzinfo=timezone.utc).timestamp()  # 0458Z (0403Z used 04:06, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_benjohnson': 'trend_benjohnson.txt', 'trend_caleb': 'trend_caleb.txt', 'trend_cairo': 'trend_cairo.txt',","'trend_jokic': 'trend_jokic.txt', 'trend_shai': 'trend_shai.txt', 'trend_jaylon': 'trend_jaylon.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_benjohnson','trend.Ben Johnson'),('trend_caleb','trend.Caleb'),('trend_cairo','trend.Cairo Santos'),","('trend_jokic','trend.Jokic'),('trend_shai','trend.Shai'),('trend_jaylon','trend.Jaylon Johnson'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0403Z.json') and '/23/' in _c: continue","if _c.endswith('0458Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-23T0303Z'","_last = '2026-10-23T0403Z'"),
('\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Ben Johnson','trend.Caleb','trend.Cairo Santos'): return 'sports'  # 0403Z",
 "        if str(_x) in ('trend.Jokic','trend.Shai','trend.Jaylon Johnson'): return 'sports'  # 0458Z: NBA (Nuggets, Thunder) and Patriots at Bears TNF\n        if str(_x) in ('trend.Ben Johnson','trend.Caleb','trend.Cairo Santos'): return 'sports'  # 0403Z"),
("but cut for the sixty-ninth run","but cut for the seventieth run"),
("cut for the seventy-first run (kept","cut for the seventy-second run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0403Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0458Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Jokic\", \"Shai\" and \"Jaylon Johnson\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 28 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Night run (12:03 AM ET"):
    lines[i]="            f'Night run (12:58 AM ET Oct 23 / 04:58 UTC Oct 23, the 05Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0403Z ended at 899, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 517 ids, so the 400 cap left out 117 posts in order (the 18 last six-hour posts and 99 slowest-growing still-gaining) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Ben Johnson\""):
    lines[i]="            f'trend names \"Jokic\", \"Shai\" and \"Jaylon Johnson\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words you/and"):
    lines[i]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0403Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the seventy-second run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the seventieth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 28 more; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
