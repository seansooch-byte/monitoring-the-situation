s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep("2026-10-19T1203Z'","2026-10-19T1302Z'",0)
rep('capture/2026/10/19/1203Z.json from','capture/2026/10/19/1302Z.json from')
rep("STARTED = '2026-10-19T12:03:00Z'","STARTED = '2026-10-19T13:02:00Z'")
rep("OBS_AT = '2026-10-19T12:04:00Z'","OBS_AT = '2026-10-19T13:03:00Z'")
rep("READS_BEFORE = 690","READS_BEFORE = 655")
import re as _r
s=_r.sub(r"READS_USED = 35  #[^\n]*","READS_USED = 30  # this run's X calls (655 to 625 left today)",s,1)
rep("datetime(2026,10,19,12,8,tzinfo=timezone.utc)","datetime(2026,10,19,13,8,tzinfo=timezone.utc)")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_joongdunk': 'trend_joongdunk.txt', 'trend_samie': 'trend_samie.txt', 'trend_gael': 'trend_gael.txt', 'trend_goodmonday': 'trend_goodmonday.txt', 'trend_mondayvibes': 'trend_mondayvibes.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_my': 'repost_my.txt',
    'trend_reparations': 'trend_reparations.txt', 'trend_victorymonday': 'trend_victorymonday.txt', 'trend_jpmcoin': 'trend_jpmcoin.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]",
    "if d['id'] in ('politics','entertainment','sports','internet','science','ideas','life','defense','disaster','business')]")
rep("""    ('quote_that','quote'),('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_joongdunk','trend.JoongDunk'),('trend_samie','trend.Samie'),('trend_gael','trend.Gael'),('trend_goodmonday','trend.Good Monday'),('trend_mondayvibes','trend.#MondayVibes'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""","""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_my','repost'),
    ('trend_reparations','trend.Reparations'),('trend_victorymonday','trend.Victory Monday'),('trend_jpmcoin','trend.JPM Coin'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""")
rep("        if str(_x) in ('trend.jeonghan',): return 'music'  # 1000Z: SEVENTEEN member Jeonghan",
    "        if str(_x) in ('trend.Victory Monday',): return 'sports'  # 1302Z: NFL teams' Victory Monday posts\n        if str(_x) in ('trend.Reparations',): return 'politics'  # 1302Z\n        if str(_x) in ('trend.JPM Coin',): return 'business'  # 1302Z: JPMorgan deposit token (a company's story; crypto retired)\n        if str(_x) in ('trend.jeonghan',): return 'music'  # 1000Z: SEVENTEEN member Jeonghan")
rep("if _c.endswith('1203Z.json') and '/19/' in _c: continue","if _c.endswith('1302Z.json') and '/19/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("and, because 12Z is a fourth hour, the rest of the last 24 hours, slowest growing last; 416 ids before the 400 cap, the 16 slowest-growing of the rest of the last 24 hours left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(13Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Reparations, "Victory Monday", "JPM Coin" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these three had no posts attached in 1203Z); quote/repost words this/is/you + my; sensors culture/sports/online; desks politics/entertainment/sports/internet/science/ideas/life/defense/disaster/business; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "this", "is", "you" and "my": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each',"""+s[j:]
rep("""        _last = '2026-10-19T0509Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last} (the overnight band since then had no sensor reads), next run',[]))""",
"""        _last = '2026-10-19T1203Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('science','ideas','life'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0304Z, due 07:04Z) but cut first by the cut order (four-hour desks) to keep this run near the ten-desk share of the budget; next run'
        elif d in ('defense','disaster','business'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0509Z, due 09:09Z) but cut first by the cut order (four-hour desks) to keep this run near the ten-desk share of the budget; next run'
        else:
            reason = 'not due this run'""","""        if d in ('world','justice','markets','music','gaming','offbeat','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1203Z, due 14:03Z)'
        else:
            reason = 'not due this run'""")
i=s.index("            f'Morning run at 8:03 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Morning run at 9:02 AM ET (13:02 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1203Z run ended at 655; calls made in parallel batches of up to 11, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names Reparations, "Victory Monday", "JPM Coin" (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names only these three had no posts attached in 1203Z; Victory Monday is NFL teams celebrating Sunday wins, JPM Coin the JPMorgan deposit token moving to Ethereum); '
            f'quote/repost words this/is/you + my (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 1203Z); '
            f'10 desk reads: hourly politics, entertainment, sports, internet; four-hour science, ideas, life (last ok 0304Z) and defense, disaster, business (last ok 0509Z); two-hour desks were read in 1203Z and are not due until 14:03Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts (one second-hop id not returned); search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1203Z.json'","out_path = f'{REPO}/capture/2026/10/19/1302Z.json'")
# run-specific skips
rep("skipped_nsfw = []\n","skipped_nsfw = []\nskip_nsfw |= {'__P1302_SKIP__'}  # 1302Z\n")
open('build_capture.py','w').write(s)
print('ok')
