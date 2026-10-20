s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b,1)
rep('"""Build capture/2026/10/20/0801Z.json','"""Build capture/2026/10/20/0906Z.json')
rep("capture/work/2026-10-20T0801Z'","capture/work/2026-10-20T0906Z'")
rep("RUN_ID = '2026-10-20T0801Z'","RUN_ID = '2026-10-20T0906Z'")
rep("STARTED = '2026-10-20T08:01:00Z'","STARTED = '2026-10-20T09:06:00Z'")
rep("OBS_AT = '2026-10-20T08:01:00Z'","OBS_AT = '2026-10-20T09:06:00Z'")
rep("READS_BEFORE = 794","READS_BEFORE = 774")
rep("datetime(2026,10,20,8,6,tzinfo=timezone.utc)","datetime(2026,10,20,9,10,tzinfo=timezone.utc)")
rep("""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_it': 'repost_it.txt',
    'trend_jaydendaniels': 'trend_jaydendaniels.txt', 'trend_angelreese': 'trend_angelreese.txt', 'trend_danquinn': 'trend_danquinn.txt', 'trend_fredwarner': 'trend_fredwarner.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""",
"""    'quote_my': 'quote_my.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_rays': 'trend_rays.txt', 'trend_endsars': 'trend_endsars.txt', 'trend_cyberpunkedgerunners2': 'trend_cyberpunkedgerunners2.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""")
rep("""    ('quote_you','quote'),('quote_and','quote'),('repost_it','repost'),
    ('trend_jaydendaniels','trend.Jayden Daniels'),('trend_angelreese','trend.Angel Reese'),('trend_danquinn','trend.Dan Quinn'),('trend_fredwarner','trend.Fred Warner'),""",
"""    ('quote_my','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_rays','trend.Rays'),('trend_endsars','trend.#EndSARS'),('trend_cyberpunkedgerunners2','trend.#CyberpunkEdgerunners2'),""")
rep("        if str(_x) in ('trend.Monday Night Football','trend.Kittle'): return 'sports'",
    "        if str(_x) == 'trend.#EndSARS': return 'world'  # 0906Z: EndSARS anniversary in Nigeria\n        if str(_x) == 'trend.#CyberpunkEdgerunners2': return 'entertainment'  # 0906Z: Cyberpunk Edgerunners 2 anime\n        if str(_x) in ('trend.Monday Night Football','trend.Kittle'): return 'sports'")
rep("    if _c.endswith('0801Z.json') and '/20/' in _c: continue","    if _c.endswith('0906Z.json') and '/20/' in _c: continue")
rep("then the rest of the last 24 hours, slowest growing last (08Z is a fourth hour; the 400 cap left out the 74 slowest-growing of that tier)","(09Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap)")
rep("""trend names "Jayden Daniels", "Angel Reese", "Dan Quinn", "Fred Warner" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the four of the current top-ten US names with no posts attached in 0704Z); quote/repost words you/"and" + it; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (100 first-hop, then the other 14 first-hop and 23 second-hop);""",
"""trend names Rays, #EndSARS, #CyberpunkEdgerunners2 (each "<name> lang:en is:retweet", newest first, 25 each; three of the five current top-ten US names with no posts attached in 0801Z, Niners and "Good Tuesday" not read for the budget); quote/repost words my/that + just; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (89 first-hop, then 18 second-hop);""")
rep("""'2 quote pages + 1 repost page (overnight budget), common words "you", "and" and "it": (you lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each (a first, unquoted and read was rejected by X as an ambiguous keyword)'""",
"""'2 quote pages + 1 repost page (overnight budget), common words "my", "that" and "just": (my lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each'""")
rep("'four-hour desk due since 07:08Z (last ok 2026-10-20T0308Z) but cut for the overnight budget (06:00-11:00 UTC, up to 20 reads; four-hour desks are cut first)' if d in ('defense','disaster','business','science','ideas','life') else 'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut for the third run for the overnight budget (06:00-11:00 UTC, up to 20 reads)'",
    "'four-hour desk due since 07:08Z (last ok 2026-10-20T0308Z) but cut for the second run for the overnight budget (06:00-11:00 UTC, up to 20 reads; four-hour desks are cut first)' if d in ('defense','disaster','business','science','ideas','life') else 'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut for the fourth run for the overnight budget (06:00-11:00 UTC, up to 20 reads)'")
rep("f'Overnight run (4:01 AM ET Oct 20 / 08:01 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the first read of this run reported 793 left, so 794 before it; the 0704Z run recorded 793), including one read X rejected (an unquoted and stream, see CAPABILITIES.md 2026-10-15T0708Z), parallel batches of up to 11, no 429 refusals. '",
    "f'Overnight run (5:06 AM ET Oct 20 / 09:06 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0801Z run ended at 774), parallel batches of up to 10, no 429 refusals. '")
rep("08Z is a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list, then the rest of the last 24 hours slowest growing last; the 400 cap left out the 74 slowest-growing; 4 reads)",
    "09Z is not a fourth hour: the watch.json, six-hour and still-gaining tiers, then the {len(ADDED_STORY)} posts cited on the pulse or in a published story that were not otherwise on the list; under the 400 cap; 4 reads)")
rep("""f'trend names "Jayden Daniels", "Angel Reese", "Dan Quinn", "Fred Warner" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; the four of the current top-ten US names with no posts attached in 0704Z; Jayden Daniels, Dan Quinn and Fred Warner are one event with 49ers, Niners, Commanders and Mike Evans, Commanders at 49ers on Monday Night Football; Rays and #WorldSeries are one event, Rays v Brewers World Series); '""",
"""f'trend names Rays, #EndSARS, #CyberpunkEdgerunners2 (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; three of the five current top-ten US names with no posts attached in 0801Z, Niners and "Good Tuesday" not read for the budget; Niners is one event with 49ers, Jayden Daniels, Dan Quinn, Fred Warner, Commanders and Mike Evans, Commanders at 49ers on Monday Night Football; Rays and #WorldSeries are one event, Rays v Brewers World Series); '""")
rep("f'quote/repost words you/\"and\" + it (3 reads plus the rejected unquoted and read, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '",
    "f'quote/repost words my/that + just (3 reads, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '")
rep("f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z, due 06:00Z) cut for the third run and the four-hour desks (last ok 0308Z, due 07:08Z) cut, both for the overnight budget; '",
    "f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z, due 06:00Z) cut for the fourth run and the four-hour desks (last ok 0308Z, due 07:08Z) cut for the second run, both for the overnight budget; '")
rep("unread first-hop (a 100-id read, then the other 14 with the second hop; 2108062331095908717 Not Found again as a referenced post)","unread first-hop (one 89-id read; 2108062331095908717 Not Found again and 2112024103037386860 Not Found as referenced posts)")
rep("out_path = f'{REPO}/capture/2026/10/20/0801Z.json'","out_path = f'{REPO}/capture/2026/10/20/0906Z.json'")
open('build_capture.py','w').write(s); print('ok')
