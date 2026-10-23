s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0959Z: "Good Friday", "Fat Albert" and "James Dolan" ("Ethan Klein" and "Hila" read in 0905Z, so skipped; "Remember Everyone Deployed" is the RED Friday tag and "#Avatarsevenhavens" the #SevenHavens name, both read in 0959Z; "Happy Friyay" left for the budget)'
OLD_WN="(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 507 long, so the 400 cap left out the 107 slowest-growing still-gaining posts in order, and no cited post)"
WATCH_NOTE="(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 505 long, so the 400 cap left out the 105 slowest-growing still-gaining posts in order, and no cited post)"
R=[
("Build capture/2026/10/23/0959Z.json","Build capture/2026/10/23/1107Z.json"),
("work/2026-10-23T0959Z'","work/2026-10-23T1107Z'"),
("RUN_ID = '2026-10-23T0959Z'","RUN_ID = '2026-10-23T1107Z'"),
("STARTED = '2026-10-23T09:59:00Z'","STARTED = '2026-10-23T11:07:00Z'"),
("OBS_AT = '2026-10-23T09:59:00Z'","OBS_AT = '2026-10-23T11:07:00Z'"),
("READS_BEFORE = 799","READS_BEFORE = 778"),
("datetime(2026,10,23,10,1,tzinfo=timezone.utc).timestamp()  # 0959Z (","datetime(2026,10,23,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (0959Z used 10:01, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_redfriday': 'trend_redfriday.txt', 'trend_creditourheritage': 'trend_creditourheritage.txt', 'trend_sevenhavens': 'trend_sevenhavens.txt',","'trend_goodfriday': 'trend_goodfriday.txt', 'trend_fatalbert': 'trend_fatalbert.txt', 'trend_jamesdolan': 'trend_jamesdolan.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_redfriday','trend.RED Friday'),('trend_creditourheritage','trend.#CreditOurHeritage'),('trend_sevenhavens','trend.#SevenHavens'),","('trend_goodfriday','trend.Good Friday'),('trend_fatalbert','trend.Fat Albert'),('trend_jamesdolan','trend.James Dolan'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0959Z.json') and '/23/' in _c: continue","if _c.endswith('1107Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T0905Z'","_last = '2026-10-23T0959Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('\'2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\''),
("but cut for the seventy-fifth run","but cut for the seventy-sixth run"),
("but cut for the seventy-seventh run","but cut for the seventy-eighth run"),
("cut for the seventy-seventh run and the four-hour desks","cut for the seventy-eighth run and the four-hour desks"),
("due since 2026-10-20T07:08Z) cut for the seventy-fifth run","due since 2026-10-20T07:08Z) cut for the seventy-sixth run"),
(OLD_WN, WATCH_NOTE),
("        if str(_x) in ('trend.RED Friday','trend.Good Friday'): return 'life'\n","        if str(_x) in ('trend.RED Friday','trend.Good Friday'): return 'life'\n        if str(_x)=='trend.James Dolan': return 'sports'  # 1107Z: Knicks owner\n"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0959Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1107Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Good Friday\", \"Fat Albert\" and \"James Dolan\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 1 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (5:59 AM ET"):
    lines[i]="            f'Morning run (7:07 AM ET Oct 23 / 11:07 UTC Oct 23, the 11Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0959Z ended at 779, so one read went elsewhere in between, likely the 7:03 AM ET daily briefing), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 505 ids, so the 400 cap left out the 105 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"RED Friday"):
    lines[i]="            f'trend names \"Good Friday\", \"Fat Albert\" and \"James Dolan\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[i]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0959Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 1 more (1746547721153241250, left out in 0606Z as likely paid, was not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
