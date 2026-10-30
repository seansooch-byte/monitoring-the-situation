s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0102Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Sneed", "Chiefs" and "#RHOP"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Jalen Williams", "Darnold" and "Mahomes"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0102Z.json","Build capture/2026/10/26/0208Z.json"),
("work/2026-10-26T0102Z'","work/2026-10-26T0208Z'"),
("RUN_ID = '2026-10-26T0102Z'","RUN_ID = '2026-10-26T0208Z'"),
("STARTED = '2026-10-26T01:02:00Z'","STARTED = '2026-10-26T02:08:00Z'"),
("OBS_AT = '2026-10-26T01:03:00Z'","OBS_AT = '2026-10-26T02:09:00Z'"),
("READS_BEFORE = 980","READS_BEFORE = 960"),
("datetime(2026,10,26,1,3,tzinfo=timezone.utc).timestamp()  # 0102Z (","datetime(2026,10,26,2,9,tzinfo=timezone.utc).timestamp()  # 0208Z (0102Z used 01:03, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_sneed': 'trend_sneed.txt', 'trend_chiefs': 'trend_chiefs.txt', 'trend_rhop': 'trend_rhop.txt',","'trend_jwilliams': 'trend_jwilliams.txt', 'trend_darnold': 'trend_darnold.txt', 'trend_mahomes': 'trend_mahomes.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_sneed','trend.Sneed'),('trend_chiefs','trend.Chiefs'),('trend_rhop','trend.#RHOP'),","('trend_jwilliams','trend.Jalen Williams'),('trend_darnold','trend.Darnold'),('trend_mahomes','trend.Mahomes'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0102Z.json') and '/26/' in _c: continue","if _c.endswith('0208Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T0004Z'","_last = '2026-10-26T0102Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("one hundred and thirty-ninth run","one hundred and fortieth run"),
("one hundred and thirty-seventh run","one hundred and thirty-eighth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0102Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0208Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0102Z: none read)","# 5) request picks (0208Z: none read)"),
("(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 56 last six-hour posts and the 122 slowest-growing still-gaining posts, and no cited post)",
 "(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 46 last six-hour posts and the 132 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words that/just + what (quoted)","quote/repost words the/this + is (quoted)"),
("        if str(_x) in ('trend.Sneed','trend.Chiefs'): return 'sports'  # 0102Z","        if str(_x) in ('trend.Jalen Williams','trend.JDub','trend.Darnold','trend.Mahomes','trend.Seahawks'): return 'sports'  # 0208Z: Jalen Williams injury (Thunder); Chiefs at Seahawks\n        if str(_x) in ('trend.Sneed','trend.Chiefs'): return 'sports'  # 0102Z"),
("for _a,_b in [('Sneed','Chiefs'),('Chiefs','Sneed')]:","for _a,_b in [('Jalen Williams','JDub'),('JDub','Jalen Williams'),('Darnold','Mahomes'),('Mahomes','Darnold'),('Darnold','Seahawks'),('Mahomes','Seahawks')]:\n    if trend_posts.get(_a): trend_posts[_b] = list(dict.fromkeys((trend_posts.get(_b) or []) + trend_posts[_a]))  # 0208Z: one event each, Jalen Williams injury; Chiefs at Seahawks\nfor _a,_b in [('Sneed','Chiefs'),('Chiefs','Sneed')]:"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR="two screening reads by id (100 unread referenced posts, most pointed-at first, then 24 in the second read: the 1 remaining plus 23 second-hop posts; 15 third-hop posts left unread for the budget)"
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Jalen Williams\", \"Darnold\" and \"Mahomes\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Evening run (9:02 PM ET":"            f'Evening run (10:08 PM ET Oct 25 / 02:08 UTC Oct 26, the 02Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0102Z ended at 960, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 578 ids, so the 400 cap left out the 46 last six-hour posts and the 132 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Sneed\"":"            f'trend names \"Jalen Williams\", \"Darnold\" and \"Mahomes\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words that/just":"            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0102Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 24 in the second read: the 1 remaining plus 23 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 15 third-hop posts left unread for the budget); 2108062331095908717 came back Not Found again, as in 1105Z through 0102Z, and 2104903179187978733 (a referenced post, never captured) came back with an Authorization Error in both reads; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'No new request: requests/ is unchanged since 0004Z (last requests/ commit a51108eb); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
