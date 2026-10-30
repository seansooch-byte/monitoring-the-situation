s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 1804Z: "AIPAC" (new), "Panamá" (new; the stream mixes the Panama earthquake, Starlink service there and a Treasury sanctions post) and "#TrumpsCrimesOnYourDime" (new); "Lindsey Graham" and "Louise Lucas" were attached in 1501Z; "Luka" and "Bond" were attached in 1706Z; "$MRNA" and "Josh Simmons" were attached in 1804Z; "Jack Lowden" was attached in 1612Z'
R=[
("Build capture/2026/10/22/1804Z.json","Build capture/2026/10/22/1902Z.json"),
("work/2026-10-22T1804Z'","work/2026-10-22T1902Z'"),
("RUN_ID = '2026-10-22T1804Z'","RUN_ID = '2026-10-22T1902Z'"),
("STARTED = '2026-10-22T18:04:00Z'","STARTED = '2026-10-22T19:02:00Z'"),
("OBS_AT = '2026-10-22T18:04:00Z'","OBS_AT = '2026-10-22T19:02:00Z'"),
("READS_BEFORE = 629","READS_BEFORE = 609"),
("datetime(2026,10,22,18,7,tzinfo=timezone.utc).timestamp()  # 1804Z (","datetime(2026,10,22,19,5,tzinfo=timezone.utc).timestamp()  # 1902Z (1804Z used 18:07, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_simmons': 'trend_simmons.txt', 'trend_mrna': 'trend_mrna.txt', 'trend_virginia': 'trend_virginia.txt',","'trend_aipac': 'trend_aipac.txt', 'trend_panama': 'trend_panama.txt', 'trend_trumpscrimes': 'trend_trumpscrimes.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_simmons','trend.Josh Simmons'),('trend_mrna','trend.$MRNA'),('trend_virginia','trend.Virginia'),","('trend_aipac','trend.AIPAC'),('trend_panama','trend.Panamá'),('trend_trumpscrimes','trend.#TrumpsCrimesOnYourDime'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1804Z.json') and '/22/' in _c: continue","if _c.endswith('1902Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T1706Z'","_last = '2026-10-22T1804Z'"),
('\'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Josh Simmons',): return 'sports'  # 1804Z: Chiefs LT Josh Simmons to IR",
 "        if str(_x) in ('trend.AIPAC',): return 'politics'  # 1902Z: AIPAC endorsement change\n        if str(_x) in ('trend.Panamá',): return 'disaster'  # 1902Z: Panama earthquake\n        if str(_x) in ('trend.#TrumpsCrimesOnYourDime',): return 'politics'  # 1902Z: hashtag campaign\n        if str(_x) in ('trend.Josh Simmons',): return 'sports'  # 1804Z: Chiefs LT Josh Simmons to IR"),
("but cut for the fifty-ninth run","but cut for the sixtieth run"),
("cut for the sixty-first run (kept","cut for the sixty-second run (kept"),
("(this 18Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 485 long, so the 400 cap left out the 85 slowest-growing still-gaining posts and no cited post)",
 "(this 19Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 494 long, so the 400 cap left out the 94 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1804Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1902Z.json'"),
("skip_nsfw |= {'2112886820119707868'}  # 1804Z:","skip_nsfw |= {'2113336264175079586','2109000277626089888'}  # 1902Z: pornographic posts in the Panamá trend stream (sexual, not captured)\nskip_nsfw |= {'2112886820119707868'}  # 1804Z:"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"AIPAC\", \"Panamá\" and \"#TrumpsCrimesOnYourDime\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then 18 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Afternoon run (2:04 PM ET"):
    lines[i]="            f'Afternoon run (3:02 PM ET / 19:02 UTC Oct 22, the 19Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1804Z ended at 609, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 494 ids, so the 400 cap left out the 94 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Josh Simmons\""):
    lines[i]="            f'trend names \"AIPAC\", \"Panamá\" and \"#TrumpsCrimesOnYourDime\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words you/and"):
    lines[i]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1804Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-second run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixtieth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 18 more second-hop (2108062331095908717 came back Not Found); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
