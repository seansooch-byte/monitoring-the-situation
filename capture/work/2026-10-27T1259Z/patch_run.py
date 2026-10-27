import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
rep('capture/2026/10/27/1211Z.json from','capture/2026/10/27/1259Z.json from')
rep("work/2026-10-27T1211Z'","work/2026-10-27T1259Z'")
rep("RUN_ID = '2026-10-27T1211Z'","RUN_ID = '2026-10-27T1259Z'")
rep("STARTED = '2026-10-27T12:11:00Z'","STARTED = '2026-10-27T12:59:00Z'")
rep("OBS_AT = '2026-10-27T12:12:00Z'","OBS_AT = '2026-10-27T13:00:00Z'")
rep("READS_BEFORE = 749","READS_BEFORE = 726")
rep("datetime(2026,10,27,12,12,tzinfo=timezone.utc).timestamp()  # 1211Z (","datetime(2026,10,27,13,0,tzinfo=timezone.utc).timestamp()  # 1259Z (1211Z used 12:12, ")
rep("""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'req_passport': 'req_passport.txt', 'req_people': 'req_people.txt',""","""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',""")
rep("""    'repost_you': 'repost_you.txt',""","""    'repost_it': 'repost_it.txt',""")
rep("""    'trend_sexiestmanalive': 'trend_sexiestmanalive.txt', 'trend_sofi': 'trend_sofi.txt', 'trend_jonathanbailey': 'trend_jonathanbailey.txt', 'trend_flamengo': 'trend_flamengo.txt',""","""    'trend_beijingppg': 'trend_beijingppg.txt', 'trend_bladerunnerppg': 'trend_bladerunnerppg.txt',""")
rep("""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""","""    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""","""    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""")
rep("""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_sexiestmanalive','trend.Sexiest Man Alive'),('trend_sofi','trend.$SOFI'),('trend_jonathanbailey','trend.Jonathan Bailey'),('trend_flamengo','trend.Flamengo'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_beijingppg','trend.#BeijingMustInvestigatePPGNow'),('trend_bladerunnerppg','trend.#BladeRunnerLovesPPGsCowDung'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Sexiest Man Alive','trend.Jonathan Bailey'): return 'entertainment'""","""        if str(_x) in ('trend.#BeijingMustInvestigatePPGNow','trend.#BladeRunnerLovesPPGsCowDung'): return 'entertainment'  # 1259Z: fan campaign against Papergames (Love and Deepspace) over a Blade Runner collaboration
        if str(_x) in ('trend.Sexiest Man Alive','trend.Jonathan Bailey'): return 'entertainment'""")
rep("if _c.endswith('1211Z.json') and '/27/' in _c: continue","if _c.endswith('1259Z.json') and '/27/' in _c: continue")
rep("""REQ_PICKS = {'r-2026-10-27-01': ['2114838714040102928','2114828995145396411','2115011654345969945','2114879998683226528','2115010479508660523','2115021719903576183','2115035264695292244']}
REQ_FILES = {'r-2026-10-27-01': 'req_passport'}
REQ_ONLY = ({t['id'] for t in (raw['req_passport'].get('data') or [])} | {t['id'] for t in (raw['req_people'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-27-01'])""","""REQ_FILES = {}
REQ_ONLY = set()""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
rep("_last = '2026-10-27T1102Z'","_last = '2026-10-27T1211Z'")
rep("not read this run (rotation: news/money/science read this run;","not read this run (rotation: culture/sports/online read this run;")
rep("ANSWERED_EARLIER = {","ANSWERED_EARLIER = {'r-2026-10-27-01':'2026-10-27T1211Z',")
i0=s.index("ANSWERS = [{"); i1=s.index("capture = {",i0)
s=s[:i0]+"ANSWERS = []\n"+s[i1:]
rep("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1211Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1259Z.json'")
rep("one hundred and seventy-first run (kept","one hundred and seventy-second run (kept")
rep("one hundred and seventy-fourth run (kept","one hundred and seventy-fifth run (kept")
rep('2 quote pages + 1 repost page (budget), common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
    '2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)')
open('build_capture.py','w').write(s)
print('ok')
