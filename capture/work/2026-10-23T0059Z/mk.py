s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0002Z: "Josh McDaniels" (new; the Patriots at Bears Thursday night game, the same event as the "Patriots", "Pats", "Kyler Gordon", "Luther Burden", "#DaBears", "#NEvsCHI" and "Swift" trends), "#911onABC" (new; the ABC 9-1-1 episode) and "Swift" (new; D\'Andre Swift\'s touchdown in the same Patriots at Bears game; its stream also carries Taylor Swift posts); "Cavs", "Sixers", "76ers", "Harden" and "#LetEmKnow" were attached in 0002Z; "Kyler Gordon", "Patriots" and "Luther Burden" left as the same event'
R=[
("Build capture/2026/10/23/0002Z.json","Build capture/2026/10/23/0059Z.json"),
("work/2026-10-23T0002Z'","work/2026-10-23T0059Z'"),
("RUN_ID = '2026-10-23T0002Z'","RUN_ID = '2026-10-23T0059Z'"),
("STARTED = '2026-10-23T00:02:00Z'","STARTED = '2026-10-23T00:59:00Z'"),
("OBS_AT = '2026-10-23T00:02:00Z'","OBS_AT = '2026-10-23T00:59:00Z'"),
("READS_BEFORE = 1000","READS_BEFORE = 979"),
("datetime(2026,10,23,0,5,tzinfo=timezone.utc).timestamp()  # 0002Z (","datetime(2026,10,23,1,1,tzinfo=timezone.utc).timestamp()  # 0059Z (0002Z used 00:05, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_cavs': 'trend_cavs.txt', 'trend_hamzah': 'trend_hamzah.txt', 'trend_letemknow': 'trend_letemknow.txt',","'trend_mcdaniels': 'trend_mcdaniels.txt', 'trend_911onabc': 'trend_911onabc.txt', 'trend_swift': 'trend_swift.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',\n","    'trends_us': 'trends_us.txt',\n"),
("trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')\n","trends = parse_trends(raw['trends_us'], 'US')\n"),
("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))","sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-23T0002Z',[]))"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_cavs','trend.Cavs'),('trend_hamzah','trend.HAMZAH'),('trend_letemknow','trend.#LetEmKnow'),","('trend_mcdaniels','trend.Josh McDaniels'),('trend_911onabc','trend.#911onABC'),('trend_swift','trend.Swift'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0002Z.json') and '/23/' in _c: continue","if _c.endswith('0059Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-22T2307Z'","_last = '2026-10-23T0002Z'"),
('\'2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Cavs',): return 'sports'  # 0002Z",
 "        if str(_x) in ('trend.Josh McDaniels','trend.Swift'): return 'sports'  # 0059Z: Patriots at Bears TNF\n        if str(_x) in ('trend.#911onABC',): return 'entertainment'  # 0059Z: ABC 9-1-1 episode\n        if str(_x) in ('trend.Cavs',): return 'sports'  # 0002Z"),
("but cut for the sixty-fifth run","but cut for the sixty-sixth run"),
("cut for the sixty-seventh run (kept","cut for the sixty-eighth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0002Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0059Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Josh McDaniels\", \"#911onABC\" and \"Swift\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (90 unread first-hop, most pointed-at first, then 20 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Evening run (8:02 PM ET"):
    lines[i]="            f'Evening run (8:59 PM ET Oct 22 / 00:59 UTC Oct 23, the 01Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0002Z ended at 979, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 509 ids, so the 400 cap left out 106 slowest-growing still-gaining posts and the 3 last six-hour posts in order, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Cavs\""):
    lines[i]="            f'trend names \"Josh McDaniels\", \"#911onABC\" and \"Swift\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[i]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0002Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-eighth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-sixth run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 98"):
    lines[i]="            f'two screening reads by id: 90 unread referenced, reply-parent and media-source posts, most pointed-at first, then 20 second-hop (2108062331095908717 and 2113355503279718485 left out of the second read, Not Found in earlier runs); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
