s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, ('missing',a[:90])
    s=s.replace(a,b,1)
rep('capture/2026/10/16/2210Z.json from','capture/2026/10/16/2303Z.json from')
rep("2026-10-16T2210Z'\nREPO","2026-10-16T2303Z'\nREPO")
rep("RUN_ID = '2026-10-16T2210Z'","RUN_ID = '2026-10-16T2303Z'")
rep("STARTED = '2026-10-16T22:10:00Z'","STARTED = '2026-10-16T23:03:00Z'")
rep("OBS_AT = '2026-10-16T22:11:00Z'","OBS_AT = '2026-10-16T23:04:00Z'")
rep("READS_BEFORE = 413","READS_BEFORE = 384")
rep("READS_AFTER = 384","READS_AFTER = 353")
rep("datetime(2026,10,16,22,15,","datetime(2026,10,16,23,8,")
old=s[s.index("files = {"):s.index("DUE = [")]
s=s.replace(old,"""files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_albion': 'trend_albion.txt', 'trend_nortefire': 'trend_nortefire.txt', 'trend_zacharia': 'trend_zacharia.txt', 'trend_scaramucci': 'trend_scaramucci.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'req_norte': 'req_norte.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
""",1)
rep("DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine']","DUE = ['politics','entertainment','music','gaming','science','ideas','sports','internet','life','offbeat']")
old=s[s.index("    ('quote_you','quote'),"):s.index("] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:")]
s=s.replace(old,"""    ('quote_that','quote'),('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_albion','trend.Albion'),('trend_nortefire','trend.#NorteFire'),('trend_zacharia','trend.Katie Zacharia'),('trend_scaramucci','trend.Scaramucci'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
""",1)
rep("        if str(_x)=='trend.Violet': return 'gaming'\n","        if str(_x)=='trend.Violet': return 'gaming'\n        if str(_x)=='trend.Albion': return 'gaming'\n")
# request picks
rep("REQ_PICKS = {}\nREQ_FILES = {}\nREQ_ONLY = set()","""REQ_PICKS = {'r-2026-10-16-01': ['2111199331437207758','2111223736066331035','2111217414297784660']}
REQ_FILES = {'r-2026-10-16-01': 'req_norte'}
REQ_ONLY = {t['id'] for t in (raw['req_norte'].get('data') or [])} - set(REQ_PICKS['r-2026-10-16-01'])""")
old=s[s.index("SENSOR_Q = {"):s.index("sweeps.append(sweep('watch'")]
s=s.replace(old,"""SENSOR_Q = {
    'culture': open(f'{W}/sensor_culture_q.txt').read().strip(),
    'sports': open(f'{W}/sensor_sports_q.txt').read().strip(),
    'online': open(f'{W}/sensor_online_q.txt').read().strip(),
}
SENSOR_READ = {'culture','sports','online'}
""",1)
rep("22Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids","23Z is not a fourth hour, so the slow tier was not added; {len(watch_ids)} unique ids")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Albion, #NorteFire, "Katie Zacharia", Scaramucci (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; Press Secretary, Violet, Josh Jacobs and San Clemente had posts attached in 2210Z; Scott Jennings and Hannity left for the read cap; Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings and Hannity one event, the White House press secretary leaving the job; San Clemente and #NorteFire one event; Albion is mostly the Yu-Gi-Oh card Albion the Branded Dragon being banned, with some Brighton and Hove Albion posts); quote/repost words that/just/what + the; sensors culture/sports/online; desks politics/entertainment/music/gaming/science/ideas/sports/internet/life/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters, file saved); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "that", "just", "what" and "the": "that lang:en is:quote -is:retweet", "just lang:en is:quote -is:retweet", "what lang:en is:quote -is:retweet", "the lang:en is:retweet", newest first, 25 each',"""+s[j:]
rep("_last = '2026-10-16T2105Z'","_last = '2026-10-16T2210Z'")
rep("'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online next'","'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science next'")
i=s.index("        if d in ('music','gaming','offbeat'):"); j=s.index("        else:\n            reason = 'not due this run'",i)
s=s[:i]+"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (last ok 2026-10-16T2210Z; two-hour desk, due 00:10Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (last ok 2026-10-16T2105Z; four-hour desk, due 01:05Z)'
"""+s[j:]
i=s.index("            f'Daytime run at 6:10 PM ET"); j=s.index("            f'three screening reads by id",i)
s=s[:i]+"""            f'Daytime run at 7:03 PM ET (23:03 UTC Oct 16; 12:00-05:00 UTC band, up to 42 reads; last run before 00:00 UTC): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2210Z run ended at 384). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour, so the slow tier was not added; under the 400 cap); trends US+WW; '
            f'trend names Albion, #NorteFire, "Katie Zacharia", Scaramucci (4 reads; Press Secretary, Violet, Josh Jacobs and San Clemente had posts attached in 2210Z; Scott Jennings and Hannity left for the read cap; Scaramucci, Katie Zacharia, Press Secretary, Scott Jennings and Hannity are one event, the White House press secretary leaving the job; San Clemente and #NorteFire one event; Albion is mostly the Yu-Gi-Oh card Albion the Branded Dragon being banned); quote/repost words that/just/what + the (3+1); '
            f'sensors culture/sports/online; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat, due 23:05Z; four-hour science, ideas, life, due 23:01Z); world/justice/markets/ai/tech/medicine (due 00:10Z) and defense/disaster/business (due 01:05Z) not due; '
"""+s[j:]
rep("f'Open requests all answered in earlier captures; none read. '","f'Request r-2026-10-16-01 (Norte Fire facts) answered with one search; the other open requests were answered in earlier captures and were not read. '")
rep("Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation.","Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation.")
rep("    'r-2026-10-10-01': 'search_posts_all","    'r-2026-10-16-01': 'search_posts_all (\"Norte Fire\" OR #NorteFire) (acres OR containment OR contained OR homes OR structures OR destroyed OR cause) -is:retweet -is:reply, start_time 2026-10-16T00:00:00Z, relevancy, 25 results; plus OCFA and KTLA originals reached through the #NorteFire trend-name stream this run',\n    'r-2026-10-10-01': 'search_posts_all")
rep("    'answers': [],","    'answers': ANSWERS,")
rep("capture = {\n    'schema'","""ANSWERS = [{
    'request_id': 'r-2026-10-16-01',
    'status': 'ok',
    'post_ids': [i for i in REQ_PICKS['r-2026-10-16-01'] if i in {p['id'] for p in posts_out}],
    'note': 'One search from 2026-10-16T00:00Z (relevancy) plus the #NorteFire trend-name stream. No post from the City of San Clemente or San Juan Capistrano was returned, and no OCFA post giving acres, containment, homes lost or cause. Kept: OCFA on evacuation shelters (2111199331437207758; its evacuation-zone post 2111182130411971037 is already on the re-read list), KTLA on firefighters protecting another home in San Juan Capistrano (2111223736066331035), and California Courier (2111217414297784660), which says, citing Cal Fire, 465 acres and 0% contained as of 2:40 p.m., at least four homes destroyed, no injuries and the cause under investigation; it names the streets where homes burned but no residents. Many repeated aggregator posts gave 250 or 465 acres and \"at least 10 homes\" without a named source and were left out.'
}]
capture = {
    'schema'""")
rep("out_path = f'{REPO}/capture/2026/10/16/2210Z.json'","out_path = f'{REPO}/capture/2026/10/16/2303Z.json'")
open('build_capture.py','w').write(s)
print('ok')
