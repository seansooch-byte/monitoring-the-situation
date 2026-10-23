s=open('build_capture.py').read()
TN='three of the six top-ten US names with no posts attached in 1107Z: "#AlconMustEndPPGcollab", "#GenshinSpecialProgram" and "#BladeRunnerCollabswithRacist" (all new; "#BladeRunnerCollabswithRacist" and "#中国上海立刻解决叠纸争议" look like the Papergames campaign attached in 1201Z on Oct 22, so only the English tag was read; "Ethan Klein" and "Hila" read in 0905Z, so skipped; "Dolan" is the James Dolan trend attached in 1107Z)'
OLD_WN="(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 505 long, so the 400 cap left out the 105 slowest-growing still-gaining posts in order, and no cited post)"
WATCH_NOTE="(this 12Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last, the list was 569 long, so the 400 cap left out 169 posts (114 still-gaining, 53 fourth-hour, 2 six-hour) in order, and no cited post)"
R=[
("Build capture/2026/10/23/1107Z.json","Build capture/2026/10/23/1200Z.json"),
("work/2026-10-23T1107Z'","work/2026-10-23T1200Z'"),
("RUN_ID = '2026-10-23T1107Z'","RUN_ID = '2026-10-23T1200Z'"),
("STARTED = '2026-10-23T11:07:00Z'","STARTED = '2026-10-23T12:00:00Z'"),
("OBS_AT = '2026-10-23T11:07:00Z'","OBS_AT = '2026-10-23T12:00:00Z'"),
("READS_BEFORE = 778","READS_BEFORE = 758"),
("datetime(2026,10,23,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (","datetime(2026,10,23,12,3,tzinfo=timezone.utc).timestamp()  # 1200Z (1107Z used 11:10, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_goodfriday': 'trend_goodfriday.txt', 'trend_fatalbert': 'trend_fatalbert.txt', 'trend_jamesdolan': 'trend_jamesdolan.txt',","'trend_alcon': 'trend_alcon.txt', 'trend_genshin': 'trend_genshin.txt', 'trend_bladerunner': 'trend_bladerunner.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_goodfriday','trend.Good Friday'),('trend_fatalbert','trend.Fat Albert'),('trend_jamesdolan','trend.James Dolan'),","('trend_alcon','trend.#AlconMustEndPPGcollab'),('trend_genshin','trend.#GenshinSpecialProgram'),('trend_bladerunner','trend.#BladeRunnerCollabswithRacist'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1107Z.json') and '/23/' in _c: continue","if _c.endswith('1200Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T0959Z'","_last = '2026-10-23T1107Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('\'2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\''),
("seventy-eighth run","seventy-ninth run"),
("seventy-sixth run","seventy-seventh run"),
("in the 06:00-11:00 UTC band, up to 20","in the 12:00-05:00 UTC band, up to 42"),
(OLD_WN, WATCH_NOTE),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1200Z.json'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"#AlconMustEndPPGcollab\", \"#GenshinSpecialProgram\" and \"#BladeRunnerCollabswithRacist\" (\"<name> lang:en is:retweet\", newest first, 25 each, hashtags unquoted; "+TN.replace("'","\\'")+"); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread first-hop, most pointed-at first, then 12 more); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (7:07 AM ET"):
    lines[i]="            f'Morning run (8:00 AM ET Oct 23 / 12:00 UTC Oct 23, the 12Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1107Z ended at 758, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 569 ids, so the 400 cap left out 169 posts (114 still-gaining, 53 fourth-hour, 2 six-hour) in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Good Friday"):
    lines[i]="            f'trend names \"#AlconMustEndPPGcollab\", \"#GenshinSpecialProgram\" and \"#BladeRunnerCollabswithRacist\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[i]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1107Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 12 more (1746547721153241250, left out in 0606Z as likely paid, was not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
