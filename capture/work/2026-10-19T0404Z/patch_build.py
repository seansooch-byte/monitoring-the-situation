import re
s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    assert n==count,('count',a[:80],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0304Z.json from saved X outputs."""','"""Build capture/2026/10/19/0404Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0304Z'","capture/work/2026-10-19T0404Z'")
R("RUN_ID = '2026-10-19T0304Z'","RUN_ID = '2026-10-19T0404Z'")
R("STARTED = '2026-10-19T03:04:00Z'","STARTED = '2026-10-19T04:04:00Z'")
R("OBS_AT = '2026-10-19T03:05:00Z'","OBS_AT = '2026-10-19T04:05:00Z'")
R("READS_BEFORE = 905","READS_BEFORE = 874")
R("datetime(2026,10,19,3,12,tzinfo=timezone.utc)","datetime(2026,10,19,4,8,tzinfo=timezone.utc)")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',""")
R("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_jordanlove': 'trend_jordanlove.txt', 'trend_rams': 'trend_rams.txt', 'trend_schotty': 'trend_schotty.txt', 'trend_dakprescott': 'trend_dakprescott.txt', 'trend_kylie': 'trend_kylie.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt', 'quote_and': 'quote_and.txt',
    'repost_this': 'repost_this.txt',
    'trend_cowboys': 'trend_cowboys.txt', 'trend_gopackgo': 'trend_gopackgo.txt', 'trend_pickens': 'trend_pickens.txt', 'trend_jerryjones': 'trend_jerryjones.txt', 'trend_dalvsgb': 'trend_dalvsgb.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
R("if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','science','ideas','life')]","if d['id'] in ('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]")
R("""    ('quote_that','quote'),('quote_just','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_jordanlove','trend.Jordan Love'),('trend_rams','trend.Rams'),('trend_schotty','trend.Schotty'),('trend_dakprescott','trend.Dak Prescott'),('trend_kylie','trend.Kylie'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_what','quote'),('quote_the','quote'),('quote_and','quote'),('repost_this','repost'),
    ('trend_cowboys','trend.Cowboys'),('trend_gopackgo','trend.#GoPackGo'),('trend_pickens','trend.Pickens'),('trend_jerryjones','trend.Jerry Jones'),('trend_dalvsgb','trend.#DALvsGB'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""    for _x in sources:
        if str(_x) in ('trend.Rams',): return 'sports'  # 0304Z: Rams (NFL)""","""    for _x in sources:
        if str(_x) in ('trend.Pickens','trend.Jerry Jones'): return 'sports'  # 0404Z: Cowboys v Packers
        if str(_x) in ('trend.Rams',): return 'sports'  # 0304Z: Rams (NFL)""")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",count=2)
R("if _c.endswith('0304Z.json') and '/19/' in _c: continue","if _c.endswith('0404Z.json') and '/19/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("(03Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
  "and, as 04Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
OLDV=re.search(r"    'sources: references followed two hops.*?screened by id with global floor/pace',\n",s,re.S).group(0)
R(OLDV,"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Cowboys, #GoPackGo, Pickens, "Jerry Jones", #DALvsGB (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0304Z; all five are the Cowboys v Packers game); quote/repost words what/the/and + this; sensors news/money/science; desks politics/entertainment/sports/internet/music/gaming/offbeat/world/justice/markets; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',\n""")
R("""'3 quote pages + 1 repost page, common words "that", "just", "my" and "it": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each'""",
  """'3 quote pages + 1 repost page, common words "what", "the", "and" and "this": (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet; the bare word was rejected first as ambiguous and the rejected read counted), (this lang:en is:retweet), newest first, 25 each'""")
R("""        _last = '2026-10-19T0200Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 0106Z); news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T0304Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 0200Z); culture/sports/online last read in {_last}, next run',[]))""")
R("""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 0200Z, due at 04:00Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 0106Z, due at 05:06Z)'""",
"""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0304Z, due at 05:04Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 0106Z, due at 05:06Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z)'""")
OLDR=re.search(r"            f'Daytime run at 11:04 PM ET.*?f'Not read for the budget:[^\n]*\n",s,re.S).group(0)
R(OLDR,"""            f'Daytime run at 12:04 AM ET (04:04 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0304Z run ended at 874, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals; one read was a rejected bare "and" query, see rising.global). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; under the 400 cap, none left out; 4 reads); trends US+WW (2 reads); '
            f'trend names Cowboys, #GoPackGo, Pickens, "Jerry Jones", #DALvsGB (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 0304Z; all five are one event, the Cowboys v Packers game); quote/repost words what/the/and + this (5 reads, one of them the rejected bare "and"); '
            f'sensors news/money/science (3 reads); 10 desk reads: hourly politics, entertainment, sports, internet; two-hour music/gaming/offbeat/world/justice/markets (last read 0200Z, due 04:00Z); two-hour ai/tech/medicine and four-hour science/ideas/life (0304Z) and four-hour defense/disaster/business (0106Z, due 05:06Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '
""")
R("out_path = f'{REPO}/capture/2026/10/19/0304Z.json'","out_path = f'{REPO}/capture/2026/10/19/0404Z.json'")
open('build_capture.py','w').write(s)
print('ok')
