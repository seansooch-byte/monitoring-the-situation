s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    s=s.replace(a,b) if count is None else s.replace(a,b,count)
rep('capture/2026/10/18/2203Z.json from saved','capture/2026/10/18/2306Z.json from saved')
rep("work/2026-10-18T2203Z'","work/2026-10-18T2306Z'")
rep("RUN_ID = '2026-10-18T2203Z'","RUN_ID = '2026-10-18T2306Z'")
rep("STARTED = '2026-10-18T22:03:00Z'","STARTED = '2026-10-18T23:06:00Z'")
rep("OBS_AT = '2026-10-18T22:04:00Z'","OBS_AT = '2026-10-18T23:07:00Z'")
rep("READS_BEFORE = 383","READS_BEFORE = 350")
rep("datetime(2026,10,18,22,5,tzinfo","datetime(2026,10,18,23,9,tzinfo")
rep("""    'quote_just': 'quote_just.txt', 'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_bears': 'trend_bears.txt', 'trend_steelers': 'trend_steelers.txt', 'trend_colts': 'trend_colts.txt', 'trend_titans': 'trend_titans.txt', 'trend_saints': 'trend_saints.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'req_omar': 'req_r-2026-10-18-02a.txt', 'req_notts': 'req_r-2026-10-18-02b.txt',""",
"""    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_rams': 'trend_rams.txt', 'trend_cardinals': 'trend_cardinals.txt', 'trend_chargers': 'trend_chargers.txt', 'trend_bensimmons': 'trend_bensimmons.txt', 'trend_chiefs': 'trend_chiefs.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]","('politics','entertainment','sports','internet','ai','tech','medicine','science','ideas','life')]")
rep("""    ('quote_just','quote'),('quote_the','quote'),('quote_this','quote'),('repost_you','repost'),
    ('trend_bears','trend.Bears'),('trend_steelers','trend.Steelers'),('trend_colts','trend.Colts'),('trend_titans','trend.Titans'),('trend_saints','trend.Saints'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_rams','trend.Rams'),('trend_cardinals','trend.Cardinals'),('trend_chargers','trend.Chargers'),('trend_bensimmons','trend.Ben Simmons'),('trend_chiefs','trend.Chiefs'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""'trend.#ForTheShoe'): return 'sports'  # 2203Z""","""'trend.#ForTheShoe'): return 'sports'  # 2203Z
        if str(_x) in ('trend.Rams','trend.Cardinals','trend.Chargers','trend.Ben Simmons','trend.Chiefs','trend.McVay','trend.Justin Herbert','trend.#BillsMafia','trend.Bowers','trend.Kirk Cousins','trend.Butker','trend.Herbert'): return 'sports'  # 2306Z""")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("(22Z is not a fourth hour, so the rest of the last 24 hours was not added)","(23Z is not a fourth hour, so the rest of the last 24 hours was not added)")
TN='trend names Rams, Cardinals, Chargers, "Ben Simmons", Chiefs (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2203Z; McVay and "Justin Herbert" are the Rams and Chargers games, Browns (read in 2005Z) and #BillsMafia cut after the five-name budget; Colts had posts from 2203Z; all but "Ben Simmons" are NFL Sunday names)'
rep('trend names Bears, Steelers, Colts, Titans, Saints (each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2102Z; Browns also had none but was read in 2005Z and cut after the five-name budget; JJ McCarthy, Giants, Falcons and Kyler Gordon had posts from 2102Z; all are NFL Sunday names); quote/repost words just/the/this + you; sensors news/money/science; desks politics/entertainment/sports/internet/music/gaming/offbeat/world/justice/markets;',
    TN+'; quote/repost words is/my/it + that; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/science/ideas/life;')
rep("""'3 quote pages + 1 repost page, common words "just", "the", "this" and "you": (just lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "is", "my", "it" and "that": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-18T2102Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 2005Z); culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-18T2203Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 2102Z); news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 2102Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 2102Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1904Z, due at 23:04Z)'""",
"""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 2203Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 2102Z, due at 01:02Z)'""")
rep("""REQ_PICKS = {'r-2026-10-18-02': ['2111435562754478490','2111502504789766245','2111851425190056198','2111473994293453205','2111736030663426263','2111889948890796116','2111828553457152190']}
REQ_FILES = {'r-2026-10-18-02': 'req_omar'}
REQ_ONLY = ({t['id'] for t in (raw['req_omar'].get('data') or [])} | {t['id'] for t in (raw['req_notts'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-18-02'])""","""REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()""")
rep("ANSWERED_EARLIER = {'r-2026-10-18-01':'2026-10-18T1807Z',","ANSWERED_EARLIER = {'r-2026-10-18-02':'2026-10-18T2203Z','r-2026-10-18-01':'2026-10-18T1807Z',")
i=s.index("ANSWERS = [{"); j=s.index("}]\n",i)
s=s[:i]+"ANSWERS = []"+s[j+2:]
rep("""            f'Daytime run at 6:03 PM ET (22:03 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2102Z run ended at 383, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names Bears, Steelers, Colts, Titans, Saints (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2102Z; Browns also had none but was cut after the five-name budget (read in 2005Z); all are NFL Sunday names); quote/repost words just/the/this + you (3+1); '
            f'sensors news/money/science (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat, world, justice, markets last read 2005Z); ai/tech/medicine and four-hour defense/disaster/business (2102Z) and science/ideas/life (1904Z, due 23:04Z) not due; '""",
"""            f'Daytime run at 7:06 PM ET (23:06 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads; last run before the 00:00 UTC reset): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2203Z run ended at 350, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names Rams, Cardinals, Chargers, "Ben Simmons", Chiefs (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2203Z; McVay and "Justin Herbert" are the Rams and Chargers games; Browns and #BillsMafia cut after the five-name budget; Colts had posts from 2203Z); quote/repost words is/my/it + that (3+1); '
            f'sensors culture/sports/online (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour ai, tech, medicine last read 2102Z; four-hour science, ideas, life last read 1904Z); music/gaming/offbeat/world/justice/markets (2203Z) and four-hour defense/disaster/business (2102Z, due 01:02Z) not due; '""")
rep("""            f'Request r-2026-10-18-02 answered with two searches (2 reads); the other open requests were answered in earlier captures and not read. '""",
"""            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '""")
rep("culture/sports/online sensors next rotation. '","news/money/science sensors next rotation. '")
rep("out_path = f'{REPO}/capture/2026/10/18/2203Z.json'","out_path = f'{REPO}/capture/2026/10/18/2306Z.json'")
if "if _c.endswith('2203Z.json') and '/18/' in _c: continue" in s:
    rep("if _c.endswith('2203Z.json') and '/18/' in _c: continue","if _c.endswith('2306Z.json') and '/18/' in _c: continue")
open('build_capture.py','w').write(s)
print('ok')
