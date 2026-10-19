import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    s=s.replace(a,b)
rep('"""Build capture/2026/10/17/1906Z.json','"""Build capture/2026/10/17/2101Z.json')
rep("capture/work/2026-10-17T2003Z'","capture/work/2026-10-17T2101Z'")
rep("RUN_ID = '2026-10-17T2003Z'","RUN_ID = '2026-10-17T2101Z'")
rep("STARTED = '2026-10-17T20:03:00Z'","STARTED = '2026-10-17T21:01:00Z'")
rep("OBS_AT = '2026-10-17T20:05:00Z'","OBS_AT = '2026-10-17T21:02:00Z'")
rep("READS_BEFORE = 458\nREADS_AFTER = 427","READS_BEFORE = 427\nREADS_AFTER = 400")
rep("datetime(2026,10,17,20,10,tzinfo","datetime(2026,10,17,21,8,tzinfo")
rep("""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_indiana': 'trend_indiana.txt', 'trend_nickmarsh': 'trend_nickmarsh.txt', 'trend_texas': 'trend_texas.txt', 'trend_hoover': 'trend_hoover.txt', 'trend_fahey': 'trend_fahey.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_macron': 'trend_macron.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']",
    "DUE = ['politics','entertainment','sports','internet','music','gaming','offbeat','science','ideas','life']")
rep("""    ('quote_and','quote'),('quote_my','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_indiana','trend.Indiana'),('trend_nickmarsh','trend.Nick Marsh'),('trend_texas','trend.Texas'),('trend_hoover','trend.Hoover'),('trend_fahey','trend.Fahey'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_macron','trend.Macron'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("('Nick Marsh','Michigan State'),('Fahey','NHL')]:","('Nick Marsh','Michigan State'),('Fahey','NHL'),('Macron','Paris'),('Macron','The French'),('Arch Manning','Arch'),('Nick Marsh','Marsh')]:")
rep("if str(_x)=='trend.Macron': return 'world'","if str(_x) in ('trend.Macron','trend.Paris','trend.The French'): return 'world'\n        if str(_x) in ('trend.Arch','trend.Marsh'): return 'sports'")
rep("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}""","""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""")
rep("(20Z is a fourth hour, so the rest of the last 24 hours, slowest growing last, is included)","(21Z is not a fourth hour, so no slow tier)")
TR_OLD='trend names Indiana, "Nick Marsh", Texas, Hoover, Fahey (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the five top-ten US names with no posts attached in 1906Z; Indiana and Hoover belong to the Ohio State v Indiana college football game, one event with Sayin, Jeremiah Smith, Ohio State, Ryan Day and #GoBucks; Texas belongs to the Texas v Florida game, one event with Arch Manning, Gators and #HookEm; Nick Marsh is Michigan State football; Fahey is NHL/hockey)'
TR_NEW='trend name Macron ("Macron lang:en is:retweet", newest first, 25; Macron was the only top-ten US name with no posts attached in 2003Z that is a separate event: it is the France 17 October protests and riots, one event with Paris and The French at US 14 and 18; "Arch" and "Marsh" are new spellings of Arch Manning (Texas v Florida) and Nick Marsh (Michigan State football), which had posts attached in 2003Z, so they were not searched; the other top-ten names had posts attached in 2003Z)'
assert s.count(TR_OLD)==2
s=s.replace(TR_OLD,TR_NEW)
rep("quote/repost words and/my/just + what; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine;",
    "quote/repost words the/this/is + you; sensors culture/sports/online; desks politics/entertainment/sports/internet/music/gaming/offbeat/science/ideas/life;")
rep("""'3 quote pages + 1 repost page, common words "and", "my", "just" and "what": ("and" lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""",
"""'3 quote pages + 1 repost page, common words "the", "this", "is" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-17T1906Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 1906Z, next run',[]))""",
"""        _last = '2026-10-17T2003Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 2003Z, next run',[]))""")
rep("""        if d in ('music','gaming','offbeat'):
            reason = 'due but cut by the 10-read desk cap (two-hour desk, last ok 2026-10-17T1906Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1706Z, due 21:06Z)'""",
"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2003Z, due 22:03Z)'""")
rep("""f'Daytime run at 4:03 PM ET (20:03 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1906Z run ended at 458, so nothing else read in between). '""",
"""f'Daytime run at 5:01 PM ET (21:01 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2003Z run ended at 427, so nothing else read in between). '""")
rep("20Z is a fourth hour, so the rest of the last 24 hours is included; under the 400 cap","21Z is not a fourth hour, so no slow tier; under the 400 cap")
rep("(5 reads); quote/repost words and/my/just + what (3+1); '","(1 read); quote/repost words the/this/is + you (3+1); '")
rep("""f'sensors news/money/science; 10 desk reads: the hourly desks politics, entertainment, sports, internet and the two-hour desks world, justice, markets, ai, tech, medicine (last ok 1807Z, due 20:07Z); music, gaming, offbeat were due since 1906Z but cut by the 10-read desk cap; '""",
"""f'sensors culture/sports/online; 10 desk reads: the hourly desks politics, entertainment, sports, internet, the two-hour desks music, gaming, offbeat (last ok 1906Z, cut by the desk cap in 2003Z) and the four-hour desks science, ideas, life (last ok 1706Z, due 21:06Z, swept 5 minutes early to keep the cadence); world, justice, markets, ai, tech, medicine next due 22:03Z, defense, disaster, business 22:07Z; '""")
rep("culture/sports/online sensors next rotation","news/money/science sensors next rotation")
rep("out_path = f'{REPO}/capture/2026/10/17/2003Z.json'","out_path = f'{REPO}/capture/2026/10/17/2101Z.json'")
open('build_capture.py','w').write(s)
print('ok')
