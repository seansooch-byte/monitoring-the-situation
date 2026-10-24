s=open('build_capture.py').read()
TN='four of the top-ten US names with no posts attached in 0000Z: "#SmackDown" (first; WWE SmackDown, and "Giulia" (third) and "Blake Monroe" (seventh) are SmackDown wrestlers, one event), "Pacers" (fifth; with "Nesmith" (sixth) one event, the Pacers game), "BANGTAN" (eighth; BTS) and "Yelich" (ninth; Christian Yelich, the World Series, Brewers v Rays); "Giulia", "Blake Monroe" and "Nesmith" were therefore skipped'
R=[
("Build capture/2026/10/24/0000Z.json","Build capture/2026/10/24/0103Z.json"),
("work/2026-10-24T0000Z'","work/2026-10-24T0103Z'"),
("RUN_ID = '2026-10-24T0000Z'","RUN_ID = '2026-10-24T0103Z'"),
("STARTED = '2026-10-24T00:00:00Z'","STARTED = '2026-10-24T01:03:00Z'"),
("OBS_AT = '2026-10-24T00:00:00Z'","OBS_AT = '2026-10-24T01:03:00Z'"),
("READS_BEFORE = 1000","READS_BEFORE = 979"),
("datetime(2026,10,24,0,1,tzinfo=timezone.utc).timestamp()  # 0000Z (","datetime(2026,10,24,1,5,tzinfo=timezone.utc).timestamp()  # 0103Z (0000Z used 00:01, "),
("'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',","'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',"),
("'repost_is': 'repost_is.txt',","'repost_my': 'repost_my.txt',"),
("'trend_worldseries': 'trend_worldseries.txt', 'trend_lukagarza': 'trend_lukagarza.txt', 'trend_masonwilliams': 'trend_masonwilliams.txt', 'trend_bulls': 'trend_bulls.txt',","'trend_smackdown': 'trend_smackdown.txt', 'trend_pacers': 'trend_pacers.txt', 'trend_bangtan': 'trend_bangtan.txt', 'trend_yelich': 'trend_yelich.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),","('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),"),
("('trend_worldseries','trend.#WorldSeries'),('trend_lukagarza','trend.Luka Garza'),('trend_masonwilliams','trend.Mason Williams'),('trend_bulls','trend.Bulls'),","('trend_smackdown','trend.#SmackDown'),('trend_pacers','trend.Pacers'),('trend_bangtan','trend.BANGTAN'),('trend_yelich','trend.Yelich'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) in ('trend.Luka Garza','trend.Mason Williams','trend.Bulls'): return 'sports'  # 0000Z: NBA (Luka Garza; Mason Williams; Bulls v Bucks)",
 "        if str(_x) in ('trend.Luka Garza','trend.Mason Williams','trend.Bulls'): return 'sports'  # 0000Z: NBA (Luka Garza; Mason Williams; Bulls v Bucks)\n        if str(_x) in ('trend.#SmackDown','trend.Pacers','trend.Yelich'): return 'sports'  # 0103Z: WWE SmackDown; Pacers game; Yelich (World Series)\n        if str(_x) in ('trend.BANGTAN',): return 'entertainment'  # 0103Z: BTS"),
("if _c.endswith('0000Z.json') and '/24/' in _c: continue","if _c.endswith('0103Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T2305Z'","_last = '2026-10-24T0000Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
 'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)'),
("quote/repost words that/just + what (quoted)","quote/repost words you/and + my (quoted)"),
("ninetieth run","ninety-first run"),
("eighty-eighth run","eighty-ninth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0000Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0103Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0000Z: none read)","# 5) request picks (0103Z: none read)"),
("(this 00Z run is a fourth hour, so the 24-hour tier was added last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and 24-hour tiers, the list was 566 long, so the 400 cap left out 166 in order (42 of 44 24-hour-tier posts, the 116 slowest-growing still-gaining posts and the 8 last-listed six-hour posts), and no cited post)",
 "(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 518 long, so the 400 cap left out the 118 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "#WorldSeries", "Luka Garza", "Mason Williams" and "Bulls" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "#SmackDown", "Pacers", "BANGTAN" and "Yelich" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (8:00 PM ET"):
    lines[k]="            f'Evening run (9:03 PM ET Oct 23 / 01:03 UTC Oct 24, the 01Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 7, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 518 ids, so the 400 cap left out the 118 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#WorldSeries\""):
    lines[k]="            f'trend names \"#SmackDown\", \"Pacers\", \"BANGTAN\" and \"Yelich\" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words the/this"):
    lines[k]="            f'quote/repost words you/and + my (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0000Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 92"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 27 left: 4 more first-hop posts and the second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
