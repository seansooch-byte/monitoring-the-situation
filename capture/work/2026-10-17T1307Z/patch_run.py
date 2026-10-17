s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]); s=s.replace(a,b)
rep("Build capture/2026/10/17/1202Z.json","Build capture/2026/10/17/1307Z.json")
rep("work/2026-10-17T1202Z'","work/2026-10-17T1307Z'")
rep("RUN_ID = '2026-10-17T1202Z'","RUN_ID = '2026-10-17T1307Z'")
rep("STARTED = '2026-10-17T12:02:00Z'","STARTED = '2026-10-17T13:07:00Z'")
rep("OBS_AT = '2026-10-17T12:08:00Z'","OBS_AT = '2026-10-17T13:09:00Z'")
rep("READS_BEFORE = 701","READS_BEFORE = 669")
rep("READS_AFTER = 669","READS_AFTER = 640")
rep("datetime(2026,10,17,12,12,tzinfo","datetime(2026,10,17,13,14,tzinfo")
rep("""    'quote_you': 'quote_you.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_james': 'trend_james.txt', 'trend_ideabank': 'trend_ideabank.txt', 'trend_cortis': 'trend_cortis.txt', 'trend_chaowesome': 'trend_chaowesome.txt', 'trend_everton': 'trend_everton.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_eveche': 'trend_eveche.txt', 'trend_emimartinez': 'trend_emimartinez.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']","DUE = ['politics','science','entertainment','music','gaming','ideas','sports','internet','life','offbeat']")
rep("""    ('quote_you','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_james','trend.JAMES THE ULTIMATE PHENOMENON'),('trend_ideabank','trend.IDEA BANK'),('trend_cortis','trend.#CORTIS_NOLFest2026'),('trend_chaowesome','trend.CHAOWESOME'),('trend_everton','trend.Everton'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_just','quote'),('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_eveche','trend.#EVECHE'),('trend_emimartinez','trend.Emi Martinez'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x)=='trend.Everton': return 'sports'\n",
    "        if str(_x)=='trend.Everton': return 'sports'\n        if str(_x) in ('trend.#EVECHE','trend.Emi Martinez','trend.Pedro Neto','trend.Caicedo','trend.Hato','trend.Paul Tierney'): return 'sports'\n")
_ev=['#EVECHE','Everton','Pedro Neto','Caicedo','Hato','Paul Tierney']
pairs=[(a,b) for a in _ev for b in _ev if a!=b]
rep("for a,b in [('JAMES THE ULTIMATE PHENOMENON', '#JAMESUnparalleled'),","for a,b in "+repr(pairs)+" + [('JAMES THE ULTIMATE PHENOMENON', '#JAMESUnparalleled'),")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("        _last = '2026-10-17T0506Z'\n        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour, last read 2026-10-17T0403Z); last read in {_last}',6,'skipped','rotation: culture/sports/online next run',[]))",
    "        _last = '2026-10-17T1202Z'\n        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 1202Z, next run',[]))")
rep("and, as 12Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(13Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
OLD=s[s.index('trend names "JAMES THE ULTIMATE PHENOMENON", "IDEA BANK", #CORTIS_NOLFest2026, CHAOWESOME, Everton (each'):]
OLD=OLD[:OLD.index('Everton is the Chelsea v Everton Premier League match)')+len('Everton is the Chelsea v Everton Premier League match)')]
TN='''trend names #EVECHE, "Emi Martinez" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the only top-ten US names with no posts attached in 1202Z; #EVECHE is the Everton v Chelsea Premier League match, one event with Everton (top ten) and Pedro Neto, Paul Tierney, Caicedo and Hato (ranks 15 to 18); the other eight top-ten names had posts attached in 1202Z)'''
rep(OLD,TN)
rep("; quote/repost words you/my/it + that; sensors news/money/science; desks politics/world/justice/markets/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop)",
    "; quote/repost words just/what/the + this; sensors culture/sports/online; desks politics/science/entertainment/music/gaming/ideas/sports/internet/life/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop)")
rep('''    '3 quote pages + 1 repost page, common words "you", "my", "it" and "that": (you lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each',''',
    '''    '3 quote pages + 1 repost page, common words "just", "what", "the" and "this": (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:retweet), newest first, 25 each',''')
rep("""        if d in ('music','gaming','offbeat'):
            reason = 'due (last ok 2026-10-17T0506Z; two-hour desk, due 07:06Z) but cut by the 10-read desk budget (hourly desks and the earlier-due two-hour desks first)'
        elif d in ('defense','disaster','business'):
            reason = 'due (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z) but cut by the 10-read desk budget (four-hour desks cut first)'
        elif d in ('science','ideas','life'):
            reason = 'due (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z) but cut by the 10-read desk budget (four-hour desks cut first)'""",
"""        if d in ('defense','disaster','business'):
            reason = 'due (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z) but cut by the 10-read desk budget (hourly desks, the two-hour desks due since 07:06Z and the four-hour desks due since 07:08Z first)'
        elif d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1202Z, due 14:02Z)'""")
i0=s.index("            f'Daytime run at 8:02 AM ET")
i1=s.index("            f'{EXTRA_NOTE} '")
NEWR='''            f'Daytime run at 9:07 AM ET (13:07 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1202Z run ended at 669). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 4 reads); trends US+WW; '
            f'trend names #EVECHE, "Emi Martinez" (2 reads; the only top-ten US names with no posts attached in 1202Z; #EVECHE is the Everton v Chelsea match, one event with Everton, Pedro Neto, Paul Tierney, Caicedo and Hato); quote/repost words just/what/the + this (3+1); '
            f'sensors culture/sports/online; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat, due since 07:06Z; four-hour science, ideas, life, due since 07:08Z); the four-hour desks defense/disaster/business (due since 09:06Z) cut by the 10-read desk cap; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '
'''
s=s[:i0]+NEWR+s[i1:]
rep("out_path = f'{REPO}/capture/2026/10/17/1202Z.json'","out_path = f'{REPO}/capture/2026/10/17/1307Z.json'")
open('build_capture.py','w').write(s); print('ok')
