s=open('build_capture.py').read()
R=[
("Build capture/2026/10/22/0706Z.json","Build capture/2026/10/22/0800Z.json"),
("work/2026-10-22T0706Z'","work/2026-10-22T0800Z'"),
("RUN_ID = '2026-10-22T0706Z'","RUN_ID = '2026-10-22T0800Z'"),
("STARTED = '2026-10-22T07:06:00Z'","STARTED = '2026-10-22T08:00:00Z'"),
("OBS_AT = '2026-10-22T07:06:00Z'","OBS_AT = '2026-10-22T08:00:00Z'"),
("READS_BEFORE = 859","READS_BEFORE = 839"),
("datetime(2026,10,22,7,10,tzinfo=timezone.utc).timestamp()  # 0706Z (","datetime(2026,10,22,8,4,tzinfo=timezone.utc).timestamp()  # 0800Z (0706Z used 07:10, "),
("'quote_the': 'quote_the.txt', 'quote_is': 'quote_is.txt',","'quote_this': 'quote_this.txt', 'quote_and': 'quote_and.txt',"),
("'repost_you': 'repost_you.txt',","'repost_that': 'repost_that.txt',"),
("'trend_warriors': 'trend_warriors.txt', 'trend_draymond': 'trend_draymond.txt', 'trend_lakeshow': 'trend_lakeshow.txt',","'trend_creditourheritage': 'trend_creditourheritage.txt', 'trend_gmmtv': 'trend_gmmtv.txt', 'trend_luka': 'trend_luka.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_this','quote'),('quote_and','quote'),('repost_that','repost'),"),
("('trend_warriors','trend.Warriors'),('trend_draymond','trend.Draymond'),('trend_lakeshow','trend.#LakeShow'),","('trend_creditourheritage','trend.#CreditOurHeritage'),('trend_gmmtv','trend.GMMTV ACCOUNTABILITY'),('trend_luka','trend.Luka'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0706Z.json') and '/22/' in _c: continue","if _c.endswith('0800Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T0607Z'","_last = '2026-10-22T0706Z'"),
("(this 07Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 440 long, so the 400 cap left out the 40 slowest-growing still-gaining posts and no cited post)",
 "(this 08Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 503 long, so the 400 cap left out the 103 slowest-growing posts of the last 24 hours and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0706Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0800Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "the", "is" and "you", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "this", "and" and "that", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Warriors','trend.Draymond','trend.#LakeShow'): return 'sports'  # 0706Z",
 "        if str(_x) in ('trend.#CreditOurHeritage','trend.GMMTV ACCOUNTABILITY'): return 'entertainment'  # 0800Z: Myanmar fan clubs asking GMMTV (Scarlet Heart TH) to credit Myanmar costumes\n        if str(_x) in ('trend.Luka',): return 'sports'  # 0800Z\n        if str(_x) in ('trend.Warriors','trend.Draymond','trend.#LakeShow'): return 'sports'  # 0706Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
TN='three of the top-ten US names with no posts attached in 0706Z: "#CreditOurHeritage" and "GMMTV ACCOUNTABILITY" (one event: Myanmar fan clubs asking GMMTV to credit Myanmar heritage costumes in Scarlet Heart TH) and "Luka" (Warriors at Lakers; last attached in 0408Z); Lakers in 0607Z, Yaxel and Kessler in 0408Z, Ty Jerome in 0502Z left for a later run'
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"#CreditOurHeritage\", \"GMMTV ACCOUNTABILITY\" and \"Luka\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words this/and + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 18 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Overnight run (3:06 AM ET"):
    lines[i]="            f'Overnight run (4:00 AM ET / 08:00 UTC Oct 22, the 08Z slot; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0706Z ended at 839, so no read went elsewhere in between), parallel batches of up to 11, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 503 ids, so the 400 cap left out the 103 slowest-growing posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Warriors\""):
    lines[i]="            f'trend names \"#CreditOurHeritage\", \"GMMTV ACCOUNTABILITY\" and \"Luka\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/is"):
    lines[i]="            f'quote/repost words this/and + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0706Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-first run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the forty-ninth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 18 remaining unread referenced posts; second-hop posts first seen in the screening reads left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
