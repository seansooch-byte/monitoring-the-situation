p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1406Z.json from saved','capture/2026/10/28/1511Z.json from saved')
R("work/2026-10-28T1406Z'","work/2026-10-28T1511Z'")
R("RUN_ID = '2026-10-28T1406Z'","RUN_ID = '2026-10-28T1511Z'")
R("STARTED = '2026-10-28T14:06:00Z'","STARTED = '2026-10-28T15:11:00Z'")
R("OBS_AT = '2026-10-28T14:07:00Z'","OBS_AT = '2026-10-28T15:12:00Z'")
R("READS_BEFORE = 633","READS_BEFORE = 596")
a=s.index("READS_USED = 37  # 1406Z"); b=s.index("\n",a)
s=s[:a]+"READS_USED = 27  # 1511Z: this run's 27 X calls (the plan's 28 reads less one screening read); the counter fell 596 to 569; no 429 refusals"+s[b:]
R("datetime(2026,10,28,14,7,tzinfo=timezone.utc).timestamp()  # 1406Z (","datetime(2026,10,28,15,12,tzinfo=timezone.utc).timestamp()  # 1511Z (1406Z used 14:07, ")
R("""    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_fomc': 'trend_fomc.txt', 'trend_butker': 'trend_butker.txt', 'trend_firstresponders': 'trend_firstresponders.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
    'context_replies': 'context_replies.txt',
""","""    'watch4': 'watch4.txt',
    'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_toledo': 'trend_toledo.txt', 'trend_jlaw': 'trend_jlaw.txt', 'trend_robin': 'trend_robin.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
    'context_replies': 'context_replies.txt', 'context_quotes': 'context_quotes.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2','watch3','watch4'):",2)
a=s.index("DUE = ['politics','world'"); b=s.index("\n",a)
s=s[:a]+"DUE = ['politics','entertainment','sports','internet']  # 1511Z: the plan (requests/plan.json for 2026-10-28T15Z) lists the four hourly desks; the two-hour desks were swept in 1406Z and are not due"+s[b:]
R("""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_fomc','trend.FOMC'),('trend_butker','trend.Butker'),('trend_firstresponders','trend.#NationalFirstRespondersDay'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""","""    ('quote_this','quote'),('repost_you','repost'),
    ('trend_toledo','trend.Toledo'),('trend_jlaw','trend.Jennifer Lawrence'),('trend_robin','trend.Nico Robin'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
R("""        if str(_x) == 'trend.FOMC': return 'markets'  # 1406Z""","""        if str(_x) == 'trend.Toledo': return 'disaster'  # 1511Z: two high-speed trains collided near Toledo, Spain (Adamuz/ADIF/Oscar Puente on the worldwide list are the same event)
        if str(_x) == 'trend.Jennifer Lawrence': return 'entertainment'  # 1511Z: Jennifer Lawrence on Call Her Daddy (plastic surgery, Hunger Games return)
        if str(_x) == 'trend.Nico Robin': return 'entertainment'  # 1511Z: One Piece character (anime)
        if str(_x) == 'trend.FOMC': return 'markets'  # 1406Z""")
R("if _c.endswith('1406Z.json') and '/28/' in _c: continue","if _c.endswith('1511Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T14Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T15Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"326 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 232 flat posts wait for their sixth run\"; its left_out also counts 5 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 4 reads; fields","{len(watch_unavailable)} unavailable, 5 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each, their own sweeps); quote and repost streams (rising.global); trend names "Toledo", "Jennifer Lawrence" and "Nico Robin" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "Good Wednesday" and "Hump Day" are greetings, "Justin Tucker", "Butker" and "The Chiefs" are the Tucker signing streamed in 1301Z and 1406Z, "FOMC" was streamed in 1406Z, "#NationalFirstRespondersDay" in 1406Z and "#CARDCRUSH" is a promotion; "Toledo" is the high-speed train collision near Toledo, Spain, and "Adamuz", "Óscar Puente" and "ADIF" on the worldwide list are the same event); hourly desks politics/entertainment/sports/internet; two screening reads by id (86 unread referenced, reply-parent and media-source posts, most pointed-at first, then 15 found on the second hop; none Not Found); story clusters not in the plan; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "this" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("you" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1301Z'","        _last = '2026-10-28T1406Z'")
R("f'not in requests/plan.json for 2026-10-28T14Z (rotation: news/money/science this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T15Z (rotation: culture/sports/online this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T14Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-28T15Z (nothing cut)'")
R("VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']","VOL_DESKS = ['sports','internet','life','offbeat']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T16:00:00Z, end_time 2026-10-28T15:00:00Z, one read per desk for the 4 desks the plan lists (volume.sports, volume.internet, volume.life, volume.offbeat; counts 4 h old); each series is the 167 full hours 2026-10-21T16:00Z to 2026-10-28T14:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-27T16:21:00Z (the post\\'s creation, 16:21:xx) and end_time 2026-10-27T16:41:00Z: (conversation_id:2115116782046372003 is:reply) and (quotes_of_tweet_id:2115116782046372003 -is:retweet); the plan gives context.top two reads, so one post: 2115116782046372003 (@nypost, Jennifer Lawrence on past plastic surgery and facelift plans, 3.68M views), the most viewed post new this run that is not old content (the larger badpostseydoux 2115162550572827024 is a fan account reposting an ELLE UK clip); 24 replies and 2 quote posts came back; the five most liked replies and both quote posts kept',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it',CTX_IDS))"+s[b:]
a=s.index("            f'Day-band run (10:06 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (11:11 AM ET Oct 28 / 15:11 UTC Oct 28, the 15Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T15Z, 28 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 or 503 refusals. '
            f'Watch: the plan\\'s 409 ids in its order, 5 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 232 flat posts the plan set aside and the 5 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, entertainment, sports and internet (4 reads; the two-hour desks are not due). Volume: sports, internet, life and offbeat (4 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors culture/sports/online (3 reads). viral.global: trend names "Toledo", "Jennifer Lawrence" and "Nico Robin" (3 reads). rising.global: quote word "this" and repost word "you" (2 reads). context.top: 2 reads for 2115116782046372003 (24 replies and 2 quotes in the window; 5 replies and 2 quotes kept). Screen: 2 reads by id (86 ids, then 15 on the second hop; the plan allowed 3). '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1406Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1511Z.json'")
R("        'plan': '2026-10-28T14Z',","        'plan': '2026-10-28T15Z',")
R("    'context': [{'post_id': '2115089006769930458', 'replies': [], 'quotes': []}],","    'context': [{'post_id': '2115116782046372003', 'replies': [i for i in CTX_REPLIES if i in posts_by_sel], 'quotes': [i for i in CTX_QUOTES if i in posts_by_sel]}],")
# context picks: taken like request picks (no floor, no author cap), not counted as viral
R("""# 5) request picks (1800Z: none read)
for _r,_ids in REQ_PICKS.items():""","""# 4b) context picks (1511Z)
for _i in CTX_IDS:
    _p = posts_by_id[_i]
    _u = users_by_id.get(_p.get('author_id')) or {}
    _h = _u.get('username')
    take(((metrics(_p)['views'] or 0), _i, 'entertainment', 'context', kind_guess(_u,_h), _h, source_of[_i] or {'context.top'}), count_author=False)
# 5) request picks (1800Z: none read)
for _r,_ids in REQ_PICKS.items():""")
R("REQ_PICKS = {}\n","REQ_PICKS = {}\nCTX_REPLIES = ['2115118185217147012','2115121384816800043','2115118875432132976','2115118020985327853','2115117369681219776']  # 1511Z: five most liked replies to nypost 2115116782046372003 in its first 20 minutes\nCTX_QUOTES = ['2115118321607827913','2115121402382848044']  # 1511Z: both quote posts in the window\nCTX_IDS = CTX_REPLIES + CTX_QUOTES\n")
R("    if reason == 'request':\n        continue\n    viral_ids.append(pid)","    if reason in ('request','context'):\n        continue\n    viral_ids.append(pid)")
R("""for _r,_ids in REQ_PICKS.items():
    for _i in _ids:
        if _i not in ordered_ids: ordered_ids.append(_i)""","""for _r,_ids in REQ_PICKS.items():
    for _i in _ids:
        if _i not in ordered_ids: ordered_ids.append(_i)
for _i in CTX_IDS:
    if _i not in ordered_ids: ordered_ids.append(_i)""")
open(p,'w').write(s); print('ok')
