s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 1307Z: "RIP Ron" (new; former New York Rangers forward Ron Duguay has died; one event with "Ron Duguay" at 11th), "WNBA" (new; WNBA Finals, the teams leaving the court for the national anthem and the league fine, and posts on fans removed from the Finals) and "#PapergamesTramplesHumanRights" (attached in 1201Z, not in 1307Z; one event with "#中国上海停止纵容姚润昊", the Papergames / Love and Deepspace harassment campaign; attached posts small); "Good Thursday", "#thursdayvibes" and "Happy Friday Eve" (greetings) left out; "Luka", "Yaxel" and "Kidnapped" were attached in 1307Z'
R=[
("Build capture/2026/10/22/1307Z.json","Build capture/2026/10/22/1409Z.json"),
("work/2026-10-22T1307Z'","work/2026-10-22T1409Z'"),
("RUN_ID = '2026-10-22T1307Z'","RUN_ID = '2026-10-22T1409Z'"),
("STARTED = '2026-10-22T13:07:00Z'","STARTED = '2026-10-22T14:09:00Z'"),
("OBS_AT = '2026-10-22T13:07:00Z'","OBS_AT = '2026-10-22T14:09:00Z'"),
("READS_BEFORE = 729","READS_BEFORE = 709"),
("datetime(2026,10,22,13,12,tzinfo=timezone.utc).timestamp()  # 1307Z (","datetime(2026,10,22,14,13,tzinfo=timezone.utc).timestamp()  # 1409Z (1307Z used 13:12, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_doc': 'trend_doc.txt', 'trend_luka': 'trend_luka.txt', 'trend_kidnapped': 'trend_kidnapped.txt',","'trend_ripron': 'trend_ripron.txt', 'trend_wnba': 'trend_wnba.txt', 'trend_papergames': 'trend_papergames.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_doc','trend.Happy Birthday Doc'),('trend_luka','trend.Luka'),('trend_kidnapped','trend.Kidnapped'),","('trend_ripron','trend.RIP Ron'),('trend_wnba','trend.WNBA'),('trend_papergames','trend.#PapergamesTramplesHumanRights'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1307Z.json') and '/22/' in _c: continue","if _c.endswith('1409Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T1201Z'","_last = '2026-10-22T1307Z'"),
("(this 13Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 464 long, so the 400 cap left out the 64 slowest-growing still-gaining posts and no cited post)",
 "(this 14Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 475 long, so the 400 cap left out the 75 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1307Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1409Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Happy Birthday Doc',): return 'entertainment'  # 1307Z",
 "        if str(_x) in ('trend.RIP Ron','trend.WNBA'): return 'sports'  # 1409Z: Ron Duguay (Rangers) death; WNBA Finals\n        if str(_x) in ('trend.Happy Birthday Doc',): return 'entertainment'  # 1307Z"),
("but cut for the fifty-fourth run","but cut for the fifty-fifth run"),
("cut for the fifty-sixth run (kept","cut for the fifty-seventh run (kept"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"RIP Ron\", \"WNBA\" and \"#PapergamesTramplesHumanRights\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words this/is + you (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then 20 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (9:07 AM ET"):
    lines[i]="            f'Morning run (10:09 AM ET / 14:09 UTC Oct 22, the 14Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1307Z ended at 709, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 475 ids, so the 400 cap left out the 75 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Happy Birthday Doc\""):
    lines[i]="            f'trend names \"RIP Ron\", \"WNBA\" and \"#PapergamesTramplesHumanRights\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[i]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1307Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-seventh run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-fifth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 20 more (2108062331095908717 came back Not Found again; 20 second- and third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
