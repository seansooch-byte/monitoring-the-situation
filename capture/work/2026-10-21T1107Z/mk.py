s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/1007Z.json","Build capture/2026/10/21/1107Z.json"),
("work/2026-10-21T1007Z'","work/2026-10-21T1107Z'"),
("RUN_ID = '2026-10-21T1007Z'","RUN_ID = '2026-10-21T1107Z'"),
("STARTED = '2026-10-21T10:07:00Z'","STARTED = '2026-10-21T11:07:00Z'"),
("OBS_AT = '2026-10-21T10:08:00Z'","OBS_AT = '2026-10-21T11:07:00Z'"),
("READS_BEFORE = 789","READS_BEFORE = 767"),
("datetime(2026,10,21,10,10,tzinfo=timezone.utc).timestamp()  # 1007Z (","datetime(2026,10,21,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (1007Z used 10:10, "),
("'quote_my': 'quote_my.txt', 'quote_that': 'quote_that.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_it': 'repost_it.txt',","'repost_the': 'repost_the.txt',"),
("'trend_wemby': 'trend_wemby.txt', 'trend_respect': 'trend_respect.txt', 'trend_helluva': 'trend_helluva.txt',","'trend_hubbard': 'trend_hubbard.txt', 'trend_lngshot': 'trend_lngshot.txt', 'trend_vassago': 'trend_vassago.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'screen0': 'screen0.txt',","'screen0': 'screen0.txt', 'screen1': 'screen1.txt',"),
("('quote_my','quote'),('quote_that','quote'),('repost_it','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_wemby','trend.Wemby'),('trend_respect','trend.#RespectMyanmar'),('trend_helluva','trend.#HelluvaBossSpoilers'),","('trend_hubbard','trend.Stephen Hubbard'),('trend_lngshot','trend.#LNGSHOT_SWISH'),('trend_vassago','trend.Vassago'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1007Z.json') and '/21/' in _c: continue","if _c.endswith('1107Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this 10Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 372 long, under the 400 cap, so nothing was left out)","(this 11Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 383 long, under the 400 cap, so nothing was left out)"),
('sensors culture/sports/online (one read each); trend names Wemby, #RespectMyanmar, #HelluvaBossSpoilers (each "<name> lang:en is:retweet", newest first, 25 each; three of the current top-ten US names with no posts attached in 0906Z); quote/repost words my/that + it ("and" was refused by X as an ambiguous keyword and replaced by "that"); hourly desks politics/entertainment/sports/internet; one screening read by id (96 unread referenced first-hop; second hop not read for the budget)',
 'sensors news/money/science (one read each); trend names Stephen Hubbard, #LNGSHOT_SWISH, Vassago (each "<name> lang:en is:retweet", newest first, 25 each, the multi-word name in quotes; three of the current top-ten US names with no posts attached in 1007Z); quote/repost words just/what + the; hourly desks politics/entertainment/sports/internet; two screening reads by id (88 unread referenced first-hop, then 18 second-hop)'),
('references followed one hop from every post read (second hop not read for the budget)','references followed two hops from every post read'),
("'2 quote pages + 1 repost page (budget), common words \"my\", \"that\" and \"it\": (my lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each; (and lang:en is:quote -is:retweet) was refused by X (400 Invalid Request: ambiguous use of and as a keyword) and replaced by that'",
 "'2 quote pages + 1 repost page (budget), common words \"just\", \"what\" and \"the\": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-21T0906Z'","_last = '2026-10-21T1007Z'"),
("but cut for the twenty-seventh run (kept","but cut for the twenty-eighth run (kept"),
("but cut for the twenty-ninth run (kept","but cut for the thirtieth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1007Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/1107Z.json'"),
("Overnight run (6:07 AM ET Oct 21 / 10:07 UTC Oct 21, the 10Z slot; 06:00-11:00 UTC band, up to 20 reads)","Overnight run (7:07 AM ET Oct 21 / 11:07 UTC Oct 21, the 11Z slot; 06:00-11:00 UTC band, up to 20 reads)"),
("0906Z ended at 789, so nothing else read in between), parallel batches of up to 13","1007Z ended at 769, so 2 reads went elsewhere in between), parallel batches of up to 13"),
("this 10Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 372 ids, under the 400 cap, so nothing was left out; 4 reads)",
 "this 11Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 383 ids, under the 400 cap, so nothing was left out; 4 reads)"),
("f'quote/repost words my/that + it (4 reads: \"and\" was refused by X with 400 Invalid Request, ambiguous use of and as a keyword, and the read was replaced by \"that\"); sensors culture/sports/online (3 reads; news/money/science last read 0906Z, next in rotation); '",
 "f'quote/repost words just/what + the (3 reads); sensors news/money/science (3 reads; culture/sports/online last read 1007Z, next in rotation); '"),
("cut for the twenty-ninth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-seventh run","cut for the thirtieth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the twenty-eighth run"),
("Not read: news/money/science sensors, worldwide trends,","Not read: culture/sports/online sensors, worldwide trends,"),
("        if str(_x) in ('trend.#RespectMyanmar','trend.#HelluvaBossSpoilers'): return 'entertainment'  # 1007Z",
 "        if str(_x) == 'trend.Stephen Hubbard': return 'world'  # 1107Z: Russia frees US citizen Stephen Hubbard (Steve Witkoff escorting him home)\n        if str(_x) == 'trend.#LNGSHOT_SWISH': return 'music'  # 1107Z: LNGSHOT Masterpiece music video release\n        if str(_x) in ('trend.#RespectMyanmar','trend.#HelluvaBossSpoilers'): return 'entertainment'  # 1007Z"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
hit=0
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Wemby, #RespectMyanmar, #HelluvaBossSpoilers"):
    lines[i]="            f'trend names Stephen Hubbard, #LNGSHOT_SWISH, Vassago (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each, \"Stephen Hubbard\" in quotes; three of the top-ten US names with no posts attached in 1007Z; Stephen Hubbard and Steve Witkoff are one event, Russia releasing the US citizen Stephen Hubbard, #LNGSHOT_SWISH, #LNGSHOT_MASTERPIECE and #롱샷_너라는_명작 are the LNGSHOT Masterpiece music video, and Vassago is the Helluva Boss season 3 episode; Good Wednesday and Happy Hump are greetings and were not read); '"; hit+=1
  if l.lstrip().startswith("f'one screening read by id: 96"):
    lines[i]="            f'two screening reads by id: 88 unread first-hop referenced, reply-parent and media-source posts (all 88 returned; 3 referenced posts inside them Not Found: 2112510160208113825, 2108062331095908717 again and 2112698835151798628), then 18 unread second-hop posts (all 18 returned); story clusters (search_news) not read for the budget. '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
