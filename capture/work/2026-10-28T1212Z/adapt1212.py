p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1104Z.json from saved','capture/2026/10/28/1212Z.json from saved')
R("work/2026-10-28T1104Z'","work/2026-10-28T1212Z'")
R("RUN_ID = '2026-10-28T1104Z'","RUN_ID = '2026-10-28T1212Z'")
R("STARTED = '2026-10-28T11:04:00Z'","STARTED = '2026-10-28T12:12:00Z'")
R("OBS_AT = '2026-10-28T11:05:00Z'","OBS_AT = '2026-10-28T12:13:00Z'")
R("READS_BEFORE = 752","READS_BEFORE = 727")
R("READS_USED = 20  # 1104Z: this run's 20 X calls; the counter fell 752 to 727 because the 7:03 AM ET daily briefing spent 5 reads on the shared counter during the run; no 429 refusals",
  "READS_USED = 49  # 1212Z: this run's 49 X calls (42 planned; 5 volume calls refused as invalid because start_time 2026-10-21T12:00Z was older than the 7-day window, and 1 volume call returned 503, then all 6 redone); the counter fell 727 to 666 because about 12 other reads hit the shared counter during the run; no 429 refusals")
R("datetime(2026,10,28,11,5,tzinfo=timezone.utc).timestamp()  # 1104Z (","datetime(2026,10,28,12,13,tzinfo=timezone.utc).timestamp()  # 1212Z (1104Z used 11:05, ")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'trend_iryo': 'trend_iryo.txt', 'trend_octavia': 'trend_octavia.txt', 'trend_striker': 'trend_striker.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt', 'watch7': 'watch7.txt',
    'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_alconent': 'trend_alconent.txt', 'trend_urda': 'trend_urda.txt', 'trend_lakers': 'trend_lakers.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'context_replies': 'context_replies.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6','watch7'):",2)
R("DUE = ['politics','entertainment','sports','internet']  # 1104Z: the plan (requests/plan.json for 2026-10-28T11Z) lists the four hourly desks; every other desk is due but cut",
  "DUE = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1212Z: the plan (requests/plan.json for 2026-10-28T12Z) lists these 17 desks; life and ideas are due but cut")
R("""    ('trend_iryo','trend.Iryo'),('trend_octavia','trend.Octavia'),('trend_striker','trend.Striker'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_and','quote'),('repost_my','repost'),
    ('trend_alconent','trend.#AlconEntFailsHumanity'),('trend_urda','trend.Urda'),('trend_lakers','trend.Lakers'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("""        if str(_x) == 'trend.Iryo': return 'disaster'""","""        if str(_x) == 'trend.Urda': return 'disaster'  # 1212Z: the same Spain high-speed train collision (near Urda, Toledo)
        if str(_x) == 'trend.Lakers': return 'sports'  # 1212Z: Blazers beat the Lakers 136-129
        if str(_x) == 'trend.#AlconEntFailsHumanity': return 'gaming'  # 1212Z: Love and Deepspace (Infold/Papergames) player campaign aimed at Alcon Entertainment
        if str(_x) == 'trend.Iryo': return 'disaster'""")
R("if _c.endswith('1104Z.json') and '/28/' in _c: continue","if _c.endswith('1212Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T11Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T12Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"326 from watch.json, then posts under 6 h old, then posts gaining 2 percent, then the rest of the last 24 h (a fourth hour); 255 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 4 reads; fields","{len(watch_unavailable)} unavailable, 8 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop where the includes carried it), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "#AlconEntFailsHumanity", "Urda" and "Lakers" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "Iryo" had posts attached in 1104Z; "Good Wednesday", "Hump Day", "#WednesdayMotivation" and "Happy Hump" are greetings; "#AlconEntLovesPPGsCowDung" and "#中国北京应立刻追查姚润昊" are the same player campaign as "#AlconEntFailsHumanity"; "Urda" is the Spain high-speed train collision near Urda, Toledo (as "Iryo"); "Lakers" is the Blazers 136-129 win over the Lakers); all 17 due desks; no screening read (screen cut by the plan), so only posts the plan reads returned (with their includes) were screened; story clusters not in the plan; global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "and" and "my", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1006Z'","        _last = '2026-10-28T1104Z'")
R("f'not in requests/plan.json for 2026-10-28T11Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T12Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = ('cut by requests/plan.json for 2026-10-28T11Z (due, but over the overnight allowance of 20)' if d in {'life','ideas','science','business','disaster','defense','offbeat','gaming','music','medicine','tech','ai','markets','justice','world'} else 'not due: requests/plan.json for 2026-10-28T11Z')",
  "reason = ('cut by requests/plan.json for 2026-10-28T12Z (due, but listed under cut to fit the day-band allowance of 42)' if d in {'life','ideas'} else 'not due: requests/plan.json for 2026-10-28T12Z')")
R("VOL_DESKS = ['sports','internet','life','offbeat']","VOL_DESKS = ['politics','world','defense','justice','disaster']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T13:00:00Z, end_time 2026-10-28T12:00:00Z, one read per desk for the 5 desks the plan lists (volume.politics, volume.world, volume.defense, volume.justice, volume.disaster; counts 4 h old); each series is the 167 full hours 2026-10-21T13:00Z to 2026-10-28T11:00Z, and each read was checked against meta.total_tweet_count (a first try with start_time 2026-10-21T12:00Z was refused as older than the 7-day window, and one world read returned 503 before the redo)',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-27T21:08:46Z (the post\\'s creation) and end_time 2026-10-27T21:28:46Z: (conversation_id:2115188985010213103 is:reply) and (quotes_of_tweet_id:2115188985010213103 -is:retweet); the plan gives context.top two reads, so one post: 2115188985010213103 (@GlobalDiss, Chinese glass company Hengxinfeng and the France riots, 2.29M views), the most viewed post new this run that is not old content',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it; the quote read came back with no results, and the reply read returned 3 replies, each with 0 likes from small private accounts, so none was kept',[]))"+s[b:]
a=s.index("            f'Overnight-band run (7:04 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (8:12 AM ET Oct 28 / 12:12 UTC Oct 28, the 12Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T12Z, 42 reads listed) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; 6 of them were redone volume calls, see volume.desks, and about 12 more off the shared counter during the run were not this run), parallel batches, no 429 refusals. '
            f'Watch: the plan\\'s 732 ids in its order, 8 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable (2114580988013559999 Not Found; not on the pulse or cited in a story); nothing added or dropped; the 255 flat posts the plan set aside and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: all 17 the plan lists (17 reads). Volume: politics, world, defense, justice and disaster (5 reads, counts 4 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "#AlconEntFailsHumanity", "Urda" and "Lakers" (3 reads). rising.global: quote word "and" and repost word "my" (2 reads). context.top: 2 reads for 2115188985010213103 (no quotes; 3 zero-like replies not kept). '
            f'Cut by the plan and not read: screen, desks life and ideas. Candidates screened with what the plan reads returned. '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1104Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1212Z.json'")
R("        'plan': '2026-10-28T11Z',","        'plan': '2026-10-28T12Z',")
R("    'context': [],","    'context': [{'post_id': '2115188985010213103', 'replies': [], 'quotes': []}],")
open(p,'w').write(s); print('ok')
