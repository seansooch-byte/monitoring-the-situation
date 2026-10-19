import re
s=open('build_capture.py').read()
def rep(a,b,count_ok=False):
    global s
    if s.count(a)<1: raise SystemExit('missing: '+repr(a[:140]))
    s=s.replace(a,b)
rep('"""Build capture/2026/10/17/2308Z.json','"""Build capture/2026/10/18/0004Z.json')
rep("capture/work/2026-10-17T2308Z'","capture/work/2026-10-18T0004Z'")
rep("RUN_ID = '2026-10-17T2308Z'","RUN_ID = '2026-10-18T0004Z'")
rep("STARTED = '2026-10-17T23:08:00Z'","STARTED = '2026-10-18T00:04:00Z'")
rep("OBS_AT = '2026-10-17T23:09:00Z'","OBS_AT = '2026-10-18T00:05:00Z'")
rep("READS_BEFORE = 368\nREADS_AFTER = 340","READS_BEFORE = 1000\nREADS_AFTER = 969")
rep("datetime(2026,10,17,23,12,tzinfo","datetime(2026,10,18,0,7,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt',
    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_georgia': 'trend_georgia.txt', 'trend_tennessee': 'trend_tennessee.txt', 'trend_rocco': 'trend_rocco.txt', 'trend_michigan': 'trend_michigan.txt', 'trend_gunner': 'trend_gunner.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_macron': 'trend_macron.txt', 'trend_carr': 'trend_carr.txt', 'trend_french': 'trend_french.txt', 'trend_grubb': 'trend_grubb.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("for batch in ('watch0','watch1'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep")
rep("for batch in ('watch0','watch1'):\n","for batch in ('watch0','watch1','watch2','watch3'):\n")
rep("DUE = ['politics','entertainment','sports','internet','music','gaming','offbeat']",
    "DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']")
rep("""    ('quote_just','quote'),('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_georgia','trend.Georgia'),('trend_tennessee','trend.Tennessee'),('trend_rocco','trend.Rocco Becht'),('trend_michigan','trend.Michigan'),('trend_gunner','trend.Gunner'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_is','quote'),('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_macron','trend.Macron'),('trend_carr','trend.Tommy Carr'),('trend_french','trend.The French'),('trend_grubb','trend.Grubb'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("'trend.Rocco Becht','trend.WAR DAMN EAGLE','trend.War Eagle'): return 'sports'",
    "'trend.Rocco Becht','trend.WAR DAMN EAGLE','trend.War Eagle','trend.Grubb','trend.DeBoer'): return 'sports'")
rep("('Rhyne','#WNBAfinals'),('Rocco Becht','Tennessee')]:",
    "('Rhyne','#WNBAfinals'),('Rocco Becht','Tennessee'),('Macron','The French'),('The French','Macron'),('The French','Paris'),('Grubb','DeBoer')]:")
rep("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""",
"""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}""")
rep("(23Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 2 reads;",
    "and, as 00Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
TR=('trend names Macron, "Tommy Carr", "The French", Grubb (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; '
    'the top-ten US names with no posts attached in 2308Z; Macron and The French are one event with Paris, the unrest in France; '
    'Tommy Carr is one event with Michigan and Bryce Underwood (Michigan quarterback change); Grubb is Ryan Grubb, one event with Tennessee and DeBoer (Alabama v Tennessee); '
    'Auburn, Georgia, Gunner, Tennessee, WAR DAMN EAGLE and War Eagle had posts attached in 2308Z)')
m=re.search(r"trend names Georgia, Tennessee, \"Rocco Becht\".*?not searched again\)", s)
if not m: raise SystemExit('trend block')
s=s.replace(m.group(0),TR)
rep("quote/repost words just/what/the + this; sensors culture/sports/online; desks politics/entertainment/sports/internet/music/gaming/offbeat;",
    "quote/repost words is/you/and + my; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine;")
rep("""'3 quote pages + 1 repost page, common words "just", "what", "the" and "this": ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each'""",
"""'3 quote pages + 1 repost page, common words "is", "you", "and" and "my": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-17T2201Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 2201Z, next run',[]))""",
"""        _last = '2026-10-17T2308Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 2308Z, next run',[]))""")
rep("""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2201Z, due 00:03Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2201Z, due 02:07Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2101Z, due 01:01Z)'""",
"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2308Z, due 01:08Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2201Z, due 02:01Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2101Z, due 01:01Z)'""")
rep("""f'Daytime run at 7:08 PM ET (23:08 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2201Z run ended at 368, so nothing else read in between). '""",
"""f'Evening run at 8:04 PM ET (00:04 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads; first run of the UTC day, the X day reset at 00:00 UTC): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2308Z run ended at 340 on the old day). '""")
rep("23Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 2 reads","00Z is a fourth hour, so the slow tier was included; under the 400 cap, none left out; 4 reads")
rep("(5 reads); quote/repost words just/what/the + this (3+1); '","(4 reads); quote/repost words is/you/and + my (3+1); '")
idx=s.find("f'sensors culture/sports/online; 7 desk reads:")
if idx<0: raise SystemExit('desk reason')
end=s.find("\n", idx)
s=s[:idx]+("f'sensors news/money/science; 10 desk reads: the hourly desks politics, entertainment, sports, internet "
     "and the two-hour desks world, justice, markets, ai, tech, medicine (last ok 2201Z, due 00:03Z); music, gaming, offbeat next due 01:08Z, "
     "science, ideas, life 01:01Z, defense, disaster, business 02:01Z; '")+s[end:]
rep("news/money/science sensors next rotation","culture/sports/online sensors next rotation")
rep("out_path = f'{REPO}/capture/2026/10/17/2308Z.json'","out_path = f'{REPO}/capture/2026/10/18/0004Z.json'")
open('build_capture.py','w').write(s); print('ok')
