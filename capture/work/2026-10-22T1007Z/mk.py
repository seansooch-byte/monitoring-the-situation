s=open('build_capture.py').read()
TN='three of the six top-ten US names with no posts attached in 0904Z: "Bellucci" (new), "#RespectMyanmarCulture" (one event with GMMTV ACCOUNTABILITY and #CreditOurHeritage, the Myanmar fan clubs asking GMMTV to credit Myanmar costumes) and "Warriors" (Warriors at Lakers, NBA opening week; one event with Luka, Yaxel, Lakers and Kessler); "Good Thursday" (a greeting), "GMMTV ACCOUNTABILITY" and "#CreditOurHeritage" (read in 0800Z) left for a later run'
R=[
("Build capture/2026/10/22/0904Z.json","Build capture/2026/10/22/1007Z.json"),
("work/2026-10-22T0904Z'","work/2026-10-22T1007Z'"),
("RUN_ID = '2026-10-22T0904Z'","RUN_ID = '2026-10-22T1007Z'"),
("STARTED = '2026-10-22T09:04:00Z'","STARTED = '2026-10-22T10:07:00Z'"),
("OBS_AT = '2026-10-22T09:04:00Z'","OBS_AT = '2026-10-22T10:07:00Z'"),
("READS_BEFORE = 819","READS_BEFORE = 799"),
("datetime(2026,10,22,9,7,tzinfo=timezone.utc).timestamp()  # 0904Z (","datetime(2026,10,22,10,10,tzinfo=timezone.utc).timestamp()  # 1007Z (0904Z used 09:07, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_is': 'repost_is.txt',"),
("'trend_kessler': 'trend_kessler.txt', 'trend_tyjerome': 'trend_tyjerome.txt', 'trend_lakers': 'trend_lakers.txt',","'trend_bellucci': 'trend_bellucci.txt', 'trend_myanmar': 'trend_myanmar.txt', 'trend_warriors': 'trend_warriors.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_is','repost'),"),
("('trend_kessler','trend.Walker Kessler'),('trend_tyjerome','trend.Ty Jerome'),('trend_lakers','trend.Lakers'),","('trend_bellucci','trend.Bellucci'),('trend_myanmar','trend.#RespectMyanmarCulture'),('trend_warriors','trend.Warriors'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0904Z.json') and '/22/' in _c: continue","if _c.endswith('1007Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T0800Z'","_last = '2026-10-22T0904Z'"),
("(this 09Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 437 long, so the 400 cap left out the 37 slowest-growing still-gaining posts and no cited post)",
 "(this 10Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 448 long, so the 400 cap left out the 48 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0904Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1007Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "my", "it" and "just", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "what", "the" and "is", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Walker Kessler','trend.Ty Jerome','trend.Lakers'): return 'sports'  # 0904Z",
 "        if str(_x) in ('trend.Warriors',): return 'sports'  # 1007Z: Warriors at Lakers (NBA opening week)\n        if str(_x) in ('trend.#RespectMyanmarCulture',): return 'entertainment'  # 1007Z: Myanmar fan clubs and GMMTV\n        if str(_x) in ('trend.Bellucci',): return 'internet'  # 1007Z: Monica Bellucci and Tim Burton meme\n        if str(_x) in ('trend.Walker Kessler','trend.Ty Jerome','trend.Lakers'): return 'sports'  # 0904Z"),
("but cut for the fiftieth run (the 06:00-11:00","but cut for the fifty-first run (the 06:00-11:00"),
("cut for the fifty-second run (the 06:00-11:00 UTC band allows up to 20 reads)'","cut for the fifty-third run (the 06:00-11:00 UTC band allows up to 20 reads)'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Bellucci\", \"#RespectMyanmarCulture\" and \"Warriors\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words what/the + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then the 11 first-hop left over and 15 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Overnight run (5:04 AM ET"):
    lines[i]="            f'Morning run (6:07 AM ET / 10:07 UTC Oct 22, the 10Z slot; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0904Z ended at 799, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 448 ids, so the 400 cap left out the 48 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Walker Kessler\""):
    lines[i]="            f'trend names \"Bellucci\", \"#RespectMyanmarCulture\" and \"Warriors\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[i]="            f'quote/repost words what/the + is (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0904Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-third run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-first run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: the 93"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 11 first-hop left over and the 15 unread second-hop posts first seen in that read (2113126269328236967 and 2108062331095908717, Not Found in earlier runs, not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
