s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1307Z: "StubHub" (fifth; Brewers fans complaining about StubHub World Series ticket problems), "#AlconMustStopPPGCollab" (eighth; Love and Deepspace (Papergames) fan campaign against the Blade Runner collab, one event with "#上海必须追究姚润昊责任", seventh, and "#BladeRunnerAndPPGInCahoots", ninth, which the same posts carry; last attached in 1204Z) and "Maresca" (tenth; read as a separate name, but its posts are about Nicolas Jackson scoring against Enzo Maresca, so it turned out to be the same Aston Villa v Manchester City event as "Donnarumma"); "Good Saturday" (first) and "Donnarumma" (second) had posts attached in 1307Z, and "Villa" (third), "Nicolas Jackson" (fourth) and "Guehi" (sixth) were cut as one event with "Donnarumma", so those were skipped'
TN='three of the top-ten US names with no posts attached in 1404Z, one per event: "#UFC333" (first; UFC 333 fight night, one event with "Kody Steele", fourth, whose first-round knockout the same stream carries), "#20YearsOfTaylorSwift" (second; twentieth anniversary of Taylor Swift\'s debut album) and "#MrFanboyEP9" (eighth; Mr Fanboy series episode 9, one event with "MR FANBOY CHAPTER 9", ninth); "StubHub" (fifth) had posts attached in 1404Z, "Donnarumma" (sixth), "Villa" (seventh) and "Nicolas Jackson" (tenth) were cut as the Aston Villa v Manchester City event attached in 1307Z and 1404Z, and "Good Saturday" (third) was attached in 1307Z and was cut as a greeting, so those were skipped'
R=[
("Build capture/2026/10/24/1404Z.json","Build capture/2026/10/24/1505Z.json"),
("work/2026-10-24T1404Z'","work/2026-10-24T1505Z'"),
("RUN_ID = '2026-10-24T1404Z'","RUN_ID = '2026-10-24T1505Z'"),
("STARTED = '2026-10-24T14:04:00Z'","STARTED = '2026-10-24T15:05:00Z'"),
("OBS_AT = '2026-10-24T14:04:00Z'","OBS_AT = '2026-10-24T15:05:00Z'"),
("READS_BEFORE = 710","READS_BEFORE = 690"),
("datetime(2026,10,24,14,6,tzinfo=timezone.utc).timestamp()  # 1404Z (1307Z used 13:09, ","datetime(2026,10,24,15,6,tzinfo=timezone.utc).timestamp()  # 1505Z (1404Z used 14:06, 1307Z used 13:09, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_stubhub': 'trend_stubhub.txt', 'trend_maresca': 'trend_maresca.txt', 'trend_alconmuststopppgcollab': 'trend_alconmuststopppgcollab.txt',","'trend_ufc333': 'trend_ufc333.txt', 'trend_20yearsoftaylorswift': 'trend_20yearsoftaylorswift.txt', 'trend_mrfanboyep9': 'trend_mrfanboyep9.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_stubhub','trend.StubHub'),('trend_maresca','trend.Maresca'),('trend_alconmuststopppgcollab','trend.#AlconMustStopPPGCollab'),","('trend_ufc333','trend.#UFC333'),('trend_20yearsoftaylorswift','trend.#20YearsOfTaylorSwift'),('trend_mrfanboyep9','trend.#MrFanboyEP9'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1404Z.json') and '/24/' in _c: continue","if _c.endswith('1505Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T1307Z'","_last = '2026-10-24T1404Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)',
 'common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)'),
("one hundred and fourth run","one hundred and fifth run"),
("one hundred and second run","one hundred and third run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1404Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1505Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1404Z: none read)","# 5) request picks (1505Z: none read)"),
("two screening reads by id (98 unread referenced posts, most pointed-at first, then the 17 second-hop posts they led to)","two screening reads by id (92 unread referenced posts, most pointed-at first, then the 26 second-hop posts they led to)"),
("quote/repost words is/you + and (quoted)","quote/repost words my/it + that (quoted)"),
('trend names "StubHub", "#AlconMustStopPPGCollab" and "Maresca" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "#UFC333", "#20YearsOfTaylorSwift" and "#MrFanboyEP9" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 554 long, so the 400 cap left out the 12 last six-hour posts and the 142 slowest-growing still-gaining posts, and no cited post)",
 "(this 15Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 561 long, so the 400 cap left out the 14 last six-hour posts and the 147 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.Maresca': return 'sports'  # 1404Z: Aston Villa v Manchester City\n",
 "        if str(_x)=='trend.Maresca': return 'sports'  # 1404Z: Aston Villa v Manchester City\n        if str(_x)=='trend.#UFC333': return 'sports'  # 1505Z: UFC 333 fight night\n        if str(_x)=='trend.#20YearsOfTaylorSwift': return 'music'  # 1505Z: Taylor Swift debut album anniversary\n        if str(_x)=='trend.#MrFanboyEP9': return 'entertainment'  # 1505Z: Mr Fanboy series episode 9\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (10:04 AM ET"):
    lines[k]="            f'Late-morning run (11:05 AM ET Oct 24 / 15:05 UTC Oct 24, the 15Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1404Z ended at 690, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 561 ids, so the 400 cap left out the 14 last six-hour posts and the 147 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"StubHub\""):
    lines[k]="            f'trend names \"#UFC333\", \"#20YearsOfTaylorSwift\" and \"#MrFanboyEP9\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words is/you"):
    lines[k]="            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1404Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 98"):
    lines[k]="            f'two screening reads by id: 92 unread referenced, reply-parent and media-source posts, most pointed-at first, with the 26 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717, Not Found in 1105Z, 1204Z, 1404Z and again this run, left out of the second read; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
