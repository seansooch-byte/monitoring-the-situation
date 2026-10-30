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
R('"""Build capture/2026/10/30/1305Z.json from saved','"""Build capture/2026/10/30/1402Z.json from saved')
R("capture/work/2026-10-30T1305Z'","capture/work/2026-10-30T1402Z'")
R("RUN_ID = '2026-10-30T1305Z'","RUN_ID = '2026-10-30T1402Z'")
L("STARTED = ","STARTED = '2026-10-30T14:02:00Z'")
L("OBS_AT = ","OBS_AT = '2026-10-30T14:03:00Z'")
R("READS_BEFORE = 654","READS_BEFORE = 626")
L("READS_USED = 28","READS_USED = 37  # 1402Z: this run's 37 X calls (watch 4, desks 13, volume 5, trends 2, sensors 3, viral.global 3, rising.global 2, context.top 2, screen 3); the counter fell 626 to 589; no 429 or 503 refusals")
R("datetime(2026,10,30,13,6,tzinfo=timezone.utc).timestamp()  # 1305Z (","datetime(2026,10,30,14,3,tzinfo=timezone.utc).timestamp()  # 1402Z (1305Z used 13:06, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',\n    'quote_this': 'quote_this.txt',\n    'repost_is': 'repost_is.txt',",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',\n    'quote_you': 'quote_you.txt',\n    'repost_and': 'repost_and.txt',")
R("for batch in ('watch0','watch1','watch2','watch3','watch4'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("    'trend_redfriday': 'trend_redfriday.txt', 'trend_cartesia': 'trend_cartesia.txt', 'trend_fridayvibes': 'trend_fridayvibes.txt',\n    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',",
  "    'trend_halloweeneve': 'trend_halloweeneve.txt', 'trend_binance': 'trend_binance.txt', 'trend_friyay': 'trend_friyay.txt',\n    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',")
L("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1402Z: the 13 desks requests/plan.json for 2026-10-30T14Z lists (defense, disaster, business, science, ideas and life not due)")
R("""    ('quote_this','quote'),('repost_is','repost'),
    ('trend_redfriday','trend.RED Friday'),('trend_cartesia','trend.Cartesia Managed Agents'),('trend_fridayvibes','trend.#FridayVibes'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_halloweeneve','trend.Happy Halloween Eve'),('trend_binance','trend.Binance'),('trend_friyay','trend.Happy Friyay'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
# cartesia promo: stream not read this run
R("skip_nsfw |= _cartesia_promo()  #","# skip_nsfw |= _cartesia_promo()  # 1402Z: trend_cartesia not read this run;")
R("skip_nsfw |= {'2116040485445808350'}  # 1305Z:",
  "skip_nsfw |= {'2115810385571766384'}  # 1402Z: likely paid (america Texas early-vote ad, 1,957 likes on 2.55M views)\nskip_nsfw |= {'2115883668140912992'}  # 1402Z: sexual text (kodenamerick)\nskip_nsfw |= {'2116158816702046456'}  # 1402Z: _Snugglebuggie #diapergirl post (fetish content)\nskip_nsfw |= {'1985421939804934648','2115202433102250178','2115806058262188258'}  # 1402Z: likely paid (KalshiSports question post, 28 likes on 1.95M views; CSVC2026 vote ad, 125 likes on 439K views; IOInteractive HITMAN promo, 1,997 likes on 1.30M views)\nskip_nsfw |= {'2040267342563922278','2116126541407191327','2116163234474729745'}  # 1402Z: Naughty2534u link-only 'Happy FriYay' promo and LiftsBeach 'POTD' photo of a woman with a betting link (sexual promo, when in doubt); _chantel_lashae cash giveaway (spam)\nskip_nsfw |= {'2115874914842587461'}  # 1402Z: mybrothersoath 'daddy's going to kill himself' kitten post (self-harm wording, when in doubt)\nskip_nsfw |= {'2116040485445808350'}  # 1305Z:")
R("CTX_REPLIES = CTXR  # 1305Z: replies to nayibbukele 2115915319134855447 in its first 20 minutes, the three most liked kept",
  "CTX_REPLIES = CTXR  # 1402Z: replies to DiscussingFilm 2115821092950684009 in its first 20 minutes, the three most liked kept")
R("CTX_IDS = ['2115915319134855447'] + CTX_REPLIES","CTX_IDS = ['2115821092950684009'] + CTX_REPLIES")
R("DESK_OVERRIDE_RUN.update({_x:'world' for _x in ['2115915319134855447']+CTXR+CTXQ})  # 1305Z:",
  "DESK_OVERRIDE_RUN.update({_x:'world' for _x in ['2115915319134855447']})\nDESK_OVERRIDE_RUN.update({_x:'gaming' for _x in ['2115821092950684009']+CTXR+CTXQ})  # 1402Z: DiscussingFilm post on Jacksepticeye as a HITMAN elusive target and its context replies and quotes are gaming  # 1305Z:")
R("if _c.endswith('1305Z.json') and '/30/' in _c: continue","if _c.endswith('1402Z.json') and '/30/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("_last = '2026-10-30T1209Z'  # 1305Z: news/money/science last read in 1209Z","_last = '2026-10-30T1305Z'  # 1402Z: culture/sports/online last read in 1305Z")
R("not in requests/plan.json for 2026-10-30T13Z (rotation: culture/sports/online this run)","not in requests/plan.json for 2026-10-30T14Z (rotation: news/money/science this run)")
R("reason = 'not read: not due in requests/plan.json for 2026-10-30T13Z (desks_not_due)'","reason = 'not read: not due in requests/plan.json for 2026-10-30T14Z (desks_not_due)'")
R("VOL_DESKS = ['world','defense','justice','disaster','markets']","VOL_DESKS = ['business','ai','tech','science','medicine']")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T13Z","5 reads;",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-30T14Z, in its order and in batches of 100 (356 ids; the plan\\'s note: \"47 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 8 flat posts wait for their sixth run\"; its left_out counts 8 slowed, 0 over cap and 2 unavailable not listed); nothing added, dropped or reordered; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
SPAN("    'sources: references followed one hop from every post read and a second hop by id","\n",
 "    'sources: references followed one hop from every post read and a second hop by id, including attachments.media_source_tweet_id (screen: 3 reads by id, 137 unread references (1 not found) then 29 second-hop; nothing left to read); sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names \"Happy Halloween Eve\", \"Binance\" and \"Happy Friyay\" (\"<name> lang:en is:retweet\", newest first, 25 each; the plan gives viral.global three reads; they are top-ten US names with no posts attached in 1305Z; \"#AlconEntHasNoDignity\", \"#PapergamesRuinsCNCredibility\" and \"#上海纵容叠纸破坏两岸交流\" are one fan campaign read in 1209Z, and \"Cartesia Managed Agents\" was read in 1305Z)',\n")
SPAN("sweeps.append(sweep('rising.global'","25 each',\n",
 "sweeps.append(sweep('rising.global','discovery',None,\n    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words \"you\" and \"and\" (1305Z used \"this\" and \"is\"), each quoted so X does not reject a bare stopword: (\"you\" lang:en is:quote -is:retweet), (\"and\" lang:en is:retweet), newest first, 25 each',\n")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-23T15:00:00Z, end_time 2026-10-30T14:00:00Z, one read per desk for the 5 desks the plan lists (volume.business, volume.ai, volume.tech, volume.science, volume.medicine: counts 4 h old); each series is the 167 full hours 2026-10-23T15:00Z to 2026-10-30T13:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-29T15:00:00Z (the post\\'s creation minute) and end_time 2026-10-29T15:20:00Z: (conversation_id:2115821092950684009 is:reply) and (quotes_of_tweet_id:2115821092950684009 -is:retweet); the plan gives context.top two reads, so one post: 2115821092950684009 (@DiscussingFilm post on Jacksepticeye added to HITMAN as an elusive target, the biggest post new this run under 24 hours old at about 1.60M views once the america Texas early-vote ad at 2.55M views was left out as likely paid); 25 replies and 8 quotes, the three most liked of each kept',None,'ok',None,[i for i in CTX_IDS if i in posts_by_sel]))")
SPAN("            f'Day-band run (8:05 AM CT","f'No open requests. Not read: story clusters (not in the plan), media descriptions. '\n",
"""            f'Day-band run (9:02 AM CT Oct 30 / 14:02 UTC Oct 30, the 14Z slot; band allowance 42): requests/plan.json is for 2026-10-30T14Z (written 13:14Z after the 1305Z capture), so it was followed (37 reads listed) top to bottom. {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 356 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 8 slowed flat posts and 2 unavailable in its left_out were not read. '
            f'Desks: the 13 the plan lists (defense, disaster, business, science, ideas and life not due). Volume: business, ai, tech, science and medicine (5 reads). Trends US and worldwide (2 reads, max 50). Sensors news/money/science (3 reads, the rotation). '
            f'viral.global: trend names "Happy Halloween Eve", "Binance" and "Happy Friyay" (3 reads). rising.global: quote stream "you" and repost stream "and" (2 reads). context.top: DiscussingFilm 2115821092950684009 (2 reads). '
            f'Screen: 3 reads by id (137 unread references, 1 not found, then 29 second-hop). '
            f'No open requests. Not read: story clusters (not in the plan), media descriptions. '
""")
R("'plan': '2026-10-30T13Z',","'plan': '2026-10-30T14Z',")
R("    'context': [{'post_id': '2115915319134855447',","    'context': [{'post_id': '2115821092950684009',")
R("f'{REPO}/capture/2026/10/30/1305Z.json'","f'{REPO}/capture/2026/10/30/1402Z.json'")
open('build_capture.py','w').write(s)
print('ok')
