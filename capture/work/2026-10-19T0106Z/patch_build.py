import re
s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    if count==1: assert n==1,('multi',a[:80],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0006Z.json from saved X outputs."""','"""Build capture/2026/10/19/0106Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0006Z'","capture/work/2026-10-19T0106Z'")
R("RUN_ID = '2026-10-19T0006Z'","RUN_ID = '2026-10-19T0106Z'")
R("STARTED = '2026-10-19T00:06:00Z'","STARTED = '2026-10-19T01:06:00Z'")
R("OBS_AT = '2026-10-19T00:07:00Z'","OBS_AT = '2026-10-19T01:07:00Z'")
R("READS_BEFORE = 1000","READS_BEFORE = 969")
R("datetime(2026,10,19,0,9,tzinfo=timezone.utc)","datetime(2026,10,19,1,17,tzinfo=timezone.utc)")
R("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',
    'repost_just': 'repost_just.txt',
    'trend_raiders': 'trend_raiders.txt', 'trend_vsfashionshow': 'trend_vsfashionshow.txt', 'trend_mcvay': 'trend_mcvay.txt', 'trend_herbert': 'trend_herbert.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_and': 'quote_and.txt', 'quote_it': 'quote_it.txt', 'quote_what': 'quote_what.txt',
    'repost_my': 'repost_my.txt',
    'trend_kylie': 'trend_kylie.txt', 'trend_jordanlove': 'trend_jordanlove.txt', 'trend_megan': 'trend_megan.txt', 'trend_deewinters': 'trend_deewinters.txt', 'trend_bensimmons': 'trend_bensimmons.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
R("if d['id'] in ('politics','entertainment','sports','internet','music','gaming','offbeat','world','justice','markets')]","if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','defense','disaster','business')]")
R("""    ('quote_the','quote'),('quote_this','quote'),('quote_you','quote'),('repost_just','repost'),
    ('trend_raiders','trend.Raiders'),('trend_vsfashionshow','trend.#VSFashionShow'),('trend_mcvay','trend.McVay'),('trend_herbert','trend.Herbert'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_and','quote'),('quote_it','quote'),('quote_what','quote'),('repost_my','repost'),
    ('trend_kylie','trend.Kylie'),('trend_jordanlove','trend.Jordan Love'),('trend_megan','trend.Megan'),('trend_deewinters','trend.Dee Winters'),('trend_bensimmons','trend.Ben Simmons'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
R("""    for _x in sources:
        if str(_x) in ('trend.Raiders',""","""    for _x in sources:
        if str(_x) in ('trend.Jordan Love','trend.Dee Winters','trend.Matthew Golden','trend.#DallasCowboys','trend.#GoPackGo','trend.Ben Simmons'): return 'sports'  # 0106Z: Cowboys v Packers SNF; Ben Simmons Achilles
        if str(_x) in ('trend.Kylie','trend.Megan'): return 'life'  # 0106Z: Kylie Jenner and Megan Thee Stallion at the Victoria's Secret Fashion Show (fashion is life)
        if str(_x) in ('trend.Raiders',""")
R("if _c.endswith('0006Z.json') and '/19/' in _c: continue","if _c.endswith('0106Z.json') and '/19/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("and, as 00Z is a fourth hour, the rest of the posts first captured in the last 24 hours, slowest growing last; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
  "(01Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
OLDV=re.search(r"    'sources: references followed two hops.*?screened by id with global floor/pace',\n",s,re.S).group(0)
R(OLDV,"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Kylie, "Jordan Love", Megan, "Dee Winters", "Ben Simmons" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0006Z; Kylie and Megan are the Victoria\\'s Secret Fashion Show, "Jordan Love" and "Dee Winters" the Cowboys v Packers game); quote/repost words and/it/what + my ("and" quoted, as X rejects it bare); sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/defense/disaster/business; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',\n""")
R("""'3 quote pages + 1 repost page, common words "the", "this", "you" and "just": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""",
  """'3 quote pages + 1 repost page, common words "and", "it", "what" and "my": ("and" lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (my lang:en is:retweet), newest first, 25 each'""")
R("""        _last = '2026-10-18T2306Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run (last read in 2203Z); culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T0006Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 2306Z); news/money/science last read in {_last}, next run',[]))""")
R("""        if d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 2306Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 2306Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 2102Z, due at 01:02Z)'""",
"""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 0006Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 2306Z, due at 03:06Z)'""")
OLDR=re.search(r"            f'Daytime run at 8:06 PM ET.*?f'No new request:",s,re.S).group(0)
R(OLDR,"""            f'Daytime run at 9:06 PM ET (01:06 UTC Oct 19; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0006Z run ended at 969, so no reads were used elsewhere between the runs; one read was lost to the bare word and, rejected by X as ambiguous and retried quoted; eleven search calls were first refused with HTTP 429 on the shared X access, no data and no reads used, and succeeded when repeated about five minutes later). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 01Z is not a fourth hour; under the 400 cap, none left out; 4 reads); trends US+WW (2 reads); '
            f'trend names Kylie, "Jordan Love", Megan, "Dee Winters", "Ben Simmons" (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 0006Z; Kylie and Megan are the Victoria\\'s Secret Fashion Show, "Jordan Love" and "Dee Winters" the Cowboys v Packers game); quote/repost words and/it/what + my (4+1, one lost); '
            f'sensors culture/sports/online (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour ai, tech, medicine last read 2306Z; four-hour defense, disaster, business last read 2102Z); music/gaming/offbeat/world/justice/markets (0006Z) and four-hour science/ideas/life (2306Z, due 03:06Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (2084792384370680094 came back Not Found and was not read again); search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request:""")
R("every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '\n            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '",
  "every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '\n            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '")
R("out_path = f'{REPO}/capture/2026/10/19/0006Z.json'","out_path = f'{REPO}/capture/2026/10/19/0106Z.json'")
open('build_capture.py','w').write(s)
print('ok')
