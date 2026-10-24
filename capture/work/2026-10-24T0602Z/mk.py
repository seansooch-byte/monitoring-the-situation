s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0507Z, one per event: "Spurs" (third; Rockets 114, Spurs 110, one event with "Thompson", "Wemby", "Sengun" and "Rockets", seventh), "Grizzlies" (eighth; Grizzlies v Warriors, one event with "Warriors") and "#CulturalCreditMatters" (ninth; Myanmar fan campaign about Scarlet Heart Thailand, one event with "CULTURAL HERITAGE RECOGNITION", tenth); "Thompson", "Wemby", "Sengun", "Warriors" and "#TheLastDriveIn" had posts attached in 0507Z, and "Rockets" and "CULTURAL HERITAGE RECOGNITION" were cut for the three-read cap as repeats of an event already read, so those were skipped'
R=[
("Build capture/2026/10/24/0507Z.json","Build capture/2026/10/24/0602Z.json"),
("work/2026-10-24T0507Z'","work/2026-10-24T0602Z'"),
("RUN_ID = '2026-10-24T0507Z'","RUN_ID = '2026-10-24T0602Z'"),
("STARTED = '2026-10-24T05:07:00Z'","STARTED = '2026-10-24T06:02:00Z'"),
("OBS_AT = '2026-10-24T05:07:00Z'","OBS_AT = '2026-10-24T06:02:00Z'"),
("READS_BEFORE = 893","READS_BEFORE = 871"),
("datetime(2026,10,24,5,8,tzinfo=timezone.utc).timestamp()  # 0507Z (","datetime(2026,10,24,6,4,tzinfo=timezone.utc).timestamp()  # 0602Z (0507Z used 05:08, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_thompson': 'trend_thompson.txt', 'trend_wemby': 'trend_wemby.txt', 'trend_sengun': 'trend_sengun.txt', 'trend_warriors': 'trend_warriors.txt', 'trend_thelastdrivein': 'trend_thelastdrivein.txt',","'trend_spurs': 'trend_spurs.txt', 'trend_grizzlies': 'trend_grizzlies.txt', 'trend_culturalcreditmatters': 'trend_culturalcreditmatters.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_thompson','trend.Thompson'),('trend_wemby','trend.Wemby'),('trend_sengun','trend.Sengun'),('trend_warriors','trend.Warriors'),('trend_thelastdrivein','trend.#TheLastDriveIn'),","('trend_spurs','trend.Spurs'),('trend_grizzlies','trend.Grizzlies'),('trend_culturalcreditmatters','trend.#CulturalCreditMatters'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x)=='trend.#TheLastDriveIn': return 'entertainment'  # 0507Z: Shudder horror show",
 "        if str(_x)=='trend.#TheLastDriveIn': return 'entertainment'  # 0507Z: Shudder horror show\n        if str(_x) in ('trend.Spurs','trend.Grizzlies'): return 'sports'  # 0602Z: Rockets v Spurs and Grizzlies v Warriors\n        if str(_x)=='trend.#CulturalCreditMatters': return 'entertainment'  # 0602Z: Myanmar fan campaign about Scarlet Heart Thailand"),
("if _c.endswith('0507Z.json') and '/24/' in _c: continue","if _c.endswith('0602Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T0400Z'","_last = '2026-10-24T0507Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
 'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)'),
("quote/repost words my/it + that (quoted)","quote/repost words just/what + the (quoted)"),
("ninety-fifth run","ninety-sixth run"),
("ninety-third run","ninety-fourth run"),
("in the 12:00-05:00 UTC band, up to 42","in the 06:00-11:00 UTC band, up to 20"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0507Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0602Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0507Z: none read)","# 5) request picks (0602Z: none read)"),
("(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 509 long, so the 400 cap left out the 3 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post)",
 "(this 06Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 515 long, so the 400 cap left out the 10 last six-hour posts and the 105 slowest-growing still-gaining posts, and no cited post)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 35 remaining and second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 41 remaining and second-hop posts they led to)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Thompson", "Wemby", "Sengun", "Warriors" and "#TheLastDriveIn" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Spurs", "Grizzlies" and "#CulturalCreditMatters" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Night run (1:07 AM ET"):
    lines[k]="            f'Overnight run (2:02 AM ET Oct 24 / 06:02 UTC Oct 24, the 06Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 515 ids, so the 400 cap left out the 10 last six-hour posts and the 105 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Thompson\""):
    lines[k]="            f'trend names \"Spurs\", \"Grizzlies\" and \"#CulturalCreditMatters\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[k]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0507Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 41 remaining and second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again; third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
