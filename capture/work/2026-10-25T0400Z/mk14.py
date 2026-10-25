s=open('build_capture.py').read()
OLDTN='three of the top-ten US names with no posts attached in 0207Z: "Arch Manning" (first; Texas quarterback in Texas v Ole Miss, the same game as "Ole Miss", "Cam Coleman" and "#HookEm"), "Sal Frelick" (fifth) and "Wisconsin" (seventh; "Badgers" (nineteenth) is the same name); "Ole Miss" (second) and "Cam Coleman" (sixth) were attached in 0102Z, "Lincoln Riley" (third), "#HookEm" (ninth) and "#AEWCollision" (tenth) in 0207Z, "Cheesecake Factory" (fourth) in 2300Z; "Clemson" (eighth) not read for the budget'
TN='three of the top-ten US names with no posts attached in 0301Z: "Foster" (fifth; O’Shaquie Foster beat Emanuel Navarrete to unify junior lightweight titles), "Pelicans" (eighth) and "Trevon Brazile" (ninth; both the Nuggets overtime win over the Pelicans); "Ole Miss" (first) was attached in 0102Z, "Cheesecake Factory" (second) in 2300Z, "Arch Manning" (third) in 0301Z, "Lincoln Riley" (fourth) and "#HookEm" (seventh) in 0207Z; "Texas" (sixth) and "Sark" (tenth) are the same Texas v Ole Miss game and were not read for the budget'
assert s.count(OLDTN)>=1
s=s.replace('trend names "Arch Manning", "Sal Frelick" and "Wisconsin"','trend names "Foster", "Pelicans" and "Trevon Brazile"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/0301Z.json","Build capture/2026/10/25/0400Z.json"),
("work/2026-10-25T0301Z'","work/2026-10-25T0400Z'"),
("RUN_ID = '2026-10-25T0301Z'","RUN_ID = '2026-10-25T0400Z'"),
("STARTED = '2026-10-25T03:01:00Z'","STARTED = '2026-10-25T04:00:00Z'"),
("OBS_AT = '2026-10-25T03:02:00Z'","OBS_AT = '2026-10-25T04:01:00Z'"),
("READS_BEFORE = 940","READS_BEFORE = 920"),
("datetime(2026,10,25,3,4,tzinfo=timezone.utc).timestamp()  # 0301Z (0207Z used 02:10, ","datetime(2026,10,25,4,4,tzinfo=timezone.utc).timestamp()  # 0400Z (0301Z used 03:04, 0207Z used 02:10, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_arch': 'trend_arch.txt', 'trend_frelick': 'trend_frelick.txt', 'trend_wisconsin': 'trend_wisconsin.txt',","'trend_foster': 'trend_foster.txt', 'trend_pelicans': 'trend_pelicans.txt', 'trend_brazile': 'trend_brazile.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_arch','trend.Arch Manning'),('trend_frelick','trend.Sal Frelick'),('trend_wisconsin','trend.Wisconsin'),","('trend_foster','trend.Foster'),('trend_pelicans','trend.Pelicans'),('trend_brazile','trend.Trevon Brazile'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0301Z.json') and '/25/' in _c: continue","if _c.endswith('0400Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T0207Z'","_last = '2026-10-25T0301Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("one hundred and seventeenth run","one hundred and eighteenth run"),
("one hundred and fifteenth run","one hundred and sixteenth run"),
("one hundred and thirteenth run","one hundred and fourteenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0301Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0400Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0301Z: none read)","# 5) request picks (0400Z: none read)"),
("two screening reads by id (99 unread referenced posts, most pointed-at first, then the 29 second-hop and remaining posts in the second read)","two screening reads by id (95 unread referenced posts, most pointed-at first, then the 18 second-hop and remaining posts in the second read)"),
("quote/repost words this/is + you (quoted)","quote/repost words and/my + it (quoted)"),
("(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 558 long, so the 400 cap left out the 42 last six-hour posts and the 116 slowest-growing still-gaining posts, and no cited post)",
 "(this 04Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 584 long, so the 400 cap left out the 27 last six-hour posts, the 120 slowest-growing still-gaining posts and 37 rest-of-24-hour posts, and no cited post)"),
("        if str(_x) in ('trend.Arch Manning','trend.Sal Frelick','trend.Wisconsin'): return 'sports'  # 0301Z: Texas v Ole Miss; Sal Frelick (Brewers); Wisconsin Badgers\n",
 "        if str(_x) in ('trend.Arch Manning','trend.Sal Frelick','trend.Wisconsin'): return 'sports'  # 0301Z: Texas v Ole Miss; Sal Frelick (Brewers); Wisconsin Badgers\n        if str(_x) in ('trend.Foster','trend.Pelicans','trend.Trevon Brazile'): return 'sports'  # 0400Z: Foster v Navarrete boxing; Nuggets v Pelicans\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Late-evening run (11:01 PM ET"):
    lines[k]="            f'Midnight run (12:00 AM ET Oct 25 / 04:00 UTC Oct 25, the 04Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0301Z ended at 920, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 584 ids, so the 400 cap left out the 27 last six-hour posts, the 120 slowest-growing still-gaining posts and 37 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[k]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0301Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 99"):
    lines[k]="            f'two screening reads by id: 95 unread referenced, reply-parent and media-source posts, most pointed-at first, then 18 in the second read (the second-hop posts the first read led to, plus 2108062331095908717 again; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 Not Found again in both reads, as in 1105Z through 0301Z; 8 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0301Z (watch.json added 2113829143792189536); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
