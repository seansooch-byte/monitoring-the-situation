s=open('build_capture.py').read()
TN_OLD='three of the six top-ten US names with no posts attached in 1200Z: "Happy Friyay", "RED Friday" and "Hila" ("Hila" last read in 0905Z; "Good Friday" and "Fat Albert" read in 1107Z and "Ethan" is the same h3h3 event as "Hila", so skipped; "#中国上海立刻解决叠纸争议", "#AlconMustEndPPGcollab" and "#BladeRunnerCollabswithRacist" are the Papergames campaign attached in 1200Z, and "Dolan" was attached in 1200Z)'
TN='three of the top-ten US names with no posts attached in 1303Z: "Oleshky" (new), "#FridayVibes" (new) and "Fat Albert" (last read in 1107Z); "Dolan" and the Papergames tags ("#中国上海立刻解决叠纸争议", "#AlconMustEndPPGcollab", "#BladeRunnerCollabswithRacist") were read in 1200Z, so skipped'
OLD_WN="(this 13Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 515 long, so the 400 cap left out the 115 slowest-growing still-gaining posts in order, and no cited post)"
WATCH_NOTE="(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 522 long, so the 400 cap left out the 122 slowest-growing still-gaining posts in order, and no cited post)"
R=[
("Build capture/2026/10/23/1303Z.json","Build capture/2026/10/23/1401Z.json"),
("work/2026-10-23T1303Z'","work/2026-10-23T1401Z'"),
("RUN_ID = '2026-10-23T1303Z'","RUN_ID = '2026-10-23T1401Z'"),
("STARTED = '2026-10-23T13:03:00Z'","STARTED = '2026-10-23T14:01:00Z'"),
("OBS_AT = '2026-10-23T13:03:00Z'","OBS_AT = '2026-10-23T14:01:00Z'"),
("READS_BEFORE = 738","READS_BEFORE = 718"),
("datetime(2026,10,23,13,5,tzinfo=timezone.utc).timestamp()  # 1303Z (","datetime(2026,10,23,14,4,tzinfo=timezone.utc).timestamp()  # 1401Z (1303Z used 13:05, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_happyfriyay': 'trend_happyfriyay.txt', 'trend_redfriday': 'trend_redfriday.txt', 'trend_hila': 'trend_hila.txt',","'trend_oleshky': 'trend_oleshky.txt', 'trend_fridayvibes': 'trend_fridayvibes.txt', 'trend_fatalbert': 'trend_fatalbert.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_happyfriyay','trend.Happy Friyay'),('trend_redfriday','trend.RED Friday'),('trend_hila','trend.Hila'),","('trend_oleshky','trend.Oleshky'),('trend_fridayvibes','trend.#FridayVibes'),('trend_fatalbert','trend.Fat Albert'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1303Z.json') and '/23/' in _c: continue","if _c.endswith('1401Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T1200Z'","_last = '2026-10-23T1303Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\''),
("eightieth run","eighty-first run"),
("seventy-eighth run","seventy-ninth run"),
(OLD_WN, WATCH_NOTE),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1303Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1401Z.json'"),
(TN_OLD, TN),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
('trend names "Happy Friyay", "RED Friday" and "Hila" ("<name> lang:en is:retweet", newest first, 25 each;','trend names "Oleshky", "#FridayVibes" and "Fat Albert" ("<name> lang:en is:retweet", newest first, 25 each, hashtag unquoted;'),
("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)"),
("        if str(_x)=='trend.Happy Friyay': return 'life'","        if str(_x)=='trend.Happy Friyay': return 'life'\n        if str(_x)=='trend.Oleshky': return 'world'  # 1401Z: White House says Melania Trump secured a localized Russia-Ukraine ceasefire in Oleshky\n        if str(_x)=='trend.#FridayVibes': return 'life'  # 1401Z\n        if str(_x)=='trend.Fat Albert': return 'internet'  # 1401Z"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (9:03 AM ET"):
    lines[i]="            f'Morning run (10:01 AM ET Oct 23 / 14:01 UTC Oct 23, the 14Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1303Z ended at 718, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 522 ids, so the 400 cap left out the 122 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Happy Friyay"):
    lines[i]="            f'trend names \"Oleshky\", \"#FridayVibes\" and \"Fat Albert\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[i]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1303Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 23 more (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
