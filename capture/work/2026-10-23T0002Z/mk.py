s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 2307Z: "Cavs" (new; the Cavaliers v 76ers game, the same event as the "Sixers", "76ers", "Mobley", "Donovan Mitchell" and "Harden" trends), "HAMZAH" (new) and "#LetEmKnow" (new); "Mario Hezonja" left for the budget; "Tom Skerritt" was attached in 2307Z, "Lindsey Graham" in 2107Z, "Marines" and "Top Gun" earlier'
R=[
("Build capture/2026/10/22/2307Z.json","Build capture/2026/10/23/0002Z.json"),
("work/2026-10-22T2307Z'","work/2026-10-23T0002Z'"),
("RUN_ID = '2026-10-22T2307Z'","RUN_ID = '2026-10-23T0002Z'"),
("STARTED = '2026-10-22T23:07:00Z'","STARTED = '2026-10-23T00:02:00Z'"),
("OBS_AT = '2026-10-22T23:07:00Z'","OBS_AT = '2026-10-23T00:02:00Z'"),
("READS_BEFORE = 529","READS_BEFORE = 1000"),
("datetime(2026,10,22,23,10,tzinfo=timezone.utc).timestamp()  # 2307Z (","datetime(2026,10,23,0,5,tzinfo=timezone.utc).timestamp()  # 0002Z (2307Z used 23:10, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_vanityfair': 'trend_vanityfair.txt', 'trend_skerritt': 'trend_skerritt.txt',","'trend_cavs': 'trend_cavs.txt', 'trend_hamzah': 'trend_hamzah.txt', 'trend_letemknow': 'trend_letemknow.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("    'trends_us': 'trends_us.txt',\n","    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',\n"),
("trends = parse_trends(raw['trends_us'], 'US')\n","trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')\n"),
("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-22T0001Z',[]))","sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_vanityfair','trend.Vanity Fair'),('trend_skerritt','trend.Tom Skerritt'),","('trend_cavs','trend.Cavs'),('trend_hamzah','trend.HAMZAH'),('trend_letemknow','trend.#LetEmKnow'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2307Z.json') and '/22/' in _c: continue","if _c.endswith('0002Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T2201Z'","_last = '2026-10-22T2307Z'"),
('\'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Vanity Fair',): return 'politics'  # 2307Z",
 "        if str(_x) in ('trend.Cavs',): return 'sports'  # 0002Z: Cavaliers v 76ers\n        if str(_x) in ('trend.Vanity Fair',): return 'politics'  # 2307Z"),
("but cut for the sixty-fourth run","but cut for the sixty-fifth run"),
("cut for the sixty-sixth run (kept","cut for the sixty-seventh run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/2307Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/0002Z.json'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Cavs\", \"HAMZAH\" and \"#LetEmKnow\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN.replace("'","\\'")+"); quote/repost words this/is + you (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (98 unread first-hop, most pointed-at first, then 23 second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Evening run (7:07 PM ET"):
    lines[i]="            f'Evening run (8:02 PM ET Oct 22 / 00:02 UTC Oct 23, the 00Z slot and the first run of the new UTC day; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the X day reset at 00:00 UTC), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 543 ids, so the 400 cap left out 143 slowest-growing posts (30 fourth-hour, 113 still-gaining) and no cited post; 4 reads); trends US and worldwide (2 reads); '"; hit+=1
  elif st.startswith("f'trend names \"Vanity Fair\""):
    lines[i]="            f'trend names \"Cavs\", \"HAMZAH\" and \"#LetEmKnow\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[i]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2307Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the sixty-seventh run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the sixty-fifth run, both for the budget; '"; hit+=1
  elif st.startswith("f'three screening reads by id: 100 then 1"):
    lines[i]="            f'two screening reads by id: 98 unread referenced, reply-parent and media-source posts, most pointed-at first (2108062331095908717 Not Found again; 2113355503279718485 left out, Not Found in 2307Z), then 23 second-hop; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
