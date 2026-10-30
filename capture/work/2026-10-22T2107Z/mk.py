s=open('build_capture.py').read()
TN='two of the top-ten US names with no posts attached in 2007Z: "Iwo Jima" (new; "Quantico" lower in the list is the same event, the damaged Iwo Jima memorial statue at Marine Corps Base Quantico) and "Cenk" (new; Cenk Uygur\'s claims about the late Lindsey Graham, the same event as the "Lindsey Graham" trend); "Tom Skerritt", "Top Gun", "Picket Fences", "Steel Magnolias", "RIP Viper" and "LeBron James" were attached in 2007Z; "Lindsey Graham" was attached in 1501Z'
R=[
("Build capture/2026/10/22/2007Z.json","Build capture/2026/10/22/2107Z.json"),
("work/2026-10-22T2007Z'","work/2026-10-22T2107Z'"),
("RUN_ID = '2026-10-22T2007Z'","RUN_ID = '2026-10-22T2107Z'"),
("STARTED = '2026-10-22T20:07:00Z'","STARTED = '2026-10-22T21:07:00Z'"),
("OBS_AT = '2026-10-22T20:07:00Z'","OBS_AT = '2026-10-22T21:07:00Z'"),
("READS_BEFORE = 589","READS_BEFORE = 569"),
("datetime(2026,10,22,20,10,tzinfo=timezone.utc).timestamp()  # 2007Z (","datetime(2026,10,22,21,10,tzinfo=timezone.utc).timestamp()  # 2107Z (2007Z used 20:10, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_skerritt': 'trend_skerritt.txt', 'trend_lebron': 'trend_lebron.txt',","'trend_iwojima': 'trend_iwojima.txt', 'trend_cenk': 'trend_cenk.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_skerritt','trend.Tom Skerritt'),('trend_lebron','trend.LeBron James'),","('trend_iwojima','trend.Iwo Jima'),('trend_cenk','trend.Cenk'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2007Z.json') and '/22/' in _c: continue","if _c.endswith('2107Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T1902Z'","_last = '2026-10-22T2007Z'"),
('\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Tom Skerritt',): return 'entertainment'  # 2007Z: actor Tom Skerritt death",
 "        if str(_x) in ('trend.Iwo Jima',): return 'politics'  # 2107Z: Iwo Jima statue at Quantico damaged\n        if str(_x) in ('trend.Cenk',): return 'politics'  # 2107Z: Cenk Uygur claims about Lindsey Graham\n        if str(_x) in ('trend.Tom Skerritt',): return 'entertainment'  # 2007Z: actor Tom Skerritt death"),
("but cut for the sixty-first run","but cut for the sixty-second run"),
("cut for the sixty-third run (kept","cut for the sixty-fourth run (kept"),
("(this 20Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 527 long, so the 400 cap left out the 127 slowest-growing posts (95 still-gaining, 32 from the fourth-hour tier) and no cited post)",
 "(this 21Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 495 long, so the 400 cap left out the 95 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2007Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2107Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Iwo Jima\" and \"Cenk\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words is/you + and (quoted); hourly desks politics/entertainment/sports/internet; three screening reads by id (100 then 6 unread first-hop, most pointed-at first, then 31 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Afternoon run (4:07 PM ET"):
    lines[i]="            f'Evening run (5:07 PM ET / 21:07 UTC Oct 22, the 21Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2007Z ended at 569, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 495 ids, so the 400 cap left out the 95 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Tom Skerritt\""):
    lines[i]="            f'trend names \"Iwo Jima\" and \"Cenk\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[i]="            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2007Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-second run, both for the budget; '"; hit+=1
  elif st.startswith("f'three screening reads by id: 100 then 12"):
    lines[i]="            f'three screening reads by id: 100 then 6 unread referenced, reply-parent and media-source posts, most pointed-at first, then 31 more second-hop (2108062331095908717 Not Found again, not re-requested in the second-hop read); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
