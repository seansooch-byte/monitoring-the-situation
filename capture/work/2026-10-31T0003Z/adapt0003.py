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
R('"""Build capture/2026/10/30/2301Z.json from saved','"""Build capture/2026/10/31/0003Z.json from saved')
R("capture/work/2026-10-30T2301Z'","capture/work/2026-10-31T0003Z'")
R("RUN_ID = '2026-10-30T2301Z'","RUN_ID = '2026-10-31T0003Z'")
L("STARTED = ","STARTED = '2026-10-31T00:03:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-31T00:04:00Z'")
R("READS_BEFORE = 317","READS_BEFORE = 1000")
L("READS_USED = 29","READS_USED = 42  # 0003Z: this run's 42 X calls (watch 7, desks 19, volume 4, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2; screen cut by the plan); the X day reset at 00:00Z, the counter fell 1000 to 958; no 429 or 503 refusals")
R("datetime(2026,10,30,23,2,tzinfo=timezone.utc).timestamp()  # 2301Z (","datetime(2026,10,31,0,4,tzinfo=timezone.utc).timestamp()  # 0003Z (2301Z used 23:02, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',  # 2301Z: three screen reads\n    'req_r01': 'req_r01.txt',  # 2301Z: the request search\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',  # 0003Z: seven watch reads; screen cut by the plan; no request asked\n")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
R("    'quote_the': 'quote_the.txt',\n    'repost_this': 'repost_this.txt',","    'quote_is': 'quote_is.txt',\n    'repost_you': 'repost_you.txt',")
R("    'trend_kucherov': 'trend_kucherov.txt', 'trend_yeon': 'trend_yeon.txt', 'trend_polish': 'trend_polish.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_halloween': 'trend_halloween.txt', 'trend_nbacup': 'trend_nbacup.txt', 'trend_stevens': 'trend_stevens.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment'","DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 0003Z: all 19 desks, as the plan for 2026-10-31T00Z lists")
R("""    ('quote_the','quote'),('repost_this','repost'),
    ('trend_kucherov','trend.Kucherov'),('trend_yeon','trend.Yeon'),('trend_polish','trend.Polish'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_halloween','trend.Halloween'),('trend_nbacup','trend.NBA Cup'),('trend_stevens','trend.Stevens'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("        if str(_x)=='trend.Polish': return 'world'  # 2301Z: the Polish Constitutional Tribunal standoff\n",
  "        if str(_x)=='trend.Polish': return 'world'  # 2301Z: the Polish Constitutional Tribunal standoff\n        if str(_x)=='trend.Halloween': return 'life'  # 0003Z: Halloween costume and greeting posts\n        if str(_x)=='trend.Stevens': return 'politics'  # 0003Z: Haley Stevens and the Michigan Senate race (Mallory McMorrow, Abdul El-Sayed)\n")
L("REQ_PICKS = {'r-2026-10-30-01'","REQ_PICKS = {}  # 0003Z: no request asked (r-2026-10-30-01 answered in 2301Z)")
R("CTX_REPLIES = CTXR  # 2301Z: replies to elonmusk 2116165938525741496 in its first 20 minutes (25 returned)",
  "CTX_REPLIES = CTXR  # 0003Z: replies to pj_sekai 2116165917382255047 in its first 20 minutes (7 returned)")
R("CTX_IDS = ['2116165938525741496'] + CTX_REPLIES","CTX_IDS = ['2116165917382255047'] + CTX_REPLIES")
R("REQ_FILES = {'r-2026-10-30-01': 'req_r01'}","REQ_FILES = {}")
R("DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116165938525741496']+CTXR+CTXQ})  # 2301Z:",
  "DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116165938525741496']})\nDESK_OVERRIDE_RUN.update({_x:'gaming' for _x in ['2116165917382255047']+CTXR+CTXQ})  # 0003Z: pj_sekai (Project Sekai) account-transfer security notice and its context replies and quotes are gaming  # 2301Z:")
R("if _c.endswith('2301Z.json') and '/30/' in _c: continue","if _c.endswith('0003Z.json') and '/31/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T2202Z'  # 2301Z: news/money/science last read in 2202Z","_last = '2026-10-30T2301Z'  # 0003Z: culture/sports/online last read in 2301Z")
R("not in requests/plan.json for 2026-10-30T23Z (rotation: culture/sports/online this run)","not in the plan for 2026-10-31T00Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T23Z (desks_not_due)'","reason = 'not read: not due in the plan for 2026-10-31T00Z (desks_not_due)'")
R("VOL_DESKS = ['politics','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T23Z","4 reads;",
 "    f'get_posts_by_ids of the watch item of the plan for 2026-10-31T00Z (requests/plan.json was for 2026-10-30T23Z, so a fresh plan was built with tools/plan-reads.mjs --at 2026-10-30T23:12:00Z --print and saved as plan.json in the work folder), in its order and in batches of 100 (681 ids; its left_out counts 98 slowed, 0 over cap and 1 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 7 reads;")
SPAN("    'sources: references followed one hop from every post read","\n",
 "    'sources: references followed one hop from every post read, including attachments.media_source_tweet_id, using the expanded referenced posts (no screen reads: the plan cut screen); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Halloween\", \"NBA Cup\" and \"Stevens\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 2301Z: Halloween costume posts, the NBA Cup group play opening tonight, and Haley Stevens in the Michigan Senate race; Sam Altman and Constitutional Tribunal were read in 2202Z and Poland/Tusk/Polish are the Tribunal event already attached); all 19 desks; story clusters not in the plan; global floor/pace',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"is\" and \"you\" (2301Z used \"the\" and \"this\"), each quoted so X does not reject a bare stopword: (\"is\" lang:en is:quote -is:retweet), (\"you\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-24T01:00:00Z, end_time 2026-10-31T00:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-24T01:00Z to 2026-10-30T23:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-30T13:50:00Z (the post\\'s creation minute) and end_time 2026-10-30T14:10:00Z: (conversation_id:2116165917382255047 is:reply) and (quotes_of_tweet_id:2116165917382255047 -is:retweet); the plan gives context.top two reads, so one post: 2116165917382255047 (@pj_sekai notice on a change to account transfer by password, the biggest post new this run under 24 hours old at about 2.32M views); 7 replies and 25 quotes returned in the window',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
R("ANSWERED_EARLIER = {","ANSWERED_EARLIER = {'r-2026-10-30-01':'2026-10-30T2301Z',")
SPAN("            f'Day-band run (7:01 PM EDT","media descriptions. '\n",
"""            f'Day-band run (8:03 PM EDT Oct 30 / 00:03 UTC Oct 31, the 00Z slot, the first run of the UTC day; band allowance 42): requests/plan.json was for 2026-10-30T23Z, so a fresh plan for 2026-10-31T00Z was built with tools/plan-reads.mjs (--at 2026-10-30T23:12:00Z --print, saved to the work folder, requests/ not written) and followed top to bottom (42 reads listed, screen cut). {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the X day reset at 00:00Z), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 681 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 98 slowed flat posts in its left_out were not read. '
            f'Desks: all 19 the plan lists. Volume: sports, internet, life and offbeat (4 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Halloween", "NBA Cup" and "Stevens" (3 reads). rising.global: quote stream "is" and repost stream "you" (2 reads). context.top: pj_sekai 2116165917382255047 (2 reads). '
            f'Screen: cut by the plan; unread references left unread. '
            f'No open request asked (r-2026-10-30-01 answered in 2301Z). Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T23Z',","'plan': '2026-10-31T00Z',")
R("    'context': [{'post_id': '2116165938525741496',","    'context': [{'post_id': '2116165917382255047',")
R("f'{REPO}/capture/2026/10/30/2301Z.json'","f'{REPO}/capture/2026/10/31/0003Z.json'")
L("ANSWERS = [{'request_id': 'r-2026-10-30-01'","ANSWERS = []")
open('build_capture.py','w').write(s)
print('ok')
s=open('build_capture.py').read()
R("skip_nsfw |= {'2115964018154471765'}  # 2301Z:",
"""skip_nsfw |= {'2042013390474768680','2116229975997317556'}  # 0003Z: kummies4kitty 'doctor said fuck an emo girl' post (sexual wording, when in doubt); ZdendaXOF 'Halloween Fuck' post from the Halloween trend stream (sexual)
EXTRA_PRIVATE |= {'2115922155095589149'}  # 0003Z: MAGAVoice video of a young man (not a public figure, possibly a minor) walking up to the President
DESK_OVERRIDE_RUN.update({'2116238774271160510':'music','2116266502533902586':'business','2116296438942765394':'medicine','2116162031376015786':'medicine','2116289989914787912':'tech','2116262141745565826':'tech'})  # 0003Z desk fixes: dreamjeons Jungkook post is music; Gwynne_Shotwell SpaceX share gift is business; elonmusk Eli Lilly post and Lilly CEO DaveARicks bet are medicine; elonmusk and XOpenSource posts on reach-limit labels are tech
skip_nsfw |= {'2115964018154471765'}  # 2301Z:""")
open('build_capture.py','w').write(s)
print('ok2')
