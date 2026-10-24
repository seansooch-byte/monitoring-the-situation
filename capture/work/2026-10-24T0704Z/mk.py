s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0507Z, one per event: "Spurs" (third; Rockets 114, Spurs 110, one event with "Thompson", "Wemby", "Sengun" and "Rockets", seventh), "Grizzlies" (eighth; Grizzlies v Warriors, one event with "Warriors") and "#CulturalCreditMatters" (ninth; Myanmar fan campaign about Scarlet Heart Thailand, one event with "CULTURAL HERITAGE RECOGNITION", tenth); "Thompson", "Wemby", "Sengun", "Warriors" and "#TheLastDriveIn" had posts attached in 0507Z, and "Rockets" and "CULTURAL HERITAGE RECOGNITION" were cut for the three-read cap as repeats of an event already read, so those were skipped'
TN='three of the top-ten US names with no posts attached in 0602Z, one per event: "Wemby" (second; Rockets 114, Spurs 110, the Amen Thompson block on Wembanyama, one event with "Sengun", sixth), "#TheLastDriveIn" (eighth; Joe Bob Briggs Halloween show on Shudder) and "#MCRLA2" (tenth; My Chemical Romance Los Angeles show); "Thompson", "Spurs", "#CulturalCreditMatters", "CULTURAL HERITAGE RECOGNITION", "Warriors" and "Grizzlies" had posts attached in 0602Z, and "Sengun" was cut for the three-read cap as a repeat of an event already read, so those were skipped'
R=[
("Build capture/2026/10/24/0602Z.json","Build capture/2026/10/24/0704Z.json"),
("work/2026-10-24T0602Z'","work/2026-10-24T0704Z'"),
("RUN_ID = '2026-10-24T0602Z'","RUN_ID = '2026-10-24T0704Z'"),
("STARTED = '2026-10-24T06:02:00Z'","STARTED = '2026-10-24T07:04:00Z'"),
("OBS_AT = '2026-10-24T06:02:00Z'","OBS_AT = '2026-10-24T07:04:00Z'"),
("READS_BEFORE = 871","READS_BEFORE = 851"),
("datetime(2026,10,24,6,4,tzinfo=timezone.utc).timestamp()  # 0602Z (","datetime(2026,10,24,7,6,tzinfo=timezone.utc).timestamp()  # 0704Z (0602Z used 06:04, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_spurs': 'trend_spurs.txt', 'trend_grizzlies': 'trend_grizzlies.txt', 'trend_culturalcreditmatters': 'trend_culturalcreditmatters.txt',","'trend_wemby': 'trend_wemby.txt', 'trend_thelastdrivein': 'trend_thelastdrivein.txt', 'trend_mcrla2': 'trend_mcrla2.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_spurs','trend.Spurs'),('trend_grizzlies','trend.Grizzlies'),('trend_culturalcreditmatters','trend.#CulturalCreditMatters'),","('trend_wemby','trend.Wemby'),('trend_thelastdrivein','trend.#TheLastDriveIn'),('trend_mcrla2','trend.#MCRLA2'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x)=='trend.#CulturalCreditMatters': return 'entertainment'  # 0602Z: Myanmar fan campaign about Scarlet Heart Thailand",
 "        if str(_x)=='trend.#CulturalCreditMatters': return 'entertainment'  # 0602Z: Myanmar fan campaign about Scarlet Heart Thailand\n        if str(_x)=='trend.#MCRLA2': return 'music'  # 0704Z: My Chemical Romance Los Angeles show"),
("if _c.endswith('0602Z.json') and '/24/' in _c: continue","if _c.endswith('0704Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T0507Z'","_last = '2026-10-24T0602Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("quote/repost words just/what + the (quoted)","quote/repost words this/is + you (quoted)"),
("ninety-sixth run","ninety-seventh run"),
("ninety-fourth run","ninety-fifth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0602Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0704Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0602Z: none read)","# 5) request picks (0704Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 41 remaining and second-hop posts they led to)","two screening reads by id (97 unread referenced posts, most pointed-at first, then the 19 second-hop posts they led to)"),
('trend names "Spurs", "Grizzlies" and "#CulturalCreditMatters" ("<name> lang:en is:retweet", newest first, 25 each; '+OLDTN,
 'trend names "Wemby", "#TheLastDriveIn" and "#MCRLA2" ("<name> lang:en is:retweet", newest first, 25 each; '+TN),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (2:02 AM ET"):
    lines[k]="            f'Overnight run (3:04 AM ET Oct 24 / 07:04 UTC Oct 24, the 07Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 525 ids, so the 400 cap left out the 15 last six-hour posts and the 110 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Spurs\""):
    lines[k]="            f'trend names \"Wemby\", \"#TheLastDriveIn\" and \"#MCRLA2\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[k]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0602Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 97 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 19 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
