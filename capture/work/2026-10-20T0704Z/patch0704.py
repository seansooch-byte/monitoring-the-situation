s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, a[:90]
    s=s.replace(a,b,1)
rep('"""Build capture/2026/10/20/0607Z.json','"""Build capture/2026/10/20/0704Z.json')
rep("capture/work/2026-10-20T0607Z'","capture/work/2026-10-20T0704Z'")
rep("RUN_ID = '2026-10-20T0607Z'","RUN_ID = '2026-10-20T0704Z'")
rep("STARTED = '2026-10-20T06:07:00Z'","STARTED = '2026-10-20T07:04:00Z'")
rep("OBS_AT = '2026-10-20T06:07:00Z'","OBS_AT = '2026-10-20T07:04:00Z'")
rep("READS_BEFORE = 831","READS_BEFORE = 813")
rep("datetime(2026,10,20,6,12,tzinfo=timezone.utc)","datetime(2026,10,20,7,9,tzinfo=timezone.utc)")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_angelreese': 'trend_angelreese.txt', 'trend_danquinn': 'trend_danquinn.txt', 'trend_fredwarner': 'trend_fredwarner.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_rays': 'trend_rays.txt', 'trend_niners': 'trend_niners.txt', 'trend_mikeevans': 'trend_mikeevans.txt', 'trend_worldseries': 'trend_worldseries.txt',""")
rep("""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_angelreese','trend.Angel Reese'),('trend_danquinn','trend.Dan Quinn'),('trend_fredwarner','trend.Fred Warner'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_rays','trend.Rays'),('trend_niners','trend.Niners'),('trend_mikeevans','trend.Mike Evans'),('trend_worldseries','trend.#WorldSeries'),""")
rep("    if _c.endswith('0607Z.json') and '/20/' in _c: continue","    if _c.endswith('0704Z.json') and '/20/' in _c: continue")
rep("(06Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap)","(07Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap)")
rep("""trend names "Angel Reese", "Dan Quinn", "Fred Warner" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the three of the current top-ten US names with no posts attached in 0501Z); quote/repost words that/just + what; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (100 first-hop, then the other 14 first-hop and 17 second-hop);""",
"""trend names Rays, Niners, "Mike Evans", #WorldSeries (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the four of the current top-ten US names with no posts attached in 0607Z); quote/repost words the/this + is; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (96 first-hop, then 16 second-hop);""")
rep("""'2 quote pages + 1 repost page (overnight budget), common words "that", "just" and "what": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each'""",
"""'2 quote pages + 1 repost page (overnight budget), common words "the", "this" and "is": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet), newest first, 25 each'""")
rep("'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut for the overnight budget (06:00-11:00 UTC, up to 20 reads)'",
    "'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut again for the overnight budget (06:00-11:00 UTC, up to 20 reads)'")
rep("'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z)'","'not due this run (four-hour desk, last ok 2026-10-20T0308Z, due 07:08Z; this run started 07:04Z)'")
rep("f'Overnight run (2:07 AM ET Oct 20 / 06:07 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0501Z run ended at 831), parallel batches of up to 10, no 429 refusals. '",
    "f'Overnight run (3:04 AM ET Oct 20 / 07:04 UTC; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the 0607Z run ended at 813), parallel batches of up to 11, no 429 refusals. '")
rep("06Z is not a fourth hour: the watch.json","07Z is not a fourth hour: the watch.json")
rep("""f'trend names "Angel Reese", "Dan Quinn", "Fred Warner" (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; the three of the current top-ten US names with no posts attached in 0501Z; Dan Quinn and Fred Warner are one event with 49ers, Jayden Daniels, Niners, Commanders and Mike Evans, Commanders at 49ers on Monday Night Football; Angel Reese is the WNBA Finals; Rays and #WorldSeries are one event); '""",
"""f'trend names Rays, Niners, "Mike Evans", #WorldSeries (4 reads; each "<name> lang:en is:retweet", newest first, 25 each; the four of the current top-ten US names with no posts attached in 0607Z; Niners and Mike Evans are one event with 49ers, Jayden Daniels, Dan Quinn, Fred Warner and Commanders, Commanders at 49ers on Monday Night Football; Rays and #WorldSeries are one event, Rays v Brewers World Series); '""")
rep("f'quote/repost words that/just + what (3 reads, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '",
    "f'quote/repost words the/this + is (3 reads, overnight budget); sensors not read for the overnight budget (news/money/science last read 0501Z, culture/sports/online 0400Z); '")
rep("f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z) were due 06:00Z but cut for the overnight budget, the four-hour desks were read in 0308Z and are due 07:08Z; '",
    "f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 0400Z) were due 06:00Z but cut again for the overnight budget, the four-hour desks were read in 0308Z and are due 07:08Z (this run started 07:04Z), next run; '")
rep("unread first-hop (a 100-id read, then the other 14 with the second hop; 2111338411768389946 Not Found)","unread first-hop (one 96-id read; 2108062331095908717 Not Found again)")
rep("out_path = f'{REPO}/capture/2026/10/20/0607Z.json'","out_path = f'{REPO}/capture/2026/10/20/0704Z.json'")
open('build_capture.py','w').write(s); print('ok')
