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
R('capture/2026/10/29/0307Z.json from saved','capture/2026/10/29/0401Z.json from saved')
R("work/2026-10-29T0307Z'","work/2026-10-29T0401Z'")
R("RUN_ID = '2026-10-29T0307Z'","RUN_ID = '2026-10-29T0401Z'")
R("STARTED = '2026-10-29T03:07:00Z'","STARTED = '2026-10-29T04:01:00Z'")
R("OBS_AT = '2026-10-29T03:09:00Z'","OBS_AT = '2026-10-29T04:03:00Z'")
R("READS_BEFORE = 903","READS_BEFORE = 864")
L("READS_USED = 39  # 0307Z","READS_USED = 36  # 0401Z: this run's 36 X calls, the plan's 36 reads (all 3 screen reads used: 100 and 31 unread references, then 24 second-hop references); the counter fell 864 to 828; no 429 or 503 refusals")
R("datetime(2026,10,29,3,9,tzinfo=timezone.utc).timestamp()  # 0307Z (","datetime(2026,10,29,4,3,tzinfo=timezone.utc).timestamp()  # 0401Z (0307Z used 03:09, ")
R("    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n",
  "    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',\n    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',\n")
R("""    'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_aminata': 'trend_aminata.txt', 'trend_clarkson': 'trend_clarkson.txt', 'trend_lee': 'trend_lee.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""","""    'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_brewers': 'trend_brewers.txt', 'trend_aew': 'trend_aew.txt', 'trend_crew': 'trend_crew.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""")
L("DUE = ['politics','world','justice','markets'","DUE = ['politics','defense','disaster','business','science','entertainment','sports','internet']  # 0401Z: the 8 desks requests/plan.json for 2026-10-29T04Z lists")
R("""    ('quote_this','quote'),('repost_is','repost'),
    ('trend_aminata','trend.Queen Aminata'),('trend_clarkson','trend.Clarkson'),('trend_lee','trend.Charles Lee'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_brewers','trend.Brewers'),('trend_aew','trend.#AEWDynamite'),('trend_crew','trend.#ThisIsMyCrew'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("        if str(_x) in ('trend.Queen Aminata','trend.Clarkson','trend.Charles Lee'): return 'sports'  # 0307Z","        if str(_x) in ('trend.Brewers','trend.#AEWDynamite','trend.#ThisIsMyCrew'): return 'sports'  # 0401Z: Brewers win the World Series (#ThisIsMyCrew is the Brewers hashtag); AEW Dynamite\n        if str(_x) in ('trend.Queen Aminata','trend.Clarkson','trend.Charles Lee'): return 'sports'  # 0307Z")
R("if _c.endswith('0307Z.json') and '/29/' in _c: continue","if _c.endswith('0401Z.json') and '/29/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T03Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-29T04Z, in its order and in batches of 100 (722 ids; its left_out counts 318 slowed flat posts and 7 unavailable posts not listed); nothing added, dropped or reordered; ")
R("unavailable, 4 reads; fields","unavailable, 8 reads; fields")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Brewers", "#AEWDynamite" and "#ThisIsMyCrew" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are the first three top-ten US names that had no posts attached in 0307Z; "Brewers", "#ThisIsMyCrew", "#WinOurWay", "Bob Uecker", "William Contreras", "Gary Sanchez", "World Champs" and "Wild Bill" are all one event: the Milwaukee Brewers won the World Series over the Tampa Bay Rays); the 8 due desks; 3 screening reads by id (100 and 31 unread referenced posts, then 24 unread second-hop references); story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "you" and "and" (0307Z used "this" and "is"), each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-29T0159Z'","        _last = '2026-10-29T0307Z'")
R("f'not in requests/plan.json for 2026-10-29T03Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-29T04Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-29T03Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-29T04Z (nothing cut)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T05:00:00Z, end_time 2026-10-29T04:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas: counts 4 h old); each series is the 167 full hours 2026-10-22T05:00Z to 2026-10-29T03:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T21:31:00Z (the post\\'s creation, 21:31:32) and end_time 2026-10-28T21:51:00Z: (conversation_id:2115557099891761437 is:reply) and (quotes_of_tweet_id:2115557099891761437 -is:retweet); the plan gives context.top two reads, so one post: 2115557099891761437 (@united on Starlink installs, 1.5M views), the most viewed post new this run; the five most liked replies (25 in the window) and five most liked quotes (8 in the window) are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
SPAN("            f'Day-band run (10:07 PM CT Oct 28","            f'No open requests.","""            f'Day-band run (11:01 PM CT Oct 28 / 04:01 UTC Oct 29, the 04Z slot; band allowance 42): followed requests/plan.json (for_run 2026-10-29T04Z, 36 reads, nothing cut) top to bottom; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 722 ids in its order, 8 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 318 slowed flat posts and the 7 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, defense, disaster, business, science, entertainment, sports and internet (8 reads; the other 11 not due). Volume: medicine, entertainment, music, gaming and ideas (5 reads). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "Brewers", "#AEWDynamite" and "#ThisIsMyCrew" (3 reads). rising.global: quote word "you" and repost word "and" (2 reads). context.top: 2 reads for 2115557099891761437. Screen: 3 reads by id (100 and 31 referenced posts, then 24 second-hop references). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0307Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/29/0401Z.json'")
R("        'plan': '2026-10-29T03Z',","        'plan': '2026-10-29T04Z',")
R("    'context': [{'post_id': '2115291395733049422',","    'context': [{'post_id': '2115557099891761437',")
SPAN("CTX_REPLIES = ['2115296146117874151'","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115560504630317269','2115560429942423916','2115561141619560748','2115561496914612455','2115560412267573428']  # 0401Z: five most liked replies to united 2115557099891761437 in its first 20 minutes\nCTX_QUOTES = ['2115560036131102985','2115560414520148268','2115561985354179065','2115561292173910380','2115560752081977632']  # 0401Z: five most liked quotes in the window (8 in it)\n")
R("0307Z: the context post is business)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'business',",
  "0307Z: business; 0401Z: the context post is tech)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'tech',")
open(p,'w').write(s); print('ok')

# desk fixes (applied after build review)
s=open(p).read()
_i=s.index("\n", s.index("DESK_OVERRIDE_RUN.update({'2109945014260244942':'gaming'"))
s=s[:_i]+"\nDESK_OVERRIDE_RUN.update({'2115433479345176884':'entertainment','2115452003887296938':'medicine','1714332256393969914':'gaming','2113272705982054613':'politics','2115444013364826346':'politics','2115280652719333425':'justice'})  # 0401Z: Rihanna Fenty interview is entertainment; phalloplasty history reply is medicine; FNAF power-outage clip is gaming; midterms ground-game post and the reply to Modi on voter lists are politics; NYPD ending an Israeli surveillance contract is justice"+s[_i:]
open(p,'w').write(s); print('desk ok')
