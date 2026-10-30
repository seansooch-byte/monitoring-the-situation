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
R('"""Build capture/2026/10/30/2102Z.json from saved','"""Build capture/2026/10/30/2202Z.json from saved')
R("capture/work/2026-10-30T2102Z'","capture/work/2026-10-30T2202Z'")
R("RUN_ID = '2026-10-30T2102Z'","RUN_ID = '2026-10-30T2202Z'")
L("STARTED = ","STARTED = '2026-10-30T22:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T22:03:00Z'")
R("READS_BEFORE = 384","READS_BEFORE = 356")
L("READS_USED = 28","READS_USED = 39  # 2202Z: this run's 39 X calls (watch 4, desks 13, volume 5, request 2 (one search, then one by-id re-read of the six picks because the search came back without full fields), trends 2, sensors 3, viral.global 3, rising.global 2, screen 3, context.top 2); the counter fell 356 to 317; no 429 or 503 refusals")
R("datetime(2026,10,30,21,3,tzinfo=timezone.utc).timestamp()  # 2102Z (","datetime(2026,10,30,22,3,tzinfo=timezone.utc).timestamp()  # 2202Z (2102Z used 21:03, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',  # 2102Z: two screen reads\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 2202Z: three screen reads\n    'req_r01': 'req_r01_picks.txt',  # 2202Z: the six request picks re-read by id with full fields\n")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("    'quote_it': 'quote_it.txt',\n    'repost_that': 'repost_that.txt',","    'quote_just': 'quote_just.txt',\n    'repost_what': 'repost_what.txt',")
R("    'trend_sungoddess': 'trend_sungoddess.txt', 'trend_hubbard': 'trend_hubbard.txt', 'trend_nisha': 'trend_nisha.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_tribunal': 'trend_tribunal.txt', 'trend_usyk': 'trend_usyk.txt', 'trend_altman': 'trend_altman.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 2202Z: the thirteen desks requests/plan.json for 2026-10-30T22Z lists")
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_sungoddess','trend.Sun Goddess'),('trend_hubbard','trend.Stephen Hubbard'),('trend_nisha','trend.Nisha'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_tribunal','trend.Constitutional Tribunal'),('trend_usyk','trend.Usyk'),('trend_altman','trend.Sam Altman'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x)=='trend.Nisha': return 'entertainment'  # 2102Z: Avatar: Seven Havens fans on the character Nisha\n",
  "        if str(_x)=='trend.Nisha': return 'entertainment'  # 2102Z: Avatar: Seven Havens fans on the character Nisha\n        if str(_x)=='trend.Constitutional Tribunal': return 'world'  # 2202Z: Polish police at the Constitutional Tribunal in Warsaw\n        if str(_x)=='trend.Usyk': return 'sports'  # 2202Z: Oleksandr Usyk boxing\n")
R("CTX_REPLIES = CTXR  # 2102Z: replies to TMZ 2116187240233656429 in its first 20 minutes (19 returned)",
  "CTX_REPLIES = CTXR  # 2202Z: replies to ScrambledFaz 2116054436178964783 in its first 20 minutes (13 returned)")
R("CTX_IDS = ['2116187240233656429'] + CTX_REPLIES","CTX_IDS = ['2116054436178964783'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2116187240233656429']+CTXR+CTXQ})  # 2102Z:",
  "DESK_OVERRIDE_RUN.update({_x:'internet' for _x in ['2116187240233656429']})\nDESK_OVERRIDE_RUN.update({_x:'music' for _x in ['2116054436178964783']+CTXR+CTXQ})  # 2202Z: ScrambledFaz post on the rapper Bleood's album KILL YOUR IDOLS and its context replies and quotes are music  # 2102Z:")
R("if _c.endswith('2102Z.json') and '/30/' in _c: continue","if _c.endswith('2202Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T2006Z'  # 2102Z: news/money/science last read in 2006Z","_last = '2026-10-30T2102Z'  # 2202Z: culture/sports/online last read in 2102Z")
R("not in requests/plan.json for 2026-10-30T21Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T22Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T21Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T22Z (desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T21Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T22Z, in its order and in batches of 100 (323 ids; the plan\\'s note: \"59 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 16 flat posts wait for their sixth run\"; its left_out counts 16 slowed, 0 over cap and 0 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: the plan\\'s 3 reads by id: the 132 unread first-hop references in 2 reads (3 Not Found), then the 29 unread second-hop references); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Constitutional Tribunal\", \"Usyk\" and \"Sam Altman\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; Constitutional Tribunal is the Polish police event (with Poland, Tusk, Karol Nawrocki and Warsaw) and had no posts attached in 2102Z, Usyk is new to the top ten, and Sam Altman still had no posts attached; Halloween and Karol Nawrocki had posts, and Honda, Philo and Tusk were read in the last few runs); desks politics/world/justice/markets/ai/tech/medicine/entertainment/music/gaming/sports/internet/offbeat; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"just\" and \"what\" (2102Z used \"it\" and \"that\"), each quoted so X does not reject a bare stopword: (\"just\" lang:en is:quote -is:retweet), (\"what\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T23:00:00Z, end_time 2026-10-30T22:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-23T23:00Z to 2026-10-30T21:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T06:27:00Z (the post\\'s creation minute) and end_time 2026-10-30T06:47:00Z: (conversation_id:2116054436178964783 is:reply) and (quotes_of_tweet_id:2116054436178964783 -is:retweet); the plan gives context.top two reads, so one post: 2116054436178964783 (@ScrambledFaz post on the rapper Bleood\\'s album KILL YOUR IDOLS, the biggest post new this run under 24 hours old at about 1.76M views; MikeVorkunov\\'s 2.18M-view post is over 24 hours old); 13 replies and 3 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (4:02 PM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (5:02 PM CT Oct 30 / 22:02 UTC Oct 30, the 22Z slot; band allowance 42): requests/plan.json is for 2026-10-30T22Z (written 21:10Z after the 2102Z capture), so it was followed (38 reads listed) top to bottom; screen used all 3 of its reads, and the request took one read more than listed (a by-id re-read of its six picks, because the search came back without full post fields), so 39 reads, within the allowance. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 323 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 16 slowed flat posts in its left_out were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (the thirteen the plan lists; defense, disaster, business, science, ideas and life not due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Constitutional Tribunal", "Usyk" and "Sam Altman" (3 reads). rising.global: quote stream "just" and repost stream "what" (2 reads). context.top: ScrambledFaz 2116054436178964783 (2 reads). '
            f'Screen: 3 reads by id (132 unread first-hop references in two reads, 3 Not Found; then 29 second-hop references). '
            f'Request r-2026-10-30-01 (Polish government and president on the police at the Constitutional Tribunal): one search of the named accounts since 00:00Z Oct 30, then the six on-topic posts re-read by id: Donald Tusk, President Nawrocki (cutting short his flight to Senegal), Justice Minister and Prosecutor General Waldemar Zurek (immunity requests to the Tribunal), two Justice Ministry videos of Zurek and the PM office video of Tusk; the President\\'s office account KPRP returned nothing in the window and Judge Anna Korwin-Piotrowska was not searched by name. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T21Z',","'plan': '2026-10-30T22Z',")
R("    'context': [{'post_id': '2116187240233656429',","    'context': [{'post_id': '2116054436178964783',")
R("f'{REPO}/capture/2026/10/30/2102Z.json'","f'{REPO}/capture/2026/10/30/2202Z.json'")
R("REQ_PICKS = {}\n","REQ_PICKS = {'r-2026-10-30-01': ['2116238502027464938','2116216763582972069','2116224112624271680','2116252860484812995','2116243440946057691','2116246219097780723']}  # 2202Z: Tusk, Nawrocki, Zurek and the Justice Ministry and PM office videos\n")
R("REQ_FILES = {}\n","REQ_FILES = {'r-2026-10-30-01': 'req_r01'}\n")
R("REQ_Q = {\n","REQ_Q = {\n    'r-2026-10-30-01': 'search_posts_all (from:donaldtusk OR from:PremierRP OR from:KPRP OR from:NawrockiKn OR from:MS_GOV_PL OR from:PK_GOV_PL OR from:Zurek_Waldemar) -is:retweet -is:reply, start_time 2026-10-30T00:00:00Z, relevancy, 25 results; Zurek\\'s own post (account w_zurek) came in as a quoted reference; the six posts on the Tribunal re-read by id with full fields (KPRP returned nothing; Judge Anna Korwin-Piotrowska not searched by name)',\n")
anchor="EXTRA_PRIVATE |= {'1844016316593971494'"
i=s.index(anchor); j=s.index("\n",i)
s=s[:j+1]+open('skips2202.txt').read()+s[j+1:]
open('build_capture.py','w').write(s)
print('ok')
