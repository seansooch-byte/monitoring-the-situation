s=open('build_capture.py').read()
R=[
("Build capture/2026/10/22/0607Z.json","Build capture/2026/10/22/0706Z.json"),
("work/2026-10-22T0607Z'","work/2026-10-22T0706Z'"),
("RUN_ID = '2026-10-22T0607Z'","RUN_ID = '2026-10-22T0706Z'"),
("STARTED = '2026-10-22T06:07:00Z'","STARTED = '2026-10-22T07:06:00Z'"),
("OBS_AT = '2026-10-22T06:07:00Z'","OBS_AT = '2026-10-22T07:06:00Z'"),
("READS_BEFORE = 879","READS_BEFORE = 859"),
("datetime(2026,10,22,6,10,tzinfo=timezone.utc).timestamp()  # 0607Z (","datetime(2026,10,22,7,10,tzinfo=timezone.utc).timestamp()  # 0706Z (0607Z used 06:10, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_is': 'quote_is.txt',"),
("'repost_what': 'repost_what.txt',","'repost_you': 'repost_you.txt',"),
("'trend_lakers': 'trend_lakers.txt', 'trend_blazers': 'trend_blazers.txt', 'trend_suns': 'trend_suns.txt',","'trend_warriors': 'trend_warriors.txt', 'trend_draymond': 'trend_draymond.txt', 'trend_lakeshow': 'trend_lakeshow.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_lakers','trend.Lakers'),('trend_blazers','trend.Blazers'),('trend_suns','trend.Suns'),","('trend_warriors','trend.Warriors'),('trend_draymond','trend.Draymond'),('trend_lakeshow','trend.#LakeShow'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0607Z.json') and '/22/' in _c: continue","if _c.endswith('0706Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T0502Z'","_last = '2026-10-22T0607Z'"),
("cut for the forty-seventh run (the 06:00-11:00","cut for the forty-eighth run (the 06:00-11:00"),
("cut for the forty-ninth run (the 06:00-11:00","cut for the fiftieth run (the 06:00-11:00"),
("(this 06Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 430 long, so the 400 cap left out the 30 slowest-growing still-gaining posts and no cited post)",
 "(this 07Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 440 long, so the 400 cap left out the 40 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0607Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0706Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "the", "is" and "you", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Lakers','trend.Blazers','trend.Suns'): return 'sports'  # 0607Z",
 "        if str(_x) in ('trend.Warriors','trend.Draymond','trend.#LakeShow'): return 'sports'  # 0706Z: Warriors at Lakers (NBA opening week)\n        if str(_x) in ('trend.Lakers','trend.Blazers','trend.Suns'): return 'sports'  # 0607Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
TN='three of the top-ten US names with no posts attached in 0607Z: "Warriors", "Draymond" and "#LakeShow" (all the Warriors at Lakers game, as Luka, Lakers and Steph); Luka, Yaxel and Kessler had posts attached in 0408Z; Ty Jerome and Steph in 0502Z; Lakers and Suns in 0607Z'
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Warriors\", \"Draymond\" and \"#LakeShow\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words the/is + you (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 7 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Overnight run (2:07 AM ET"):
    lines[i]="            f'Overnight run (3:06 AM ET / 07:06 UTC Oct 22, the 07Z slot; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0607Z ended at 859, so no read went elsewhere in between), parallel batches of up to 10, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 440 ids, so the 400 cap left out the 40 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Lakers\""):
    lines[i]="            f'trend names \"Warriors\", \"Draymond\" and \"#LakeShow\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[i]="            f'quote/repost words the/is + you (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0607Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fiftieth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the forty-eighth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned; 2108062331095908717, Not Found in earlier runs, again reported Not Found as a referenced post), then the 7 remaining unread referenced posts (7 returned); second-hop posts first seen in the screening reads left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
