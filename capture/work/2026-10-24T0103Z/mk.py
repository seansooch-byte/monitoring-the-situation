s=open('build_capture.py').read()
TN='four of the top-ten US names with no posts attached in 2305Z: "#WorldSeries" (third: World Series, Brewers v Rays), "Luka Garza" (fourth) and "Mason Williams" (ninth), and "Bulls" (second; last read 2107Z, and with "Bucks", "Leonard Miller" and "Caleb Wilson" one event, the Bulls v Bucks game); "Leonard Miller" is that game too, "Ethan" is the h3h3 event read as "Ethan Klein" in 1808Z and "End of 1" is a game-score phrase, so those were skipped'
R=[
("Build capture/2026/10/23/2305Z.json","Build capture/2026/10/24/0000Z.json"),
("work/2026-10-23T2305Z'","work/2026-10-24T0000Z'"),
("RUN_ID = '2026-10-23T2305Z'","RUN_ID = '2026-10-24T0000Z'"),
("STARTED = '2026-10-23T23:05:00Z'","STARTED = '2026-10-24T00:00:00Z'"),
("OBS_AT = '2026-10-23T23:05:00Z'","OBS_AT = '2026-10-24T00:00:00Z'"),
("READS_BEFORE = 541","READS_BEFORE = 1000"),
("datetime(2026,10,23,23,7,tzinfo=timezone.utc).timestamp()  # 2305Z (","datetime(2026,10,24,0,1,tzinfo=timezone.utc).timestamp()  # 0000Z (2305Z used 23:07, "),
("'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',","'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',"),
("'repost_what': 'repost_what.txt',","'repost_is': 'repost_is.txt',"),
("'trend_calebwilson': 'trend_calebwilson.txt', 'trend_byron': 'trend_byron.txt', 'trend_tylerherro': 'trend_tylerherro.txt', 'trend_sammysmith': 'trend_sammysmith.txt',","'trend_worldseries': 'trend_worldseries.txt', 'trend_lukagarza': 'trend_lukagarza.txt', 'trend_masonwilliams': 'trend_masonwilliams.txt', 'trend_bulls': 'trend_bulls.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),","('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),"),
("('trend_calebwilson','trend.Caleb Wilson'),('trend_byron','trend.Byron'),('trend_tylerherro','trend.Tyler Herro'),('trend_sammysmith','trend.Sammy Smith'),","('trend_worldseries','trend.#WorldSeries'),('trend_lukagarza','trend.Luka Garza'),('trend_masonwilliams','trend.Mason Williams'),('trend_bulls','trend.Bulls'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) in ('trend.Byron',): return 'politics'  # 2305Z: Byron Donalds at the Fort Myers rally",
 "        if str(_x) in ('trend.Byron',): return 'politics'  # 2305Z: Byron Donalds at the Fort Myers rally\n        if str(_x) in ('trend.Luka Garza','trend.Mason Williams','trend.Bulls'): return 'sports'  # 0000Z: NBA (Luka Garza; Mason Williams; Bulls v Bucks)"),
("if _c.endswith('2305Z.json') and '/23/' in _c: continue","if _c.endswith('0000Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T2107Z'","_last = '2026-10-23T2305Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
 'common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)'),
("eighty-ninth run","ninetieth run"),
("eighty-seventh run","eighty-eighth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/2305Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0000Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (2305Z: none read)","# 5) request picks (0000Z: none read)"),
("(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 517 long, so the 400 cap left out the 117 slowest-growing still-gaining posts, and no cited post)",
 "(this 00Z run is a fourth hour, so the 24-hour tier was added last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and 24-hour tiers, the list was 566 long, so the 400 cap left out 166 in order (42 of 44 24-hour-tier posts, the 116 slowest-growing still-gaining posts and the 8 last-listed six-hour posts), and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Caleb Wilson", "Byron", "Tyler Herro" and "Sammy Smith" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "#WorldSeries", "Luka Garza", "Mason Williams" and "Bulls" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (7:05 PM ET"):
    lines[k]="            f'Evening run (8:00 PM ET Oct 23 / 00:00 UTC Oct 24, the 00Z slot, first run of the new X day; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the daily count reset at 00:00 UTC; 2305Z ended the 2026-10-23 day at 520), parallel batches of up to 14, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and 24-hour tiers; 566 ids, so the 400 cap left out 166 (42 24-hour-tier, 116 slowest-growing still-gaining and 8 last-listed six-hour posts) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Caleb Wilson\""):
    lines[k]="            f'trend names \"#WorldSeries\", \"Luka Garza\", \"Mason Williams\" and \"Bulls\" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words that/just"):
    lines[k]="            f'quote/repost words the/this + is (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2305Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 92 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 19 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
