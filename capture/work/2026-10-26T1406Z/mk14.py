s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T1313Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Victory Monday" and "La Granja VIP"'
NEWN='trend names "#IDontWantToOverreactBUT", "Anthropic S-1" and "$ANT"'
print('tn names count',s.count(a0))
s=s.replace(a0,NEWN).replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/1313Z.json","Build capture/2026/10/26/1406Z.json"),
("work/2026-10-26T1313Z'","work/2026-10-26T1406Z'"),
("RUN_ID = '2026-10-26T1313Z'","RUN_ID = '2026-10-26T1406Z'"),
("STARTED = '2026-10-26T13:13:00Z'","STARTED = '2026-10-26T14:06:00Z'"),
("OBS_AT = '2026-10-26T13:14:00Z'","OBS_AT = '2026-10-26T14:07:00Z'"),
("READS_BEFORE = 740","READS_BEFORE = 720"),
("datetime(2026,10,26,13,14,tzinfo=timezone.utc).timestamp()  # 1313Z (","datetime(2026,10,26,14,7,tzinfo=timezone.utc).timestamp()  # 1406Z (1313Z used 13:14, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_victorymonday': 'trend_victorymonday.txt', 'trend_lagranja': 'trend_lagranja.txt',","'trend_overreact': 'trend_overreact.txt', 'trend_anthropics1': 'trend_anthropics1.txt', 'trend_ant': 'trend_ant.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_victorymonday','trend.Victory Monday'),('trend_lagranja','trend.La Granja VIP'),","('trend_overreact','trend.#IDontWantToOverreactBUT'),('trend_anthropics1','trend.Anthropic S-1'),('trend_ant','trend.$ANT'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1313Z.json') and '/26/' in _c: continue","if _c.endswith('1406Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T1204Z'","_last = '2026-10-26T1313Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)'),
("one hundred and fifty-first run","one hundred and fifty-second run"),
("one hundred and forty-eighth run","one hundred and forty-ninth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1313Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1406Z.json'"),
("# 5) request picks (1313Z: none read)","# 5) request picks (1406Z: none read)"),
("(this 13Z run is not a fourth hour, as in 2026-10-25T1301Z; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 615 long, so the 400 cap left out the 67 last six-hour posts and the 148 slowest-growing still-gaining posts, and no cited post)",
 "(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 619 long, so the 400 cap left out the 65 last six-hour posts and the 154 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.La Granja VIP': return 'entertainment'","        if str(_x) in ('trend.Anthropic S-1','trend.$ANT'): return 'ai'  # 1406Z: Anthropic IPO filing (S-1), Nasdaq ticker ANT\n        if str(_x)=='trend.#IDontWantToOverreactBUT': return 'sports'  # 1406Z: Pat McAfee Show prompt, NFL fan posts\n        if str(_x)=='trend.La Granja VIP': return 'entertainment'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "+NEWN.replace("'","\\'")+" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Morning run (9:13 AM ET":"            f'Morning run (10:06 AM ET Oct 26 / 14:06 UTC Oct 26, the 14Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1313Z ended at 720, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 619 ids, so the 400 cap left out the 65 last six-hour posts and the 154 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Victory":"            f'"+NEWN.replace("'","\\'")+" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words you/and":"            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1313Z, so news/money/science were next in rotation); '",
"f'three screening reads by id:":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 1313Z; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 1204Z and 1313Z; story clusters (search_news) not read for the budget. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
