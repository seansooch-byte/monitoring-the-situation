p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/0406Z.json from saved','capture/2026/10/28/0501Z.json from saved')
R("work/2026-10-28T0406Z'","work/2026-10-28T0501Z'")
R("RUN_ID = '2026-10-28T0406Z'","RUN_ID = '2026-10-28T0501Z'")
R("STARTED = '2026-10-28T04:06:00Z'","STARTED = '2026-10-28T05:01:00Z'")
R("OBS_AT = '2026-10-28T04:07:00Z'","OBS_AT = '2026-10-28T05:02:00Z'")
R("READS_BEFORE = 915","READS_BEFORE = 871")
R("datetime(2026,10,28,4,7,tzinfo=timezone.utc).timestamp()  # 0406Z (","datetime(2026,10,28,5,2,tzinfo=timezone.utc).timestamp()  # 0501Z (0406Z used 04:07, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt',
    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_cooperpratt': 'trend_cooperpratt.txt', 'trend_worldseries': 'trend_worldseries.txt', 'trend_ianseymour': 'trend_ianseymour.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_drohan': 'trend_drohan.txt', 'trend_game5': 'trend_game5.txt', 'trend_benwilliamson': 'trend_benwilliamson.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
R("    'trends_us': 'trends_us.txt',\n","    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',\n")
R("DUE = [d['id'] for d in json.load(open(f'{REPO}/contract/desks.json'))['desks'] ]  # 0406Z top-up: every desk was due (hourly four plus the two- and four-hour desks)",
  "DUE = ['politics','entertainment','sports','internet']  # 0501Z: the plan (requests/plan.json for 2026-10-28T05Z) lists the four hourly desks; the others were swept in 0406Z and are not due")
R("""    ('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_cooperpratt','trend.Cooper Pratt'),('trend_worldseries','trend.#WorldSeries'),('trend_ianseymour','trend.Ian Seymour'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('repost_you','repost'),
    ('trend_drohan','trend.Drohan'),('trend_game5','trend.Game 5'),('trend_benwilliamson','trend.Ben Williamson'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""        if str(_x) in ('trend.Cooper Pratt','trend.#WorldSeries','trend.Ian Seymour'): return 'sports'""",
"""        if str(_x) in ('trend.Drohan','trend.Game 5','trend.Ben Williamson'): return 'sports'  # 0501Z: World Series (Brewers-Rays) and NFL names
        if str(_x) in ('trend.Cooper Pratt','trend.#WorldSeries','trend.Ian Seymour'): return 'sports'""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("if _c.endswith('0406Z.json') and '/28/' in _c: continue","if _c.endswith('0501Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("trends = parse_trends(raw['trends_us'], 'US')","trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')")
# watch sweep method
a=s.index("f'get_posts_by_ids of requests/watch.json ({len(watch_json)} ids)"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T05Z (contract/PLAN.md), in its order and in batches of 100: {len(watch_json)} ids from requests/watch.json, then posts under 6 hours old, then posts gaining 2 percent; the plan set aside 221 flat posts waiting for their sixth run and 4 unavailable posts; nothing added, dropped or reordered; "+s[b:]
R("unavailable, 6 reads; fields created_at","unavailable, 4 reads; fields created_at")
R("sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-23T0002Z',[]))",
  "sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))")
TR='trend names "Drohan", "Game 5" and "Ben Williamson" ("<name> lang:en is:retweet", newest first, 25 each; of the top-ten US names, "Cooper Pratt" and "#WorldSeries" were attached in 0406Z and "#dwts" in 0101Z; "Rays", "Brewers", "Joe Davis" and "Joey Ortiz" are the same Brewers-Rays World Series as "Game 5" and "Drohan" and were not read, the plan giving viral.global three reads)'
a=s.index("'sources: references followed one hop"); b=s.index("\n",a)
s=s[:a]+"'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); "+TR+"; the rising.global quote and repost streams; hourly desks politics/entertainment/sports/internet; one screening read by id: 94 unread referenced, reply-parent and media-source posts, most pointed-at first; story clusters not in the plan; screened by id with global floor/pace',"+s[b:]
R("""    '2 quote pages + 1 repost page (budget), common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each',""",
  """    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "is" and "you", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each',""")
R("        _last = '2026-10-28T0305Z'","        _last = '2026-10-28T0406Z'")
R("f'not read this run (rotation: news/money/science read this run; kept to about 20 reads to pace the daily budget); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T05Z (rotation: culture/sports/online this run); last read in {_last}'")
R("f'not in this run rotation of three groups (kept to about 20 reads to pace the daily budget); last read in {_last}'","f'not in the plan this run (three groups a run in rotation); last read in {_last}'")
a=s.index("        reason = 'four-hour desk due since 07:08Z"); b=s.index("\n",a)
s=s[:a]+"        reason = 'not due: swept in 2026-10-28T0406Z; listed under left_out.desks_not_due in requests/plan.json for 2026-10-28T05Z'"+s[b:]
R("VOL_DESKS = ['politics','world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
R("start_time 2026-10-21T05:00:00Z, end_time 2026-10-28T04:00:00Z, one read per desk for 5 desks this run (rotation slot 0 of 4 in capture/CAPABILITIES.md: politics, world, defense, justice, disaster); each series is the 167 full hours 2026-10-21T05:00Z to 2026-10-28T03:00Z",
  "start_time 2026-10-21T06:00:00Z, end_time 2026-10-28T05:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science, never counted before); each series is the 167 full hours 2026-10-21T06:00Z to 2026-10-28T04:00Z")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0406Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/0501Z.json'")
R("        'requests_rev': REQUESTS_REV,\n    },","        'requests_rev': REQUESTS_REV,\n        'reads': READS_USED,\n        'reads_left': READS_AFTER,\n        'plan': '2026-10-28T05Z',\n    },")
open(p,'w').write(s); print('ok')
