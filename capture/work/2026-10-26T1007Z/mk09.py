s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0800Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Eric Bauza" and "Chiefs"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Lula" and "Komanche"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0800Z.json","Build capture/2026/10/26/0906Z.json"),
("work/2026-10-26T0800Z'","work/2026-10-26T0906Z'"),
("RUN_ID = '2026-10-26T0800Z'","RUN_ID = '2026-10-26T0906Z'"),
("STARTED = '2026-10-26T08:00:00Z'","STARTED = '2026-10-26T09:06:00Z'"),
("OBS_AT = '2026-10-26T08:01:00Z'","OBS_AT = '2026-10-26T09:08:00Z'"),
("READS_BEFORE = 842","READS_BEFORE = 823"),
("datetime(2026,10,26,8,1,tzinfo=timezone.utc).timestamp()  # 0800Z (","datetime(2026,10,26,9,8,tzinfo=timezone.utc).timestamp()  # 0906Z (0800Z used 08:01, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_bauza': 'trend_bauza.txt', 'trend_chiefs': 'trend_chiefs.txt',","'trend_lula': 'trend_lula.txt', 'trend_komanche': 'trend_komanche.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_bauza','trend.Eric Bauza'),('trend_chiefs','trend.Chiefs'),","('trend_lula','trend.Lula'),('trend_komanche','trend.Komanche'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0800Z.json') and '/26/' in _c: continue","if _c.endswith('0906Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-26T0709Z'","_last = '2026-10-26T0800Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("one hundred and forty-sixth run","one hundred and forty-seventh run"),
("one hundred and forty-fourth run","one hundred and forty-fifth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0800Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0906Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0800Z: none read)","# 5) request picks (0906Z: none read)"),
("(this 08Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 627 long, so the 400 cap left out the 61 last six-hour posts, the 121 slowest-growing still-gaining posts and the 45 slowest rest-of-24-hour posts, and no cited post)",
 "(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 568 long, so the 400 cap left out the 37 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words just/what + the (quoted)","quote/repost words this/is + you (quoted)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Lula\" and \"Komanche\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words this/is + you (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Overnight run (4:00 AM ET":"            f'Overnight run (5:06 AM ET Oct 26 / 09:06 UTC Oct 26, the 09Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0800Z ended at 823, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 568 ids, so the 400 cap left out the 37 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Lula\"":"            f'trend names \"Lula\" and \"Komanche\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words just/what":"            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0800Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 0800Z; story clusters (search_news) not read for the budget. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
