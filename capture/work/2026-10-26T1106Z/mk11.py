s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T1007Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Eric Bauza", "Chiefs" and "Nicki Minaj"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "#JAMESxPrada", "Victory Monday" and "Komanche"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/1007Z.json","Build capture/2026/10/26/1106Z.json"),
("work/2026-10-26T1007Z'","work/2026-10-26T1106Z'"),
("RUN_ID = '2026-10-26T1007Z'","RUN_ID = '2026-10-26T1106Z'"),
("STARTED = '2026-10-26T10:07:00Z'","STARTED = '2026-10-26T11:06:00Z'"),
("OBS_AT = '2026-10-26T10:08:00Z'","OBS_AT = '2026-10-26T11:07:00Z'"),
("READS_BEFORE = 804","READS_BEFORE = 784"),
("datetime(2026,10,26,10,8,tzinfo=timezone.utc).timestamp()  # 1007Z (","datetime(2026,10,26,11,7,tzinfo=timezone.utc).timestamp()  # 1106Z (1007Z used 10:08, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_bauza': 'trend_bauza.txt', 'trend_chiefs': 'trend_chiefs.txt', 'trend_minaj': 'trend_minaj.txt',","'trend_jamesprada': 'trend_jamesprada.txt', 'trend_victorymonday': 'trend_victorymonday.txt', 'trend_komanche': 'trend_komanche.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_bauza','trend.Eric Bauza'),('trend_chiefs','trend.Chiefs'),('trend_minaj','trend.Nicki Minaj'),","('trend_jamesprada','trend.#JAMESxPrada'),('trend_victorymonday','trend.Victory Monday'),('trend_komanche','trend.Komanche'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1007Z.json') and '/26/' in _c: continue","if _c.endswith('1106Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-26T0906Z'","_last = '2026-10-26T1007Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("one hundred and forty-eighth run","one hundred and forty-ninth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1007Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1106Z.json'"),
("# 5) request picks (1007Z: none read)","# 5) request picks (1106Z: none read)"),
("(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 35 last six-hour posts and the 143 slowest-growing still-gaining posts, and no cited post)",
 "(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 589 long, so the 400 cap left out the 48 last six-hour posts and the 141 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.Nicki Minaj': return 'music'  # 1007Z\n","        if str(_x)=='trend.Nicki Minaj': return 'music'  # 1007Z\n        if str(_x)=='trend.#JAMESxPrada': return 'music'  # 1106Z: CORTIS member James and Prada\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR=open('scr.txt').read().strip()
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"#JAMESxPrada\", \"Victory Monday\" and \"Komanche\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Overnight run (6:07 AM ET":"            f'Morning run (7:06 AM ET Oct 26 / 11:06 UTC Oct 26, the 11Z slot, last of the 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1007Z ended at 784, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 589 ids, so the 400 cap left out the 48 last six-hour posts and the 141 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"#JAMESxPrada\"":"            f'trend names \"#JAMESxPrada\", \"Victory Monday\" and \"Komanche\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words and/my":"            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1007Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id:":"            f'"+SCR.replace("'","\\'")+" (ids left out earlier as likely paid or sexual were not read again); 2108062331095908717 came back Not Found again, as in 1105Z through 1007Z; in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error; story clusters (search_news) not read for the budget. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
