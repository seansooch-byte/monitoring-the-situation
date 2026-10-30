s=open('build_capture.py').read()
BAND="kept to about 20 reads, the 06:00-11:00 UTC overnight band limit"
R=[
("Build capture/2026/10/21/0559Z.json","Build capture/2026/10/21/0705Z.json"),
("work/2026-10-21T0559Z'","work/2026-10-21T0705Z'"),
("RUN_ID = '2026-10-21T0559Z'","RUN_ID = '2026-10-21T0705Z'"),
("STARTED = '2026-10-21T05:59:00Z'","STARTED = '2026-10-21T07:05:00Z'"),
("OBS_AT = '2026-10-21T06:00:00Z'","OBS_AT = '2026-10-21T07:06:00Z'"),
("READS_BEFORE = 873","READS_BEFORE = 849"),
("datetime(2026,10,21,6,2,tzinfo=timezone.utc).timestamp()  # 0559Z (0507Z used 05:10,","datetime(2026,10,21,7,8,tzinfo=timezone.utc).timestamp()  # 0705Z (0559Z used 06:02, 0507Z used 05:10,"),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_eagle4': 'trend_eagle4.txt', 'trend_dwts': 'trend_dwts.txt', 'trend_wemby': 'trend_wemby.txt',","'trend_visionquest': 'trend_visionquest.txt', 'trend_sixers': 'trend_sixers.txt', 'trend_spurs': 'trend_spurs.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt', 'screen3': 'screen3.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_eagle4','trend.EAGLE-4'),('trend_dwts','trend.#dwts'),('trend_wemby','trend.Wemby'),","('trend_visionquest','trend.#VisionQuest'),('trend_sixers','trend.Sixers'),('trend_spurs','trend.Spurs'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) == 'trend.#dwts': return 'entertainment'  # 0559Z: Dancing with the Stars\n","        if str(_x) == 'trend.#dwts': return 'entertainment'  # 0559Z: Dancing with the Stars\n        if str(_x) == 'trend.#VisionQuest': return 'entertainment'  # 0705Z: Marvel VisionQuest series episode\n"),
("if _c.endswith('0559Z.json') and '/21/' in _c: continue","if _c.endswith('0705Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this run, started 05:59Z for the 06Z slot, is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 380 long, under the 400 cap, so nothing was left out)","(this 07Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 363 long, under the 400 cap, so nothing was left out)"),
('sensors culture/sports/online (one read each); trend names EAGLE-4, #dwts, Wemby (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0507Z); quote/repost words is/you + "and"; hourly desks politics/entertainment/sports/internet; four screening reads by id (107 unread referenced first-hop in two reads, then 22 second-hop, then 2 posts re-read for their media)',
 'sensors news/money/science (one read each); trend names #VisionQuest, Sixers, Spurs (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0559Z); quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id (96 unread referenced first-hop in one read, then 14 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"is\", \"you\" and \"and\": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (\"and\" lang:en is:retweet; and unquoted was refused as an ambiguous keyword, one read spent), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"my\", \"it\" and \"that\": (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T0507Z'","_last = '2026-10-21T0559Z'"),
("four-hour desk due since 07:08Z (last ok 2026-10-20T0308Z) but cut for the twenty-third run","four-hour desk due since 07:08Z on 2026-10-20 (last ok 2026-10-20T0308Z) but cut for the twenty-fourth run"),
("but cut for the twenty-fifth run (kept","but cut for the twenty-sixth run (kept"),
("kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42",BAND),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0559Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0705Z.json'"),
("Late-night run (1:59 AM ET Oct 21 / 05:59 UTC Oct 21, firing early for the 06Z slot; 12:00-05:00 UTC band, up to 42 reads, "+BAND+")","Overnight run (3:05 AM ET Oct 21 / 07:05 UTC Oct 21, the 07Z slot; 06:00-11:00 UTC band, up to 20 reads)"),
("0507Z ended at 873, so no read went elsewhere in between; one of them was the refused unquoted \"and\" repost query), parallel batches of up to 9","0559Z ended at 850, so one read went elsewhere in between), parallel batches of up to 13"),
("this run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 380 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); ",
 "this 07Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 363 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("f'quote/repost words is/you + \"and\" (4 reads, one refused: X rejected the unquoted query \"and lang:en is:retweet\" as an ambiguous use of and as a keyword, so it was rerun quoted); sensors culture/sports/online (3 reads; news/money/science last read 0507Z, next in rotation); '",
 "f'quote/repost words my/it + that (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0559Z, next in rotation); '"),
("cut for the twenty-fifth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the twenty-third run","cut for the twenty-sixth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-fourth run"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names EAGLE-4, #dwts, Wemby"):
    lines[i]="            f'trend names #VisionQuest, Sixers, Spurs (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0559Z; Wemby, Spurs, Shai, Chet, Mara, #ThunderUp and Jared McCain are one event, the Thunder and Spurs NBA game, and Sixers, Knicks, Maxey, Embiid, LeBron and 76ers are one event, the 76ers NBA opener); '"
  if l.lstrip().startswith("f'four screening reads by id: 107"):
    lines[i]="            f'two screening reads by id: 96 unread first-hop and 14 second-hop referenced, reply-parent and media-source posts (3 of them not returned by X; 8 third-hop left unread for the budget); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
