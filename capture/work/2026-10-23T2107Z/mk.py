s=open('build_capture.py').read()
TN='four of the top-ten US names with no posts attached in 2005Z: "Bulls" (new, first) and "Norman Powell" (new, fifth), one event (Bucks at Bulls tonight; Powell plays for the Bulls), "Cleetus" (new, eighth: Cleetus McFarland and Tony Stewart in the Talladega truck race Stage 1 crash) and "#ValkoIsInnocent" (new, ninth: Love and Deepspace fans on the character Valko); "Ethan" is the h3h3 event read as "Ethan Klein" in 1808Z, "Lassie" and "1 Pro" were read in 1905Z, "Oregon State" is the Jesse Legree event and "Skye" were read in 2005Z, and "#MGSMC2AlienwareSweepstakes" is a giveaway, so those were skipped'
R=[
("Build capture/2026/10/23/2005Z.json","Build capture/2026/10/23/2107Z.json"),
("work/2026-10-23T2005Z'","work/2026-10-23T2107Z'"),
("RUN_ID = '2026-10-23T2005Z'","RUN_ID = '2026-10-23T2107Z'"),
("STARTED = '2026-10-23T20:05:00Z'","STARTED = '2026-10-23T21:07:00Z'"),
("OBS_AT = '2026-10-23T20:05:00Z'","OBS_AT = '2026-10-23T21:07:00Z'"),
("READS_BEFORE = 598","READS_BEFORE = 579"),
("datetime(2026,10,23,20,8,tzinfo=timezone.utc).timestamp()  # 2005Z (","datetime(2026,10,23,21,11,tzinfo=timezone.utc).timestamp()  # 2107Z (2005Z used 20:08, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_skye': 'trend_skye.txt', 'trend_jesselegree': 'trend_jesselegree.txt',","'trend_bulls': 'trend_bulls.txt', 'trend_normanpowell': 'trend_normanpowell.txt', 'trend_cleetus': 'trend_cleetus.txt', 'trend_valkoisinnocent': 'trend_valkoisinnocent.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_skye','trend.Skye'),('trend_jesselegree','trend.Jesse Legree'),","('trend_bulls','trend.Bulls'),('trend_normanpowell','trend.Norman Powell'),('trend_cleetus','trend.Cleetus'),('trend_valkoisinnocent','trend.#ValkoIsInnocent'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) in ('trend.Skye','trend.Jesse Legree'): return 'sports'  # 2005Z: Skye Blakely world all-around title; Oregon State WR Jesse Legree re-signs",
 "        if str(_x) in ('trend.Skye','trend.Jesse Legree'): return 'sports'  # 2005Z: Skye Blakely world all-around title; Oregon State WR Jesse Legree re-signs\n        if str(_x) in ('trend.Bulls','trend.Norman Powell','trend.Cleetus'): return 'sports'  # 2107Z: Bucks at Bulls; Talladega truck race crash\n        if str(_x) in ('trend.#ValkoIsInnocent',): return 'gaming'  # 2107Z: Love and Deepspace character Valko"),
("if _c.endswith('2005Z.json') and '/23/' in _c: continue","if _c.endswith('2107Z.json') and '/23/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-23T1905Z'","_last = '2026-10-23T2005Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("eighty-seventh run","eighty-eighth run"),
("eighty-fifth run","eighty-sixth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/2005Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/2107Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("two screening reads by id (100 unread first-hop, most pointed-at first, then 19 second-hop)","two screening reads by id (100 unread first-hop, most pointed-at first, then 31 more: 8 first-hop and 23 second-hop)"),
("# 5) request picks (2005Z: none read)","# 5) request picks (2107Z: none read)"),
("skip_nsfw |= {'2045592694072737958'}  # 2005Z:","skip_nsfw |= {'2099079137981800577','2113310763850862881','2113707163105308852','2113520320590365107','2113281707709186138','2113362436371702059','2113464244377473190','2113458457844101316'}  # 2107Z: sexual posts that use the word bulls (six: Seductive/BBC accounts), a like-and-RT giveaway (Haddzy mystery bonuses) and a crypto pump reply, all from the Bulls trend stream\nskip_nsfw |= {'2045592694072737958'}  # 2005Z:"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
i=s.find('trend names "Skye" and "Jesse Legree" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find('so those were skipped',i)+len('so those were skipped')
print('VIRAL SEG',i,j)
s=s[:i]+'trend names "Bulls", "Norman Powell", "Cleetus" and "#ValkoIsInnocent" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Afternoon run (4:05 PM ET"):
    lines[k]="            f'Evening run (5:07 PM ET Oct 23 / 21:07 UTC Oct 23, the 21Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2005Z ended at 579, so no reads went elsewhere in between), parallel batches of up to 14, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 526 ids, so the 400 cap left out 126 in order (the 119 slowest-growing still-gaining and the 7 last-listed six-hour posts) and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Skye\""):
    lines[k]="            f'trend names \"Bulls\", \"Norman Powell\", \"Cleetus\" and \"#ValkoIsInnocent\" (4 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[k]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2005Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 31 more (the 8 remaining first-hop and 23 second-hop posts; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 returned Not Found again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
