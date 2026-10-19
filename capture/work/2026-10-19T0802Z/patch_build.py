s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count,('count',a[:90],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0703Z.json from saved X outputs."""','"""Build capture/2026/10/19/0802Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0703Z'","capture/work/2026-10-19T0802Z'")
R("RUN_ID = '2026-10-19T0703Z'","RUN_ID = '2026-10-19T0802Z'")
R("STARTED = '2026-10-19T07:03:00Z'","STARTED = '2026-10-19T08:02:00Z'")
R("OBS_AT = '2026-10-19T07:04:00Z'","OBS_AT = '2026-10-19T08:03:00Z'")
R("READS_BEFORE = 793","READS_BEFORE = 776")
R("datetime(2026,10,19,7,7,tzinfo=timezone.utc)","datetime(2026,10,19,8,6,tzinfo=timezone.utc)")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_schotty': 'trend_schotty.txt', 'trend_dak': 'trend_dak.txt', 'trend_rams': 'trend_rams.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt',
    'repost_that': 'repost_that.txt',
    'trend_goku': 'trend_goku.txt', 'trend_lagranja': 'trend_lagranja.txt', 'trend_jlove': 'trend_jlove.txt',""")
R("""    ('quote_the','quote'),('quote_this','quote'),('repost_you','repost'),
    ('trend_schotty','trend.Schotty'),('trend_dak','trend.Dak Prescott'),('trend_rams','trend.Rams'),""",
"""    ('quote_is','quote'),('quote_my','quote'),('repost_that','repost'),
    ('trend_goku','trend.Goku'),('trend_lagranja','trend.#LaGranjaGala'),('trend_jlove','trend.Jordan Love'),""")
R("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
R("if _c.endswith('0703Z.json') and '/19/' in _c: continue","if _c.endswith('0802Z.json') and '/19/' in _c: continue")
R("""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Schotty, "Dak Prescott", Rams (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0603Z; Schotty and "Dak Prescott" are the Cowboys v Packers game, Schotty being Cowboys coach Brian Schottenheimer, Rams the NFL team; "Jordan Love", #LaGranjaGala and Pickens cut for the overnight budget); quote/repost words the/this + you; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',""",
"""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Goku, #LaGranjaGala, "Jordan Love" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these, #GoPackGo and "Green Bay" had no posts attached in 0703Z; Goku is new to the top ten, #LaGranjaGala is the La Granja VIP reality-show gala, "Jordan Love" the Cowboys v Packers game; #GoPackGo and "Green Bay", also that game, cut for the overnight budget); quote/repost words is/my + that; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop with the first-hop remainder); screened by id with global floor/pace',""")
R("""'2 quote pages + 1 repost page, common words "the", "this" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each',""",
"""'2 quote pages + 1 repost page, common words "is", "my" and "that": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each',""")
R("""  # unchanged: not read in 0603Z or 0703Z""","""  # unchanged: not read in 0603Z, 0703Z or 0802Z""")
R("""(06Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;""",
"""and, as 08Z is a fourth hour, the rest of the last 24 hours; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;""")
R("""            reason = 'due (two-hour desk, last ok 2026-10-19T0404Z, due 06:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0509Z, due at 07:09Z; this run started 07:03Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z; this run started 07:03Z)'""",
"""            reason = 'due (two-hour desk, last ok 2026-10-19T0404Z, due 06:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('ai','tech','medicine'):
            reason = 'due (two-hour desk, last ok 2026-10-19T0509Z, due 07:09Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('science','ideas','life'):
            reason = 'due (four-hour desk, last ok 2026-10-19T0304Z, due 07:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'""")
i=s.index("            f'Overnight run at 3:03 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Overnight run at 4:02 AM ET (08:02 UTC Oct 19; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0703Z run ended at 776, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 08Z is a fourth hour, so the rest of the last 24 hours was added; under the 400 cap, none left out; 4 reads); trends US+WW (2 reads); '
            f'trend names Goku, #LaGranjaGala, "Jordan Love" (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, #GoPackGo and "Green Bay" had no posts attached in 0703Z; Goku is new to the top ten, #LaGranjaGala is the La Granja VIP reality-show gala, "Jordan Love" the Cowboys v Packers game; #GoPackGo and "Green Bay", also that game, cut for the overnight budget); quote/repost words is/my + that (3 reads); '
            f'hourly desks politics, entertainment, sports, internet (4 reads; two-hour music, gaming, offbeat, world, justice, markets due 06:04Z, two-hour ai, tech, medicine due 07:09Z and four-hour science, ideas, life due 07:04Z, all cut for the overnight budget; defense, disaster, business not due); '
            f'two screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split(","))} unread first-hop, then the other 10 first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (2112091059450753316 and 2111478987923067039 came back Not Found in the first and were not read again). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the overnight budget: sensors, story clusters, volume, context.top, media descriptions; x_stories omitted. '
"""+s[j:]
R("out_path = f'{REPO}/capture/2026/10/19/0703Z.json'","out_path = f'{REPO}/capture/2026/10/19/0802Z.json'")
open('build_capture.py','w').write(s)
print('patched')
