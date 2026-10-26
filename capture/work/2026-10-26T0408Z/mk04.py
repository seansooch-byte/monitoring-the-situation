s=open('build_capture.py').read()
OLDTN=open('../2026-10-26T0306Z/tn.txt').read().strip()
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
a0='trend names "Chiefs", "Butker" and "Packers"'
print('tn names count',s.count(a0))
s=s.replace(a0,'trend names "Eric Bauza" and "Jalen Williams"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/26/0306Z.json","Build capture/2026/10/26/0408Z.json"),
("work/2026-10-26T0306Z'","work/2026-10-26T0408Z'"),
("RUN_ID = '2026-10-26T0306Z'","RUN_ID = '2026-10-26T0408Z'"),
("STARTED = '2026-10-26T03:06:00Z'","STARTED = '2026-10-26T04:08:00Z'"),
("OBS_AT = '2026-10-26T03:07:00Z'","OBS_AT = '2026-10-26T04:08:00Z'"),
("READS_BEFORE = 940","READS_BEFORE = 918"),
("datetime(2026,10,26,3,7,tzinfo=timezone.utc).timestamp()  # 0306Z (","datetime(2026,10,26,4,8,tzinfo=timezone.utc).timestamp()  # 0408Z (0306Z used 03:07, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt', 'req_bolsonaro': 'req_bolsonaro.txt', 'req_flavio': 'req_flavio.txt',","'repost_just': 'repost_just.txt',"),
("'trend_chiefs': 'trend_chiefs.txt', 'trend_butker': 'trend_butker.txt', 'trend_packers': 'trend_packers.txt',","'trend_bauza': 'trend_bauza.txt', 'trend_jwilliams': 'trend_jwilliams.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_chiefs','trend.Chiefs'),('trend_butker','trend.Butker'),('trend_packers','trend.Packers'),","('trend_bauza','trend.Eric Bauza'),('trend_jwilliams','trend.Jalen Williams'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0306Z.json') and '/26/' in _c: continue","if _c.endswith('0408Z.json') and '/26/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-26T0208Z'","_last = '2026-10-26T0306Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)'),
("one hundred and forty-first run","one hundred and forty-second run"),
("one hundred and thirty-ninth run","one hundred and fortieth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0306Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/0408Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0306Z: r-2026-10-26-01)","# 5) request picks (0408Z: none read)"),
("(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 579 long, so the 400 cap left out the 61 last six-hour posts and the 118 slowest-growing still-gaining posts, and no cited post)",
 "(this 04Z run is a fourth hour, so the rest of the last 24 hours, slowest growing last, joined the list; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 597 long, so the 400 cap left out the 54 last six-hour posts, the 112 slowest-growing still-gaining posts and the 31 slowest rest-of-24-hour posts, and no cited post)"),
("quote/repost words you/and + my (quoted)","quote/repost words it/that + just (quoted)"),
("        if str(_x) in ('trend.Chiefs','trend.Butker'): return 'sports'  # 0306Z","        if str(_x)=='trend.Eric Bauza': return 'entertainment'  # 0408Z: voice actor\n        if str(_x) in ('trend.Chiefs','trend.Butker'): return 'sports'  # 0306Z"),
("for _a,_b in [('Chiefs','Butker'),","for _a,_b in [('Jalen Williams','JDub')]:\n    if trend_posts.get(_a): trend_posts[_b] = list(dict.fromkeys((trend_posts.get(_b) or []) + trend_posts[_a]))  # 0408Z: one event, Jalen Williams injury\nfor _a,_b in [('Chiefs','Butker'),"),
("REQ_PICKS = {'r-2026-10-26-01': ['2114540676385796571', '2114524317891567653', '2114464153544896672', '2114481162605183155', '2114513330664575450']}\nREQ_FILES = {'r-2026-10-26-01': 'req_bolsonaro'}\nREQ_ONLY = {t['id'] for t in (raw['req_bolsonaro'].get('data') or [])} - set(REQ_PICKS['r-2026-10-26-01'])",
 "REQ_PICKS = {}\nREQ_FILES = {}\nREQ_ONLY = set()"),
("ANSWERED_EARLIER = {","ANSWERED_EARLIER = {'r-2026-10-26-01':'2026-10-26T0306Z',"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
# ANSWERS block -> []
i=s.find("ANSWERS = [{"); j=s.find("\n}]",i)+3
s=s[:i]+"ANSWERS = []"+s[j:]
SCR="two screening reads by id (100 unread referenced posts, most pointed-at first, then 25 in the second read: the 4 remaining plus 21 second-hop posts; 8 third-hop posts left unread for the budget)"
L={
"'sources: references followed one hop":"    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names \"Eric Bauza\" and \"Jalen Williams\" (\"<name> lang:en is:retweet\", newest first, 25 each; "+TN.replace("'","\\'")+"); quote/repost words it/that + just (quoted); hourly desks politics/entertainment/sports/internet; "+SCR+"; story clusters not read for the budget; screened by id with global floor/pace',",
"f'Night run (11:06 PM ET":"            f'Night run (12:08 AM ET Oct 26 / 04:08 UTC Oct 26, the 04Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0306Z ended at 918, so no read went elsewhere in between), parallel batches of up to 12, no 429 refusals. '",
"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z":"            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 597 ids, so the 400 cap left out the 54 last six-hour posts, the 112 slowest-growing still-gaining posts and the 31 slowest rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '",
"f'trend names \"Chiefs\"":"            f'trend names \"Eric Bauza\" and \"Jalen Williams\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '",
"f'quote/repost words you/and":"            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0306Z, so news/money/science were next in rotation); '",
"f'two screening reads by id: 100":"            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 25 in the second read: the 4 remaining plus 21 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 8 third-hop posts left unread for the budget); 2108062331095908717 came back Not Found again, as in 1105Z through 0306Z; story clusters (search_news) not read for the budget. '",
"f'New request r-2026-10-26-01":"            f'No new request: r-2026-10-26-01 was answered in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '",
"f'Not read: news/money/science sensors":"            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '",
}
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  for pre,new in L.items():
    if st.startswith(pre): lines[k]=new; hit+=1
print('line hits',hit,'of',len(L))
open('build_capture.py','w').write('\n'.join(lines))
