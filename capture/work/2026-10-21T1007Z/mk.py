s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0906Z.json","Build capture/2026/10/21/1007Z.json"),
("work/2026-10-21T0906Z'","work/2026-10-21T1007Z'"),
("RUN_ID = '2026-10-21T0906Z'","RUN_ID = '2026-10-21T1007Z'"),
("STARTED = '2026-10-21T09:06:00Z'","STARTED = '2026-10-21T10:07:00Z'"),
("OBS_AT = '2026-10-21T09:08:00Z'","OBS_AT = '2026-10-21T10:08:00Z'"),
("READS_BEFORE = 809","READS_BEFORE = 789"),
("datetime(2026,10,21,9,10,tzinfo=timezone.utc).timestamp()  # 0906Z (0804Z used 08:07,","datetime(2026,10,21,10,10,tzinfo=timezone.utc).timestamp()  # 1007Z (0906Z used 09:10, 0804Z used 08:07,"),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_my': 'quote_my.txt', 'quote_that': 'quote_that.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_vassago': 'trend_vassago.txt', 'trend_myanmar': 'trend_myanmar.txt', 'trend_dropfx': 'trend_dropfx.txt',","'trend_wemby': 'trend_wemby.txt', 'trend_respect': 'trend_respect.txt', 'trend_helluva': 'trend_helluva.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt',","'screen0': 'screen0.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_my','quote'),('quote_that','quote'),('repost_it','repost'),"),
("('trend_vassago','trend.Vassago'),('trend_myanmar','trend.#MyanmarCulture'),('trend_dropfx','trend.#TheDropFX'),","('trend_wemby','trend.Wemby'),('trend_respect','trend.#RespectMyanmar'),('trend_helluva','trend.#HelluvaBossSpoilers'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('0906Z.json') and '/21/' in _c: continue","if _c.endswith('1007Z.json') and '/21/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("(this 09Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 394 long, under the 400 cap, so nothing was left out)","(this 10Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 372 long, under the 400 cap, so nothing was left out)"),
('sensors news/money/science (one read each); trend names Vassago, #MyanmarCulture, #TheDropFX (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0804Z); quote/repost words this/is + you; hourly desks politics/entertainment/sports/internet; two screening reads by id (97 unread referenced first-hop in one read, then 20 second-hop)',
 'sensors culture/sports/online (one read each); trend names Wemby, #RespectMyanmar, #HelluvaBossSpoilers (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0906Z); quote/repost words my/that + it ("and" was refused by X as an ambiguous keyword and replaced by "that"); hourly desks politics/entertainment/sports/internet; one screening read by id (96 unread referenced first-hop; second hop not read for the budget)'),
("'2 quote pages + 1 repost page (budget), common words \"this\", \"is\" and \"you\": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"my\", \"that\" and \"it\": (my lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each; (and lang:en is:quote -is:retweet) was refused by X (400 Invalid Request: ambiguous use of and as a keyword) and replaced by that'"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-21T0804Z'","_last = '2026-10-21T0906Z'"),
("but cut for the twenty-sixth run (kept","but cut for the twenty-seventh run (kept"),
("but cut for the twenty-eighth run (kept","but cut for the twenty-ninth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0906Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1007Z.json'"),
("Overnight run (5:06 AM ET Oct 21 / 09:06 UTC Oct 21, the 09Z slot; 06:00-11:00 UTC band, up to 20 reads)","Overnight run (6:07 AM ET Oct 21 / 10:07 UTC Oct 21, the 10Z slot; 06:00-11:00 UTC band, up to 20 reads)"),
("0804Z ended at 809, so nothing else read in between), parallel batches of up to 13","0906Z ended at 789, so nothing else read in between), parallel batches of up to 13"),
("this 09Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 394 ids, under the 400 cap, so nothing was left out; 4 reads)",
 "this 10Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 372 ids, under the 400 cap, so nothing was left out; 4 reads)"),
("f'quote/repost words this/is + you (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 0804Z, next in rotation); '",
 "f'quote/repost words my/that + it (4 reads: \"and\" was refused by X with 400 Invalid Request, ambiguous use of and as a keyword, and the read was replaced by \"that\"); sensors culture/sports/online (3 reads; news/money/science last read 0906Z, next in rotation); '"),
("cut for the twenty-eighth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-sixth run","cut for the twenty-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-seventh run"),
("Not read: culture/sports/online sensors, worldwide trends,","Not read: news/money/science sensors, worldwide trends,"),
("        if str(_x) in ('trend.Vassago','trend.#MyanmarCulture','trend.#TheDropFX'): return 'entertainment'",
 "        if str(_x) in ('trend.#RespectMyanmar','trend.#HelluvaBossSpoilers'): return 'entertainment'  # 1007Z: fan campaign over Burmese dress in Scarlet Heart Thailand; Helluva Boss season 3 spoilers\n        if str(_x) == 'trend.Wemby': return 'sports'  # 1007Z: Thunder and Spurs NBA game\n        if str(_x) in ('trend.Vassago','trend.#MyanmarCulture','trend.#TheDropFX'): return 'entertainment'"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Vassago, #MyanmarCulture, #TheDropFX"):
    lines[i]="            f'trend names Wemby, #RespectMyanmar, #HelluvaBossSpoilers (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the top-ten US names with no posts attached in 0906Z; Wemby, Spurs, Shai and Chet are one event, the Thunder and Spurs NBA game, #RespectMyanmar and #ScarletHeartTH are the fan campaign over Burmese traditional dress in the GMMTV series Scarlet Heart Thailand, and #HelluvaBossSpoilers and Vassago are the Helluva Boss season 3 episode); '"
  if l.lstrip().startswith("f'two screening reads by id: 97"):
    lines[i]="            f'one screening read by id: 96 unread first-hop referenced, reply-parent and media-source posts (all 96 returned; 2 referenced posts inside them Not Found, 2108062331095908717 again and 2112698835151798628; second hop left unread for the budget, the refused \"and\" read used its place); story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
