s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0003Z: "Cam Coleman" (first) and "Ole Miss" (second) are one event (No. 19 Texas v No. 7 Ole Miss: Texas led 24-3 in the second quarter, Coleman dropped a deep Arch Manning ball; "#HookEm" (eleventh) is the same game), and "Giannis" (fourth; Giannis Antetokounmpo fouled out as the Heat lost to Charlotte and fell to 0-3; "Hornets" and "Heat" are the same game); "Cheesecake Factory" (third), "Scott Frost" (sixth) and "Iowa" (tenth) were attached in 2300Z, "Tennessee" (fifth), "South Carolina" (eighth, same game) and "Big 12" (ninth) in 0003Z; "#AEWCollision" (seventh) not read for the budget'
i=s.index('trend names "Tennessee", "Big 12" and "Dan Lanning" ("<name> lang:en is:retweet", newest first, 25 each; ')
j=s.index('); quote/repost words is/you + and (quoted)',i)
s=s[:i]+'trend names "Cam Coleman", "Ole Miss" and "Giannis" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
R=[
("Build capture/2026/10/25/0003Z.json","Build capture/2026/10/25/0102Z.json"),
("work/2026-10-25T0003Z'","work/2026-10-25T0102Z'"),
("RUN_ID = '2026-10-25T0003Z'","RUN_ID = '2026-10-25T0102Z'"),
("STARTED = '2026-10-25T00:03:00Z'","STARTED = '2026-10-25T01:02:00Z'"),
("OBS_AT = '2026-10-25T00:04:00Z'","OBS_AT = '2026-10-25T01:03:00Z'"),
("READS_BEFORE = 1000","READS_BEFORE = 980"),
("datetime(2026,10,25,0,6,tzinfo=timezone.utc).timestamp()  # 0003Z (","datetime(2026,10,25,1,5,tzinfo=timezone.utc).timestamp()  # 0102Z (0003Z used 00:06, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_tennessee': 'trend_tennessee.txt', 'trend_big12': 'trend_big12.txt', 'trend_lanning': 'trend_lanning.txt',","'trend_coleman': 'trend_coleman.txt', 'trend_olemiss': 'trend_olemiss.txt', 'trend_giannis': 'trend_giannis.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_tennessee','trend.Tennessee'),('trend_big12','trend.Big 12'),('trend_lanning','trend.Dan Lanning'),","('trend_coleman','trend.Cam Coleman'),('trend_olemiss','trend.Ole Miss'),('trend_giannis','trend.Giannis'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0003Z.json') and '/25/' in _c: continue","if _c.endswith('0102Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T2300Z'","_last = '2026-10-25T0003Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet)',
 'common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)'),
("one hundred and fourteenth run","one hundred and fifteenth run"),
("one hundred and twelfth run","one hundred and thirteenth run"),
("one hundred and tenth run","one hundred and eleventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0003Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0102Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0003Z: none read)","# 5) request picks (0102Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 20 second-hop and remaining posts in the second read)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 38 second-hop and remaining posts in the second read)"),
("quote/repost words is/you + and (quoted)","quote/repost words my/it + that (quoted)"),
("(this 00Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 602 long, so the 400 cap left out the 40 last six-hour posts, the 133 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post)",
 "(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 557 long, so the 400 cap left out the 39 last six-hour posts and the 118 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x) in ('trend.Tennessee','trend.Big 12','trend.Dan Lanning'): return 'sports'  # 0003Z: South Carolina v Tennessee, UCF v BYU and the Big 12, Oregon after losing to Illinois\n",
 "        if str(_x) in ('trend.Tennessee','trend.Big 12','trend.Dan Lanning'): return 'sports'  # 0003Z: South Carolina v Tennessee, UCF v BYU and the Big 12, Oregon after losing to Illinois\n        if str(_x) in ('trend.Cam Coleman','trend.Ole Miss','trend.Giannis'): return 'sports'  # 0102Z: Texas v Ole Miss; Heat lose to Charlotte\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (8:03 PM ET"):
    lines[k]="            f'Evening run (9:02 PM ET Oct 24 / 01:02 UTC Oct 25, the 01Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0003Z ended at 980, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 557 ids, so the 400 cap left out the 39 last six-hour posts and the 118 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Tennessee\""):
    lines[k]="            f'trend names \"Cam Coleman\", \"Ole Miss\" and \"Giannis\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words is/you"):
    lines[k]="            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0003Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 38 in the second read (the 20 left from the first list and the 18 second-hop posts the first read led to; ids left out earlier as likely paid or sexual were not read again; 2114132975323382087 and 2113945791022928033 Not Found and 1681178487967588352 Authorization Error in the second read, 2108062331095908717 Not Found again as a reference, as in 1105Z through 0003Z; 11 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0003Z (watch.json gained 2113667772211421244 and 2113762242327892456, both read in watch); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
