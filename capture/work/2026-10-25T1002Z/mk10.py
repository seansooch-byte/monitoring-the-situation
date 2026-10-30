s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0800Z: "Cheesecake Factory" (first; Obama said Trump has the White House looking like Saddam Hussein opened a Cheesecake Factory, plus replies defending the chain), "Utah" (second; mixed: Utah Supreme Court Justice Diana Hagen resigned, the Utah lieutenant governor on voter rolls, Utah football coach Morgan Scalley on Nick Saban, Hurricane, Utah floods) and "Shock" (ninth and tenth; mixed uses of the word: a Nigerian electric-fence billboard video, boxer Shakur "Shock" Foster, a Marvel trailer reaction); "Brewers" (third), "Utes" (fourth, the same Utah football as "Utah"), "#MCRLA3" (sixth) and "Houston" (seventh) were not read again for the budget; "Ole Miss" (fifth) and "Lincoln Riley" (eighth) had posts attached in 0800Z'
TN='three of the top-ten US names with no posts attached in 0903Z: "Good Sunday" (second; Sunday-morning greeting posts, all small), "Brewers" (third; Milwaukee came back from 4-0 down to win World Series Game 2 and lead 2-0, Christian Yelich pinch-hit go-ahead home run) and "#MCRLA3" (fifth; My Chemical Romance third Hollywood Bowl show, Gerard Way with a chainsaw on stage); "Utes" (sixth, the same Utah football as "Utah"), "Ole Miss" (seventh), "Lincoln Riley" (eighth) and "The Cut" (ninth) were not read for the budget; "Cheesecake Factory" (first), "Utah" (fourth) and "Shock" (tenth) had posts attached in 0903Z'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Cheesecake Factory", "Utah" and "Shock"','trend names "Good Sunday", "Brewers" and "#MCRLA3"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0903Z.json","Build capture/2026/10/25/1002Z.json"),
("work/2026-10-25T0903Z'","work/2026-10-25T1002Z'"),
("RUN_ID = '2026-10-25T0903Z'","RUN_ID = '2026-10-25T1002Z'"),
("STARTED = '2026-10-25T09:03:00Z'","STARTED = '2026-10-25T10:02:00Z'"),
("OBS_AT = '2026-10-25T09:04:00Z'","OBS_AT = '2026-10-25T10:03:00Z'"),
("READS_BEFORE = 821","READS_BEFORE = 801"),
("datetime(2026,10,25,9,5,tzinfo=timezone.utc).timestamp()  # 0903Z (0800Z used 08:02, ","datetime(2026,10,25,10,5,tzinfo=timezone.utc).timestamp()  # 1002Z (0903Z used 09:05, 0800Z used 08:02, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_my': 'repost_my.txt',"),
("'trend_cheesecake': 'trend_cheesecake.txt', 'trend_utah': 'trend_utah.txt', 'trend_shock': 'trend_shock.txt',","'trend_goodsunday': 'trend_goodsunday.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_mcrla3': 'trend_mcrla3.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_my','repost'),"),
("('trend_cheesecake','trend.Cheesecake Factory'),('trend_utah','trend.Utah'),('trend_shock','trend.Shock'),","('trend_goodsunday','trend.Good Sunday'),('trend_brewers','trend.Brewers'),('trend_mcrla3','trend.#MCRLA3'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0903Z.json') and '/25/' in _c: continue","if _c.endswith('1002Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T0800Z'","_last = '2026-10-25T0903Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
 'common words "is", "you" and "my", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("one hundred and twenty-third run","one hundred and twenty-fourth run"),
("one hundred and twenty-first run","one hundred and twenty-second run"),
("one hundred and nineteenth run","one hundred and twentieth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0903Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1002Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0903Z: none read)","# 5) request picks (1002Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 11 remaining in the second read; 24 second-hop posts left unread for the budget)","two screening reads by id (96 unread referenced posts, most pointed-at first, then 24 second-hop posts in the second read; 11 third-hop posts left unread for the budget)"),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + my (quoted)"),
("(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 557 long, so the 400 cap left out the 42 last six-hour posts and the 115 slowest-growing still-gaining posts, and no cited post)",
 "(this 10Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 562 long, so the 400 cap left out the 36 last six-hour posts and the 126 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
s=s.replace("        if str(_x)=='trend.Good Sunday': return 'life'  # 1004Z","        if str(_x)=='trend.Good Sunday': return 'life'  # 1004Z\n        if str(_x)=='trend.#MCRLA3': return 'music'  # 1002Z: My Chemical Romance Hollywood Bowl shows",1)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (5:03 AM ET"):
    lines[k]="            f'Overnight run (6:02 AM ET Oct 25 / 10:02 UTC Oct 25, the 10Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0903Z ended at 801, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 562 ids, so the 400 cap left out the 36 last six-hour posts and the 126 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[k]="            f'quote/repost words is/you + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0903Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 96 unread referenced, reply-parent and media-source posts, most pointed-at first, then 24 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 11 third-hop posts left unread for the budget); 119 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 0903Z; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0903Z (watch.json dropped 2113731069518434519 and added 2114129811224629577 and 2114029066349093173); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
