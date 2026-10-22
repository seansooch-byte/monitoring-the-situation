s=open('build_capture.py').read()
TN='three of the seven top-ten US names with no posts attached in 1007Z: "Eala" (new; Alex Eala lost to Diana Shnaider at the Ningbo Open), "Kidnapped" (new; several stories, mostly the California man who said ICE kidnapped his wife and was charged with her murder) and "Luka" (Warriors at Lakers, NBA opening week; one event with Yaxel and Lakers); "Good Thursday" and "Happy Friday Eve" (greetings), "Yaxel" and "Lakers" (the same game as Luka), "#CreditOurHeritage" and "GMMTV ACCOUNTABILITY" (the Myanmar fan-club campaign attached in 1007Z as #RespectMyanmarCulture) left out'
R=[
("Build capture/2026/10/22/1007Z.json","Build capture/2026/10/22/1107Z.json"),
("work/2026-10-22T1007Z'","work/2026-10-22T1107Z'"),
("RUN_ID = '2026-10-22T1007Z'","RUN_ID = '2026-10-22T1107Z'"),
("STARTED = '2026-10-22T10:07:00Z'","STARTED = '2026-10-22T11:07:00Z'"),
("OBS_AT = '2026-10-22T10:07:00Z'","OBS_AT = '2026-10-22T11:07:00Z'"),
("READS_BEFORE = 799","READS_BEFORE = 779"),
("datetime(2026,10,22,10,10,tzinfo=timezone.utc).timestamp()  # 1007Z (","datetime(2026,10,22,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (1007Z used 10:10, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',"),
("'repost_is': 'repost_is.txt',","'repost_and': 'repost_and.txt',"),
("'trend_bellucci': 'trend_bellucci.txt', 'trend_myanmar': 'trend_myanmar.txt', 'trend_warriors': 'trend_warriors.txt',","'trend_eala': 'trend_eala.txt', 'trend_kidnapped': 'trend_kidnapped.txt', 'trend_luka': 'trend_luka.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_is','repost'),","('quote_this','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_bellucci','trend.Bellucci'),('trend_myanmar','trend.#RespectMyanmarCulture'),('trend_warriors','trend.Warriors'),","('trend_eala','trend.Eala'),('trend_kidnapped','trend.Kidnapped'),('trend_luka','trend.Luka'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1007Z.json') and '/22/' in _c: continue","if _c.endswith('1107Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T0904Z'","_last = '2026-10-22T1007Z'"),
("(this 10Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 448 long, so the 400 cap left out the 48 slowest-growing still-gaining posts and no cited post)",
 "(this 11Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 446 long, so the 400 cap left out the 46 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1007Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1107Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "what", "the" and "is", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "this", "you" and "and", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Warriors',): return 'sports'  # 1007Z",
 "        if str(_x) in ('trend.Eala','trend.Luka'): return 'sports'  # 1107Z: Alex Eala at the Ningbo Open; Warriors at Lakers\n        if str(_x) in ('trend.Kidnapped',): return 'politics'  # 1107Z: mostly the ICE-kidnapping claim and murder charge\n        if str(_x) in ('trend.Warriors',): return 'sports'  # 1007Z"),
("but cut for the fifty-first run (the 06:00-11:00","but cut for the fifty-second run (the 06:00-11:00"),
("cut for the fifty-third run (the 06:00-11:00 UTC band allows up to 20 reads)'","cut for the fifty-fourth run (the 06:00-11:00 UTC band allows up to 20 reads)'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Eala\", \"Kidnapped\" and \"Luka\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words this/you + and (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (87 unread referenced first-hop, then 21 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (6:07 AM ET"):
    lines[i]="            f'Morning run (7:07 AM ET / 11:07 UTC Oct 22, the 11Z slot; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1007Z ended at 779, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 446 ids, so the 400 cap left out the 46 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Bellucci\""):
    lines[i]="            f'trend names \"Eala\", \"Kidnapped\" and \"Luka\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[i]="            f'quote/repost words this/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1007Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-fourth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-second run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 87 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 21 unread second-hop posts first seen in that read (1696895709092454422 and 2108062331095908717 came back Not Found as expansions and were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
