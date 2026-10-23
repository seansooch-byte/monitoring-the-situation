s=open('build_capture.py').read()
TN_OLD='three of the top-ten US names with no posts attached in 1401Z: "Ethan Klein" (new name; "Ethan" is the h3h3 event last read as "Hila" in 0905Z), "Meghan" (new) and "#LetterboxdFriday" (new); "Good Friday" (read in 1107Z), "Dolan" and "RED Friday" (read in 1200Z) skipped, and "#LastFourWatched" is the same Friday film-list prompt as "#LetterboxdFriday"'
TN='three of the top-ten US names with no posts attached in 1459Z: "Hellebuyck" (new), "Chad Patrick" (new) and "Oleshky" (last read in 1401Z); "Ethan Klein" and "Meghan" (read in 1459Z), "Fat Albert" and "#FridayVibes" (read in 1401Z), "Good Friday" (read in 1107Z) and "Dolan" (read in 1200Z) skipped, and "#LastFourWatched" is the same Friday film-list prompt as "#LetterboxdFriday" (read in 1459Z)'
R=[
("Build capture/2026/10/23/1459Z.json","Build capture/2026/10/23/1602Z.json"),
("work/2026-10-23T1459Z'","work/2026-10-23T1602Z'"),
("RUN_ID = '2026-10-23T1459Z'","RUN_ID = '2026-10-23T1602Z'"),
("STARTED = '2026-10-23T14:59:00Z'","STARTED = '2026-10-23T16:02:00Z'"),
("OBS_AT = '2026-10-23T14:59:00Z'","OBS_AT = '2026-10-23T16:02:00Z'"),
("READS_BEFORE = 698","READS_BEFORE = 678"),
("datetime(2026,10,23,15,2,tzinfo=timezone.utc).timestamp()  # 1459Z (","datetime(2026,10,23,16,5,tzinfo=timezone.utc).timestamp()  # 1602Z (1459Z used 15:02, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_ethanklein': 'trend_ethanklein.txt', 'trend_meghan': 'trend_meghan.txt', 'trend_letterboxdfriday': 'trend_letterboxdfriday.txt',","'trend_hellebuyck': 'trend_hellebuyck.txt', 'trend_chadpatrick': 'trend_chadpatrick.txt', 'trend_oleshky': 'trend_oleshky.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_ethanklein','trend.Ethan Klein'),('trend_meghan','trend.Meghan'),('trend_letterboxdfriday','trend.#LetterboxdFriday'),","('trend_hellebuyck','trend.Hellebuyck'),('trend_chadpatrick','trend.Chad Patrick'),('trend_oleshky','trend.Oleshky'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1459Z.json') and '/23/' in _c: continue","if _c.endswith('1602Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T1401Z'","_last = '2026-10-23T1459Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\''),
("eighty-second run","eighty-third run"),
("eightieth run","eighty-first run"),
("(this 15Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 510 long, so the 400 cap left out the 110 slowest-growing","(this 16Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and fourth-hour tiers, the list was 563 long, so the 400 cap left out 163 (115 slowest-growing still-gaining and 48 fourth-hour), the slowest-growing"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1459Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1602Z.json'"),
(TN_OLD, TN),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
('trend names "Ethan Klein", "Meghan" and "#LetterboxdFriday" ("<name> lang:en is:retweet", newest first, 25 each, hashtag unquoted;','trend names "Hellebuyck", "Chad Patrick" and "Oleshky" ("<name> lang:en is:retweet", newest first, 25 each;'),
("quote/repost words it/that + just (quoted)","quote/repost words what/the + this (quoted)"),
("        if str(_x)=='trend.#LetterboxdFriday': return 'entertainment'  # 1459Z","        if str(_x)=='trend.#LetterboxdFriday': return 'entertainment'  # 1459Z\n        if str(_x) in ('trend.Hellebuyck','trend.Chad Patrick'): return 'sports'  # 1602Z"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (10:59 AM ET"):
    lines[i]="            f'Midday run (12:02 PM ET Oct 23 / 16:02 UTC Oct 23, the 16Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1459Z ended at 678, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 563 ids, so the 400 cap left out 163 (115 slowest-growing still-gaining and 48 fourth-hour) in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Ethan Klein"):
    lines[i]="            f'trend names \"Hellebuyck\", \"Chad Patrick\" and \"Oleshky\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[i]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1459Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 8 more (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 returned Not Found); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
