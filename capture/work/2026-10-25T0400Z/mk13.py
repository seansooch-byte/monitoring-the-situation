s=open('build_capture.py').read()
TN='three of the top-ten US names with no posts attached in 0207Z: "Arch Manning" (first; Texas quarterback in Texas v Ole Miss, the same game as "Ole Miss", "Cam Coleman" and "#HookEm"), "Sal Frelick" (fifth) and "Wisconsin" (seventh; "Badgers" (nineteenth) is the same name); "Ole Miss" (second) and "Cam Coleman" (sixth) were attached in 0102Z, "Lincoln Riley" (third), "#HookEm" (ninth) and "#AEWCollision" (tenth) in 0207Z, "Cheesecake Factory" (fourth) in 2300Z; "Clemson" (eighth) not read for the budget'
OLD_TN_START='trend names "Lincoln Riley", "#AEWCollision" and "#HookEm" ("<name> lang:en is:retweet", newest first, 25 each; '
i=s.index(OLD_TN_START)
j=s.index('); quote/repost words just/what + the (quoted)',i)
s=s[:i]+'trend names "Arch Manning", "Sal Frelick" and "Wisconsin" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
R=[
("Build capture/2026/10/25/0207Z.json","Build capture/2026/10/25/0301Z.json"),
("work/2026-10-25T0207Z'","work/2026-10-25T0301Z'"),
("RUN_ID = '2026-10-25T0207Z'","RUN_ID = '2026-10-25T0301Z'"),
("STARTED = '2026-10-25T02:07:00Z'","STARTED = '2026-10-25T03:01:00Z'"),
("OBS_AT = '2026-10-25T02:08:00Z'","OBS_AT = '2026-10-25T03:02:00Z'"),
("READS_BEFORE = 960","READS_BEFORE = 940"),
("datetime(2026,10,25,2,10,tzinfo=timezone.utc).timestamp()  # 0207Z (0102Z used 01:05, ","datetime(2026,10,25,3,4,tzinfo=timezone.utc).timestamp()  # 0301Z (0207Z used 02:10, 0102Z used 01:05, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_riley': 'trend_riley.txt', 'trend_aew': 'trend_aew.txt', 'trend_hookem': 'trend_hookem.txt',","'trend_arch': 'trend_arch.txt', 'trend_frelick': 'trend_frelick.txt', 'trend_wisconsin': 'trend_wisconsin.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_riley','trend.Lincoln Riley'),('trend_aew','trend.#AEWCollision'),('trend_hookem','trend.#HookEm'),","('trend_arch','trend.Arch Manning'),('trend_frelick','trend.Sal Frelick'),('trend_wisconsin','trend.Wisconsin'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0207Z.json') and '/25/' in _c: continue","if _c.endswith('0301Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T0102Z'","_last = '2026-10-25T0207Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("one hundred and sixteenth run","one hundred and seventeenth run"),
("one hundred and fourteenth run","one hundred and fifteenth run"),
("one hundred and twelfth run","one hundred and thirteenth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0207Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0301Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (0207Z: none read)","# 5) request picks (0301Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 24 second-hop and remaining posts in the second read)","two screening reads by id (99 unread referenced posts, most pointed-at first, then the 29 second-hop and remaining posts in the second read)"),
("quote/repost words just/what + the (quoted)","quote/repost words this/is + you (quoted)"),
("(this 02Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 545 long, so the 400 cap left out the 21 last six-hour posts and the 124 slowest-growing still-gaining posts, and no cited post)",
 "(this 03Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 558 long, so the 400 cap left out the 42 last six-hour posts and the 116 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x) in ('trend.Lincoln Riley','trend.#AEWCollision','trend.#HookEm'): return 'sports'  # 0207Z: USC game; AEW Collision (wrestling beat); Texas v Ole Miss\n",
 "        if str(_x) in ('trend.Lincoln Riley','trend.#AEWCollision','trend.#HookEm'): return 'sports'  # 0207Z: USC game; AEW Collision (wrestling beat); Texas v Ole Miss\n        if str(_x) in ('trend.Arch Manning','trend.Sal Frelick','trend.Wisconsin'): return 'sports'  # 0301Z: Texas v Ole Miss; Sal Frelick (Brewers); Wisconsin Badgers\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Evening run (10:07 PM ET"):
    lines[k]="            f'Late-evening run (11:01 PM ET Oct 24 / 03:01 UTC Oct 25, the 03Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0207Z ended at 940, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 558 ids, so the 400 cap left out the 42 last six-hour posts and the 116 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Lincoln Riley\""):
    lines[k]="            f'trend names \"Arch Manning\", \"Sal Frelick\" and \"Wisconsin\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[k]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 0207Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 99 unread referenced, reply-parent and media-source posts, most pointed-at first, then 29 in the second read (the 9 left from the first list and the 20 second-hop posts the first read led to; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 Not Found again in both reads, as in 1105Z through 0207Z; 8 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 0207Z (watch.json added 2113720887052497277 and 2114072539366613045); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
