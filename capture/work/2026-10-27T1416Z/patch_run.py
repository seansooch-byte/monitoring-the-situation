s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
rep('capture/2026/10/27/1259Z.json from','capture/2026/10/27/1416Z.json from')
rep("work/2026-10-27T1259Z'","work/2026-10-27T1416Z'")
rep("RUN_ID = '2026-10-27T1259Z'","RUN_ID = '2026-10-27T1416Z'")
rep("STARTED = '2026-10-27T12:59:00Z'","STARTED = '2026-10-27T14:16:00Z'")
rep("OBS_AT = '2026-10-27T13:00:00Z'","OBS_AT = '2026-10-27T14:17:00Z'")
rep("READS_BEFORE = 726","READS_BEFORE = 706")
rep("datetime(2026,10,27,13,0,tzinfo=timezone.utc).timestamp()  # 1259Z (","datetime(2026,10,27,14,17,tzinfo=timezone.utc).timestamp()  # 1416Z (1259Z used 13:00, ")
rep("""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',""","""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',""")
rep("""    'repost_it': 'repost_it.txt',""","""    'repost_what': 'repost_what.txt',""")
rep("""    'trend_beijingppg': 'trend_beijingppg.txt', 'trend_bladerunnerppg': 'trend_bladerunnerppg.txt',""","""    'trend_shawnhatosy': 'trend_shawnhatosy.txt',""")
rep("""    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""","""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("""    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""","""    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_beijingppg','trend.#BeijingMustInvestigatePPGNow'),('trend_bladerunnerppg','trend.#BladeRunnerLovesPPGsCowDung'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_shawnhatosy','trend.Shawn Hatosy'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.#BeijingMustInvestigatePPGNow','trend.#BladeRunnerLovesPPGsCowDung'): return 'entertainment'""","""        if str(_x) in ('trend.Shawn Hatosy',): return 'entertainment'  # 1416Z: actor on The Pitt
        if str(_x) in ('trend.#BeijingMustInvestigatePPGNow','trend.#BladeRunnerLovesPPGsCowDung'): return 'entertainment'""")
rep("if _c.endswith('1259Z.json') and '/27/' in _c: continue","if _c.endswith('1416Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
rep("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
rep("_last = '2026-10-27T1211Z'","_last = '2026-10-27T1259Z'")
rep("not read this run (rotation: culture/sports/online read this run;","not read this run (rotation: news/money/science read this run;")
rep("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1259Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1416Z.json'")
rep("one hundred and seventy-second run (kept","one hundred and seventy-third run (kept")
rep("one hundred and seventy-fifth run (kept","one hundred and seventy-sixth run (kept")
rep('2 quote pages + 1 repost page (budget), common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)',
    '2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)')
open('build_capture.py','w').write(s)
print('ok')
