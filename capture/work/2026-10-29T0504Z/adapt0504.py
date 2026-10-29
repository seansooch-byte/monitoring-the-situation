p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
def L(start,new):
    global s
    a=s.index(start); b=s.index("\n",a); s=s[:a]+new+s[b:]
def SPAN(start,end,new):
    global s
    a=s.index(start); b=s.index(end,a); s=s[:a]+new+s[b:]
R('capture/2026/10/29/0401Z.json from saved','capture/2026/10/29/0504Z.json from saved')
R("work/2026-10-29T0401Z'","work/2026-10-29T0504Z'")
R("RUN_ID = '2026-10-29T0401Z'","RUN_ID = '2026-10-29T0504Z'")
R("STARTED = '2026-10-29T04:01:00Z'","STARTED = '2026-10-29T05:04:00Z'")
R("OBS_AT = '2026-10-29T04:03:00Z'","OBS_AT = '2026-10-29T05:05:00Z'")
R("READS_BEFORE = 864","READS_BEFORE = 828")
L("READS_USED = 36  # 0401Z","READS_USED = 39  # 0504Z: this run's 39 X calls, the plan's 39 reads (all 3 screen reads used: 100 and 52 unread references, then 28 second-hop references); the counter fell 828 to 789; no 429 or 503 refusals")
R("datetime(2026,10,29,4,3,tzinfo=timezone.utc).timestamp()  # 0401Z (","datetime(2026,10,29,5,5,tzinfo=timezone.utc).timestamp()  # 0504Z (0401Z used 04:03, ")
R("    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',\n","    'watch4': 'watch4.txt', 'watch5': 'watch5.txt',\n")
R("""    'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_brewers': 'trend_brewers.txt', 'trend_aew': 'trend_aew.txt', 'trend_crew': 'trend_crew.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_winourway': 'trend_winourway.txt', 'trend_contreras': 'trend_contreras.txt', 'trend_clippers': 'trend_clippers.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""")
L("DUE = ['politics','defense','disaster'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 0504Z: the 13 desks requests/plan.json for 2026-10-29T05Z lists")
R("""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_brewers','trend.Brewers'),('trend_aew','trend.#AEWDynamite'),('trend_crew','trend.#ThisIsMyCrew'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_my','quote'),('repost_it','repost'),
    ('trend_winourway','trend.#WinOurWay'),('trend_contreras','trend.William Contreras'),('trend_clippers','trend.Clippers'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("        if str(_x) in ('trend.Brewers','trend.#AEWDynamite','trend.#ThisIsMyCrew'): return 'sports'  # 0401Z","        if str(_x) in ('trend.#WinOurWay','trend.William Contreras','trend.Clippers'): return 'sports'  # 0504Z: Brewers World Series title (#WinOurWay, William Contreras) and the Clippers\n        if str(_x) in ('trend.Brewers','trend.#AEWDynamite','trend.#ThisIsMyCrew'): return 'sports'  # 0401Z")
R("if _c.endswith('0401Z.json') and '/29/' in _c: continue","if _c.endswith('0504Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T04Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T05Z, in its order and in batches of 100 (501 ids; its left_out counts 247 slowed flat posts and 5 unavailable posts not listed); nothing added, dropped or reordered; ")
R("unavailable, 8 reads; fields","unavailable, 6 reads; fields")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "#WinOurWay", "William Contreras" and "Clippers" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the first three top-ten US names that had no posts attached in 0401Z; "Brewers", "#WinOurWay", "#ThisIsMyCrew", "Bob Uecker", "William Contreras", "Gary Sanchez", "Christian Yelich", "World Champs" and "Pat Murphy" are all one event: the Milwaukee Brewers won the World Series); the 13 due desks; 3 screening reads by id (100 and 52 unread referenced posts, then 28 unread second-hop references); story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "my" and "it" (0401Z used "you" and "and"), each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-29T0307Z'","        _last = '2026-10-29T0401Z'")
R("f'not in requests/plan.json for 2026-10-29T04Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T05Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-29T04Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-29T05Z (nothing cut)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['politics','sports','internet','life','offbeat']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T06:00:00Z, end_time 2026-10-29T05:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.sports, volume.internet, volume.life, volume.offbeat: counts 4 h old); each series is the 167 full hours 2026-10-22T06:00Z to 2026-10-29T04:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T14:00:00Z (the post\\'s creation, 14:00:23) and end_time 2026-10-28T14:20:00Z: (conversation_id:2115443563655754171 is:reply) and (quotes_of_tweet_id:2115443563655754171 -is:retweet); the plan gives context.top two reads, so one post: 2115443563655754171 (@Dexerto on passengers kicked off an endless cruise, 2.7M views), the most viewed post new this run; the five most liked replies (15 in the window) and the one quote in the window are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
SPAN("            f'Day-band run (11:01 PM CT Oct 28","            f'No open requests.","""            f'Day-band run (12:04 AM CT Oct 29 / 05:04 UTC Oct 29, the 05Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T05Z, 39 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 501 ids in its order, 6 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 247 slowed flat posts and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (13 reads; the other 6 not due). Volume: politics, sports, internet, life and offbeat (5 reads). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "#WinOurWay", "William Contreras" and "Clippers" (3 reads). rising.global: quote word "my" and repost word "it" (2 reads). context.top: 2 reads for 2115443563655754171. Screen: 3 reads by id (100 and 52 referenced posts, then 28 second-hop references). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0401Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0504Z.json'")
R("        'plan': '2026-10-29T04Z',","        'plan': '2026-10-29T05Z',")
R("    'context': [{'post_id': '2115557099891761437',","    'context': [{'post_id': '2115443563655754171',")
SPAN("CTX_REPLIES = ['2115560504630317269'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115446958747971592','2115443565333533091','2115446424695353499','2115446806356144572','2115444087591502325']  # 0504Z: five most liked replies to Dexerto 2115443563655754171 in its first 20 minutes (15 in the window)\nCTX_QUOTES = ['2115444146374680844']  # 0504Z: the one quote in the window\n")
R("0401Z: the context post is tech)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'tech',",
  "0401Z: tech; 0504Z: the context post is business)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'business',")
open(p,'w').write(s); print('ok')
# appended: watch batches 0-5
s=open(p).read()
R("('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7')","('watch0','watch1','watch2','watch3','watch4','watch5')",2)
open(p,'w').write(s); print('ok2')
# appended 2: desk fixes after review
s=open(p).read()
_a="DESK_OVERRIDE_RUN.update({'2115433479345176884':'entertainment'"
_i=s.index(_a); _j=s.index("\n",_i)
s=s[:_j+1]+"DESK_OVERRIDE_RUN.update({'2115459788108714244':'sports','2115443563655754171':'business','2113978144655126613':'internet','2114529911314473395':'world','2115513582641389772':'justice','2014638710420275639':'life'})  # 0504Z: Kompany shoulder dislocation is sports; Dexerto endless-cruise post is business like its context replies; India most-liked-posts list is internet; Brazil electoral court statement is world; Hennepin county attorney post is justice; messedupfoods food clip is life\n"+s[_j+1:]
open(p,'w').write(s); print('ok3')
