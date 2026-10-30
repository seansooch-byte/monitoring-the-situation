s=open('build_capture.py').read()
TN='three of the five top-ten US names with no posts attached in 0800Z: "Walker Kessler" (last attached as Kessler in 0408Z), "Ty Jerome" (last attached in 0502Z) and "Lakers" (last attached in 0607Z), all Warriors at Lakers (NBA opening week); Warriors and #LakeShow (read in 0706Z) left for a later run'
R=[
("Build capture/2026/10/22/0800Z.json","Build capture/2026/10/22/0904Z.json"),
("work/2026-10-22T0800Z'","work/2026-10-22T0904Z'"),
("RUN_ID = '2026-10-22T0800Z'","RUN_ID = '2026-10-22T0904Z'"),
("STARTED = '2026-10-22T08:00:00Z'","STARTED = '2026-10-22T09:04:00Z'"),
("OBS_AT = '2026-10-22T08:00:00Z'","OBS_AT = '2026-10-22T09:04:00Z'"),
("READS_BEFORE = 839","READS_BEFORE = 819"),
("datetime(2026,10,22,8,4,tzinfo=timezone.utc).timestamp()  # 0800Z (","datetime(2026,10,22,9,7,tzinfo=timezone.utc).timestamp()  # 0904Z (0800Z used 08:04, "),
("'quote_this': 'quote_this.txt', 'quote_and': 'quote_and.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_that': 'repost_that.txt',","'repost_just': 'repost_just.txt',"),
("'trend_creditourheritage': 'trend_creditourheritage.txt', 'trend_gmmtv': 'trend_gmmtv.txt', 'trend_luka': 'trend_luka.txt',","'trend_kessler': 'trend_kessler.txt', 'trend_tyjerome': 'trend_tyjerome.txt', 'trend_lakers': 'trend_lakers.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_and','quote'),('repost_that','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_just','repost'),"),
("('trend_creditourheritage','trend.#CreditOurHeritage'),('trend_gmmtv','trend.GMMTV ACCOUNTABILITY'),('trend_luka','trend.Luka'),","('trend_kessler','trend.Walker Kessler'),('trend_tyjerome','trend.Ty Jerome'),('trend_lakers','trend.Lakers'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0800Z.json') and '/22/' in _c: continue","if _c.endswith('0904Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T0706Z'","_last = '2026-10-22T0800Z'"),
("(this 08Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 503 long, so the 400 cap left out the 103 slowest-growing posts of the last 24 hours and no cited post)",
 "(this 09Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 437 long, so the 400 cap left out the 37 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0800Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0904Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "this", "and" and "that", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "my", "it" and "just", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.#CreditOurHeritage','trend.GMMTV ACCOUNTABILITY'): return 'entertainment'  # 0800Z",
 "        if str(_x) in ('trend.Walker Kessler','trend.Ty Jerome','trend.Lakers'): return 'sports'  # 0904Z: Warriors at Lakers (NBA opening week)\n        if str(_x) in ('trend.#CreditOurHeritage','trend.GMMTV ACCOUNTABILITY'): return 'entertainment'  # 0800Z"),
("cut for the forty-eighth run (the 06:00-11:00","cut for the fiftieth run (the 06:00-11:00"),
("cut for the fiftieth run (the 06:00-11:00 UTC band allows up to 20 reads)'","cut for the fifty-second run (the 06:00-11:00 UTC band allows up to 20 reads)'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Walker Kessler\", \"Ty Jerome\" and \"Lakers\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words my/it + just (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (93 unread referenced first-hop, then 15 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Overnight run (4:00 AM ET"):
    lines[i]="            f'Overnight run (5:04 AM ET / 09:04 UTC Oct 22, the 09Z slot; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0800Z ended at 819, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 437 ids, so the 400 cap left out the 37 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"#CreditOurHeritage\""):
    lines[i]="            f'trend names \"Walker Kessler\", \"Ty Jerome\" and \"Lakers\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/and"):
    lines[i]="            f'quote/repost words my/it + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0800Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-second run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fiftieth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: the 93 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 15 unread second-hop posts first seen in that read (2113126269328236967 and 2108062331095908717, Not Found, not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
