s=open('build_capture.py').read()
TN=open('tn.txt').read().strip()
R=[
("Build capture/2026/10/26/0004Z.json","Build capture/2026/10/26/0102Z.json"),
("work/2026-10-26T0004Z'","work/2026-10-26T0102Z'"),
("RUN_ID = '2026-10-26T0004Z'","RUN_ID = '2026-10-26T0102Z'"),
("STARTED = '2026-10-26T00:04:00Z'","STARTED = '2026-10-26T01:02:00Z'"),
("OBS_AT = '2026-10-26T00:05:00Z'","OBS_AT = '2026-10-26T01:03:00Z'"),
("READS_BEFORE = 1000","READS_BEFORE = 980"),
("datetime(2026,10,26,0,5,tzinfo=timezone.utc).timestamp()  # 0004Z (","datetime(2026,10,26,1,3,tzinfo=timezone.utc).timestamp()  # 0102Z (0004Z used 00:05, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_campbell': 'trend_campbell.txt', 'trend_smack': 'trend_smack.txt', 'trend_lula': 'trend_lula.txt',","'trend_sneed': 'trend_sneed.txt', 'trend_chiefs': 'trend_chiefs.txt', 'trend_rhop': 'trend_rhop.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_campbell','trend.Dan Campbell'),('trend_smack','trend.Trey Smack'),('trend_lula','trend.Lula'),","('trend_sneed','trend.Sneed'),('trend_chiefs','trend.Chiefs'),('trend_rhop','trend.#RHOP'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0004Z.json') and '/26/' in _c: continue","if _c.endswith('0102Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T2308Z'","_last = '2026-10-26T0004Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("one hundred and thirty-eighth run","one hundred and thirty-ninth run"),
("one hundred and thirty-sixth run","one hundred and thirty-seventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0004Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0102Z.json'"),
("# 5) request picks (0004Z: none read)","# 5) request picks (0102Z: none read)"),
("(this 00Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 599 long, so the 400 cap left out the 36 last six-hour posts, the 139 slowest-growing still-gaining posts and 24 rest-of-24-hour posts, and no cited post)",
 "(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 56 last six-hour posts and the 122 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x) in ('trend.Dan Campbell','trend.Trey Smack'","        if str(_x) in ('trend.Sneed','trend.Chiefs'): return 'sports'  # 0102Z: Chiefs at Seahawks, Sunday night\n        if str(_x)=='trend.#RHOP': return 'entertainment'  # 0102Z: Real Housewives of Potomac\n        if str(_x) in ('trend.Dan Campbell','trend.Trey Smack'"),
("for _a,_b in [('Lula','Brazil'),('Brazil','Lula')]:","for _a,_b in [('Sneed','Chiefs'),('Chiefs','Sneed')]:\n    if trend_posts.get(_a): trend_posts[_b] = list(dict.fromkeys((trend_posts.get(_b) or []) + trend_posts[_a]))  # 0102Z: one event, Chiefs at Seahawks\nfor _a,_b in [('Lula','Brazil'),('Brazil','Lula')]:"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR="two screening reads by id (100 unread referenced posts, most pointed-at first, then 6 in the second read: the 5 remaining plus 2113737233853264245, which came back Not Found in the first read and was returned in the second; no second-hop or third-hop post left unread)"
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Sneed\", \"Chiefs\" and \"#RHOP\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words that/just + what (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Evening run (8:04 PM ET":"            f'Evening run (9:02 PM ET Oct 25 / 01:02 UTC Oct 26, the 01Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0004Z ended at 980, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 578 ids, so the 400 cap left out the 56 last six-hour posts and the 122 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Dan Campbell\"":"            f'trend names \"Sneed\", \"Chiefs\" and \"#RHOP\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words and/my":"            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0004Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 6 in the second read: the 5 remaining plus 2113737233853264245, which came back Not Found in the first read and was returned in the second (ids left out earlier as likely paid or sexual were not read again; no second-hop or third-hop post left unread); 2108062331095908717 came back Not Found again, as in 1105Z through 0004Z, and 1965290794203689251 (a referenced post, never captured) came back with an Authorization Error, as in 2003Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/ is unchanged since 0004Z (last requests/ commit a51108eb); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
