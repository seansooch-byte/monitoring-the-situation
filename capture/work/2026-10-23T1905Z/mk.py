import re
s=open('build_capture.py').read()
TN='two of the top-ten US names with no posts attached in 1808Z: "1 Pro" (new) and "Lassie" (last read in 1659Z); "Ethan" and "Hila" are one h3h3 event with "Ethan Klein" (read in 1808Z), "Mercer", "Devils", "Hellebuyck" and "Winnipeg" are the Jets-Devils Hellebuyck trade (read in 1602Z and 1659Z), "Dan Sullivan" was read in 1808Z, and "#MGSMC2AlienwareSweepstakes" is a giveaway, so those were skipped; the "1 Pro" stream matches the words in unrelated posts (product names and a thread numbered 1/) and shows no single event; the "Lassie" stream mixes the Breeders Cup horse Scottish Lassie with posts about the TV collie'
R=[
("Build capture/2026/10/23/1808Z.json","Build capture/2026/10/23/1905Z.json"),
("work/2026-10-23T1808Z'","work/2026-10-23T1905Z'"),
("RUN_ID = '2026-10-23T1808Z'","RUN_ID = '2026-10-23T1905Z'"),
("STARTED = '2026-10-23T18:08:00Z'","STARTED = '2026-10-23T19:05:00Z'"),
("OBS_AT = '2026-10-23T18:08:00Z'","OBS_AT = '2026-10-23T19:05:00Z'"),
("READS_BEFORE = 636","READS_BEFORE = 617"),
("datetime(2026,10,23,18,10,tzinfo=timezone.utc).timestamp()  # 1808Z (","datetime(2026,10,23,19,7,tzinfo=timezone.utc).timestamp()  # 1905Z (1808Z used 18:10, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt',"),
("'repost_just': 'repost_just.txt',\n    'req_oleshky': 'req_r-2026-10-23-02.txt',","'repost_the': 'repost_the.txt',"),
("'trend_dansullivan': 'trend_dansullivan.txt', 'trend_ethanklein': 'trend_ethanklein.txt',","'trend_1pro': 'trend_1pro.txt', 'trend_lassie': 'trend_lassie.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'screen0': 'screen0.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_my','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_dansullivan','trend.Dan Sullivan'),('trend_ethanklein','trend.Ethan Klein'),","('trend_1pro','trend.1 Pro'),('trend_lassie','trend.Lassie'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1808Z.json') and '/23/' in _c: continue","if _c.endswith('1905Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T1659Z'","_last = '2026-10-23T1808Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "my", "what" and "the", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each\''),
("eighty-fifth run","eighty-sixth run"),
("eighty-third run","eighty-fourth run"),
("(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 511 long, so the 400 cap left out 111, the slowest-growing","(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 526 long, so the 400 cap left out 126 (120 slowest-growing still-gaining and the 6 last-listed six-hour posts), the slowest-growing"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1808Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1905Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("ANSWERED_EARLIER = {'r-2026-10-23-01':'2026-10-23T1659Z',","ANSWERED_EARLIER = {'r-2026-10-23-02':'2026-10-23T1808Z','r-2026-10-23-01':'2026-10-23T1659Z',"),
("# 5) request picks (1808Z: r-2026-10-23-02 re-read once after the editor rewrote the ask)","# 5) request picks (1905Z: none read)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Dan Sullivan" and "Ethan Klein" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find(')',s.find('skipped',i))
print('VIRAL SEG',i,s[j-120:j+5])
s=s[:i]+'trend names "1 Pro" and "Lassie" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
a=s.find("REQ_PICKS = {"); b=s.find("ADDED_STORY = ",a)
s=s[:a]+"REQ_PICKS = {}\nREQ_FILES = {}\nREQ_ONLY = set()\n"+s[b:]
a=s.find("ANSWERS = [{"); b=s.find("}]\ncapture = {",a)
s=s[:a]+"ANSWERS = []\ncapture = {"+s[b+len("}]\ncapture = {"):]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Afternoon run (2:08 PM ET"):
    lines[k]="            f'Afternoon run (3:05 PM ET Oct 23 / 19:05 UTC Oct 23, the 19Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1808Z ended at 617, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 526 ids, so the 400 cap left out 126 in order (120 slowest-growing still-gaining and the 6 last-listed six-hour posts) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Dan Sullivan"):
    lines[k]="            f'trend names \"1 Pro\" and \"Lassie\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[k]="            f'quote/repost words my/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1808Z, next in rotation); '"; hit+=1
  elif st.startswith("f'one screening read by id"):
    lines[k]="            f'two screening reads by id: 98 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 17 second-hop posts they pointed at (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 returned Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Request r-2026-10-23-02 read once more"):
    lines[k]="            f'No new request: r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
