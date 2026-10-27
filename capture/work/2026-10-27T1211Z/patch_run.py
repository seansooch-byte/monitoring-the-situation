import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
rep('capture/2026/10/27/1102Z.json from','capture/2026/10/27/1211Z.json from')
rep("work/2026-10-27T1102Z'","work/2026-10-27T1211Z'")
rep("RUN_ID = '2026-10-27T1102Z'","RUN_ID = '2026-10-27T1211Z'")
rep("STARTED = '2026-10-27T11:02:00Z'","STARTED = '2026-10-27T12:11:00Z'")
rep("OBS_AT = '2026-10-27T11:03:00Z'","OBS_AT = '2026-10-27T12:12:00Z'")
rep("READS_BEFORE = 775","READS_BEFORE = 749")
rep("datetime(2026,10,27,11,3,tzinfo=timezone.utc).timestamp()  # 1102Z (","datetime(2026,10,27,12,12,tzinfo=timezone.utc).timestamp()  # 1211Z (1102Z used 11:03, ")
rep("""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',""","""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'req_passport': 'req_passport.txt', 'req_people': 'req_people.txt',""")
rep("""    'repost_the': 'repost_the.txt',""","""    'repost_you': 'repost_you.txt',""")
rep("""    'trend_gmmtvnext': 'trend_gmmtvnext.txt', 'trend_noahwyle': 'trend_noahwyle.txt',""","""    'trend_sexiestmanalive': 'trend_sexiestmanalive.txt', 'trend_sofi': 'trend_sofi.txt', 'trend_jonathanbailey': 'trend_jonathanbailey.txt', 'trend_flamengo': 'trend_flamengo.txt',""")
rep("""    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""","""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_gmmtvnext','trend.#GMMTVNEXT'),('trend_noahwyle','trend.Noah Wyle'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_sexiestmanalive','trend.Sexiest Man Alive'),('trend_sofi','trend.$SOFI'),('trend_jonathanbailey','trend.Jonathan Bailey'),('trend_flamengo','trend.Flamengo'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.#GMMTVNEXT','trend.Noah Wyle'): return 'entertainment'""","""        if str(_x) in ('trend.Sexiest Man Alive','trend.Jonathan Bailey'): return 'entertainment'  # 1211Z: People's Sexiest Man Alive 2026 (Noah Wyle); Jonathan Bailey was the 2025 pick
        if str(_x)=='trend.Flamengo': return 'sports'  # 1211Z
        if str(_x)=='trend.$SOFI': return 'markets'  # 1211Z: SoFi stock (earnings)
        if str(_x) in ('trend.#GMMTVNEXT','trend.Noah Wyle'): return 'entertainment'""")
rep("if _c.endswith('1102Z.json') and '/27/' in _c: continue","if _c.endswith('1211Z.json') and '/27/' in _c: continue")
rep("""REQ_FILES = {}
REQ_ONLY = set()""","""REQ_PICKS = {'r-2026-10-27-01': ['2114838714040102928','2114828995145396411','2115011654345969945','2114879998683226528','2115010479508660523','2115021719903576183','2115035264695292244']}
REQ_FILES = {'r-2026-10-27-01': 'req_passport'}
REQ_ONLY = ({t['id'] for t in (raw['req_passport'].get('data') or [])} | {t['id'] for t in (raw['req_people'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-27-01'])""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
rep("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
rep("_last = '2026-10-27T1004Z'","_last = '2026-10-27T1102Z'")
rep("not read this run (rotation: culture/sports/online read this run;","not read this run (rotation: news/money/science read this run;")
rep("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1102Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1211Z.json'")
open('build_capture.py','w').write(s)
print('ok')
