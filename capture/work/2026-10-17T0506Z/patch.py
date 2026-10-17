import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    if count==1: assert n==1,(n,a[:80])
    s=s.replace(a,b)
rep('capture/2026/10/17/0403Z.json from','capture/2026/10/17/0506Z.json from')
rep("work/2026-10-17T0403Z'","work/2026-10-17T0506Z'")
rep("RUN_ID = '2026-10-17T0403Z'","RUN_ID = '2026-10-17T0506Z'")
rep("STARTED = '2026-10-17T04:03:00Z'","STARTED = '2026-10-17T05:06:00Z'")
rep("OBS_AT = '2026-10-17T04:04:00Z'","OBS_AT = '2026-10-17T05:07:00Z'")
rep("READS_BEFORE = 876","READS_BEFORE = 844")
rep("READS_AFTER = 844","READS_AFTER = 813")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_trevino': 'trend_trevino.txt', 'trend_adin': 'trend_adin.txt', 'trend_purdue': 'trend_purdue.txt', 'trend_smackdown': 'trend_smackdown.txt', 'trend_memphis': 'trend_memphis.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_pfl': 'trend_pfl.txt', 'trend_mamu': 'trend_mamu.txt', 'trend_oplive': 'trend_oplive.txt', 'trend_kessler': 'trend_kessler.txt', 'trend_osiris': 'trend_osiris.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']",
    "DUE = ['politics','defense','disaster','business','entertainment','music','gaming','sports','internet','offbeat']")
rep("""    ('quote_that','quote'),('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_trevino','trend.ash trevino'),('trend_adin','trend.Adin Ross'),('trend_purdue','trend.Purdue'),('trend_smackdown','trend.#SmackDown'),('trend_memphis','trend.Memphis'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),
    ('trend_pfl','trend.#PFLChicago'),('trend_mamu','trend.Mamu'),('trend_oplive','trend.#OPLive'),('trend_kessler','trend.Kessler'),('trend_osiris','trend.YK Osiris'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("('watch0','watch1','watch2','watch3')","('watch0','watch1','watch2')",count=3)
rep("""        if str(_x) in ('trend.#Dateline','trend.Johnny Carson'): return 'entertainment'
""","""        if str(_x) in ('trend.#Dateline','trend.Johnny Carson'): return 'entertainment'
        if str(_x) in ('trend.#PFLChicago','trend.Mamu','trend.Kessler'): return 'sports'
        if str(_x)=='trend.YK Osiris': return 'music'
""")
rep("    _tmap = {'trend.ash trevino':'internet',","    _tmap = {'trend.#PFLChicago':'sports','trend.Mamu':'sports','trend.Kessler':'sports','trend.YK Osiris':'music','trend.ash trevino':'internet',")
rep("for a,b in [('ash trevino','Adin Ross'),","for a,b in [('Mamu','Kessler'),('Kessler','Mamu'),('ash trevino','Adin Ross'),")
rep("""SENSOR_Q = {
    'news': open(f'{W}/sensor_news_q.txt').read().strip(),
    'money': open(f'{W}/sensor_money_q.txt').read().strip(),
    'science': open(f'{W}/sensor_science_q.txt').read().strip(),
}
SENSOR_READ = {'news','money','science'}""","""SENSOR_Q = {
    'culture': open(f'{W}/sensor_culture_q.txt').read().strip(),
    'sports': open(f'{W}/sensor_sports_q.txt').read().strip(),
    'online': open(f'{W}/sensor_online_q.txt').read().strip(),
}
SENSOR_READ = {'culture','sports','online'}""")
rep("and, as 04Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(05Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
TN='trend names #PFLChicago, Mamu, #OPLive, Kessler, "YK Osiris" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0403Z; #PFLChicago is the PFL Chicago MMA card; Mamu and Kessler are one event, the Lakers at Nuggets preseason game; #OPLive is the On Patrol: Live TV show; YK Osiris is the rapper; Purdue, #SmackDown, ash trevino, Memphis and Tulane had posts attached in 0403Z)'
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; "+TN+"; quote/repost words this/is/you + and; sensors culture/sports/online; desks politics/defense/disaster/business/entertainment/music/gaming/sports/internet/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"+s[j:]
rep("""'3 quote pages + 1 repost page, common words "that", "just", "what" and "the": "that lang:en is:quote -is:retweet", "just lang:en is:quote -is:retweet", "what lang:en is:quote -is:retweet", "the lang:en is:retweet", newest first, 25 each'""",
"""'3 quote pages + 1 repost page, common words "this", "is", "you" and "and" (quoted, as a bare and is an operator): "this lang:en is:quote -is:retweet", "is lang:en is:quote -is:retweet", "you lang:en is:quote -is:retweet", "\\"and\\" lang:en is:retweet", newest first, 25 each'""")
rep("""        _last = '2026-10-17T0308Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next',[]))""",
"""        _last = '2026-10-17T0403Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next',[]))""")
rep("""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; two-hour desk, due 05:08Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-17T0105Z; four-hour desk, due 05:05Z)'""",
"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (last ok 2026-10-17T0403Z; two-hour desk, due 06:03Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z)'""")
i=s.index("            f'Daytime run at 12:03 AM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Daytime run at 1:06 AM ET (05:06 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour, so no slow tier; under the 400 cap, none left out); trends US+WW; '
            f'"""+TN.replace('(each','(5 reads; each')+"""; quote/repost words this/is/you + and (3+1); '
            f'sensors culture/sports/online; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; four-hour defense, disaster, business, due 05:05Z; two-hour music, gaming, offbeat, due 05:08Z); world/justice/markets/ai/tech/medicine (due 06:03Z) and science/ideas/life (due 07:08Z) not due; '
"""+s[j:]
rep("culture/sports/online sensors next rotation. '","news/money/science sensors next rotation. '")
rep("out_path = f'{REPO}/capture/2026/10/17/0403Z.json'","out_path = f'{REPO}/capture/2026/10/17/0506Z.json'")
open('build_capture.py','w').write(s)
print('ok')
