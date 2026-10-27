s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)>=1, ('MISSING', a[:80])
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('"""Build capture/2026/10/27/0204Z.json','"""Build capture/2026/10/27/0302Z.json')
rep("work/2026-10-27T0204Z'","work/2026-10-27T0302Z'")
rep("RUN_ID = '2026-10-27T0204Z'","RUN_ID = '2026-10-27T0302Z'")
rep("STARTED = '2026-10-27T02:04:00Z'","STARTED = '2026-10-27T03:02:00Z'")
rep("OBS_AT = '2026-10-27T02:05:00Z'","OBS_AT = '2026-10-27T03:04:00Z'")
rep("READS_BEFORE = 956","READS_BEFORE = 934")
rep("datetime(2026,10,27,2,5,tzinfo=timezone.utc).timestamp()  # 0204Z (","datetime(2026,10,27,3,4,tzinfo=timezone.utc).timestamp()  # 0302Z (0204Z used 02:05, ")
rep("""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_brewers': 'trend_brewers.txt', 'trend_worldseries': 'trend_worldseries.txt', 'trend_stokes': 'trend_stokes.txt', 'trend_bayley': 'trend_bayley.txt', 'trend_pickens': 'trend_pickens.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_jayz': 'trend_jayz.txt', 'trend_giannis': 'trend_giannis.txt', 'trend_eagles': 'trend_eagles.txt', 'trend_rays': 'trend_rays.txt', 'trend_worldseries': 'trend_worldseries.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""")
rep("""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_brewers','trend.The Brewers'),('trend_worldseries','trend.#WorldSeries2026'),('trend_stokes','trend.Kiah Stokes'),('trend_bayley','trend.Bayley'),('trend_pickens','trend.Pickens'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_jayz','trend.Jay-Z'),('trend_giannis','trend.Giannis'),('trend_eagles','trend.Eagles'),('trend_rays','trend.Rays'),('trend_worldseries','trend.#WorldSeries'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""")
rep("        if str(_x) in ('trend.The Brewers',",
 "        if str(_x) == 'trend.Jay-Z': return 'music'  # 0302Z: Jay-Z named Super Bowl LXI halftime headliner\n        if str(_x) in ('trend.Giannis','trend.Eagles','trend.Rays','trend.#WorldSeries'): return 'sports'  # 0302Z: Giannis triple-double as the Heat fall to 0-4 against the Mavericks; Cowboys at Eagles on Monday Night Football; Brewers-Rays World Series Game 3\n        if str(_x) in ('trend.The Brewers',")
rep("if _c.endswith('0204Z.json') and '/27/' in _c: continue","if _c.endswith('0302Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
 "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("TREND_OFF = {'Warriors': {'2112959155925299672'}}","TREND_OFF = {'Warriors': {'2112959155925299672'}, 'Rays': {'2114721842837471359','1963275716306272336'}}  # 0302Z: 'Rays of sun' (BeautymarksFeet) and a 2025 scripture post match the word, not the Tampa Bay Rays;")
open('build_capture.py','w').write(s); print('ok')
