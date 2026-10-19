s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count,('count',a[:90],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0509Z.json from saved X outputs."""','"""Build capture/2026/10/19/0603Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0509Z'","capture/work/2026-10-19T0603Z'")
R("RUN_ID = '2026-10-19T0509Z'","RUN_ID = '2026-10-19T0603Z'")
R("STARTED = '2026-10-19T05:09:00Z'","STARTED = '2026-10-19T06:03:00Z'")
R("OBS_AT = '2026-10-19T05:10:00Z'","OBS_AT = '2026-10-19T06:04:00Z'")
R("READS_BEFORE = 841","READS_BEFORE = 810")
R("datetime(2026,10,19,5,14,tzinfo=timezone.utc)","datetime(2026,10,19,6,7,tzinfo=timezone.utc)")
R("""    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt', 'quote_my': 'quote_my.txt',
    'repost_that': 'repost_that.txt',
    'trend_dakprescott': 'trend_dakprescott.txt', 'trend_schotty': 'trend_schotty.txt', 'trend_jordanlove': 'trend_jordanlove.txt', 'trend_rams': 'trend_rams.txt', 'trend_lagranjagala': 'trend_lagranjagala.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""",
"""    'quote_it': 'quote_it.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_gopackgo': 'trend_gopackgo.txt', 'trend_jerry': 'trend_jerry.txt', 'trend_greenbay': 'trend_greenbay.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
R("if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','defense','disaster','business')]","if d['id'] in ('politics','entertainment','sports','internet')]")
R("""    ('quote_is','quote'),('quote_you','quote'),('quote_my','quote'),('repost_that','repost'),
    ('trend_dakprescott','trend.Dak Prescott'),('trend_schotty','trend.Schotty'),('trend_jordanlove','trend.Jordan Love'),('trend_rams','trend.Rams'),('trend_lagranjagala','trend.#LaGranjaGala'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_it','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_gopackgo','trend.#GoPackGo'),('trend_jerry','trend.Jerry'),('trend_greenbay','trend.Green Bay'),""")
R("""        if str(_x) in ('trend.#LaGranjaGala',): return 'entertainment'  # 0509Z""","""        if str(_x) in ('trend.Jerry',): return 'sports'  # 0603Z: Jerry Jones, Cowboys v Packers
        if str(_x) in ('trend.#LaGranjaGala',): return 'entertainment'  # 0509Z""")
R("if _c.endswith('0509Z.json') and '/19/' in _c: continue","if _c.endswith('0603Z.json') and '/19/' in _c: continue")
R("(05Z is not a fourth hour, so the rest","(06Z is not a fourth hour, so the rest")
R("""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "Dak Prescott", Schotty, "Jordan Love", Rams, #LaGranjaGala (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0404Z; "Dak Prescott", Schotty and "Jordan Love" are the Cowboys v Packers game, Rams the NFL team, #LaGranjaGala the La Granja VIP reality-show gala; GOTI cut after the five-name budget); quote/repost words is/you/my + that; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/defense/disaster/business; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',""",
"""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #GoPackGo, Jerry, "Green Bay" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0509Z; all three are one event, the Cowboys v Packers Sunday Night Football game, Jerry being Cowboys owner Jerry Jones; Pickens cut for the overnight budget); quote/repost words it/just + what; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',""")
R("""'3 quote pages + 1 repost page, common words "is", "you", "my" and "that": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each',""",
"""'2 quote pages + 1 repost page, common words "it", "just" and "what": (it lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',""")
R("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""","""SENSOR_Q = {}
SENSOR_READ = set()""")
R("""        _last = '2026-10-19T0404Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 0304Z); news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T0404Z' if g in ('news','money','science') else '2026-10-19T0509Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (overnight band, up to 20 reads; sensors are not in the overnight list); last read in {_last}',6,'skipped',f'cut for the overnight read budget (06:00-11:00 UTC: re-reads, trends, both global sweeps, the hourly desks); last read in {_last}',[]))""")
R("""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 0404Z, due at 06:04Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z)'
        else:
            reason = 'not due this run'""",
"""        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'due (two-hour desk, last ok 2026-10-19T0404Z, due 06:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0509Z, due at 07:09Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, read in 0509Z, due at 09:09Z)'
        else:
            reason = 'not due this run'""")
import re
i=s.index("            f'Daytime run at 1:09 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Overnight run at 2:03 AM ET (06:03 UTC Oct 19; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0509Z run ended at 810, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 06Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names #GoPackGo, Jerry, "Green Bay" (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these and Pickens had no posts attached in 0509Z; all one event, the Cowboys v Packers Sunday Night Football game, Jerry being Cowboys owner Jerry Jones; Pickens cut for the overnight budget); quote/repost words it/just + what (3 reads); '
            f'hourly desks politics, entertainment, sports, internet (4 reads; two-hour music, gaming, offbeat, world, justice, markets due 06:04Z but cut for the overnight budget; ai, tech, medicine, science, ideas, life, defense, disaster, business not due); '
            f'two screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (the second read also took the three first-hop ids left over from the first). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the overnight budget: sensors, story clusters, volume, context.top, media descriptions; x_stories omitted. '
"""+s[j:]
R("out_path = f'{REPO}/capture/2026/10/19/0509Z.json'","out_path = f'{REPO}/capture/2026/10/19/0603Z.json'")
open('build_capture.py','w').write(s)
print('patched')
