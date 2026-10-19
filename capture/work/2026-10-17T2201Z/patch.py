s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)>=1, ('missing',a[:90])
    s=s.replace(a,b)
rep('"""Build capture/2026/10/17/2101Z.json','"""Build capture/2026/10/17/2200Z.json')
rep("capture/work/2026-10-17T2101Z'","capture/work/2026-10-17T2200Z'")
rep("RUN_ID = '2026-10-17T2101Z'","RUN_ID = '2026-10-17T2200Z'")
rep("STARTED = '2026-10-17T21:01:00Z'","STARTED = '2026-10-17T22:01:00Z'")
rep("OBS_AT = '2026-10-17T21:02:00Z'","OBS_AT = '2026-10-17T22:02:00Z'")
rep("READS_BEFORE = 427\nREADS_AFTER = 400","READS_BEFORE = 400\nREADS_AFTER = 368")
rep("datetime(2026,10,17,21,8,tzinfo","datetime(2026,10,17,22,6,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_macron': 'trend_macron.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt',
    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_auburn': 'trend_auburn.txt', 'trend_underwood': 'trend_underwood.txt', 'trend_rhyne': 'trend_rhyne.txt', 'trend_carr': 'trend_carr.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("DUE = ['politics','entertainment','sports','internet','music','gaming','offbeat','science','ideas','life']",
    "DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','defense','disaster','business']")
rep("""    ('quote_the','quote'),('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_macron','trend.Macron'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_and','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_auburn','trend.Auburn'),('trend_underwood','trend.Bryce Underwood'),('trend_rhyne','trend.Rhyne'),('trend_carr','trend.Tommy Carr'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) in ('trend.Arch','trend.Marsh'): return 'sports'",
    "        if str(_x) in ('trend.Arch','trend.Marsh'): return 'sports'\n        if str(_x) in ('trend.Auburn','trend.Gunner','trend.Bryce Underwood','trend.Tommy Carr','trend.Michigan','trend.Rhyne','trend.#WNBAfinals','trend.Gabby Williams'): return 'sports'")
rep("('Arch Manning','Arch'),('Nick Marsh','Marsh')]:","('Arch Manning','Arch'),('Nick Marsh','Marsh'),('Auburn','Gunner'),('Bryce Underwood','Tommy Carr'),('Tommy Carr','Bryce Underwood'),('Bryce Underwood','Michigan'),('Tommy Carr','Michigan'),('Rhyne','#WNBAfinals')]:")
rep("for batch in ('watch0','watch1','watch2'):  # noqa keep","for batch in ('watch0','watch1'):  # noqa keep")
rep("for batch in ('watch0','watch1','watch2'):\n","for batch in ('watch0','watch1'):\n")
rep("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""","""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}""")
rep("(21Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "(22Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 2 reads;")
TR='trend names Auburn, "Bryce Underwood", Rhyne, "Tommy Carr" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the top-ten US names with no posts attached in 2101Z that are new events; Auburn is the Auburn v Georgia college football game, one event with Gunner (Gunner Stockton) at US 14; Bryce Underwood and Tommy Carr are one event, Michigan benching Bryce Underwood for Tommy Carr against Penn State, with Michigan at US 13, both searched before the overlap was seen; Rhyne is Rhyne Howard in the WNBA Finals, one event with #WNBAfinals and Gabby Williams; Arch, Sark, Indiana, Ohio State and Sayin are the Texas v Florida and Ohio State v Indiana games, searched in 1706Z to 2003Z, not searched again; Macron had posts attached in 2101Z)'
OLD1='trend name Macron ("Macron lang:en is:retweet", newest first, 25; Macron was the only top-ten US name with no posts attached in 2003Z that is a separate event: it is the protests and unrest in France (Paris, Lyon), one event with Paris and The French at US 14 and 18; "Arch" and "Marsh" are new spellings of Arch Manning (Texas v Florida) and Nick Marsh (Michigan State football), which had posts attached in 2003Z, so they were not searched; the other top-ten names had posts attached in 2003Z)'
assert s.count(OLD1)==2, s.count(OLD1)
s=s.replace(OLD1,TR)
rep("quote/repost words the/this/is + you; sensors culture/sports/online; desks politics/entertainment/sports/internet/music/gaming/offbeat/science/ideas/life;",
    "quote/repost words and/my/it + that; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine/defense/disaster/business;")
rep("""'3 quote pages + 1 repost page, common words "the", "this", "is" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'""",
"""'3 quote pages + 1 repost page, common words "and", "my", "it" and "that": ("and" lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-17T2003Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 2003Z, next run',[]))""",
"""        _last = '2026-10-17T2101Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 2101Z, next run',[]))""")
rep("""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2003Z, due 22:03Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1807Z, due 22:07Z)'""",
"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2101Z, due 23:01Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2101Z, due 01:01Z)'""")
rep("""f'Daytime run at 5:01 PM ET (21:01 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2003Z run ended at 427, so nothing else read in between). '""",
"""f'Daytime run at 6:01 PM ET (22:01 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2101Z run ended at 400, so nothing else read in between). '""")
rep("21Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 3 reads","22Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 2 reads")
rep("(1 read); quote/repost words the/this/is + you (3+1); '","(4 reads); quote/repost words and/my/it + that (3+1); '")
rep("""f'sensors culture/sports/online; 10 desk reads: the hourly desks politics, entertainment, sports, internet, the two-hour desks music, gaming, offbeat (last ok 1906Z, cut by the desk cap in 2003Z) and the four-hour desks science, ideas, life (last ok 1706Z, due 21:06Z, swept a few minutes early to keep the cadence); world, justice, markets, ai, tech, medicine next due 22:03Z, defense, disaster, business 22:07Z; '""",
"""f'sensors news/money/science; 13 desk reads: the hourly desks politics, entertainment, sports, internet, the two-hour desks world, justice, markets, ai, tech, medicine (last ok 2003Z, due 22:03Z) and the four-hour desks defense, disaster, business (last ok 1807Z, due 22:07Z, swept a few minutes early to keep the cadence; the desk cap was raised to 13 inside the 42-read run budget, as in 1807Z); music, gaming, offbeat next due 23:01Z; '""")
rep("news/money/science sensors next rotation","culture/sports/online sensors next rotation")
rep("out_path = f'{REPO}/capture/2026/10/17/2101Z.json'","out_path = f'{REPO}/capture/2026/10/17/2200Z.json'")
open('build_capture.py','w').write(s)
print('ok')
