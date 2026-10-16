import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)>=1, ('missing',a[:80])
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('capture/2026/10/16/2105Z.json from','capture/2026/10/16/2210Z.json from')
rep("2026-10-16T2105Z'\nREPO","2026-10-16T2210Z'\nREPO")
rep("RUN_ID = '2026-10-16T2105Z'","RUN_ID = '2026-10-16T2210Z'")
rep("STARTED = '2026-10-16T21:05:00Z'","STARTED = '2026-10-16T22:10:00Z'")
rep("OBS_AT = '2026-10-16T21:06:00Z'","OBS_AT = '2026-10-16T22:11:00Z'")
rep("READS_BEFORE = 445","READS_BEFORE = 413")
rep("READS_AFTER = 413","READS_AFTER = 384")
rep("datetime(2026,10,16,21,9,","datetime(2026,10,16,22,15,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_violet': 'trend_violet.txt', 'trend_jacobs': 'trend_jacobs.txt', 'trend_giamanco': 'trend_giamanco.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""")
rep("DUE = ['politics','defense','disaster','business','entertainment','music','gaming','sports','internet','offbeat']","DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']")
rep("for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep","for batch in ('watch0','watch1','watch2'):  # noqa keep")
rep("for batch in ('watch0','watch1','watch2','watch3'):\n","for batch in ('watch0','watch1','watch2'):\n")
old=s[s.index("    ('quote_what','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_you','quote'),('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_violet','trend.Violet'),('trend_jacobs','trend.Josh Jacobs'),('trend_giamanco','trend.Kaylub Giamanco'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
rep("        if str(_x) in ('trend.#NorteFire','trend.San Clemente'): return 'disaster'\n","        if str(_x) in ('trend.#NorteFire','trend.San Clemente'): return 'disaster'\n        if str(_x)=='trend.Violet': return 'gaming'\n        if str(_x)=='trend.Josh Jacobs': return 'sports'\n")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'news': open(f'{W}/sensor_news_q.txt').read().strip(),
    'money': open(f'{W}/sensor_money_q.txt').read().strip(),
    'science': open(f'{W}/sensor_science_q.txt').read().strip(),
}
SENSOR_READ = {'news','money','science'}
""")
rep("21Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;","22Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Violet, "Josh Jacobs", "Kaylub Giamanco" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the other seven of the US top ten (Scaramucci, Press Secretary, Katie Zacharia, Scott Jennings, Tesla, San Clemente, #NorteFire) had posts attached in 2105Z; Scaramucci, Katie Zacharia, Press Secretary and Scott Jennings remain one event, the White House press secretary leaving the job; San Clemente and #NorteFire one event; Violet is the new hero in the game Deadlock); quote/repost words you/"and"/my + it; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "you", "and" (quoted, as a bare and is an operator), "my" and "it": "you lang:en is:quote -is:retweet", "\\\\"and\\\\" lang:en is:quote -is:retweet", "my lang:en is:quote -is:retweet", "it lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-16T2007Z'","_last = '2026-10-16T2105Z'")
rep("'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'","'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'")
i=s.index("        if d in ('world','justice','markets','ai','tech','medicine'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-16T2105Z; two-hour desk, due 23:05Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-16T1901Z; four-hour desk, due 23:01Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-16T2105Z; four-hour desk, due 01:05Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 5:05 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 6:10 PM ET (22:10 UTC Oct 16; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2105Z run ended at 413). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z is not a fourth hour, so the slow tier was not added; under the 400 cap); trends US+WW; '
            f'trend names Violet, "Josh Jacobs", "Kaylub Giamanco" (3 reads; the other seven of the US top ten had posts attached in 2105Z; Scaramucci, Katie Zacharia, Press Secretary and Scott Jennings are still one event, the White House press secretary leaving the job; San Clemente and #NorteFire one event; Violet is the new hero in the game Deadlock); quote/repost words you/"and"/my + it (3+1); '
            f'sensors news/money/science; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour world, justice, markets, ai, tech, medicine, due 22:07Z); music/gaming/offbeat (due 23:05Z), science/ideas/life (due 23:01Z) and defense/disaster/business (due 01:05Z) not due; '
"""+s[j:]
rep("Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.")
rep("out_path = f'{REPO}/capture/2026/10/16/2105Z.json'","out_path = f'{REPO}/capture/2026/10/16/2210Z.json'")
open('build_capture.py','w').write(s)
print('ok')
