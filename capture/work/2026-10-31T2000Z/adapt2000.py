s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    assert s.count(start)>=1,start
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/31/1909Z.json from saved','"""Build capture/2026/10/31/2000Z.json from saved')
R("capture/work/2026-10-31T1909Z'","capture/work/2026-10-31T2000Z'")
R("RUN_ID = '2026-10-31T1909Z'","RUN_ID = '2026-10-31T2000Z'")
L("STARTED = ","STARTED = '2026-10-31T20:00:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T20:01:00Z'")
R("READS_BEFORE = 424","READS_BEFORE = 395")
L("READS_USED = 29","READS_USED = 42  # 2000Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 395 to 353; no 429 or 503 refusals")
R("datetime(2026,10,31,19,10,tzinfo=timezone.utc).timestamp()  # 1909Z (","datetime(2026,10,31,20,1,tzinfo=timezone.utc).timestamp()  # 2000Z (1909Z used 19:10, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',  # 1909Z: five watch reads
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 1909Z: three screen reads; no request asked
    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 2000Z: seven watch reads; screen cut by the plan; no request asked
    'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
""")
R("""    'trend_arizona': 'trend_arizona.txt', 'trend_persona1': 'trend_persona1.txt', 'trend_furtherado': 'trend_furtherado.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'trend_riftbound': 'trend_riftbound.txt', 'trend_tommycarr': 'trend_tommycarr.txt', 'trend_syracuse': 'trend_syracuse.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 2000Z: all 19 desks, as the plan for 2026-10-31T20Z lists")
open('build_capture.py','w').write(s); print('part1 ok')
