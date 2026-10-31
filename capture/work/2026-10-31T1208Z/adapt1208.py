s=open('build_capture.py').read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end); s=s[:i]+new+s[j:]
R('"""Build capture/2026/10/31/1105Z.json from saved','"""Build capture/2026/10/31/1208Z.json from saved')
R("capture/work/2026-10-31T1105Z'","capture/work/2026-10-31T1208Z'")
R("RUN_ID = '2026-10-31T1105Z'","RUN_ID = '2026-10-31T1208Z'")
L("STARTED = ","STARTED = '2026-10-31T12:08:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T12:09:00Z'")
R("READS_BEFORE = 692","READS_BEFORE = 671")
L("READS_USED = 21","READS_USED = 42  # 1208Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the counter fell 671 to 629; no 429 or 503 refusals")
R("datetime(2026,10,31,11,6,tzinfo=timezone.utc).timestamp()  # 1105Z (","datetime(2026,10,31,12,9,tzinfo=timezone.utc).timestamp()  # 1208Z (1105Z used 11:06, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',  # 1000Z: three watch reads\n    'trend_poland': 'trend_poland.txt', 'trend_goodsat': 'trend_goodsat.txt', 'trend_lakers': 'trend_lakers.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 1208Z: seven watch reads; screen cut by the plan; no request asked\n    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',\n    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',\n    'trend_angola': 'trend_angola.txt', 'trend_oasis': 'trend_oasis.txt', 'trend_spencer': 'trend_spencer.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',\n")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 1208Z: all 19 desks, as the plan for 2026-10-31T12Z lists")
R("    ('trend_poland','trend.Poland'),('trend_goodsat','trend.Good Saturday'),('trend_lakers','trend.Lakers'),\n    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),",
  "    ('quote_and','quote'),('repost_my','repost'),\n    ('trend_angola','trend.#AngolaWordAblaze'),('trend_oasis','trend.#OASISxJoongDunk'),('trend_spencer','trend.Spencer Lee'),\n    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),")
R("if _c.endswith('1105Z.json') and '/31/' in _c: continue","if _c.endswith('1208Z.json') and '/31/' in _c: continue")
R("for batch in ('watch0','watch1','watch2'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):  # noqa keep")
R("for batch in ('watch0','watch1','watch2'):\n","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):\n")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T0959Z'  # 1105Z: news/money/science last read in 0959Z","_last = '2026-10-31T1105Z'  # 1208Z: culture/sports/online last read in 1105Z")
R("not in requests/plan.json for 2026-10-31T11Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T12Z (rotation: news/money/science this run)")
s=s.replace("cut by requests/plan.json for 2026-10-31T11Z (overnight band, allowance 20)","cut by requests/plan.json for 2026-10-31T12Z (day band, allowance 42)")
s=s.replace("not due in requests/plan.json for 2026-10-31T11Z (desks_not_due)","not due in requests/plan.json for 2026-10-31T12Z (desks_not_due)")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T11Z","3 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T12Z, in its order and in batches of 100 (654 ids; its left_out counts 120 slowed, 0 over cap and 3 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"#AngolaWordAblaze\", \"#OASISxJoongDunk\" and \"Spencer Lee\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1105Z and not read there; #OASISxJoongDunk and JOONGDUNK OASIS MEMORIES are one event; Happy Halloween, #YouManiacSeriesFinalEP/MANIAC FINAL MOMENT and the NuNew concert were read in 0959Z); all 19 desks; story clusters not in the plan; global floor/pace',\n")
R("sweeps.append(sweep('rising.global','discovery',None,'quote and repost streams: not read, cut by requests/plan.json for 2026-10-31T11Z',6,'skipped','cut by the plan (overnight band, allowance 20)',[]))",
  "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"and\" and \"my\" (0500Z, the last run with rising reads, used \"is\" and \"you\"), each quoted so X does not reject a bare stopword: (\"and\" lang:en is:quote -is:retweet), (\"my\" lang:en is:retweet), newest first, 25 each',\n    6,'ok',None, rising_ids[:30]))")
R("start_time 2026-10-24T12:00:00Z, end_time 2026-10-31T11:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-24T12:00Z to 2026-10-31T10:00Z",
  "start_time 2026-10-24T13:00:00Z, end_time 2026-10-31T12:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T13:00Z to 2026-10-31T11:00Z")
R("sweeps.append(sweep('context.top','context',None,'not read: cut by requests/plan.json for 2026-10-31T11Z',None,'skipped','cut by the plan (overnight band, allowance 20)',[]))",
  "sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T18:31:00Z (the post\\'s creation minute) and end_time 2026-10-30T18:51:00Z: (conversation_id:2116236558852657655 is:reply) and (quotes_of_tweet_id:2116236558852657655 -is:retweet); the plan gives context.top two reads, so one post: 2116236558852657655 (IsraelMilitaryX \"Breaking News: U.S. Vice President J.D. Vance was seen abruptly leaving his midterm election campaign\" post, 2.3M views, the biggest new post under 24 hours once sexual and likely-paid posts are left out); 1 reply (grok) and no quotes in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
R("CTXR = []; CTXQ = []  # 0600Z: context.top cut by the plan\nCTX_REPLIES = []\nCTX_QUOTES = []\nCTX_IDS = []  # 0500Z: the context post itself; 24 replies and 25 quotes returned",
  "CTXR = _top3('context_replies.txt'); CTXQ = _top3('context_quotes.txt')\nCTX_REPLIES = CTXR  # 1208Z: replies to IsraelMilitaryX 2116236558852657655 in its first 20 minutes (the three most liked kept)\nCTX_QUOTES = CTXQ  # 1208Z: quotes in the window, the three most liked kept\nCTX_IDS = ['2116236558852657655'] + CTX_REPLIES + CTX_QUOTES  # 1208Z: the context post itself; 1 reply, the quote read returned nothing")
a=s.index("            f'Overnight-band run (7:05 AM EDT"); b=s.index("            f'{EXTRA_NOTE} '",a)
s=s[:a]+"""            f'Day-band run (8:08 AM EDT Oct 31 / 12:08 UTC Oct 31, the 12Z slot; band allowance 42): requests/plan.json is for 2026-10-31T12Z (written 11:11Z after the 1105Z run) and was followed top to bottom (42 reads listed, screen cut). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; nothing else used reads between 1105Z and this run, the counter was 671 at both points), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 654 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 120 slowed flat posts and 3 unavailable posts in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "#AngolaWordAblaze" (Owuor\\'s Luanda gospel conference), "#OASISxJoongDunk" (Joong and Dunk Halloween fan event) and "Spencer Lee" (US wrestler into the world final) (3 reads). rising.global: quote stream "and" and repost stream "my" (2 reads). context.top: IsraelMilitaryX 2116236558852657655 (2 reads; 1 reply, from grok, and no quotes in the 20-minute window). '
            f'Screen: cut by the plan; unread references left unread. '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
"""+s[b:]
R("'plan': '2026-10-31T11Z',","'plan': '2026-10-31T12Z',")
R("    'context': [],","    'context': [{'post_id': '2116236558852657655', 'replies': [i for i in CTX_REPLIES if i in posts_by_sel], 'quotes': [i for i in CTX_QUOTES if i in posts_by_sel]}],")
R("f'{REPO}/capture/2026/10/31/1105Z.json'","f'{REPO}/capture/2026/10/31/1208Z.json'")
i=s.index("    for _x in sources:\n"); j=i+len("    for _x in sources:\n")
s=s[:j]+"        if str(_x)=='trend.#AngolaWordAblaze': return 'ideas'  # 1208Z: Owuor's gospel conference in Luanda, Angola (religion)\n        if str(_x) in ('trend.#OASISxJoongDunk','trend.JOONGDUNK OASIS MEMORIES'): return 'entertainment'  # 1208Z: Thai actors Joong and Dunk at an OASIS Halloween fan event, one event\n        if str(_x)=='trend.Spencer Lee': return 'sports'  # 1208Z: US wrestler Spencer Lee into the world final\n"+s[j:]
i=s.index("DESK_OVERRIDE_RUN.update({'2116317669796512086'")
s=s[:i]+"DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116236558852657655']+CTXR+CTXQ})  # 1208Z: the IsraelMilitaryX Vance rumour post and its context replies and quotes are politics\n"+s[i:]
open('build_capture.py','w').write(s); print('ok')
