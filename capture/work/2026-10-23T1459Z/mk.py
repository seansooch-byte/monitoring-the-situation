s=open('build_capture.py').read()
TN_OLD='three of the top-ten US names with no posts attached in 1303Z: "Oleshky" (new), "#FridayVibes" (new) and "Fat Albert" (last read in 1107Z); "Dolan" and the Papergames tags ("#中国上海立刻解决叠纸争议", "#AlconMustEndPPGcollab", "#BladeRunnerCollabswithRacist") were read in 1200Z, so skipped'
TN='three of the top-ten US names with no posts attached in 1401Z: "Ethan Klein" (new name; "Ethan" is the h3h3 event last read as "Hila" in 0905Z), "Meghan" (new) and "#LetterboxdFriday" (new); "Good Friday" (read in 1107Z), "Dolan" and "RED Friday" (read in 1200Z) skipped, and "#LastFourWatched" is the same Friday film-list prompt as "#LetterboxdFriday"'
R=[
("Build capture/2026/10/23/1401Z.json","Build capture/2026/10/23/1459Z.json"),
("work/2026-10-23T1401Z'","work/2026-10-23T1459Z'"),
("RUN_ID = '2026-10-23T1401Z'","RUN_ID = '2026-10-23T1459Z'"),
("STARTED = '2026-10-23T14:01:00Z'","STARTED = '2026-10-23T14:59:00Z'"),
("OBS_AT = '2026-10-23T14:01:00Z'","OBS_AT = '2026-10-23T14:59:00Z'"),
("READS_BEFORE = 718","READS_BEFORE = 698"),
("datetime(2026,10,23,14,4,tzinfo=timezone.utc).timestamp()  # 1401Z (","datetime(2026,10,23,15,2,tzinfo=timezone.utc).timestamp()  # 1459Z (1401Z used 14:04, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_oleshky': 'trend_oleshky.txt', 'trend_fridayvibes': 'trend_fridayvibes.txt', 'trend_fatalbert': 'trend_fatalbert.txt',","'trend_ethanklein': 'trend_ethanklein.txt', 'trend_meghan': 'trend_meghan.txt', 'trend_letterboxdfriday': 'trend_letterboxdfriday.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_oleshky','trend.Oleshky'),('trend_fridayvibes','trend.#FridayVibes'),('trend_fatalbert','trend.Fat Albert'),","('trend_ethanklein','trend.Ethan Klein'),('trend_meghan','trend.Meghan'),('trend_letterboxdfriday','trend.#LetterboxdFriday'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1401Z.json') and '/23/' in _c: continue","if _c.endswith('1459Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T1303Z'","_last = '2026-10-23T1401Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\''),
("eighty-first run","eighty-second run"),
("seventy-ninth run","eightieth run"),
("(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 522 long, so the 400 cap left out the 122 slowest-growing","(this 15Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 510 long, so the 400 cap left out the 110 slowest-growing"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1401Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1459Z.json'"),
(TN_OLD, TN),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
('trend names "Oleshky", "#FridayVibes" and "Fat Albert" ("<name> lang:en is:retweet", newest first, 25 each, hashtag unquoted;','trend names "Ethan Klein", "Meghan" and "#LetterboxdFriday" ("<name> lang:en is:retweet", newest first, 25 each, hashtag unquoted;'),
("quote/repost words you/and + my (quoted)","quote/repost words it/that + just (quoted)"),
("then 23 more);","then 7 more);"),
("        if str(_x)=='trend.Fat Albert': return 'internet'  # 1401Z","        if str(_x)=='trend.Fat Albert': return 'internet'  # 1401Z\n        if str(_x)=='trend.Ethan Klein': return 'internet'  # 1459Z\n        if str(_x)=='trend.#LetterboxdFriday': return 'entertainment'  # 1459Z"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (10:01 AM ET"):
    lines[i]="            f'Morning run (10:59 AM ET Oct 23 / 14:59 UTC Oct 23, the 15Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1401Z ended at 698, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 510 ids, so the 400 cap left out the 110 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Oleshky"):
    lines[i]="            f'trend names \"Ethan Klein\", \"Meghan\" and \"#LetterboxdFriday\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words you/and"):
    lines[i]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1401Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 7 more (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 returned Not Found); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
