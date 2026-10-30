s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0400Z: "Ole Miss" (first; Texas beat No. 7 Ole Miss, Arch Manning three touchdowns), "Brewers" (third; the Brewers erased a 4-0 deficit to lead the World Series 2-0) and "Lincoln Riley" (fourth; Wisconsin upset No. 16 USC); "Cheesecake Factory" (second) had a post attached in 0400Z; "Arch" (fifth), "Texas" (ninth) and "#HookEm" (tenth) are the same Texas v Ole Miss game; "Foster" (sixth), "Pelicans" (seventh) and "Trevon Brazile" (eighth) were attached in 0400Z'
TN='three of the top-ten US names with no posts attached in 0501Z: "Utah" (fourth; No. 10 Utah beat No. 14 Houston 21-13 to stay undefeated, plus Hurricane, Utah flash flooding), "Shock" (sixth and seventh, listed twice; no single event in the stream, the word in unrelated posts) and "Houston" (tenth; the same Utah v Houston game, plus Houston ICE posts: voters leaving stickers where Lorenzo Salgado Araujo was shot and a Houston ICE raid); "Cheesecake Factory" (first) was attached in 0400Z and "Pelicans" (eighth) in 0400Z, not read again for the budget; "Ole Miss" (second), "Brewers" (third), "Lincoln Riley" (fifth) and "Arch" (ninth) had posts attached in 0501Z'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Ole Miss", "Brewers" and "Lincoln Riley"','trend names "Utah", "Shock" and "Houston"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0501Z.json","Build capture/2026/10/25/0605Z.json"),
("work/2026-10-25T0501Z'","work/2026-10-25T0605Z'"),
("RUN_ID = '2026-10-25T0501Z'","RUN_ID = '2026-10-25T0605Z'"),
("STARTED = '2026-10-25T05:01:00Z'","STARTED = '2026-10-25T06:05:00Z'"),
("OBS_AT = '2026-10-25T05:02:00Z'","OBS_AT = '2026-10-25T06:06:00Z'"),
("READS_BEFORE = 900","READS_BEFORE = 880"),
("datetime(2026,10,25,5,5,tzinfo=timezone.utc).timestamp()  # 0501Z (0400Z used 04:04, ","datetime(2026,10,25,6,7,tzinfo=timezone.utc).timestamp()  # 0605Z (0501Z used 05:05, 0400Z used 04:04, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_olemiss': 'trend_olemiss.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_riley': 'trend_riley.txt',","'trend_utah': 'trend_utah.txt', 'trend_shock': 'trend_shock.txt', 'trend_houston': 'trend_houston.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_olemiss','trend.Ole Miss'),('trend_brewers','trend.Brewers'),('trend_riley','trend.Lincoln Riley'),","('trend_utah','trend.Utah'),('trend_shock','trend.Shock'),('trend_houston','trend.Houston'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0501Z.json') and '/25/' in _c: continue","if _c.endswith('0605Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T0400Z'","_last = '2026-10-25T0501Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("one hundred and nineteenth run","one hundred and twentieth run"),
("one hundred and seventeenth run","one hundred and eighteenth run"),
("one hundred and fifteenth run","one hundred and sixteenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0501Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0605Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0501Z: none read)","# 5) request picks (0605Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 27 second-hop and remaining posts in the second read)","one screening read by id (96 unread referenced posts, most pointed-at first; no second-hop post was left unread, so no second read)"),
("quote/repost words that/just + what (quoted)","quote/repost words the/this + is (quoted)"),
("in the 12:00-05:00 UTC band, up to 42","in the 06:00-11:00 UTC band, up to 20"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (1:01 AM ET"):
    lines[k]="            f'Overnight run (2:05 AM ET Oct 25 / 06:05 UTC Oct 25, the 06Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0501Z ended at 880, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 537 ids, so the 400 cap left out the 40 last six-hour posts and the 97 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[k]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0501Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'one screening read by id: 96 unread referenced, reply-parent and media-source posts, most pointed-at first (ids left out earlier as likely paid or sexual were not read again); 96 returned; 2108062331095908717 came back Not Found again as an expansion error, as in 1105Z through 0501Z; every second-hop post the read led to came back in its includes, so no second screening read was needed; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0501Z (watch.json dropped 2113675605451456873 and 2113667772211421244 and added 2114063986744275011, 2113997959117561902 and 2114042449287168149); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
  elif st.startswith("f'trend names \"Utah\""):
    hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
