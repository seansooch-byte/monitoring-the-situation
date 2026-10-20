s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b,1)
rep('"""Build capture/2026/10/20/0704Z.json','"""Build capture/2026/10/20/0801Z.json')
rep("capture/work/2026-10-20T0704Z'","capture/work/2026-10-20T0801Z'")
rep("RUN_ID = '2026-10-20T0704Z'","RUN_ID = '2026-10-20T0801Z'")
rep("STARTED = '2026-10-20T07:04:00Z'","STARTED = '2026-10-20T08:01:00Z'")
rep("OBS_AT = '2026-10-20T07:04:00Z'","OBS_AT = '2026-10-20T08:01:00Z'")
rep("READS_BEFORE = 813","READS_BEFORE = 794")
rep("datetime(2026,10,20,7,9,tzinfo=timezone.utc)","datetime(2026,10,20,8,6,tzinfo=timezone.utc)")
rep("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_rays': 'trend_rays.txt', 'trend_niners': 'trend_niners.txt', 'trend_mikeevans': 'trend_mikeevans.txt', 'trend_worldseries': 'trend_worldseries.txt',""",
"""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_it': 'repost_it.txt',
    'trend_jaydendaniels': 'trend_jaydendaniels.txt', 'trend_angelreese': 'trend_angelreese.txt', 'trend_danquinn': 'trend_danquinn.txt', 'trend_fredwarner': 'trend_fredwarner.txt',""")
rep("""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_rays','trend.Rays'),('trend_niners','trend.Niners'),('trend_mikeevans','trend.Mike Evans'),('trend_worldseries','trend.#WorldSeries'),""",
"""    ('quote_you','quote'),('quote_and','quote'),('repost_it','repost'),
    ('trend_jaydendaniels','trend.Jayden Daniels'),('trend_angelreese','trend.Angel Reese'),('trend_danquinn','trend.Dan Quinn'),('trend_fredwarner','trend.Fred Warner'),""")
rep("    if _c.endswith('0704Z.json') and '/20/' in _c: continue","    if _c.endswith('0801Z.json') and '/20/' in _c: continue")
rep("(07Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap)","then the rest of the last 24 hours, slowest growing last (08Z is a fourth hour; the 400 cap left out the 74 slowest-growing of that tier)")
rep("""trend names Rays, Niners, "Mike Evans", #WorldSeries (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the four of the current top-ten US names with no posts attached in 0607Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (96 first-hop, then 16 second-hop);""",
"""trend names "Jayden Daniels", "Angel Reese", "Dan Quinn", "Fred Warner" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the four of the current top-ten US names with no posts attached in 0704Z); quote/repost words you/"and" + it; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (100 first-hop, then the other 14 first-hop and 23 second-hop);""")
rep("""'2 quote pages + 1 repost page (overnight budget), common words "the", "this" and "is": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'""",
"""'2 quote pages + 1 repost page (overnight budget), common words "you", "and" and "it": (you lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each (a first, unquoted and read was rejected by X as an ambiguous keyword)'""")
rep("'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z; this run started 07:04Z)' if d in ('defense','disaster','business','science','ideas','life') else 'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut again for the overnight budget (06:00-11:00 UTC, up to 20 reads)'",
    "'four-hour desk due since 07:08Z (last ok 2026-10-20T0308Z) but cut for the overnight budget (06:00-11:00 UTC, up to 20 reads; four-hour desks are cut first)' if d in ('defense','disaster','business','science','ideas','life') else 'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut for the third run for the overnight budget (06:00-11:00 UTC, up to 20 reads)'")
rep("f'Overnight run (3:04 AM ET Oct 20 / 07:04 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0607Z run ended at 813), parallel batches of up to 11, no 429 refusals. '",
    "f'Overnight run (4:01 AM ET Oct 20 / 08:01 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the first read of this run reported 793 left, so 794 before it; the 0704Z run recorded 793), including one read X rejected (an unquoted and stream, see CAPABILITIES.md 2026-10-15T0708Z), parallel batches of up to 11, no 429 refusals. '")
rep("07Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads)",
    "08Z is a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list, then the rest of the last 24 hours slowest growing last; the 400 cap left out the 74 slowest-growing; 4 reads)")
rep("""f'trend names Rays, Niners, "Mike Evans", #WorldSeries (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; the four of the current top-ten US names with no posts attached in 0607Z; Niners and Mike Evans are one event with 49ers, Jayden Daniels, Dan Quinn, Fred Warner and Commanders, Commanders at 49ers on Monday Night Football; Rays and #WorldSeries are one event, Rays v Brewers World Series); '""",
"""f'trend names "Jayden Daniels", "Angel Reese", "Dan Quinn", "Fred Warner" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; the four of the current top-ten US names with no posts attached in 0704Z; Jayden Daniels, Dan Quinn and Fred Warner are one event with 49ers, Niners, Commanders and Mike Evans, Commanders at 49ers on Monday Night Football; Rays and #WorldSeries are one event, Rays v Brewers World Series); '""")
rep("f'quote/repost words the/this + is (3 reads, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '",
    "f'quote/repost words you/\"and\" + it (3 reads plus the rejected unquoted and read, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '")
rep("f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z) were due 06:00Z but cut again for the overnight budget, the four-hour desks were read in 0308Z and are due 07:08Z (this run started 07:04Z), next run; '",
    "f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z, due 06:00Z) cut for the third run and the four-hour desks (last ok 0308Z, due 07:08Z) cut, both for the overnight budget; '")
rep("unread first-hop (one 96-id read; 2108062331095908717 Not Found again)","unread first-hop (a 100-id read, then the other 14 with the second hop; 2108062331095908717 Not Found again as a referenced post)")
rep("out_path = f'{REPO}/capture/2026/10/20/0704Z.json'","out_path = f'{REPO}/capture/2026/10/20/0801Z.json'")
open('build_capture.py','w').write(s); print('ok')
