import re
s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    assert n==count,('count',a[:80],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0404Z.json from saved X outputs."""','"""Build capture/2026/10/19/0509Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0404Z'","capture/work/2026-10-19T0509Z'")
R("RUN_ID = '2026-10-19T0404Z'","RUN_ID = '2026-10-19T0509Z'")
R("STARTED = '2026-10-19T04:04:00Z'","STARTED = '2026-10-19T05:09:00Z'")
R("OBS_AT = '2026-10-19T04:05:00Z'","OBS_AT = '2026-10-19T05:10:00Z'")
R("READS_BEFORE = 874","READS_BEFORE = 841")
R("datetime(2026,10,19,4,8,tzinfo=timezone.utc)","datetime(2026,10,19,5,14,tzinfo=timezone.utc)")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',""","""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',""")
R("""    'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt', 'quote_and': 'quote_and.txt',
    'repost_this': 'repost_this.txt',
    'trend_cowboys': 'trend_cowboys.txt', 'trend_gopackgo': 'trend_gopackgo.txt', 'trend_pickens': 'trend_pickens.txt', 'trend_jerryjones': 'trend_jerryjones.txt', 'trend_dalvsgb': 'trend_dalvsgb.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_my': 'quote_my.txt',
    'repost_that': 'repost_that.txt',
    'trend_dakprescott': 'trend_dakprescott.txt', 'trend_schotty': 'trend_schotty.txt', 'trend_jordanlove': 'trend_jordanlove.txt', 'trend_rams': 'trend_rams.txt', 'trend_lagranjagala': 'trend_lagranjagala.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
R("if d['id'] in ('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]","if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','defense','disaster','business')]")
R("""    ('quote_what','quote'),('quote_the','quote'),('quote_and','quote'),('repost_this','repost'),
    ('trend_cowboys','trend.Cowboys'),('trend_gopackgo','trend.#GoPackGo'),('trend_pickens','trend.Pickens'),('trend_jerryjones','trend.Jerry Jones'),('trend_dalvsgb','trend.#DALvsGB'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_is','quote'),('quote_you','quote'),('quote_my','quote'),('repost_that','repost'),
    ('trend_dakprescott','trend.Dak Prescott'),('trend_schotty','trend.Schotty'),('trend_jordanlove','trend.Jordan Love'),('trend_rams','trend.Rams'),('trend_lagranjagala','trend.#LaGranjaGala'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""    for _x in sources:
        if str(_x) in ('trend.Pickens','trend.Jerry Jones'): return 'sports'  # 0404Z: Cowboys v Packers""","""    for _x in sources:
        if str(_x) in ('trend.#LaGranjaGala',): return 'entertainment'  # 0509Z: La Granja VIP reality show gala
        if str(_x) in ('trend.Pickens','trend.Jerry Jones'): return 'sports'  # 0404Z: Cowboys v Packers""")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",count=2)
R("if _c.endswith('0404Z.json') and '/19/' in _c: continue","if _c.endswith('0509Z.json') and '/19/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("and, as 04Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
  "(05Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
OLDV=re.search(r"    'sources: references followed two hops.*?screened by id with global floor/pace',\n",s,re.S).group(0)
R(OLDV,"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "Dak Prescott", Schotty, "Jordan Love", Rams, #LaGranjaGala (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0404Z; "Dak Prescott", Schotty and "Jordan Love" are the Cowboys v Packers game, Rams the NFL team, #LaGranjaGala the La Granja VIP reality-show gala; GOTI cut after the five-name budget); quote/repost words is/you/my + that; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/defense/disaster/business; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',\n""")
R("""'3 quote pages + 1 repost page, common words "what", "the", "and" and "this": (what lang:en is:quote -is:retweet), (the lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet; the bare word was rejected first as ambiguous and the rejected read counted), (this lang:en is:retweet), newest first, 25 each'""",
  """'3 quote pages + 1 repost page, common words "is", "you", "my" and "that": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'""")
R("""        _last = '2026-10-19T0304Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 0200Z); culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T0404Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 0304Z); news/money/science last read in {_last}, next run',[]))""")
R("""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0304Z, due at 05:04Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 0106Z, due at 05:06Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z)'""",
"""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 0404Z, due at 06:04Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z)'""")
OLDR=re.search(r"            f'Daytime run at 12:04 AM ET.*?f'Not read for the budget:[^\n]*\n",s,re.S).group(0)
R(OLDR,"""            f'Daytime run at 1:09 AM ET (05:09 UTC Oct 19; 12:00-05:00 UTC band, its last hour, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0404Z run ended at 841, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 05Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names "Dak Prescott", Schotty, "Jordan Love", Rams, #LaGranjaGala (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 0404Z; "Dak Prescott", Schotty and "Jordan Love" are one event, the Cowboys v Packers game, Rams the NFL team, #LaGranjaGala the La Granja VIP reality-show gala; GOTI cut after the five-name budget); quote/repost words is/you/my + that (4 reads); '
            f'sensors culture/sports/online (3 reads); 10 desk reads: hourly politics, entertainment, sports, internet; two-hour ai/tech/medicine (last read 0304Z, due 05:04Z) and four-hour defense/disaster/business (last read 0106Z, due 05:06Z); two-hour music/gaming/offbeat/world/justice/markets (0404Z) and four-hour science/ideas/life (0304Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (2111478987923067039 not read again: not authorised in earlier runs); search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '
""")
R("out_path = f'{REPO}/capture/2026/10/19/0404Z.json'","out_path = f'{REPO}/capture/2026/10/19/0509Z.json'")
open('build_capture.py','w').write(s)
print('ok')
