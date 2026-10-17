s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)
rep('"""Build capture/2026/10/17/1501Z.json','"""Build capture/2026/10/17/1600Z.json')
rep("W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1501Z'","W = '/workspace/monitoring-the-situation/capture/work/2026-10-17T1600Z'")
rep("RUN_ID = '2026-10-17T1501Z'","RUN_ID = '2026-10-17T1600Z'")
rep("STARTED = '2026-10-17T15:01:00Z'","STARTED = '2026-10-17T16:00:00Z'")
rep("OBS_AT = '2026-10-17T15:01:00Z'","OBS_AT = '2026-10-17T16:01:00Z'")
rep("READS_BEFORE = 608","READS_BEFORE = 581")
rep("READS_AFTER = 581","READS_AFTER = 551")
rep("datetime(2026,10,17,15,8,tzinfo=timezone.utc)","datetime(2026,10,17,16,5,tzinfo=timezone.utc)")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_mrfanboy': 'trend_mrfanboy.txt', 'trend_nokings': 'trend_nokings.txt', 'trend_brentford': 'trend_brentford.txt', 'trend_everton': 'trend_everton.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_foster': 'trend_foster.txt', 'trend_isak': 'trend_isak.txt', 'trend_munoz': 'trend_munoz.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("DUE = ['politics','entertainment','music','gaming','sports','internet','offbeat']",
    "DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']")
rep("""    ('quote_it','quote'),('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_mrfanboy','trend.#MrFanboyEP8'),('trend_nokings','trend.No Kings'),('trend_brentford','trend.Brentford'),('trend_everton','trend.Everton'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_foster','trend.Foster'),('trend_isak','trend.Isak'),('trend_munoz','trend.Munoz'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x)=='trend.Everton': return 'sports'\n",
    "        if str(_x)=='trend.Everton': return 'sports'\n        if str(_x) in ('trend.Isak','trend.Munoz','trend.Barcola','trend.#BRELIV'): return 'sports'\n")
rep("for batch in ('watch0','watch1','watch2'):  # noqa keep","for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep")
rep("for batch in ('watch0','watch1','watch2'):\n","for batch in ('watch0','watch1','watch2','watch3'):\n")
rep("for a,b in [('#MrFanboyEP8','MR FANBOY CHAPTER 8'),","for a,b in [('Isak','Munoz'),('Munoz','Isak'),('Isak','Brentford'),('Munoz','Brentford'),('#MrFanboyEP8','MR FANBOY CHAPTER 8'),")
# sweep texts
rep("(15Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "and, as 16Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
import re
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Foster, Isak, Munoz (each "<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached in 1501Z; Isak and Munoz are one event with Brentford, the Brentford v Liverpool match (#BRELIV), Brentford had posts attached in 1501Z; Foster is mostly Kristi Noem\\'s pheasant-opener post with her dog Foster, with unrelated foster-pet and foster-care posts; Gameday is one event with "GAME DAY", which had posts attached in 1403Z; "Good Saturday" is weekend greetings, searched in 1108Z, not searched again); quote/repost words the/this/is + you; sensors news/money/science; desks politics/world/justice/markets/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
rep("""'3 quote pages + 1 repost page, common words "it", "that", "just" and "what": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "the", "this", "is" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'""")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("""        _last = '2026-10-17T1403Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 1403Z, next run',[]))""",
"""        _last = '2026-10-17T1501Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 1501Z, next run',[]))""")
rep("""        if d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1307Z, due 17:07Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1403Z, due 18:03Z)'
        elif d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1403Z, due 16:03Z)'""",
"""        if d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1307Z, due 17:07Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T1403Z, due 18:03Z)'
        elif d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T1501Z, due 17:01Z)'""")
i=s.index("            f'Daytime run at 11:01 AM ET"); j=s.index("            f'{EXTRA_NOTE} '",i)
s=s[:i]+"""            f'Daytime run at 12:00 PM ET (16:00 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1501Z run ended at 581). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; under the 400 cap, none left out; 4 reads); trends US+WW; '
            f'trend names Foster, Isak, Munoz (3 reads; the top-ten US names with no posts attached in 1501Z; Isak and Munoz are one event with Brentford, the Brentford v Liverpool match (#BRELIV), which had posts attached in 1501Z; Foster is no single event, mostly Kristi Noem\\'s pheasant-opener post with her dog Foster plus unrelated foster-pet and foster-care posts; Gameday is one event with "GAME DAY", which had posts attached in 1403Z; "Good Saturday" is weekend greetings, searched in 1108Z, not searched again); quote/repost words the/this/is + you (3+1); '
            f'sensors news/money/science; 10 desk reads: the hourly desks politics, entertainment, sports, internet and the two-hour desks world, justice, markets, ai, tech, medicine (last ok 1403Z, due 16:03Z); '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/17/1501Z.json'","out_path = f'{REPO}/capture/2026/10/17/1600Z.json'")
open('build_capture.py','w').write(s); print('ok')
