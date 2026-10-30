s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T1204Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "KEONHO CHANEL BOY REDEFINED", "#BladeRunnerYieldToRacist", "Eric Bauza" and "IKEONIC"'
NEWN='trend names "Victory Monday" and "La Granja VIP"'
print('tn names count',s.count(a0))
s=s.replace(a0,NEWN).replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/1204Z.json","Build capture/2026/10/26/1313Z.json"),
("work/2026-10-26T1204Z'","work/2026-10-26T1313Z'"),
("RUN_ID = '2026-10-26T1204Z'","RUN_ID = '2026-10-26T1313Z'"),
("STARTED = '2026-10-26T12:04:00Z'","STARTED = '2026-10-26T13:13:00Z'"),
("OBS_AT = '2026-10-26T12:06:00Z'","OBS_AT = '2026-10-26T13:14:00Z'"),
("READS_BEFORE = 762","READS_BEFORE = 740"),
("datetime(2026,10,26,12,6,tzinfo=timezone.utc).timestamp()  # 1204Z (","datetime(2026,10,26,13,14,tzinfo=timezone.utc).timestamp()  # 1313Z (1204Z used 12:06, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_keonho': 'trend_keonho.txt', 'trend_bladerunner': 'trend_bladerunner.txt', 'trend_bauza': 'trend_bauza.txt', 'trend_ikeonic': 'trend_ikeonic.txt',","'trend_victorymonday': 'trend_victorymonday.txt', 'trend_lagranja': 'trend_lagranja.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_keonho','trend.KEONHO CHANEL BOY REDEFINED'),('trend_bladerunner','trend.#BladeRunnerYieldToRacist'),('trend_bauza','trend.Eric Bauza'),('trend_ikeonic','trend.IKEONIC'),","('trend_victorymonday','trend.Victory Monday'),('trend_lagranja','trend.La Granja VIP'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1204Z.json') and '/26/' in _c: continue","if _c.endswith('1313Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-26T1106Z'","_last = '2026-10-26T1204Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("one hundred and fiftieth run","one hundred and fifty-first run"),
("one hundred and forty-seventh run","one hundred and forty-eighth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1204Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1313Z.json'"),
("# 5) request picks (1204Z: none read)","# 5) request picks (1313Z: none read)"),
("(this 12Z run is not a fourth hour, as in 2026-10-25T1207Z; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 603 long, so the 400 cap left out the 59 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post)",
 "(this 13Z run is not a fourth hour, as in 2026-10-25T1301Z; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 615 long, so the 400 cap left out the 67 last six-hour posts and the 148 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.#BladeRunnerYieldToRacist': return 'gaming'","        if str(_x)=='trend.La Granja VIP': return 'entertainment'  # 1313Z: Spanish-language reality show (empty lang:en stream)\n        if str(_x)=='trend.#BladeRunnerYieldToRacist': return 'gaming'"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "+NEWN.replace("'","\\'")+" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Morning run (8:04 AM ET":"            f'Morning run (9:13 AM ET Oct 26 / 13:13 UTC Oct 26, the 13Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1204Z ended at 740, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour, as in 2026-10-25T1301Z: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 615 ids, so the 400 cap left out the 67 last six-hour posts and the 148 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Victory":"            f'"+NEWN.replace("'","\\'")+" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words the/this":"            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1204Z, so culture/sports/online were next in rotation); '",
"f'three screening reads by id:":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 1204Z; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 1204Z; story clusters (search_news) not read for the budget. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
