s=open('build_capture.py').read()
import re
OLDTN=re.findall(r'three of the top-ten US names with no posts attached in 1404Z.*?had posts attached in 1404Z and "Good Sunday" \(seventh\) and "Cheesecake Factory" \(tenth\) in 1207Z',s)[0]
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Steelers", "Darnell Washington" and "Tyler Warren"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Carrick", "Saints" and "Chase Young"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1505Z.json","Build capture/2026/10/25/1606Z.json"),
("work/2026-10-25T1505Z'","work/2026-10-25T1606Z'"),
("RUN_ID = '2026-10-25T1505Z'","RUN_ID = '2026-10-25T1606Z'"),
("STARTED = '2026-10-25T15:05:00Z'","STARTED = '2026-10-25T16:06:00Z'"),
("OBS_AT = '2026-10-25T15:06:00Z'","OBS_AT = '2026-10-25T16:08:00Z'"),
("READS_BEFORE = 697","READS_BEFORE = 677"),
("datetime(2026,10,25,15,6,tzinfo=timezone.utc).timestamp()  # 1505Z (","datetime(2026,10,25,16,8,tzinfo=timezone.utc).timestamp()  # 1606Z (1505Z used 15:06, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_steelers': 'trend_steelers.txt', 'trend_darnellwashington': 'trend_darnellwashington.txt', 'trend_tylerwarren': 'trend_tylerwarren.txt',","'trend_carrick': 'trend_carrick.txt', 'trend_saints': 'trend_saints.txt', 'trend_chaseyoung': 'trend_chaseyoung.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_steelers','trend.Steelers'),('trend_darnellwashington','trend.Darnell Washington'),('trend_tylerwarren','trend.Tyler Warren'),","('trend_carrick','trend.Carrick'),('trend_saints','trend.Saints'),('trend_chaseyoung','trend.Chase Young'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1505Z.json') and '/25/' in _c: continue","if _c.endswith('1606Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T1404Z'","_last = '2026-10-25T1505Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("one hundred and twenty-ninth run","one hundred and thirtieth run"),
("one hundred and twenty-seventh run","one hundred and twenty-eighth run"),
("one hundred and twenty-fifth run","one hundred and twenty-sixth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1505Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1606Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1505Z: none read)","# 5) request picks (1606Z: none read)"),
("(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 567 long, so the 400 cap left out the 23 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post)",
 "(this 16Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the 24 hours, the list was 619 long, so the 400 cap left out the 35 last six-hour posts, the 149 slowest-growing still-gaining posts and 35 of the 39 rest-of-24-hour posts, and no cited post)"),
("quote/repost words and/my + it (quoted)","quote/repost words the/this + is (quoted)"),
("then 31 (the 2 remaining plus 29 second-hop posts) in the second read; 13 third-hop posts left unread for the budget)","then 34 (the 8 remaining plus 26 second-hop posts) in the second read; 17 third-hop posts left unread for the budget)"),
("        if str(_x)=='trend.Steelers': return 'sports'  # 1505Z: Steelers v Saints, NFL Paris game\n","        if str(_x)=='trend.Carrick': return 'sports'  # 1606Z: Manchester United v Bournemouth, Carrick's job\n        if str(_x)=='trend.Saints': return 'sports'  # 1606Z: Steelers v Saints, NFL Paris game\n        if str(_x)=='trend.Chase Young': return 'sports'  # 1606Z: same game\n        if str(_x)=='trend.Steelers': return 'sports'  # 1505Z: Steelers v Saints, NFL Paris game\n"),
("for a,b in [('Steelers','#HereWeGo'),","for a,b in [('Saints','Chase Young'),('Saints','Shough'),('Saints','#HereWeGo'),('Saints','Payton Wilson'),('Saints','Steelers'),('Carrick','#MUFC'),('Carrick','Bournemouth'),('Steelers','#HereWeGo'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Morning run (11:05 AM ET":"            f'Midday run (12:06 PM ET Oct 25 / 16:06 UTC Oct 25, the 16Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1505Z ended at 677, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the 24 hours; 619 ids, so the 400 cap left out the 35 last six-hour posts, the 149 slowest-growing still-gaining posts and 35 of the 39 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words that/just":"            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1505Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 34 (the 8 remaining plus 26 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 17 third-hop posts left unread for the budget); 133 returned; 2108062331095908717 came back Not Found again in the second read, as in 1105Z through 1505Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 1505Z (watch.json swapped 2113829143792189536 for 2114085789139140865); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
