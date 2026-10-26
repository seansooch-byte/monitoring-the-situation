s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0208Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Jalen Williams", "Darnold" and "Mahomes"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Chiefs", "Butker" and "Packers"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0208Z.json","Build capture/2026/10/26/0306Z.json"),
("work/2026-10-26T0208Z'","work/2026-10-26T0306Z'"),
("RUN_ID = '2026-10-26T0208Z'","RUN_ID = '2026-10-26T0306Z'"),
("STARTED = '2026-10-26T02:08:00Z'","STARTED = '2026-10-26T03:06:00Z'"),
("OBS_AT = '2026-10-26T02:09:00Z'","OBS_AT = '2026-10-26T03:07:00Z'"),
("READS_BEFORE = 960","READS_BEFORE = 940"),
("datetime(2026,10,26,2,9,tzinfo=timezone.utc).timestamp()  # 0208Z (","datetime(2026,10,26,3,7,tzinfo=timezone.utc).timestamp()  # 0306Z (0208Z used 02:09, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt', 'req_bolsonaro': 'req_bolsonaro.txt', 'req_flavio': 'req_flavio.txt',"),
("'trend_jwilliams': 'trend_jwilliams.txt', 'trend_darnold': 'trend_darnold.txt', 'trend_mahomes': 'trend_mahomes.txt',","'trend_chiefs': 'trend_chiefs.txt', 'trend_butker': 'trend_butker.txt', 'trend_packers': 'trend_packers.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_jwilliams','trend.Jalen Williams'),('trend_darnold','trend.Darnold'),('trend_mahomes','trend.Mahomes'),","('trend_chiefs','trend.Chiefs'),('trend_butker','trend.Butker'),('trend_packers','trend.Packers'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0208Z.json') and '/26/' in _c: continue","if _c.endswith('0306Z.json') and '/26/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-26T0102Z'","_last = '2026-10-26T0208Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("one hundred and fortieth run","one hundred and forty-first run"),
("one hundred and thirty-eighth run","one hundred and thirty-ninth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0208Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0306Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0208Z: none read)","# 5) request picks (0306Z: r-2026-10-26-01)"),
("(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 578 long, so the 400 cap left out the 46 last six-hour posts and the 132 slowest-growing still-gaining posts, and no cited post)",
 "(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 579 long, so the 400 cap left out the 61 last six-hour posts and the 118 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)"),
("        if str(_x) in ('trend.Jalen Williams','trend.JDub'","        if str(_x) in ('trend.Chiefs','trend.Butker'): return 'sports'  # 0306Z: Chiefs at Seahawks, Sunday night\n        if str(_x) in ('trend.Jalen Williams','trend.JDub'"),
("for _a,_b in [('Jalen Williams','JDub'),","for _a,_b in [('Chiefs','Butker'),('Butker','Chiefs'),('Butker','Mahomes'),('Chiefs','Mahomes'),('Butker','Seahawks'),('Chiefs','Seahawks'),('Butker','Darnold'),('Chiefs','Darnold')]:\n    if trend_posts.get(_a): trend_posts[_b] = list(dict.fromkeys((trend_posts.get(_b) or []) + trend_posts[_a]))  # 0306Z: one event, Chiefs at Seahawks\nfor _a,_b in [('Jalen Williams','JDub'),"),
("REQ_PICKS = {}\nREQ_FILES = {}\nREQ_ONLY = set()",
 "REQ_PICKS = {'r-2026-10-26-01': ['2114540676385796571', '2114524317891567653', '2114464153544896672', '2114481162605183155', '2114513330664575450']}\nREQ_FILES = {'r-2026-10-26-01': 'req_bolsonaro'}\nREQ_ONLY = {t['id'] for t in (raw['req_bolsonaro'].get('data') or [])} - set(REQ_PICKS['r-2026-10-26-01'])"),
("REQ_Q = {\n","REQ_Q = {\n    'r-2026-10-26-01': 'two search_posts_all reads, start_time 2026-10-25T18:00:00Z, 25 results each: (\"Flávio Bolsonaro\" OR \"Flavio Bolsonaro\" OR FlavioBolsonaro OR TSE OR \"electoral court\" OR \"Superior Electoral Court\") (Lula OR runoff OR result OR resultado OR eleito OR elected OR winner OR challenge OR recurso OR horário OR \"voting hours\") -is:retweet -is:reply, relevancy; and from:FlavioBolsonaro -is:reply, newest first (no result)',\n"),
("ANSWERS = []","ANSWERS = [{\n    'request_id': 'r-2026-10-26-01',\n    'status': 'ok',\n    'post_ids': [i for i in REQ_PICKS['r-2026-10-26-01'] if i in _here],\n    'note': \"Two searches from 2026-10-25T18:00Z. from:FlavioBolsonaro returned no post since then, so no statement from Flávio Bolsonaro himself was found. Kept five posts: DiretoDaAmerica (2114540676385796571) reports that Flávio Bolsonaro will not concede and will ask for the election to be annulled, without a source link or quote in the text; tommysantos14 (2114524317891567653) quotes a report that both campaigns asked the Superior Electoral Court to extend voting hours; MayadeenEnglish (2114464153544896672) says the court paused the count after a Supreme Court justice ordered voting extended by two hours; VocalPolitics1 (2114481162605183155) says the court's president delayed the extension decision until many ballot boxes had closed; ConflictRadarME (2114513330664575450) says the court officially announced Lula as the winner. No post from the electoral court's own account and no filed legal challenge was returned.\",\n}]"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
SCR="two screening reads by id (100 unread referenced posts, most pointed-at first, then 41 in the second read: the 19 remaining plus 22 second-hop posts; 8 third-hop posts left unread for the budget)"
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"Chiefs\", \"Butker\" and \"Packers\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; request r-2026-10-26-01 (two reads); "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Evening run (10:08 PM ET":"            f'Night run (11:06 PM ET Oct 25 / 03:06 UTC Oct 26, the 03Z slot; 12:00-05:00 UTC band, up to 42, kept to about 22 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0208Z ended at 940, so no read went elsewhere in between), parallel batches of up to 14, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 579 ids, so the 400 cap left out the 61 last six-hour posts and the 118 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'quote/repost words the/this":"            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0208Z, so culture/sports/online were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 41 in the second read: the 19 remaining plus 22 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 8 third-hop posts left unread for the budget); 2108062331095908717 came back Not Found again, as in 1105Z through 0208Z; story clusters (search_news) not read for the budget. '",
"f'No new request:":"            f'New request r-2026-10-26-01 (requests/ commit 1007a88a): two reads, a relevancy search from 2026-10-25T18:00Z and from:FlavioBolsonaro (no result); five posts kept, see answers. r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: culture/sports/online sensors":"            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
