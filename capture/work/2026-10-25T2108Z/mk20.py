s=open('build_capture.py').read()
OLDTN=open('../2026-10-25T1904Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Panthers", "Ravens" and "Zac Taylor"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Falcons", "Daniel Jones" and "Jets"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1904Z.json","Build capture/2026/10/25/2003Z.json"),
("work/2026-10-25T1904Z'","work/2026-10-25T2003Z'"),
("RUN_ID = '2026-10-25T1904Z'","RUN_ID = '2026-10-25T2003Z'"),
("STARTED = '2026-10-25T19:04:00Z'","STARTED = '2026-10-25T20:03:00Z'"),
("OBS_AT = '2026-10-25T19:05:00Z'","OBS_AT = '2026-10-25T20:04:00Z'"),
("READS_BEFORE = 617","READS_BEFORE = 597"),
("datetime(2026,10,25,19,5,tzinfo=timezone.utc).timestamp()  # 1904Z (","datetime(2026,10,25,20,4,tzinfo=timezone.utc).timestamp()  # 2003Z (1904Z used 19:05, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_panthers': 'trend_panthers.txt', 'trend_ravens': 'trend_ravens.txt', 'trend_zactaylor': 'trend_zactaylor.txt',","'trend_falcons': 'trend_falcons.txt', 'trend_danieljones': 'trend_danieljones.txt', 'trend_jets': 'trend_jets.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_panthers','trend.Panthers'),('trend_ravens','trend.Ravens'),('trend_zactaylor','trend.Zac Taylor'),","('trend_falcons','trend.Falcons'),('trend_danieljones','trend.Daniel Jones'),('trend_jets','trend.Jets'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1904Z.json') and '/25/' in _c: continue","if _c.endswith('2003Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T1804Z'","_last = '2026-10-25T1904Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
 'common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)'),
("one hundred and thirty-third run","one hundred and thirty-fourth run"),
("one hundred and thirty-first run","one hundred and thirty-second run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1904Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2003Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1904Z: none read)","# 5) request picks (2003Z: none read)"),
("(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 580 long, so the 400 cap left out the 41 last six-hour posts and the 139 slowest-growing still-gaining posts, and no cited post)",
 "(this 20Z run is a fourth hour, so the rest of the last 24 hours was added last, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 589 long, so the 400 cap left out the 35 last six-hour posts, the 125 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post)"),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + and (quoted)"),
("        if str(_x) in ('trend.Panthers','trend.Ravens','trend.Zac Taylor'): return 'sports'  # 1904Z: Panthers at Bucs; Bengals at Ravens\n","        if str(_x) in ('trend.Falcons','trend.Daniel Jones','trend.Jets'): return 'sports'  # 2003Z: 49ers at Falcons; Colts at Vikings; Dolphins at Jets\n        if str(_x) in ('trend.Panthers','trend.Ravens','trend.Zac Taylor'): return 'sports'  # 1904Z: Panthers at Bucs; Bengals at Ravens\n"),
("then 27 in the second read: the 4 remaining plus 23 second-hop posts; 11 third-hop posts left unread for the budget)","then 24 second-hop posts in the second read; 11 third-hop posts left unread for the budget)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Afternoon run (3:04 PM ET":"            f'Afternoon run (4:03 PM ET Oct 25 / 20:03 UTC Oct 25, the 20Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1904Z ended at 597, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 589 ids, so the 400 cap left out the 35 last six-hour posts, the 125 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words what/the":"            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1904Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 97 unread referenced, reply-parent and media-source posts, most pointed-at first, then 24 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 11 third-hop posts left unread for the budget); 119 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 1904Z, and 1965290794203689251 came back Authorization Error; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 1904Z (watch.json dropped 2113882115104296989 and 2113881313489080523, added 2114303439819747717 and 2114004969435136445 and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
