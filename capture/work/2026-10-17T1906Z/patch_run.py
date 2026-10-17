s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)
rep('"""Build capture/2026/10/17/1807Z.json','"""Build capture/2026/10/17/1906Z.json')
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1807Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1906Z'")
rep("RUN_ID = '2026-10-17T1807Z'","RUN_ID = '2026-10-17T1906Z'")
rep("STARTED = '2026-10-17T18:07:00Z'","STARTED = '2026-10-17T19:06:00Z'")
rep("OBS_AT = '2026-10-17T18:08:00Z'","OBS_AT = '2026-10-17T19:07:00Z'")
rep("READS_BEFORE = 520\nREADS_AFTER = 486","READS_BEFORE = 486\nREADS_AFTER = 458")
rep("datetime(2026,10,17,18,11,tzinfo=timezone.utc)","datetime(2026,10,17,19,9,tzinfo=timezone.utc)")
rep("""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_ryanday': 'trend_ryanday.txt', 'trend_arthursmith': 'trend_arthursmith.txt', 'trend_betis': 'trend_betis.txt', 'trend_gators': 'trend_gators.txt', 'trend_nokings': 'trend_nokings.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_that': 'quote_that.txt',
    'repost_it': 'repost_it.txt',
    'trend_jsmith': 'trend_jsmith.txt', 'trend_sayin': 'trend_sayin.txt', 'trend_manning': 'trend_manning.txt', 'trend_sark': 'trend_sark.txt', 'trend_timmons': 'trend_timmons.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','medicine','entertainment','sports','internet']","DUE = ['politics','entertainment','music','gaming','sports','internet','offbeat']")
rep("""    ('quote_just','quote'),('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_ryanday','trend.Ryan Day'),('trend_arthursmith','trend.Arthur Smith'),('trend_betis','trend.Betis'),('trend_gators','trend.Gators'),('trend_nokings','trend.No Kings'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('quote_you','quote'),('quote_that','quote'),('repost_it','repost'),
    ('trend_jsmith','trend.Jeremiah Smith'),('trend_sayin','trend.Sayin'),('trend_manning','trend.Arch Manning'),('trend_sark','trend.Sark'),('trend_timmons','trend.Jay Timmons'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("        if str(_x) in ('trend.Ryan Day','trend.Arthur Smith','trend.Betis','trend.Gators','trend.Indiana'): return 'sports'",
    "        if str(_x) in ('trend.Ryan Day','trend.Arthur Smith','trend.Betis','trend.Gators','trend.Indiana'): return 'sports'\n        if str(_x) in ('trend.Jeremiah Smith','trend.Sayin','trend.Arch Manning','trend.Sark','trend.Jay Timmons'): return 'sports'")
rep("('Ryan Day','Ohio State'),","('Ryan Day','Ohio State'),('Jeremiah Smith','Ohio State'),('Sayin','Julian Sayin'),('Sayin','Ohio State'),('Jeremiah Smith','Julian Sayin'),('Arch Manning','Gators'),('Sark','Gators'),('Arch Manning','#HookEm'),('Sark','#HookEm'),('Sark','Arch Manning'),('Arch Manning','Sark'),")
rep("(18Z is not a fourth hour, so no slow tier)","(19Z is not a fourth hour, so no slow tier)")
rep("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}""","""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""")
rep("        _last = '2026-10-17T1706Z'","        _last = '2026-10-17T1807Z'")
rep("'rotation: culture/sports/online read in 1706Z, next run'","'rotation: news/money/science read in 1807Z, next run'")
rep("""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1706Z, due 19:06Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1706Z, due 21:06Z)'""","""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1807Z, due 20:07Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1706Z, due 21:06Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1807Z, due 22:07Z)'""")
rep("out_path = f'{REPO}/capture/2026/10/17/1807Z.json'","out_path = f'{REPO}/capture/2026/10/17/1906Z.json'")
open('build_capture.py','w').write(s); print('ok')
