s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1604Z, one per event: "Sam Leavitt" (third; LSU quarterback in LSU v Auburn, one event with "Jackson Harris", ninth, whose touchdown catch the same stream carries), "Mallory" (seventh; Miami freshman running back Javian Mallory rushing touchdown) and "Thicknesse" (tenth; Colby Thicknesse beat Asaf Chopurov at UFC 333, one event with "Chopurov", eighth, read as its own name as "Malkoun" was in 1604Z); "#UFC333" (first) and "#20YearsOfTaylorSwift" (sixth) had posts attached in 1505Z, and "Jason Beck" (second), "Grant Dawson" (fourth) and "Tommy Carr" (fifth) were not read to keep to about 20 reads'
TN='three of the top-ten US names with no posts attached in 1700Z, one per event: "Michigan" (second; Michigan sheriff William Federspiel leaving the Democratic Party to back Mike Rogers, the biggest origin in the stream), "Malachi Toney" (fourth; Miami receiver 53-yard touchdown against Pitt) and "Texas Tech" (fifth; Cincinnati leading No. 8 Texas Tech by 18 at halftime, one event with "Cincinnati", thirteenth); "#UFC333" (first) had posts attached in 1505Z, "Sam Leavitt" (ninth) and "Jackson Harris" (eighth, the same LSU v Auburn event) in 1700Z, and "Jason Beck" (third), "Tommy Carr" (sixth) and "Reyes" (seventh) were not read to keep to about 20 reads'
R=[
("Build capture/2026/10/24/1700Z.json","Build capture/2026/10/24/1807Z.json"),
("work/2026-10-24T1700Z'","work/2026-10-24T1807Z'"),
("RUN_ID = '2026-10-24T1700Z'","RUN_ID = '2026-10-24T1807Z'"),
("STARTED = '2026-10-24T17:00:00Z'","STARTED = '2026-10-24T18:07:00Z'"),
("OBS_AT = '2026-10-24T17:00:00Z'","OBS_AT = '2026-10-24T18:07:00Z'"),
("READS_BEFORE = 650","READS_BEFORE = 630"),
("datetime(2026,10,24,17,1,tzinfo=timezone.utc).timestamp()  # 1700Z (1604Z used 16:06, ","datetime(2026,10,24,18,8,tzinfo=timezone.utc).timestamp()  # 1807Z (1700Z used 17:01, 1604Z used 16:06, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_samleavitt': 'trend_samleavitt.txt', 'trend_mallory': 'trend_mallory.txt', 'trend_thicknesse': 'trend_thicknesse.txt',","'trend_michigan': 'trend_michigan.txt', 'trend_malachitoney': 'trend_malachitoney.txt', 'trend_texastech': 'trend_texastech.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_samleavitt','trend.Sam Leavitt'),('trend_mallory','trend.Mallory'),('trend_thicknesse','trend.Thicknesse'),","('trend_michigan','trend.Michigan'),('trend_malachitoney','trend.Malachi Toney'),('trend_texastech','trend.Texas Tech'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1700Z.json') and '/24/' in _c: continue","if _c.endswith('1807Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T1604Z'","_last = '2026-10-24T1700Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("one hundred and seventh run","one hundred and eighth run"),
("one hundred and fifth run","one hundred and sixth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1700Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1807Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1700Z: none read)","# 5) request picks (1807Z: none read)"),
("two screening reads by id (95 unread referenced posts, most pointed-at first, then the 14 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 19 second-hop posts they led to)"),
("quote/repost words this/is + you (quoted)","quote/repost words and/my + it (quoted)"),
('trend names "Sam Leavitt", "Mallory" and "Thicknesse" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Michigan", "Malachi Toney" and "Texas Tech" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 17Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 564 long, so the 400 cap left out the 33 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)",
 "(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 561 long, so the 400 cap left out the 23 last six-hour posts and the 138 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.Thicknesse': return 'sports'  # 1700Z: UFC 333 bout\n",
 "        if str(_x)=='trend.Thicknesse': return 'sports'  # 1700Z: UFC 333 bout\n        if str(_x)=='trend.Michigan': return 'politics'  # 1807Z: Michigan sheriff party switch\n        if str(_x)=='trend.Malachi Toney': return 'sports'  # 1807Z: Miami v Pitt\n        if str(_x)=='trend.Texas Tech': return 'sports'  # 1807Z: Cincinnati v Texas Tech\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Early-afternoon run (1:00 PM ET"):
    lines[k]="            f'Afternoon run (2:07 PM ET Oct 24 / 18:07 UTC Oct 24, the 18Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1700Z ended at 630, so no read went elsewhere in between), parallel batches of up to 10, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 561 ids, so the 400 cap left out the 23 last six-hour posts and the 138 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Sam Leavitt\""):
    lines[k]="            f'trend names \"Michigan\", \"Malachi Toney\" and \"Texas Tech\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[k]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1700Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 95"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, with the 19 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again, as in 1105Z, 1204Z, 1404Z, 1505Z, 1604Z and 1700Z, so it was not read in the second read; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
