s=open('build_capture.py').read()
TN='three of the top-ten US names, none with posts attached in 0059Z: "Jaylon Johnson" (the Patriots at Bears Thursday night game, the same event as the "Bears", "Drake Maye", "Luther Burden", "Ben Johnson", "Patriots", "Rome Odunze", "Josh McDaniels", "Al Michaels" and "#ThrowTheBallUp" trends), "Cavs" (Cavaliers v 76ers, the same event as "Sixers", "76ers", "Harden", "Maxey", "Donovan Mitchell" and "Kenny Atkinson") and "#VERZUZ" (new; the Verzuz battle, likely the same event as "Carl Thomas"); the other top-ten names left as the same two games'
R=[
("Build capture/2026/10/23/0059Z.json","Build capture/2026/10/23/0205Z.json"),
("work/2026-10-23T0059Z'","work/2026-10-23T0205Z'"),
("RUN_ID = '2026-10-23T0059Z'","RUN_ID = '2026-10-23T0205Z'"),
("STARTED = '2026-10-23T00:59:00Z'","STARTED = '2026-10-23T02:05:00Z'"),
("OBS_AT = '2026-10-23T00:59:00Z'","OBS_AT = '2026-10-23T02:05:00Z'"),
("READS_BEFORE = 979","READS_BEFORE = 959"),
("datetime(2026,10,23,1,1,tzinfo=timezone.utc).timestamp()  # 0059Z (","datetime(2026,10,23,2,7,tzinfo=timezone.utc).timestamp()  # 0205Z (0059Z used 01:01, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_mcdaniels': 'trend_mcdaniels.txt', 'trend_911onabc': 'trend_911onabc.txt', 'trend_swift': 'trend_swift.txt',","'trend_jaylon': 'trend_jaylon.txt', 'trend_cavs': 'trend_cavs.txt', 'trend_verzuz': 'trend_verzuz.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_mcdaniels','trend.Josh McDaniels'),('trend_911onabc','trend.#911onABC'),('trend_swift','trend.Swift'),","('trend_jaylon','trend.Jaylon Johnson'),('trend_cavs','trend.Cavs'),('trend_verzuz','trend.#VERZUZ'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0059Z.json') and '/23/' in _c: continue","if _c.endswith('0205Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-23T0002Z'","_last = '2026-10-23T0059Z'"),
("last read in 2026-10-23T0002Z',[]))","last read in 2026-10-23T0002Z',[]))"),
('\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Josh McDaniels','trend.Swift'): return 'sports'  # 0059Z: Patriots at Bears TNF",
 "        if str(_x) in ('trend.Jaylon Johnson',): return 'sports'  # 0205Z: Patriots at Bears TNF\n        if str(_x) in ('trend.#VERZUZ',): return 'music'  # 0205Z: Verzuz battle\n        if str(_x) in ('trend.Josh McDaniels','trend.Swift'): return 'sports'  # 0059Z: Patriots at Bears TNF"),
("but cut for the sixty-sixth run","but cut for the sixty-seventh run"),
("cut for the sixty-eighth run (kept","cut for the sixty-ninth run (kept"),
("(this 00Z-slot run is a fourth hour, so the rest of the last 24 hours was added slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 543 long, so the 400 cap left out the 143 slowest-growing posts (113 still-gaining, 30 fourth-hour) and no cited post)",
 "(this 02Z-slot run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 510 long, so the 400 cap left out the 103 slowest-growing still-gaining posts and the 7 last six-hour posts in order, and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0059Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0205Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Jaylon Johnson\", \"Cavs\" and \"#VERZUZ\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 14 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Evening run (8:59 PM ET"):
    lines[i]="            f'Evening run (10:05 PM ET Oct 22 / 02:05 UTC Oct 23, the 02Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0059Z ended at 959, so no read went elsewhere in between), parallel batches of up to 15, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 510 ids, so the 400 cap left out 103 slowest-growing still-gaining posts and the 7 last six-hour posts in order, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Josh McDaniels\""):
    lines[i]="            f'trend names \"Jaylon Johnson\", \"Cavs\" and \"#VERZUZ\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[i]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0059Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-seventh run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 90"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 14 more (2113355503279718485 left out of the second read, Not Found in the watch read this run; 2108062331095908717 Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
