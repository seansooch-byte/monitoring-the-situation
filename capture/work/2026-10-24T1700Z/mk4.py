s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1505Z, one per event: "Malkoun" (third; a UFC 333 bout, one event with "Chopurov", sixth, read as its own name because "#UFC333" itself was attached in 1505Z), "#EternalDiamondLeeKnow" (seventh; Stray Kids member Lee Know birthday, one event with "#노_맘대로_즐기는_리노생일", tenth) and "StubHub" (ninth; Brewers fans on StubHub World Series tickets, last attached in 1404Z); "#UFC333" (first), "#20YearsOfTaylorSwift" (second) and "#MrFanboyEP9" (fourth, one event with "MR FANBOY CHAPTER 9", eighth) had posts attached in 1505Z, and "Good Saturday" (fifth) was attached in 1307Z and was cut as a greeting, so those were skipped'
TN='three of the top-ten US names with no posts attached in 1604Z, one per event: "Sam Leavitt" (third; LSU quarterback in LSU v Auburn, one event with "Jackson Harris", ninth, whose touchdown catch the same stream carries), "Mallory" (seventh; Miami freshman running back Javian Mallory rushing touchdown) and "Thicknesse" (tenth; Colby Thicknesse beat Asaf Chopurov at UFC 333, one event with "Chopurov", eighth, read as its own name as "Malkoun" was in 1604Z); "#UFC333" (first) and "#20YearsOfTaylorSwift" (sixth) had posts attached in 1505Z, and "Jason Beck" (second), "Grant Dawson" (fourth) and "Tommy Carr" (fifth) were not read to keep to about 20 reads'
R=[
("Build capture/2026/10/24/1604Z.json","Build capture/2026/10/24/1700Z.json"),
("work/2026-10-24T1604Z'","work/2026-10-24T1700Z'"),
("RUN_ID = '2026-10-24T1604Z'","RUN_ID = '2026-10-24T1700Z'"),
("STARTED = '2026-10-24T16:04:00Z'","STARTED = '2026-10-24T17:00:00Z'"),
("OBS_AT = '2026-10-24T16:04:00Z'","OBS_AT = '2026-10-24T17:00:00Z'"),
("READS_BEFORE = 670","READS_BEFORE = 650"),
("datetime(2026,10,24,16,6,tzinfo=timezone.utc).timestamp()  # 1604Z (1505Z used 15:06, ","datetime(2026,10,24,17,1,tzinfo=timezone.utc).timestamp()  # 1700Z (1604Z used 16:06, 1505Z used 15:06, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_malkoun': 'trend_malkoun.txt', 'trend_eternaldiamondleeknow': 'trend_eternaldiamondleeknow.txt', 'trend_stubhub': 'trend_stubhub.txt',","'trend_samleavitt': 'trend_samleavitt.txt', 'trend_mallory': 'trend_mallory.txt', 'trend_thicknesse': 'trend_thicknesse.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_malkoun','trend.Malkoun'),('trend_eternaldiamondleeknow','trend.#EternalDiamondLeeKnow'),('trend_stubhub','trend.StubHub'),","('trend_samleavitt','trend.Sam Leavitt'),('trend_mallory','trend.Mallory'),('trend_thicknesse','trend.Thicknesse'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1604Z.json') and '/24/' in _c: continue","if _c.endswith('1700Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T1505Z'","_last = '2026-10-24T1604Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("one hundred and sixth run","one hundred and seventh run"),
("one hundred and fourth run","one hundred and fifth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1604Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1700Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1604Z: none read)","# 5) request picks (1700Z: none read)"),
("two screening reads by id (102 unread referenced posts, most pointed-at first, 100 in the first read and the last 2 in the second; second-hop ids left unread)","two screening reads by id (95 unread referenced posts, most pointed-at first, then the 14 second-hop posts they led to)"),
("(second-hop ids left unread this run)","(and a second hop)"),
("quote/repost words just/what + the (quoted)","quote/repost words this/is + you (quoted)"),
('trend names "Malkoun", "#EternalDiamondLeeKnow" and "StubHub" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Sam Leavitt", "Mallory" and "Thicknesse" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 16Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 564 long, so the 400 cap left out the 19 last six-hour posts and the 145 slowest-growing still-gaining posts, and no cited post)",
 "(this 17Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 564 long, so the 400 cap left out the 33 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.#EternalDiamondLeeKnow': return 'music'  # 1604Z: Stray Kids Lee Know birthday\n",
 "        if str(_x)=='trend.#EternalDiamondLeeKnow': return 'music'  # 1604Z: Stray Kids Lee Know birthday\n        if str(_x)=='trend.Sam Leavitt': return 'sports'  # 1700Z: LSU v Auburn\n        if str(_x)=='trend.Mallory': return 'sports'  # 1700Z: Miami running back Javian Mallory\n        if str(_x)=='trend.Thicknesse': return 'sports'  # 1700Z: UFC 333 bout\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Midday run (12:04 PM ET"):
    lines[k]="            f'Early-afternoon run (1:00 PM ET Oct 24 / 17:00 UTC Oct 24, the 17Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1604Z ended at 650, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 564 ids, so the 400 cap left out the 33 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Malkoun\""):
    lines[k]="            f'trend names \"Sam Leavitt\", \"Mallory\" and \"Thicknesse\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[k]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1604Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 102"):
    lines[k]="            f'two screening reads by id: 95 unread referenced, reply-parent and media-source posts, most pointed-at first, with the 14 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again, as in 1105Z, 1204Z, 1404Z, 1505Z and 1604Z, and 2042119594282823945 returned Authorization Error, so neither was read in the second read; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
