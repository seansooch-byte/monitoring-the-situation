import re
s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    assert n==count,('count',a[:80],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0200Z.json from saved X outputs."""','"""Build capture/2026/10/19/0304Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0200Z'","capture/work/2026-10-19T0304Z'")
R("RUN_ID = '2026-10-19T0200Z'","RUN_ID = '2026-10-19T0304Z'")
R("STARTED = '2026-10-19T02:00:00Z'","STARTED = '2026-10-19T03:04:00Z'")
R("OBS_AT = '2026-10-19T02:01:00Z'","OBS_AT = '2026-10-19T03:05:00Z'")
R("READS_BEFORE = 936","READS_BEFORE = 905")
R("datetime(2026,10,19,2,9,tzinfo=timezone.utc)","datetime(2026,10,19,3,12,tzinfo=timezone.utc)")
R("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_cowboys': 'trend_cowboys.txt', 'trend_packers': 'trend_packers.txt', 'trend_matthewgolden': 'trend_matthewgolden.txt', 'trend_vsfashionshow': 'trend_vsfashionshow.txt', 'trend_gopackgo': 'trend_gopackgo.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_jordanlove': 'trend_jordanlove.txt', 'trend_rams': 'trend_rams.txt', 'trend_schotty': 'trend_schotty.txt', 'trend_dakprescott': 'trend_dakprescott.txt', 'trend_kylie': 'trend_kylie.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
R("if d['id'] in ('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]","if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','science','ideas','life')]")
R("""    ('quote_the','quote'),('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_cowboys','trend.Cowboys'),('trend_packers','trend.Packers'),('trend_matthewgolden','trend.Matthew Golden'),('trend_vsfashionshow','trend.#VSFashionShow'),('trend_gopackgo','trend.#GoPackGo'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_that','quote'),('quote_just','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_jordanlove','trend.Jordan Love'),('trend_rams','trend.Rams'),('trend_schotty','trend.Schotty'),('trend_dakprescott','trend.Dak Prescott'),('trend_kylie','trend.Kylie'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""    for _x in sources:
        if str(_x) in ('trend.Cowboys',""","""    for _x in sources:
        if str(_x) in ('trend.Rams',): return 'sports'  # 0304Z: Rams (NFL)
        if str(_x) in ('trend.Cowboys',""")
R("if _c.endswith('0200Z.json') and '/19/' in _c: continue","if _c.endswith('0304Z.json') and '/19/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("(02Z is not a fourth hour,","(03Z is not a fourth hour,")
OLDV=re.search(r"    'sources: references followed two hops.*?screened by id with global floor/pace',\n",s,re.S).group(0)
R(OLDV,"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "Jordan Love", Rams, Schotty, "Dak Prescott", Kylie (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0200Z; "Jordan Love", Schotty and "Dak Prescott" are the Cowboys v Packers game, Kylie the Victoria\\'s Secret Fashion Show); quote/repost words that/just/my + it; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/science/ideas/life; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',\n""")
R("""'3 quote pages + 1 repost page, common words "the", "this", "is" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each'""",
  """'3 quote pages + 1 repost page, common words "that", "just", "my" and "it": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each'""")
R("""        _last = '2026-10-19T0106Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 0006Z); culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T0200Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 0106Z); news/money/science last read in {_last}, next run',[]))""")
R("""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0106Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 0106Z, due at 05:06Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 2306Z, due at 03:06Z)'""",
"""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 0200Z, due at 04:00Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 0106Z, due at 05:06Z)'""")
OLDR=re.search(r"            f'Daytime run at 10:00 PM ET.*?f'Not read for the budget:[^\n]*\n",s,re.S).group(0)
R(OLDR,"""            f'Daytime run at 11:04 PM ET (03:04 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0200Z run ended at 905, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names "Jordan Love", Rams, Schotty, "Dak Prescott", Kylie (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 0200Z; "Jordan Love", Schotty and "Dak Prescott" are one event, the Cowboys v Packers game, Kylie is the Victoria\\'s Secret Fashion Show, Rams the NFL team); quote/repost words that/just/my + it (4 reads); '
            f'sensors culture/sports/online (3 reads); 10 desk reads: hourly politics, entertainment, sports, internet; two-hour ai/tech/medicine (last read 0106Z, due 03:06Z) and four-hour science/ideas/life (last read 2306Z, due 03:06Z) read two minutes early in this run to keep the rotation even; two-hour music/gaming/offbeat/world/justice/markets (0200Z) and four-hour defense/disaster/business (0106Z, due 05:06Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '
""")
R("out_path = f'{REPO}/capture/2026/10/19/0200Z.json'","out_path = f'{REPO}/capture/2026/10/19/0304Z.json'")
open('build_capture.py','w').write(s)
print('ok')
