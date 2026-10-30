import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert s.count(a)>=1, ('missing',a[:80])
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('capture/2026/10/16/2007Z.json from','capture/2026/10/16/2105Z.json from')
rep("2026-10-16T2007Z'\nREPO","2026-10-16T2105Z'\nREPO")
rep("RUN_ID = '2026-10-16T2007Z'","RUN_ID = '2026-10-16T2105Z'")
rep("STARTED = '2026-10-16T20:07:00Z'","STARTED = '2026-10-16T21:05:00Z'")
rep("OBS_AT = '2026-10-16T20:08:00Z'","OBS_AT = '2026-10-16T21:06:00Z'")
rep("READS_BEFORE = 474","READS_BEFORE = 445")
rep("READS_AFTER = 445","READS_AFTER = 413")
rep("datetime(2026,10,16,20,11,","datetime(2026,10,16,21,9,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_scaramucci': 'trend_scaramucci.txt', 'trend_jennings': 'trend_jennings.txt', 'trend_hannity': 'trend_hannity.txt',
    'trend_nortefire': 'trend_nortefire.txt', 'trend_sanclemente': 'trend_sanclemente.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""")
rep("DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']","DUE = ['politics','defense','disaster','business','entertainment','music','gaming','sports','internet','offbeat']")
old=s[s.index("    ('quote_my','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_what','quote'),('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_scaramucci','trend.Scaramucci'),('trend_jennings','trend.Scott Jennings'),('trend_hannity','trend.Hannity'),
    ('trend_nortefire','trend.#NorteFire'),('trend_sanclemente','trend.San Clemente'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""")
rep("        if str(_x)=='trend.Kaylub Giamanco': return 'justice'\n","        if str(_x)=='trend.Kaylub Giamanco': return 'justice'\n        if str(_x) in ('trend.#NorteFire','trend.San Clemente'): return 'disaster'\n")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'culture': open(f'{W}/sensor_culture_q.txt').read().strip(),
    'sports': open(f'{W}/sensor_sports_q.txt').read().strip(),
    'online': open(f'{W}/sensor_online_q.txt').read().strip(),
}
SENSOR_READ = {'culture','sports','online'}
""")
rep("and, as 20Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap,","21Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap,")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Scaramucci, "Scott Jennings", Hannity, #NorteFire, "San Clemente" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the other five of the US top ten (Katie Zacharia, Press Secretary, Josh Jacobs, Tesla, Kaylub Giamanco) had posts attached in 2007Z; Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings, Hannity and Mooch remain one event, the White House press secretary leaving the job; #NorteFire and San Clemente look like one event); quote/repost words what/the/this + is; sensors culture/sports/online; desks politics/defense/disaster/business/entertainment/music/gaming/sports/internet/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "what", "the", "this" and "is": "what lang:en is:quote -is:retweet", "the lang:en is:quote -is:retweet", "this lang:en is:quote -is:retweet", "is lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-16T1901Z'","_last = '2026-10-16T2007Z'")
rep("'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'","'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'")
i=s.index("        if d in ('music','gaming','offbeat'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (last ok 2026-10-16T2007Z; two-hour desk, due 22:07Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-16T1901Z; four-hour desk, due 23:01Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 4:07 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 5:05 PM ET (21:05 UTC Oct 16; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2007Z run ended at 445). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour, so the slow tier was not added; under the 400 cap); trends US+WW; '
            f'trend names Scaramucci, "Scott Jennings", Hannity, #NorteFire, "San Clemente" (5 reads; the other five of the US top ten had posts attached in 2007Z; Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings, Hannity and Mooch are still one event, the White House press secretary leaving the job; #NorteFire and San Clemente look like one event); quote/repost words what/the/this + is (3+1); '
            f'sensors culture/sports/online; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat, due 21:01Z; four-hour defense, disaster, business, due 21:02Z); world/justice/markets/ai/tech/medicine (due 22:07Z) and science/ideas/life (due 23:01Z) not due; '
"""+s[j:]
rep("Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.")
rep("out_path = f'{REPO}/capture/2026/10/16/2007Z.json'","out_path = f'{REPO}/capture/2026/10/16/2105Z.json'")
rep("for a,b in [('#The24thBloomOfPor','POR 24TH BIRTHDAY'),","for a,b in [('#NorteFire','San Clemente'),('San Clemente','#NorteFire'),('Scaramucci','Press Secretary'),('Scaramucci','Katie Zacharia'),('#The24thBloomOfPor','POR 24TH BIRTHDAY'),")
open('build_capture.py','w').write(s)
print('ok')
