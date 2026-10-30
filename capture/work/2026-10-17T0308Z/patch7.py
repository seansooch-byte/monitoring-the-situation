s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert a in s, ('missing',a[:90])
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
rep('2026-10-17T0203Z','2026-10-17T0308Z',0)
rep("capture/2026/10/17/0203Z.json","capture/2026/10/17/0308Z.json",0)
rep("STARTED = '2026-10-17T02:03:00Z'","STARTED = '2026-10-17T03:08:00Z'")
rep("OBS_AT = '2026-10-17T02:05:00Z'","OBS_AT = '2026-10-17T03:09:00Z'")
rep("READS_BEFORE = 936","READS_BEFORE = 905")
rep("READS_AFTER = 905","READS_AFTER = 876")
rep("datetime(2026,10,17,1,12,","datetime(2026,10,17,3,11,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_oplive': 'trend_oplive.txt', 'trend_dateline': 'trend_dateline.txt', 'trend_carson': 'trend_carson.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""",1)
rep("DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']","DUE = ['politics','entertainment','music','gaming','science','ideas','sports','internet','life','offbeat']")
old=s[s.index("    ('quote_what','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_you','quote'),('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_oplive','trend.#OPLive'),('trend_dateline','trend.#Dateline'),('trend_carson','trend.Johnny Carson'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""",1)
rep("_tmap = {","_tmap = {'trend.#Dateline':'entertainment','trend.Johnny Carson':'entertainment',")
rep("        if str(_x)=='trend.Heartbeat': return 'music'","        if str(_x)=='trend.Heartbeat': return 'music'\n        if str(_x) in ('trend.#Dateline','trend.Johnny Carson'): return 'entertainment'")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'culture': open(f'{W}/sensor_culture_q.txt').read().strip(),
    'sports': open(f'{W}/sensor_sports_q.txt').read().strip(),
    'online': open(f'{W}/sensor_online_q.txt').read().strip(),
}
SENSOR_READ = {'culture','sports','online'}
""",1)
rep("02Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids","03Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #OPLive, #Dateline, "Johnny Carson" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the top-ten US names with no posts attached in 0203Z; #OPLive is the On Patrol: Live TV show; #Dateline is viewers of an NBC Dateline true-crime episode; the other seven (#SmackDown, Memphis, Purdue, Tulane, Heartbeat, Marcus Stokes, Baron Corbin) had posts attached in 0203Z; Memphis, Tulane and Marcus Stokes remain one event, the Memphis at Tulane college football game); quote/repost words you/"and"/my + it; sensors culture/sports/online; desks politics/entertainment/music/gaming/science/ideas/sports/internet/life/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "you", "and" (quoted, as a bare and is an operator), "my" and "it": "you lang:en is:quote -is:retweet", "\\\\"and\\\\" lang:en is:quote -is:retweet", "my lang:en is:quote -is:retweet", "it lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-17T0105Z'","_last = '2026-10-17T0203Z'")
rep("'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'","'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'")
i=s.index("        if d in ('music','gaming','offbeat'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (last ok 2026-10-17T0203Z; two-hour desk, due 04:03Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-17T0105Z; four-hour desk, due 05:05Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 10:03 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 11:08 PM ET (03:08 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour, so the slow tier was not added; under the 400 cap, none left out); trends US+WW; '
            f'trend names #OPLive, #Dateline, "Johnny Carson" (3 reads; the top-ten US names with no posts attached in 0203Z; #OPLive is the On Patrol: Live TV show; #Dateline is viewers of an NBC Dateline true-crime episode; Johnny Carson is mostly one post comparing him with Jimmy Kimmel, reposted by many accounts; the other seven had posts attached in 0203Z, Memphis, Tulane and Marcus Stokes remaining one event, the Memphis at Tulane college football game); quote/repost words you/"and"/my + it (3+1); '
            f'sensors culture/sports/online; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat; four-hour science, ideas, life); world/justice/markets/ai/tech/medicine (due 04:03Z) and defense/disaster/business (due 05:05Z) not due; '
"""+s[j:]
rep("Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.")
open('build_capture.py','w').write(s)
print('ok')
