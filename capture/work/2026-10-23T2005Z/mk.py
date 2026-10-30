s=open('build_capture.py').read()
TN='two of the top-ten-plus US names with no posts attached in 1905Z: "Skye" (new, fifth) and "Jesse Legree" (new, twelfth; read as the only other new name); "Ethan" and "Hila" are one h3h3 event with "Ethan Klein" (read in 1808Z), "Mercer", "Devils", "Hellebuyck" and "Winnipeg" are the Jets-Devils Hellebuyck trade (read in 1602Z and 1659Z), "Dan Sullivan" was read in 1808Z, "Lassie" and "1 Pro" were read in 1905Z, and "#MGSMC2AlienwareSweepstakes" is a giveaway, so those were skipped'
R=[
("Build capture/2026/10/23/1905Z.json","Build capture/2026/10/23/2005Z.json"),
("work/2026-10-23T1905Z'","work/2026-10-23T2005Z'"),
("RUN_ID = '2026-10-23T1905Z'","RUN_ID = '2026-10-23T2005Z'"),
("STARTED = '2026-10-23T19:05:00Z'","STARTED = '2026-10-23T20:05:00Z'"),
("OBS_AT = '2026-10-23T19:05:00Z'","OBS_AT = '2026-10-23T20:05:00Z'"),
("READS_BEFORE = 617","READS_BEFORE = 598"),
("datetime(2026,10,23,19,7,tzinfo=timezone.utc).timestamp()  # 1905Z (","datetime(2026,10,23,20,8,tzinfo=timezone.utc).timestamp()  # 2005Z (1905Z used 19:07, "),
("'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_1pro': 'trend_1pro.txt', 'trend_lassie': 'trend_lassie.txt',","'trend_skye': 'trend_skye.txt', 'trend_jesselegree': 'trend_jesselegree.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_my','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_1pro','trend.1 Pro'),('trend_lassie','trend.Lassie'),","('trend_skye','trend.Skye'),('trend_jesselegree','trend.Jesse Legree'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1905Z.json') and '/23/' in _c: continue","if _c.endswith('2005Z.json') and '/23/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T1808Z'","_last = '2026-10-23T1905Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "my", "what" and "the", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("eighty-sixth run","eighty-seventh run"),
("eighty-fourth run","eighty-fifth run"),
("(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 526 long, so the 400 cap left out 126 (120 slowest-growing still-gaining and the 6 last-listed six-hour posts), the slowest-growing still-gaining posts in order, and no cited post)",
 "(this 20Z run is a fourth hour, so the 24-hour tier was added last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and 24-hour tiers, the list was 564 long, so the 400 cap left out 164 in order (41 of 43 24-hour-tier posts, 113 slowest-growing still-gaining and the 10 last-listed six-hour posts), and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1905Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/2005Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("quote/repost words is/you + and (quoted)","quote/repost words this/is + you (quoted)"),
("two screening reads by id (100 unread first-hop, most pointed-at first, then 6 more)","two screening reads by id (100 unread first-hop, most pointed-at first, then 19 second-hop)"),
("# 5) request picks (1905Z: none read)","# 5) request picks (2005Z: none read)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "1 Pro" and "Lassie" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('TV collie)',i)+len('TV collie')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Skye" and "Jesse Legree" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Afternoon run (3:05 PM ET"):
    lines[k]="            f'Afternoon run (4:05 PM ET Oct 23 / 20:05 UTC Oct 23, the 20Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1905Z ended at 598, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and 24-hour tiers; 564 ids, so the 400 cap left out 164 in order (41 of the 43 24-hour-tier posts, the 113 slowest-growing still-gaining and the 10 last-listed six-hour posts) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"1 Pro\""):
    lines[k]="            f'trend names \"Skye\" and \"Jesse Legree\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/what"):
    lines[k]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1905Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 98"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 19 second-hop posts they pointed at (ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 returned Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request: r-2026-10-23-02 was answered in 1659Z and 1808Z"):
    hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
