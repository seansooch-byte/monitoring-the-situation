p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1212Z.json from saved','capture/2026/10/28/1301Z.json from saved')
R("work/2026-10-28T1212Z'","work/2026-10-28T1301Z'")
R("RUN_ID = '2026-10-28T1212Z'","RUN_ID = '2026-10-28T1301Z'")
R("STARTED = '2026-10-28T12:12:00Z'","STARTED = '2026-10-28T13:01:00Z'")
R("OBS_AT = '2026-10-28T12:13:00Z'","OBS_AT = '2026-10-28T13:02:00Z'")
R("READS_BEFORE = 727","READS_BEFORE = 666")
a=s.index("READS_USED = 49  # 1212Z"); b=s.index("\n",a)
s=s[:a]+"READS_USED = 33  # 1301Z: this run's 33 X calls (the plan’s 33 reads, nothing cut); the counter fell 666 to 633; no 429 refusals"+s[b:]
R("datetime(2026,10,28,12,13,tzinfo=timezone.utc).timestamp()  # 1212Z (","datetime(2026,10,28,13,2,tzinfo=timezone.utc).timestamp()  # 1301Z (1212Z used 12:13, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',
    'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_alconent': 'trend_alconent.txt', 'trend_urda': 'trend_urda.txt', 'trend_lakers': 'trend_lakers.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'context_replies': 'context_replies.txt',
""","""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_tucker': 'trend_tucker.txt', 'trend_nunew': 'trend_nunew.txt', 'trend_skhynix': 'trend_skhynix.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'context_replies': 'context_replies.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):",2)
a=s.index("DUE = ['politics','world'"); b=s.index("\n",a)
s=s[:a]+"DUE = ['politics','entertainment','ideas','sports','internet','life']  # 1301Z: the plan (requests/plan.json for 2026-10-28T13Z) lists the four hourly desks plus ideas and life (every 4 h); the others are not due"+s[b:]
R("""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_alconent','trend.#AlconEntFailsHumanity'),('trend_urda','trend.Urda'),('trend_lakers','trend.Lakers'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_tucker','trend.Justin Tucker'),('trend_nunew','trend.#BORNTOBEByNuNew'),('trend_skhynix','trend.SK Hynix'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("""        if str(_x) == 'trend.Urda': return 'disaster'  # 1212Z""","""        if str(_x) == 'trend.Justin Tucker': return 'sports'  # 1301Z: Chiefs sign K Justin Tucker to the practice squad
        if str(_x) == 'trend.#BORNTOBEByNuNew': return 'music'  # 1301Z: Thai singer NuNew's special single "Born to Be"
        if str(_x) == 'trend.SK Hynix': return 'markets'  # 1301Z: SK Hynix Q3 earnings
        if str(_x) == 'trend.Urda': return 'disaster'  # 1212Z""")
R("if _c.endswith('1212Z.json') and '/28/' in _c: continue","if _c.endswith('1301Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T12Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T13Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"324 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 243 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 8 reads; fields","{len(watch_unavailable)} unavailable, 7 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Justin Tucker", "#BORNTOBEByNuNew" and "SK Hynix" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "Good Wednesday", "Hump Day", "#WednesdayMotivation" and "Happy Hump" are greetings; "#AlconEntFailsHumanity" and "Urda" had posts attached in 1212Z; "#中国北京应立刻追查姚润昊" and "#AlconEntLovesPPGsCowDung" are the same player campaign as "#AlconEntFailsHumanity"; "NUNEW SPECIAL SINGLE" is the same release as "#BORNTOBEByNuNew"; "Iryo" (12th) is the same Urda train collision, so "SK Hynix" (13th) took the third read); hourly desks politics/entertainment/sports/internet plus ideas and life; three screening reads by id (unread referenced, reply-parent and media-source posts, most pointed-at first, then a second hop; 2114804068011184133 Not Found, 2114811447004058030 Authorization Error); story clusters not in the plan; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "it" and "that", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1104Z'","        _last = '2026-10-28T1212Z'")
R("f'not in requests/plan.json for 2026-10-28T12Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T13Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = ('cut by requests/plan.json for 2026-10-28T12Z (due, but listed under cut to fit the day-band allowance of 42)' if d in {'life','ideas'} else 'not due: requests/plan.json for 2026-10-28T12Z')",
  "reason = 'not due: requests/plan.json for 2026-10-28T13Z (nothing cut)'")
R("VOL_DESKS = ['politics','world','defense','justice','disaster']","VOL_DESKS = ['markets','business','ai','tech','science']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T14:00:00Z, end_time 2026-10-28T13:00:00Z, one read per desk for the 5 desks the plan lists (volume.markets, volume.business, volume.ai, volume.tech, volume.science; counts 4 h old); each series is the 167 full hours 2026-10-21T14:00Z to 2026-10-28T12:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-27T18:23:13Z (the post\\'s creation) and end_time 2026-10-27T18:43:13Z: (conversation_id:2115147320408891516 is:reply) and (quotes_of_tweet_id:2115147320408891516 -is:retweet); the plan gives context.top two reads, so one post: 2115147320408891516 (@twinkpummeler, screenshots of the New York Times story on ChatGPT advice to cut a seizure drug, 5.79M views), the most viewed post new this run that is not old content or left out',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it; the quote read came back with no results, and the reply read returned only the author\\'s own follow-up reply with the article link (2115147467226587530), which is not a reaction, so none was kept',[]))"+s[b:]
a=s.index("            f'Day-band run (8:12 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (9:01 AM ET Oct 28 / 13:01 UTC Oct 28, the 13Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T13Z, 33 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 606 ids in its order, 7 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 243 flat posts the plan set aside and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, ideas, sports, internet and life (6 reads). Volume: markets, business, ai, tech and science (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Justin Tucker", "#BORNTOBEByNuNew" and "SK Hynix" (3 reads). rising.global: quote word "it" and repost word "that" (2 reads). context.top: 2 reads for 2115147320408891516 (no quotes; only the author\\'s own link reply). Screen: 3 reads by id. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1212Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1301Z.json'")
R("        'plan': '2026-10-28T12Z',","        'plan': '2026-10-28T13Z',")
R("    'context': [{'post_id': '2115188985010213103', 'replies': [], 'quotes': []}],","    'context': [{'post_id': '2115147320408891516', 'replies': [], 'quotes': []}],")
open(p,'w').write(s); print('ok')
