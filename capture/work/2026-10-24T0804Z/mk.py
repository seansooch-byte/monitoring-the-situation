s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0602Z, one per event: "Wemby" (second; Rockets 114, Spurs 110, the Amen Thompson block on Wembanyama, one event with "Sengun", sixth), "#TheLastDriveIn" (eighth; Joe Bob Briggs Halloween show on Shudder) and "#MCRLA2" (tenth; My Chemical Romance Los Angeles show); "Thompson", "Spurs", "#CulturalCreditMatters", "CULTURAL HERITAGE RECOGNITION", "Warriors" and "Grizzlies" had posts attached in 0602Z, and "Sengun" was cut for the three-read cap as a repeat of an event already read, so those were skipped'
TN='three of the top-ten US names with no posts attached in 0704Z, one per event: "#CulturalCreditMatters" (third; Myanmar fan campaign about Scarlet Heart Thailand, one event with "CULTURAL HERITAGE RECOGNITION", fourth), "Sengun" (sixth; Rockets 114, Spurs 110) and "Grizzlies" (ninth; Grizzlies v Warriors); "Thompson", "Wemby", "Spurs", "Warriors", "#TheLastDriveIn" and "#MCRLA2" had posts attached in 0704Z, and "CULTURAL HERITAGE RECOGNITION" was cut for the three-read cap as a repeat of an event already read, so those were skipped'
R=[
("Build capture/2026/10/24/0704Z.json","Build capture/2026/10/24/0804Z.json"),
("work/2026-10-24T0704Z'","work/2026-10-24T0804Z'"),
("RUN_ID = '2026-10-24T0704Z'","RUN_ID = '2026-10-24T0804Z'"),
("STARTED = '2026-10-24T07:04:00Z'","STARTED = '2026-10-24T08:04:00Z'"),
("OBS_AT = '2026-10-24T07:04:00Z'","OBS_AT = '2026-10-24T08:04:00Z'"),
("READS_BEFORE = 851","READS_BEFORE = 831"),
("datetime(2026,10,24,7,6,tzinfo=timezone.utc).timestamp()  # 0704Z (","datetime(2026,10,24,8,5,tzinfo=timezone.utc).timestamp()  # 0804Z (0704Z used 07:06, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_wemby': 'trend_wemby.txt', 'trend_thelastdrivein': 'trend_thelastdrivein.txt', 'trend_mcrla2': 'trend_mcrla2.txt',","'trend_culturalcreditmatters': 'trend_culturalcreditmatters.txt', 'trend_sengun': 'trend_sengun.txt', 'trend_grizzlies': 'trend_grizzlies.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_wemby','trend.Wemby'),('trend_thelastdrivein','trend.#TheLastDriveIn'),('trend_mcrla2','trend.#MCRLA2'),","('trend_culturalcreditmatters','trend.#CulturalCreditMatters'),('trend_sengun','trend.Sengun'),('trend_grizzlies','trend.Grizzlies'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0704Z.json') and '/24/' in _c: continue","if _c.endswith('0804Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T0602Z'","_last = '2026-10-24T0704Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("quote/repost words this/is + you (quoted)","quote/repost words and/my + it (quoted)"),
("ninety-seventh run","ninety-eighth run"),
("ninety-fifth run","ninety-sixth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0704Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0804Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0704Z: none read)","# 5) request picks (0804Z: none read)"),
("two screening reads by id (97 unread referenced posts, most pointed-at first, then the 19 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 7 remaining and 19 second-hop posts they led to)"),
('trend names "Wemby", "#TheLastDriveIn" and "#MCRLA2" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "#CulturalCreditMatters", "Sengun" and "Grizzlies" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
("(this 06Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 515 long, so the 400 cap left out the 10 last six-hour posts and the 105 slowest-growing still-gaining posts, and no cited post)",
 "(this 08Z run is a fourth hour, so the rest-of-24-hour tier was added; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 559 long, so the 400 cap left out the 9 last six-hour posts, the 118 slowest-growing still-gaining posts and the 32 slowest rest-of-24-hour posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (3:04 AM ET"):
    lines[k]="            f'Overnight run (4:04 AM ET Oct 24 / 08:04 UTC Oct 24, the 08Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 559 ids, so the 400 cap left out the 9 last six-hour posts, the 118 slowest-growing still-gaining posts and the 32 slowest rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Wemby\""):
    lines[k]="            f'trend names \"#CulturalCreditMatters\", \"Sengun\" and \"Grizzlies\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[k]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0704Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 97"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 7 remaining and the 19 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
