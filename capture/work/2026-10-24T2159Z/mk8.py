s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1907Z: "Marcel Reed" (fourth) and "Dijon Lee" (eighth), one event (Alabama v Texas A&M: Dijon Lee Jr. returning a Marcel Reed interception for a touchdown), and "Kavanagh" (ninth; Lone\'er Kavanagh knocking out Ramazan Temirov in round one at UFC 333, the same card as "#UFC333"); "#UFC333" (second) and "Jason Beck" (third) had posts attached in 1907Z, "Hoover" (sixth) and "#iufb" (seventh) are the Indiana v Michigan event attached in 1907Z under "Josh Hoover", "Michigan" (first) and "Texas Tech" (fifth) had posts attached in 1807Z, and "Tommy Carr" (tenth) was not read to keep to about 20 reads'
TN='three of the top-ten US names with no posts attached in 2007Z: "Merab" (third) and "Petr Yan" (fourth), one event (UFC 333 main event: Petr Yan beating Merab Dvalishvili by unanimous decision to keep the bantamweight title, the same card as "#UFC333"), and "Indiana" (seventh; Indiana beating Michigan in overtime, the same event as "Hoover" (ninth) and "#iufb" (tenth), attached in 1907Z under "Josh Hoover"); "#UFC333" (first) and "Marcel Reed" (fifth) had posts attached in 2007Z, "Jason Beck" (sixth) in 1907Z, and "Michigan" (second) and "Texas Tech" (eighth) in 1807Z'
R=[
("Build capture/2026/10/24/2007Z.json","Build capture/2026/10/24/2103Z.json"),
("work/2026-10-24T2007Z'","work/2026-10-24T2103Z'"),
("RUN_ID = '2026-10-24T2007Z'","RUN_ID = '2026-10-24T2103Z'"),
("STARTED = '2026-10-24T20:07:00Z'","STARTED = '2026-10-24T21:03:00Z'"),
("OBS_AT = '2026-10-24T20:07:00Z'","OBS_AT = '2026-10-24T21:03:00Z'"),
("READS_BEFORE = 590","READS_BEFORE = 570"),
("datetime(2026,10,24,20,9,tzinfo=timezone.utc).timestamp()  # 2007Z (1907Z used 19:08, ","datetime(2026,10,24,21,5,tzinfo=timezone.utc).timestamp()  # 2103Z (2007Z used 20:09, 1907Z used 19:08, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_marcelreed': 'trend_marcelreed.txt', 'trend_dijonlee': 'trend_dijonlee.txt', 'trend_kavanagh': 'trend_kavanagh.txt',","'trend_merab': 'trend_merab.txt', 'trend_petryan': 'trend_petryan.txt', 'trend_indiana': 'trend_indiana.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_marcelreed','trend.Marcel Reed'),('trend_dijonlee','trend.Dijon Lee'),('trend_kavanagh','trend.Kavanagh'),","('trend_merab','trend.Merab'),('trend_petryan','trend.Petr Yan'),('trend_indiana','trend.Indiana'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2007Z.json') and '/24/' in _c: continue","if _c.endswith('2103Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T1907Z'","_last = '2026-10-24T2007Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("one hundred and eighth run","one hundred and ninth run"),
("one hundred and tenth run","one hundred and eleventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/2007Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/2103Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (2007Z: none read)","# 5) request picks (2103Z: none read)"),
("two screening reads by id (96 unread referenced posts, most pointed-at first, then the 17 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 26 second-hop and remaining posts in the second read)"),
("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)"),
('trend names "Marcel Reed", "Dijon Lee" and "Kavanagh" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Merab", "Petr Yan" and "Indiana" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 20Z run is a fourth hour, so the rest of the last 24 hours followed, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 591 long, so the 400 cap left out the 29 last six-hour posts, the 135 slowest-growing still-gaining posts and 27 of the 29 rest-of-24-hour posts, and no cited post)",
 "(this 21Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 566 long, so the 400 cap left out the 43 last six-hour posts and the 123 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x) in ('trend.Marcel Reed','trend.Dijon Lee','trend.Kavanagh'): return 'sports'  # 2007Z: Alabama v Texas A&M, UFC 333\n",
 "        if str(_x) in ('trend.Marcel Reed','trend.Dijon Lee','trend.Kavanagh'): return 'sports'  # 2007Z: Alabama v Texas A&M, UFC 333\n        if str(_x) in ('trend.Merab','trend.Petr Yan','trend.Indiana'): return 'sports'  # 2103Z: UFC 333 main event, Indiana v Michigan\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Afternoon run (4:07 PM ET"):
    lines[k]="            f'Late-afternoon run (5:03 PM ET Oct 24 / 21:03 UTC Oct 24, the 21Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2007Z ended at 570, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 566 ids, so the 400 cap left out the 43 last six-hour posts and the 123 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Marcel Reed\""):
    lines[k]="            f'trend names \"Merab\", \"Petr Yan\" and \"Indiana\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[k]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2007Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 96"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 26 in the second read (the 10 left from the first list and the second-hop posts they led to; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again in the first read, as in 1105Z through 2007Z, so it was not read in the second; 2113507644690583691 returned Authorization Error in the second; 9 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
