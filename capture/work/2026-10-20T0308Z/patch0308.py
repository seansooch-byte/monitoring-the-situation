s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:120]
    s=s.replace(a,b,count)
rep("capture/2026/10/20/0200Z.json from","capture/2026/10/20/0308Z.json from")
rep("work/2026-10-20T0200Z'","work/2026-10-20T0308Z'")
rep("RUN_ID = '2026-10-20T0200Z'","RUN_ID = '2026-10-20T0308Z'")
rep("STARTED = '2026-10-20T02:00:00Z'","STARTED = '2026-10-20T03:08:00Z'")
rep("OBS_AT = '2026-10-20T02:01:00Z'","OBS_AT = '2026-10-20T03:09:00Z'")
rep("READS_BEFORE = 958","READS_BEFORE = 923")
rep("datetime(2026,10,20,2,2,tzinfo=timezone.utc)","datetime(2026,10,20,3,10,tzinfo=timezone.utc)")
rep("""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_just': 'repost_just.txt',
    'trend_jaydendaniels': 'trend_jaydendaniels.txt', 'trend_danquinn': 'trend_danquinn.txt', 'trend_wweraw': 'trend_wweraw.txt', 'trend_mikeevans': 'trend_mikeevans.txt', 'trend_angelreese': 'trend_angelreese.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_it': 'quote_it.txt', 'quote_my': 'quote_my.txt',
    'repost_what': 'repost_what.txt',
    'trend_fredwarner': 'trend_fredwarner.txt', 'trend_rays': 'trend_rays.txt', 'trend_niners': 'trend_niners.txt', 'trend_commanders': 'trend_commanders.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'req_spacexa': 'req_r-2026-10-20-01a.txt', 'req_spacexb': 'req_r-2026-10-20-01b.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]",
    "if d['id'] in ('politics','entertainment','sports','internet','defense','disaster','business','science','ideas','life')]")
s0=s.count("('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_just','repost'),")
rep("""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_just','repost'),
    ('trend_jaydendaniels','trend.Jayden Daniels'),('trend_danquinn','trend.Dan Quinn'),('trend_wweraw','trend.#WWERaw'),('trend_mikeevans','trend.Mike Evans'),('trend_angelreese','trend.Angel Reese'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""",
"""    ('quote_the','quote'),('quote_it','quote'),('quote_my','quote'),('repost_what','repost'),
    ('trend_fredwarner','trend.Fred Warner'),('trend_rays','trend.Rays'),('trend_niners','trend.Niners'),('trend_commanders','trend.Commanders'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("        if str(_x) in ('trend.Jayden Daniels',",
    "        if str(_x) in ('trend.Fred Warner','trend.Rays','trend.Niners','trend.Commanders'): return 'sports'  # 0308Z: 49ers v Commanders MNF (Fred Warner helmet hit, Niners, Commanders); Rays clinch the AL pennant\n        if str(_x) in ('trend.Jayden Daniels',")
rep("for a,b in [('Jayden Daniels','Dan Quinn'),","for a,b in [('Fred Warner','Niners'),('Niners','Fred Warner'),('Niners','Commanders'),('Commanders','Niners'),('Fred Warner','Commanders'),('Commanders','Fred Warner'),('Niners','49ers'),('Commanders','49ers'),('Rays','Junior Caminero'),('Rays','Yandy Diaz'),('Jayden Daniels','Dan Quinn'),")
rep("if _c.endswith('0200Z.json') and '/20/' in _c: continue","if _c.endswith('0308Z.json') and '/20/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}")
rep("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}")
rep("""        _last = '2026-10-20T0004Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-20T0200Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""")
rep("""        reason = 'not due this run (four-hour desk, last ok 2026-10-19T2209Z, due 02:09Z; this run started 02:00Z)'""",
"""        reason = 'not due this run (two-hour desk, last ok 2026-10-20T0200Z, due 04:00Z)'""")
rep("(02Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;",
    "(03Z is not a fourth hour, so the rest of the last 24 hours was not added); no ids left out by the 400 cap;")
rep("""trend names "Jayden Daniels", "Dan Quinn", #WWERaw, "Mike Evans", "Angel Reese" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; none of the current top-ten US names had posts attached in 0004Z, the last capture; five read for the budget, Terry, 49ers, Brock Purdy, #RaiseHail and Diggs not read); quote/repost words this/is/you + just; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet and the two-hour desks world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop);""",
    """trend names "Fred Warner", Rays, Niners, Commanders (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the four of the current top-ten US names with no posts attached in 0200Z); quote/repost words the/it/my + what; sensors news/money/science; hourly desks politics/entertainment/sports/internet and the four-hour desks defense/disaster/business/science/ideas/life; three screening reads by id of unread referenced posts (two first-hop, one second-hop);""")
rep("""'3 quote pages + 1 repost page, common words "this", "is", "you" and "just": (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""",
    """'3 quote pages + 1 repost page, common words "the", "it", "my" and "what": (the lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""")
i=s.index("            f'Late evening run (10:00 PM ET"); j=s.index("            f'three screening reads by id:",i)
s=s[:i]+"""            f'Late evening run (the hourly trigger fired late: 11:08 PM ET Oct 19 / 03:08 UTC Oct 20; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0200Z run ended at 923), parallel batches of up to 12, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 03Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; 4 reads); trends US+WW (2 reads); '
            f'trend names "Fred Warner", Rays, Niners, Commanders (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; the four of the current top-ten US names with no posts attached in 0200Z; Fred Warner, Niners, Commanders, 49ers, Jayden Daniels and Dan Quinn are one event, Commanders at 49ers on Monday Night Football; Rays, Junior Caminero and Yandy Diaz are one event, the Rays clinching the American League pennant and a World Series against the Brewers); '
            f'quote/repost words the/it/my + what (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 0200Z); '
            f'10 desk reads: hourly politics, entertainment, sports, internet and the four-hour desks defense, disaster, business, science, ideas, life (last ok 2209Z, due 02:09Z); the two-hour desks were read in 0200Z and are due 04:00Z; '
"""+s[j:]
rep("(a 100-id read and a 67-id read)","(a 100-id read and a 30-id read)")
rep("""            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2026-10-18T2203Z) and was not read again. '""",
    """            f'New request r-2026-10-20-01 answered with two searches (2 reads, relevancy, from 2026-10-19T07:50Z); every other open request was answered in an earlier capture and was not read again. '""")
rep("out_path = f'{REPO}/capture/2026/10/20/0200Z.json'","out_path = f'{REPO}/capture/2026/10/20/0308Z.json'")
rep("""REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()""","""REQ_PICKS = {'r-2026-10-20-01': ['2112323120380129562','2112286669508694289','2112256359022362891','2112227716183277635','2112211740884975910']}
REQ_FILES = {'r-2026-10-20-01': 'req_spacexa'}
REQ_ONLY = ({t['id'] for t in (raw['req_spacexa'].get('data') or [])} | {t['id'] for t in (raw['req_spacexb'].get('data') or [])}) - set(REQ_PICKS['r-2026-10-20-01']) - {'2112089556615123114'}""")
rep("""    'r-2026-10-18-02': 'two search_posts_all reads""","""    'r-2026-10-20-01': 'two search_posts_all reads, start_time 2026-10-19T07:50:00Z, relevancy, 25 results each: ("SpaceX shares" OR "SpaceX share" OR "SpaceX stock") (kids OR kid OR children OR "Trump Accounts" OR "Trump Account" OR Treasury OR eligible OR eligibility) -is:retweet -is:reply; and (from:SpaceX OR from:USTreasury OR from:SecScottBessent OR from:TrumpAccounts OR from:elonmusk) (shares OR share OR kids OR children OR "Trump Accounts" OR account OR eligible) -is:retweet',
    'r-2026-10-18-02': 'two search_posts_all reads""")
rep("""ANSWERS = []
capture = {""","""ANSWERS = [{
    'request_id': 'r-2026-10-20-01',
    'status': 'ok',
    'post_ids': [i for i in REQ_PICKS['r-2026-10-20-01'] if i in _here],
    'note': 'Two searches from 2026-10-19T07:50Z (relevancy). No post from SpaceX or from the Trump Accounts account (@TrumpAccounts) was returned, and no post gave a mechanism, timetable or eligibility rule for the shares. Kept: SecScottBessent (2112323120380129562), the Treasury Secretary thanking Musk, saying more than $8 billion has already been deposited into children\\'s accounts and this donation will push that higher, and pointing parents to the Trump Accounts app to claim an account; DeItaone (2112286669508694289), headline that President Trump thanked Musk for pledging SpaceX shares to millions of children through Trump Accounts; rosewdc (2112256359022362891), a report (source link in the post) that Treasury rules let charities donate individual stocks to children\\'s Trump Accounts, that parents cannot refuse the contributions and the stocks cannot be sold for five years, and that Musk gave no indication how the shares would be distributed; dlcampbell05 (2112227716183277635), a summary citing CNBC (reached out to SpaceX and Musk\\'s family office for details; no details on timing, eligibility or how families would claim a share), CBS News (the shares could go through Trump Accounts, for children born 2025 through 2028) and CNN; elonmusk (2112211740884975910), Musk replying that giving shares directly to the people is the way. The pledge post itself (2112089556615123114) is on requests/watch.json and was re-read in watch.'
}]
capture = {""")
rep("# 5) request picks (none this run)","# 5) request picks (r-2026-10-20-01)")
open('build_capture.py','w').write(s)
print('ok')
