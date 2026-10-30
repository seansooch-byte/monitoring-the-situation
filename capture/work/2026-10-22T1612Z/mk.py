s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 1501Z, all one event: "Jack Lowden", "Josh O\'Connor" and "Callum Turner" (new; reported finalists to be the next James Bond); "Luka", "Ron Duguay" and "Yaxel" were attached in 1409Z; "Lindsey Graham", "Louise Lucas", "#NINGNINGShines24ever" and "#닝닝의생일_민족의영광" were attached in 1501Z'
R=[
("Build capture/2026/10/22/1501Z.json","Build capture/2026/10/22/1612Z.json"),
("work/2026-10-22T1501Z'","work/2026-10-22T1612Z'"),
("RUN_ID = '2026-10-22T1501Z'","RUN_ID = '2026-10-22T1612Z'"),
("STARTED = '2026-10-22T15:01:00Z'","STARTED = '2026-10-22T16:12:00Z'"),
("OBS_AT = '2026-10-22T15:01:00Z'","OBS_AT = '2026-10-22T16:12:00Z'"),
("READS_BEFORE = 689","READS_BEFORE = 669"),
("datetime(2026,10,22,15,6,tzinfo=timezone.utc).timestamp()  # 1501Z (","datetime(2026,10,22,16,20,tzinfo=timezone.utc).timestamp()  # 1612Z (1501Z used 15:06, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_lucas': 'trend_lucas.txt', 'trend_graham': 'trend_graham.txt', 'trend_ningning': 'trend_ningning.txt',","'trend_lowden': 'trend_lowden.txt', 'trend_oconnor': 'trend_oconnor.txt', 'trend_turner': 'trend_turner.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_lucas','trend.Louise Lucas'),('trend_graham','trend.Lindsey Graham'),('trend_ningning','trend.#NINGNINGShines24ever'),","('trend_lowden','trend.Jack Lowden'),('trend_oconnor',\"trend.Josh O'Connor\"),('trend_turner','trend.Callum Turner'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1501Z.json') and '/22/' in _c: continue","if _c.endswith('1612Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T1409Z'","_last = '2026-10-22T1501Z'"),
('\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Louise Lucas','trend.Lindsey Graham'): return 'politics'  # 1501Z",
 "        if str(_x) in ('trend.Jack Lowden',\"trend.Josh O'Connor\",'trend.Callum Turner'): return 'entertainment'  # 1612Z: James Bond casting finalists\n        if str(_x) in ('trend.Louise Lucas','trend.Lindsey Graham'): return 'politics'  # 1501Z"),
("but cut for the fifty-sixth run","but cut for the fifty-seventh run"),
("cut for the fifty-eighth run (kept","cut for the fifty-ninth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1501Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1612Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Jack Lowden\", \"Josh O\\'Connor\" and \"Callum Turner\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then 19 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (11:01 AM ET"):
    lines[i]="            f'Midday run (12:12 PM ET / 16:12 UTC Oct 22, the 16Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1501Z ended at 669, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 536 ids, so the 400 cap left out the 136 slowest-growing still-gaining and fourth-hour posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Louise Lucas\""):
    lines[i]="            f'trend names \"Jack Lowden\", \"Josh O\\'Connor\" and \"Callum Turner\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[i]="            f'quote/repost words that/just + what (3 reads, each word quoted; the \"that\" quote page returned 16 posts); sensors culture/sports/online (3 reads; news/money/science last read 1501Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-seventh run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 19 more second-hop (2108062331095908717 came back Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
