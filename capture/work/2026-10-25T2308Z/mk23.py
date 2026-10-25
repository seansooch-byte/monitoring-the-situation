s=open('build_capture.py').read()
OLDTN=open('../2026-10-25T2203Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Ravens", "Larson" and "Browns"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Packers", "Lions" and "Raiders"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/2203Z.json","Build capture/2026/10/25/2308Z.json"),
("work/2026-10-25T2203Z'","work/2026-10-25T2308Z'"),
("RUN_ID = '2026-10-25T2203Z'","RUN_ID = '2026-10-25T2308Z'"),
("STARTED = '2026-10-25T22:03:00Z'","STARTED = '2026-10-25T23:08:00Z'"),
("OBS_AT = '2026-10-25T22:04:00Z'","OBS_AT = '2026-10-25T23:09:00Z'"),
("READS_BEFORE = 557","READS_BEFORE = 537"),
("datetime(2026,10,25,22,4,tzinfo=timezone.utc).timestamp()  # 2203Z (","datetime(2026,10,25,23,9,tzinfo=timezone.utc).timestamp()  # 2308Z (2203Z used 22:04, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_ravens': 'trend_ravens.txt', 'trend_larson': 'trend_larson.txt', 'trend_browns': 'trend_browns.txt',","'trend_packers': 'trend_packers.txt', 'trend_lions': 'trend_lions.txt', 'trend_raiders': 'trend_raiders.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_ravens','trend.Ravens'),('trend_larson','trend.Larson'),('trend_browns','trend.Browns'),","('trend_packers','trend.Packers'),('trend_lions','trend.Lions'),('trend_raiders','trend.Raiders'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2203Z.json') and '/25/' in _c: continue","if _c.endswith('2308Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T2108Z'","_last = '2026-10-25T2203Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("one hundred and thirty-sixth run","one hundred and thirty-seventh run"),
("one hundred and thirty-fourth run","one hundred and thirty-fifth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2203Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2308Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (2203Z: none read)","# 5) request picks (2308Z: none read)"),
("(this 22Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 577 long, so the 400 cap left out the 52 last six-hour posts and the 125 slowest-growing still-gaining posts, and no cited post)",
 "(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 580 long, so the 400 cap left out the 47 last six-hour posts and the 133 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words just/what + the (quoted)","quote/repost words this/is + you (quoted)"),
("        if str(_x) in ('trend.Ravens','trend.Larson','trend.Browns'): return 'sports'  # 2203Z","        if str(_x) in ('trend.Packers','trend.Lions','trend.Raiders'): return 'sports'  # 2308Z: Packers at Lions; Rams at Raiders\n        if str(_x) in ('trend.Ravens','trend.Larson','trend.Browns'): return 'sports'  # 2203Z"),
("then 31 in the second read: the 8 remaining plus 23 second-hop posts; 12 third-hop posts left unread for the budget)","then 42 in the second read: the 17 remaining plus 25 second-hop posts; 15 third-hop posts left unread for the budget)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Evening run (6:03 PM ET":"            f'Evening run (7:08 PM ET Oct 25 / 23:08 UTC Oct 25, the 23Z slot and the last run of the UTC day; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2203Z ended at 537, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 580 ids, so the 400 cap left out the 47 last six-hour posts and the 133 slowest-growing still-gaining posts, and no cited post; 4 reads; 2114311015894843773, first captured in 1904Z and not cited on the pulse, in a story or in watch.json, came back Not Found); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words just/what":"            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2203Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 42 in the second read: the 17 remaining plus 25 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 15 third-hop posts left unread for the budget); 140 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 2203Z, and 1327343231353450496 (a 2020 post referenced by a post read this run) came back Not Found; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 2203Z (watch.json added 2114296536922529937 and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
