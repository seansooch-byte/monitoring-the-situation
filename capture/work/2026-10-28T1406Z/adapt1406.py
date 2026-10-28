p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
R('capture/2026/10/28/1301Z.json from saved','capture/2026/10/28/1406Z.json from saved')
R("work/2026-10-28T1301Z'","work/2026-10-28T1406Z'")
R("RUN_ID = '2026-10-28T1301Z'","RUN_ID = '2026-10-28T1406Z'")
R("STARTED = '2026-10-28T13:01:00Z'","STARTED = '2026-10-28T14:06:00Z'")
R("OBS_AT = '2026-10-28T13:02:00Z'","OBS_AT = '2026-10-28T14:07:00Z'")
R("READS_BEFORE = 666","READS_BEFORE = 633")
a=s.index("READS_USED = 33  # 1301Z"); b=s.index("\n",a)
s=s[:a]+"READS_USED = 37  # 1406Z: this run's 37 X calls (the plan's 37 reads less one screening read, plus one music volume read redone after a 503); the counter fell 633 to 596; no 429 refusals"+s[b:]
R("datetime(2026,10,28,13,2,tzinfo=timezone.utc).timestamp()  # 1301Z (","datetime(2026,10,28,14,7,tzinfo=timezone.utc).timestamp()  # 1406Z (1301Z used 13:02, ")
R("""    'watch4': 'watch4.txt', 'watch5': 'watch5.txt', 'watch6': 'watch6.txt',
    'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_tucker': 'trend_tucker.txt', 'trend_nunew': 'trend_nunew.txt', 'trend_skhynix': 'trend_skhynix.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
""","""    'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_fomc': 'trend_fomc.txt', 'trend_butker': 'trend_butker.txt', 'trend_firstresponders': 'trend_firstresponders.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
""")
R("for batch in ('watch0','watch1','watch2','watch3','watch4','watch5','watch6'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
a=s.index("DUE = ['politics','entertainment'"); b=s.index("\n",a)
s=s[:a]+"DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']  # 1406Z: the plan (requests/plan.json for 2026-10-28T14Z) lists the four hourly desks plus the nine two-hour desks due since 1212Z; the others are not due"+s[b:]
R("""    ('quote_it','quote'),('repost_that','repost'),
    ('trend_tucker','trend.Justin Tucker'),('trend_nunew','trend.#BORNTOBEByNuNew'),('trend_skhynix','trend.SK Hynix'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""","""    ('quote_just','quote'),('repost_what','repost'),
    ('trend_fomc','trend.FOMC'),('trend_butker','trend.Butker'),('trend_firstresponders','trend.#NationalFirstRespondersDay'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
R("""        if str(_x) == 'trend.Justin Tucker': return 'sports'  # 1301Z""","""        if str(_x) == 'trend.FOMC': return 'markets'  # 1406Z: Fed rate decision day (FOMC statement 2 PM ET Oct 28)
        if str(_x) == 'trend.Butker': return 'sports'  # 1406Z: same event as Justin Tucker (Chiefs sign Tucker to the practice squad behind K Harrison Butker)
        if str(_x) == 'trend.#NationalFirstRespondersDay': return 'life'  # 1406Z: National First Responders Day (Oct 28)
        if str(_x) == 'trend.Justin Tucker': return 'sports'  # 1301Z""")
R("if _c.endswith('1301Z.json') and '/28/' in _c: continue","if _c.endswith('1406Z.json') and '/28/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
a=s.index("    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T13Z"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"    f'get_posts_by_ids of the watch item of requests/plan.json for 2026-10-28T14Z (contract/PLAN.md), in its order and in batches of 100 (the plan’s note: \"324 from watch.json, then posts under 6 h old, then posts gaining 2 percent; 218 flat posts wait for their sixth run\"; its left_out also counts 4 unavailable posts not listed); nothing added, dropped or reordered; "+s[b:]
R("{len(watch_unavailable)} unavailable, 7 reads; fields","{len(watch_unavailable)} unavailable, 4 reads; fields")
a=s.index("sweeps.append(sweep('viral.global'"); b=s.index("for g in ['news','money','science','culture','sports','online']:",a)
s=s[:a]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each, their own sweeps); quote and repost streams (rising.global); trend names "FOMC", "Butker" and "#NationalFirstRespondersDay" ("<name> lang:en is:retweet", newest first, 25 each; the plan gives viral.global three reads; of the top-ten US names, "Good Wednesday", "Hump Day", "#WednesdayMotivation" and "Happy Hump" are greetings; "Justin Tucker" had posts attached in 1301Z and "Butker" is the same event (the Chiefs signing Tucker to the practice squad behind kicker Harrison Butker); "#AlconEntLovesPPGsCowDung" and "#AlconEntFailsHumanity" are the player campaign that had posts attached in 1212Z); hourly desks politics/entertainment/sports/internet plus the nine due two-hour desks; two screening reads by id (all 146 unread referenced, reply-parent and media-source posts, most pointed-at first; none Not Found; the second hop found nothing unread); story clusters not in the plan; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '1 quote page + 1 repost page (the plan gives rising.global two reads), common words "just" and "what", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
"""+s[b:]
R("        _last = '2026-10-28T1212Z'","        _last = '2026-10-28T1301Z'")
R("f'not in requests/plan.json for 2026-10-28T13Z (rotation: culture/sports/online this run); last read in {_last}'","f'not in requests/plan.json for 2026-10-28T14Z (rotation: news/money/science this run); last read in {_last}'")
R("reason = 'not due: requests/plan.json for 2026-10-28T13Z (nothing cut)'","reason = 'not due: requests/plan.json for 2026-10-28T14Z (nothing cut)'")
R("VOL_DESKS = ['markets','business','ai','tech','science']","VOL_DESKS = ['medicine','entertainment','music','gaming','ideas']")
a=s.index("sweeps.append(sweep('volume.desks'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-10-21T15:00:00Z, end_time 2026-10-28T14:00:00Z, one read per desk for the 5 desks the plan lists (volume.medicine, volume.entertainment, volume.music, volume.gaming, volume.ideas; counts 4 h old; the music read returned 503 Service Unavailable once and was redone); each series is the 167 full hours 2026-10-21T15:00Z to 2026-10-28T13:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))"+s[b:]
a=s.index("sweeps.append(sweep('context.top'"); b=s.index("\n",a)
s=s[:a]+"sweeps.append(sweep('context.top','context',None,'search_posts_all, relevancy, 25 results each, start_time 2026-10-27T14:31:30Z (the post\\'s creation) and end_time 2026-10-27T14:51:30Z: (conversation_id:2115089006769930458 is:reply) and (quotes_of_tweet_id:2115089006769930458 -is:retweet); the plan gives context.top two reads, so one post: 2115089006769930458 (@saurabh_gunjal_, \"No wonder microsoft is cutting workforce\" video, 2.41M views), the most viewed post new this run that is not old content, left out or about a private person (the larger isisilomilo 2115158914774016011 is a TikTok clip of a private woman and is flagged private_individual)',None,'partial','two reads covered one of the three biggest new posts, as the plan sized it; both reads came back with no results in the 20-minute window, so none was kept',[]))"+s[b:]
a=s.index("            f'Day-band run (9:01 AM ET"); b=s.index("            f'No open requests.",a)
s=s[:a]+"""            f'Day-band run (10:06 AM ET Oct 28 / 14:06 UTC Oct 28, the 14Z slot; band allowance 42): executed requests/plan.json (for_run 2026-10-28T14Z, 37 reads listed, nothing cut) top to bottom per contract/PLAN.md; {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today), parallel batches, no 429 refusals (one 503 on a volume read, redone). '
            f'Watch: the plan\\'s 399 ids in its order, 4 reads, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable; nothing added or dropped; the 218 flat posts the plan set aside and the 4 standing unavailable posts are in its left_out and were not read. '
            f'Desks: politics, world, justice, markets, ai, tech, medicine, entertainment, music, gaming, sports, internet and offbeat (13 reads). Volume: medicine, entertainment, music, gaming and ideas (6 reads with the redone 503, counts 4 h old). Trends US and worldwide (2 reads). Sensors news/money/science (3 reads). viral.global: trend names "FOMC", "Butker" and "#NationalFirstRespondersDay" (3 reads). rising.global: quote word "just" and repost word "what" (2 reads). context.top: 2 reads for 2115089006769930458 (no replies or quotes in the window). Screen: 2 reads by id (146 ids; the plan allowed 3). '
"""+s[b:]
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1301Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/28/1406Z.json'")
R("        'plan': '2026-10-28T13Z',","        'plan': '2026-10-28T14Z',")
R("    'context': [{'post_id': '2115147320408891516', 'replies': [], 'quotes': []}],","    'context': [{'post_id': '2115089006769930458', 'replies': [], 'quotes': []}],")
R("EXTRA_PRIVATE |= {'2114072055180358072'","EXTRA_PRIVATE |= {'2115158914774016011'}  # 1406Z: isisilomilo repost of a TikTok gym-progress clip of a private young woman with a health comment (private person, health)\nEXTRA_PRIVATE |= {'2114072055180358072'")
open(p,'w').write(s); print('ok')
