s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0501Z: "Utah" (fourth; No. 10 Utah beat No. 14 Houston 21-13 to stay undefeated, plus Hurricane, Utah flash flooding), "Shock" (sixth and seventh, listed twice; no single event in the stream, the word in unrelated posts) and "Houston" (tenth; the same Utah v Houston game, plus Houston ICE posts: voters leaving stickers where Lorenzo Salgado Araujo was shot and a Houston ICE raid); "Cheesecake Factory" (first) was attached in 0400Z and "Pelicans" (eighth) in 0400Z, not read again for the budget; "Ole Miss" (second), "Brewers" (third), "Lincoln Riley" (fifth) and "Arch" (ninth) had posts attached in 0501Z'
TN='three of the top-ten US names with no posts attached in 0605Z: "Cheesecake Factory" (first; Obama said Trump has the White House looking like Saddam Hussein opened a Cheesecake Factory, plus replies), "Brewers" (fourth; the Brewers erased a 4-0 deficit to lead the World Series 2-0, plus a StubHub ticket complaint from a Brewers fan) and "#MCRLA3" (tenth; My Chemical Romance third Los Angeles show, Gerard Way with a chainsaw and the Black Parade ending); "Ole Miss" (second), "Lincoln Riley" (seventh) and "Pelicans" (ninth) were attached in 0501Z or 0400Z and not read again for the budget; "Utes" (fifth) is the same Utah v Houston game as "Utah" (third) and "Houston" (sixth), which with "Shock" (eighth) were attached in 0605Z'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Utah", "Shock" and "Houston"','trend names "Cheesecake Factory", "Brewers" and "#MCRLA3"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0605Z.json","Build capture/2026/10/25/0704Z.json"),
("work/2026-10-25T0605Z'","work/2026-10-25T0704Z'"),
("RUN_ID = '2026-10-25T0605Z'","RUN_ID = '2026-10-25T0704Z'"),
("STARTED = '2026-10-25T06:05:00Z'","STARTED = '2026-10-25T07:04:00Z'"),
("OBS_AT = '2026-10-25T06:06:00Z'","OBS_AT = '2026-10-25T07:05:00Z'"),
("READS_BEFORE = 880","READS_BEFORE = 861"),
("datetime(2026,10,25,6,7,tzinfo=timezone.utc).timestamp()  # 0605Z (0501Z used 05:05, ","datetime(2026,10,25,7,6,tzinfo=timezone.utc).timestamp()  # 0704Z (0605Z used 06:07, 0501Z used 05:05, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_utah': 'trend_utah.txt', 'trend_shock': 'trend_shock.txt', 'trend_houston': 'trend_houston.txt',","'trend_cheesecake': 'trend_cheesecake.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_mcrla3': 'trend_mcrla3.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_utah','trend.Utah'),('trend_shock','trend.Shock'),('trend_houston','trend.Houston'),","('trend_cheesecake','trend.Cheesecake Factory'),('trend_brewers','trend.Brewers'),('trend_mcrla3','trend.#MCRLA3'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0605Z.json') and '/25/' in _c: continue","if _c.endswith('0704Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T0501Z'","_last = '2026-10-25T0605Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("one hundred and twentieth run","one hundred and twenty-first run"),
("one hundred and eighteenth run","one hundred and nineteenth run"),
("one hundred and sixteenth run","one hundred and seventeenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0605Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0704Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0605Z: none read)","# 5) request picks (0704Z: none read)"),
("one screening read by id (96 unread referenced posts, most pointed-at first; no second-hop post was left unread, so no second read)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 5 remaining posts in the second read)"),
("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (2:05 AM ET"):
    lines[k]="            f'Overnight run (3:04 AM ET Oct 25 / 07:04 UTC Oct 25, the 07Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0605Z ended at 861, so no read went elsewhere in between), parallel batches of up to 15, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 550 ids, so the 400 cap left out the 47 last six-hour posts and the 103 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[k]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0605Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'one screening read by id: 96"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 5 remaining (ids left out earlier as likely paid or sexual were not read again); 105 returned; 2108062331095908717 came back Not Found again as an expansion error, as in 1105Z through 0605Z; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0605Z (watch.json dropped 2113680701770068067 and added 2114115124395196886); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
