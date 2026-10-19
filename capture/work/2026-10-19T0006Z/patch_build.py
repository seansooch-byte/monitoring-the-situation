import re
s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    if count==1: assert n==1,('multi',a[:80],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/18/2306Z.json from saved X outputs."""','"""Build capture/2026/10/19/0006Z.json from saved X outputs."""')
R("capture/work/2026-10-18T2306Z'","capture/work/2026-10-19T0006Z'")
R("RUN_ID = '2026-10-18T2306Z'","RUN_ID = '2026-10-19T0006Z'")
R("STARTED = '2026-10-18T23:06:00Z'","STARTED = '2026-10-19T00:06:00Z'")
R("OBS_AT = '2026-10-18T23:07:00Z'","OBS_AT = '2026-10-19T00:07:00Z'")
R("READS_BEFORE = 350","READS_BEFORE = 1000")
R("datetime(2026,10,18,23,9,tzinfo=timezone.utc)","datetime(2026,10,19,0,9,tzinfo=timezone.utc)")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_rams': 'trend_rams.txt', 'trend_cardinals': 'trend_cardinals.txt', 'trend_chargers': 'trend_chargers.txt', 'trend_bensimmons': 'trend_bensimmons.txt', 'trend_chiefs': 'trend_chiefs.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',
    'repost_just': 'repost_just.txt',
    'trend_raiders': 'trend_raiders.txt', 'trend_vsfashionshow': 'trend_vsfashionshow.txt', 'trend_mcvay': 'trend_mcvay.txt', 'trend_herbert': 'trend_herbert.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
R("if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','science','ideas','life')]","if d['id'] in ('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]")
R("""    ('quote_is','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_rams','trend.Rams'),('trend_cardinals','trend.Cardinals'),('trend_chargers','trend.Chargers'),('trend_bensimmons','trend.Ben Simmons'),('trend_chiefs','trend.Chiefs'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('quote_you','quote'),('repost_just','repost'),
    ('trend_raiders','trend.Raiders'),('trend_vsfashionshow','trend.#VSFashionShow'),('trend_mcvay','trend.McVay'),('trend_herbert','trend.Herbert'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""    for _x in sources:
        if str(_x) in ('trend.World Series',""","""    for _x in sources:
        if str(_x) in ('trend.Raiders','trend.McVay','trend.Herbert','trend.#RaiderNation','trend.Harbaugh','trend.Tre Tucker','trend.Aaron Donald','trend.Tate'): return 'sports'  # 0006Z
        if str(_x) in ('trend.#VSFashionShow','trend.#VictoriasSecretFashionShow','trend.#VSFS2026'): return 'life'  # 0006Z: Victoria's Secret Fashion Show (fashion is life)
        if str(_x) in ('trend.World Series',""")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",count=2)
R("if _c.endswith('2306Z.json') and '/18/' in _c: continue","if _c.endswith('0006Z.json') and '/19/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("(23Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
  "and, as 00Z is a fourth hour, the rest of the posts first captured in the last 24 hours, slowest growing last; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
OLDV=re.search(r"    'sources: references followed two hops.*?screened by id with global floor/pace',\n",s,re.S).group(0)
R(OLDV,"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Raiders, #VSFashionShow, McVay, Herbert (each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2306Z; McVay and Herbert are the Rams and Chargers games; #VSFashionShow and #VictoriasSecretFashionShow are one event, so one was read); quote/repost words the/this/you + just; sensors news/money/science; desks politics/entertainment/sports/internet/music/gaming/offbeat/world/justice/markets; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',\n""")
R("""'3 quote pages + 1 repost page, common words "is", "my", "it" and "that": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'""",
  """'3 quote pages + 1 repost page, common words "the", "this", "you" and "just": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""")
R("""        _last = '2026-10-18T2203Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 2102Z); news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-18T2306Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 2203Z); culture/sports/online last read in {_last}, next run',[]))""")
R("""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 2203Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 2102Z, due at 01:02Z)'""",
"""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 2306Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 2306Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 2102Z, due at 01:02Z)'""")
OLDR=re.search(r"            f'Daytime run at 7:06 PM ET.*?f'No new request:",s,re.S).group(0)
R(OLDR,"""            f'Daytime run at 8:06 PM ET (00:06 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads; first run of the new UTC day, which reset at 00:00): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour, so the rest of the last 24 hours was added, slowest last; under the 400 cap, none left out; 4 reads); trends US+WW (2 reads); '
            f'trend names Raiders, #VSFashionShow, McVay, Herbert (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 2306Z; McVay and Herbert are the Rams and Chargers games; #VictoriasSecretFashionShow is the same event as #VSFashionShow and was not read separately); quote/repost words the/this/you + just (3+1); '
            f'sensors news/money/science (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour music, gaming, offbeat, world, justice, markets last read 2203Z); ai/tech/medicine and four-hour science/ideas/life (2306Z) and four-hour defense/disaster/business (2102Z, due 01:02Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (2111478987923067039, not authorised in earlier runs, was not read again); search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request:""")
R("every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '\n            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '",
  "every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '\n            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '")
R("out_path = f'{REPO}/capture/2026/10/18/2306Z.json'","out_path = f'{REPO}/capture/2026/10/19/0006Z.json'")
open('build_capture.py','w').write(s)
print('ok')
