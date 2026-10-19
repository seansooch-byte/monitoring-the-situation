s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b) if count==0 else s.replace(a,b,count)
import re as _r
rep("2026-10-19T1410Z'","2026-10-19T1519Z'",0)
rep('capture/2026/10/19/1410Z.json from','capture/2026/10/19/1519Z.json from')
rep("STARTED = '2026-10-19T14:10:00Z'","STARTED = '2026-10-19T15:19:00Z'")
rep("OBS_AT = '2026-10-19T14:11:00Z'","OBS_AT = '2026-10-19T15:21:00Z'")
rep("READS_BEFORE = 625","READS_BEFORE = 590")
s=_r.sub(r"READS_USED = 35  #[^\n]*","READS_USED = 25  # this run's X calls (590 to 565 left today); no 429 refusals",s,1)
rep("datetime(2026,10,19,14,18,tzinfo=timezone.utc)","datetime(2026,10,19,15,24,tzinfo=timezone.utc)")
rep("""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_chrisballard': 'trend_chrisballard.txt', 'trend_idontwant': 'trend_idontwant.txt', 'trend_papergames': 'trend_papergames.txt', 'trend_carlie': 'trend_carlie.txt', 'trend_mondaymotivation': 'trend_mondaymotivation.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_jalen': 'trend_jalen.txt', 'trend_chrisbosh': 'trend_chrisbosh.txt', 'trend_victorymonday': 'trend_victorymonday.txt', 'trend_dwightpowell': 'trend_dwightpowell.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("if d['id'] in ('politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','music','gaming','offbeat')]",
    "if d['id'] in ('politics','entertainment','sports','internet')]")
rep("""    ('quote_it','quote'),('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_chrisballard','trend.Chris Ballard'),('trend_idontwant','trend.#IDontWantToOverreactBUT'),('trend_papergames','trend.#PapergamesIsCyberMurderer'),('trend_carlie','trend.Carlie'),('trend_mondaymotivation','trend.#MondayMotivation'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
]""","""    ('quote_the','quote'),('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_jalen','trend.Jalen'),('trend_chrisbosh','trend.Chris Bosh'),('trend_victorymonday','trend.Victory Monday'),('trend_dwightpowell','trend.Dwight Powell'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
]""")
rep("        if str(_x) in ('trend.Chris Ballard',",
    "        if str(_x) in ('trend.Jalen','trend.Chris Bosh','trend.Dwight Powell'): return 'sports'  # 1519Z\n        if str(_x) in ('trend.Chris Ballard',")
rep("set(open(f'{W}/reread_ids.txt').read().split()[271:])  # 1410Z","set(open(f'{W}/reread_ids.txt').read().split()[277:])  # 1519Z")
rep("if _c.endswith('1410Z.json') and '/19/' in _c: continue","if _c.endswith('1519Z.json') and '/19/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
    "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
rep("(14Z is not a fourth hour, so the rest of the last 24 hours was not added), plus the 105 ids cited in published stories (moments/) that were not otherwise on the list;",
    "(15Z is not a fourth hour, so the rest of the last 24 hours was not added), plus the 105 ids cited in pulse/current.json or in published stories (moments/) that were not otherwise on the list;")
i=s.index("    'sources: references followed two hops"); j=s.index("\n",i)
s=s[:i]+"""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Jalen, "Chris Bosh", "Victory Monday", "Dwight Powell" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these four had no posts attached in 1410Z); quote/repost words the/this/is + you; sensors culture/sports/online; hourly desks politics/entertainment/sports/internet; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"""+s[j:]
i=s.index("    '3 quote pages + 1 repost page"); j=s.index("\n",i)
s=s[:i]+"""    '3 quote pages + 1 repost page, common words "the", "this", "is" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each',"""+s[j:]
rep("""        _last = '2026-10-19T1302Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this run); last read in {_last}',6,'skipped',f'rotation: news/money/science read this run; culture/sports/online last read in {_last}, next run',[]))""",
"""        _last = '2026-10-19T1410Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this run); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run; news/money/science last read in {_last}, next run',[]))""")
rep("""        if d in ('science','ideas','life','defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T1302Z, due 17:02Z)'
        else:""","""        if d in ('science','ideas','life','defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-19T1302Z, due 17:02Z)'
        elif d in ('world','justice','markets','music','gaming','offbeat','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-19T1410Z, due 16:10Z)'
        else:""")
i=s.index("            f'Late morning run at 10:10 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Late morning run at 11:19 AM ET (15:19 UTC Oct 19; the hourly trigger fired late; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 1410Z run ended at 590; calls made in parallel batches of up to 8, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour, so the rest of the last 24 hours was not added; every post cited on the pulse or in a published story was added, 105 of them not otherwise on the list; under the 400 cap; 4 reads); trends US+WW (2 reads); '
            f'trend names Jalen, "Chris Bosh", "Victory Monday", "Dwight Powell" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these four had no posts attached in 1410Z); '
            f'quote/repost words the/this/is + you (4 reads); sensors culture/sports/online (3 reads; news/money/science next rotation, last read 1410Z); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; two-hour desks were read in 1410Z and are not due until 16:10Z; four-hour desks were read in 1302Z and are not due until 17:02Z; '
            f'three screening reads by id: {len([x for x in open(f"{W}/screen_ids.txt").read().split() if x])} unread first-hop and {len([x for x in open(f"{W}/screen_ids_hop2.txt").read().split() if x])} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved in the work folder). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions. '
"""+s[j:]
rep("out_path = f'{REPO}/capture/2026/10/19/1410Z.json'","out_path = f'{REPO}/capture/2026/10/19/1519Z.json'")
open('build_capture.py','w').write(s)
print('ok')
