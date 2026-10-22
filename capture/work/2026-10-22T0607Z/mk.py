s=open('build_capture.py').read()
R=[
("Build capture/2026/10/22/0502Z.json","Build capture/2026/10/22/0607Z.json"),
("work/2026-10-22T0502Z'","work/2026-10-22T0607Z'"),
("RUN_ID = '2026-10-22T0502Z'","RUN_ID = '2026-10-22T0607Z'"),
("STARTED = '2026-10-22T05:02:00Z'","STARTED = '2026-10-22T06:07:00Z'"),
("OBS_AT = '2026-10-22T05:02:00Z'","OBS_AT = '2026-10-22T06:07:00Z'"),
("READS_BEFORE = 899","READS_BEFORE = 879"),
("datetime(2026,10,22,5,4,tzinfo=timezone.utc).timestamp()  # 0502Z (","datetime(2026,10,22,6,10,tzinfo=timezone.utc).timestamp()  # 0607Z (0502Z used 05:04, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_steph': 'trend_steph.txt', 'trend_tyjerome': 'trend_tyjerome.txt', 'trend_giannis': 'trend_giannis.txt',","'trend_lakers': 'trend_lakers.txt', 'trend_blazers': 'trend_blazers.txt', 'trend_suns': 'trend_suns.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_steph','trend.Steph'),('trend_tyjerome','trend.Ty Jerome'),('trend_giannis','trend.Giannis'),","('trend_lakers','trend.Lakers'),('trend_blazers','trend.Blazers'),('trend_suns','trend.Suns'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0502Z.json') and '/22/' in _c: continue","if _c.endswith('0607Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run; kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42)","rotation: culture/sports/online read this run; the 06:00-11:00 UTC band allows up to 20 reads)"),
("(kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42); last read in {_last}","(the 06:00-11:00 UTC band allows up to 20 reads); last read in {_last}"),
("_last = '2026-10-22T0408Z'","_last = '2026-10-22T0502Z'"),
("cut for the forty-sixth run (kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42; four-hour desks are cut first)","cut for the forty-seventh run (the 06:00-11:00 UTC band allows up to 20 reads; four-hour desks are cut first)"),
("cut for the forty-eighth run (kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42)","cut for the forty-ninth run (the 06:00-11:00 UTC band allows up to 20 reads)"),
("'cut for the read budget (kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42)'","'cut for the read budget (the 06:00-11:00 UTC band allows up to 20 reads)'"),
("(this 05Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 429 long, so the 400 cap left out the 29 slowest-growing still-gaining posts and no cited post)",
 "(this 06Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 430 long, so the 400 cap left out the 30 slowest-growing still-gaining posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0502Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/0607Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Steph','trend.Ty Jerome','trend.Giannis'): return 'sports'  # 0502Z",
 "        if str(_x) in ('trend.Lakers','trend.Blazers','trend.Suns'): return 'sports'  # 0607Z: NBA opening week (Warriors at Lakers; Blazers; Suns)\n        if str(_x) in ('trend.Steph','trend.Ty Jerome','trend.Giannis'): return 'sports'  # 0502Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
TN='three of the top-ten US names with no posts attached in 0502Z: "Lakers" (Warriors at Lakers; Luka, Warriors, #LakeShow, Draymond and Steph are the same game), "Blazers" and "Suns" (NBA opening week; Suns last read in 0300Z); Yaxel had posts attached in 0408Z; Ty Jerome had posts attached in 0502Z'
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Lakers\", \"Blazers\" and \"Suns\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 21 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Night run (1:02 AM ET"):
    lines[i]="            f'Overnight run (2:07 AM ET / 06:07 UTC Oct 22, the 06Z slot; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0502Z ended at 879, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 430 ids, so the 400 cap left out the 30 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Steph\""):
    lines[i]="            f'trend names \"Lakers\", \"Blazers\" and \"Suns\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my + it"):
    lines[i]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0502Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the forty-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the forty-seventh run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (99 returned; Not Found for 2112850676569215081 and for 2108062331095908717, Not Found in earlier runs), then the 21 remaining unread referenced posts (21 returned); second-hop posts first seen in the screening reads left unread for the budget; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
