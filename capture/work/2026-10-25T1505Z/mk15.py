s=open('build_capture.py').read()
import re
OLDTN=re.findall(r'three of the top-ten US names with no posts attached in 1301Z.*?had posts attached in 1207Z',s)[0]
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "#PITvsNO", "Jaylen Warren" and "#TTPatEFW26ICONSIAM"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Steelers", "Darnell Washington" and "Tyler Warren"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1404Z.json","Build capture/2026/10/25/1505Z.json"),
("work/2026-10-25T1404Z'","work/2026-10-25T1505Z'"),
("RUN_ID = '2026-10-25T1404Z'","RUN_ID = '2026-10-25T1505Z'"),
("STARTED = '2026-10-25T14:04:00Z'","STARTED = '2026-10-25T15:05:00Z'"),
("OBS_AT = '2026-10-25T14:05:00Z'","OBS_AT = '2026-10-25T15:06:00Z'"),
("READS_BEFORE = 717","READS_BEFORE = 697"),
("datetime(2026,10,25,14,5,tzinfo=timezone.utc).timestamp()  # 1404Z (","datetime(2026,10,25,15,6,tzinfo=timezone.utc).timestamp()  # 1505Z (1404Z used 14:05, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_pitvsno': 'trend_pitvsno.txt', 'trend_jaylenwarren': 'trend_jaylenwarren.txt', 'trend_ttpat': 'trend_ttpat.txt',","'trend_steelers': 'trend_steelers.txt', 'trend_darnellwashington': 'trend_darnellwashington.txt', 'trend_tylerwarren': 'trend_tylerwarren.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_pitvsno','trend.#PITvsNO'),('trend_jaylenwarren','trend.Jaylen Warren'),('trend_ttpat','trend.#TTPatEFW26ICONSIAM'),","('trend_steelers','trend.Steelers'),('trend_darnellwashington','trend.Darnell Washington'),('trend_tylerwarren','trend.Tyler Warren'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1404Z.json') and '/25/' in _c: continue","if _c.endswith('1505Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T1301Z'","_last = '2026-10-25T1404Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("one hundred and twenty-eighth run","one hundred and twenty-ninth run"),
("one hundred and twenty-sixth run","one hundred and twenty-seventh run"),
("one hundred and twenty-fourth run","one hundred and twenty-fifth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1404Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1505Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1404Z: none read)","# 5) request picks (1505Z: none read)"),
("        if str(_x)=='trend.#PITvsNO': return 'sports'  # 1404Z: Steelers v Saints, NFL Paris game\n","        if str(_x)=='trend.Steelers': return 'sports'  # 1505Z: Steelers v Saints, NFL Paris game\n        if str(_x)=='trend.Darnell Washington': return 'sports'  # 1505Z: same game\n        if str(_x)=='trend.Tyler Warren': return 'sports'  # 1505Z: same broadcast\n        if str(_x)=='trend.#PITvsNO': return 'sports'  # 1404Z: Steelers v Saints, NFL Paris game\n"),
("for a,b in [('#PITvsNO','Jaylen Warren'),","for a,b in [('Steelers','#HereWeGo'),('Steelers','Shough'),('Steelers','TJ Watt'),('Steelers','Ramsey'),('Steelers','Darnell Washington'),('Steelers','Tyler Warren'),('Tyler Warren','Jaylen Warren'),('#PITvsNO','Jaylen Warren'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Morning run (10:04 AM ET":"            f'Morning run (11:05 AM ET Oct 25 / 15:05 UTC Oct 25, the 15Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1404Z ended at 697, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 573 ids, so the 400 cap left out the 29 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words and/my":"            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1404Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 43 (the 20 remaining plus 23 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 15 third-hop posts left unread for the budget); 143 returned; 2108062331095908717 came back Not Found again in the second read, as in 1105Z through 1404Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 1404Z (watch.json added 2114130963085000934); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
