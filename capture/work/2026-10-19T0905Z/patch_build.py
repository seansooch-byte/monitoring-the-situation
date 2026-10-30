s=open('build_capture.py').read()
def R(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count,('count',a[:90],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/19/0802Z.json from saved X outputs."""','"""Build capture/2026/10/19/0905Z.json from saved X outputs."""')
R("capture/work/2026-10-19T0802Z'","capture/work/2026-10-19T0905Z'")
R("RUN_ID = '2026-10-19T0802Z'","RUN_ID = '2026-10-19T0905Z'")
R("STARTED = '2026-10-19T08:02:00Z'","STARTED = '2026-10-19T09:05:00Z'")
R("OBS_AT = '2026-10-19T08:03:00Z'","OBS_AT = '2026-10-19T09:06:00Z'")
R("READS_BEFORE = 776","READS_BEFORE = 758")
R("datetime(2026,10,19,8,6,tzinfo=timezone.utc)","datetime(2026,10,19,9,9,tzinfo=timezone.utc)")
R("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_is': 'quote_is.txt', 'quote_my': 'quote_my.txt',
    'repost_that': 'repost_that.txt',
    'trend_goku': 'trend_goku.txt', 'trend_lagranja': 'trend_lagranja.txt', 'trend_jlove': 'trend_jlove.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_what': 'quote_what.txt', 'quote_it': 'quote_it.txt',
    'repost_just': 'repost_just.txt',
    'trend_packers': 'trend_packers.txt', 'trend_goodmonday': 'trend_goodmonday.txt', 'trend_happynewweek': 'trend_happynewweek.txt',""")
R("""    ('quote_is','quote'),('quote_my','quote'),('repost_that','repost'),
    ('trend_goku','trend.Goku'),('trend_lagranja','trend.#LaGranjaGala'),('trend_jlove','trend.Jordan Love'),""",
"""    ('quote_what','quote'),('quote_it','quote'),('repost_just','repost'),
    ('trend_packers','trend.Packers'),('trend_goodmonday','trend.Good Monday'),('trend_happynewweek','trend.Happy New Week'),""")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",2)
R("if _c.endswith('0802Z.json') and '/19/' in _c: continue","if _c.endswith('0905Z.json') and '/19/' in _c: continue")
R("""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Goku, #LaGranjaGala, "Jordan Love" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these, #GoPackGo and "Green Bay" had no posts attached in 0703Z; Goku is new to the top ten, #LaGranjaGala is the La Granja VIP reality-show gala, "Jordan Love" the Cowboys v Packers game; #GoPackGo and "Green Bay", also that game, cut for the overnight budget); quote/repost words is/my + that; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop with the first-hop remainder); screened by id with global floor/pace',""",
"""'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names Packers, "Good Monday", "Happy New Week" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these, Cowboys, Schotty, "Dak Prescott", #GoPackGo and "Jerry Jones" had no posts attached in 0802Z; Packers, Cowboys, Schotty, "Dak Prescott", #GoPackGo and "Jerry Jones" are one event, the Cowboys v Packers game, so Packers stands for it; "Good Monday" and "Happy New Week" are start-of-week greetings; the other game names cut for the overnight budget); quote/repost words what/it + just; hourly desks politics/entertainment/sports/internet; two screening reads by id of unread referenced posts (one first-hop, one second-hop); screened by id with global floor/pace',""")
R("""'2 quote pages + 1 repost page, common words "is", "my" and "that": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each',""",
"""'2 quote pages + 1 repost page, common words "what", "it" and "just": (what lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (just lang:en is:retweet), newest first, 25 each',""")
R("""  # unchanged: not read in 0603Z, 0703Z or 0802Z""","""  # unchanged: not read in 0603Z, 0703Z, 0802Z or 0905Z""")
R("""and, as 08Z is a fourth hour, the rest of the last 24 hours; {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;""",
"""(09Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;""")
i=s.index("            f'Overnight run at 4:02 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
s=s[:i]+"""            f'Overnight run at 5:05 AM ET (09:05 UTC Oct 19; 06:00-11:00 UTC band, up to 20 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 0802Z run ended at 758, so no reads were used elsewhere between the runs; calls made one or two at a time, no 429 refusals). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 09Z is not a fourth hour, so the rest of the last 24 hours was not added; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names Packers, "Good Monday", "Happy New Week" (3 reads; each "<name> lang:en is:retweet", newest first, 25 each; of the current top-ten US names these, Cowboys, Schotty, "Dak Prescott", #GoPackGo and "Jerry Jones" had no posts attached in 0802Z; all but the two greetings are the Cowboys v Packers game, so Packers stands for it and the rest were cut for the overnight budget; "Good Monday" and "Happy New Week" are start-of-week greetings); quote/repost words what/it + just (3 reads); '
            f'hourly desks politics, entertainment, sports, internet (4 reads; two-hour music, gaming, offbeat, world, justice, markets due 06:04Z, two-hour ai, tech, medicine due 07:09Z and four-hour science, ideas, life due 07:04Z, all cut for the overnight budget; defense, disaster, business not due until 09:09Z); '
            f'two screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split(","))} unread first-hop, then {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts (2084792384370680094 and 2094256408246292612, referenced by posts in the first, came back Not Found and were not read again; 2112096226065715484, referenced in the second, came back Not Found). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-02 in 2203Z) and was not read again. '
            f'Not read for the overnight budget: sensors, story clusters, volume, context.top, media descriptions; x_stories omitted. '
"""+s[j:]
R("out_path = f'{REPO}/capture/2026/10/19/0802Z.json'","out_path = f'{REPO}/capture/2026/10/19/0905Z.json'")
open('build_capture.py','w').write(s)
print('patched')
