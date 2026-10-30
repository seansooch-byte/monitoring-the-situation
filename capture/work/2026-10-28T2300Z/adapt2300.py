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
R('capture/2026/10/28/2004Z.json from saved','capture/2026/10/28/2300Z.json from saved')
R("work/2026-10-28T2004Z'","work/2026-10-28T2300Z'")
R("RUN_ID = '2026-10-28T2004Z'","RUN_ID = '2026-10-28T2300Z'")
R("STARTED = '2026-10-28T20:04:00Z'","STARTED = '2026-10-28T23:00:00Z'")
R("OBS_AT = '2026-10-28T20:06:00Z'","OBS_AT = '2026-10-28T23:03:00Z'")
R("READS_BEFORE = 431","READS_BEFORE = 389")
L("READS_USED = 42  # 2004Z","READS_USED = 40  # 2300Z: this run's 40 X calls (the plan's 40 reads, screen 3 used in full); the counter fell 389 to 349; no 429 or 503 refusals")
R("datetime(2026,10,28,20,6,tzinfo=timezone.utc).timestamp()  # 2004Z (","datetime(2026,10,28,23,3,tzinfo=timezone.utc).timestamp()  # 2300Z (2004Z used 20:06, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',
    'quote_the': 'quote_the.txt',
    'repost_is': 'repost_is.txt',
    'trend_huerta': 'trend_huerta.txt', 'trend_gemini': 'trend_gemini.txt', 'trend_macbook': 'trend_macbook.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
""","""    'watch4': 'watch4.txt',
    'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_fofana': 'trend_fofana.txt', 'trend_sullivan': 'trend_sullivan.txt', 'trend_googl': 'trend_googl.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
L("DUE = ['politics','world','defense'","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']  # 2300Z: the 15 desks requests/plan.json for 2026-10-28T23Z lists (defense, disaster, business and science not due)")
R("""    ('quote_the','quote'),('repost_is','repost'),
    ('trend_huerta','trend.Dolores Huerta'),('trend_gemini','trend.Gemini 4 Carbon'),('trend_macbook','trend.MacBook Pro'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_you','quote'),('repost_and','repost'),
    ('trend_fofana','trend.Fofana'),('trend_sullivan','trend.Dan Sullivan'),('trend_googl','trend.$GOOGL'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("        if str(_x) == 'trend.Ernie': return 'sports'","        if str(_x) == 'trend.Fofana': return 'sports'  # 2300Z: Liverpool knock Chelsea out of the Carabao Cup on penalties; Wesley Fofana gave away a penalty and missed his own (Estevao, Gravenberch, Liverpool, Alonso, Joe Gomez, Tsimikas on the US list are the same match)\n        if str(_x) == 'trend.$GOOGL': return 'markets'  # 2300Z: Alphabet Q3 earnings\n        if str(_x) == 'trend.Ernie': return 'sports'")
R("if _c.endswith('2004Z.json') and '/28/' in _c: continue","if _c.endswith('2300Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
SPAN("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T20Z","{len(watch_ids)} ids read,",
 "    f'get_posts_by_ids of the watch item of the 2026-10-28T23Z plan (contract/PLAN.md; the committed requests/plan.json was for 2026-10-28T21Z, so the plan for this hour was made with tools/plan-reads.mjs --at 2026-10-28T22:59:00Z --print), in its order and in batches of 100 (the plan’s note: \"340 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 228 flat posts wait for their sixth run\"; its left_out also counts 5 unavailable posts not listed); nothing added, dropped or reordered; ")
R("{len(watch_unavailable)} unavailable, 8 reads; fields","{len(watch_unavailable)} unavailable, 5 reads; fields")
SPAN("sweeps.append(sweep('viral.global'","for g in ['news','money','science','culture','sports','online']:","""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Fofana", "Dan Sullivan" and "$GOOGL" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; these are three top-ten US names that had no posts attached in 2004Z (Ernie and Inside the NBA had posts in 2004Z; "Alaska" and "Peltola" are the same event as "Dan Sullivan", and "Estevao", "Gravenberch" and "Liverpool" the same match as "Fofana"); "Fofana" is Liverpool knocking Chelsea out of the Carabao Cup on penalties, "Dan Sullivan" is the NYT report and DOJ probe on the second Dan Sullivan on the Alaska Senate ballot, "$GOOGL" is Alphabet\\'s Q3 earnings); the 15 due desks; 3 screening reads by id (165 unread referenced posts in two reads, then 25 second-hop references in one), so every referenced post was read; story clusters not in the plan; screened with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "you" and "and" (2004Z used "the" and "is"), each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
""")
R("        _last = '2026-10-28T1904Z'","        _last = '2026-10-28T2004Z'")
R("f'not in requests/plan.json for 2026-10-28T20Z (rotation: news/money/science this run); last read in {_last}'","f'not in the 2026-10-28T23Z plan (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T20Z (only screen was cut)'","reason = 'not due: the 2026-10-28T23Z plan (nothing cut)'")
R("VOL_DESKS = ['politics','world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
L("sweeps.append(sweep('volume.desks'","sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-22T00:00:00Z, end_time 2026-10-28T23:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science; counts 6 h old); each series is the 167 full hours 2026-10-22T00:00Z to 2026-10-28T22:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))")
L("sweeps.append(sweep('context.top'","sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-28T16:33:00Z (the post\\'s creation, 16:33) and end_time 2026-10-28T16:53:00Z: (conversation_id:2115482148803412332 is:reply) and (quotes_of_tweet_id:2115482148803412332 -is:retweet); the plan gives context.top two reads, so one post: 2115482148803412332 (@DerrickEvans4WV, iPhone accessibility setting tip, 3.75M views), the most viewed post new this run; 2 replies and no quotes came back in the window; the replies are kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))")
SPAN("            f'Day-band run (3:04 PM CT","            f'No open requests.","""            f'Day-band run (6:00 PM CT Oct 28 / 23:00 UTC Oct 28, the 23Z slot, last run of the UTC day; band allowance 42): the committed requests/plan.json was for 2026-10-28T21Z (no 21Z or 22Z capture was made), so per contract/PLAN.md the plan for this hour was made with node tools/plan-reads.mjs --at 2026-10-28T22:59:00Z --print (for_run 2026-10-28T23Z, 40 reads, nothing cut) and executed top to bottom; requests/plan.json was not changed; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 487 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 228 flat posts the plan set aside and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, ideas, sports, internet, life and offbeat (15 reads; defense, disaster, business and science not due). Volume: markets, business, ai, tech and science (5 reads, counts 6 h old). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Fofana", "Dan Sullivan" and "$GOOGL" (3 reads). rising.global: quote word "you" and repost word "and" (2 reads). context.top: 2 reads for 2115482148803412332 (2 replies and no quotes in the window; the replies kept). Screen: 3 reads by id (165 referenced posts, then 25 second-hop references). '
""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/2004Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/2300Z.json'")
R("        'plan': '2026-10-28T20Z',","        'plan': '2026-10-28T23Z',")
R("    'context': [{'post_id': '2115397320292663758',","    'context': [{'post_id': '2115482148803412332',")
SPAN("CTX_REPLIES = ['2115399226301493746']","CTX_IDS = CTX_REPLIES + CTX_QUOTES","CTX_REPLIES = ['2115483912944361783','2115482291560763811']  # 2300Z: the two replies to DerrickEvans4WV 2115482148803412332 in its first 20 minutes\nCTX_QUOTES = []  # 2300Z: no quotes in the window\n")
R("2004Z: the context post is internet)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'internet',",
  "2004Z: internet; 2300Z: the context post is tech)\nfor _i in CTX_IDS:\n    _p = posts_by_id[_i]\n    _u = users_by_id.get(_p.get('author_id')) or {}\n    _h = _u.get('username')\n    take(((metrics(_p)['views'] or 0), _i, 'tech',")
open(p,'w').write(s); print('ok')
