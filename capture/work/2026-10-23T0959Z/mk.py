s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0905Z and not read before as names: "RED Friday", "#CreditOurHeritage" and "#SevenHavens" ("GMMTV RESPECT OUR CULTURE" read in 0801Z, "Jokic" and "Dear JT" in 0707Z, so skipped; "Bears" and "Caleb" are Patriots at Bears TNF, "Caleb" read in 0905Z), and "Ethan Klein", "Hila" and "Caleb" had posts attached in 0905Z'
OLD_WN="(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 504 long, so the 400 cap left out the 104 slowest-growing still-gaining posts in order, and no cited post)"
WATCH_NOTE="(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 507 long, so the 400 cap left out the 107 slowest-growing still-gaining posts in order, and no cited post)"
R=[
("Build capture/2026/10/23/0905Z.json","Build capture/2026/10/23/0959Z.json"),
("work/2026-10-23T0905Z'","work/2026-10-23T0959Z'"),
("RUN_ID = '2026-10-23T0905Z'","RUN_ID = '2026-10-23T0959Z'"),
("STARTED = '2026-10-23T09:05:00Z'","STARTED = '2026-10-23T09:59:00Z'"),
("OBS_AT = '2026-10-23T09:05:00Z'","OBS_AT = '2026-10-23T09:59:00Z'"),
("READS_BEFORE = 819","READS_BEFORE = 799"),
("datetime(2026,10,23,9,7,tzinfo=timezone.utc).timestamp()  # 0905Z (","datetime(2026,10,23,10,1,tzinfo=timezone.utc).timestamp()  # 0959Z (0905Z used 09:07, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_hila': 'trend_hila.txt', 'trend_caleb': 'trend_caleb.txt', 'trend_patriots': 'trend_patriots.txt',","'trend_redfriday': 'trend_redfriday.txt', 'trend_creditourheritage': 'trend_creditourheritage.txt', 'trend_sevenhavens': 'trend_sevenhavens.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_hila','trend.Hila'),('trend_caleb','trend.Caleb'),('trend_patriots','trend.Patriots'),","('trend_redfriday','trend.RED Friday'),('trend_creditourheritage','trend.#CreditOurHeritage'),('trend_sevenhavens','trend.#SevenHavens'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0905Z.json') and '/23/' in _c: continue","if _c.endswith('0959Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T0801Z'","_last = '2026-10-23T0905Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('\'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\''),
("but cut for the seventy-fourth run","but cut for the seventy-fifth run"),
("but cut for the seventy-sixth run","but cut for the seventy-seventh run"),
("cut for the seventy-sixth run and the four-hour desks","cut for the seventy-seventh run and the four-hour desks"),
("due since 2026-10-20T07:08Z) cut for the seventy-fourth run","due since 2026-10-20T07:08Z) cut for the seventy-fifth run"),
(OLD_WN, WATCH_NOTE),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0905Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0959Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"RED Friday\", \"#CreditOurHeritage\" and \"#SevenHavens\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words this/is + you (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 17 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (5:05 AM ET"):
    lines[i]="            f'Morning run (5:59 AM ET Oct 23 / 09:59 UTC Oct 23, the 10Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0905Z ended at 799, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 507 ids, so the 400 cap left out the 107 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Hila"):
    lines[i]="            f'trend names \"RED Friday\", \"#CreditOurHeritage\" and \"#SevenHavens\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[i]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0905Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 17 more (1746547721153241250, left out in 0606Z as likely paid, and 2113473131914445206, left out in 0905Z as likely paid, were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
