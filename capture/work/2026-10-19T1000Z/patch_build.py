s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count,('count',a[:90],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0905Z.json from saved X outputs."""','"""Build capture/2026/10/19/1000Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0905Z'","capture/work/2026-10-19T1000Z'")
R("RUN_ID = '2026-10-19T0905Z'","RUN_ID = '2026-10-19T1000Z'")
R("STARTED = '2026-10-19T09:05:00Z'","STARTED = '2026-10-19T10:00:00Z'")
R("OBS_AT = '2026-10-19T09:06:00Z'","OBS_AT = '2026-10-19T10:01:00Z'")
R("READS_BEFORE = 758","READS_BEFORE = 741")
R("datetime(2026,10,19,9,7,tzinfo=timezone.utc)","datetime(2026,10,19,10,8,tzinfo=timezone.utc)")
R("""    'quote_what': 'quote_what.txt', 'quote_it': 'quote_it.txt',
    'repost_just': 'repost_just.txt',
    'trend_packers': 'trend_packers.txt', 'trend_goodmonday': 'trend_goodmonday.txt', 'trend_happynewweek': 'trend_happynewweek.txt',""",
"""    'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',
    'repost_that': 'repost_that.txt',
    'trend_mondaymotivation': 'trend_mondaymotivation.txt', 'trend_goku': 'trend_goku.txt', 'trend_jeonghan': 'trend_jeonghan.txt',""")
R("""    ('quote_what','quote'),('quote_it','quote'),('repost_just','repost'),
    ('trend_packers','trend.Packers'),('trend_goodmonday','trend.Good Monday'),('trend_happynewweek','trend.Happy New Week'),""",
"""    ('quote_this','quote'),('quote_you','quote'),('repost_that','repost'),
    ('trend_mondaymotivation','trend.#MondayMotivation'),('trend_goku','trend.Goku'),('trend_jeonghan','trend.jeonghan'),""")
R("""        if str(_x) in ('trend.Jerry',): return 'sports'  # 0603Z: Jerry Jones, Cowboys v Packers""",
"""        if str(_x) in ('trend.jeonghan',): return 'music'  # 1000Z: SEVENTEEN member Jeonghan
        if str(_x) in ('trend.Jerry',): return 'sports'  # 0603Z: Jerry Jones, Cowboys v Packers""")
R("if _c.endswith('0905Z.json') and '/19/' in _c: continue","if _c.endswith('1000Z.json') and '/19/' in _c: continue")
VG_OLD = s[s.index("""    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Packers"""):]
VG_OLD = VG_OLD[:VG_OLD.index("',\n")+3]
R(VG_OLD, """    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #MondayMotivation, Goku, jeonghan (each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, Cowboys, "PC gaming", Schotty and "Dak Prescott" also had no posts attached in 0905Z; Cowboys, Schotty and "Dak Prescott" are the Cowboys v Packers game, which already has posts attached under Packers, and "PC gaming" was cut for the overnight budget); quote/repost words this/you + that; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',\n""")
R("""'2 quote pages + 1 repost page, common words "what", "it" and "just": (what lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each',""",
"""'2 quote pages + 1 repost page, common words "this", "you" and "that": (this lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each (a first quote read with the bare word and was refused as Invalid Request, "Ambiguous use of and as a keyword", and still counted)',""")
R("""  # unchanged: not read in 0603Z, 0703Z, 0802Z or 0905Z""","""  # unchanged: not read in 0603Z, 0703Z, 0802Z, 0905Z or 1000Z""")
R("""(09Z is not a fourth hour, so the rest of the last 24 hours was not added)""","""(10Z is not a fourth hour, so the rest of the last 24 hours was not added)""")
R("""            reason = 'not due this run (four-hour desk, read in 0509Z, due at 09:09Z)'""","""            reason = 'due (four-hour desk, last ok 2026-10-19T0509Z, due 09:09Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'""")
i=s.index("            f'Overnight run at 5:05 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Overnight run at 6:00 AM ET (10:00 UTC Oct 19; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0905Z run ended at 741, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 10Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names #MondayMotivation, Goku, jeonghan (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, Cowboys, "PC gaming", Schotty and "Dak Prescott" also had no posts attached in 0905Z; Cowboys, Schotty and "Dak Prescott" are the Cowboys v Packers game, which already has posts under Packers, and "PC gaming" was cut for the overnight budget); '
            f'quote/repost words this/you + that (3 reads, plus 1 refused read: the bare word and was rejected as Invalid Request, "Ambiguous use of and as a keyword", which still counted, as noted in CAPABILITIES.md on 2026-10-15); '
            f'hourly desks politics, entertainment, sports, internet (4 reads; two-hour music, gaming, offbeat, world, justice, markets due 06:04Z, two-hour ai, tech, medicine due 07:09Z and four-hour science, ideas, life due 07:04Z and defense, disaster, business due 09:09Z, all cut for the overnight budget); '
            f'two screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split(","))} unread first-hop, then {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (all returned). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the overnight budget: sensors, story clusters, volume, context.top, media descriptions; x_stories omitted. '
"""+s[j:]
R("out_path = f'{REPO}/capture/2026/10/19/0905Z.json'","out_path = f'{REPO}/capture/2026/10/19/1000Z.json'")
open('build_capture.py','w').write(s)
print('patched')
