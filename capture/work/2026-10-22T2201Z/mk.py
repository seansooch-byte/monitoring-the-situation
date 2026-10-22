s=open('build_capture.py').read()
TN='two of the top-ten US names with no posts attached in 2107Z: "Marnie" (new; Sara Paxton reportedly eyed to return as Marnie Piper in a fifth Halloweentown film at Disney+, the same event as the "Kimberly J Brown" trend) and "Marines" (new; the damaged Iwo Jima memorial statue at Marine Corps Base Quantico, the same event as the "Iwo Jima" and "Quantico" trends attached in 2107Z); "Tom Skerritt", "Top Gun", "Picket Fences" were attached in 2007Z; "Lindsey Graham", "Iwo Jima" and "Cenk" were attached in 2107Z; "Steel Magnolias" and "Viper" are the Tom Skerritt event attached in 2007Z'
R=[
("Build capture/2026/10/22/2107Z.json","Build capture/2026/10/22/2201Z.json"),
("work/2026-10-22T2107Z'","work/2026-10-22T2201Z'"),
("RUN_ID = '2026-10-22T2107Z'","RUN_ID = '2026-10-22T2201Z'"),
("STARTED = '2026-10-22T21:07:00Z'","STARTED = '2026-10-22T22:01:00Z'"),
("OBS_AT = '2026-10-22T21:07:00Z'","OBS_AT = '2026-10-22T22:01:00Z'"),
("READS_BEFORE = 569","READS_BEFORE = 549"),
("datetime(2026,10,22,21,10,tzinfo=timezone.utc).timestamp()  # 2107Z (","datetime(2026,10,22,22,3,tzinfo=timezone.utc).timestamp()  # 2201Z (2107Z used 21:10, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_iwojima': 'trend_iwojima.txt', 'trend_cenk': 'trend_cenk.txt',","'trend_marnie': 'trend_marnie.txt', 'trend_marines': 'trend_marines.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_iwojima','trend.Iwo Jima'),('trend_cenk','trend.Cenk'),","('trend_marnie','trend.Marnie'),('trend_marines','trend.Marines'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2107Z.json') and '/22/' in _c: continue","if _c.endswith('2201Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T2007Z'","_last = '2026-10-22T2107Z'"),
('\'2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Iwo Jima',): return 'politics'  # 2107Z",
 "        if str(_x) in ('trend.Marines',): return 'politics'  # 2201Z: Iwo Jima statue at Quantico damaged\n        if str(_x) in ('trend.Marnie',): return 'entertainment'  # 2201Z: Halloweentown 5 casting\n        if str(_x) in ('trend.Iwo Jima',): return 'politics'  # 2107Z"),
("but cut for the sixty-second run","but cut for the sixty-third run"),
("cut for the sixty-fourth run (kept","cut for the sixty-fifth run (kept"),
("(this 21Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 495 long, so the 400 cap left out the 95 slowest-growing still-gaining posts and no cited post)",
 "(this 22Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 503 long, so the 400 cap left out the 103 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2201Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Marnie\" and \"Marines\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words my/it + that (quoted); hourly desks politics/entertainment/sports/internet; three screening reads by id (100 then 6 unread first-hop, most pointed-at first, then 20 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Evening run (5:07 PM ET"):
    lines[i]="            f'Evening run (6:01 PM ET / 22:01 UTC Oct 22, the 22Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2107Z ended at 549, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 503 ids, so the 400 cap left out the 103 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Iwo Jima\""):
    lines[i]="            f'trend names \"Marnie\" and \"Marines\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words is/you"):
    lines[i]="            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2107Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-fifth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-third run, both for the budget; '"; hit+=1
  elif st.startswith("f'three screening reads by id: 100 then 6"):
    lines[i]="            f'three screening reads by id: 100 then 6 unread referenced, reply-parent and media-source posts, most pointed-at first, then 20 more second-hop (2108062331095908717 Not Found again, not re-requested in the second-hop read); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
