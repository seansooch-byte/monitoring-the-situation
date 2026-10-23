s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0707Z: "GMMTV RESPECT OUR CULTURE", "Ben Johnson" and "Jaylon Johnson" ("GMMTV RESPECT OUR CULTURE" not read before as a name, the Myanmar fan campaign about GMMTV; "Ben Johnson" last read in 0403Z and "Jaylon Johnson" in 0458Z); "Bears", "Ben Johnson", "Maye" and "Jaylon Johnson" are all Patriots at Bears TNF ("Bears" and "Maye" read in 0606Z), and "Ethan Klein", "Hila", "Caleb", "Jokic" and "Dear JT" had posts attached in 0707Z'
WATCH_NOTE="(this 08Z run is a fourth hour, so the 6-to-24-hour posts that gained under 2 percent were added after the still-gaining tier; with every pulse- and story-cited post placed right after the watch.json ids the list was 551 long, so the 400 cap left out the 16 last six-hour posts, the 104 slowest-growing still-gaining posts and 31 of the 36 fourth-hour posts in order, and no cited post)"
R=[
("Build capture/2026/10/23/0707Z.json","Build capture/2026/10/23/0801Z.json"),
("work/2026-10-23T0707Z'","work/2026-10-23T0801Z'"),
("RUN_ID = '2026-10-23T0707Z'","RUN_ID = '2026-10-23T0801Z'"),
("STARTED = '2026-10-23T07:07:00Z'","STARTED = '2026-10-23T08:01:00Z'"),
("OBS_AT = '2026-10-23T07:07:00Z'","OBS_AT = '2026-10-23T08:01:00Z'"),
("READS_BEFORE = 859","READS_BEFORE = 839"),
("datetime(2026,10,23,7,11,tzinfo=timezone.utc).timestamp()  # 0707Z (","datetime(2026,10,23,8,3,tzinfo=timezone.utc).timestamp()  # 0801Z (0707Z used 07:11, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_ethan': 'trend_ethan.txt', 'trend_dearjt': 'trend_dearjt.txt', 'trend_jokic': 'trend_jokic.txt',","'trend_gmmtv': 'trend_gmmtv.txt', 'trend_benjohnson': 'trend_benjohnson.txt', 'trend_jaylon': 'trend_jaylon.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_ethan','trend.Ethan Klein'),('trend_dearjt','trend.Dear JT'),('trend_jokic','trend.Jokic'),","('trend_gmmtv','trend.GMMTV RESPECT OUR CULTURE'),('trend_benjohnson','trend.Ben Johnson'),('trend_jaylon','trend.Jaylon Johnson'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0707Z.json') and '/23/' in _c: continue","if _c.endswith('0801Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T0606Z'","_last = '2026-10-23T0707Z'"),
('\'2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) == 'trend.Ethan Klein': return 'internet'  # 0707Z: h3h3 podcaster",
 "        if str(_x) == 'trend.GMMTV RESPECT OUR CULTURE': return 'entertainment'  # 0801Z: Myanmar fan campaign about GMMTV\n        if str(_x) == 'trend.Ethan Klein': return 'internet'  # 0707Z: h3h3 podcaster"),
("but cut for the seventy-second run","but cut for the seventy-third run"),
("cut for the seventy-fourth run (kept","cut for the seventy-fifth run (kept"),
("(this 07Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 513 long, so the 400 cap left out the 110 slowest-growing still-gaining posts and the 3 last six-hour posts in order, and no cited post)", WATCH_NOTE),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0707Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0801Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"GMMTV RESPECT OUR CULTURE\", \"Ben Johnson\" and \"Jaylon Johnson\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words my/it + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 24 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (3:07 AM ET"):
    lines[i]="            f'Morning run (4:01 AM ET Oct 23 / 08:01 UTC Oct 23, the 08Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0707Z ended at 839, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 551 ids, so the 400 cap left out 151 posts in order (the 16 last six-hour posts, 104 slowest-growing still-gaining and 31 fourth-hour) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Ethan Klein\""):
    lines[i]="            f'trend names \"GMMTV RESPECT OUR CULTURE\", \"Ben Johnson\" and \"Jaylon Johnson\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words is/you"):
    lines[i]="            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0707Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 24 more (2113143833588613393, left out in 0002Z as minor bait, and 1746547721153241250, left out in 0606Z as likely paid, were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
