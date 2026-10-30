s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0906Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Lula" and "Komanche"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Eric Bauza", "Chiefs" and "Nicki Minaj"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0906Z.json","Build capture/2026/10/26/1007Z.json"),
("work/2026-10-26T0906Z'","work/2026-10-26T1007Z'"),
("RUN_ID = '2026-10-26T0906Z'","RUN_ID = '2026-10-26T1007Z'"),
("STARTED = '2026-10-26T09:06:00Z'","STARTED = '2026-10-26T10:07:00Z'"),
("OBS_AT = '2026-10-26T09:08:00Z'","OBS_AT = '2026-10-26T10:08:00Z'"),
("READS_BEFORE = 823","READS_BEFORE = 804"),
("datetime(2026,10,26,9,8,tzinfo=timezone.utc).timestamp()  # 0906Z (","datetime(2026,10,26,10,8,tzinfo=timezone.utc).timestamp()  # 1007Z (0906Z used 09:08, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_lula': 'trend_lula.txt', 'trend_komanche': 'trend_komanche.txt',","'trend_bauza': 'trend_bauza.txt', 'trend_chiefs': 'trend_chiefs.txt', 'trend_minaj': 'trend_minaj.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_lula','trend.Lula'),('trend_komanche','trend.Komanche'),","('trend_bauza','trend.Eric Bauza'),('trend_chiefs','trend.Chiefs'),('trend_minaj','trend.Nicki Minaj'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0906Z.json') and '/26/' in _c: continue","if _c.endswith('1007Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T0800Z'","_last = '2026-10-26T0906Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("one hundred and forty-seventh run","one hundred and forty-eighth run"),
("one hundred and forty-fifth run","one hundred and forty-sixth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0906Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1007Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0906Z: none read)","# 5) request picks (1007Z: none read)"),
("(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 568 long, so the 400 cap left out the 37 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)",
 "(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 35 last six-hour posts and the 143 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words this/is + you (quoted)","quote/repost words and/my + it (quoted)"),
("        if str(_x)=='trend.Eric Bauza': return 'entertainment'  # 0408Z: voice actor\n","        if str(_x)=='trend.Eric Bauza': return 'entertainment'  # 0408Z: voice actor\n        if str(_x)=='trend.Nicki Minaj': return 'music'  # 1007Z\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Eric Bauza\", \"Chiefs\" and \"Nicki Minaj\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Overnight run (5:06 AM ET":"            f'Overnight run (6:07 AM ET Oct 26 / 10:07 UTC Oct 26, the 10Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0906Z ended at 804, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 578 ids, so the 400 cap left out the 35 last six-hour posts and the 143 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Eric Bauza\"":"            f'trend names \"Eric Bauza\", \"Chiefs\" and \"Nicki Minaj\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words this/is":"            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0906Z, so news/money/science were next in rotation); '",
"f'two screening reads by id:":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 0906Z, and so did 2114632745511182523 (a quoted post) and 2114600527891976370; story clusters (search_news) not read for the budget. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
