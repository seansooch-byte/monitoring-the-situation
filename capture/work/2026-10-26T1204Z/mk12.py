s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T1106Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "#JAMESxPrada", "Victory Monday" and "Komanche"'
NEWN='trend names "KEONHO CHANEL BOY REDEFINED", "#BladeRunnerYieldToRacist", "Eric Bauza" and "IKEONIC"'
print('tn names count',s.count(a0))
s=s.replace(a0,NEWN).replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/1106Z.json","Build capture/2026/10/26/1204Z.json"),
("work/2026-10-26T1106Z'","work/2026-10-26T1204Z'"),
("RUN_ID = '2026-10-26T1106Z'","RUN_ID = '2026-10-26T1204Z'"),
("STARTED = '2026-10-26T11:06:00Z'","STARTED = '2026-10-26T12:04:00Z'"),
("OBS_AT = '2026-10-26T11:07:00Z'","OBS_AT = '2026-10-26T12:06:00Z'"),
("READS_BEFORE = 784","READS_BEFORE = 762"),
("datetime(2026,10,26,11,7,tzinfo=timezone.utc).timestamp()  # 1106Z (","datetime(2026,10,26,12,6,tzinfo=timezone.utc).timestamp()  # 1204Z (1106Z used 11:07, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_jamesprada': 'trend_jamesprada.txt', 'trend_victorymonday': 'trend_victorymonday.txt', 'trend_komanche': 'trend_komanche.txt',","'trend_keonho': 'trend_keonho.txt', 'trend_bladerunner': 'trend_bladerunner.txt', 'trend_bauza': 'trend_bauza.txt', 'trend_ikeonic': 'trend_ikeonic.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_jamesprada','trend.#JAMESxPrada'),('trend_victorymonday','trend.Victory Monday'),('trend_komanche','trend.Komanche'),","('trend_keonho','trend.KEONHO CHANEL BOY REDEFINED'),('trend_bladerunner','trend.#BladeRunnerYieldToRacist'),('trend_bauza','trend.Eric Bauza'),('trend_ikeonic','trend.IKEONIC'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1106Z.json') and '/26/' in _c: continue","if _c.endswith('1204Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T1007Z'","_last = '2026-10-26T1106Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("one hundred and forty-ninth run","one hundred and fiftieth run"),
("one hundred and forty-sixth run","one hundred and forty-seventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1106Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1204Z.json'"),
("# 5) request picks (1106Z: none read)","# 5) request picks (1204Z: none read)"),
("(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 589 long, so the 400 cap left out the 48 last six-hour posts and the 141 slowest-growing still-gaining posts, and no cited post)",
 "(this 12Z run is not a fourth hour, as in 2026-10-25T1207Z; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 603 long, so the 400 cap left out the 59 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.#JAMESxPrada': return 'music'  # 1106Z: CORTIS member James and Prada\n","        if str(_x)=='trend.#JAMESxPrada': return 'music'  # 1106Z: CORTIS member James and Prada\n        if str(_x) in ('trend.KEONHO CHANEL BOY REDEFINED','trend.IKEONIC'): return 'music'  # 1204Z: AHOF member Keonho fan campaign (Chanel, Vogue)\n        if str(_x)=='trend.#BladeRunnerYieldToRacist': return 'gaming'  # 1204Z: Love and Deepspace (Papergames) fan campaign, as #BladeRunnerCollabswithRacist in 1200Z\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "+NEWN.replace("'","\\'")+" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Morning run (7:06 AM ET":"            f'Morning run (8:04 AM ET Oct 26 / 12:04 UTC Oct 26, the 12Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1106Z ended at 764, so 2 reads went elsewhere in between, most likely the 7:03 AM Eastern daily briefing), parallel batches of up to 14, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is not a fourth hour, as in 2026-10-25T1207Z: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 603 ids, so the 400 cap left out the 59 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"#JAMESxPrada\"":"            f'"+NEWN.replace("'","\\'")+" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words that/just":"            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1106Z, so news/money/science were next in rotation); '",
"f'two screening reads by id:":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 1106Z; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 1106Z; story clusters (search_news) not read for the budget. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
