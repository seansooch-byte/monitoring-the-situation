s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0704Z, one per event: "#CulturalCreditMatters" (third; Myanmar fan campaign about Scarlet Heart Thailand, one event with "CULTURAL HERITAGE RECOGNITION", fourth), "Sengun" (sixth; Rockets 114, Spurs 110) and "Grizzlies" (ninth; Grizzlies v Warriors); "Thompson", "Wemby", "Spurs", "Warriors", "#TheLastDriveIn" and "#MCRLA2" had posts attached in 0704Z, and "CULTURAL HERITAGE RECOGNITION" was cut for the three-read cap as a repeat of an event already read, so those were skipped'
TN='two of the top-ten US names with no posts attached in 0804Z, one per event: "Thompson" (third; Rockets 114, Spurs 110, the Amen Thompson block on Wembanyama, one event with "Wemby", fourth, and "Spurs", fifth) and "#MCRLA2" (eighth; My Chemical Romance Los Angeles show); "#CulturalCreditMatters", "CULTURAL HERITAGE RECOGNITION", "Sengun", "Warriors" and "Grizzlies" had posts attached in 0804Z, and "Wemby", "Spurs" and "#ScarletHeartTH" (tenth; one event with "#CulturalCreditMatters") were cut as repeats of events already read or attached, so those were skipped'
R=[
("Build capture/2026/10/24/0804Z.json","Build capture/2026/10/24/0905Z.json"),
("work/2026-10-24T0804Z'","work/2026-10-24T0905Z'"),
("RUN_ID = '2026-10-24T0804Z'","RUN_ID = '2026-10-24T0905Z'"),
("STARTED = '2026-10-24T08:04:00Z'","STARTED = '2026-10-24T09:05:00Z'"),
("OBS_AT = '2026-10-24T08:04:00Z'","OBS_AT = '2026-10-24T09:05:00Z'"),
("READS_BEFORE = 831","READS_BEFORE = 811"),
("datetime(2026,10,24,8,5,tzinfo=timezone.utc).timestamp()  # 0804Z (","datetime(2026,10,24,9,6,tzinfo=timezone.utc).timestamp()  # 0905Z (0804Z used 08:05, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_culturalcreditmatters': 'trend_culturalcreditmatters.txt', 'trend_sengun': 'trend_sengun.txt', 'trend_grizzlies': 'trend_grizzlies.txt',","'trend_thompson': 'trend_thompson.txt', 'trend_mcrla2': 'trend_mcrla2.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_culturalcreditmatters','trend.#CulturalCreditMatters'),('trend_sengun','trend.Sengun'),('trend_grizzlies','trend.Grizzlies'),","('trend_thompson','trend.Thompson'),('trend_mcrla2','trend.#MCRLA2'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0804Z.json') and '/24/' in _c: continue","if _c.endswith('0905Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T0704Z'","_last = '2026-10-24T0804Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("quote/repost words and/my + it (quoted)","quote/repost words that/just + what (quoted)"),
("ninety-eighth run","ninety-ninth run"),
("ninety-sixth run","ninety-seventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0804Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0905Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0804Z: none read)","# 5) request picks (0905Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 7 remaining and 19 second-hop posts they led to)","two screening reads by id (90 unread referenced posts, most pointed-at first, then the 15 second-hop posts they led to)"),
('trend names "#CulturalCreditMatters", "Sengun" and "Grizzlies" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Thompson" and "#MCRLA2" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 08Z run is a fourth hour, so the rest-of-24-hour tier was added; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 559 long, so the 400 cap left out the 9 last six-hour posts, the 118 slowest-growing still-gaining posts and the 32 slowest rest-of-24-hour posts, and no cited post)",
 "(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 532 long, so the 400 cap left out the 12 last six-hour posts and the 120 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (4:04 AM ET"):
    lines[k]="            f'Early morning run (5:05 AM ET Oct 24 / 09:05 UTC Oct 24, the 09Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 532 ids, so the 400 cap left out the 12 last six-hour posts and the 120 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#CulturalCreditMatters\""):
    lines[k]="            f'trend names \"Thompson\" and \"#MCRLA2\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[k]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0804Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 90 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 15 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
