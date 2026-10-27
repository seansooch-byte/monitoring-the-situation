import re
s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
rep('1503Z.json from saved','1604Z.json from saved')
rep("work/2026-10-27T1503Z'","work/2026-10-27T1604Z'")
rep("RUN_ID = '2026-10-27T1503Z'","RUN_ID = '2026-10-27T1604Z'")
rep("STARTED = '2026-10-27T15:03:00Z'","STARTED = '2026-10-27T16:04:00Z'")
rep("OBS_AT = '2026-10-27T15:04:00Z'","OBS_AT = '2026-10-27T16:06:00Z'")
rep("READS_BEFORE = 688","READS_BEFORE = 668")
rep("datetime(2026,10,27,15,4,tzinfo=timezone.utc).timestamp()  # 1503Z (","datetime(2026,10,27,16,6,tzinfo=timezone.utc).timestamp()  # 1604Z (1503Z used 15:04, ")
rep("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_ericswalwell': 'trend_ericswalwell.txt', 'trend_beverlyhills': 'trend_beverlyhills.txt', 'trend_maozedong': 'trend_maozedong.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',""","""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_stephencloobeck': 'trend_stephencloobeck.txt', 'trend_kateallie': 'trend_kateallie.txt', 'trend_mcmillan': 'trend_mcmillan.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt',""")
rep("""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_ericswalwell','trend.Eric Swalwell'),('trend_beverlyhills','trend.Beverly Hills'),('trend_maozedong','trend.Mao Zedong'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""","""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_stephencloobeck','trend.Stephen Cloobeck'),('trend_kateallie','trend.Kate & Allie'),('trend_mcmillan','trend.McMillan'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
rep("""        if str(_x) in ('trend.Eric Swalwell','trend.Beverly Hills'): return 'justice'""","""        if str(_x) in ('trend.Stephen Cloobeck',): return 'justice'  # 1604Z: FBI search of the Beverly Hills mansion of donor Stephen Cloobeck in the Eric Swalwell investigation (same event as Eric Swalwell and Beverly Hills)
        if str(_x) in ('trend.Kate & Allie','trend.McMillan'): return 'entertainment'  # 1604Z: death of actress Susan Saint James (one event)
        if str(_x) in ('trend.Eric Swalwell','trend.Beverly Hills'): return 'justice'""")
rep("if _c.endswith('1503Z.json') and '/27/' in _c: continue","if _c.endswith('1604Z.json') and '/27/' in _c: continue")
rep("for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}","for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
rep("this 15Z run is not a","this 16Z run is not a")
rep("the list was 525 long, so the 400 cap left out the 91 last six-hour posts, the 22 slowest-growing still-gaining posts and 12 story-cited posts not on the pulse (2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 2113455120692195588 was read in screening as a referenced post), because the 301 watch.json",
    "the list was 516 long, so the 400 cap left out the 79 last six-hour posts, the 21 slowest-growing still-gaining posts and 16 story-cited posts not on the pulse (2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 2113455120692195588 was read in screening as a referenced post), because the 305 watch.json")
# viral sources
i=s.index("'sources: references followed one hop"); j=s.index("\n",i)
s=s[:i]+"""'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names "Stephen Cloobeck", "Kate & Allie" and "McMillan" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached earlier today that are not greetings: "Stephen Cloobeck" (fourth, new) is the FBI search of his Beverly Hills mansion, the same event as "Eric Swalwell" (first) and "Beverly Hills" (second), which had posts attached in 1503Z; "Kate & Allie" (ninth, new) and "McMillan" (tenth, new) are one event, the death of actress Susan Saint James; the "Kate & Allie" read returned no posts; "Taco Tuesday" (eighth) is a greeting; "#BladeRunnerLovesPPGsCowDung" (fifth), "#中国北京彻查上海叠纸" (sixth) and "#BeijingMustInvestigatePPGNow" (seventh) had posts attached in 1259Z; "Noah Wyle" (third) had posts attached earlier today); quote/repost words you/and + my (quoted); hourly desks politics/entertainment/sports/internet; one screening read by id: 82 unread referenced, reply-parent and media-source posts, most pointed-at first, which also covered the second hop; the only post left unread is 2114971940788310059 (Authorization Error); story clusters not read for the budget; screened by id with global floor/pace',"""+s[j:]
rep('common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)',
    'common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet)')
rep("_last = '2026-10-27T1416Z'","_last = '2026-10-27T1503Z'")
rep("rotation: culture/sports/online read this run","rotation: news/money/science read this run")
rep("one hundred and seventy-fourth run","one hundred and seventy-fifth run")
rep("one hundred and seventy-seventh run","one hundred and seventy-eighth run")
# reason block
i=s.index("            f'Morning run (11:03 AM ET"); j=s.index("            f'{EXTRA_NOTE} '")
new = """            f'Morning run (12:04 PM ET Oct 27 / 16:04 UTC Oct 27, the 16Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1503Z ended at 668, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 16Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 516 ids, so the 400 cap left out the 79 last six-hour posts, the 21 slowest-growing still-gaining posts and 16 story-cited posts not on the pulse (2110717676851216815, 2110872117445013817, 2110897247663853658, 2110901393238474863, 2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'trend names "Stephen Cloobeck", "Kate & Allie" and "McMillan" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached earlier today that are not greetings: "Stephen Cloobeck" (fourth, new) is the FBI search of his Beverly Hills mansion, the same event as "Eric Swalwell" (first) and "Beverly Hills" (second), attached in 1503Z; "Kate & Allie" (ninth, new) and "McMillan" (tenth, new) are one event, the death of actress Susan Saint James, and the "Kate & Allie" read returned no posts; "Taco Tuesday" (eighth) is a greeting; "#BladeRunnerLovesPPGsCowDung" (fifth), "#中国北京彻查上海叠纸" (sixth) and "#BeijingMustInvestigatePPGNow" (seventh) had posts attached in 1259Z; "Noah Wyle" (third) had posts attached earlier today) (3 reads); '
            f'quote/repost words you/and + my (3 reads, each word quoted; 1503Z used the/this + is); sensors news/money/science (3 reads; culture/sports/online read 1503Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and seventy-seventh run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and seventy-fourth run, both for the budget; '
            f'one screening read by id: 82 unread referenced, reply-parent and media-source posts, most pointed-at first (80 returned; 2108062331095908717 Not Found again and 2114971940788310059 Authorization Error, both pointed at as referenced posts); the second hop of the screened posts was already read, so no second screening read was needed (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1503Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, in watch.json; no longer cited on the pulse) came back Not Found for the fifth run running; story clusters (search_news) not read for the budget. '
            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
"""
s=s[:i]+new+s[j:]
rep("capture/2026/10/27/1503Z.json'","capture/2026/10/27/1604Z.json'")
open('build_capture.py','w').write(s)
print('ok')
