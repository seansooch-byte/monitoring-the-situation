s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 1003Z, one per event: "#NIKKE4thAnniversary" (first; Goddess of Victory: NIKKE game fourth-anniversary countdown), "Wemby" (fifth; Rockets 114, Spurs 110, the Amen Thompson block on Wembanyama, one event with "Amen Thompson", sixth, and "Spurs", seventh) and "Warriors" (tenth; Grizzlies comeback win over the Warriors); "Good Saturday", "#CulturalCreditMatters", "CULTURAL HERITAGE RECOGNITION", "#ScarletHeartTH" and "#pw_mg" had posts attached in 1003Z, and "Amen Thompson" and "Spurs" were cut as one event with "Wemby", so those were skipped'
TN='three of the top-ten US names with no posts attached in 1105Z, one per event: "#AlconMustStopPPGCollab" (third; Love and Deepspace (Papergames) fan campaign against the Blade Runner collab, one event with "#BladeRunnerAndPPGInCahoots", fourth, and "#上海必须追究姚润昊责任", fifth, which the same posts carry), "Guehi" (sixth; Aston Villa v Manchester City, one event with "Nicolas Jackson", eighth) and "#YouManiacSeriesEP9" (seventh; GMMTV series episode hashtag); "#NIKKE4thAnniversary" (first) had posts attached in 1105Z, "Good Saturday" (second) and "CULTURAL HERITAGE RECOGNITION" (tenth) were read in 1003Z, "#BladeRunnerAndPPGInCahoots", "#上海必须追究姚润昊责任" and "Nicolas Jackson" were cut as one event with names read, and "Caturday" (ninth) was cut to keep to about 20 reads, so those were skipped'
R=[
("Build capture/2026/10/24/1105Z.json","Build capture/2026/10/24/1204Z.json"),
("work/2026-10-24T1105Z'","work/2026-10-24T1204Z'"),
("RUN_ID = '2026-10-24T1105Z'","RUN_ID = '2026-10-24T1204Z'"),
("STARTED = '2026-10-24T11:05:00Z'","STARTED = '2026-10-24T12:04:00Z'"),
("OBS_AT = '2026-10-24T11:05:00Z'","OBS_AT = '2026-10-24T12:04:00Z'"),
("READS_BEFORE = 772","READS_BEFORE = 750"),
("datetime(2026,10,24,11,7,tzinfo=timezone.utc).timestamp()  # 1105Z (","datetime(2026,10,24,12,5,tzinfo=timezone.utc).timestamp()  # 1204Z (1105Z used 11:07, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_nikke4thanniversary': 'trend_nikke4thanniversary.txt', 'trend_wemby': 'trend_wemby.txt', 'trend_warriors': 'trend_warriors.txt',","'trend_alconmuststopppgcollab': 'trend_alconmuststopppgcollab.txt', 'trend_guehi': 'trend_guehi.txt', 'trend_youmaniacseriesep9': 'trend_youmaniacseriesep9.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_nikke4thanniversary','trend.#NIKKE4thAnniversary'),('trend_wemby','trend.Wemby'),('trend_warriors','trend.Warriors'),","('trend_alconmuststopppgcollab','trend.#AlconMustStopPPGCollab'),('trend_guehi','trend.Guehi'),('trend_youmaniacseriesep9','trend.#YouManiacSeriesEP9'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1105Z.json') and '/24/' in _c: continue","if _c.endswith('1204Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T1003Z'","_last = '2026-10-24T1105Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)'),
("one hundred and first run","one hundred and second run"),
("ninety-ninth run","one hundredth run"),
("06:00-11:00 UTC band, up to 20; four-hour","12:00-05:00 UTC band, up to 42; four-hour"),
("06:00-11:00 UTC band, up to 20)'","12:00-05:00 UTC band, up to 42)'"),
("in the 06:00-11:00 UTC band, up to 20)',None,'skipped'","in the 12:00-05:00 UTC band, up to 42)',None,'skipped'"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1105Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1204Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1105Z: none read)","# 5) request picks (1204Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 9 remaining and 22 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 3 remaining and 22 second-hop posts they led to)"),
('trend names "#NIKKE4thAnniversary", "Wemby" and "Warriors" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "#AlconMustStopPPGCollab", "Guehi" and "#YouManiacSeriesEP9" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 544 long, so the 400 cap left out the 25 last six-hour posts and the 119 slowest-growing still-gaining posts, and no cited post)",
 "(this 12Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 577 long, so the 400 cap left out the 4 last six-hour posts, the 134 slowest-growing still-gaining posts and the 39 slowest rest-of-24-hour posts, and no cited post)"),
("        if str(_x)=='trend.#CulturalCreditMatters': return 'entertainment'  # 0602Z: Myanmar fan campaign about Scarlet Heart Thailand\n",
 "        if str(_x)=='trend.#CulturalCreditMatters': return 'entertainment'  # 0602Z: Myanmar fan campaign about Scarlet Heart Thailand\n        if str(_x)=='trend.#AlconMustStopPPGCollab': return 'gaming'  # 1204Z: Love and Deepspace (Papergames) fan campaign against the Blade Runner collab\n        if str(_x)=='trend.Guehi': return 'sports'  # 1204Z: Aston Villa v Manchester City\n        if str(_x)=='trend.#YouManiacSeriesEP9': return 'entertainment'  # 1204Z: GMMTV series episode hashtag\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (7:05 AM ET"):
    lines[k]="            f'Morning run (8:04 AM ET Oct 24 / 12:04 UTC Oct 24, the 12Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1105Z ended at 752, so 2 reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 577 ids, so the 400 cap left out the 4 last six-hour posts, the 134 slowest-growing still-gaining posts and the 39 slowest rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#NIKKE4thAnniversary\""):
    lines[k]="            f'trend names \"#AlconMustStopPPGCollab\", \"Guehi\" and \"#YouManiacSeriesEP9\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words you/and"):
    lines[k]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1105Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 109"):
    lines[k]="            f'two screening reads by id: 103 unread referenced, reply-parent and media-source posts, most pointed-at first (100, then 3), with the 22 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
