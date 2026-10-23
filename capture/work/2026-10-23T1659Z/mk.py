s=open('build_capture.py').read()
TN_OLD='three of the top-ten US names with no posts attached in 1459Z: "Hellebuyck" (new), "Chad Patrick" (new) and "Oleshky" (last read in 1401Z); "Ethan Klein" and "Meghan" (read in 1459Z), "Fat Albert" and "#FridayVibes" (read in 1401Z), "Good Friday" (read in 1107Z) and "Dolan" (read in 1200Z) skipped, and "#LastFourWatched" is the same Friday film-list prompt as "#LetterboxdFriday" (read in 1459Z)'
TN='three of the top-ten US names with no posts attached in 1602Z: "Mercer" (new), "Lassie" (new) and "Jarmo" (new); "Mercer", "Jarmo", "Winnipeg" and "Devils" are one event with "Hellebuyck" (read in 1602Z): the Jets traded Connor Hellebuyck to the Devils for Dawson Mercer, Alexander Command, Nico Daws, Nick Bjugstad and two picks, and Sabres GM Jarmo Kekalainen is criticised for missing out; "Lassie" is the Breeders\' Cup horse Scottish Lassie; "Ethan Klein" and "Hila" (one h3h3 event, read in 1459Z) and "Oleshky" (read in 1602Z) skipped'
R=[
("Build capture/2026/10/23/1602Z.json","Build capture/2026/10/23/1659Z.json"),
("work/2026-10-23T1602Z'","work/2026-10-23T1659Z'"),
("RUN_ID = '2026-10-23T1602Z'","RUN_ID = '2026-10-23T1659Z'"),
("STARTED = '2026-10-23T16:02:00Z'","STARTED = '2026-10-23T16:59:00Z'"),
("OBS_AT = '2026-10-23T16:02:00Z'","OBS_AT = '2026-10-23T16:59:00Z'"),
("READS_BEFORE = 678","READS_BEFORE = 658"),
("datetime(2026,10,23,16,5,tzinfo=timezone.utc).timestamp()  # 1602Z (","datetime(2026,10,23,17,1,tzinfo=timezone.utc).timestamp()  # 1659Z (1602Z used 16:05, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',\n    'req_talarico': 'req_r-2026-10-23-01.txt', 'req_oleshky': 'req_r-2026-10-23-02.txt',"),
("'trend_hellebuyck': 'trend_hellebuyck.txt', 'trend_chadpatrick': 'trend_chadpatrick.txt', 'trend_oleshky': 'trend_oleshky.txt',","'trend_mercer': 'trend_mercer.txt', 'trend_lassie': 'trend_lassie.txt', 'trend_jarmo': 'trend_jarmo.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_hellebuyck','trend.Hellebuyck'),('trend_chadpatrick','trend.Chad Patrick'),('trend_oleshky','trend.Oleshky'),","('trend_mercer','trend.Mercer'),('trend_lassie','trend.Lassie'),('trend_jarmo','trend.Jarmo'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1602Z.json') and '/23/' in _c: continue","if _c.endswith('1659Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T1459Z'","_last = '2026-10-23T1602Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('\'2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\''),
("eighty-third run","eighty-fourth run"),
("eighty-first run","eighty-second run"),
("(this 16Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and fourth-hour tiers, the list was 563 long, so the 400 cap left out 163 (115 slowest-growing still-gaining and 48 fourth-hour), the slowest-growing","(this 17Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 514 long, so the 400 cap left out 114, the slowest-growing"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1602Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1659Z.json'"),
(TN_OLD, TN),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
('trend names "Hellebuyck", "Chad Patrick" and "Oleshky" ("<name> lang:en is:retweet", newest first, 25 each;','trend names "Mercer", "Lassie" and "Jarmo" ("<name> lang:en is:retweet", newest first, 25 each;'),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + and (quoted)"),
("        if str(_x) in ('trend.Hellebuyck','trend.Chad Patrick'): return 'sports'  # 1602Z","        if str(_x) in ('trend.Hellebuyck','trend.Chad Patrick'): return 'sports'  # 1602Z\n        if str(_x) in ('trend.Mercer','trend.Lassie','trend.Jarmo'): return 'sports'  # 1659Z"),
("REQ_PICKS = {}\nREQ_FILES = {}\nREQ_ONLY = set()",
 "REQ_PICKS = {'r-2026-10-23-01': ['2113606724188098991','2113463298498888090','2113532320485667327','2113611610317091142','2113516360588259686'], 'r-2026-10-23-02': ['2113664656984379402','2113665259428823051','2113664679952482591','2113661338484715693','2113665622961721590']}\nREQ_FILES = {'r-2026-10-23-01': 'req_talarico', 'r-2026-10-23-02': 'req_oleshky'}\nREQ_ONLY = ({t['id'] for t in (raw['req_talarico'].get('data') or [])} | {t['id'] for t in (raw['req_oleshky'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-23-01']) - set(REQ_PICKS['r-2026-10-23-02'])"),
("# 5) request picks (none this run)","# 5) request picks (1659Z: r-2026-10-23-01 and r-2026-10-23-02)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Midday run (12:02 PM ET"):
    lines[i]="            f'Midday run (12:59 PM ET Oct 23 / 16:59 UTC Oct 23, the 17Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 plus two request reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1602Z ended at 658, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 514 ids, so the 400 cap left out 114 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Hellebuyck"):
    lines[i]="            f'trend names \"Mercer\", \"Lassie\" and \"Jarmo\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'").replace("\\\\'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[i]="            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1602Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 6 more (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[i]="            f'Two new requests read once each (search_posts_all, relevancy, 25 results): r-2026-10-23-01 found no post from James Talarico or his campaign and no named outlet quoting them, only partisan reposts of the same voter ID clip text, two of which date the \"I oppose voter ID\" line to 2021; the five most liked are kept. r-2026-10-23-02 found the Russian side: Gerasimov (General Staff) announcing a ceasefire on the Kherson front from 04:00 Moscow time on 27 October (kadmitriev, nexta_tv, NOELreports, WarMonltor citing Interfax) and the Kremlin saying its military is working out the timing (TheInsiderPaper); no post from the Ukrainian president office or the Ukrainian southern command was returned; the five most liked are kept and no post showing residents was kept. Earlier requests were answered in earlier captures and not read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[i]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
