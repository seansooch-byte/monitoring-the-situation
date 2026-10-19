s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    s=s.replace(a,b) if count is None else s.replace(a,b,count)
rep('capture/2026/10/18/2102Z.json from saved','capture/2026/10/18/2203Z.json from saved')
rep("work/2026-10-18T2102Z'","work/2026-10-18T2203Z'")
rep("RUN_ID = '2026-10-18T2102Z'","RUN_ID = '2026-10-18T2203Z'")
rep("STARTED = '2026-10-18T21:02:00Z'","STARTED = '2026-10-18T22:03:00Z'")
rep("OBS_AT = '2026-10-18T21:03:00Z'","OBS_AT = '2026-10-18T22:04:00Z'")
rep("READS_BEFORE = 413","READS_BEFORE = 383")
rep("datetime(2026,10,18,21,4,tzinfo","datetime(2026,10,18,22,5,tzinfo")
rep("""    'quote_is': 'quote_is.txt', 'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_what': 'repost_what.txt',
    'trend_jjmccarthy': 'trend_jjmccarthy.txt', 'trend_giants': 'trend_giants.txt', 'trend_kylergordon': 'trend_kylergordon.txt', 'trend_ajbrown': 'trend_ajbrown.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_just': 'quote_just.txt', 'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_bears': 'trend_bears.txt', 'trend_steelers': 'trend_steelers.txt', 'trend_colts': 'trend_colts.txt', 'trend_titans': 'trend_titans.txt', 'trend_saints': 'trend_saints.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'req_omar': 'req_r-2026-10-18-02a.txt', 'req_notts': 'req_r-2026-10-18-02b.txt',""")
rep("('politics','entertainment','sports','internet','ai','tech','medicine','defense','disaster','business')]","('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]")
rep("""    ('quote_is','quote'),('quote_it','quote'),('quote_that','quote'),('repost_what','repost'),
    ('trend_jjmccarthy','trend.JJ McCarthy'),('trend_giants','trend.Giants'),('trend_kylergordon','trend.Kyler Gordon'),('trend_ajbrown','trend.AJ Brown'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_just','quote'),('quote_the','quote'),('quote_this','quote'),('repost_you','repost'),
    ('trend_bears','trend.Bears'),('trend_steelers','trend.Steelers'),('trend_colts','trend.Colts'),('trend_titans','trend.Titans'),('trend_saints','trend.Saints'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""'trend.#TitanUp'): return 'sports'  # 2102Z""","""'trend.#TitanUp'): return 'sports'  # 2102Z
        if str(_x) in ('trend.Bears','trend.Steelers','trend.Colts','trend.Titans','trend.Saints','trend.Browns','trend.CJ Gardner Johnson','trend.CJGJ','trend.Harbaugh','trend.Kenneth Walker','trend.#DaBears','trend.#Saints','trend.#ForTheShoe'): return 'sports'  # 2203Z""")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("(21Z is not a fourth hour, so the rest of the last 24 hours was not added)","(22Z is not a fourth hour, so the rest of the last 24 hours was not added)")
TN='trend names Bears, Steelers, Colts, Titans, Saints (each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2102Z; Browns also had none but was read in 2005Z and cut after the five-name budget; JJ McCarthy, Giants, Falcons and Kyler Gordon had posts from 2102Z; all are NFL Sunday names)'
rep('trend names "JJ McCarthy", Giants, "Kyler Gordon", "AJ Brown" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2005Z; Steelers, Browns, Colts, Titans, Falcons and Saints already had posts from 2005Z and were not read again; only four names qualified; all are NFL Sunday names); quote/repost words is/it/that + what; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/defense/disaster/business;',
    TN+'; quote/repost words just/the/this + you; sensors news/money/science; desks politics/entertainment/sports/internet/music/gaming/offbeat/world/justice/markets;')
rep("""'3 quote pages + 1 repost page, common words "is", "it", "that" and "what": (is lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "just", "the", "this" and "you": (just lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'""")
rep("""        _last = '2026-10-18T2005Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 1904Z); news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-18T2102Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 2005Z); culture/sports/online last read in {_last}, next run',[]))""")
rep("""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 2005Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1904Z)'""",
"""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 2102Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 2102Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1904Z, due at 23:04Z)'""")
rep("""REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()""","""REQ_PICKS = {'r-2026-10-18-02': ['2111435562754478490','2111502504789766245','2111851425190056198','2111473994293453205','2111736030663426263','2111889948890796116','2111828553457152190']}
REQ_FILES = {'r-2026-10-18-02': 'req_omar'}
REQ_ONLY = ({t['id'] for t in (raw['req_omar'].get('data') or [])} | {t['id'] for t in (raw['req_notts'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-18-02'])""")
rep("""REQ_Q = {
""","""REQ_Q = {
    'r-2026-10-18-02': 'two search_posts_all reads, start_time 2026-10-17T12:00:00Z, relevancy, 25 results each: Omar (search OR searched OR raid OR citizenship OR FBI OR DOJ OR "Justice Department" OR DHS OR denaturalization) -is:retweet -is:reply; and (from:nottspolice OR (Nottingham (officer OR police OR policeman) (shot OR shooting))) -is:retweet -is:reply',
""")
rep("""ANSWERS = []""","""ANSWERS = [{
    'request_id': 'r-2026-10-18-02',
    'status': 'ok',
    'post_ids': [i for i in REQ_PICKS['r-2026-10-18-02'] if i in _here],
    'note': 'Two searches from 2026-10-17T12:00Z (relevancy). No post from the Justice Department, Homeland Security, Rep. Omar or her office was returned, and no post from Nottinghamshire Police (from:nottspolice) was returned. Kept for the Omar search: MichaelARothman (2111435562754478490), a Fox News clip of Homeland Security Secretary Markwayne Mullin calling it a strong case; MSN (2111502504789766245), Omar\\'s attorneys say the search was neither justified nor lawful while the Justice Department says agents complied with court orders; ryanjreilly (2111851425190056198), a former FBI official saying the search flies in the face of Justice Department protocols; UnmaskTheSys (2111473994293453205), Omar\\'s lawyers\\' letter to the Justice Department demanding the seized property back. Posts that mention or name her relatives were left out. Kept for Nottingham: TheBritishIntel (2111736030663426263), officer shot in the foot on Angel Row shortly before 4:50am, two suspects on the run, Nottinghamshire Police recovered a firearm; Newsforce (2111828553457152190), the same details; Channel4News (2111889948890796116), headline only.'
}]""")
rep("""            f'Daytime run at 5:02 PM ET (21:02 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2005Z run ended at 413, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names "JJ McCarthy", Giants, "Kyler Gordon", "AJ Brown" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2005Z; Steelers, Browns, Colts, Titans, Falcons and Saints already had posts and were not read again; all are NFL Sunday names); quote/repost words is/it/that + what (3+1); '
            f'sensors culture/sports/online (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour ai, tech, medicine last read 1807Z; four-hour defense, disaster, business last read 1709Z, coming due at 21:09Z); music/gaming/offbeat/world/justice/markets (2005Z) and four-hour science/ideas/life (1904Z) not due; '""",
"""            f'Daytime run at 6:03 PM ET (22:03 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2102Z run ended at 383, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names Bears, Steelers, Colts, Titans, Saints (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2102Z; Browns also had none but was cut after the five-name budget (read in 2005Z); all are NFL Sunday names); quote/repost words just/the/this + you (3+1); '
            f'sensors news/money/science (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat, world, justice, markets last read 2005Z); ai/tech/medicine and four-hour defense/disaster/business (2102Z) and science/ideas/life (1904Z, due 23:04Z) not due; '""")
rep("""            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop""","""            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop""")
rep("""            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-01 in 1807Z) and was not read again. '""",
"""            f'Request r-2026-10-18-02 answered with two searches (2 reads); the other open requests were answered in earlier captures and not read. '""")
rep("news/money/science sensors next rotation. '","culture/sports/online sensors next rotation. '")
rep("out_path = f'{REPO}/capture/2026/10/18/2102Z.json'","out_path = f'{REPO}/capture/2026/10/18/2203Z.json'")
rep("if _c.endswith('2102Z.json') and '/18/' in _c: continue","if _c.endswith('2203Z.json') and '/18/' in _c: continue")
open('build_capture.py','w').write(s)
print('ok')
