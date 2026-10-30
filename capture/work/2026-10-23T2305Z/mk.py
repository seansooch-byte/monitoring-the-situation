s=open('build_capture.py').read()
TN='four of the top-ten US names with no posts attached in 2107Z: "Caleb Wilson" (new, first) and "Tyler Herro" (new, sixth), one event (Bulls beat the Bucks, the same game as "Bulls" read in 2107Z; "Bucks", "Leonard Miller", "Giddey" and "Matas" are that game too), "Byron" (new, fifth: Byron Donalds, Florida governor candidate, calling a transgender person "sir" at a Trump rally in Fort Myers) and "Sammy Smith" (new, ninth: Sammy Smith wins the Talladega Truck Series race, the race of "Cleetus" in 2107Z); "Bulls" was read in 2107Z and "Ethan" is the h3h3 event read as "Ethan Klein" in 1808Z, so those were skipped'
R=[
("Build capture/2026/10/23/2107Z.json","Build capture/2026/10/23/2305Z.json"),
("work/2026-10-23T2107Z'","work/2026-10-23T2305Z'"),
("RUN_ID = '2026-10-23T2107Z'","RUN_ID = '2026-10-23T2305Z'"),
("STARTED = '2026-10-23T21:07:00Z'","STARTED = '2026-10-23T23:05:00Z'"),
("OBS_AT = '2026-10-23T21:07:00Z'","OBS_AT = '2026-10-23T23:05:00Z'"),
("READS_BEFORE = 579","READS_BEFORE = 541"),
("datetime(2026,10,23,21,11,tzinfo=timezone.utc).timestamp()  # 2107Z (","datetime(2026,10,23,23,7,tzinfo=timezone.utc).timestamp()  # 2305Z (2107Z used 21:11, "),
("'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_bulls': 'trend_bulls.txt', 'trend_normanpowell': 'trend_normanpowell.txt', 'trend_cleetus': 'trend_cleetus.txt', 'trend_valkoisinnocent': 'trend_valkoisinnocent.txt',","'trend_calebwilson': 'trend_calebwilson.txt', 'trend_byron': 'trend_byron.txt', 'trend_tylerherro': 'trend_tylerherro.txt', 'trend_sammysmith': 'trend_sammysmith.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_bulls','trend.Bulls'),('trend_normanpowell','trend.Norman Powell'),('trend_cleetus','trend.Cleetus'),('trend_valkoisinnocent','trend.#ValkoIsInnocent'),","('trend_calebwilson','trend.Caleb Wilson'),('trend_byron','trend.Byron'),('trend_tylerherro','trend.Tyler Herro'),('trend_sammysmith','trend.Sammy Smith'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("        if str(_x) in ('trend.#ValkoIsInnocent',): return 'gaming'  # 2107Z: Love and Deepspace character Valko",
 "        if str(_x) in ('trend.#ValkoIsInnocent',): return 'gaming'  # 2107Z: Love and Deepspace character Valko\n        if str(_x) in ('trend.Caleb Wilson','trend.Tyler Herro','trend.Sammy Smith'): return 'sports'  # 2305Z: Bulls beat Bucks; Talladega truck race\n        if str(_x) in ('trend.Byron',): return 'politics'  # 2305Z: Byron Donalds at the Fort Myers rally"),
("if _c.endswith('2107Z.json') and '/23/' in _c: continue","if _c.endswith('2305Z.json') and '/23/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T2005Z'","_last = '2026-10-23T2107Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
 'common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)'),
("eighty-eighth run","eighty-ninth run"),
("eighty-sixth run","eighty-seventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/2107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/2305Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("quote/repost words this/is + you (quoted)","quote/repost words that/just + what (quoted)"),
("two screening reads by id (100 unread first-hop, most pointed-at first, then 31 more: 8 first-hop and 23 second-hop)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 11 remaining)"),
("# 5) request picks (2107Z: none read)","# 5) request picks (2305Z: none read)"),
("(this 20Z run is a fourth hour, so the 24-hour tier was added last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and 24-hour tiers, the list was 564 long, so the 400 cap left out 164 in order (41 of 43 24-hour-tier posts, 113 slowest-growing still-gaining and the 10 last-listed six-hour posts), and no cited post)",
 "(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 517 long, so the 400 cap left out the 117 slowest-growing still-gaining posts, and no cited post)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Bulls", "Norman Powell", "Cleetus" and "#ValkoIsInnocent" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Caleb Wilson", "Byron", "Tyler Herro" and "Sammy Smith" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (5:07 PM ET"):
    lines[k]="            f'Evening run (7:05 PM ET Oct 23 / 23:05 UTC Oct 23, the 23Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2107Z ended at 558; an interrupted 2202Z attempt used 5 reads (watch and trends, 558 to 553) and wrote no capture, and 12 more reads (553 to 541) went elsewhere before this run), parallel batches of up to 14, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 517 ids, so the 400 cap left out the 117 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Bulls\""):
    lines[k]="            f'trend names \"Caleb Wilson\", \"Byron\", \"Tyler Herro\" and \"Sammy Smith\" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words and/my"):
    lines[k]="            f'quote/repost words that/just + what (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2107Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 11 remaining (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
