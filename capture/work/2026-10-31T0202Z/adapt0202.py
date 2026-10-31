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
R('"""Build capture/2026/10/31/0102Z.json from saved','"""Build capture/2026/10/31/0202Z.json from saved')
R("capture/work/2026-10-31T0102Z'","capture/work/2026-10-31T0202Z'")
R("RUN_ID = '2026-10-31T0102Z'","RUN_ID = '2026-10-31T0202Z'")
L("STARTED = ","STARTED = '2026-10-31T02:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T02:04:00Z'")
R("READS_BEFORE = 958","READS_BEFORE = 930")
L("READS_USED = 28","READS_USED = 37  # 0202Z: this run's 37 X calls (watch 4, trends 2, desks 13, sensors 3, viral.global 3, rising.global 2, volume 5, context.top 2, screen 3); the counter fell 930 to 893; no 429 or 503 refusals")
R("datetime(2026,10,31,1,3,tzinfo=timezone.utc).timestamp()  # 0102Z (","datetime(2026,10,31,2,4,tzinfo=timezone.utc).timestamp()  # 0202Z (0102Z used 01:03, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',  # 0102Z: five watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',  # 0102Z: two screen reads; no request asked\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',  # 0202Z: four watch reads\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 0202Z: three screen reads; no request asked\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("    'quote_and': 'quote_and.txt',\n    'repost_my': 'repost_my.txt',","    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',")
R("    'trend_smackdown': 'trend_smackdown.txt', 'trend_emmys': 'trend_emmys.txt', 'trend_wade': 'trend_wade.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_simons': 'trend_simons.txt', 'trend_bona': 'trend_bona.txt', 'trend_elvis': 'trend_elvis.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 0202Z: the 13 desks the plan for 2026-10-31T02Z lists")
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_smackdown','trend.#SmackDown'),('trend_emmys','trend.#DaytimeEmmys'),('trend_wade','trend.Dean Wade'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_simons','trend.Simons'),('trend_bona','trend.Bona'),('trend_elvis','trend.ELVIS'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x)=='trend.#SmackDown': return 'sports'  # 0102Z: WWE SmackDown tonight\n",
  "        if str(_x)=='trend.#SmackDown': return 'sports'  # 0102Z: WWE SmackDown tonight\n        if str(_x) in ('trend.Simons','trend.Bona'): return 'sports'  # 0202Z: Anfernee Simons and Adem Bona in tonight's NBA games\n        if str(_x)=='trend.ELVIS': return 'music'  # 0202Z: Harry Styles dressed as Elvis for the first Harryween show at Madison Square Garden\n")
L("REQ_PICKS = {}","REQ_PICKS = {}  # 0202Z: no request asked (none open and unanswered)")
R("CTX_REPLIES = CTXR  # 0102Z: replies to AarushYadav47 2116198463847408066 in its first 20 minutes (25 returned)",
  "CTX_REPLIES = CTXR  # 0202Z: replies to Mangaaposts 2116059923759133013 in its first 20 minutes (none returned)")
R("CTX_IDS = []  # 0102Z: 2116198463847408066 was left out as likely promoted in 1803Z, so neither it nor its context is kept",
  "CTX_IDS = ['2116059923759133013'] + CTX_REPLIES + CTX_QUOTES  # 0202Z: the context post itself; both context reads returned nothing")
R("skip_nsfw |= set(CTXR + CTXQ)  # 0102Z:","# skip_nsfw |= set(CTXR + CTXQ)  # 0102Z:")
R("DESK_OVERRIDE_RUN.update({_x:'tech' for _x in ['2116198463847408066']+CTXR+CTXQ})",
  "DESK_OVERRIDE_RUN.update({_x:'tech' for _x in ['2116198463847408066']})\nDESK_OVERRIDE_RUN.update({_x:'entertainment' for _x in ['2116059923759133013']+CTXR+CTXQ})  # 0202Z: Mangaaposts anime clip is entertainment")
R("if _c.endswith('0102Z.json') and '/31/' in _c: continue","if _c.endswith('0202Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-31T0003Z'  # 0102Z: news/money/science last read in 0003Z","_last = '2026-10-31T0102Z'  # 0202Z: culture/sports/online last read in 0102Z")
R("not in requests/plan.json for 2026-10-31T01Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-31T02Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-31T01Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-31T02Z (desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T01Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-31T02Z, in its order and in batches of 100 (332 ids; its left_out counts 22 slowed, 0 over cap and 1 unavailable, not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 128 unread first-hop references (2 Not Found) then 23 second-hop references); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Simons\", \"Bona\" and \"ELVIS\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 0102Z; #SmackDown and #DaytimeEmmys were read in 0102Z, Halloween and Kucherov earlier, Poland/Tusk are the Constitutional Tribunal event already attached, and #OPLive is a police reality show left unread); desks politics/world/justice/markets/ai/tech/medicine/entertainment/music/gaming/sports/internet/offbeat; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"it\" and \"that\" (0102Z used \"and\" and \"my\"), each quoted so X does not reject a bare stopword: (\"it\" lang:en is:quote -is:retweet), (\"that\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T03:00:00Z, end_time 2026-10-31T02:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-24T03:00Z to 2026-10-31T01:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T06:49:00Z (the post\\'s creation minute) and end_time 2026-10-30T07:09:00Z: (conversation_id:2116059923759133013 is:reply) and (quotes_of_tweet_id:2116059923759133013 -is:retweet); the plan gives context.top two reads, so one post: 2116059923759133013 (@Mangaaposts anime clip, the biggest post new this run under 24 hours old at about 2.88M views); both reads returned no posts in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (9:02 PM EDT","media descriptions. '\n",
"""            f'Day-band run (10:02 PM EDT Oct 30 / 02:02 UTC Oct 31, the 02Z slot; band allowance 42): requests/plan.json is for 2026-10-31T02Z (written 01:12Z after the 0102Z run) and was followed top to bottom (37 reads listed; screen used all 3). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 332 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 22 slowed flat posts and 1 unavailable post in its left_out were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (the 13 due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Simons", "Bona" and "ELVIS" (3 reads). rising.global: quote stream "it" and repost stream "that" (2 reads). context.top: Mangaaposts 2116059923759133013 (2 reads, no replies or quotes returned in the 20-minute window). '
            f'Screen: 3 reads by id (128 unread first-hop references, 2 Not Found, then 23 second-hop). '
            f'No open request asked. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-31T01Z',","'plan': '2026-10-31T02Z',")
R("    'context': [],","    'context': [{'post_id': '2116059923759133013', 'replies': [i for i in CTX_REPLIES if i in posts_by_sel], 'quotes': [i for i in CTX_QUOTES if i in posts_by_sel]}],")
R("f'{REPO}/capture/2026/10/31/0102Z.json'","f'{REPO}/capture/2026/10/31/0202Z.json'")
open('build_capture.py','w').write(s)
print('ok')
