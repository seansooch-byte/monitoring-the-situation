import re
s=open('build_capture.py').read()
def rep(a,b):
    global s
    if s.count(a)<1: raise SystemExit('missing: '+repr(a[:140]))
    s=s.replace(a,b)
rep('"""Build capture/2026/10/18/0004Z.json','"""Build capture/2026/10/18/0059Z.json')
rep("capture/work/2026-10-18T0004Z'","capture/work/2026-10-18T0059Z'")
rep("RUN_ID = '2026-10-18T0004Z'","RUN_ID = '2026-10-18T0059Z'")
rep("STARTED = '2026-10-18T00:04:00Z'","STARTED = '2026-10-18T00:59:00Z'")
rep("OBS_AT = '2026-10-18T00:05:00Z'","OBS_AT = '2026-10-18T01:00:00Z'")
rep("READS_BEFORE = 1000\nREADS_AFTER = 969","READS_BEFORE = 969\nREADS_AFTER = int(open(f'{W}/reads_after.txt').read().strip())")
rep("datetime(2026,10,18,0,7,tzinfo","datetime(2026,10,18,1,10,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_macron': 'trend_macron.txt', 'trend_carr': 'trend_carr.txt', 'trend_french': 'trend_french.txt', 'trend_grubb': 'trend_grubb.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_auburn': 'trend_auburn.txt', 'trend_tennessee': 'trend_tennessee.txt', 'trend_aew': 'trend_aew.txt', 'trend_ufc': 'trend_ufc.txt', 'trend_wareagle': 'trend_wareagle.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep","for batch in ('watch0','watch1','watch2'):  # noqa keep")
rep("for batch in ('watch0','watch1','watch2','watch3'):\n","for batch in ('watch0','watch1','watch2'):\n")
rep("DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']",
    "DUE = ['politics','science','entertainment','music','gaming','ideas','sports','internet','life','offbeat']")
rep("""    ('quote_is','quote'),('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_macron','trend.Macron'),('trend_carr','trend.Tommy Carr'),('trend_french','trend.The French'),('trend_grubb','trend.Grubb'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_auburn','trend.Auburn'),('trend_tennessee','trend.Tennessee'),('trend_aew','trend.#AEWWrestleDream'),('trend_ufc','trend.#UFCEdmonton'),('trend_wareagle','trend.War Eagle'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("'trend.WAR DAMN EAGLE','trend.War Eagle','trend.Grubb','trend.DeBoer'): return 'sports'",
    "'trend.WAR DAMN EAGLE','trend.War Eagle','trend.Grubb','trend.DeBoer','trend.#AEWWrestleDream','trend.#UFCEdmonton','trend.War Damn Eagle','trend.Go Vols','trend.Kromah','trend.Notre Dame'): return 'sports'")
rep("('The French','Paris'),('Grubb','DeBoer')]:",
    "('The French','Paris'),('Grubb','DeBoer'),('Auburn','War Eagle'),('War Eagle','Auburn'),('Auburn','War Damn Eagle'),('War Eagle','War Damn Eagle'),('Tennessee','Go Vols'),('Tennessee','DeBoer'),('Tennessee','Grubb')]:")
rep("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}""",
"""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""")
rep("and, as 00Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(01Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
TR=('trend names Auburn, Tennessee, #AEWWrestleDream, #UFCEdmonton, "War Eagle" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; '
    'the top-ten US names with no posts attached in 0004Z; Auburn and War Eagle are one event (Auburn football, with War Damn Eagle); Tennessee is one event with Grubb, DeBoer and Go Vols (Alabama v Tennessee); '
    'Georgia, Macron, The French, Paris and Tommy Carr had posts attached in 0004Z and were not searched again)')
m=re.search(r"trend names Macron, \"Tommy Carr\".*?had posts attached in 2308Z\)", s)
if not m: raise SystemExit('trend block')
s=re.sub(r"trend names Macron, \"Tommy Carr\".*?had posts attached in 2308Z\)", lambda _m: TR, s)
rep("quote/repost words is/you/and + my; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine;",
    "quote/repost words it/that/just + what; sensors culture/sports/online; desks politics/science/entertainment/music/gaming/ideas/sports/internet/life/offbeat;")
rep("""'3 quote pages + 1 repost page, common words "is", "you", "and" and "my": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each'""",
"""'3 quote pages + 1 repost page, common words "it", "that", "just" and "what": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-17T2308Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 2308Z, next run',[]))""",
"""        _last = '2026-10-18T0004Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 0004Z, next run',[]))""")
rep("""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2308Z, due 01:08Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2201Z, due 02:01Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2101Z, due 01:01Z)'""",
"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-18T0004Z, due 02:04Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2201Z, due 02:01Z)'""")
rep("""f'Evening run at 8:04 PM ET (00:04 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads; first run of the UTC day, the X day reset at 00:00 UTC): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2308Z run ended at 340 on the old day). '""",
"""f'Evening run at 8:59 PM ET (00:59 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0004Z run ended at 969, so nothing else read in between). '""")
rep("00Z is a fourth hour, so the slow tier was included; under the 400 cap, none left out; 4 reads","01Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 3 reads")
rep("(4 reads); quote/repost words is/you/and + my (3+1); '","(5 reads); quote/repost words it/that/just + what (3+1); '")
idx=s.find("f'sensors news/money/science; 10 desk reads:")
if idx<0: raise SystemExit('desk reason')
end=s.find("\n", idx)
s=s[:idx]+("f'sensors culture/sports/online; 10 desk reads: the hourly desks politics, entertainment, sports, internet (last ok 0004Z), "
     "the four-hour desks science, ideas, life (last ok 2101Z, due 01:01Z) and the two-hour desks music, gaming, offbeat (last ok 2308Z, due 01:08Z, read at 01:08Z); "
     "world, justice, markets, ai, tech, medicine next due 02:04Z, defense, disaster, business 02:01Z; '")+s[end:]
rep("culture/sports/online sensors next rotation","news/money/science sensors next rotation")
rep("out_path = f'{REPO}/capture/2026/10/18/0004Z.json'","out_path = f'{REPO}/capture/2026/10/18/0059Z.json'")
open('build_capture.py','w').write(s); print('ok')
