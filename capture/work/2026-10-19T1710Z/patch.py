s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
import re as _r
rep("2026-10-19T1620Z'","2026-10-19T1710Z'",0)
rep('capture/2026/10/19/1620Z.json from','capture/2026/10/19/1710Z.json from')
rep("STARTED = '2026-10-19T16:20:00Z'","STARTED = '2026-10-19T17:10:00Z'")
rep("OBS_AT = '2026-10-19T16:22:00Z'","OBS_AT = '2026-10-19T17:11:00Z'")
rep("READS_BEFORE = 565","READS_BEFORE = 530")
s=_r.sub(r"READS_USED = 35  #[^\n]*","READS_USED = 32  # this run's X calls (530 to 498 left today), including one rejected 'and' query; 11 HTTP 429 refusals at 17:12Z used no reads",s,1)
rep("datetime(2026,10,19,16,25,tzinfo=timezone.utc)","datetime(2026,10,19,17,15,tzinfo=timezone.utc)")
rep("""    'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt', 'quote_that': 'quote_that.txt',
    'repost_it': 'repost_it.txt',
    'trend_london': 'trend_london.txt', 'trend_chrisballard': 'trend_chrisballard.txt', 'trend_hardrockbet': 'trend_hardrockbet.txt', 'trend_michaelrobinson': 'trend_michaelrobinson.txt', 'trend_idontwant': 'trend_idontwant.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_just': 'quote_just.txt', 'quote_you': 'quote_you.txt', 'quote_this': 'quote_this.txt',
    'repost_the': 'repost_the.txt',
    'trend_chrisbosh': 'trend_chrisbosh.txt', 'trend_leslie': 'trend_leslie.txt', 'trend_nelson': 'trend_nelson.txt', 'trend_victorymonday': 'trend_victorymonday.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]",
    "if d['id'] in ('politics','entertainment','sports','internet','defense','disaster','business','science','ideas','life')]")
rep("""    ('quote_my','quote'),('quote_what','quote'),('quote_that','quote'),('repost_it','repost'),
    ('trend_london','trend.London'),('trend_chrisballard','trend.Chris Ballard'),('trend_hardrockbet','trend.#HardRockBet'),('trend_michaelrobinson','trend.Michael Robinson'),('trend_idontwant','trend.#IDontWantToOverreactBUT'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""","""    ('quote_just','quote'),('quote_you','quote'),('quote_this','quote'),('repost_the','repost'),
    ('trend_chrisbosh','trend.Chris Bosh'),('trend_leslie','trend.Leslie'),('trend_nelson','trend.Nelson'),('trend_victorymonday','trend.Victory Monday'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""")
rep("        if str(_x) in ('trend.Michael Robinson','trend.#HardRockBet'): return 'sports'  # 1620Z",
    "        if str(_x) in ('trend.Leslie',): return 'politics'  # 1710Z: the stream is mostly Lesley Stahl's 60 Minutes remarks on non-citizen voting\n        if str(_x) in ('trend.Michael Robinson','trend.#HardRockBet'): return 'sports'  # 1620Z")
rep("if _c.endswith('1620Z.json') and '/19/' in _c: continue","if _c.endswith('1710Z.json') and '/19/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("plus the 105 ids cited in pulse/current.json or in published stories (moments/) that were not otherwise on the list, then (16Z is a fourth hour) the rest of the last 24 hours, slowest growing last; {len(watch_ids)} ids at the 400 cap, the 104 slowest-growing posts of the rest of the last 24 hours left out;",
    "(17Z is not a fourth hour, so the rest of the last 24 hours was not added), plus the 105 ids cited in pulse/current.json or in published stories (moments/) that were not otherwise on the list; {len(watch_ids)} ids, under the 400 cap, none left out;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "Chris Bosh", Leslie, Nelson, "Victory Monday" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 1620Z; Chris Bosh is the Jalen Hurts blood-clot story, Leslie is mostly Lesley Stahl of 60 Minutes, Victory Monday is NFL teams after Sunday wins); quote/repost words just/you/this + the; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet and four-hour desks defense/disaster/business/science/ideas/life; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "just", "you", "this" and "the": (just lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (the lang:en is:retweet), newest first, 25 each; a first try with the bare word and was rejected by X as an ambiguous keyword (known, see CAPABILITIES.md) and replaced by this',"""+s[j:]
rep("""        _last = '2026-10-19T1519Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T1620Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('science','ideas','life','defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T1302Z, due 17:02Z)'
        elif d in ('world','justice','markets','music','gaming','offbeat','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1410Z, due 16:10Z)'""",
"""        if d in ('world','justice','markets','music','gaming','offbeat','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1620Z, due 18:20Z)'""")
i=s.index("            f'Midday run at 12:20 PM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Early afternoon run at 1:10 PM ET (17:10 UTC Oct 19; the hourly trigger fired late; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1620Z run ended at 530). The first batch of 11 searches at 17:12 UTC all drew HTTP 429 refusals on the shared X access (no reads used); after a one-minute wait they went out again in batches of up to 6 with no further refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z is not a fourth hour; the watch.json, six-hour and still-gaining tiers plus the 105 posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names "Chris Bosh", Leslie, Nelson, "Victory Monday" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; the only current top-ten US names with no posts attached in 1620Z; Chris Bosh is largely the Jalen Hurts blood-clot story; Leslie is mostly Lesley Stahl of 60 Minutes on non-citizen voting; Nelson is several unrelated people; Victory Monday is NFL teams after Sunday wins); '
            f'quote/repost words just/you/this + the (4 reads, plus 1 read lost to a rejected bare "and" query, a known X quirk); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 1620Z); '
            f'10 desk reads: hourly politics, entertainment, sports, internet; four-hour defense, disaster, business, science, ideas, life (last ok 1302Z, due 17:02Z); two-hour desks were read in 1620Z and are not due until 18:20Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1620Z.json'","out_path = f'{REPO}/capture/2026/10/19/1710Z.json'")
open('build_capture.py','w').write(s)
print('ok')
