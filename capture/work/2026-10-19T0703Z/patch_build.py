s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count,('count',a[:90],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0603Z.json from saved X outputs."""','"""Build capture/2026/10/19/0703Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0603Z'","capture/work/2026-10-19T0703Z'")
R("RUN_ID = '2026-10-19T0603Z'","RUN_ID = '2026-10-19T0703Z'")
R("STARTED = '2026-10-19T06:03:00Z'","STARTED = '2026-10-19T07:03:00Z'")
R("OBS_AT = '2026-10-19T06:04:00Z'","OBS_AT = '2026-10-19T07:04:00Z'")
R("READS_BEFORE = 810","READS_BEFORE = 793")
R("datetime(2026,10,19,6,7,tzinfo=timezone.utc)","datetime(2026,10,19,7,7,tzinfo=timezone.utc)")
R("""    'quote_it': 'quote_it.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_gopackgo': 'trend_gopackgo.txt', 'trend_jerry': 'trend_jerry.txt', 'trend_greenbay': 'trend_greenbay.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_you': 'repost_you.txt',
    'trend_schotty': 'trend_schotty.txt', 'trend_dak': 'trend_dak.txt', 'trend_rams': 'trend_rams.txt',""")
R("""    ('quote_it','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_gopackgo','trend.#GoPackGo'),('trend_jerry','trend.Jerry'),('trend_greenbay','trend.Green Bay'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('repost_you','repost'),
    ('trend_schotty','trend.Schotty'),('trend_dak','trend.Dak Prescott'),('trend_rams','trend.Rams'),""")
R("if _c.endswith('0603Z.json') and '/19/' in _c: continue","if _c.endswith('0703Z.json') and '/19/' in _c: continue")
R("""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names #GoPackGo, Jerry, "Green Bay" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0509Z; all three are one event, the Cowboys v Packers Sunday Night Football game, Jerry being Cowboys owner Jerry Jones; Pickens cut for the overnight budget); quote/repost words it/just + what; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',""",
"""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Schotty, "Dak Prescott", Rams (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 0603Z; Schotty and "Dak Prescott" are the Cowboys v Packers game, Schotty being Cowboys coach Brian Schottenheimer, Rams the NFL team; "Jordan Love", #LaGranjaGala and Pickens cut for the overnight budget); quote/repost words the/this + you; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',""")
R("""'2 quote pages + 1 repost page, common words "it", "just" and "what": (it lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',""",
"""'2 quote pages + 1 repost page, common words "the", "this" and "you": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (you lang:en is:retweet), newest first, 25 each',""")
R("""        _last = '2026-10-19T0404Z' if g in ('news','money','science') else '2026-10-19T0509Z'""","""        _last = '2026-10-19T0404Z' if g in ('news','money','science') else '2026-10-19T0509Z'  # unchanged: not read in 0603Z or 0703Z""")
R("""            reason = 'due (two-hour desk, last ok 2026-10-19T0404Z, due 06:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0509Z, due at 07:09Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z)'""",
"""            reason = 'due (two-hour desk, last ok 2026-10-19T0404Z, due 06:04Z) but cut for the overnight read budget (06:00-11:00 UTC band, up to 20 reads: the hourly desks only)'
        elif d in ('ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, read in 0509Z, due at 07:09Z; this run started 07:03Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 0304Z, due at 07:04Z; this run started 07:03Z)'""")
i=s.index("            f'Overnight run at 2:03 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Overnight run at 3:03 AM ET (07:03 UTC Oct 19; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0603Z run ended at 793, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 07Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names Schotty, "Dak Prescott", Rams (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, "Jordan Love", #LaGranjaGala and Pickens had no posts attached in 0603Z; Schotty and "Dak Prescott" are the Cowboys v Packers game, Rams the NFL team; the other three cut for the overnight budget); quote/repost words the/this + you (3 reads); '
            f'hourly desks politics, entertainment, sports, internet (4 reads; two-hour music, gaming, offbeat, world, justice, markets due 06:04Z but cut for the overnight budget; ai, tech, medicine, science, ideas, life, defense, disaster, business not due); '
            f'two screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts. '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the overnight budget: sensors, story clusters, volume, context.top, media descriptions; x_stories omitted. '
"""+s[j:]
R("out_path = f'{REPO}/capture/2026/10/19/0603Z.json'","out_path = f'{REPO}/capture/2026/10/19/0703Z.json'")
open('build_capture.py','w').write(s)
print('patched')
