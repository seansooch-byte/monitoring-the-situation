s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert a in s, ('missing',a[:90])
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
rep('capture/2026/10/16/2303Z.json from','capture/2026/10/17/0003Z.json from')
rep("2026-10-16T2303Z'\nREPO","2026-10-17T0003Z'\nREPO")
rep("RUN_ID = '2026-10-16T2303Z'","RUN_ID = '2026-10-17T0003Z'")
rep("STARTED = '2026-10-16T23:03:00Z'","STARTED = '2026-10-17T00:03:00Z'")
rep("OBS_AT = '2026-10-16T23:04:00Z'","OBS_AT = '2026-10-17T00:04:00Z'")
rep("READS_BEFORE = 384","READS_BEFORE = 1000")
rep("READS_AFTER = 353","READS_AFTER = 968")
rep("datetime(2026,10,16,23,8,","datetime(2026,10,17,0,6,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_violet': 'trend_violet.txt', 'trend_jennings': 'trend_jennings.txt', 'trend_neera': 'trend_neera.txt', 'trend_jacobs': 'trend_jacobs.txt', 'trend_redrising': 'trend_redrising.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""",1)
rep("DUE = ['politics','entertainment','music','gaming','science','ideas','sports','internet','life','offbeat']","DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']")
old=s[s.index("    ('quote_that','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),
    ('trend_violet','trend.Violet'),('trend_jennings','trend.Scott Jennings'),('trend_neera','trend.Neera'),('trend_jacobs','trend.Josh Jacobs'),('trend_redrising','trend.Red Rising'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
""",1)
rep("_tmap = {","_tmap = {'trend.Scott Jennings':'politics','trend.Neera':'politics','trend.Josh Jacobs':'sports','trend.Red Rising':'entertainment',")
rep("""REQ_PICKS = {'r-2026-10-16-01': ['2111199331437207758','2111217414297784660']}
REQ_FILES = {'r-2026-10-16-01': 'req_norte'}
REQ_ONLY = {t['id'] for t in (raw['req_norte'].get('data') or [])} - set(REQ_PICKS['r-2026-10-16-01'])""","REQ_PICKS = {}\nREQ_FILES = {}\nREQ_ONLY = set()")
rep("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",0)
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'news': open(f'{W}/sensor_news_q.txt').read().strip(),
    'money': open(f'{W}/sensor_money_q.txt').read().strip(),
    'science': open(f'{W}/sensor_science_q.txt').read().strip(),
}
SENSOR_READ = {'news','money','science'}
""",1)
rep("23Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads","and, as 00Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Violet, "Scott Jennings", Neera, "Josh Jacobs", "Red Rising" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the top-ten US names with no posts attached in 2303Z; Norte Fire is one event with #NorteFire and San Clemente, which had posts attached in 2303Z; Scott Jennings is one event with Scaramucci, Katie Zacharia and Press Secretary, the White House press secretary leaving the job); quote/repost words this/is/you + "and"; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "this", "is", "you" and "and": "this lang:en is:quote -is:retweet", "is lang:en is:quote -is:retweet", "you lang:en is:quote -is:retweet", "\\\\"and\\\\" lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-16T2210Z'","_last = '2026-10-16T2303Z'")
rep("'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'","'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'")
i=s.index("        if d in ('world','justice','markets','ai','tech','medicine'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (last ok 2026-10-16T2303Z; two-hour desk, due 01:05Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (last ok 2026-10-16T2303Z; four-hour desk, due 03:01Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-16T2105Z; four-hour desk, due 01:05Z)'
"""+s[j:]
rep("ANSWERED_EARLIER = {","ANSWERED_EARLIER = {'r-2026-10-16-01':'2026-10-16T2303Z',")
i=s.index("ANSWERS = [{"); j=s.index("capture = {\n    'schema'")
s=s[:i]+"ANSWERS = []\n"+s[j:]
i=s.index("            f'Daytime run at 7:03 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 8:03 PM ET (00:03 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads; first run of the UTC day, the X day reset at 00:00 UTC): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2303Z run ended at 353 on the old day). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour, so the slow tier was added; under the 400 cap, none left out); trends US+WW; '
            f'trend names Violet, "Scott Jennings", Neera, "Josh Jacobs", "Red Rising" (5 reads; the top-ten US names with no posts attached in 2303Z; Norte Fire is one event with #NorteFire and San Clemente, which had posts attached in 2303Z; Scott Jennings is one event with Scaramucci, Katie Zacharia and Press Secretary, the White House press secretary leaving the job); quote/repost words this/is/you + "and" (3+1); '
            f'sensors news/money/science; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour world, justice, markets, ai, tech, medicine, due 00:10Z, swept 4 minutes early to keep the cadence); music/gaming/offbeat (due 01:05Z), defense/disaster/business (due 01:05Z) and science/ideas/life (due 03:01Z) not due; '
"""+s[j:]
rep("f'Request r-2026-10-16-01 (Norte Fire facts) answered with one search; the other open requests were answered in earlier captures and were not read. '","f'Open requests all answered in earlier captures (r-2026-10-16-01 in 2303Z); none read. '")
rep("Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.")
rep("out_path = f'{REPO}/capture/2026/10/16/2303Z.json'","out_path = f'{REPO}/capture/2026/10/17/0003Z.json'")
open('build_capture.py','w').write(s)
print('ok')
