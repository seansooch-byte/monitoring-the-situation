s=open('build_capture.py').read()
TN='five of the top-ten US names with no posts attached in 0303Z: "Megill" (fifth), "#WinOurWay" (seventh) and "DeLuca" (tenth), all World Series Game 1 (Brewers v Rays) with "#Brewers" (eighth) and "#WorldSeries" (first), "Tatum" (second; Celtics game) and "#SmackDown" (fourth; WWE); "Giannis" (sixth) and "Brook Lopez" (ninth) had posts attached in 0303Z, "#WorldSeries" had a post attached in 0303Z, "#Brewers" is one event with "Megill", and "#TheLastDriveIn" (third) was cut for the five-read cap, so those were skipped'
R=[
("Build capture/2026/10/24/0303Z.json","Build capture/2026/10/24/0400Z.json"),
("work/2026-10-24T0303Z'","work/2026-10-24T0400Z'"),
("RUN_ID = '2026-10-24T0303Z'","RUN_ID = '2026-10-24T0400Z'"),
("STARTED = '2026-10-24T03:03:00Z'","STARTED = '2026-10-24T04:00:00Z'"),
("OBS_AT = '2026-10-24T03:03:00Z'","OBS_AT = '2026-10-24T04:00:00Z'"),
("READS_BEFORE = 937","READS_BEFORE = 915"),
("datetime(2026,10,24,3,4,tzinfo=timezone.utc).timestamp()  # 0303Z (","datetime(2026,10,24,4,2,tzinfo=timezone.utc).timestamp()  # 0400Z (0303Z used 03:04, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_giannis': 'trend_giannis.txt', 'trend_brooklopez': 'trend_brooklopez.txt', 'trend_contreras': 'trend_contreras.txt', 'trend_paulreed': 'trend_paulreed.txt',","'trend_megill': 'trend_megill.txt', 'trend_winourway': 'trend_winourway.txt', 'trend_deluca': 'trend_deluca.txt', 'trend_tatum': 'trend_tatum.txt', 'trend_smackdown': 'trend_smackdown.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_giannis','trend.Giannis'),('trend_brooklopez','trend.Brook Lopez'),('trend_contreras','trend.Contreras'),('trend_paulreed','trend.Paul Reed'),","('trend_megill','trend.Megill'),('trend_winourway','trend.#WinOurWay'),('trend_deluca','trend.DeLuca'),('trend_tatum','trend.Tatum'),('trend_smackdown','trend.#SmackDown'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) in ('trend.Brook Lopez','trend.Contreras','trend.Paul Reed'): return 'sports'  # 0303Z: NBA and MLB games",
 "        if str(_x) in ('trend.Brook Lopez','trend.Contreras','trend.Paul Reed'): return 'sports'  # 0303Z: NBA and MLB games\n        if str(_x) in ('trend.Megill','trend.#WinOurWay','trend.DeLuca'): return 'sports'  # 0400Z: World Series Game 1 (Brewers v Rays)"),
("if _c.endswith('0303Z.json') and '/24/' in _c: continue","if _c.endswith('0400Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T0200Z'","_last = '2026-10-24T0303Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
 'common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)'),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + and (quoted)"),
("ninety-third run","ninety-fourth run"),
("ninety-first run","ninety-second run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0303Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0400Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0303Z: none read)","# 5) request picks (0400Z: none read)"),
("(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 518 long, so the 400 cap left out the 112 slowest-growing still-gaining posts and the 6 last six-hour posts, and no cited post)",
 "(this 04Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 540 long, so the 400 cap left out the 4 last six-hour posts, the 103 slowest-growing still-gaining posts and the 33 slowest rest-of-24-hour posts, and no cited post)"),
("three screening reads by id (119 unread referenced posts, most pointed-at first, then the 27 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 21 second-hop posts they led to)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Giannis", "Brook Lopez", "Contreras" and "Paul Reed" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Megill", "#WinOurWay", "DeLuca", "Tatum" and "#SmackDown" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Late evening run (11:03 PM ET"):
    lines[k]="            f'Midnight run (12:00 AM ET Oct 24 / 04:00 UTC Oct 24, the 04Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 15, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 540 ids, so the 400 cap left out the 4 last six-hour posts, the 103 slowest-growing still-gaining posts and the 33 slowest rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Giannis\""):
    lines[k]="            f'trend names \"Megill\", \"#WinOurWay\", \"DeLuca\", \"Tatum\" and \"#SmackDown\" (5 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[k]="            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0303Z, next in rotation); '"; hit+=1
  elif st.startswith("f'three screening reads by id: 119"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 21 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
