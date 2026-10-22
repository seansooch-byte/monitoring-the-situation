s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 1706Z: "Josh Simmons" (new), "$MRNA" (new) and "Virginia" (new; the same event as the Louise Lucas indictment attached in 1501Z); "Lindsey Graham", "Louise Lucas", "#NINGNINGShines24ever" and "#닝닝의생일_민족의영광" were attached in 1501Z; "Luka" and "Bond" were attached in 1706Z; "Jack Lowden" was attached in 1612Z'
R=[
("Build capture/2026/10/22/1706Z.json","Build capture/2026/10/22/1804Z.json"),
("work/2026-10-22T1706Z'","work/2026-10-22T1804Z'"),
("RUN_ID = '2026-10-22T1706Z'","RUN_ID = '2026-10-22T1804Z'"),
("STARTED = '2026-10-22T17:06:00Z'","STARTED = '2026-10-22T18:04:00Z'"),
("OBS_AT = '2026-10-22T17:06:00Z'","OBS_AT = '2026-10-22T18:04:00Z'"),
("READS_BEFORE = 649","READS_BEFORE = 629"),
("datetime(2026,10,22,17,9,tzinfo=timezone.utc).timestamp()  # 1706Z (","datetime(2026,10,22,18,7,tzinfo=timezone.utc).timestamp()  # 1804Z (1706Z used 17:09, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_bond': 'trend_bond.txt', 'trend_airbnb': 'trend_airbnb.txt', 'trend_luka': 'trend_luka.txt',","'trend_simmons': 'trend_simmons.txt', 'trend_mrna': 'trend_mrna.txt', 'trend_virginia': 'trend_virginia.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_bond','trend.Bond'),('trend_airbnb','trend.Airbnb'),('trend_luka','trend.Luka'),","('trend_simmons','trend.Josh Simmons'),('trend_mrna','trend.$MRNA'),('trend_virginia','trend.Virginia'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1706Z.json') and '/22/' in _c: continue","if _c.endswith('1804Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T1612Z'","_last = '2026-10-22T1706Z'"),
('\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Bond',): return 'entertainment'  # 1706Z: James Bond casting",
 "        if str(_x) in ('trend.Josh Simmons',): return 'sports'  # 1804Z: Chiefs LT Josh Simmons to IR\n        if str(_x) in ('trend.$MRNA',): return 'markets'  # 1804Z: Moderna stock drop\n        if str(_x) in ('trend.Virginia',): return 'politics'  # 1804Z: Louise Lucas indictment\n        if str(_x) in ('trend.Bond',): return 'entertainment'  # 1706Z: James Bond casting"),
("but cut for the fifty-eighth run","but cut for the fifty-ninth run"),
("cut for the sixtieth run (kept","cut for the sixty-first run (kept"),
("(this 17Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 491 long, so the 400 cap left out the 91 slowest-growing still-gaining posts and no cited post)",
 "(this 18Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 485 long, so the 400 cap left out the 85 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1706Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1804Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Josh Simmons\", \"$MRNA\" and \"Virginia\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then 32 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Midday run (1:06 PM ET"):
    lines[i]="            f'Afternoon run (2:04 PM ET / 18:04 UTC Oct 22, the 18Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1706Z ended at 629, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 485 ids, so the 400 cap left out the 85 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Bond\""):
    lines[i]="            f'trend names \"Josh Simmons\", \"$MRNA\" and \"Virginia\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[i]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1706Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-first run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-ninth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 32 more second-hop (2108062331095908717 and 1914164422034997635 came back Not Found); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
