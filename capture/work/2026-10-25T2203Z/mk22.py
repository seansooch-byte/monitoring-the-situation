s=open('build_capture.py').read()
OLDTN=open('../2026-10-25T2108Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Giants", "Texans" and "49ers"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Ravens", "Larson" and "Browns"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/2108Z.json","Build capture/2026/10/25/2203Z.json"),
("work/2026-10-25T2108Z'","work/2026-10-25T2203Z'"),
("RUN_ID = '2026-10-25T2108Z'","RUN_ID = '2026-10-25T2203Z'"),
("STARTED = '2026-10-25T21:08:00Z'","STARTED = '2026-10-25T22:03:00Z'"),
("OBS_AT = '2026-10-25T21:09:00Z'","OBS_AT = '2026-10-25T22:04:00Z'"),
("READS_BEFORE = 577","READS_BEFORE = 557"),
("datetime(2026,10,25,21,9,tzinfo=timezone.utc).timestamp()  # 2108Z (","datetime(2026,10,25,22,4,tzinfo=timezone.utc).timestamp()  # 2203Z (2108Z used 21:09, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_giants': 'trend_giants.txt', 'trend_texans': 'trend_texans.txt', 'trend_49ers': 'trend_49ers.txt',","'trend_ravens': 'trend_ravens.txt', 'trend_larson': 'trend_larson.txt', 'trend_browns': 'trend_browns.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_giants','trend.Giants'),('trend_texans','trend.Texans'),('trend_49ers','trend.49ers'),","('trend_ravens','trend.Ravens'),('trend_larson','trend.Larson'),('trend_browns','trend.Browns'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2108Z.json') and '/25/' in _c: continue","if _c.endswith('2203Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T2003Z'","_last = '2026-10-25T2108Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
 'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)'),
("one hundred and thirty-fifth run","one hundred and thirty-sixth run"),
("one hundred and thirty-third run","one hundred and thirty-fourth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2108Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2203Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (2108Z: none read)","# 5) request picks (2203Z: none read)"),
("(this 21Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 566 long, so the 400 cap left out the 35 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)",
 "(this 22Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 577 long, so the 400 cap left out the 52 last six-hour posts and the 125 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words my/it + that (quoted)","quote/repost words just/what + the (quoted)"),
("        if str(_x) in ('trend.Giants','trend.Texans','trend.49ers'): return 'sports'  # 2108Z","        if str(_x) in ('trend.Ravens','trend.Larson','trend.Browns'): return 'sports'  # 2203Z: Bengals at Ravens; NASCAR at Talladega; Titans at Browns\n        if str(_x) in ('trend.Giants','trend.Texans','trend.49ers'): return 'sports'  # 2108Z"),
("then 26 second-hop posts in the second read; 9 third-hop posts left unread for the budget)","then 31 in the second read: the 8 remaining plus 23 second-hop posts; 12 third-hop posts left unread for the budget)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Afternoon run (5:08 PM ET":"            f'Evening run (6:03 PM ET Oct 25 / 22:03 UTC Oct 25, the 22Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2108Z ended at 557, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 577 ids, so the 400 cap left out the 52 last six-hour posts and the 125 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words my/it":"            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2108Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 31 in the second read: the 8 remaining plus 23 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 12 third-hop posts left unread for the budget); 130 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 2108Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 2108Z (watch.json added 2114452368632803490, 2114452582722646279, 2114455735538987220 and 2114313023636856844 and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
