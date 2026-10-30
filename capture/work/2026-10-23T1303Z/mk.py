s=open('build_capture.py').read()
TN_OLD='three of the six top-ten US names with no posts attached in 1107Z: "#AlconMustEndPPGcollab", "#GenshinSpecialProgram" and "#BladeRunnerCollabswithRacist" (all new; "#AlconMustEndPPGcollab", "#BladeRunnerCollabswithRacist" and "#中国上海立刻解决叠纸争议" are one event, the Love and Deepspace (Papergames) fan campaign against the Blade Runner collab, and the same posts carry all three tags; "#GenshinSpecialProgram" is the Genshin Impact Version 7.2 Special Program; "Ethan Klein" and "Hila" read in 0905Z, so skipped; "Dolan" is the James Dolan trend attached in 1107Z)'
TN='three of the six top-ten US names with no posts attached in 1200Z: "Happy Friyay", "RED Friday" and "Hila" ("Hila" last read in 0905Z; "Good Friday" and "Fat Albert" read in 1107Z and "Ethan" is the same h3h3 event as "Hila", so skipped; "#中国上海立刻解决叠纸争议", "#AlconMustEndPPGcollab" and "#BladeRunnerCollabswithRacist" are the Papergames campaign attached in 1200Z, and "Dolan" was attached in 1200Z)'
OLD_WN="(this 12Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last, the list was 569 long, so the 400 cap left out 169 posts (114 still-gaining, 53 fourth-hour, 2 six-hour) in order, and no cited post)"
WATCH_NOTE="(this 13Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids the list was 515 long, so the 400 cap left out the 115 slowest-growing still-gaining posts in order, and no cited post)"
R=[
("Build capture/2026/10/23/1200Z.json","Build capture/2026/10/23/1303Z.json"),
("work/2026-10-23T1200Z'","work/2026-10-23T1303Z'"),
("RUN_ID = '2026-10-23T1200Z'","RUN_ID = '2026-10-23T1303Z'"),
("STARTED = '2026-10-23T12:00:00Z'","STARTED = '2026-10-23T13:03:00Z'"),
("OBS_AT = '2026-10-23T12:00:00Z'","OBS_AT = '2026-10-23T13:03:00Z'"),
("READS_BEFORE = 758","READS_BEFORE = 738"),
("datetime(2026,10,23,12,3,tzinfo=timezone.utc).timestamp()  # 1200Z (","datetime(2026,10,23,13,5,tzinfo=timezone.utc).timestamp()  # 1303Z (1200Z used 12:03, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_alcon': 'trend_alcon.txt', 'trend_genshin': 'trend_genshin.txt', 'trend_bladerunner': 'trend_bladerunner.txt',","'trend_happyfriyay': 'trend_happyfriyay.txt', 'trend_redfriday': 'trend_redfriday.txt', 'trend_hila': 'trend_hila.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_alcon','trend.#AlconMustEndPPGcollab'),('trend_genshin','trend.#GenshinSpecialProgram'),('trend_bladerunner','trend.#BladeRunnerCollabswithRacist'),","('trend_happyfriyay','trend.Happy Friyay'),('trend_redfriday','trend.RED Friday'),('trend_hila','trend.Hila'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1200Z.json') and '/23/' in _c: continue","if _c.endswith('1303Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T1107Z'","_last = '2026-10-23T1200Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('\'2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each\''),
("seventy-ninth run","eightieth run"),
("seventy-seventh run","seventy-eighth run"),
(OLD_WN, WATCH_NOTE),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1200Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1303Z.json'"),
(TN_OLD, TN),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
('trend names "#AlconMustEndPPGcollab", "#GenshinSpecialProgram" and "#BladeRunnerCollabswithRacist" ("<name> lang:en is:retweet", newest first, 25 each, hashtags unquoted;','trend names "Happy Friyay", "RED Friday" and "Hila" ("<name> lang:en is:retweet", newest first, 25 each;'),
("quote/repost words that/just + what (quoted)","quote/repost words the/this + is (quoted)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (8:00 AM ET"):
    lines[i]="            f'Morning run (9:03 AM ET Oct 23 / 13:03 UTC Oct 23, the 13Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1200Z ended at 738, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 515 ids, so the 400 cap left out the 115 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#AlconMustEndPPGcollab"):
    lines[i]="            f'trend names \"Happy Friyay\", \"RED Friday\" and \"Hila\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[i]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1200Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 14 more (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
