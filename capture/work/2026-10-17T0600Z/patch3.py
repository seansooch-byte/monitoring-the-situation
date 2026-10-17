s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    if count==1: assert n==1,(n,a[:80])
    s=s.replace(a,b)
rep('capture/2026/10/17/0506Z.json from','capture/2026/10/17/0600Z.json from')
rep("work/2026-10-17T0506Z'","work/2026-10-17T0600Z'")
rep("RUN_ID = '2026-10-17T0506Z'","RUN_ID = '2026-10-17T0600Z'")
rep("STARTED = '2026-10-17T05:06:00Z'","STARTED = '2026-10-17T06:00:00Z'")
rep("OBS_AT = '2026-10-17T05:07:00Z'","OBS_AT = '2026-10-17T06:01:00Z'")
rep("READS_BEFORE = 844","READS_BEFORE = 813")
rep("READS_AFTER = 813","READS_AFTER = 796")
rep("datetime(2026,10,17,4,7,tzinfo=timezone.utc)","datetime(2026,10,17,6,2,tzinfo=timezone.utc)")
rep("""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_pfl': 'trend_pfl.txt', 'trend_mamu': 'trend_mamu.txt', 'trend_oplive': 'trend_oplive.txt', 'trend_kessler': 'trend_kessler.txt', 'trend_osiris': 'trend_osiris.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""",
"""    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_johnnycarson': 'trend_johnnycarson.txt', 'trend_purdue': 'trend_purdue.txt', 'trend_memphis': 'trend_memphis.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("DUE = ['politics','defense','disaster','business','entertainment','music','gaming','sports','internet','offbeat']",
    "DUE = ['politics','entertainment','sports','internet']")
rep("""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),
    ('trend_pfl','trend.#PFLChicago'),('trend_mamu','trend.Mamu'),('trend_oplive','trend.#OPLive'),('trend_kessler','trend.Kessler'),('trend_osiris','trend.YK Osiris'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_johnnycarson','trend.Johnny Carson'),('trend_purdue','trend.Purdue'),('trend_memphis','trend.Memphis'),""")
rep("""SENSOR_Q = {
    'culture': open(f'{W}/sensor_culture_q.txt').read().strip(),
    'sports': open(f'{W}/sensor_sports_q.txt').read().strip(),
    'online': open(f'{W}/sensor_online_q.txt').read().strip(),
}
SENSOR_READ = {'culture','sports','online'}""","""SENSOR_Q = {}
SENSOR_READ = set()""")
rep("(05Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "(06Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
TN='trend names "Johnny Carson", Purdue, Memphis (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0506Z were Purdue, #SmackDown, "Johnny Carson", Memphis and Tulane; Memphis and Tulane are one event, the Memphis at Tulane college football game; #SmackDown and Tulane not read for the overnight budget)'
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; "+TN+"; quote/repost words my/it + that; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',"+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '2 quote pages + 1 repost page, common words "my", "it" and "that": "my lang:en is:quote -is:retweet", "it lang:en is:quote -is:retweet", "that lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("""        _last = '2026-10-17T0403Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next',[]))""",
"""        _last = '2026-10-17T0403Z' if g in ('news','money','science') else '2026-10-17T0506Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read: overnight budget (06:00-11:00 UTC, up to 20 reads: re-reads, trends, both global sweeps, the hourly desks); last read in {_last}',6,'skipped','overnight read budget',[]))""")
rep("""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (last ok 2026-10-17T0403Z; two-hour desk, due 06:03Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z)'""",
"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'due (last ok 2026-10-17T0403Z; two-hour desk, due 06:03Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'
        elif d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-17T0506Z; two-hour desk, due 07:06Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z)'""")
i=s.index("            f'Daytime run at 1:06 AM ET"); j=s.index("            f'Open requests all answered",i)
s=s[:i]+"""            f'Overnight run at 2:00 AM ET (06:00 UTC Oct 17; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour, so no slow tier; under the 400 cap, none left out); trends US+WW; '
            f'"""+TN.replace('(each','(3 reads; each')+"""; quote/repost words my/it + that (2+1); '
            f'hourly desks politics, entertainment, sports, internet (two-hour world, justice, markets, ai, tech, medicine due 06:03Z but cut for the overnight budget; music, gaming, offbeat, defense, disaster, business, science, ideas, life not due); '
            f'two screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts. '
"""+s[j:]
rep("f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '",
    "f'Not read for the overnight budget: sensors, story clusters, volume, context.top, media descriptions; x_stories omitted. '")
rep("'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid, search_news)'","'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid)'")
rep("out_path = f'{REPO}/capture/2026/10/17/0506Z.json'","out_path = f'{REPO}/capture/2026/10/17/0600Z.json'")
open('build_capture.py','w').write(s)
print('ok')
