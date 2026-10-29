import re
s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R("1102Z.json from saved","1206Z.json from saved")
R("capture/work/2026-10-29T1102Z'","capture/work/2026-10-29T1206Z'")
R("RUN_ID = '2026-10-29T1102Z'","RUN_ID = '2026-10-29T1206Z'")
R("STARTED = '2026-10-29T11:02:00Z'","STARTED = '2026-10-29T12:06:00Z'")
R("OBS_AT = '2026-10-29T11:04:00Z'","OBS_AT = '2026-10-29T12:08:00Z'")
R("READS_BEFORE = 710","READS_BEFORE = 685")
SPAN("READS_USED = 19","\n","READS_USED = 40  # 1206Z: this run's 40 X calls, the plan's 42 reads less the screen item it cuts (watch 7, desks 18, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2 = 42; 2 of the listed... see reason); no 429 or 503 refusals\n")
R("datetime(2026,10,29,11,4,tzinfo=timezone.utc).timestamp()  # 1102Z (","datetime(2026,10,29,12,8,tzinfo=timezone.utc).timestamp()  # 1206Z (1102Z used 11:04, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'trend_happyfridayeve': 'trend_happyfridayeve.txt', 'trend_nationalcatday': 'trend_nationalcatday.txt', 'trend_cardcrush': 'trend_cardcrush.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_alconent': 'trend_alconent.txt', 'trend_thursdayvibes': 'trend_thursdayvibes.txt', 'trend_thankfulthursday': 'trend_thankfulthursday.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',""")
SPAN("DUE = ['politics','entertainment','sports','internet']","\n","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','offbeat']  # 1206Z: the 18 desks requests/plan.json for 2026-10-29T12Z lists (desk.life cut by it)\n")
R("""    ('trend_happyfridayeve','trend.Happy Friday Eve'),('trend_nationalcatday','trend.National Cat Day'),('trend_cardcrush','trend.#CARDCRUSH'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_alconent','trend.#AlconEntLongForCowDung'),('trend_thursdayvibes','trend.#thursdayvibes'),('trend_thankfulthursday','trend.Thankful Thursday'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x) == 'trend.National Cat Day': return 'offbeat'""","""        if str(_x) == 'trend.#AlconEntLongForCowDung': return 'gaming'  # 1206Z: fan campaign against Papergames (PPG) and its Alcon Entertainment collab (games)
        if str(_x) in ('trend.#thursdayvibes','trend.Thankful Thursday'): return 'life'  # 1206Z: morning greeting posts, like Good Thursday
        if str(_x) == 'trend.National Cat Day': return 'offbeat'""")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
R("if _c.endswith('1102Z.json') and '/29/' in _c: continue","if _c.endswith('1206Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-29T1009Z'  # 1102Z: news/money/science last read in 1009Z","_last = '2026-10-29T1102Z'  # 1206Z: culture/sports/online last read in 1102Z")
R("not in requests/plan.json for 2026-10-29T11Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-29T12Z (rotation: news/money/science this run)")
R("reason = 'cut by requests/plan.json for 2026-10-29T11Z (overnight band, allowance 20)'","reason = 'cut by requests/plan.json for 2026-10-29T12Z (day band, allowance 42; it cuts desk.life)'")
R("VOL_DESKS = ['world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
open('build_capture.py','w').write(s)
print('ok')
