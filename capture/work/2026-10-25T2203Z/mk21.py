s=open('build_capture.py').read()
OLDTN=open('../2026-10-25T2003Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Falcons", "Daniel Jones" and "Jets"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Giants", "Texans" and "49ers"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/2003Z.json","Build capture/2026/10/25/2108Z.json"),
("work/2026-10-25T2003Z'","work/2026-10-25T2108Z'"),
("RUN_ID = '2026-10-25T2003Z'","RUN_ID = '2026-10-25T2108Z'"),
("STARTED = '2026-10-25T20:03:00Z'","STARTED = '2026-10-25T21:08:00Z'"),
("OBS_AT = '2026-10-25T20:04:00Z'","OBS_AT = '2026-10-25T21:09:00Z'"),
("READS_BEFORE = 597","READS_BEFORE = 577"),
("datetime(2026,10,25,20,4,tzinfo=timezone.utc).timestamp()  # 2003Z (","datetime(2026,10,25,21,9,tzinfo=timezone.utc).timestamp()  # 2108Z (2003Z used 20:04, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_falcons': 'trend_falcons.txt', 'trend_danieljones': 'trend_danieljones.txt', 'trend_jets': 'trend_jets.txt',","'trend_giants': 'trend_giants.txt', 'trend_texans': 'trend_texans.txt', 'trend_49ers': 'trend_49ers.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_falcons','trend.Falcons'),('trend_danieljones','trend.Daniel Jones'),('trend_jets','trend.Jets'),","('trend_giants','trend.Giants'),('trend_texans','trend.Texans'),('trend_49ers','trend.49ers'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2003Z.json') and '/25/' in _c: continue","if _c.endswith('2108Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T1904Z'","_last = '2026-10-25T2003Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)',
 'common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)'),
("one hundred and thirty-fourth run","one hundred and thirty-fifth run"),
("one hundred and thirty-second run","one hundred and thirty-third run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2003Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2108Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (2003Z: none read)","# 5) request picks (2108Z: none read)"),
("(this 20Z run is a fourth hour, so the rest of the last 24 hours was added last, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 589 long, so the 400 cap left out the 35 last six-hour posts, the 125 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post)",
 "(this 21Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 566 long, so the 400 cap left out the 35 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words is/you + and (quoted)","quote/repost words my/it + that (quoted)"),
("        if str(_x) in ('trend.Falcons','trend.Daniel Jones','trend.Jets'): return 'sports'  # 2003Z","        if str(_x) in ('trend.Giants','trend.Texans','trend.49ers'): return 'sports'  # 2108Z: Giants at Texans; 49ers at Falcons\n        if str(_x) in ('trend.Falcons','trend.Daniel Jones','trend.Jets'): return 'sports'  # 2003Z"),
("then 24 second-hop posts in the second read; 11 third-hop posts left unread for the budget)","then 26 second-hop posts in the second read; 9 third-hop posts left unread for the budget)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Afternoon run (4:03 PM ET":"            f'Afternoon run (5:08 PM ET Oct 25 / 21:08 UTC Oct 25, the 21Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2003Z ended at 577, so no read went elsewhere in between), parallel batches of up to 9, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 566 ids, so the 400 cap left out the 35 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words is/you":"            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2003Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 97":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 26 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 9 third-hop posts left unread for the budget); 125 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 2003Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 2003Z (watch.json added 2114211348384997862 and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
