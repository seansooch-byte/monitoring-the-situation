s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1204Z, one per event: "Donnarumma" (second; Aston Villa v Manchester City, Nicolas Jackson goal past Donnarumma, one event with "Nicolas Jackson", seventh, "Guehi", eighth, "Nico Jackson", ninth, and "Villa", tenth), "#NIKKE4thAnniversary" (third; Goddess of Victory: NIKKE game fourth-anniversary countdown) and "Good Saturday" (first; weekend greeting); "#AlconMustStopPPGCollab" (fourth) had posts attached in 1204Z, and "#上海必须追究姚润昊责任" (fifth) and "#BladeRunnerAndPPGInCahoots" (sixth) were cut as one event with it, and "Nicolas Jackson", "Guehi", "Nico Jackson" and "Villa" as one event with "Donnarumma", so those were skipped'
TN='three of the top-ten US names with no posts attached in 1307Z: "StubHub" (fifth; Brewers fans complaining about StubHub World Series ticket problems), "#AlconMustStopPPGCollab" (eighth; Love and Deepspace (Papergames) fan campaign against the Blade Runner collab, one event with "#上海必须追究姚润昊责任", seventh, and "#BladeRunnerAndPPGInCahoots", ninth, which the same posts carry; last attached in 1204Z) and "Maresca" (tenth; read as a separate name, but its posts are about Nicolas Jackson scoring against Enzo Maresca, so it turned out to be the same Aston Villa v Manchester City event as "Donnarumma"); "Good Saturday" (first) and "Donnarumma" (second) had posts attached in 1307Z, and "Villa" (third), "Nicolas Jackson" (fourth) and "Guehi" (sixth) were cut as one event with "Donnarumma", so those were skipped'
R=[
("Build capture/2026/10/24/1307Z.json","Build capture/2026/10/24/1404Z.json"),
("work/2026-10-24T1307Z'","work/2026-10-24T1404Z'"),
("RUN_ID = '2026-10-24T1307Z'","RUN_ID = '2026-10-24T1404Z'"),
("STARTED = '2026-10-24T13:07:00Z'","STARTED = '2026-10-24T14:04:00Z'"),
("OBS_AT = '2026-10-24T13:07:00Z'","OBS_AT = '2026-10-24T14:04:00Z'"),
("READS_BEFORE = 730","READS_BEFORE = 710"),
("datetime(2026,10,24,13,9,tzinfo=timezone.utc).timestamp()  # 1307Z (1204Z used 12:05, ","datetime(2026,10,24,14,6,tzinfo=timezone.utc).timestamp()  # 1404Z (1307Z used 13:09, 1204Z used 12:05, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_donnarumma': 'trend_donnarumma.txt', 'trend_nikke4thanniversary': 'trend_nikke4thanniversary.txt', 'trend_goodsaturday': 'trend_goodsaturday.txt',","'trend_stubhub': 'trend_stubhub.txt', 'trend_maresca': 'trend_maresca.txt', 'trend_alconmuststopppgcollab': 'trend_alconmuststopppgcollab.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_donnarumma','trend.Donnarumma'),('trend_nikke4thanniversary','trend.#NIKKE4thAnniversary'),('trend_goodsaturday','trend.Good Saturday'),","('trend_stubhub','trend.StubHub'),('trend_maresca','trend.Maresca'),('trend_alconmuststopppgcollab','trend.#AlconMustStopPPGCollab'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1307Z.json') and '/24/' in _c: continue","if _c.endswith('1404Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T1204Z'","_last = '2026-10-24T1307Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
 'common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)'),
("one hundred and third run","one hundred and fourth run"),
("one hundred and first run","one hundred and second run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1307Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1404Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1307Z: none read)","# 5) request picks (1404Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 11 remaining and 21 second-hop posts they led to)","two screening reads by id (98 unread referenced posts, most pointed-at first, then the 17 second-hop posts they led to)"),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + and (quoted)"),
('trend names "Donnarumma", "#NIKKE4thAnniversary" and "Good Saturday" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "StubHub", "#AlconMustStopPPGCollab" and "Maresca" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 13Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 548 long, so the 400 cap left out the 7 last six-hour posts and the 141 slowest-growing still-gaining posts, and no cited post)",
 "(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 554 long, so the 400 cap left out the 12 last six-hour posts and the 142 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.#NIKKE4thAnniversary': return 'gaming'  # 1307Z: NIKKE game anniversary countdown\n",
 "        if str(_x)=='trend.#NIKKE4thAnniversary': return 'gaming'  # 1307Z: NIKKE game anniversary countdown\n        if str(_x)=='trend.StubHub': return 'sports'  # 1404Z: Brewers World Series ticket complaints\n        if str(_x)=='trend.Maresca': return 'sports'  # 1404Z: Aston Villa v Manchester City\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (9:07 AM ET"):
    lines[k]="            f'Morning run (10:04 AM ET Oct 24 / 14:04 UTC Oct 24, the 14Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1307Z ended at 710, so no read went elsewhere in between), parallel batches of up to 10, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 554 ids, so the 400 cap left out the 12 last six-hour posts and the 142 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Donnarumma\""):
    lines[k]="            f'trend names \"StubHub\", \"#AlconMustStopPPGCollab\" and \"Maresca\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[k]="            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1307Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 111"):
    lines[k]="            f'two screening reads by id: 98 unread referenced, reply-parent and media-source posts, most pointed-at first, with the 17 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717, Not Found in 1105Z, 1204Z and this run, and 2113380735763808296, Authorization Error this run, not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
