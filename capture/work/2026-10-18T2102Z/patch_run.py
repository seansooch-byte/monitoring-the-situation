s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    s=s.replace(a,b) if count is None else s.replace(a,b,count)
rep('capture/2026/10/18/2005Z.json from saved','capture/2026/10/18/2102Z.json from saved')
rep("work/2026-10-18T2005Z'","work/2026-10-18T2102Z'")
rep("RUN_ID = '2026-10-18T2005Z'","RUN_ID = '2026-10-18T2102Z'")
rep("STARTED = '2026-10-18T20:05:00Z'","STARTED = '2026-10-18T21:02:00Z'")
rep("OBS_AT = '2026-10-18T20:06:00Z'","OBS_AT = '2026-10-18T21:03:00Z'")
rep("READS_BEFORE = 446","READS_BEFORE = 413")
rep("datetime(2026,10,18,20,7,tzinfo","datetime(2026,10,18,21,4,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',
    'repost_just': 'repost_just.txt',
    'trend_browns': 'trend_browns.txt', 'trend_falcons': 'trend_falcons.txt', 'trend_colts': 'trend_colts.txt', 'trend_titans': 'trend_titans.txt', 'trend_jets': 'trend_jets.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_is': 'quote_is.txt', 'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_what': 'repost_what.txt',
    'trend_jjmccarthy': 'trend_jjmccarthy.txt', 'trend_giants': 'trend_giants.txt', 'trend_kylergordon': 'trend_kylergordon.txt', 'trend_ajbrown': 'trend_ajbrown.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]","('politics','entertainment','sports','internet','ai','tech','medicine','defense','disaster','business')]")
rep("""    ('quote_the','quote'),('quote_this','quote'),('quote_you','quote'),('repost_just','repost'),
    ('trend_browns','trend.Browns'),('trend_falcons','trend.Falcons'),('trend_colts','trend.Colts'),('trend_titans','trend.Titans'),('trend_jets','trend.Jets'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('quote_it','quote'),('quote_that','quote'),('repost_what','repost'),
    ('trend_jjmccarthy','trend.JJ McCarthy'),('trend_giants','trend.Giants'),('trend_kylergordon','trend.Kyler Gordon'),('trend_ajbrown','trend.AJ Brown'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""'trend.Aaron Rodgers'): return 'sports'  # 2005Z""","""'trend.Aaron Rodgers'): return 'sports'  # 2005Z
        if str(_x) in ('trend.Steelers','trend.Browns','trend.Colts','trend.JJ McCarthy','trend.Giants','trend.Titans','trend.Falcons','trend.Kyler Gordon','trend.Saints','trend.AJ Brown','trend.Jameis','trend.#HereWeGo','trend.Bucs','trend.Jets','trend.Daniel Jones','trend.Panthers','trend.Huntley','trend.Jalen Ramsey','trend.Ballard','trend.#TitanUp'): return 'sports'  # 2102Z""")
rep("for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep","for batch in ('watch0','watch1','watch2'):  # noqa keep")
rep("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("(20Z is a fourth hour, so the rest of the last 24 hours was added, slowest growing last); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(21Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
TN='trend names "JJ McCarthy", Giants, "Kyler Gordon", "AJ Brown" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2005Z; Steelers, Browns, Colts, Titans, Falcons and Saints already had posts from 2005Z and were not read again; only four names qualified; all are NFL Sunday names)'
rep('trend names Browns, Falcons, Colts, Titans, Jets (each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 1904Z; Steelers and AJ Brown already had posts from 1904Z and were not read again; Saints, JJ McCarthy and Kyler Gordon were also new but cut after the five-name budget; all are NFL Sunday names); quote/repost words the/this/you + just; sensors news/money/science; desks politics/entertainment/sports/internet/music/gaming/offbeat/world/justice/markets;',
    TN+'; quote/repost words is/it/that + what; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/defense/disaster/business;')
rep("""'3 quote pages + 1 repost page, common words "the", "this", "you" and "just": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "is", "it", "that" and "what": (is lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-18T1904Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-18T2005Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 1904Z); news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 1807Z; markets/world/justice taken this run as they came due)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1904Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 1709Z)'""",
"""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 2005Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1904Z)'""")
rep("""            f'Daytime run at 4:05 PM ET (20:05 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1904Z run ended at 446, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour; under the 400 cap, none left out; 4 reads); trends US+WW (2 reads); '
            f'trend names Browns, Falcons, Colts, Titans, Jets (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 1904Z; Steelers and AJ Brown already had posts and were not read again; Saints, JJ McCarthy and Kyler Gordon were also new but cut after the five-name budget; all are NFL Sunday names); quote/repost words the/this/you + just (3+1); '
            f'sensors news/money/science (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat last read 1709Z; two-hour world, justice, markets coming due at 20:07 from 1807Z); ai/tech/medicine (1807Z) and four-hour science/ideas/life (1904Z) and defense/disaster/business (1709Z) not due; '""",
"""            f'Daytime run at 5:02 PM ET (21:02 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2005Z run ended at 413, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names "JJ McCarthy", Giants, "Kyler Gordon", "AJ Brown" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2005Z; Steelers, Browns, Colts, Titans, Falcons and Saints already had posts and were not read again; all are NFL Sunday names); quote/repost words is/it/that + what (3+1); '
            f'sensors culture/sports/online (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour ai, tech, medicine last read 1807Z; four-hour defense, disaster, business last read 1709Z, coming due at 21:09Z); music/gaming/offbeat/world/justice/markets (2005Z) and four-hour science/ideas/life (1904Z) not due; '""")
rep("culture/sports/online sensors next rotation. '","news/money/science sensors next rotation. '")
rep("out_path = f'{REPO}/capture/2026/10/18/2005Z.json'","out_path = f'{REPO}/capture/2026/10/18/2102Z.json'")
rep("if _c.endswith('1904Z.json') and '/18/' in _c: continue","if _c.endswith('2102Z.json') and '/18/' in _c: continue")
open('build_capture.py','w').write(s)
print('ok')
