s=open('build_capture.py').read()
TN='five of the top-ten US names with no posts attached in 0400Z: "Thompson" (first), "Wemby" (second) and "Sengun" (fourth), all Rockets 114, Spurs 110 (Amen Thompson game-sealing block on Victor Wembanyama) with "Spurs" (third) and "Rockets" (seventh), "Warriors" (fifth; Grizzlies comeback win over the Warriors, one event with "Grizzlies", ninth) and "#TheLastDriveIn" (eighth; the Shudder horror-movie show); "#WorldSeries" (sixth) had a post attached in 0400Z, and "Walker Kessler" (tenth) was cut for the five-read cap, so those were skipped'
R=[
("Build capture/2026/10/24/0400Z.json","Build capture/2026/10/24/0507Z.json"),
("work/2026-10-24T0400Z'","work/2026-10-24T0507Z'"),
("RUN_ID = '2026-10-24T0400Z'","RUN_ID = '2026-10-24T0507Z'"),
("STARTED = '2026-10-24T04:00:00Z'","STARTED = '2026-10-24T05:07:00Z'"),
("OBS_AT = '2026-10-24T04:00:00Z'","OBS_AT = '2026-10-24T05:07:00Z'"),
("READS_BEFORE = 915","READS_BEFORE = 893"),
("datetime(2026,10,24,4,2,tzinfo=timezone.utc).timestamp()  # 0400Z (","datetime(2026,10,24,5,8,tzinfo=timezone.utc).timestamp()  # 0507Z (0400Z used 04:02, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_megill': 'trend_megill.txt', 'trend_winourway': 'trend_winourway.txt', 'trend_deluca': 'trend_deluca.txt', 'trend_tatum': 'trend_tatum.txt', 'trend_smackdown': 'trend_smackdown.txt',","'trend_thompson': 'trend_thompson.txt', 'trend_wemby': 'trend_wemby.txt', 'trend_sengun': 'trend_sengun.txt', 'trend_warriors': 'trend_warriors.txt', 'trend_thelastdrivein': 'trend_thelastdrivein.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_megill','trend.Megill'),('trend_winourway','trend.#WinOurWay'),('trend_deluca','trend.DeLuca'),('trend_tatum','trend.Tatum'),('trend_smackdown','trend.#SmackDown'),","('trend_thompson','trend.Thompson'),('trend_wemby','trend.Wemby'),('trend_sengun','trend.Sengun'),('trend_warriors','trend.Warriors'),('trend_thelastdrivein','trend.#TheLastDriveIn'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) in ('trend.Megill','trend.#WinOurWay','trend.DeLuca'): return 'sports'  # 0400Z: World Series Game 1 (Brewers v Rays)",
 "        if str(_x) in ('trend.Megill','trend.#WinOurWay','trend.DeLuca'): return 'sports'  # 0400Z: World Series Game 1 (Brewers v Rays)\n        if str(_x) in ('trend.Thompson','trend.Wemby','trend.Sengun','trend.Warriors'): return 'sports'  # 0507Z: Rockets v Spurs and Grizzlies v Warriors\n        if str(_x)=='trend.#TheLastDriveIn': return 'entertainment'  # 0507Z: Shudder horror show"),
("if _c.endswith('0400Z.json') and '/24/' in _c: continue","if _c.endswith('0507Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T0303Z'","_last = '2026-10-24T0400Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)',
 'common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)'),
("quote/repost words is/you + and (quoted)","quote/repost words my/it + that (quoted)"),
("ninety-fourth run","ninety-fifth run"),
("ninety-second run","ninety-third run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0400Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0507Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0400Z: none read)","# 5) request picks (0507Z: none read)"),
("(this 04Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 540 long, so the 400 cap left out the 4 last six-hour posts, the 103 slowest-growing still-gaining posts and the 33 slowest rest-of-24-hour posts, and no cited post)",
 "(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 509 long, so the 400 cap left out the 3 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 21 second-hop posts they led to)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 35 remaining and second-hop posts they led to)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Megill", "#WinOurWay", "DeLuca", "Tatum" and "#SmackDown" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Thompson", "Wemby", "Sengun", "Warriors" and "#TheLastDriveIn" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Midnight run (12:00 AM ET"):
    lines[k]="            f'Night run (1:07 AM ET Oct 24 / 05:07 UTC Oct 24, the 05Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 15, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 509 ids, so the 400 cap left out the 3 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Megill\""):
    lines[k]="            f'trend names \"Thompson\", \"Wemby\", \"Sengun\", \"Warriors\" and \"#TheLastDriveIn\" (5 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words is/you"):
    lines[k]="            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0400Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 35 remaining and second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again; 12 third-hop or unreturned ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
