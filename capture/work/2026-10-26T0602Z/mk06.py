s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0502Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Mahomes" and "Seahawks"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Looney Tunes" and "Lula"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0502Z.json","Build capture/2026/10/26/0602Z.json"),
("work/2026-10-26T0502Z'","work/2026-10-26T0602Z'"),
("RUN_ID = '2026-10-26T0502Z'","RUN_ID = '2026-10-26T0602Z'"),
("STARTED = '2026-10-26T05:02:00Z'","STARTED = '2026-10-26T06:02:00Z'"),
("OBS_AT = '2026-10-26T05:03:00Z'","OBS_AT = '2026-10-26T06:03:00Z'"),
("READS_BEFORE = 899","READS_BEFORE = 880"),
("datetime(2026,10,26,5,3,tzinfo=timezone.utc).timestamp()  # 0502Z (","datetime(2026,10,26,6,3,tzinfo=timezone.utc).timestamp()  # 0602Z (0502Z used 05:03, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_mahomes': 'trend_mahomes.txt', 'trend_seahawks': 'trend_seahawks.txt',","'trend_looney': 'trend_looney.txt', 'trend_lula': 'trend_lula.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_mahomes','trend.Mahomes'),('trend_seahawks','trend.Seahawks'),","('trend_looney','trend.Looney Tunes'),('trend_lula','trend.Lula'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0502Z.json') and '/26/' in _c: continue","if _c.endswith('0602Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T0408Z'","_last = '2026-10-26T0502Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
 'common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)'),
("one hundred and forty-third run","one hundred and forty-fourth run"),
("one hundred and forty-first run","one hundred and forty-second run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0502Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0602Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0502Z: none read)","# 5) request picks (0602Z: none read)"),
("(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 579 long, so the 400 cap left out the 72 last six-hour posts and the 107 slowest-growing still-gaining posts, and no cited post)",
 "(this 06Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 72 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + and (quoted)"),
("        if str(_x)=='trend.Eric Bauza': return 'entertainment'  # 0408Z: voice actor","        if str(_x)=='trend.Eric Bauza': return 'entertainment'  # 0408Z: voice actor\n        if str(_x)=='trend.Looney Tunes': return 'entertainment'  # 0602Z: one event with Eric Bauza"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Looney Tunes\" and \"Lula\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words is/you + and (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Night run (1:02 AM ET":"            f'Overnight run (2:02 AM ET Oct 26 / 06:02 UTC Oct 26, the 06Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0502Z ended at 880, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 578 ids, so the 400 cap left out the 72 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Looney Tunes\"":"            f'trend names \"Looney Tunes\" and \"Lula\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words what/the":"            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0502Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 0502Z, and 2114404611331076530 came back Not Found; story clusters (search_news) not read for the budget. '",
"f'No new request: r-2026-10-26-01":"            f'No new request: r-2026-10-26-01 was answered in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
