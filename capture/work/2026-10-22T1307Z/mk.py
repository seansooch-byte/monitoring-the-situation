s=open('build_capture.py').read()
SH='#中国上海停止纵容姚润昊'
TN='three of the top-ten US names with no posts attached in 1201Z: "Happy Birthday Doc" (new; Christopher Lloyd, Doc Brown in Back to the Future, turns 88; one event with "Great Scott" at 20th), "Luka" (Warriors at Lakers, NBA opening week, attached in 1107Z; one event with "Yaxel") and "Kidnapped" (attached in 1107Z; mostly the California man who said ICE kidnapped his wife and was charged with her murder); "Good Thursday", "Happy Friday Eve", "Thirsty Thursday" and "#thursdayvibes" (greetings), "Yaxel" (the same game as Luka) left out; "#PapergamesTramplesHumanRights" and "'+SH+'" were attached in 1201Z'
R=[
("Build capture/2026/10/22/1201Z.json","Build capture/2026/10/22/1307Z.json"),
("work/2026-10-22T1201Z'","work/2026-10-22T1307Z'"),
("RUN_ID = '2026-10-22T1201Z'","RUN_ID = '2026-10-22T1307Z'"),
("STARTED = '2026-10-22T12:01:00Z'","STARTED = '2026-10-22T13:07:00Z'"),
("OBS_AT = '2026-10-22T12:01:00Z'","OBS_AT = '2026-10-22T13:07:00Z'"),
("READS_BEFORE = 749","READS_BEFORE = 729"),
("datetime(2026,10,22,12,4,tzinfo=timezone.utc).timestamp()  # 1201Z (","datetime(2026,10,22,13,12,tzinfo=timezone.utc).timestamp()  # 1307Z (1201Z used 12:04, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_papergames': 'trend_papergames.txt', 'trend_shanghai': 'trend_shanghai.txt', 'trend_gmmtv': 'trend_gmmtv.txt',","'trend_doc': 'trend_doc.txt', 'trend_luka': 'trend_luka.txt', 'trend_kidnapped': 'trend_kidnapped.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_papergames','trend.#PapergamesTramplesHumanRights'),('trend_shanghai','trend."+SH+"'),('trend_gmmtv','trend.GMMTV ACCOUNTABILITY'),","('trend_doc','trend.Happy Birthday Doc'),('trend_luka','trend.Luka'),('trend_kidnapped','trend.Kidnapped'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1201Z.json') and '/22/' in _c: continue","if _c.endswith('1307Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T1107Z'","_last = '2026-10-22T1201Z'"),
("(this 12Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 519 long, so the 400 cap left out the 119 slowest-growing still-gaining and fourth-hour posts and no cited post)",
 "(this 13Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 464 long, so the 400 cap left out the 64 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1201Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1307Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.#PapergamesTramplesHumanRights','trend."+SH+"'): return 'gaming'  # 1201Z",
 "        if str(_x) in ('trend.Happy Birthday Doc',): return 'entertainment'  # 1307Z: Christopher Lloyd (Doc Brown) birthday\n        if str(_x) in ('trend.#PapergamesTramplesHumanRights','trend."+SH+"'): return 'gaming'  # 1201Z"),
("but cut for the fifty-third run","but cut for the fifty-fourth run"),
("cut for the fifty-fifth run (kept","cut for the fifty-sixth run (kept"),
("per the scheduling instruction","to pace the day's budget"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Happy Birthday Doc\", \"Luka\" and \"Kidnapped\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then the 8 that did not fit); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (8:01 AM ET"):
    lines[i]="            f'Morning run (9:07 AM ET / 13:07 UTC Oct 22, the 13Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the day\\'s budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1201Z ended at 729, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 464 ids, so the 400 cap left out the 64 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"#PapergamesTramplesHumanRights\""):
    lines[i]="            f'trend names \"Happy Birthday Doc\", \"Luka\" and \"Kidnapped\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[i]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1201Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-sixth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-fourth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 8 first-hop that did not fit (2108062331095908717 came back Not Found as an expansion again; 21 second- and third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
