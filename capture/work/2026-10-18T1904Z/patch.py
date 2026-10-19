import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
rep('"""Build capture/2026/10/18/1807Z.json','"""Build capture/2026/10/18/1904Z.json')
rep("capture/work/2026-10-18T1807Z'","capture/work/2026-10-18T1904Z'")
rep("RUN_ID = '2026-10-18T1807Z'","RUN_ID = '2026-10-18T1904Z'")
rep("STARTED = '2026-10-18T18:07:00Z'","STARTED = '2026-10-18T19:04:00Z'")
rep("OBS_AT = '2026-10-18T18:08:00Z'","OBS_AT = '2026-10-18T19:05:00Z'")
rep("READS_BEFORE = 505","READS_BEFORE = 474")
rep("datetime(2026,10,18,17,13,tzinfo","datetime(2026,10,18,19,7,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',
    'repost_just': 'repost_just.txt',
    'trend_calebwilliams': 'trend_calebwilliams.txt', 'trend_boswell': 'trend_boswell.txt', 'trend_goku': 'trend_goku.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'req_wainwright': 'req_r-2026-10-18-01.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt',
    'repost_that': 'repost_that.txt',
    'trend_ajbrown': 'trend_ajbrown.txt', 'trend_steelers': 'trend_steelers.txt', 'trend_camward': 'trend_camward.txt', 'trend_danieljones': 'trend_danieljones.txt', 'trend_panthers': 'trend_panthers.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
rep("if d['id'] in ('politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet')]","if d['id'] in ('politics','entertainment','sports','internet','science','ideas','life')]")
rep("""    ('quote_the','quote'),('quote_this','quote'),('quote_you','quote'),('repost_just','repost'),
    ('trend_calebwilliams','trend.Caleb Williams'),('trend_boswell','trend.Boswell'),('trend_goku','trend.Goku'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
    ('req_wainwright','request'),
""","""    ('quote_is','quote'),('quote_my','quote'),('quote_what','quote'),('repost_that','repost'),
    ('trend_ajbrown','trend.AJ Brown'),('trend_steelers','trend.Steelers'),('trend_camward','trend.Cam Ward'),('trend_danieljones','trend.Daniel Jones'),('trend_panthers','trend.Panthers'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
rep("""        if str(_x) in ('trend.Goku','trend.#DEATHBATTLE'): return 'entertainment'  # 1807Z""","""        if str(_x) in ('trend.Goku','trend.#DEATHBATTLE'): return 'entertainment'  # 1807Z
        if str(_x) in ('trend.AJ Brown','trend.Steelers','trend.Cam Ward','trend.Daniel Jones','trend.Panthers','trend.Mike McCarthy','trend.Travis Hunter','trend.#Jets','trend.#DaBears','trend.Aaron Glenn','trend.Charlie Jones','trend.Deshaun Watson'): return 'sports'  # 1904Z""")
rep("""REQ_PICKS = {'r-2026-10-18-01': ['2111578871921274962','2111861770444739018','2111652303854076191','2111689401051103636']}
REQ_FILES = {'r-2026-10-18-01': 'req_wainwright'}
REQ_ONLY = {t['id'] for t in (raw['req_wainwright'].get('data') or [])} - set(REQ_PICKS['r-2026-10-18-01'])""","""REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()""")
s=s.replace("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):")
rep("if _c.endswith('1807Z.json') and '/18/' in _c: continue","if _c.endswith('1904Z.json') and '/18/' in _c: continue")
rep("""DESK_OVERRIDE_1807 = {""","""DESK_OVERRIDE_RUN = {}  # 1904Z
DESK_OVERRIDE_1807 = {""")
rep("""    if pid in DESK_OVERRIDE_1807:
        rec['desk'] = DESK_OVERRIDE_1807[pid]""","""    if pid in DESK_OVERRIDE_RUN:
        rec['desk'] = DESK_OVERRIDE_RUN[pid]
    elif pid in DESK_OVERRIDE_1807:
        rec['desk'] = DESK_OVERRIDE_1807[pid]""")
rep("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("""        _last = '2026-10-18T1709Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 1600Z); culture/online/sports last read in {_last}, next run',[]))""","""        _last = '2026-10-18T1807Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 1709Z); news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, read in 1709Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 1709Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1501Z, due 19:01Z)'""","""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, read in 1709Z, due 19:09Z)'
        elif d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 1807Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 1709Z)'""")
rep("ANSWERED_EARLIER = {","ANSWERED_EARLIER = {'r-2026-10-18-01':'2026-10-18T1807Z',")
i=s.index("ANSWERS = [{"); j=s.index("capture = {")
s=s[:i]+"ANSWERS = []\n"+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/18/1807Z.json'","out_path = f'{REPO}/capture/2026/10/18/1904Z.json'")
open('build_capture.py','w').write(s)
print('ok')
