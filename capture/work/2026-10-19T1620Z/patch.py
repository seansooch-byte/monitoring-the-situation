s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
import re as _r
rep("2026-10-19T1519Z'","2026-10-19T1620Z'",0)
rep('capture/2026/10/19/1519Z.json from','capture/2026/10/19/1620Z.json from')
rep("STARTED = '2026-10-19T15:19:00Z'","STARTED = '2026-10-19T16:20:00Z'")
rep("OBS_AT = '2026-10-19T15:21:00Z'","OBS_AT = '2026-10-19T16:22:00Z'")
rep("READS_BEFORE = 590","READS_BEFORE = 565")
s=_r.sub(r"READS_USED = 25  #[^\n]*","READS_USED = 35  # this run's X calls (565 to 530 left today); no 429 refusals",s,1)
rep("datetime(2026,10,19,15,24,tzinfo=timezone.utc)","datetime(2026,10,19,16,25,tzinfo=timezone.utc)")
rep("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_jalen': 'trend_jalen.txt', 'trend_chrisbosh': 'trend_chrisbosh.txt', 'trend_victorymonday': 'trend_victorymonday.txt', 'trend_dwightpowell': 'trend_dwightpowell.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_my': 'quote_my.txt', 'quote_what': 'quote_what.txt', 'quote_that': 'quote_that.txt',
    'repost_it': 'repost_it.txt',
    'trend_london': 'trend_london.txt', 'trend_chrisballard': 'trend_chrisballard.txt', 'trend_hardrockbet': 'trend_hardrockbet.txt', 'trend_michaelrobinson': 'trend_michaelrobinson.txt', 'trend_idontwant': 'trend_idontwant.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet')]",
    "if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]")
rep("""    ('quote_the','quote'),('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_jalen','trend.Jalen'),('trend_chrisbosh','trend.Chris Bosh'),('trend_victorymonday','trend.Victory Monday'),('trend_dwightpowell','trend.Dwight Powell'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""","""    ('quote_my','quote'),('quote_what','quote'),('quote_that','quote'),('repost_it','repost'),
    ('trend_london','trend.London'),('trend_chrisballard','trend.Chris Ballard'),('trend_hardrockbet','trend.#HardRockBet'),('trend_michaelrobinson','trend.Michael Robinson'),('trend_idontwant','trend.#IDontWantToOverreactBUT'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""")
rep("        if str(_x) in ('trend.Jalen','trend.Chris Bosh','trend.Dwight Powell'): return 'sports'  # 1519Z",
    "        if str(_x) in ('trend.Michael Robinson','trend.#HardRockBet'): return 'sports'  # 1620Z: NFL Network analyst on Jalen Hurts; sportsbook promo hashtag\n        if str(_x) in ('trend.Jalen','trend.Chris Bosh','trend.Dwight Powell'): return 'sports'  # 1519Z")
rep("if _c.endswith('1519Z.json') and '/19/' in _c: continue","if _c.endswith('1620Z.json') and '/19/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("(15Z is not a fourth hour, so the rest of the last 24 hours was not added), plus the 105 ids cited in pulse/current.json or in published stories (moments/) that were not otherwise on the list; {len(watch_ids)} ids, under the 400 cap, none left out;",
    "plus the 105 ids cited in pulse/current.json or in published stories (moments/) that were not otherwise on the list, then (16Z is a fourth hour) the rest of the last 24 hours, slowest growing last; {len(watch_ids)} ids at the 400 cap, the 104 slowest-growing posts of the rest of the last 24 hours left out;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names London, "Chris Ballard", #HardRockBet, "Michael Robinson", #IDontWantToOverreactBUT (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 1519Z; Colts is the Chris Ballard firing and Good Monday a greeting, so they were not read; Jalen, London, Michael Robinson and Howie are largely one event, Jalen Hurts playing in London with blood clots); quote/repost words my/what/that + it; sensors news/money/science; hourly desks politics/entertainment/sports/internet and two-hour desks world/justice/markets/music/gaming/offbeat/ai/tech/medicine; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "my", "what", "that" and "it": (my lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each',"""+s[j:]
rep("""        _last = '2026-10-19T1410Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T1519Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""")
i=s.index("            f'Late morning run at 11:19 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Midday run at 12:20 PM ET (16:20 UTC Oct 19; the hourly trigger fired late; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1519Z run ended at 565; calls made in parallel batches of up to 10, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is a fourth hour; every post cited on the pulse or in a published story was added after the watch.json, six-hour and still-gaining tiers, 105 of them not otherwise on the list, then 20 of the 124 other posts of the last 24 hours, slowest growing last, until the 400 cap; 104 slowest-growing posts left out; 4 reads); trends US+WW (2 reads); '
            f'trend names London, "Chris Ballard", #HardRockBet, "Michael Robinson", #IDontWantToOverreactBUT (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 1519Z; Colts is the same event as Chris Ballard and Good Monday is a greeting, so neither was read; Jalen, London and Michael Robinson are largely one event, Jalen Hurts playing in London with blood clots in his lungs); '
            f'quote/repost words my/what/that + it (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 1519Z); '
            f'13 desk reads: hourly politics, entertainment, sports, internet; two-hour world, justice, markets, music, gaming, offbeat, ai, tech, medicine (last ok 1410Z, due 16:10Z); four-hour desks were read in 1302Z and are not due until 17:02Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1519Z.json'","out_path = f'{REPO}/capture/2026/10/19/1620Z.json'")
open('build_capture.py','w').write(s)
print('ok')
