s=open('build_capture.py').read()
OLDTN=open('../2026-10-25T2308Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Packers", "Lions" and "Raiders"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Dan Campbell", "Trey Smack" and "Lula"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/2308Z.json","Build capture/2026/10/26/0004Z.json"),
("work/2026-10-25T2308Z'","work/2026-10-26T0004Z'"),
("RUN_ID = '2026-10-25T2308Z'","RUN_ID = '2026-10-26T0004Z'"),
("STARTED = '2026-10-25T23:08:00Z'","STARTED = '2026-10-26T00:04:00Z'"),
("OBS_AT = '2026-10-25T23:09:00Z'","OBS_AT = '2026-10-26T00:05:00Z'"),
("READS_BEFORE = 537","READS_BEFORE = 1000"),
("datetime(2026,10,25,23,9,tzinfo=timezone.utc).timestamp()  # 2308Z (","datetime(2026,10,26,0,5,tzinfo=timezone.utc).timestamp()  # 0004Z (2308Z used 23:09, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_packers': 'trend_packers.txt', 'trend_lions': 'trend_lions.txt', 'trend_raiders': 'trend_raiders.txt',","'trend_campbell': 'trend_campbell.txt', 'trend_smack': 'trend_smack.txt', 'trend_lula': 'trend_lula.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_packers','trend.Packers'),('trend_lions','trend.Lions'),('trend_raiders','trend.Raiders'),","('trend_campbell','trend.Dan Campbell'),('trend_smack','trend.Trey Smack'),('trend_lula','trend.Lula'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2308Z.json') and '/25/' in _c: continue","if _c.endswith('0004Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T2203Z'","_last = '2026-10-25T2308Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("one hundred and thirty-seventh run","one hundred and thirty-eighth run"),
("one hundred and thirty-fifth run","one hundred and thirty-sixth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/2308Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0004Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (2308Z: none read)","# 5) request picks (0004Z: none read)"),
("(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 580 long, so the 400 cap left out the 47 last six-hour posts and the 133 slowest-growing still-gaining posts, and no cited post)",
 "(this 00Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 599 long, so the 400 cap left out the 36 last six-hour posts, the 139 slowest-growing still-gaining posts and 24 rest-of-24-hour posts, and no cited post)"),
("quote/repost words this/is + you (quoted)","quote/repost words and/my + it (quoted)"),
("        if str(_x) in ('trend.Packers','trend.Lions','trend.Raiders'): return 'sports'  # 2308Z","        if str(_x) in ('trend.Dan Campbell','trend.Trey Smack','trend.Gibbs','trend.Green Bay','trend.#GBvsDET'): return 'sports'  # 0004Z: Lions beat Packers\n        if str(_x) in ('trend.Lula','trend.Brazil'): return 'world'  # 0004Z: Brazil presidential runoff\n        if str(_x) in ('trend.Packers','trend.Lions','trend.Raiders'): return 'sports'  # 2308Z"),
("then 42 in the second read: the 17 remaining plus 25 second-hop posts; 15 third-hop posts left unread for the budget)","then 38 in the second read: the 17 remaining plus 21 second-hop posts; 16 third-hop posts left unread for the budget)"),
("_GBDET = ('Packers','Lions','#GoPackGo','#OnePride','Goff','Jordan Love','Brian Branch','Josh Jacobs')  # 2308Z","_GBDET = ('Packers','Lions','#GoPackGo','#OnePride','Goff','Jordan Love','Brian Branch','Josh Jacobs','Dan Campbell','Trey Smack','Gibbs','Green Bay','#GBvsDET')  # 2308Z (0004Z added Dan Campbell, Trey Smack, Gibbs, Green Bay, #GBvsDET)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
s=s.replace("trend_posts['Raiders'] = [x for x","for _a,_b in [('Lula','Brazil'),('Brazil','Lula')]:\n    if trend_posts.get(_a): trend_posts[_b] = list(dict.fromkeys((trend_posts.get(_b) or []) + trend_posts[_a]))  # 0004Z: one event, Brazil runoff\ntrend_posts['Raiders'] = [x for x",1)
L={
"f'Evening run (7:08 PM ET":"            f'Evening run (8:04 PM ET Oct 25 / 00:04 UTC Oct 26, the 00Z slot and the first run of the new UTC day; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the X day reset at 00:00 UTC), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 599 ids, so the 400 cap left out the 36 last six-hour posts, the 139 slowest-growing still-gaining posts and 24 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words this/is":"            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2308Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 38 in the second read: the 17 remaining plus 21 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 16 third-hop posts left unread for the budget); 135 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 2308Z, and 2114383440703373608 (referenced by a post read this run, never captured) came back Not Found in both reads; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/open.json changed only its updated_at since 2308Z (watch.json dropped 2113944605888819292 and changed its updated_at); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
