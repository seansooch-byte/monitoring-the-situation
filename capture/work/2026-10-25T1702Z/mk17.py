s=open('build_capture.py').read()
import re
OLDTN=re.findall(r'three of the top-ten US names with no posts attached in 1505Z.*?"Jaylen Warren" \(seventh\) in 1404Z and "Cheesecake Factory" \(tenth\) in 1207Z',s)[0]
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Carrick", "Saints" and "Chase Young"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Aaron Rodgers", "Kellen Moore" and "Shough"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1606Z.json","Build capture/2026/10/25/1702Z.json"),
("work/2026-10-25T1606Z'","work/2026-10-25T1702Z'"),
("RUN_ID = '2026-10-25T1606Z'","RUN_ID = '2026-10-25T1702Z'"),
("STARTED = '2026-10-25T16:06:00Z'","STARTED = '2026-10-25T17:02:00Z'"),
("OBS_AT = '2026-10-25T16:08:00Z'","OBS_AT = '2026-10-25T17:03:00Z'"),
("READS_BEFORE = 677","READS_BEFORE = 657"),
("datetime(2026,10,25,16,8,tzinfo=timezone.utc).timestamp()  # 1606Z (","datetime(2026,10,25,17,3,tzinfo=timezone.utc).timestamp()  # 1702Z (1606Z used 16:08, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_carrick': 'trend_carrick.txt', 'trend_saints': 'trend_saints.txt', 'trend_chaseyoung': 'trend_chaseyoung.txt',","'trend_aaronrodgers': 'trend_aaronrodgers.txt', 'trend_kellenmoore': 'trend_kellenmoore.txt', 'trend_shough': 'trend_shough.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_carrick','trend.Carrick'),('trend_saints','trend.Saints'),('trend_chaseyoung','trend.Chase Young'),","('trend_aaronrodgers','trend.Aaron Rodgers'),('trend_kellenmoore','trend.Kellen Moore'),('trend_shough','trend.Shough'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1606Z.json') and '/25/' in _c: continue","if _c.endswith('1702Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T1505Z'","_last = '2026-10-25T1606Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("one hundred and thirtieth run","one hundred and thirty-first run"),
("one hundred and twenty-eighth run","one hundred and twenty-ninth run"),
("one hundred and twenty-sixth run","one hundred and twenty-seventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1606Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1702Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1606Z: none read)","# 5) request picks (1702Z: none read)"),
("(this 16Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the 24 hours, the list was 619 long, so the 400 cap left out the 35 last six-hour posts, the 149 slowest-growing still-gaining posts and 35 of the 39 rest-of-24-hour posts, and no cited post)",
 "(this 17Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 584 long, so the 400 cap left out the 46 last six-hour posts and the 138 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)"),
("        if str(_x)=='trend.Carrick': return 'sports'  # 1606Z: Manchester United v Bournemouth, Carrick job\n","        if str(_x) in ('trend.Aaron Rodgers','trend.Kellen Moore','trend.Shough'): return 'sports'  # 1702Z: Steelers v Saints, NFL Paris game\n        if str(_x)=='trend.Carrick': return 'sports'  # 1606Z: Manchester United v Bournemouth, Carrick job\n"),
("for a,b in [('Saints','Chase Young'),","for a,b in [('Aaron Rodgers','Shough'),('Kellen Moore','Shough'),('Aaron Rodgers','Steelers'),('Kellen Moore','Saints'),('Shough','Saints'),('Saints','Chase Young'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Midday run (12:06 PM ET":"            f'Afternoon run (1:02 PM ET Oct 25 / 17:02 UTC Oct 25, the 17Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1606Z ended at 657, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 584 ids, so the 400 cap left out the 46 last six-hour posts and the 138 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words the/this":"            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1606Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 29 (the 8 remaining plus 21 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 10 third-hop posts left unread for the budget); 128 returned; 2108062331095908717 came back Not Found again in the second read, as in 1105Z through 1606Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 1606Z (watch.json likewise only its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
