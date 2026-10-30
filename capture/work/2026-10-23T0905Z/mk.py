s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0801Z: "Hila", "Caleb" and "Patriots" ("Ethan Klein", "Jokic" and "Dear JT" last read in 0707Z, "Maye" in 0606Z; "Bears", "Maye", "Patriots", "Caleb" and "Ben Johnson" are all Patriots at Bears TNF), and "Bears", "GMMTV RESPECT OUR CULTURE" and "Ben Johnson" had posts attached in 0801Z'
OLD_WN="(this 08Z run is a fourth hour, so the 6-to-24-hour posts that gained under 2 percent were added after the still-gaining tier; with every pulse- and story-cited post placed right after the watch.json ids the list was 551 long, so the 400 cap left out the 16 last six-hour posts, the 104 slowest-growing still-gaining posts and 31 of the 36 fourth-hour posts in order, and no cited post)"
WATCH_NOTE="(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 504 long, so the 400 cap left out the 104 slowest-growing still-gaining posts in order, and no cited post)"
R=[
("Build capture/2026/10/23/0801Z.json","Build capture/2026/10/23/0905Z.json"),
("work/2026-10-23T0801Z'","work/2026-10-23T0905Z'"),
("RUN_ID = '2026-10-23T0801Z'","RUN_ID = '2026-10-23T0905Z'"),
("STARTED = '2026-10-23T08:01:00Z'","STARTED = '2026-10-23T09:05:00Z'"),
("OBS_AT = '2026-10-23T08:01:00Z'","OBS_AT = '2026-10-23T09:05:00Z'"),
("READS_BEFORE = 839","READS_BEFORE = 819"),
("datetime(2026,10,23,8,3,tzinfo=timezone.utc).timestamp()  # 0801Z (","datetime(2026,10,23,9,7,tzinfo=timezone.utc).timestamp()  # 0905Z (0801Z used 08:03, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_gmmtv': 'trend_gmmtv.txt', 'trend_benjohnson': 'trend_benjohnson.txt', 'trend_jaylon': 'trend_jaylon.txt',","'trend_hila': 'trend_hila.txt', 'trend_caleb': 'trend_caleb.txt', 'trend_patriots': 'trend_patriots.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_gmmtv','trend.GMMTV RESPECT OUR CULTURE'),('trend_benjohnson','trend.Ben Johnson'),('trend_jaylon','trend.Jaylon Johnson'),","('trend_hila','trend.Hila'),('trend_caleb','trend.Caleb'),('trend_patriots','trend.Patriots'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0801Z.json') and '/23/' in _c: continue","if _c.endswith('0905Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T0707Z'","_last = '2026-10-23T0801Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('\'2 quote pages + 1 repost page (budget), common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) == 'trend.GMMTV RESPECT OUR CULTURE': return 'entertainment'  # 0801Z",
 "        if str(_x) in ('trend.Hila',): return 'internet'  # 0905Z: Hila Klein (h3h3), one event with Ethan Klein\n        if str(_x) == 'trend.GMMTV RESPECT OUR CULTURE': return 'entertainment'  # 0801Z"),
("but cut for the seventy-third run","but cut for the seventy-fourth run"),
("but cut for the seventy-fifth run","but cut for the seventy-sixth run"),
("cut for the seventy-fourth run and the four-hour desks","cut for the seventy-sixth run and the four-hour desks"),
("due since 2026-10-20T07:08Z) cut for the seventy-second run","due since 2026-10-20T07:08Z) cut for the seventy-fourth run"),
(OLD_WN, WATCH_NOTE),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0801Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0905Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Hila\", \"Caleb\" and \"Patriots\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 6 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (4:01 AM ET"):
    lines[i]="            f'Morning run (5:05 AM ET Oct 23 / 09:05 UTC Oct 23, the 09Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0801Z ended at 819, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 504 ids, so the 400 cap left out the 104 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"GMMTV"):
    lines[i]="            f'trend names \"Hila\", \"Caleb\" and \"Patriots\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[i]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0801Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 6 more (2113143833588613393, left out in 0002Z as minor bait, and 1746547721153241250, left out in 0606Z as likely paid, were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
