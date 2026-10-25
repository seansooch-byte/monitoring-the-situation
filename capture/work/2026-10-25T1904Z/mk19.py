s=open('build_capture.py').read()
OLDTN=open('../2026-10-25T1804Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Bengals", "Dolphins" and "Zay Flowers"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Panthers", "Ravens" and "Zac Taylor"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1804Z.json","Build capture/2026/10/25/1904Z.json"),
("work/2026-10-25T1804Z'","work/2026-10-25T1904Z'"),
("RUN_ID = '2026-10-25T1804Z'","RUN_ID = '2026-10-25T1904Z'"),
("STARTED = '2026-10-25T18:04:00Z'","STARTED = '2026-10-25T19:04:00Z'"),
("OBS_AT = '2026-10-25T18:06:00Z'","OBS_AT = '2026-10-25T19:05:00Z'"),
("READS_BEFORE = 637","READS_BEFORE = 617"),
("datetime(2026,10,25,18,6,tzinfo=timezone.utc).timestamp()  # 1804Z (","datetime(2026,10,25,19,5,tzinfo=timezone.utc).timestamp()  # 1904Z (1804Z used 18:06, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_bengals': 'trend_bengals.txt', 'trend_dolphins': 'trend_dolphins.txt', 'trend_zayflowers': 'trend_zayflowers.txt',","'trend_panthers': 'trend_panthers.txt', 'trend_ravens': 'trend_ravens.txt', 'trend_zactaylor': 'trend_zactaylor.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_bengals','trend.Bengals'),('trend_dolphins','trend.Dolphins'),('trend_zayflowers','trend.Zay Flowers'),","('trend_panthers','trend.Panthers'),('trend_ravens','trend.Ravens'),('trend_zactaylor','trend.Zac Taylor'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1804Z.json') and '/25/' in _c: continue","if _c.endswith('1904Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T1702Z'","_last = '2026-10-25T1804Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("one hundred and thirty-second run","one hundred and thirty-third run"),
("one hundred and thirtieth run","one hundred and thirty-first run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1804Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1904Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1804Z: none read)","# 5) request picks (1904Z: none read)"),
("(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 580 long, so the 400 cap left out the 44 last six-hour posts and the 136 slowest-growing still-gaining posts, and no cited post)",
 "(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 580 long, so the 400 cap left out the 41 last six-hour posts and the 139 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words it/that + just (quoted)","quote/repost words what/the + this (quoted)"),
("        if str(_x) in ('trend.Bengals','trend.Dolphins','trend.Zay Flowers'): return 'sports'  # 1804Z: Bengals at Ravens; Dolphins at Jets\n","        if str(_x) in ('trend.Panthers','trend.Ravens','trend.Zac Taylor'): return 'sports'  # 1904Z: Panthers at Bucs; Bengals at Ravens\n        if str(_x) in ('trend.Bengals','trend.Dolphins','trend.Zay Flowers'): return 'sports'  # 1804Z: Bengals at Ravens; Dolphins at Jets\n"),
("for a,b in [('Bengals','Zay Flowers'),","for a,b in [('Ravens','Zac Taylor'),('Ravens','Bengals'),('Zac Taylor','Bengals'),('Bengals','Zay Flowers'),"),
("then 21 second-hop posts in the second read; 9 third-hop posts left unread for the budget)","then 27 in the second read: the 4 remaining plus 23 second-hop posts; 11 third-hop posts left unread for the budget)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Afternoon run (2:04 PM ET":"            f'Afternoon run (3:04 PM ET Oct 25 / 19:04 UTC Oct 25, the 19Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1804Z ended at 617, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 580 ids, so the 400 cap left out the 41 last six-hour posts and the 139 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words it/that":"            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1804Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 27 (the 4 remaining plus 23 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 11 third-hop posts left unread for the budget); 125 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 1804Z, and 2114036672669348026 came back Not Found; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 1804Z (watch.json dropped 2113861020590710934, added 2114338298818908594 and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
