s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0408Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Eric Bauza" and "Jalen Williams"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Mahomes" and "Seahawks"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0408Z.json","Build capture/2026/10/26/0502Z.json"),
("work/2026-10-26T0408Z'","work/2026-10-26T0502Z'"),
("RUN_ID = '2026-10-26T0408Z'","RUN_ID = '2026-10-26T0502Z'"),
("STARTED = '2026-10-26T04:08:00Z'","STARTED = '2026-10-26T05:02:00Z'"),
("OBS_AT = '2026-10-26T04:08:00Z'","OBS_AT = '2026-10-26T05:03:00Z'"),
("READS_BEFORE = 918","READS_BEFORE = 899"),
("datetime(2026,10,26,4,8,tzinfo=timezone.utc).timestamp()  # 0408Z (","datetime(2026,10,26,5,3,tzinfo=timezone.utc).timestamp()  # 0502Z (0408Z used 04:08, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_bauza': 'trend_bauza.txt', 'trend_jwilliams': 'trend_jwilliams.txt',","'trend_mahomes': 'trend_mahomes.txt', 'trend_seahawks': 'trend_seahawks.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_bauza','trend.Eric Bauza'),('trend_jwilliams','trend.Jalen Williams'),","('trend_mahomes','trend.Mahomes'),('trend_seahawks','trend.Seahawks'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0408Z.json') and '/26/' in _c: continue","if _c.endswith('0502Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-26T0306Z'","_last = '2026-10-26T0408Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("one hundred and forty-second run","one hundred and forty-third run"),
("one hundred and fortieth run","one hundred and forty-first run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0408Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0502Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0408Z: none read)","# 5) request picks (0502Z: none read)"),
("(this 04Z run is a fourth hour, so the rest of the last 24 hours, slowest growing last, joined the list; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 597 long, so the 400 cap left out the 54 last six-hour posts, the 112 slowest-growing still-gaining posts and the 31 slowest rest-of-24-hour posts, and no cited post)",
 "(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 579 long, so the 400 cap left out the 72 last six-hour posts and the 107 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words it/that + just (quoted)","quote/repost words what/the + this (quoted)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR="two screening reads by id (100 unread referenced posts, most pointed-at first, then 37 in the second read: the 12 remaining plus 25 second-hop posts; 13 third-hop posts left unread for the budget)"
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Mahomes\" and \"Seahawks\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words what/the + this (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Night run (12:08 AM ET":"            f'Night run (1:02 AM ET Oct 26 / 05:02 UTC Oct 26, the 05Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0408Z ended at 899, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 579 ids, so the 400 cap left out the 72 last six-hour posts and the 107 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Eric Bauza\"":"            f'trend names \"Mahomes\" and \"Seahawks\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'trend names \"Mahomes\"":"            f'trend names \"Mahomes\" and \"Seahawks\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words it/that":"            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0408Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 37 in the second read: the 12 remaining plus 25 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 13 third-hop posts left unread for the budget); 2108062331095908717 came back Not Found again, as in 1105Z through 0408Z, and 2114400523386298570 came back with an Authorization Error; story clusters (search_news) not read for the budget. '",
"f'No new request: r-2026-10-26-01":"            f'No new request: r-2026-10-26-01 was answered in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
