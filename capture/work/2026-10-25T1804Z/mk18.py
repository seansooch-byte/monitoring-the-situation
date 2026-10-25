s=open('build_capture.py').read()
import re
OLDTN=open('../2026-10-25T1702Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Aaron Rodgers", "Kellen Moore" and "Shough"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Bengals", "Dolphins" and "Zay Flowers"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1702Z.json","Build capture/2026/10/25/1804Z.json"),
("work/2026-10-25T1702Z'","work/2026-10-25T1804Z'"),
("RUN_ID = '2026-10-25T1702Z'","RUN_ID = '2026-10-25T1804Z'"),
("STARTED = '2026-10-25T17:02:00Z'","STARTED = '2026-10-25T18:04:00Z'"),
("OBS_AT = '2026-10-25T17:03:00Z'","OBS_AT = '2026-10-25T18:06:00Z'"),
("READS_BEFORE = 657","READS_BEFORE = 637"),
("datetime(2026,10,25,17,3,tzinfo=timezone.utc).timestamp()  # 1702Z (","datetime(2026,10,25,18,6,tzinfo=timezone.utc).timestamp()  # 1804Z (1702Z used 17:03, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_aaronrodgers': 'trend_aaronrodgers.txt', 'trend_kellenmoore': 'trend_kellenmoore.txt', 'trend_shough': 'trend_shough.txt',","'trend_bengals': 'trend_bengals.txt', 'trend_dolphins': 'trend_dolphins.txt', 'trend_zayflowers': 'trend_zayflowers.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_aaronrodgers','trend.Aaron Rodgers'),('trend_kellenmoore','trend.Kellen Moore'),('trend_shough','trend.Shough'),","('trend_bengals','trend.Bengals'),('trend_dolphins','trend.Dolphins'),('trend_zayflowers','trend.Zay Flowers'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1702Z.json') and '/25/' in _c: continue","if _c.endswith('1804Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T1606Z'","_last = '2026-10-25T1702Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)'),
("one hundred and thirty-first run","one hundred and thirty-second run"),
("one hundred and twenty-ninth run","one hundred and thirtieth run"),
("one hundred and twenty-seventh run","one hundred and twenty-eighth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1702Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1804Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1702Z: none read)","# 5) request picks (1804Z: none read)"),
("(this 17Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 584 long, so the 400 cap left out the 46 last six-hour posts and the 138 slowest-growing still-gaining posts, and no cited post)",
 "(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 580 long, so the 400 cap left out the 44 last six-hour posts and the 136 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words you/and + my (quoted)","quote/repost words it/that + just (quoted)"),
("        if str(_x) in ('trend.Aaron Rodgers','trend.Kellen Moore','trend.Shough'): return 'sports'  # 1702Z: Steelers v Saints, NFL Paris game\n","        if str(_x) in ('trend.Bengals','trend.Dolphins','trend.Zay Flowers'): return 'sports'  # 1804Z: Bengals at Ravens; Dolphins at Jets\n        if str(_x) in ('trend.Aaron Rodgers','trend.Kellen Moore','trend.Shough'): return 'sports'  # 1702Z: Steelers v Saints, NFL Paris game\n"),
("for a,b in [('Aaron Rodgers','Shough'),","for a,b in [('Bengals','Zay Flowers'),('Bengals','Zac Taylor'),('Zac Taylor','Zay Flowers'),('Aaron Rodgers','Shough'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
L={
"f'Afternoon run (1:02 PM ET":"            f'Afternoon run (2:04 PM ET Oct 25 / 18:04 UTC Oct 25, the 18Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1702Z ended at 637, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 580 ids, so the 400 cap left out the 44 last six-hour posts and the 136 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words you/and":"            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1702Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 21 (second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 9 third-hop posts left unread for the budget); 120 returned; 2108062331095908717 came back Not Found again in the second read, as in 1105Z through 1702Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 1702Z (watch.json dropped five ids and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
