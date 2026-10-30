s=open('build_capture.py').read()
TN='four of the top-ten US names with no posts attached in 0103Z: "Tatum" (second; Jayson Tatum, with "#Celtics" (eighteenth) the Celtics game), "#TheLastDriveIn" (fourth; Joe Bob Briggs horror show), "Michin" (eighth) and "Mikal" (ninth; Mikal Bridges, with "Josh Hart" (fifteenth) the Knicks game); "#SmackDown" (first), "Pacers" (sixth), "Giulia" (seventh) and "Nesmith" (tenth) were read or are one event with names read in 0103Z, and "#WorldSeries" (third) and "Mason Williams" (fifth) were read in 0000Z, so those were skipped'
R=[
("Build capture/2026/10/24/0103Z.json","Build capture/2026/10/24/0200Z.json"),
("work/2026-10-24T0103Z'","work/2026-10-24T0200Z'"),
("RUN_ID = '2026-10-24T0103Z'","RUN_ID = '2026-10-24T0200Z'"),
("STARTED = '2026-10-24T01:03:00Z'","STARTED = '2026-10-24T02:00:00Z'"),
("OBS_AT = '2026-10-24T01:03:00Z'","OBS_AT = '2026-10-24T02:00:00Z'"),
("READS_BEFORE = 979","READS_BEFORE = 958"),
("datetime(2026,10,24,1,5,tzinfo=timezone.utc).timestamp()  # 0103Z (","datetime(2026,10,24,2,1,tzinfo=timezone.utc).timestamp()  # 0200Z (0103Z used 01:05, "),
("'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_my': 'repost_my.txt',","'repost_just': 'repost_just.txt',"),
("'trend_smackdown': 'trend_smackdown.txt', 'trend_pacers': 'trend_pacers.txt', 'trend_bangtan': 'trend_bangtan.txt', 'trend_yelich': 'trend_yelich.txt',","'trend_tatum': 'trend_tatum.txt', 'trend_thelastdrivein': 'trend_thelastdrivein.txt', 'trend_michin': 'trend_michin.txt', 'trend_mikal': 'trend_mikal.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_smackdown','trend.#SmackDown'),('trend_pacers','trend.Pacers'),('trend_bangtan','trend.BANGTAN'),('trend_yelich','trend.Yelich'),","('trend_tatum','trend.Tatum'),('trend_thelastdrivein','trend.#TheLastDriveIn'),('trend_michin','trend.Michin'),('trend_mikal','trend.Mikal'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) in ('trend.BANGTAN',): return 'entertainment'  # 0103Z: BTS",
 "        if str(_x) in ('trend.BANGTAN',): return 'entertainment'  # 0103Z: BTS\n        if str(_x) in ('trend.Tatum','trend.Mikal'): return 'sports'  # 0200Z: Celtics game (Jayson Tatum); Knicks game (Mikal Bridges)\n        if str(_x) in ('trend.#TheLastDriveIn',): return 'entertainment'  # 0200Z: Joe Bob Briggs horror show"),
("if _c.endswith('0103Z.json') and '/24/' in _c: continue","if _c.endswith('0200Z.json') and '/24/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-24T0000Z'","_last = '2026-10-24T0103Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)',
 'common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)'),
("quote/repost words you/and + my (quoted)","quote/repost words it/that + just (quoted)"),
("ninety-first run","ninety-second run"),
("eighty-ninth run","ninetieth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0103Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/0200Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0103Z: none read)","# 5) request picks (0200Z: none read)"),
("(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 518 long, so the 400 cap left out the 118 slowest-growing still-gaining posts, and no cited post)",
 "(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 514 long, so the 400 cap left out the 114 slowest-growing still-gaining posts, and no cited post)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 11 remaining)","two screening reads by id (95 unread referenced posts, most pointed-at first, then the 23 second-hop posts they led to)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "#SmackDown", "Pacers", "BANGTAN" and "Yelich" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
j2=s.find('were therefore skipped',i)
print('VIRAL SEG',i,j,j2)
if j < len('so those were skipped')+5 or (j2!=-1 and j2<j): j=j2+len('were therefore skipped')
s=s[:i]+'trend names "Tatum", "#TheLastDriveIn", "Michin" and "Mikal" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (9:03 PM ET"):
    lines[k]="            f'Evening run (10:00 PM ET Oct 23 / 02:00 UTC Oct 24, the 02Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today), parallel batches of up to 14, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 514 ids, so the 400 cap left out the 114 slowest-growing still-gaining posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"#SmackDown\""):
    lines[k]="            f'trend names \"Tatum\", \"#TheLastDriveIn\", \"Michin\" and \"Mikal\" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words you/and"):
    lines[k]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0103Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 95 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 23 second-hop posts they led to (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
