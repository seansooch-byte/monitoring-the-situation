s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0102Z: "Lincoln Riley" (fifth; USC fans on head coach Lincoln Riley during a USC game), "#AEWCollision" (fourth; AEW Collision on TNT and HBO Max, wrestling beat; "The Last Outfit" (eighteenth) is a name revealed on the show) and "#HookEm" (eighth; Texas v Ole Miss, the same game as "Cam Coleman" and "Ole Miss" attached in 0102Z); "Cheesecake Factory" (first) and "Scott Frost" (ninth) were attached in 2300Z, "Tennessee" (seventh) and "Big 12" (tenth) in 0003Z, "Cam Coleman" (second), "Ole Miss" (third) and "Giannis" (sixth) in 0102Z'
OLD_TN_START='trend names "Cam Coleman", "Ole Miss" and "Giannis" ("<name> lang:en is:retweet", newest first, 25 each; '
i=s.index(OLD_TN_START)
j=s.index('); quote/repost words my/it + that (quoted)',i)
s=s[:i]+'trend names "Lincoln Riley", "#AEWCollision" and "#HookEm" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
R=[
("Build capture/2026/10/25/0102Z.json","Build capture/2026/10/25/0207Z.json"),
("work/2026-10-25T0102Z'","work/2026-10-25T0207Z'"),
("RUN_ID = '2026-10-25T0102Z'","RUN_ID = '2026-10-25T0207Z'"),
("STARTED = '2026-10-25T01:02:00Z'","STARTED = '2026-10-25T02:07:00Z'"),
("OBS_AT = '2026-10-25T01:03:00Z'","OBS_AT = '2026-10-25T02:08:00Z'"),
("READS_BEFORE = 980","READS_BEFORE = 960"),
("datetime(2026,10,25,1,5,tzinfo=timezone.utc).timestamp()  # 0102Z (","datetime(2026,10,25,2,10,tzinfo=timezone.utc).timestamp()  # 0207Z (0102Z used 01:05, "),
("'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_coleman': 'trend_coleman.txt', 'trend_olemiss': 'trend_olemiss.txt', 'trend_giannis': 'trend_giannis.txt',","'trend_riley': 'trend_riley.txt', 'trend_aew': 'trend_aew.txt', 'trend_hookem': 'trend_hookem.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_coleman','trend.Cam Coleman'),('trend_olemiss','trend.Ole Miss'),('trend_giannis','trend.Giannis'),","('trend_riley','trend.Lincoln Riley'),('trend_aew','trend.#AEWCollision'),('trend_hookem','trend.#HookEm'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0102Z.json') and '/25/' in _c: continue","if _c.endswith('0207Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T0003Z'","_last = '2026-10-25T0102Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
 'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)'),
("one hundred and fifteenth run","one hundred and sixteenth run"),
("one hundred and thirteenth run","one hundred and fourteenth run"),
("one hundred and eleventh run","one hundred and twelfth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0102Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0207Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (0102Z: none read)","# 5) request picks (0207Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 38 second-hop and remaining posts in the second read)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 24 second-hop and remaining posts in the second read)"),
("quote/repost words my/it + that (quoted)","quote/repost words just/what + the (quoted)"),
("(this 01Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 557 long, so the 400 cap left out the 39 last six-hour posts and the 118 slowest-growing still-gaining posts, and no cited post)",
 "(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 545 long, so the 400 cap left out the 21 last six-hour posts and the 124 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x) in ('trend.Cam Coleman','trend.Ole Miss','trend.Giannis'): return 'sports'  # 0102Z: Texas v Ole Miss; Heat lose to Charlotte\n",
 "        if str(_x) in ('trend.Cam Coleman','trend.Ole Miss','trend.Giannis'): return 'sports'  # 0102Z: Texas v Ole Miss; Heat lose to Charlotte\n        if str(_x) in ('trend.Lincoln Riley','trend.#AEWCollision','trend.#HookEm'): return 'sports'  # 0207Z: USC game; AEW Collision (wrestling beat); Texas v Ole Miss\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (9:02 PM ET"):
    lines[k]="            f'Evening run (10:07 PM ET Oct 24 / 02:07 UTC Oct 25, the 02Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0102Z ended at 960, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 545 ids, so the 400 cap left out the 21 last six-hour posts and the 124 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Cam Coleman\""):
    lines[k]="            f'trend names \"Lincoln Riley\", \"#AEWCollision\" and \"#HookEm\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words my/it"):
    lines[k]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 0102Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 24 in the second read (the 3 left from the first list and the 21 second-hop posts the first read led to; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 Not Found again in both reads, as in 1105Z through 0102Z; 12 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0102Z (watch.json dropped 2113616429257765174); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
