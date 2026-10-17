s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert a in s, ('missing',a[:90])
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
rep('2026-10-17T0308Z','2026-10-17T0403Z',0)
rep("capture/2026/10/17/0308Z.json","capture/2026/10/17/0403Z.json",0)
rep("STARTED = '2026-10-17T03:08:00Z'","STARTED = '2026-10-17T04:03:00Z'")
rep("OBS_AT = '2026-10-17T03:09:00Z'","OBS_AT = '2026-10-17T04:04:00Z'")
rep("READS_BEFORE = 905","READS_BEFORE = 876")
rep("READS_AFTER = 876","READS_AFTER = 844")
rep("datetime(2026,10,17,3,11,","datetime(2026,10,17,4,7,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_trevino': 'trend_trevino.txt', 'trend_adin': 'trend_adin.txt', 'trend_purdue': 'trend_purdue.txt', 'trend_smackdown': 'trend_smackdown.txt', 'trend_memphis': 'trend_memphis.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""",1)
rep("('watch0','watch1','watch2')","('watch0','watch1','watch2','watch3')",0)
rep("DUE = ['politics','entertainment','music','gaming','science','ideas','sports','internet','life','offbeat']","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']")
old=s[s.index("    ('quote_you','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_that','quote'),('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_trevino','trend.ash trevino'),('trend_adin','trend.Adin Ross'),('trend_purdue','trend.Purdue'),('trend_smackdown','trend.#SmackDown'),('trend_memphis','trend.Memphis'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""",1)
rep("_tmap = {","_tmap = {'trend.ash trevino':'internet','trend.Adin Ross':'internet',")
rep("        if str(_x)=='trend.Heartbeat': return 'music'","        if str(_x)=='trend.Heartbeat': return 'music'\n        if str(_x) in ('trend.ash trevino','trend.Adin Ross'): return 'internet'")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'news': open(f'{W}/sensor_news_q.txt').read().strip(),
    'money': open(f'{W}/sensor_money_q.txt').read().strip(),
    'science': open(f'{W}/sensor_science_q.txt').read().strip(),
}
SENSOR_READ = {'news','money','science'}
""",1)
rep("between their last two readings, 03Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;","between their last two readings, and, as 04Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "ash trevino", "Adin Ross", Purdue, #SmackDown, Memphis (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0308Z; ash trevino and Adin Ross are one event, fights at an Adin Ross boxing event; Purdue is the Washington at Purdue college football game; Memphis, Tulane and Marcus Stokes remain one event, the Memphis at Tulane college football game, so Tulane and Marcus Stokes were not searched again; Heartbeat left for the read cap); quote/repost words that/just/what + the; sensors news/money/science; desks politics/world/justice/markets/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "that", "just", "what" and "the": "that lang:en is:quote -is:retweet", "just lang:en is:quote -is:retweet", "what lang:en is:quote -is:retweet", "the lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-17T0203Z'","_last = '2026-10-17T0308Z'")
rep("'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'","'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'")
i=s.index("        if d in ('world','justice','markets','ai','tech','medicine'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; two-hour desk, due 05:08Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-17T0105Z; four-hour desk, due 05:05Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 11:08 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 12:03 AM ET (04:03 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour, so the slow tier was added; under the 400 cap, none left out); trends US+WW; '
            f'trend names "ash trevino", "Adin Ross", Purdue, #SmackDown, Memphis (5 reads; top-ten US names with no posts attached in 0308Z; ash trevino and Adin Ross are one event, fights at an Adin Ross boxing event; Purdue is the Washington at Purdue college football game; #SmackDown is WWE SmackDown; Memphis, Tulane and Marcus Stokes remain one event, the Memphis at Tulane college football game; Heartbeat left for the read cap); quote/repost words that/just/what + the (3+1); '
            f'sensors news/money/science; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour world, justice, markets, ai, tech, medicine); music/gaming/offbeat (due 05:08Z), science/ideas/life (due 07:08Z) and defense/disaster/business (due 05:05Z) not due; '
"""+s[j:]
rep("Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.")
a="for a,b in [('Memphis','Marcus Stokes'),"
rep(a,"for a,b in [('ash trevino','Adin Ross'),('Adin Ross','ash trevino'),('Memphis','Marcus Stokes'),")
open('build_capture.py','w').write(s)
print('ok')
