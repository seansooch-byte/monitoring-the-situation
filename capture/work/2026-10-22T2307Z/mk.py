s=open('build_capture.py').read()
TN='two of the top-ten US names with no posts attached in 2201Z: "Vanity Fair" (new; a Vanity Fair excerpt from Matthew Cole\'s book Princes and Thieves alleging that Jared Kushner\'s hacked iPhone exposed secret discussions) and "Tom Skerritt" (the actor\'s death at 93, last attached in 2007Z; the same event as the "Top Gun", "Picket Fences", "Steel Magnolias" and "Viper" trends); "Lindsey Graham" was attached in 2107Z; "Marines", "Iwo Jima" and "Marnie" were attached in 2201Z'
R=[
("Build capture/2026/10/22/2201Z.json","Build capture/2026/10/22/2307Z.json"),
("work/2026-10-22T2201Z'","work/2026-10-22T2307Z'"),
("RUN_ID = '2026-10-22T2201Z'","RUN_ID = '2026-10-22T2307Z'"),
("STARTED = '2026-10-22T22:01:00Z'","STARTED = '2026-10-22T23:07:00Z'"),
("OBS_AT = '2026-10-22T22:01:00Z'","OBS_AT = '2026-10-22T23:07:00Z'"),
("READS_BEFORE = 549","READS_BEFORE = 529"),
("datetime(2026,10,22,22,3,tzinfo=timezone.utc).timestamp()  # 2201Z (","datetime(2026,10,22,23,10,tzinfo=timezone.utc).timestamp()  # 2307Z (2201Z used 22:03, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_marnie': 'trend_marnie.txt', 'trend_marines': 'trend_marines.txt',","'trend_vanityfair': 'trend_vanityfair.txt', 'trend_skerritt': 'trend_skerritt.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_marnie','trend.Marnie'),('trend_marines','trend.Marines'),","('trend_vanityfair','trend.Vanity Fair'),('trend_skerritt','trend.Tom Skerritt'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2201Z.json') and '/22/' in _c: continue","if _c.endswith('2307Z.json') and '/22/' in _c: continue"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T2107Z'","_last = '2026-10-22T2201Z'"),
('\'2 quote pages + 1 repost page (budget), common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Marines',): return 'politics'  # 2201Z",
 "        if str(_x) in ('trend.Vanity Fair',): return 'politics'  # 2307Z: Vanity Fair Kushner excerpt\n        if str(_x) in ('trend.Tom Skerritt',): return 'entertainment'  # 2307Z: actor dies at 93\n        if str(_x) in ('trend.Marines',): return 'politics'  # 2201Z"),
("but cut for the sixty-third run","but cut for the sixty-fourth run"),
("cut for the sixty-fifth run (kept","cut for the sixty-sixth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2201Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2307Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Vanity Fair\" and \"Tom Skerritt\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; three screening reads by id (100 then 1 unread first-hop, most pointed-at first, then 24 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Evening run (6:01 PM ET"):
    lines[i]="            f'Evening run (7:07 PM ET / 23:07 UTC Oct 22, the 23Z slot and the last run of the UTC day; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2201Z ended at 529, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 504 ids, so the 400 cap left out the 104 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Marnie\""):
    lines[i]="            f'trend names \"Vanity Fair\" and \"Tom Skerritt\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[i]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2201Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-sixth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-fourth run, both for the budget; '"; hit+=1
  elif st.startswith("f'three screening reads by id: 100 then 6"):
    lines[i]="            f'three screening reads by id: 100 then 1 unread referenced, reply-parent and media-source posts, most pointed-at first, then 24 more second-hop (2108062331095908717 and 2113355503279718485 Not Found, not re-requested in the second-hop read); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
