s=open('build_capture.py').read()
TN='two of the top-ten US names with no posts attached in 1902Z: "Tom Skerritt" (new; "Top Gun", "Picket Fences", "Steel Magnolias" and "RIP Viper" are the same event, the death of actor Tom Skerritt, so one read covers them) and "LeBron James" (new); "Lindsey Graham" and "Louise Lucas" were attached in 1501Z; "Luka" and "Bond" were attached in 1706Z'
R=[
("Build capture/2026/10/22/1902Z.json","Build capture/2026/10/22/2007Z.json"),
("work/2026-10-22T1902Z'","work/2026-10-22T2007Z'"),
("RUN_ID = '2026-10-22T1902Z'","RUN_ID = '2026-10-22T2007Z'"),
("STARTED = '2026-10-22T19:02:00Z'","STARTED = '2026-10-22T20:07:00Z'"),
("OBS_AT = '2026-10-22T19:02:00Z'","OBS_AT = '2026-10-22T20:07:00Z'"),
("READS_BEFORE = 609","READS_BEFORE = 589"),
("datetime(2026,10,22,19,5,tzinfo=timezone.utc).timestamp()  # 1902Z (","datetime(2026,10,22,20,10,tzinfo=timezone.utc).timestamp()  # 2007Z (1902Z used 19:05, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_aipac': 'trend_aipac.txt', 'trend_panama': 'trend_panama.txt', 'trend_trumpscrimes': 'trend_trumpscrimes.txt',","'trend_skerritt': 'trend_skerritt.txt', 'trend_lebron': 'trend_lebron.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_aipac','trend.AIPAC'),('trend_panama','trend.Panamá'),('trend_trumpscrimes','trend.#TrumpsCrimesOnYourDime'),","('trend_skerritt','trend.Tom Skerritt'),('trend_lebron','trend.LeBron James'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1902Z.json') and '/22/' in _c: continue","if _c.endswith('2007Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T1804Z'","_last = '2026-10-22T1902Z'"),
('\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.AIPAC',): return 'politics'  # 1902Z: AIPAC endorsement change",
 "        if str(_x) in ('trend.Tom Skerritt',): return 'entertainment'  # 2007Z: actor Tom Skerritt death\n        if str(_x) in ('trend.LeBron James',): return 'sports'  # 2007Z\n        if str(_x) in ('trend.AIPAC',): return 'politics'  # 1902Z: AIPAC endorsement change"),
("but cut for the sixtieth run","but cut for the sixty-first run"),
("cut for the sixty-second run (kept","cut for the sixty-third run (kept"),
("(this 19Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 494 long, so the 400 cap left out the 94 slowest-growing still-gaining posts and no cited post)",
 "(this 20Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 527 long, so the 400 cap left out the 127 slowest-growing posts (95 still-gaining, 32 from the fourth-hour tier) and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1902Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2007Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Tom Skerritt\" and \"LeBron James\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words what/the + this (quoted); hourly desks politics/entertainment/sports/internet; three screening reads by id (100 then 12 unread first-hop, most pointed-at first, then 25 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Afternoon run (3:02 PM ET"):
    lines[i]="            f'Afternoon run (4:07 PM ET / 20:07 UTC Oct 22, the 20Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1902Z ended at 589, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 527 ids, so the 400 cap left out the 127 slowest-growing posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"AIPAC\""):
    lines[i]="            f'trend names \"Tom Skerritt\" and \"LeBron James\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[i]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1902Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-first run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'three screening reads by id: 100 then 12 unread referenced, reply-parent and media-source posts, most pointed-at first, then 25 more second-hop (2108062331095908717 Not Found again, not re-requested in the second-hop read); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
