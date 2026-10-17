s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert a in s, ('missing',a[:90])
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
rep('capture/2026/10/17/0003Z.json from','capture/2026/10/17/0105Z.json from')
rep("2026-10-17T0003Z'\nREPO","2026-10-17T0105Z'\nREPO")
rep("RUN_ID = '2026-10-17T0003Z'","RUN_ID = '2026-10-17T0105Z'")
rep("STARTED = '2026-10-17T00:03:00Z'","STARTED = '2026-10-17T01:05:00Z'")
rep("OBS_AT = '2026-10-17T00:04:00Z'","OBS_AT = '2026-10-17T01:07:00Z'")
rep("READS_BEFORE = 1000","READS_BEFORE = 968")
rep("READS_AFTER = 968","READS_AFTER = 936")
rep("datetime(2026,10,17,0,6,","datetime(2026,10,17,1,12,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_smackdown': 'trend_smackdown.txt', 'trend_nikki': 'trend_nikki.txt', 'trend_sanclemente': 'trend_sanclemente.txt', 'trend_oplive': 'trend_oplive.txt', 'trend_purdue': 'trend_purdue.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""",1)
rep("DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']","DUE = ['politics','defense','disaster','business','entertainment','music','gaming','sports','internet','offbeat']")
old=s[s.index("    ('quote_this','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_my','quote'),('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_smackdown','trend.#SmackDown'),('trend_nikki','trend.Nikki Bella'),('trend_sanclemente','trend.San Clemente'),('trend_oplive','trend.#OPLive'),('trend_purdue','trend.Purdue'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""",1)
rep("_tmap = {","_tmap = {'trend.#SmackDown':'sports','trend.Nikki Bella':'sports','trend.#OPLive':'entertainment','trend.Purdue':'sports',")
rep("        if str(_x)=='trend.Josh Jacobs': return 'sports'","        if str(_x)=='trend.Josh Jacobs': return 'sports'\n        if str(_x) in ('trend.#SmackDown','trend.Nikki Bella','trend.Purdue'): return 'sports'\n        if str(_x)=='trend.#OPLive': return 'entertainment'")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'culture': open(f'{W}/sensor_culture_q.txt').read().strip(),
    'sports': open(f'{W}/sensor_sports_q.txt').read().strip(),
    'online': open(f'{W}/sensor_online_q.txt').read().strip(),
}
SENSOR_READ = {'culture','sports','online'}
""",1)
rep("and, as 00Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids","01Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #SmackDown, "Nikki Bella", "San Clemente", #OPLive, Purdue (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0003Z; #SmackDown and Nikki Bella are one event, WWE SmackDown; San Clemente is one event with Norte Fire; End 1Q, Memphis and Tulane left for the read cap); quote/repost words my/it/that + "just"; sensors culture/sports/online; desks politics/defense/disaster/business/entertainment/music/gaming/sports/internet/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "my", "it", "that" and "just": "my lang:en is:quote -is:retweet", "it lang:en is:quote -is:retweet", "that lang:en is:quote -is:retweet", "just lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-16T2303Z'","_last = '2026-10-17T0003Z'")
rep("'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'","'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'")
i=s.index("        if d in ('music','gaming','offbeat'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (last ok 2026-10-17T0003Z; two-hour desk, due 02:03Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-16T2303Z; four-hour desk, due 03:03Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 8:03 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 9:05 PM ET (01:05 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour, so the slow tier was not added; under the 400 cap, none left out); trends US+WW; '
            f'trend names #SmackDown, "Nikki Bella", "San Clemente", #OPLive, Purdue (5 reads; top-ten US names with no posts attached in 0003Z; #SmackDown and Nikki Bella are one event, WWE SmackDown with Nikki Bella and Paige; San Clemente is one event with Norte Fire; #OPLive is the On Patrol: Live broadcast; End 1Q, Memphis and Tulane left for the read cap); quote/repost words my/it/that + "just" (3+1); '
            f'sensors culture/sports/online; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat; four-hour defense, disaster, business); world/justice/markets/ai/tech/medicine (due 02:03Z) and science/ideas/life (due 03:03Z) not due; '
"""+s[j:]
rep("f'Open requests all answered in earlier captures (r-2026-10-16-01 in 2303Z); none read. '","f'Open requests all answered in earlier captures; none read. '")
rep("Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.")
rep("out_path = f'{REPO}/capture/2026/10/17/0003Z.json'","out_path = f'{REPO}/capture/2026/10/17/0105Z.json'")
open('build_capture.py','w').write(s)
print('ok')
