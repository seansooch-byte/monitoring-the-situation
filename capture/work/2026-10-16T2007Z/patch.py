import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep('capture/2026/10/16/1901Z.json from','capture/2026/10/16/2007Z.json from')
rep("2026-10-16T1901Z'\nREPO","2026-10-16T2007Z'\nREPO")
rep("RUN_ID = '2026-10-16T1901Z'","RUN_ID = '2026-10-16T2007Z'")
rep("STARTED = '2026-10-16T19:01:00Z'","STARTED = '2026-10-16T20:07:00Z'")
rep("OBS_AT = '2026-10-16T19:02:00Z'","OBS_AT = '2026-10-16T20:08:00Z'")
rep("READS_BEFORE = 506","READS_BEFORE = 474")
rep("READS_AFTER = 474","READS_AFTER = 445")
s=re.sub(r"EXTRA_NOTE = '.*?'\n", "EXTRA_NOTE = open(f'{W}/extra_note.txt').read().strip() if os.path.exists(f'{W}/extra_note.txt') else ''\n", s, count=1)
rep("datetime(2026,10,16,19,5,","datetime(2026,10,16,20,11,")
old_files=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old_files,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_tesla': 'trend_tesla.txt', 'trend_jacobs': 'trend_jacobs.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""")
rep("DUE = ['politics','entertainment','music','gaming','sports','internet','offbeat','science','ideas','life']","DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']")
old=s[s.index("    ('quote_this','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_my','quote'),('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_tesla','trend.Tesla'),('trend_jacobs','trend.Josh Jacobs'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""")
rep("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",0)
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'news': open(f'{W}/sensor_news_q.txt').read().strip(),
    'money': open(f'{W}/sensor_money_q.txt').read().strip(),
    'science': open(f'{W}/sensor_science_q.txt').read().strip(),
}
SENSOR_READ = {'news','money','science'}
""")
rep("that gained at least 2 percent between their last two readings (19Z is not a fourth hour); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "that gained at least 2 percent between their last two readings, and, as 20Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
old=s[s.index("    'sources: references followed two hops"):s.index("    24,'ok',None, viral_core))")]
s=s.replace(old,"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Tesla, "Josh Jacobs" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the other eight of the US top ten (Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings, Hannity, Kaylub Giamanco, Mooch, Mexico City) had posts attached in 1901Z; Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings, Hannity and Mooch remain one event, the White House press secretary leaving the job); quote/repost words my/it/that + just; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',
""")
old=s[s.index("    '3 quote pages + 1 repost page"):s.index("    6,'ok',None, rising_ids[:30]))")]
s=s.replace(old,"""    '3 quote pages + 1 repost page, common words "my", "it", "that" and "just": "my lang:en is:quote -is:retweet", "it lang:en is:quote -is:retweet", "that lang:en is:quote -is:retweet", "just lang:en is:retweet", newest first, 25 each',
""")
rep("_last = '2026-10-16T1804Z'","_last = '2026-10-16T1901Z'")
rep("'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'","'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'")
old=s[s.index("        if d in ('world','justice','markets','ai','tech','medicine'):"):s.index("        else:\n            reason = 'not due this run'")]
s=s.replace(old,"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-16T1901Z; two-hour desk, due 21:01Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-16T1702Z; four-hour desk, due 21:02Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-16T1901Z; four-hour desk, due 23:01Z)'
""")
old=s[s.index("            f'Daytime run at 3:01 PM ET"):s.index("            f'{EXTRA_NOTE} '")]
s=s.replace(old,"""            f'Daytime run at 4:07 PM ET (20:07 UTC Oct 16; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1901Z run ended at 474). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 20Z is a fourth hour, so the slow tier was added, all under the 400 cap); trends US+WW; '
            f'trend names Tesla, "Josh Jacobs" (2 reads; the other eight of the US top ten had posts attached in 1901Z; Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings, Hannity and Mooch are still one event, the White House press secretary leaving the job); quote/repost words my/it/that + just (3+1); '
            f'sensors news/money/science; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour world, justice, markets, ai, tech, medicine, due 20:04Z); music/gaming/offbeat (due 21:01Z), defense/disaster/business (due 21:02Z) and science/ideas/life (due 23:01Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '
""")
rep("out_path = f'{REPO}/capture/2026/10/16/1901Z.json'","out_path = f'{REPO}/capture/2026/10/16/2007Z.json'")
open('build_capture.py','w').write(s)
print('ok')
