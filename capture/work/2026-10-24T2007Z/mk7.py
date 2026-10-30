s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1807Z, one per event: "Josh Hoover" (fourth; Indiana quarterback in Indiana v Michigan, one event with "#iufb", eighth), "Chelsea" (sixth; Tottenham beating Chelsea, one event with "#COYS", eleventh, and "Tottenham", twelfth) and "Volkov" (ninth; Alexander Volkov winning by decision at UFC 333); "Michigan" (first), "Jason Beck" (third), "Texas Tech" (fifth) and "Malachi Toney" (seventh) had posts attached in 1807Z, "#UFC333" (second) in 1505Z, and "Tommy Carr" (tenth) was not read to keep to about 20 reads'
TN='three of the top-ten US names with no posts attached in 1907Z: "Marcel Reed" (fourth) and "Dijon Lee" (eighth), one event (Alabama v Texas A&M: Dijon Lee Jr. returning a Marcel Reed interception for a touchdown), and "Kavanagh" (ninth; Lone\'er Kavanagh knocking out Ramazan Temirov in round one at UFC 333, the same card as "#UFC333"); "#UFC333" (second) and "Jason Beck" (third) had posts attached in 1907Z, "Hoover" (sixth) and "#iufb" (seventh) are the Indiana v Michigan event attached in 1907Z under "Josh Hoover", "Michigan" (first) and "Texas Tech" (fifth) had posts attached in 1807Z, and "Tommy Carr" (tenth) was not read to keep to about 20 reads'
R=[
("Build capture/2026/10/24/1907Z.json","Build capture/2026/10/24/2007Z.json"),
("work/2026-10-24T1907Z'","work/2026-10-24T2007Z'"),
("RUN_ID = '2026-10-24T1907Z'","RUN_ID = '2026-10-24T2007Z'"),
("STARTED = '2026-10-24T19:07:00Z'","STARTED = '2026-10-24T20:07:00Z'"),
("OBS_AT = '2026-10-24T19:07:00Z'","OBS_AT = '2026-10-24T20:07:00Z'"),
("READS_BEFORE = 610","READS_BEFORE = 590"),
("datetime(2026,10,24,19,8,tzinfo=timezone.utc).timestamp()  # 1907Z (1807Z used 18:08, ","datetime(2026,10,24,20,9,tzinfo=timezone.utc).timestamp()  # 2007Z (1907Z used 19:08, 1807Z used 18:08, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_joshhoover': 'trend_joshhoover.txt', 'trend_chelsea': 'trend_chelsea.txt', 'trend_volkov': 'trend_volkov.txt',","'trend_marcelreed': 'trend_marcelreed.txt', 'trend_dijonlee': 'trend_dijonlee.txt', 'trend_kavanagh': 'trend_kavanagh.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_joshhoover','trend.Josh Hoover'),('trend_chelsea','trend.Chelsea'),('trend_volkov','trend.Volkov'),","('trend_marcelreed','trend.Marcel Reed'),('trend_dijonlee','trend.Dijon Lee'),('trend_kavanagh','trend.Kavanagh'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1907Z.json') and '/24/' in _c: continue","if _c.endswith('2007Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T1807Z'","_last = '2026-10-24T1907Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("one hundred and seventh run","one hundred and eighth run"),
("one hundred and ninth run","one hundred and tenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1907Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/2007Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1907Z: none read)","# 5) request picks (2007Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 29 second-hop and remaining posts in the second read)","two screening reads by id (96 unread referenced posts, most pointed-at first, then the 17 second-hop posts they led to)"),
("quote/repost words that/just + what (quoted)","quote/repost words the/this + is (quoted)"),
('trend names "Josh Hoover", "Chelsea" and "Volkov" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Marcel Reed", "Dijon Lee" and "Kavanagh" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 563 long, so the 400 cap left out the 23 last six-hour posts and the 140 slowest-growing still-gaining posts, and no cited post)",
 "(this 20Z run is a fourth hour, so the rest of the last 24 hours followed, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 591 long, so the 400 cap left out the 29 last six-hour posts, the 135 slowest-growing still-gaining posts and 27 of the 29 rest-of-24-hour posts, and no cited post)"),
("        if str(_x) in ('trend.Josh Hoover','trend.Chelsea','trend.Volkov'): return 'sports'  # 1907Z: Indiana v Michigan, Tottenham v Chelsea, UFC 333\n",
 "        if str(_x) in ('trend.Josh Hoover','trend.Chelsea','trend.Volkov'): return 'sports'  # 1907Z: Indiana v Michigan, Tottenham v Chelsea, UFC 333\n        if str(_x) in ('trend.Marcel Reed','trend.Dijon Lee','trend.Kavanagh'): return 'sports'  # 2007Z: Alabama v Texas A&M, UFC 333\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Afternoon run (3:07 PM ET"):
    lines[k]="            f'Afternoon run (4:07 PM ET Oct 24 / 20:07 UTC Oct 24, the 20Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1907Z ended at 590, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 591 ids, so the 400 cap left out the 29 last six-hour posts, the 135 slowest-growing still-gaining posts and 27 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Josh Hoover\""):
    lines[k]="            f'trend names \"Marcel Reed\", \"Dijon Lee\" and \"Kavanagh\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[k]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1907Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 96 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 17 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again in the first read, as in 1105Z through 1907Z, so it was not read in the second; 11 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
