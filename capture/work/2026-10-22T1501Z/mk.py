s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 1409Z: "Louise Lucas" (new; Virginia state Senator L. Louise Lucas arrested on federal racketeering, money laundering and marijuana distribution charges), "Lindsey Graham" (new; men saying they were paid for sex by Lindsey Graham, around a documentary; posts that describe one of them as a minor were left out under the minors rule) and "#NINGNINGShines24ever" (new; aespa member Ningning birthday; one event with "#닝닝의생일_민족의영광" at 4th; attached posts small); "Good Thursday" (greeting) left out; "Kidnapped" (no posts attached in 1409Z) not read for the budget; "Luka", "Ron Duguay", "Yaxel" and "RIP Ron" were attached in 1409Z'
R=[
("Build capture/2026/10/22/1409Z.json","Build capture/2026/10/22/1501Z.json"),
("work/2026-10-22T1409Z'","work/2026-10-22T1501Z'"),
("RUN_ID = '2026-10-22T1409Z'","RUN_ID = '2026-10-22T1501Z'"),
("STARTED = '2026-10-22T14:09:00Z'","STARTED = '2026-10-22T15:01:00Z'"),
("OBS_AT = '2026-10-22T14:09:00Z'","OBS_AT = '2026-10-22T15:01:00Z'"),
("READS_BEFORE = 709","READS_BEFORE = 689"),
("datetime(2026,10,22,14,13,tzinfo=timezone.utc).timestamp()  # 1409Z (","datetime(2026,10,22,15,6,tzinfo=timezone.utc).timestamp()  # 1501Z (1409Z used 14:13, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_ripron': 'trend_ripron.txt', 'trend_wnba': 'trend_wnba.txt', 'trend_papergames': 'trend_papergames.txt',","'trend_lucas': 'trend_lucas.txt', 'trend_graham': 'trend_graham.txt', 'trend_ningning': 'trend_ningning.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_ripron','trend.RIP Ron'),('trend_wnba','trend.WNBA'),('trend_papergames','trend.#PapergamesTramplesHumanRights'),","('trend_lucas','trend.Louise Lucas'),('trend_graham','trend.Lindsey Graham'),('trend_ningning','trend.#NINGNINGShines24ever'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1409Z.json') and '/22/' in _c: continue","if _c.endswith('1501Z.json') and '/22/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T1307Z'","_last = '2026-10-22T1409Z'"),
('\'2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.RIP Ron','trend.WNBA'): return 'sports'  # 1409Z",
 "        if str(_x) in ('trend.Louise Lucas','trend.Lindsey Graham'): return 'politics'  # 1501Z: Virginia state senator arrested; Graham allegations\n        if str(_x) in ('trend.#NINGNINGShines24ever',): return 'music'  # 1501Z: aespa Ningning birthday\n        if str(_x) in ('trend.RIP Ron','trend.WNBA'): return 'sports'  # 1409Z"),
("but cut for the fifty-fifth run","but cut for the fifty-sixth run"),
("cut for the fifty-seventh run (kept","cut for the fifty-eighth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1409Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1501Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Louise Lucas\", \"Lindsey Graham\" and \"#NINGNINGShines24ever\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, most pointed-at first, then 3 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (10:09 AM ET"):
    lines[i]="            f'Morning run (11:01 AM ET / 15:01 UTC Oct 22, the 15Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1409Z ended at 689, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 482 ids, so the 400 cap left out the 82 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"RIP Ron\""):
    lines[i]="            f'trend names \"Louise Lucas\", \"Lindsey Graham\" and \"#NINGNINGShines24ever\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[i]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1409Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-eighth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-sixth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 3 more (2108062331095908717 came back Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
