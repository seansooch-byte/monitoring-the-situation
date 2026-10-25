s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0704Z: "Ole Miss" (fourth; Texas beat No. 7 Ole Miss with no time remaining, Arch Manning three touchdowns, plus a weekend-of-upsets roundup), "Lincoln Riley" (seventh; USC lost to Wisconsin and fans call for Riley to be fired) and "Pelicans" (tenth; the Nuggets came back from 23 down against the Pelicans, Jokic triple-double and Murray 42, plus Herb Jones minutes complaints); "Utah" (second), "Utes" (third), "Houston" (sixth) and "Shock" (eighth) were attached in 0605Z and not read again for the budget (Utah, Utes and Houston are one game, Utah v Houston); "Cheesecake Factory" (first), "Brewers" (fifth) and "#MCRLA3" (ninth) had posts attached in 0704Z'
TN='three of the top-ten US names with no posts attached in 0800Z: "Cheesecake Factory" (first; Obama said Trump has the White House looking like Saddam Hussein opened a Cheesecake Factory, plus replies defending the chain), "Utah" (second; mixed: Utah Supreme Court Justice Diana Hagen resigned, the Utah lieutenant governor on voter rolls, Utah football coach Morgan Scalley on Nick Saban, Hurricane, Utah floods) and "Shock" (ninth and tenth; mixed uses of the word: a Nigerian electric-fence billboard video, boxer Shakur "Shock" Foster, a Marvel trailer reaction); "Brewers" (third), "Utes" (fourth, the same Utah football as "Utah"), "#MCRLA3" (sixth) and "Houston" (seventh) were not read again for the budget; "Ole Miss" (fifth) and "Lincoln Riley" (eighth) had posts attached in 0800Z'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Ole Miss", "Lincoln Riley" and "Pelicans"','trend names "Cheesecake Factory", "Utah" and "Shock"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0800Z.json","Build capture/2026/10/25/0903Z.json"),
("work/2026-10-25T0800Z'","work/2026-10-25T0903Z'"),
("RUN_ID = '2026-10-25T0800Z'","RUN_ID = '2026-10-25T0903Z'"),
("STARTED = '2026-10-25T08:00:00Z'","STARTED = '2026-10-25T09:03:00Z'"),
("OBS_AT = '2026-10-25T08:01:00Z'","OBS_AT = '2026-10-25T09:04:00Z'"),
("READS_BEFORE = 841","READS_BEFORE = 821"),
("datetime(2026,10,25,8,2,tzinfo=timezone.utc).timestamp()  # 0800Z (0704Z used 07:06, ","datetime(2026,10,25,9,5,tzinfo=timezone.utc).timestamp()  # 0903Z (0800Z used 08:02, 0704Z used 07:06, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_olemiss': 'trend_olemiss.txt', 'trend_riley': 'trend_riley.txt', 'trend_pelicans': 'trend_pelicans.txt',","'trend_cheesecake': 'trend_cheesecake.txt', 'trend_utah': 'trend_utah.txt', 'trend_shock': 'trend_shock.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_olemiss','trend.Ole Miss'),('trend_riley','trend.Lincoln Riley'),('trend_pelicans','trend.Pelicans'),","('trend_cheesecake','trend.Cheesecake Factory'),('trend_utah','trend.Utah'),('trend_shock','trend.Shock'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0800Z.json') and '/25/' in _c: continue","if _c.endswith('0903Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T0704Z'","_last = '2026-10-25T0800Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("one hundred and twenty-second run","one hundred and twenty-third run"),
("one hundred and twentieth run","one hundred and twenty-first run"),
("one hundred and eighteenth run","one hundred and nineteenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0800Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0903Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0800Z: none read)","# 5) request picks (0903Z: none read)"),
("two screening reads by id (99 unread referenced posts, most pointed-at first, then 17 second-hop posts in the second read; 11 third-hop posts left unread for the budget)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 11 remaining in the second read; 24 second-hop posts left unread for the budget)"),
("quote/repost words it/that + just (quoted)","quote/repost words what/the + this (quoted)"),
("(this 08Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 601 long, so the 400 cap left out the 59 last six-hour posts, the 100 slowest-growing still-gaining posts and 42 rest-of-24-hour posts, and no cited post)",
 "(this 09Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 557 long, so the 400 cap left out the 42 last six-hour posts and the 115 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (4:00 AM ET"):
    lines[k]="            f'Overnight run (5:03 AM ET Oct 25 / 09:03 UTC Oct 25, the 09Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0800Z ended at 821, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 557 ids, so the 400 cap left out the 42 last six-hour posts and the 115 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[k]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0800Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 99"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 11 remaining (ids left out earlier as likely paid or sexual were not read again; 24 second-hop posts left unread for the budget); 111 returned; 2108062331095908717 came back Not Found again as an expansion error, as in 1105Z through 0800Z; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0800Z (watch.json dropped 2113730012633321482, 2113720887052497277 and 2113723222843691122 and added 2114161656573944062, 2114094338158342403, 2113986385908842870, 2114008889796563101 and 2114187364176134471); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
