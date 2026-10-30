s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0903Z: "Good Sunday" (second; Sunday-morning greeting posts, all small), "Brewers" (third; Milwaukee came back from 4-0 down to win World Series Game 2 and lead 2-0, Christian Yelich pinch-hit go-ahead home run) and "#MCRLA3" (fifth; My Chemical Romance third Hollywood Bowl show, Gerard Way with a chainsaw on stage); "Utes" (sixth, the same Utah football as "Utah"), "Ole Miss" (seventh), "Lincoln Riley" (eighth) and "The Cut" (ninth) were not read for the budget; "Cheesecake Factory" (first), "Utah" (fourth) and "Shock" (tenth) had posts attached in 0903Z'
TN=open('tn.txt').read().strip()
assert s.count(OLDTN)>=1
s=s.replace('trend names "Good Sunday", "Brewers" and "#MCRLA3"','trend names "Cheesecake Factory", "Courtois" and "Blessed Sunday"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1002Z.json","Build capture/2026/10/25/1107Z.json"),
("work/2026-10-25T1002Z'","work/2026-10-25T1107Z'"),
("RUN_ID = '2026-10-25T1002Z'","RUN_ID = '2026-10-25T1107Z'"),
("STARTED = '2026-10-25T10:02:00Z'","STARTED = '2026-10-25T11:07:00Z'"),
("OBS_AT = '2026-10-25T10:03:00Z'","OBS_AT = '2026-10-25T11:08:00Z'"),
("READS_BEFORE = 801","READS_BEFORE = 781"),
("READS_USED = READS_BEFORE - READS_AFTER","READS_USED = 20  # 781-757=24 but 4 reads went to the 7:03 AM ET briefing during this run"),
("datetime(2026,10,25,10,5,tzinfo=timezone.utc).timestamp()  # 1002Z (","datetime(2026,10,25,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (1002Z used 10:05, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_and': 'quote_and.txt', 'quote_it': 'quote_it.txt',"),
("'repost_my': 'repost_my.txt',","'repost_that': 'repost_that.txt',"),
("'trend_goodsunday': 'trend_goodsunday.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_mcrla3': 'trend_mcrla3.txt',","'trend_cheesecake': 'trend_cheesecake.txt', 'trend_courtois': 'trend_courtois.txt', 'trend_blessedsunday': 'trend_blessedsunday.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_my','repost'),","('quote_and','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_goodsunday','trend.Good Sunday'),('trend_brewers','trend.Brewers'),('trend_mcrla3','trend.#MCRLA3'),","('trend_cheesecake','trend.Cheesecake Factory'),('trend_courtois','trend.Courtois'),('trend_blessedsunday','trend.Blessed Sunday'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1002Z.json') and '/25/' in _c: continue","if _c.endswith('1107Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T0903Z'","_last = '2026-10-25T1002Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "is", "you" and "my", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "and", "it" and "that", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)'),
("one hundred and twenty-fourth run","one hundred and twenty-fifth run"),
("one hundred and twenty-second run","one hundred and twenty-third run"),
("one hundred and twentieth run","one hundred and twenty-first run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1002Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1107Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1002Z: none read)","# 5) request picks (1107Z: none read)"),
("two screening reads by id (96 unread referenced posts, most pointed-at first, then 24 second-hop posts in the second read; 11 third-hop posts left unread for the budget)","two screening reads by id (100 unread referenced posts, most pointed-at first, then 35 (the 9 remaining plus 26 second-hop posts) in the second read; 21 third-hop posts left unread for the budget)"),
("quote/repost words is/you + my (quoted)","quote/repost words and/it + that (quoted)"),
("(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 562 long, so the 400 cap left out the 36 last six-hour posts and the 126 slowest-growing still-gaining posts, and no cited post)",
 "(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 562 long, so the 400 cap left out the 34 last six-hour posts and the 128 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (6:02 AM ET"):
    lines[k]="            f'Morning run (7:07 AM ET Oct 25 / 11:07 UTC Oct 25, the 11Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the counter fell 24 because 4 reads went to the 7:03 AM ET daily briefing while this run was reading; 1002Z ended at 781), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 562 ids, so the 400 cap left out the 34 last six-hour posts and the 128 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Cheesecake Factory\""):
    pass
  elif st.startswith("f'quote/repost words is/you"):
    lines[k]="            f'quote/repost words and/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1002Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 96"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 35 (the 9 remaining plus 26 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 21 third-hop posts left unread for the budget); 133 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 1002Z, and 2113278168291279352 Not Found; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 1002Z (watch.json dropped 2113746559527727121 and 2113750562042769432 and added 2114204084932858174, 2114202300780601830 and 2114026298825674781); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
