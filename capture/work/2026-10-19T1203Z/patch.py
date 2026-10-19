import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
rep("2026-10-19T1104Z'","2026-10-19T1203Z'",0)
rep("STARTED = '2026-10-19T11:04:00Z'","STARTED = '2026-10-19T12:03:00Z'")
rep("OBS_AT = '2026-10-19T11:05:00Z'","OBS_AT = '2026-10-19T12:04:00Z'")
rep("READS_BEFORE = 723","READS_BEFORE = 690")
rep("READS_USED = 16  #","READS_USED = 35  #")
rep("datetime(2026,10,19,11,8,tzinfo=timezone.utc)","datetime(2026,10,19,12,8,tzinfo=timezone.utc)")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_jpm_coin': 'trend_jpm_coin.txt', 'trend_jun_maeda': 'trend_jun_maeda.txt', 'trend_shawn_ryan': 'trend_shawn_ryan.txt',
    'screen0': 'screen0.txt',""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_joongdunk': 'trend_joongdunk.txt', 'trend_samie': 'trend_samie.txt', 'trend_gael': 'trend_gael.txt', 'trend_goodmonday': 'trend_goodmonday.txt', 'trend_mondayvibes': 'trend_mondayvibes.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet')]","if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]")
rep("""    ('quote_is','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_jpm_coin','trend.JPM Coin'),('trend_jun_maeda','trend.Jun Maeda'),('trend_shawn_ryan','trend.Shawn Ryan'),
]""","""    ('quote_that','quote'),('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_joongdunk','trend.JoongDunk'),('trend_samie','trend.Samie'),('trend_gael','trend.Gael'),('trend_goodmonday','trend.Good Monday'),('trend_mondayvibes','trend.#MondayVibes'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""")
rep("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",0)
rep("if _c.endswith('1104Z.json') and '/19/' in _c: continue","if _c.endswith('1203Z.json') and '/19/' in _c: continue")
rep("SENSOR_Q = {}\nSENSOR_READ = set()","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("(11Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "and, because 12Z is a fourth hour, the rest of the last 24 hours, slowest growing last; 416 ids before the 400 cap, the 16 slowest-growing of the rest of the last 24 hours left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
rep("""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names JPM Coin, Jun Maeda, Shawn Ryan (each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, Cowboys, Victory Monday, JPM Coin, Jun Maeda, #ScarletHeartTH and Shawn Ryan had no posts attached in 1000Z; Cowboys and Victory Monday are the Cowboys v Packers game, which already has posts under Packers/Cowboys-adjacent, and #ScarletHeartTH was cut for the overnight budget); quote/repost words is/my + it; hourly desks politics/entertainment/sports/internet; one screening read by id of 18 unread first-hop referenced posts (second hop had no further unread); screened by id with global floor/pace',""",
"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names JoongDunk, Samie, Gael, "Good Monday", #MondayVibes (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these, #MondayMotivation and Victory Monday had no posts attached in 1104Z; Victory Monday is the Cowboys v Packers game and #MondayMotivation was read in 1000Z, so both were cut for the five-name limit); quote/repost words that/just/what + the; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',""")
rep("""    '2 quote pages + 1 repost page, common words "is", "my" and "it": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each',""",
"""    '3 quote pages + 1 repost page, common words "that", "just", "what" and "the": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each',""")
rep("""        _last = '2026-10-19T0404Z' if g in ('news','money','science') else '2026-10-19T0509Z'  # unchanged: not read in 0603Z through 1104Z overnight band
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (overnight band, up to 20 reads; sensors are not in the overnight list); last read in {_last}',6,'skipped',f'cut for the overnight read budget (06:00-11:00 UTC: re-reads, trends, both global sweeps, the hourly desks); last read in {_last}',[]))""",
"""        _last = '2026-10-19T0509Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last} (the overnight band since then had no sensor reads), next run',[]))""")
rep("""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'due (two-hour desk, last ok 2026-10-19T0404Z, due 06:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('ai','tech','medicine'):
            reason = 'due (two-hour desk, last ok 2026-10-19T0509Z, due 07:09Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('science','ideas','life'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0304Z, due 07:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('defense','disaster','business'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0509Z, due 09:09Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'""",
"""        if d in ('science','ideas','life'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0304Z, due 07:04Z) but cut first by the cut order (four-hour desks) to keep this run near the ten-desk share of the budget; next run'
        elif d in ('defense','disaster','business'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0509Z, due 09:09Z) but cut first by the cut order (four-hour desks) to keep this run near the ten-desk share of the budget; next run'""")
# run reason
i=s.index("            f'Overnight run at 7:04 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Morning run at 8:03 AM ET (12:03 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1104Z run ended at 693 and 3 were used elsewhere before this run; calls made in parallel batches of up to 13, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; 416 ids before the 400 cap, the 16 slowest-growing of that last tier left out; 4 reads); trends US+WW (2 reads); '
            f'trend names JoongDunk, Samie, Gael, "Good Monday", #MondayVibes (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, #MondayMotivation and Victory Monday had no posts attached in 1104Z; Victory Monday is the Cowboys v Packers game and #MondayMotivation was read in 1000Z, so both were cut for the five-name limit); '
            f'quote/repost words that/just/what + the (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 0509Z); '
            f'13 desk reads: hourly politics, entertainment, sports, internet; two-hour world, justice, markets, music, gaming, offbeat (last ok 0404Z) and ai, tech, medicine (last ok 0509Z); four-hour science, ideas, life (due 07:04Z) and defense, disaster, business (due 09:09Z) cut first by the cut order, next run; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts (one first-hop id not found); search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions. '
"""+s[j:]
open('build_capture.py','w').write(s)
print('ok')
