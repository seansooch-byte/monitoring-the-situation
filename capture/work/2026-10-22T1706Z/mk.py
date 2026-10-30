s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 1612Z: "Bond" (new; the same event as the James Bond finalist names attached in 1612Z), "Airbnb" (new) and "Luka" (attached last in 1409Z); "Ron Duguay" and "Yaxel" were attached in 1409Z; "Lindsey Graham", "Louise Lucas", "#NINGNINGShines24ever" and "#닝닝의생일_민족의영광" were attached in 1501Z; "Jack Lowden" was attached in 1612Z'
R=[
("Build capture/2026/10/22/1612Z.json","Build capture/2026/10/22/1706Z.json"),
("work/2026-10-22T1612Z'","work/2026-10-22T1706Z'"),
("RUN_ID = '2026-10-22T1612Z'","RUN_ID = '2026-10-22T1706Z'"),
("STARTED = '2026-10-22T16:12:00Z'","STARTED = '2026-10-22T17:06:00Z'"),
("OBS_AT = '2026-10-22T16:12:00Z'","OBS_AT = '2026-10-22T17:06:00Z'"),
("READS_BEFORE = 669","READS_BEFORE = 649"),
("datetime(2026,10,22,16,20,tzinfo=timezone.utc).timestamp()  # 1612Z (","datetime(2026,10,22,17,9,tzinfo=timezone.utc).timestamp()  # 1706Z (1612Z used 16:20, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_lowden': 'trend_lowden.txt', 'trend_oconnor': 'trend_oconnor.txt', 'trend_turner': 'trend_turner.txt',","'trend_bond': 'trend_bond.txt', 'trend_airbnb': 'trend_airbnb.txt', 'trend_luka': 'trend_luka.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_lowden','trend.Jack Lowden'),('trend_oconnor',\"trend.Josh O'Connor\"),('trend_turner','trend.Callum Turner'),","('trend_bond','trend.Bond'),('trend_airbnb','trend.Airbnb'),('trend_luka','trend.Luka'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1612Z.json') and '/22/' in _c: continue","if _c.endswith('1706Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T1501Z'","_last = '2026-10-22T1612Z'"),
('\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Jack Lowden',\"trend.Josh O'Connor\",'trend.Callum Turner'): return 'entertainment'  # 1612Z: James Bond casting finalists",
 "        if str(_x) in ('trend.Bond',): return 'entertainment'  # 1706Z: James Bond casting\n        if str(_x) in ('trend.Luka',): return 'sports'  # 1706Z\n        if str(_x) in ('trend.Jack Lowden',\"trend.Josh O'Connor\",'trend.Callum Turner'): return 'entertainment'  # 1612Z: James Bond casting finalists"),
("but cut for the fifty-seventh run","but cut for the fifty-eighth run"),
("cut for the fifty-ninth run (kept","cut for the sixtieth run (kept"),
("(this 14Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 475 long, so the 400 cap left out the 75 slowest-growing still-gaining posts and no cited post)",
 "(this 17Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 491 long, so the 400 cap left out the 91 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1612Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1706Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Bond\", \"Airbnb\" and \"Luka\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then 26 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Midday run (12:12 PM ET"):
    lines[i]="            f'Midday run (1:06 PM ET / 17:06 UTC Oct 22, the 17Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1612Z ended at 649, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 491 ids, so the 400 cap left out the 91 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Jack Lowden\""):
    lines[i]="            f'trend names \"Bond\", \"Airbnb\" and \"Luka\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[i]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1612Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixtieth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-eighth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 26 more second-hop (2108062331095908717 came back Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
