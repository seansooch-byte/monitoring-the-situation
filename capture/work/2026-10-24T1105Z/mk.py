s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0905Z, one per event: "#CulturalCreditMatters" (first; Myanmar fan campaign about Scarlet Heart Thailand, one event with "CULTURAL HERITAGE RECOGNITION", second, and "#ScarletHeartTH", seventh), "Good Saturday" (third; weekend greeting) and "#pw_mg" (ninth); "Wemby", "Spurs" and "#mcrla2" had posts attached in 0905Z, and "Amen Thompson" (fourth; Rockets 114, Spurs 110, one event with "Thompson", attached in 0905Z) and "Sengun" (tenth; same game) were cut as repeats of events already attached, so those were skipped'
TN='three of the top-ten US names with no posts attached in 1003Z, one per event: "#NIKKE4thAnniversary" (first; Goddess of Victory: NIKKE game fourth-anniversary countdown), "Wemby" (fifth; Rockets 114, Spurs 110, the Amen Thompson block on Wembanyama, one event with "Amen Thompson", sixth, and "Spurs", seventh) and "Warriors" (tenth; Grizzlies comeback win over the Warriors); "Good Saturday", "#CulturalCreditMatters", "CULTURAL HERITAGE RECOGNITION", "#ScarletHeartTH" and "#pw_mg" had posts attached in 1003Z, and "Amen Thompson" and "Spurs" were cut as one event with "Wemby", so those were skipped'
R=[
("Build capture/2026/10/24/1003Z.json","Build capture/2026/10/24/1105Z.json"),
("work/2026-10-24T1003Z'","work/2026-10-24T1105Z'"),
("RUN_ID = '2026-10-24T1003Z'","RUN_ID = '2026-10-24T1105Z'"),
("STARTED = '2026-10-24T10:03:00Z'","STARTED = '2026-10-24T11:05:00Z'"),
("OBS_AT = '2026-10-24T10:03:00Z'","OBS_AT = '2026-10-24T11:05:00Z'"),
("READS_BEFORE = 792","READS_BEFORE = 772"),
("datetime(2026,10,24,10,4,tzinfo=timezone.utc).timestamp()  # 1003Z (","datetime(2026,10,24,11,7,tzinfo=timezone.utc).timestamp()  # 1105Z (1003Z used 10:04, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_culturalcreditmatters': 'trend_culturalcreditmatters.txt', 'trend_goodsaturday': 'trend_goodsaturday.txt', 'trend_pw_mg': 'trend_pw_mg.txt',","'trend_nikke4thanniversary': 'trend_nikke4thanniversary.txt', 'trend_wemby': 'trend_wemby.txt', 'trend_warriors': 'trend_warriors.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_culturalcreditmatters','trend.#CulturalCreditMatters'),('trend_goodsaturday','trend.Good Saturday'),('trend_pw_mg','trend.#pw_mg'),","('trend_nikke4thanniversary','trend.#NIKKE4thAnniversary'),('trend_wemby','trend.Wemby'),('trend_warriors','trend.Warriors'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1003Z.json') and '/24/' in _c: continue","if _c.endswith('1105Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T0905Z'","_last = '2026-10-24T1003Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)"),
("one hundredth run","one hundred and first run"),
("ninety-eighth run","ninety-ninth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1003Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1105Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1003Z: none read)","# 5) request picks (1105Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 10 remaining and 20 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 9 remaining and 22 second-hop posts they led to)"),
('trend names "#CulturalCreditMatters", "Good Saturday" and "#pw_mg" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "#NIKKE4thAnniversary", "Wemby" and "Warriors" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 534 long, so the 400 cap left out the 11 last six-hour posts and the 123 slowest-growing still-gaining posts, and no cited post)",
 "(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 544 long, so the 400 cap left out the 25 last six-hour posts and the 119 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (6:03 AM ET"):
    lines[k]="            f'Morning run (7:05 AM ET Oct 24 / 11:05 UTC Oct 24, the 11Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 544 ids, so the 400 cap left out the 25 last six-hour posts and the 119 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#CulturalCreditMatters\""):
    lines[k]="            f'trend names \"#NIKKE4thAnniversary\", \"Wemby\" and \"Warriors\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[k]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1003Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 110"):
    lines[k]="            f'two screening reads by id: 109 unread referenced, reply-parent and media-source posts, most pointed-at first (100, then 9), with the 22 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
