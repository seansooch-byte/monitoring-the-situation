s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0804Z.json","Build capture/2026/10/21/0906Z.json"),
("work/2026-10-21T0804Z'","work/2026-10-21T0906Z'"),
("RUN_ID = '2026-10-21T0804Z'","RUN_ID = '2026-10-21T0906Z'"),
("STARTED = '2026-10-21T08:04:00Z'","STARTED = '2026-10-21T09:06:00Z'"),
("OBS_AT = '2026-10-21T08:05:00Z'","OBS_AT = '2026-10-21T09:08:00Z'"),
("READS_BEFORE = 829","READS_BEFORE = 809"),
("datetime(2026,10,21,8,7,tzinfo=timezone.utc).timestamp()  # 0804Z (0705Z used 07:08,","datetime(2026,10,21,9,10,tzinfo=timezone.utc).timestamp()  # 0906Z (0804Z used 08:07, 0705Z used 07:08,"),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_chet': 'trend_chet.txt', 'trend_dwts': 'trend_dwts.txt', 'trend_knicks': 'trend_knicks.txt',","'trend_vassago': 'trend_vassago.txt', 'trend_myanmar': 'trend_myanmar.txt', 'trend_dropfx': 'trend_dropfx.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_chet','trend.Chet'),('trend_dwts','trend.#dwts'),('trend_knicks','trend.Knicks'),","('trend_vassago','trend.Vassago'),('trend_myanmar','trend.#MyanmarCulture'),('trend_dropfx','trend.#TheDropFX'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('0804Z.json') and '/21/' in _c: continue","if _c.endswith('0906Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this 08Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 467 long, so the 400 cap left out the 67 slowest-growing fourth-hour-tier posts and no cited post)","(this 09Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 394 long, under the 400 cap, so nothing was left out)"),
('sensors culture/sports/online (one read each); trend names Chet, #dwts, Knicks (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0705Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop in one read, then 23 second-hop and leftover first-hop)',
 'sensors news/money/science (one read each); trend names Vassago, #MyanmarCulture, #TheDropFX (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0804Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (97 unread referenced first-hop in one read, then 20 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T0705Z'","_last = '2026-10-21T0804Z'"),
("but cut for the twenty-fifth run (kept","but cut for the twenty-sixth run (kept"),
("but cut for the twenty-seventh run (kept","but cut for the twenty-eighth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0804Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0906Z.json'"),
("Overnight run (4:04 AM ET Oct 21 / 08:04 UTC Oct 21, the 08Z slot; 06:00-11:00 UTC band, up to 20 reads)","Overnight run (5:06 AM ET Oct 21 / 09:06 UTC Oct 21, the 09Z slot; 06:00-11:00 UTC band, up to 20 reads)"),
("0705Z ended at 829, so nothing else read in between), parallel batches of up to 13","0804Z ended at 809, so nothing else read in between), parallel batches of up to 13"),
("this 08Z-slot run is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and fourth-hour tiers; 467 ids, so the 400 cap left out the 67 slowest-growing fourth-hour-tier posts and no cited post; 4 reads)",
 "this 09Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 394 ids, under the 400 cap, so nothing was left out; 4 reads)"),
("f'quote/repost words just/what + the (3 reads); sensors culture/sports/online (3 reads; news/money/science last read 0705Z, next in rotation); '",
 "f'quote/repost words this/is + you (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0804Z, next in rotation); '"),
("cut for the twenty-seventh run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-fifth run","cut for the twenty-eighth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-sixth run"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
("        if str(_x) == 'trend.#VisionQuest': return 'entertainment'  # 0705Z: Marvel VisionQuest series episode\n",
 "        if str(_x) == 'trend.#VisionQuest': return 'entertainment'  # 0705Z: Marvel VisionQuest series episode\n        if str(_x) in ('trend.Vassago','trend.#MyanmarCulture','trend.#TheDropFX'): return 'entertainment'  # 0906Z: Helluva Boss season 3 episode (Vassago); fan campaign over Burmese dress in the GMMTV series Scarlet Heart Thailand; the FX series The Drop\n"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Chet, #dwts, Knicks"):
    lines[i]="            f'trend names Vassago, #MyanmarCulture, #TheDropFX (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0804Z; Wemby, Spurs, Shai, Chet and Mara are one event, the Thunder and Spurs NBA game, Vassago is the Helluva Boss season 3 episode, #MyanmarCulture is a fan campaign over Burmese traditional dress in the GMMTV series Scarlet Heart Thailand, and #TheDropFX is the FX series The Drop); '"
  if l.lstrip().startswith("f'two screening reads by id: 100"):
    lines[i]="            f'two screening reads by id: 97 unread first-hop, then 20 second-hop referenced, reply-parent and media-source posts (SCREEN_MISSING of them not returned by X; 10 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
