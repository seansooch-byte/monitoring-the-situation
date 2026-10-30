s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0709Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Jalen Williams" and "Komanche"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Eric Bauza" and "Chiefs"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0709Z.json","Build capture/2026/10/26/0800Z.json"),
("work/2026-10-26T0709Z'","work/2026-10-26T0800Z'"),
("RUN_ID = '2026-10-26T0709Z'","RUN_ID = '2026-10-26T0800Z'"),
("STARTED = '2026-10-26T07:09:00Z'","STARTED = '2026-10-26T08:00:00Z'"),
("OBS_AT = '2026-10-26T07:10:00Z'","OBS_AT = '2026-10-26T08:01:00Z'"),
("READS_BEFORE = 861","READS_BEFORE = 842"),
("datetime(2026,10,26,7,10,tzinfo=timezone.utc).timestamp()  # 0709Z (","datetime(2026,10,26,8,1,tzinfo=timezone.utc).timestamp()  # 0800Z (0709Z used 07:10, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_jalen': 'trend_jalen.txt', 'trend_komanche': 'trend_komanche.txt',","'trend_bauza': 'trend_bauza.txt', 'trend_chiefs': 'trend_chiefs.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_jalen','trend.Jalen Williams'),('trend_komanche','trend.Komanche'),","('trend_bauza','trend.Eric Bauza'),('trend_chiefs','trend.Chiefs'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0709Z.json') and '/26/' in _c: continue","if _c.endswith('0800Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T0602Z'","_last = '2026-10-26T0709Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
 'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)'),
("one hundred and forty-fifth run","one hundred and forty-sixth run"),
("one hundred and forty-third run","one hundred and forty-fourth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0709Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0800Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0709Z: none read)","# 5) request picks (0800Z: none read)"),
("(this 07Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 569 long, so the 400 cap left out the 48 last six-hour posts and the 121 slowest-growing still-gaining posts, and no cited post)",
 "(this 08Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 627 long, so the 400 cap left out the 61 last six-hour posts, the 121 slowest-growing still-gaining posts and the 45 slowest rest-of-24-hour posts, and no cited post)"),
("quote/repost words my/it + that (quoted)","quote/repost words just/what + the (quoted)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Eric Bauza\" and \"Chiefs\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words just/what + the (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Overnight run (3:09 AM ET":"            f'Overnight run (4:00 AM ET Oct 26 / 08:00 UTC Oct 26, the 08Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0709Z ended at 842, so no read went elsewhere in between), parallel batches of up to 8, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 627 ids, so the 400 cap left out the 61 last six-hour posts, the 121 slowest-growing still-gaining posts and the 45 slowest rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Eric Bauza\"":"            f'trend names \"Eric Bauza\" and \"Chiefs\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words my/it":"            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0709Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 0709Z, and 2114036672669348026 came back Not Found; story clusters (search_news) not read for the budget. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
