s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 2300Z: "Tennessee" (second; South Carolina beat No. 11 Tennessee on a field goal with no time left; "South Carolina" (third), "Heupel" (ninth) and "David Smith" are the same game), "Big 12" (fifth; UCF beat No. 2 BYU in double overtime and Cincinnati beat Texas Tech; "2 BYU" (sixth) and "#BYUvsUCF" (eighth) are the same game as "Scott Frost" (first, attached in 2300Z)) and "Dan Lanning" (tenth; Oregon lost to Illinois); "Iowa" (fourth) and "Cheesecake Factory" (seventh) were attached in 2300Z'
i=s.index('trend names "Iowa", "Cheesecake Factory" and "Scott Frost" ("<name> lang:en is:retweet", newest first, 25 each; ')
j=s.index('); quote/repost words what/the + this (quoted)',i)
s=s[:i]+'trend names "Tennessee", "Big 12" and "Dan Lanning" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
R=[
("Build capture/2026/10/24/2300Z.json","Build capture/2026/10/25/0003Z.json"),
("work/2026-10-24T2300Z'","work/2026-10-25T0003Z'"),
("RUN_ID = '2026-10-24T2300Z'","RUN_ID = '2026-10-25T0003Z'"),
("STARTED = '2026-10-24T23:00:00Z'","STARTED = '2026-10-25T00:03:00Z'"),
("OBS_AT = '2026-10-24T23:01:00Z'","OBS_AT = '2026-10-25T00:04:00Z'"),
("READS_BEFORE = 530","READS_BEFORE = 1000"),
("datetime(2026,10,24,23,2,tzinfo=timezone.utc).timestamp()  # 2300Z (","datetime(2026,10,25,0,6,tzinfo=timezone.utc).timestamp()  # 0003Z (2300Z used 23:02, "),
("'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',","'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',"),
("'repost_this': 'repost_this.txt',","'repost_and': 'repost_and.txt',"),
("'trend_iowa': 'trend_iowa.txt', 'trend_cheesecake': 'trend_cheesecake.txt', 'trend_frost': 'trend_frost.txt',","'trend_tennessee': 'trend_tennessee.txt', 'trend_big12': 'trend_big12.txt', 'trend_lanning': 'trend_lanning.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),","('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),"),
("('trend_iowa','trend.Iowa'),('trend_cheesecake','trend.Cheesecake Factory'),('trend_frost','trend.Scott Frost'),","('trend_tennessee','trend.Tennessee'),('trend_big12','trend.Big 12'),('trend_lanning','trend.Dan Lanning'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('2300Z.json') and '/24/' in _c: continue","if _c.endswith('0003Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T2159Z'","_last = '2026-10-24T2300Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)',
 'common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)'),
("one hundred and thirteenth run","one hundred and fourteenth run"),
("one hundred and eleventh run","one hundred and twelfth run"),
("one hundred and ninth run","one hundred and tenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/2300Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0003Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (2300Z: none read)","# 5) request picks (0003Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 37 second-hop and remaining posts in the second read)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 20 second-hop and remaining posts in the second read)"),
("quote/repost words what/the + this (quoted)","quote/repost words is/you + and (quoted)"),
("(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 565 long, so the 400 cap left out the 30 last six-hour posts and the 135 slowest-growing still-gaining posts, and no cited post)",
 "(this 00Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 602 long, so the 400 cap left out the 40 last six-hour posts, the 133 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post)"),
("        if str(_x)=='trend.Cheesecake Factory': return 'politics'  # 2300Z: Obama remark on Trump's White House\n",
 "        if str(_x)=='trend.Cheesecake Factory': return 'politics'  # 2300Z: Obama remark on Trump's White House\n        if str(_x) in ('trend.Tennessee','trend.Big 12','trend.Dan Lanning'): return 'sports'  # 0003Z: South Carolina v Tennessee, UCF v BYU and the Big 12, Oregon after losing to Illinois\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (7:00 PM ET"):
    lines[k]="            f'Evening run (8:03 PM ET Oct 24 / 00:03 UTC Oct 25, the 00Z slot and the first run of the new UTC day; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the X day reset at 00:00 UTC, and 2300Z ended the old day at 510), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 602 ids, so the 400 cap left out the 40 last six-hour posts, the 133 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Iowa\""):
    lines[k]="            f'trend names \"Tennessee\", \"Big 12\" and \"Dan Lanning\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words what/the"):
    lines[k]="            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2300Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 20 in the second read (the 1 left from the first list, 2108062331095908717, and the 19 second-hop posts the first read led to; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again in the second read, as in 1105Z through 2300Z; 8 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 2300Z (watch.json dropped 2113498434431025427, read here in screening, and gained 2113990281322221932, read in watch); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
