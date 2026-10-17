s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]); s=s.replace(a,b)
rep("Build capture/2026/10/17/1108Z.json","Build capture/2026/10/17/1202Z.json")
rep("work/2026-10-17T1108Z'","work/2026-10-17T1202Z'")
rep("RUN_ID = '2026-10-17T1108Z'","RUN_ID = '2026-10-17T1202Z'")
rep("STARTED = '2026-10-17T11:08:00Z'","STARTED = '2026-10-17T12:02:00Z'")
rep("OBS_AT = '2026-10-17T11:09:00Z'","OBS_AT = '2026-10-17T12:08:00Z'")
rep("READS_BEFORE = 718","READS_BEFORE = 701")
rep("READS_AFTER = 701","READS_AFTER = 669")
rep("datetime(2026,10,17,11,13,tzinfo","datetime(2026,10,17,12,12,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_goodsat': 'trend_goodsat.txt', 'trend_lingorm': 'trend_lingorm.txt', 'trend_fourth': 'trend_fourth.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_you': 'quote_you.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_james': 'trend_james.txt', 'trend_ideabank': 'trend_ideabank.txt', 'trend_cortis': 'trend_cortis.txt', 'trend_chaowesome': 'trend_chaowesome.txt', 'trend_everton': 'trend_everton.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',""")
rep("DUE = ['politics','entertainment','sports','internet']","DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','sports','internet']")
rep("""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_goodsat','trend.Good Saturday'),('trend_lingorm','trend.#LingOrmBetweenUsConcertD1'),('trend_fourth','trend.KEEP GOING AMAZING FOURTH'),""",
"""    ('quote_you','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_james','trend.JAMES THE ULTIMATE PHENOMENON'),('trend_ideabank','trend.IDEA BANK'),('trend_cortis','trend.#CORTIS_NOLFest2026'),('trend_chaowesome','trend.CHAOWESOME'),('trend_everton','trend.Everton'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x)=='trend.Good Saturday': return 'life'\n",
    "        if str(_x)=='trend.Good Saturday': return 'life'\n        if str(_x) in ('trend.JAMES THE ULTIMATE PHENOMENON','trend.IDEA BANK','trend.#CORTIS_NOLFest2026','trend.CHAOWESOME','trend.#JAMESUnparalleled'): return 'music'\n        if str(_x)=='trend.Everton': return 'sports'\n")
rep("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
_ev=['JAMES THE ULTIMATE PHENOMENON','#JAMESUnparalleled','IDEA BANK','CHAOWESOME','#CORTIS_NOLFest2026','NOL Festival','KEONHO CAPTIVATES THE LENS','IKEONIC','ACEKEON MAKNAE','5TH GEN IT BOY','HOGAN EFFECT']
pairs=[(a,b) for a in _ev for b in _ev if a!=b]
rep("for a,b in [('KEONHO CAPTIVATES THE LENS', 'NOL Festival'),","for a,b in "+repr(pairs)+" + [('KEONHO CAPTIVATES THE LENS', 'NOL Festival'),")
rep("SENSOR_Q = {}\nSENSOR_READ = set()","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("(11Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "and, as 12Z is a fourth hour, the rest of the last 24 hours, slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
TN='''trend names "JAMES THE ULTIMATE PHENOMENON", "IDEA BANK", #CORTIS_NOLFest2026, CHAOWESOME, Everton (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the top-ten US names with no posts attached in 1108Z were "JAMES THE ULTIMATE PHENOMENON", "IDEA BANK", #CORTIS_NOLFest2026, #JAMESUnparalleled, CHAOWESOME, "NOL Festival" and Everton; all but Everton are one event, fan hashtag campaigns for CORTIS and its member James at NOL Festival 2026 (one event with "KEONHO CAPTIVATES THE LENS" and the related names of 0959Z), so #JAMESUnparalleled and "NOL Festival" were not searched separately; Everton is the Chelsea v Everton Premier League match)'''
OLD=s[s.index('trend names "Good Saturday", #LingOrmBetweenUsConcertD1, "KEEP GOING AMAZING FOURTH" (each'):]
OLD=OLD[:OLD.index('(#FourthConcertD2))')+len('(#FourthConcertD2))')]
rep(OLD,TN)
rep("; quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace",
    "; quote/repost words you/my/it + that; sensors news/money/science; desks politics/world/justice/markets/ai/tech/medicine/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace")
rep('''    '2 quote pages + 1 repost page, common words "the", "this" and "is": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each',''',
    '''    '3 quote pages + 1 repost page, common words "you", "my", "it" and "that": (you lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each',''')
rep("""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'due (last ok 2026-10-17T0403Z; two-hour desk, due 06:03Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'
        elif d in ('music','gaming','offbeat'):
            reason = 'due (last ok 2026-10-17T0506Z; two-hour desk, due 07:06Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'
        elif d in ('defense','disaster','business'):
            reason = 'due (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'
        elif d in ('science','ideas','life'):
            reason = 'due (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'""",
"""        if d in ('music','gaming','offbeat'):
            reason = 'due (last ok 2026-10-17T0506Z; two-hour desk, due 07:06Z) but cut by the 10-read desk budget (hourly desks and the earlier-due two-hour desks first)'
        elif d in ('defense','disaster','business'):
            reason = 'due (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z) but cut by the 10-read desk budget (four-hour desks cut first)'
        elif d in ('science','ideas','life'):
            reason = 'due (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z) but cut by the 10-read desk budget (four-hour desks cut first)'""")
i0=s.index("            f'Overnight run at 7:08 AM ET")
i1=s.index("            f'{EXTRA_NOTE} '")
NEWR='''            f'Daytime run at 8:02 AM ET (12:02 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1108Z run ended at 701). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; under the 400 cap, none left out; 4 reads); trends US+WW; '
            f'trend names "JAMES THE ULTIMATE PHENOMENON", "IDEA BANK", #CORTIS_NOLFest2026, CHAOWESOME, Everton (5 reads; the top-ten US names with no posts attached in 1108Z; all but Everton are one event, fan hashtag campaigns for CORTIS and member James at NOL Festival 2026, one event with the Keonho names of 0959Z, so #JAMESUnparalleled and "NOL Festival" were not searched separately; Everton is the Chelsea v Everton match); quote/repost words you/my/it + that (3+1); '
            f'sensors news/money/science; all 10 desk-cap slots (hourly politics, entertainment, sports, internet; two-hour world, justice, markets, ai, tech, medicine, due since 06:03Z); music/gaming/offbeat (due since 07:06Z) and the four-hour desks science/ideas/life (due since 07:08Z) and defense/disaster/business (due since 09:06Z) cut by the 10-read desk cap; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: volume, context.top, media descriptions; culture/sports/online sensors next rotation. '
'''
s=s[:i0]+NEWR+s[i1:]
rep("'method': 'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid)'","'method': 'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid, search_news)'")
rep("out_path = f'{REPO}/capture/2026/10/17/1108Z.json'","out_path = f'{REPO}/capture/2026/10/17/1202Z.json'")
open('build_capture.py','w').write(s); print('ok')
