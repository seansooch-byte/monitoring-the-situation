s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0301Z: "Foster" (fifth; O’Shaquie Foster beat Emanuel Navarrete to unify junior lightweight titles), "Pelicans" (eighth) and "Trevon Brazile" (ninth; both the Nuggets overtime win over the Pelicans); "Ole Miss" (first) was attached in 0102Z, "Cheesecake Factory" (second) in 2300Z, "Arch Manning" (third) in 0301Z, "Lincoln Riley" (fourth) and "#HookEm" (seventh) in 0207Z; "Texas" (sixth) and "Sark" (tenth) are the same Texas v Ole Miss game and were not read for the budget'
TN='three of the top-ten US names with no posts attached in 0400Z: "Ole Miss" (first; Texas beat No. 7 Ole Miss, Arch Manning three touchdowns), "Brewers" (third; the Brewers erased a 4-0 deficit to lead the World Series 2-0) and "Lincoln Riley" (fourth; Wisconsin upset No. 16 USC); "Cheesecake Factory" (second) had a post attached in 0400Z; "Arch" (fifth), "Texas" (ninth) and "#HookEm" (tenth) are the same Texas v Ole Miss game; "Foster" (sixth), "Pelicans" (seventh) and "Trevon Brazile" (eighth) were attached in 0400Z'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Foster", "Pelicans" and "Trevon Brazile"','trend names "Ole Miss", "Brewers" and "Lincoln Riley"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0400Z.json","Build capture/2026/10/25/0501Z.json"),
("work/2026-10-25T0400Z'","work/2026-10-25T0501Z'"),
("RUN_ID = '2026-10-25T0400Z'","RUN_ID = '2026-10-25T0501Z'"),
("STARTED = '2026-10-25T04:00:00Z'","STARTED = '2026-10-25T05:01:00Z'"),
("OBS_AT = '2026-10-25T04:01:00Z'","OBS_AT = '2026-10-25T05:02:00Z'"),
("READS_BEFORE = 920","READS_BEFORE = 900"),
("datetime(2026,10,25,4,4,tzinfo=timezone.utc).timestamp()  # 0400Z (0301Z used 03:04, ","datetime(2026,10,25,5,5,tzinfo=timezone.utc).timestamp()  # 0501Z (0400Z used 04:04, 0301Z used 03:04, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_foster': 'trend_foster.txt', 'trend_pelicans': 'trend_pelicans.txt', 'trend_brazile': 'trend_brazile.txt',","'trend_olemiss': 'trend_olemiss.txt', 'trend_brewers': 'trend_brewers.txt', 'trend_riley': 'trend_riley.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_foster','trend.Foster'),('trend_pelicans','trend.Pelicans'),('trend_brazile','trend.Trevon Brazile'),","('trend_olemiss','trend.Ole Miss'),('trend_brewers','trend.Brewers'),('trend_riley','trend.Lincoln Riley'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0400Z.json') and '/25/' in _c: continue","if _c.endswith('0501Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T0301Z'","_last = '2026-10-25T0400Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("one hundred and eighteenth run","one hundred and nineteenth run"),
("one hundred and sixteenth run","one hundred and seventeenth run"),
("one hundred and fourteenth run","one hundred and fifteenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0400Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0501Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0400Z: none read)","# 5) request picks (0501Z: none read)"),
("two screening reads by id (95 unread referenced posts, most pointed-at first, then the 18 second-hop and remaining posts in the second read)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 27 second-hop and remaining posts in the second read)"),
("quote/repost words and/my + it (quoted)","quote/repost words that/just + what (quoted)"),
("(this 04Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 584 long, so the 400 cap left out the 27 last six-hour posts, the 120 slowest-growing still-gaining posts and 37 rest-of-24-hour posts, and no cited post)",
 "(this 05Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 540 long, so the 400 cap left out the 34 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Midnight run (12:00 AM ET"):
    lines[k]="            f'Overnight run (1:01 AM ET Oct 25 / 05:01 UTC Oct 25, the 05Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0400Z ended at 900, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 540 ids, so the 400 cap left out the 34 last six-hour posts and the 106 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[k]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0400Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 95"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 27 in the second read (the second-hop posts the first read led to, the 9 first-pass ids that did not fit, plus 2108062331095908717 again; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 Not Found again, as in 1105Z through 0400Z; 10 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0400Z (watch.json dropped 2113656547834487022 and added 2113723222843691122); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
