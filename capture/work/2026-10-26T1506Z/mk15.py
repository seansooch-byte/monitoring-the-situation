s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T1406Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "#IDontWantToOverreactBUT", "Anthropic S-1" and "$ANT"'
NEWN='trend names "Brazil", "Anthropic" and "iPad mini"'
print('tn names count',s.count(a0))
s=s.replace(a0,NEWN).replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/1406Z.json","Build capture/2026/10/26/1506Z.json"),
("work/2026-10-26T1406Z'","work/2026-10-26T1506Z'"),
("RUN_ID = '2026-10-26T1406Z'","RUN_ID = '2026-10-26T1506Z'"),
("STARTED = '2026-10-26T14:06:00Z'","STARTED = '2026-10-26T15:06:00Z'"),
("OBS_AT = '2026-10-26T14:07:00Z'","OBS_AT = '2026-10-26T15:07:00Z'"),
("READS_BEFORE = 720","READS_BEFORE = 699"),
("datetime(2026,10,26,14,7,tzinfo=timezone.utc).timestamp()  # 1406Z (","datetime(2026,10,26,15,7,tzinfo=timezone.utc).timestamp()  # 1506Z (1406Z used 14:07, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_overreact': 'trend_overreact.txt', 'trend_anthropics1': 'trend_anthropics1.txt', 'trend_ant': 'trend_ant.txt',","'trend_brazil': 'trend_brazil.txt', 'trend_anthropic': 'trend_anthropic.txt', 'trend_ipadmini': 'trend_ipadmini.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_overreact','trend.#IDontWantToOverreactBUT'),('trend_anthropics1','trend.Anthropic S-1'),('trend_ant','trend.$ANT'),","('trend_brazil','trend.Brazil'),('trend_anthropic','trend.Anthropic'),('trend_ipadmini','trend.iPad mini'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1406Z.json') and '/26/' in _c: continue","if _c.endswith('1506Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-26T1313Z'","_last = '2026-10-26T1406Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("one hundred and fifty-second run","one hundred and fifty-third run"),
("one hundred and forty-ninth run","one hundred and fiftieth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1406Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1506Z.json'"),
("# 5) request picks (1406Z: none read)","# 5) request picks (1506Z: none read)"),
("(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 619 long, so the 400 cap left out the 65 last six-hour posts and the 154 slowest-growing still-gaining posts, and no cited post)",
 "(this 15Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 621 long, so the 400 cap left out the 74 last six-hour posts and the 147 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.La Granja VIP': return 'entertainment'","        if str(_x)=='trend.Anthropic': return 'ai'  # 1506Z: Anthropic IPO filing, as $ANT and Anthropic S-1 in 1406Z\n        if str(_x)=='trend.iPad mini': return 'tech'  # 1506Z\n        if str(_x)=='trend.Brazil': return 'world'  # 1506Z: Brazilian election result (Lula)\n        if str(_x)=='trend.La Granja VIP': return 'entertainment'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "+NEWN.replace("'","\\'")+" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words what/the + this (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Morning run (10:06 AM ET":"            f'Morning run (11:06 AM ET Oct 26 / 15:06 UTC Oct 26, the 15Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1406Z ended at 699, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 621 ids, so the 400 cap left out the 74 last six-hour posts and the 147 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"#IDontWant":"            f'"+NEWN.replace("'","\\'")+" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words it/that":"            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1406Z, so culture/sports/online were next in rotation); '",
"f'three screening reads by id:":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 1406Z; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 1204Z through 1406Z; story clusters (search_news) not read for the budget. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
