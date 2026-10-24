s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1105Z, one per event: "#AlconMustStopPPGCollab" (third; Love and Deepspace (Papergames) fan campaign against the Blade Runner collab, one event with "#BladeRunnerAndPPGInCahoots", fourth, and "#上海必须追究姚润昊责任", fifth, which the same posts carry), "Guehi" (sixth; Aston Villa v Manchester City, one event with "Nicolas Jackson", eighth) and "#YouManiacSeriesEP9" (seventh; GMMTV series episode hashtag); "#NIKKE4thAnniversary" (first) had posts attached in 1105Z, "Good Saturday" (second) and "CULTURAL HERITAGE RECOGNITION" (tenth) were read in 1003Z, "#BladeRunnerAndPPGInCahoots", "#上海必须追究姚润昊责任" and "Nicolas Jackson" were cut as one event with names read, and "Caturday" (ninth) was cut to keep to about 20 reads, so those were skipped'
TN='three of the top-ten US names with no posts attached in 1204Z, one per event: "Donnarumma" (second; Aston Villa v Manchester City, Nicolas Jackson goal past Donnarumma, one event with "Nicolas Jackson", seventh, "Guehi", eighth, "Nico Jackson", ninth, and "Villa", tenth), "#NIKKE4thAnniversary" (third; Goddess of Victory: NIKKE game fourth-anniversary countdown) and "Good Saturday" (first; weekend greeting); "#AlconMustStopPPGCollab" (fourth) had posts attached in 1204Z, and "#上海必须追究姚润昊责任" (fifth) and "#BladeRunnerAndPPGInCahoots" (sixth) were cut as one event with it, and "Nicolas Jackson", "Guehi", "Nico Jackson" and "Villa" as one event with "Donnarumma", so those were skipped'
R=[
("Build capture/2026/10/24/1204Z.json","Build capture/2026/10/24/1307Z.json"),
("work/2026-10-24T1204Z'","work/2026-10-24T1307Z'"),
("RUN_ID = '2026-10-24T1204Z'","RUN_ID = '2026-10-24T1307Z'"),
("STARTED = '2026-10-24T12:04:00Z'","STARTED = '2026-10-24T13:07:00Z'"),
("OBS_AT = '2026-10-24T12:04:00Z'","OBS_AT = '2026-10-24T13:07:00Z'"),
("READS_BEFORE = 750","READS_BEFORE = 730"),
("datetime(2026,10,24,12,5,tzinfo=timezone.utc).timestamp()  # 1204Z (","datetime(2026,10,24,13,9,tzinfo=timezone.utc).timestamp()  # 1307Z (1204Z used 12:05, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_alconmuststopppgcollab': 'trend_alconmuststopppgcollab.txt', 'trend_guehi': 'trend_guehi.txt', 'trend_youmaniacseriesep9': 'trend_youmaniacseriesep9.txt',","'trend_donnarumma': 'trend_donnarumma.txt', 'trend_nikke4thanniversary': 'trend_nikke4thanniversary.txt', 'trend_goodsaturday': 'trend_goodsaturday.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_alconmuststopppgcollab','trend.#AlconMustStopPPGCollab'),('trend_guehi','trend.Guehi'),('trend_youmaniacseriesep9','trend.#YouManiacSeriesEP9'),","('trend_donnarumma','trend.Donnarumma'),('trend_nikke4thanniversary','trend.#NIKKE4thAnniversary'),('trend_goodsaturday','trend.Good Saturday'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1204Z.json') and '/24/' in _c: continue","if _c.endswith('1307Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T1105Z'","_last = '2026-10-24T1204Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("one hundred and second run","one hundred and third run"),
("one hundredth run","one hundred and first run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1204Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1307Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1204Z: none read)","# 5) request picks (1307Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 3 remaining and 22 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 11 remaining and 21 second-hop posts they led to)"),
("quote/repost words you/and + my (quoted)","quote/repost words what/the + this (quoted)"),
('trend names "#AlconMustStopPPGCollab", "Guehi" and "#YouManiacSeriesEP9" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Donnarumma", "#NIKKE4thAnniversary" and "Good Saturday" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 12Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 577 long, so the 400 cap left out the 4 last six-hour posts, the 134 slowest-growing still-gaining posts and the 39 slowest rest-of-24-hour posts, and no cited post)",
 "(this 13Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 548 long, so the 400 cap left out the 7 last six-hour posts and the 141 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.#YouManiacSeriesEP9': return 'entertainment'  # 1204Z: GMMTV series episode hashtag\n",
 "        if str(_x)=='trend.#YouManiacSeriesEP9': return 'entertainment'  # 1204Z: GMMTV series episode hashtag\n        if str(_x)=='trend.Donnarumma': return 'sports'  # 1307Z: Aston Villa v Manchester City\n        if str(_x)=='trend.#NIKKE4thAnniversary': return 'gaming'  # 1307Z: NIKKE game anniversary countdown\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (8:04 AM ET"):
    lines[k]="            f'Morning run (9:07 AM ET Oct 24 / 13:07 UTC Oct 24, the 13Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1204Z ended at 730, so no read went elsewhere in between), parallel batches of up to 10, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 548 ids, so the 400 cap left out the 7 last six-hour posts and the 141 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#AlconMustStopPPGCollab\""):
    lines[k]="            f'trend names \"Donnarumma\", \"#NIKKE4thAnniversary\" and \"Good Saturday\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[k]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1204Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 103"):
    lines[k]="            f'two screening reads by id: 111 unread referenced, reply-parent and media-source posts, most pointed-at first (100, then 11), with the 21 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717, Not Found in 1105Z and 1204Z, not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
