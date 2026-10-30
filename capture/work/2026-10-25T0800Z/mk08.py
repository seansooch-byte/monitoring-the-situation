s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0605Z: "Cheesecake Factory" (first; Obama said Trump has the White House looking like Saddam Hussein opened a Cheesecake Factory, plus replies), "Brewers" (fourth; the Brewers erased a 4-0 deficit to lead the World Series 2-0, plus a StubHub ticket complaint from a Brewers fan) and "#MCRLA3" (tenth; My Chemical Romance third Los Angeles show, Gerard Way with a chainsaw and the Black Parade ending); "Ole Miss" (second), "Lincoln Riley" (seventh) and "Pelicans" (ninth) were attached in 0501Z or 0400Z and not read again for the budget; "Utes" (fifth) is the same Utah v Houston game as "Utah" (third) and "Houston" (sixth), which with "Shock" (eighth) were attached in 0605Z'
TN='three of the top-ten US names with no posts attached in 0704Z: "Ole Miss" (fourth; Texas beat No. 7 Ole Miss with no time remaining, Arch Manning three touchdowns, plus a weekend-of-upsets roundup), "Lincoln Riley" (seventh; USC lost to Wisconsin and fans call for Riley to be fired) and "Pelicans" (tenth; the Nuggets came back from 23 down against the Pelicans, Jokic triple-double and Murray 42, plus Herb Jones minutes complaints); "Utah" (second), "Utes" (third), "Houston" (sixth) and "Shock" (eighth) were attached in 0605Z and not read again for the budget (Utah, Utes and Houston are one game, Utah v Houston); "Cheesecake Factory" (first), "Brewers" (fifth) and "#MCRLA3" (ninth) had posts attached in 0704Z'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Cheesecake Factory", "Brewers" and "#MCRLA3"','trend names "Ole Miss", "Lincoln Riley" and "Pelicans"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0704Z.json","Build capture/2026/10/25/0800Z.json"),
("work/2026-10-25T0704Z'","work/2026-10-25T0800Z'"),
("RUN_ID = '2026-10-25T0704Z'","RUN_ID = '2026-10-25T0800Z'"),
("STARTED = '2026-10-25T07:04:00Z'","STARTED = '2026-10-25T08:00:00Z'"),
("OBS_AT = '2026-10-25T07:05:00Z'","OBS_AT = '2026-10-25T08:01:00Z'"),
("READS_BEFORE = 861","READS_BEFORE = 841"),
("datetime(2026,10,25,7,6,tzinfo=timezone.utc).timestamp()  # 0704Z (0605Z used 06:07, ","datetime(2026,10,25,8,2,tzinfo=timezone.utc).timestamp()  # 0800Z (0704Z used 07:06, 0605Z used 06:07, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_cheesecake': 'trend_cheesecake.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_mcrla3': 'trend_mcrla3.txt',","'trend_olemiss': 'trend_olemiss.txt', 'trend_riley': 'trend_riley.txt', 'trend_pelicans': 'trend_pelicans.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_cheesecake','trend.Cheesecake Factory'),('trend_brewers','trend.Brewers'),('trend_mcrla3','trend.#MCRLA3'),","('trend_olemiss','trend.Ole Miss'),('trend_riley','trend.Lincoln Riley'),('trend_pelicans','trend.Pelicans'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0704Z.json') and '/25/' in _c: continue","if _c.endswith('0800Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T0605Z'","_last = '2026-10-25T0704Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)'),
("one hundred and twenty-first run","one hundred and twenty-second run"),
("one hundred and nineteenth run","one hundred and twentieth run"),
("one hundred and seventeenth run","one hundred and eighteenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0704Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0800Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0704Z: none read)","# 5) request picks (0800Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 5 remaining posts in the second read)","two screening reads by id (99 unread referenced posts, most pointed-at first, then 17 second-hop posts in the second read; 11 third-hop posts left unread for the budget)"),
("quote/repost words you/and + my (quoted)","quote/repost words it/that + just (quoted)"),
("(this 07Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 550 long, so the 400 cap left out the 47 last six-hour posts and the 103 slowest-growing still-gaining posts, and no cited post)",
 "(this 08Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 601 long, so the 400 cap left out the 59 last six-hour posts, the 100 slowest-growing still-gaining posts and 42 rest-of-24-hour posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Overnight run (3:04 AM ET"):
    lines[k]="            f'Overnight run (4:00 AM ET Oct 25 / 08:00 UTC Oct 25, the 08Z slot; 06:00-11:00 UTC band, up to 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0704Z ended at 841, so no read went elsewhere in between), parallel batches of up to 15, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 601 ids, so the 400 cap left out the 59 last six-hour posts, the 100 slowest-growing still-gaining posts and 42 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words you/and"):
    lines[k]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0704Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 99 unread referenced, reply-parent and media-source posts, most pointed-at first, then 17 second-hop posts (ids left out earlier as likely paid or sexual were not read again; 11 third-hop posts left unread for the budget); 116 returned; 2108062331095908717 came back Not Found again as an expansion error, as in 1105Z through 0704Z, and was not asked for again in the second read; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0704Z (watch.json dropped 2113697877298188733, 2113697902916751661 and 2113707043840250341 and added 2114184998651822094); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
