s=open('build_capture.py').read()
R=[
("Build capture/2026/10/21/0006Z.json","Build capture/2026/10/21/0059Z.json"),
("work/2026-10-21T0006Z'","work/2026-10-21T0059Z'"),
("RUN_ID = '2026-10-21T0006Z'","RUN_ID = '2026-10-21T0059Z'"),
("STARTED = '2026-10-21T00:06:00Z'","STARTED = '2026-10-21T00:59:00Z'"),
("OBS_AT = '2026-10-21T00:07:00Z'","OBS_AT = '2026-10-21T01:00:00Z'"),
("READS_BEFORE = 1000","READS_BEFORE = 978"),
("datetime(2026,10,21,0,9,tzinfo=timezone.utc).timestamp()  # 0006Z (2258Z","datetime(2026,10,21,1,3,tzinfo=timezone.utc).timestamp()  # 0059Z (0006Z used 00:09, 2258Z"),
("'quote_you': 'quote_you.txt', 'quote_my': 'quote_my.txt',","'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',"),
("'repost_it': 'repost_it.txt',","'repost_what': 'repost_what.txt',"),
("'trend_embiid': 'trend_embiid.txt', 'trend_eagle4': 'trend_eagle4.txt', 'trend_drummond': 'trend_drummond.txt',","'trend_dwts': 'trend_dwts.txt', 'trend_ezra': 'trend_ezra.txt', 'trend_knicks': 'trend_knicks.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',","'trends_us': 'trends_us.txt',"),
("trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')","trends = parse_trends(raw['trends_us'], 'US')"),
("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))","sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-21T0006Z',[]))"),
("('quote_you','quote'),('quote_my','quote'),('repost_it','repost'),","('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),"),
("('trend_embiid','trend.Embiid'),('trend_eagle4','trend.EAGLE-4'),('trend_drummond','trend.Drummond'),","('trend_dwts','trend.#dwts'),('trend_ezra','trend.Ezra'),('trend_knicks','trend.Knicks'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("        if str(_x) == 'trend.EAGLE-4': return 'ai'  # 0006Z: EAGLE-4 speculative-decoding release (LLM inference speed)\n","        if str(_x) == 'trend.EAGLE-4': return 'ai'  # 0006Z: EAGLE-4 speculative-decoding release (LLM inference speed)\n        if str(_x) in ('trend.#dwts','trend.Ezra','trend.Tatyana','trend.Amber','trend.Maura'): return 'entertainment'  # 0059Z: Dancing with the Stars episode (Ezra Frech, Tatyana, Amber, Maura are contestants)\n"),
("if _c.endswith('0006Z.json') and '/21/' in _c: continue","if _c.endswith('0059Z.json') and '/21/' in _c: continue"),
("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}"),
("(this 00Z-slot run is a fourth hour, so the rest of the last 24 hours was added, fastest growing first; with every pulse- and story-cited post placed right after the watch.json ids the list was 484 long, so the 400 cap left out the 84 slowest-growing posts (the fourth-hour tier), and no cited post)","(this 01Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 398 long, under the 400 cap, so nothing was left out)"),
('sensors culture/sports/online (one read each); trend names Embiid, "EAGLE-4", Drummond (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space or a hyphen; three of the six current top-ten US names with no posts attached in 2258Z); quote/repost words you/my + it; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (121 first-hop in two reads, then 25 second-hop)',
 'sensors news/money/science (one read each); trend names #dwts, Ezra, Knicks (each "<name> lang:en is:retweet", newest first, 25 each; three of the six current top-ten US names with no posts attached in 0006Z); quote/repost words that/just + what; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (118 first-hop in two reads, then 22 second-hop)'),
("'2 quote pages + 1 repost page (budget), common words \"you\", \"my\" and \"it\": (you lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each'",
 "'2 quote pages + 1 repost page (budget), common words \"that\", \"just\" and \"what\": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'"),
("rotation: culture/sports/online read this run;","rotation: news/money/science read this run;"),
("_last = '2026-10-20T2258Z'","_last = '2026-10-21T0006Z'"),
("cut for the seventeenth run (kept","cut for the eighteenth run (kept"),
("but cut for the nineteenth run (kept","but cut for the twentieth run (kept"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0006Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/21/0059Z.json'"),
("Evening run (8:06 PM ET Oct 20 / 00:06 UTC Oct 21, the 00Z slot and the first run of the new UTC day;","Evening run (8:59 PM ET Oct 20 / 00:59 UTC Oct 21, an early fire of the 01Z slot;"),
("the X day reset at 00:00 UTC, so no read went elsewhere in between), parallel batches of up to 13","0006Z ended at 978, so no read went elsewhere in between), parallel batches of up to 13"),
("this 00Z-slot run is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the fourth-hour tier fastest growing first; 484 ids, so the 400 cap left out the 84 slowest-growing posts (all of the fourth-hour tier) and no cited post; 4 reads); trends US+WW (2 reads); ",
 "this 01Z-slot run is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 398 ids, under the 400 cap, so nothing was left out; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0006Z); "),
("sensors culture/sports/online (3 reads; news/money/science last read 2258Z, next in rotation)","sensors news/money/science (3 reads; culture/sports/online last read 0006Z, next in rotation)"),
("quote/repost words you/my + it (3 reads)","quote/repost words that/just + what (3 reads)"),
("the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the nineteenth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the seventeenth run","the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the twentieth run and the four-hour desks (last ok 2026-10-20T0308Z, due 07:08Z) cut for the eighteenth run"),
("Not read: news/money/science sensors,","Not read: culture/sports/online sensors, worldwide trends,"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n')
for i,l in enumerate(lines):
  if l.lstrip().startswith("f'trend names Embiid, \"EAGLE-4\""):
    lines[i]="            f'trend names #dwts, Ezra, Knicks (3 reads; each \"<name> lang:en is:retweet\", newest first, 25 each; three of the six top-ten US names with no posts attached in 0006Z; #dwts, Ezra, Tatyana and Amber are one event, the Dancing with the Stars episode, so #dwts and Ezra stand for it and Tatyana and Amber were not read; Knicks is the Knicks home opener and banner night, and Maxey is one event with the 76ers opener read in 0006Z); '"
  if l.lstrip().startswith("f'three screening reads by id: 121"):
    lines[i]="            f'three screening reads by id: 118 unread first-hop (two reads) and 22 second-hop referenced, reply-parent and media-source posts; story clusters (search_news) not read for the budget. '"
s='\n'.join(lines)
open('build_capture.py','w').write(s)
