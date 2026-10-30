s=open('build_capture.py').read()
TN='four of the top-ten US names with no posts attached in 0200Z: "Giannis" (seventh) and "Brook Lopez" (fifth; one Bucks game), "Contreras" (sixth; with "Aaron Ashby" (eighth) one Brewers game) and "Paul Reed" (tenth); "#SmackDown" (first), "Tatum" (second), "#TheLastDriveIn" (fourth) and "#MutantFam" (ninth) had posts attached in 0200Z, "#WorldSeries" (third) was read in 0000Z, and "Aaron Ashby" is one event with "Contreras", so those were skipped'
R=[
("Build capture/2026/10/24/0200Z.json","Build capture/2026/10/24/0303Z.json"),
("work/2026-10-24T0200Z'","work/2026-10-24T0303Z'"),
("RUN_ID = '2026-10-24T0200Z'","RUN_ID = '2026-10-24T0303Z'"),
("STARTED = '2026-10-24T02:00:00Z'","STARTED = '2026-10-24T03:03:00Z'"),
("OBS_AT = '2026-10-24T02:00:00Z'","OBS_AT = '2026-10-24T03:03:00Z'"),
("READS_BEFORE = 958","READS_BEFORE = 937"),
("datetime(2026,10,24,2,1,tzinfo=timezone.utc).timestamp()  # 0200Z (","datetime(2026,10,24,3,4,tzinfo=timezone.utc).timestamp()  # 0303Z (0200Z used 02:01, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_tatum': 'trend_tatum.txt', 'trend_thelastdrivein': 'trend_thelastdrivein.txt', 'trend_michin': 'trend_michin.txt', 'trend_mikal': 'trend_mikal.txt',","'trend_giannis': 'trend_giannis.txt', 'trend_brooklopez': 'trend_brooklopez.txt', 'trend_contreras': 'trend_contreras.txt', 'trend_paulreed': 'trend_paulreed.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_tatum','trend.Tatum'),('trend_thelastdrivein','trend.#TheLastDriveIn'),('trend_michin','trend.Michin'),('trend_mikal','trend.Mikal'),","('trend_giannis','trend.Giannis'),('trend_brooklopez','trend.Brook Lopez'),('trend_contreras','trend.Contreras'),('trend_paulreed','trend.Paul Reed'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) in ('trend.#TheLastDriveIn',): return 'entertainment'  # 0200Z: Joe Bob Briggs horror show",
 "        if str(_x) in ('trend.#TheLastDriveIn',): return 'entertainment'  # 0200Z: Joe Bob Briggs horror show\n        if str(_x) in ('trend.Brook Lopez','trend.Contreras','trend.Paul Reed'): return 'sports'  # 0303Z: NBA and MLB games"),
("if _c.endswith('0200Z.json') and '/24/' in _c: continue","if _c.endswith('0303Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T0103Z'","_last = '2026-10-24T0200Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("quote/repost words it/that + just (quoted)","quote/repost words what/the + this (quoted)"),
("ninety-second run","ninety-third run"),
("ninetieth run","ninety-first run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0200Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0303Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0200Z: none read)","# 5) request picks (0303Z: none read)"),
("(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 514 long, so the 400 cap left out the 114 slowest-growing still-gaining posts, and no cited post)",
 "(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 518 long, so the 400 cap left out the 112 slowest-growing still-gaining posts and the 6 last six-hour posts, and no cited post)"),
("two screening reads by id (95 unread referenced posts, most pointed-at first, then the 23 second-hop posts they led to)","three screening reads by id (119 unread referenced posts, most pointed-at first, then the 27 second-hop posts they led to)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Tatum", "#TheLastDriveIn", "Michin" and "Mikal" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Giannis", "Brook Lopez", "Contreras" and "Paul Reed" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (10:00 PM ET"):
    lines[k]="            f'Late evening run (11:03 PM ET Oct 23 / 03:03 UTC Oct 24, the 03Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 14, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 518 ids, so the 400 cap left out the 112 slowest-growing still-gaining posts and the 6 last six-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Tatum\""):
    lines[k]="            f'trend names \"Giannis\", \"Brook Lopez\", \"Contreras\" and \"Paul Reed\" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[k]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0200Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 95"):
    lines[k]="            f'three screening reads by id: 119 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 27 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
