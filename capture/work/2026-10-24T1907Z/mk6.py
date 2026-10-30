s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1700Z, one per event: "Michigan" (second; Michigan sheriff William Federspiel leaving the Democratic Party to back Mike Rogers, the biggest origin in the stream), "Malachi Toney" (fourth; Miami receiver 53-yard touchdown against Pitt) and "Texas Tech" (fifth; Cincinnati leading No. 8 Texas Tech by 18 at halftime, one event with "Cincinnati", thirteenth); "#UFC333" (first) had posts attached in 1505Z, "Sam Leavitt" (ninth) and "Jackson Harris" (eighth, the same LSU v Auburn event) in 1700Z, and "Jason Beck" (third), "Tommy Carr" (sixth) and "Reyes" (seventh) were not read to keep to about 20 reads'
TN='three of the top-ten US names with no posts attached in 1807Z, one per event: "Josh Hoover" (fourth; Indiana quarterback in Indiana v Michigan, one event with "#iufb", eighth), "Chelsea" (sixth; Tottenham beating Chelsea, one event with "#COYS", eleventh, and "Tottenham", twelfth) and "Volkov" (ninth; Alexander Volkov winning by decision at UFC 333); "Michigan" (first), "Jason Beck" (third), "Texas Tech" (fifth) and "Malachi Toney" (seventh) had posts attached in 1807Z, "#UFC333" (second) in 1505Z, and "Tommy Carr" (tenth) was not read to keep to about 20 reads'
R=[
("Build capture/2026/10/24/1807Z.json","Build capture/2026/10/24/1907Z.json"),
("work/2026-10-24T1807Z'","work/2026-10-24T1907Z'"),
("RUN_ID = '2026-10-24T1807Z'","RUN_ID = '2026-10-24T1907Z'"),
("STARTED = '2026-10-24T18:07:00Z'","STARTED = '2026-10-24T19:07:00Z'"),
("OBS_AT = '2026-10-24T18:07:00Z'","OBS_AT = '2026-10-24T19:07:00Z'"),
("READS_BEFORE = 630","READS_BEFORE = 610"),
("datetime(2026,10,24,18,8,tzinfo=timezone.utc).timestamp()  # 1807Z (1700Z used 17:01, ","datetime(2026,10,24,19,8,tzinfo=timezone.utc).timestamp()  # 1907Z (1807Z used 18:08, 1700Z used 17:01, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_michigan': 'trend_michigan.txt', 'trend_malachitoney': 'trend_malachitoney.txt', 'trend_texastech': 'trend_texastech.txt',","'trend_joshhoover': 'trend_joshhoover.txt', 'trend_chelsea': 'trend_chelsea.txt', 'trend_volkov': 'trend_volkov.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_michigan','trend.Michigan'),('trend_malachitoney','trend.Malachi Toney'),('trend_texastech','trend.Texas Tech'),","('trend_joshhoover','trend.Josh Hoover'),('trend_chelsea','trend.Chelsea'),('trend_volkov','trend.Volkov'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1807Z.json') and '/24/' in _c: continue","if _c.endswith('1907Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T1700Z'","_last = '2026-10-24T1807Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("one hundred and sixth run","one hundred and seventh run"),
("one hundred and eighth run","one hundred and ninth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1807Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1907Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1807Z: none read)","# 5) request picks (1907Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 19 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 29 second-hop and remaining posts in the second read)"),
("quote/repost words and/my + it (quoted)","quote/repost words that/just + what (quoted)"),
('trend names "Michigan", "Malachi Toney" and "Texas Tech" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Josh Hoover", "Chelsea" and "Volkov" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 561 long, so the 400 cap left out the 23 last six-hour posts and the 138 slowest-growing still-gaining posts, and no cited post)",
 "(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 563 long, so the 400 cap left out the 23 last six-hour posts and the 140 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.Texas Tech': return 'sports'  # 1807Z: Cincinnati v Texas Tech\n",
 "        if str(_x)=='trend.Texas Tech': return 'sports'  # 1807Z: Cincinnati v Texas Tech\n        if str(_x) in ('trend.Josh Hoover','trend.Chelsea','trend.Volkov'): return 'sports'  # 1907Z: Indiana v Michigan, Tottenham v Chelsea, UFC 333\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Afternoon run (2:07 PM ET"):
    lines[k]="            f'Afternoon run (3:07 PM ET Oct 24 / 19:07 UTC Oct 24, the 19Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1807Z ended at 610, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 563 ids, so the 400 cap left out the 23 last six-hour posts and the 140 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Michigan\""):
    lines[k]="            f'trend names \"Josh Hoover\", \"Chelsea\" and \"Volkov\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[k]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1807Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 29 in the second read (the 8 left from the first list and the 21 second-hop posts; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again in the first read, as in 1105Z through 1807Z, so it was not read in the second; 2113500777217970641 was Not Found in the second read; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
