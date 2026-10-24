s=open('build_capture.py').read()
OLDTN='two of the top-ten US names with no posts attached in 0804Z, one per event: "Thompson" (third; Rockets 114, Spurs 110, the Amen Thompson block on Wembanyama, one event with "Wemby", fourth, and "Spurs", fifth) and "#MCRLA2" (eighth; My Chemical Romance Los Angeles show); "#CulturalCreditMatters", "CULTURAL HERITAGE RECOGNITION", "Sengun", "Warriors" and "Grizzlies" had posts attached in 0804Z, and "Wemby", "Spurs" and "#ScarletHeartTH" (tenth; one event with "#CulturalCreditMatters") were cut as repeats of events already read or attached, so those were skipped'
TN='three of the top-ten US names with no posts attached in 0905Z, one per event: "#CulturalCreditMatters" (first; Myanmar fan campaign about Scarlet Heart Thailand, one event with "CULTURAL HERITAGE RECOGNITION", second, and "#ScarletHeartTH", seventh), "Good Saturday" (third; weekend greeting) and "#pw_mg" (ninth); "Wemby", "Spurs" and "#mcrla2" had posts attached in 0905Z, and "Amen Thompson" (fourth; Rockets 114, Spurs 110, one event with "Thompson", attached in 0905Z) and "Sengun" (tenth; same game) were cut as repeats of events already attached, so those were skipped'
R=[
("Build capture/2026/10/24/0905Z.json","Build capture/2026/10/24/1003Z.json"),
("work/2026-10-24T0905Z'","work/2026-10-24T1003Z'"),
("RUN_ID = '2026-10-24T0905Z'","RUN_ID = '2026-10-24T1003Z'"),
("STARTED = '2026-10-24T09:05:00Z'","STARTED = '2026-10-24T10:03:00Z'"),
("OBS_AT = '2026-10-24T09:05:00Z'","OBS_AT = '2026-10-24T10:03:00Z'"),
("READS_BEFORE = 811","READS_BEFORE = 792"),
("datetime(2026,10,24,9,6,tzinfo=timezone.utc).timestamp()  # 0905Z (","datetime(2026,10,24,10,4,tzinfo=timezone.utc).timestamp()  # 1003Z (0905Z used 09:06, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_thompson': 'trend_thompson.txt', 'trend_mcrla2': 'trend_mcrla2.txt',","'trend_culturalcreditmatters': 'trend_culturalcreditmatters.txt', 'trend_goodsaturday': 'trend_goodsaturday.txt', 'trend_pw_mg': 'trend_pw_mg.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_thompson','trend.Thompson'),('trend_mcrla2','trend.#MCRLA2'),","('trend_culturalcreditmatters','trend.#CulturalCreditMatters'),('trend_goodsaturday','trend.Good Saturday'),('trend_pw_mg','trend.#pw_mg'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0905Z.json') and '/24/' in _c: continue","if _c.endswith('1003Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T0804Z'","_last = '2026-10-24T0905Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("quote/repost words that/just + what (quoted)","quote/repost words the/this + is (quoted)"),
("ninety-ninth run","one hundredth run"),
("ninety-seventh run","ninety-eighth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0905Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/1003Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0905Z: none read)","# 5) request picks (1003Z: none read)"),
("two screening reads by id (90 unread referenced posts, most pointed-at first, then the 15 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 10 remaining and 20 second-hop posts they led to)"),
('trend names "Thompson" and "#MCRLA2" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "#CulturalCreditMatters", "Good Saturday" and "#pw_mg" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 532 long, so the 400 cap left out the 12 last six-hour posts and the 120 slowest-growing still-gaining posts, and no cited post)",
 "(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 534 long, so the 400 cap left out the 11 last six-hour posts and the 123 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Early morning run (5:05 AM ET"):
    lines[k]="            f'Morning run (6:03 AM ET Oct 24 / 10:03 UTC Oct 24, the 10Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 534 ids, so the 400 cap left out the 11 last six-hour posts and the 123 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Thompson\""):
    lines[k]="            f'trend names \"#CulturalCreditMatters\", \"Good Saturday\" and \"#pw_mg\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[k]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0905Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 90"):
    lines[k]="            f'two screening reads by id: 110 unread referenced, reply-parent and media-source posts, most pointed-at first (100, then 10), with the 20 second-hop posts they led to in the second read (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
