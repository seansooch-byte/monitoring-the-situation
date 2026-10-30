s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0303Z: "Ben Johnson" (the Bears head coach in the Patriots at Bears Thursday night game), "Caleb" (Bears quarterback Caleb Williams in the same game) and "Cairo Santos" (the Bears kicker in the same game); "Bears", "Jaylon Johnson", "Patriots", "Drake Maye", "AJ Brown" and "Pats" are the same game, and "Cavs" and "Sixers" are Cavaliers v 76ers (attached in 0303Z or read in 0205Z)'
R=[
("Build capture/2026/10/23/0303Z.json","Build capture/2026/10/23/0403Z.json"),
("work/2026-10-23T0303Z'","work/2026-10-23T0403Z'"),
("RUN_ID = '2026-10-23T0303Z'","RUN_ID = '2026-10-23T0403Z'"),
("STARTED = '2026-10-23T03:03:00Z'","STARTED = '2026-10-23T04:03:00Z'"),
("OBS_AT = '2026-10-23T03:03:00Z'","OBS_AT = '2026-10-23T04:03:00Z'"),
("READS_BEFORE = 939","READS_BEFORE = 919"),
("datetime(2026,10,23,3,5,tzinfo=timezone.utc).timestamp()  # 0303Z (","datetime(2026,10,23,4,6,tzinfo=timezone.utc).timestamp()  # 0403Z (0303Z used 03:05, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_ajbrown': 'trend_ajbrown.txt', 'trend_sixers': 'trend_sixers.txt', 'trend_maye': 'trend_maye.txt',","'trend_benjohnson': 'trend_benjohnson.txt', 'trend_caleb': 'trend_caleb.txt', 'trend_cairo': 'trend_cairo.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_ajbrown','trend.AJ Brown'),('trend_sixers','trend.Sixers'),('trend_maye','trend.Drake Maye'),","('trend_benjohnson','trend.Ben Johnson'),('trend_caleb','trend.Caleb'),('trend_cairo','trend.Cairo Santos'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0303Z.json') and '/23/' in _c: continue","if _c.endswith('0403Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-23T0205Z'","_last = '2026-10-23T0303Z'"),
('\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Drake Maye','trend.Sixers'): return 'sports'  # 0303Z",
 "        if str(_x) in ('trend.Ben Johnson','trend.Caleb','trend.Cairo Santos'): return 'sports'  # 0403Z: Patriots at Bears TNF\n        if str(_x) in ('trend.Drake Maye','trend.Sixers'): return 'sports'  # 0303Z"),
("but cut for the sixty-eighth run","but cut for the sixty-ninth run"),
("cut for the seventieth run (kept","cut for the seventy-first run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0303Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0403Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Ben Johnson\", \"Caleb\" and \"Cairo Santos\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 17 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Night run (11:03 PM ET"):
    lines[i]="            f'Night run (12:03 AM ET Oct 23 / 04:03 UTC Oct 23, the 04Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0303Z ended at 919, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 540 ids, so the 400 cap left out 140 posts in order (the 6 last six-hour posts, 107 slowest-growing still-gaining and 27 fourth-hour) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"AJ Brown\""):
    lines[i]="            f'trend names \"Ben Johnson\", \"Caleb\" and \"Cairo Santos\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[i]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0303Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the seventy-first run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-ninth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 17 more; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
