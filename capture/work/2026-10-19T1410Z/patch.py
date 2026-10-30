s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
import re as _r
rep("2026-10-19T1302Z'","2026-10-19T1410Z'",0)
rep('capture/2026/10/19/1302Z.json from','capture/2026/10/19/1410Z.json from')
rep("STARTED = '2026-10-19T13:02:00Z'","STARTED = '2026-10-19T14:10:00Z'")
rep("OBS_AT = '2026-10-19T13:03:00Z'","OBS_AT = '2026-10-19T14:11:00Z'")
rep("READS_BEFORE = 655","READS_BEFORE = 625")
s=_r.sub(r"READS_USED = 30  #[^\n]*","READS_USED = 35  # this run's X calls (625 to 590 left today); 12 more calls were refused with HTTP 429 and used no read",s,1)
rep("datetime(2026,10,19,13,8,tzinfo=timezone.utc)","datetime(2026,10,19,14,18,tzinfo=timezone.utc)")
rep("""    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_my': 'repost_my.txt',
    'trend_reparations': 'trend_reparations.txt', 'trend_victorymonday': 'trend_victorymonday.txt', 'trend_jpmcoin': 'trend_jpmcoin.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""",
"""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_chrisballard': 'trend_chrisballard.txt', 'trend_idontwant': 'trend_idontwant.txt', 'trend_papergames': 'trend_papergames.txt', 'trend_carlie': 'trend_carlie.txt', 'trend_mondaymotivation': 'trend_mondaymotivation.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','science','ideas','life','defense','disaster','business')]",
    "if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]")
rep("""    ('quote_this','quote'),('quote_is','quote'),('quote_you','quote'),('repost_my','repost'),
    ('trend_reparations','trend.Reparations'),('trend_victorymonday','trend.Victory Monday'),('trend_jpmcoin','trend.JPM Coin'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""","""    ('quote_it','quote'),('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_chrisballard','trend.Chris Ballard'),('trend_idontwant','trend.#IDontWantToOverreactBUT'),('trend_papergames','trend.#PapergamesIsCyberMurderer'),('trend_carlie','trend.Carlie'),('trend_mondaymotivation','trend.#MondayMotivation'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""")
rep("        if str(_x) in ('trend.Victory Monday',): return 'sports'  # 1302Z: NFL teams' Victory Monday posts",
    "        if str(_x) in ('trend.Chris Ballard','trend.Carlie','trend.#IDontWantToOverreactBUT','trend.Colts'): return 'sports'  # 1410Z: Colts fire GM Chris Ballard (Carlie Irsay-Gordon statement); McAfee show hashtag\n        if str(_x) in ('trend.#PapergamesIsCyberMurderer',): return 'gaming'  # 1410Z: Love and Deepspace (Papergames) fan campaign\n        if str(_x) in ('trend.#MondayMotivation',): return 'life'  # 1410Z\n        if str(_x) in ('trend.Victory Monday',): return 'sports'  # 1302Z: NFL teams' Victory Monday posts")
rep("if _c.endswith('1302Z.json') and '/19/' in _c: continue","if _c.endswith('1410Z.json') and '/19/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("(13Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read,",
    "(14Z is not a fourth hour, so the rest of the last 24 hours was not added), plus the 105 ids cited in published stories (moments/) that were not otherwise on the list; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read,")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "Chris Ballard", #IDontWantToOverreactBUT, #PapergamesIsCyberMurderer, Carlie, #MondayMotivation (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 1302Z; Chris Ballard, Carlie and Colts are one event, the Colts firing GM Chris Ballard, so Colts was not read; #BR2049RewardsCyberMurderer and #中国叠纸杀人公司 are the same Papergames campaign as #PapergamesIsCyberMurderer, so only that one was read); quote/repost words it/that/just + what; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine/music/gaming/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "it", "that", "just" and "what": (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',"""+s[j:]
rep("""        _last = '2026-10-19T1203Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T1302Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""")
rep("""        if d in ('world','justice','markets','music','gaming','offbeat','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1203Z, due 14:03Z)'
        else:
            reason = 'not due this run'""","""        if d in ('science','ideas','life','defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T1302Z, due 17:02Z)'
        else:
            reason = 'not due this run'""")
i=s.index("            f'Morning run at 9:02 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Late morning run at 10:10 AM ET (14:10 UTC Oct 19; the hourly trigger fired late; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1302Z run ended at 625; calls made in parallel batches of up to 7; the first batch of 13 searches at 14:12 UTC drew 12 HTTP 429 refusals on the shared X access, which used no reads, and the 12 were sent again a minute later in smaller batches without further refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour, so the rest of the last 24 hours was not added; every post cited in a published story was added, 105 of them not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names "Chris Ballard", #IDontWantToOverreactBUT, #PapergamesIsCyberMurderer, Carlie, #MondayMotivation (5 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these had no posts attached in 1302Z; Chris Ballard, Carlie and Colts are one event, the Colts firing GM Chris Ballard, with a statement from owner Carlie Irsay-Gordon, so Colts was not read; #BR2049RewardsCyberMurderer and #中国叠纸杀人公司 are the same Papergames campaign as #PapergamesIsCyberMurderer); '
            f'quote/repost words it/that/just + what (4 reads); sensors news/money/science (3 reads; culture/sports/online next rotation, last read 1302Z); '
            f'13 desk reads: hourly politics, entertainment, sports, internet; two-hour world, justice, markets, music, gaming, offbeat, ai, tech, medicine (last ok 1203Z, due 14:03Z); four-hour desks were read in 1302Z and are not due until 17:02Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1302Z.json'","out_path = f'{REPO}/capture/2026/10/19/1410Z.json'")
open('build_capture.py','w').write(s)
print('ok')
