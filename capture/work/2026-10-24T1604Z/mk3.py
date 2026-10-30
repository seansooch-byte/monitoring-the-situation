s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1404Z, one per event: "#UFC333" (first; UFC 333 fight night, one event with "Kody Steele", fourth, whose first-round knockout the same stream carries), "#20YearsOfTaylorSwift" (second; twentieth anniversary of the Taylor Swift debut album) and "#MrFanboyEP9" (eighth; Mr Fanboy series episode 9, one event with "MR FANBOY CHAPTER 9", ninth); "StubHub" (fifth) had posts attached in 1404Z, "Donnarumma" (sixth), "Villa" (seventh) and "Nicolas Jackson" (tenth) were cut as the Aston Villa v Manchester City event attached in 1307Z and 1404Z, and "Good Saturday" (third) was attached in 1307Z and was cut as a greeting, so those were skipped'
TN='three of the top-ten US names with no posts attached in 1505Z, one per event: "Malkoun" (third; a UFC 333 bout, one event with "Chopurov", sixth, read as its own name because "#UFC333" itself was attached in 1505Z), "#EternalDiamondLeeKnow" (seventh; Stray Kids member Lee Know birthday, one event with "#노_맘대로_즐기는_리노생일", tenth) and "StubHub" (ninth; Brewers fans on StubHub World Series tickets, last attached in 1404Z); "#UFC333" (first), "#20YearsOfTaylorSwift" (second) and "#MrFanboyEP9" (fourth, one event with "MR FANBOY CHAPTER 9", eighth) had posts attached in 1505Z, and "Good Saturday" (fifth) was attached in 1307Z and was cut as a greeting, so those were skipped'
R=[
("Build capture/2026/10/24/1505Z.json","Build capture/2026/10/24/1604Z.json"),
("work/2026-10-24T1505Z'","work/2026-10-24T1604Z'"),
("RUN_ID = '2026-10-24T1505Z'","RUN_ID = '2026-10-24T1604Z'"),
("STARTED = '2026-10-24T15:05:00Z'","STARTED = '2026-10-24T16:04:00Z'"),
("OBS_AT = '2026-10-24T15:05:00Z'","OBS_AT = '2026-10-24T16:04:00Z'"),
("READS_BEFORE = 690","READS_BEFORE = 670"),
("datetime(2026,10,24,15,6,tzinfo=timezone.utc).timestamp()  # 1505Z (1404Z used 14:06, ","datetime(2026,10,24,16,6,tzinfo=timezone.utc).timestamp()  # 1604Z (1505Z used 15:06, 1404Z used 14:06, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_ufc333': 'trend_ufc333.txt', 'trend_20yearsoftaylorswift': 'trend_20yearsoftaylorswift.txt', 'trend_mrfanboyep9': 'trend_mrfanboyep9.txt',","'trend_malkoun': 'trend_malkoun.txt', 'trend_eternaldiamondleeknow': 'trend_eternaldiamondleeknow.txt', 'trend_stubhub': 'trend_stubhub.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_ufc333','trend.#UFC333'),('trend_20yearsoftaylorswift','trend.#20YearsOfTaylorSwift'),('trend_mrfanboyep9','trend.#MrFanboyEP9'),","('trend_malkoun','trend.Malkoun'),('trend_eternaldiamondleeknow','trend.#EternalDiamondLeeKnow'),('trend_stubhub','trend.StubHub'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1505Z.json') and '/24/' in _c: continue","if _c.endswith('1604Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T1404Z'","_last = '2026-10-24T1505Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
 'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)'),
("one hundred and fifth run","one hundred and sixth run"),
("one hundred and third run","one hundred and fourth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1505Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1604Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1505Z: none read)","# 5) request picks (1604Z: none read)"),
("two screening reads by id (92 unread referenced posts, most pointed-at first, then the 26 second-hop posts they led to)","two screening reads by id (102 unread referenced posts, most pointed-at first, 100 in the first read and the last 2 in the second; second-hop ids left unread)"),
("quote/repost words my/it + that (quoted)","quote/repost words just/what + the (quoted)"),
('trend names "#UFC333", "#20YearsOfTaylorSwift" and "#MrFanboyEP9" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Malkoun", "#EternalDiamondLeeKnow" and "StubHub" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 15Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 561 long, so the 400 cap left out the 14 last six-hour posts and the 147 slowest-growing still-gaining posts, and no cited post)",
 "(this 16Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 564 long, so the 400 cap left out the 19 last six-hour posts and the 145 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.#MrFanboyEP9': return 'entertainment'  # 1505Z: Mr Fanboy series episode 9\n",
 "        if str(_x)=='trend.#MrFanboyEP9': return 'entertainment'  # 1505Z: Mr Fanboy series episode 9\n        if str(_x)=='trend.Malkoun': return 'sports'  # 1604Z: UFC 333 bout\n        if str(_x)=='trend.#EternalDiamondLeeKnow': return 'music'  # 1604Z: Stray Kids Lee Know birthday\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Late-morning run (11:05 AM ET"):
    lines[k]="            f'Midday run (12:04 PM ET Oct 24 / 16:04 UTC Oct 24, the 16Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1505Z ended at 670, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 564 ids, so the 400 cap left out the 19 last six-hour posts and the 145 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#UFC333\""):
    lines[k]="            f'trend names \"Malkoun\", \"#EternalDiamondLeeKnow\" and \"StubHub\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[k]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1505Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 92"):
    lines[k]="            f'two screening reads by id: 102 unread referenced, reply-parent and media-source posts, most pointed-at first, 100 in the first read and the last 2 in the second (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again, as in 1105Z, 1204Z, 1404Z and 1505Z, and 2113551602225197365 was Not Found; second-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
