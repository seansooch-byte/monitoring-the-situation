s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert a in s, ('missing',a[:90])
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
rep('2026-10-17T0105Z','2026-10-17T0203Z',0)
rep("capture/2026/10/17/0105Z.json","capture/2026/10/17/0203Z.json",0)
rep("STARTED = '2026-10-17T01:05:00Z'","STARTED = '2026-10-17T02:03:00Z'")
rep("OBS_AT = '2026-10-17T01:07:00Z'","OBS_AT = '2026-10-17T02:05:00Z'")
rep("READS_BEFORE = 968","READS_BEFORE = 936")
rep("READS_AFTER = 936","READS_AFTER = 905")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_memphis': 'trend_memphis.txt', 'trend_heartbeat': 'trend_heartbeat.txt', 'trend_stokes': 'trend_stokes.txt', 'trend_sixers': 'trend_sixers.txt', 'trend_corbin': 'trend_corbin.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""",1)
rep("('watch0','watch1','watch2','watch3')","('watch0','watch1','watch2')",0)
rep("DUE = ['politics','defense','disaster','business','entertainment','music','gaming','sports','internet','offbeat']","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']")
old=s[s.index("    ('quote_my','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_what','quote'),('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_memphis','trend.Memphis'),('trend_heartbeat','trend.Heartbeat'),('trend_stokes','trend.Marcus Stokes'),('trend_sixers','trend.Sixers'),('trend_corbin','trend.Baron Corbin'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""",1)
rep("_tmap = {","_tmap = {'trend.Memphis':'sports','trend.Marcus Stokes':'sports','trend.Tulane':'sports','trend.Sixers':'sports','trend.Baron Corbin':'sports','trend.Heartbeat':'music',")
rep("        if str(_x)=='trend.#OPLive': return 'entertainment'","        if str(_x)=='trend.#OPLive': return 'entertainment'\n        if str(_x) in ('trend.Memphis','trend.Marcus Stokes','trend.Sixers','trend.Baron Corbin'): return 'sports'\n        if str(_x)=='trend.Heartbeat': return 'music'")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'news': open(f'{W}/sensor_news_q.txt').read().strip(),
    'money': open(f'{W}/sensor_money_q.txt').read().strip(),
    'science': open(f'{W}/sensor_science_q.txt').read().strip(),
}
SENSOR_READ = {'news','money','science'}
""",1)
rep("01Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;","02Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Memphis, Heartbeat, "Marcus Stokes", Sixers, "Baron Corbin" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0105Z; Memphis, Marcus Stokes and Tulane are one event, the Memphis at Tulane college football game; Baron Corbin is one event with #SmackDown, Cody Rhodes and Randy Orton on WWE SmackDown; Heartbeat is BTS performing the song live in Chile; Tulane left as one event with Memphis); quote/repost words what/the/this + "is"; sensors news/money/science; desks politics/world/justice/markets/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "what", "the", "this" and "is": "what lang:en is:quote -is:retweet", "the lang:en is:quote -is:retweet", "this lang:en is:quote -is:retweet", "is lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-17T0003Z'","_last = '2026-10-17T0105Z'")
rep("'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'","'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'")
i=s.index("        if d in ('world','justice','markets','ai','tech','medicine'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-17T0105Z; two-hour desk, due 03:05Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-16T2303Z; four-hour desk, due 03:03Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-17T0105Z; four-hour desk, due 05:05Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 9:05 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 10:03 PM ET (02:03 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour, so the slow tier was not added; under the 400 cap, none left out); trends US+WW; '
            f'trend names Memphis, Heartbeat, "Marcus Stokes", Sixers, "Baron Corbin" (5 reads; top-ten US names with no posts attached in 0105Z; Memphis, Marcus Stokes and Tulane are one event, the Memphis at Tulane college football game; Baron Corbin is one event with #SmackDown; Heartbeat is BTS performing the song live in Chile; Sixers is the Sixers-Celtics preseason game; Tulane left as one event with Memphis); quote/repost words what/the/this + "is" (3+1); '
            f'sensors news/money/science; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour world, justice, markets, ai, tech, medicine); music/gaming/offbeat (due 03:05Z), science/ideas/life (due 03:03Z) and defense/disaster/business (due 05:05Z) not due; '
"""+s[j:]
rep("Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.")
open('build_capture.py','w').write(s)
print('ok')
