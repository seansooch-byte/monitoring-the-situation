s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70]); s=s.replace(a,b)
rep("Build capture/2026/10/17/0806Z.json","Build capture/2026/10/17/0907Z.json")
rep("work/2026-10-17T0806Z'","work/2026-10-17T0907Z'")
rep("RUN_ID = '2026-10-17T0806Z'","RUN_ID = '2026-10-17T0907Z'")
rep("STARTED = '2026-10-17T08:06:00Z'","STARTED = '2026-10-17T09:07:00Z'")
rep("OBS_AT = '2026-10-17T08:07:00Z'","OBS_AT = '2026-10-17T09:09:00Z'")
rep("READS_BEFORE = 779","READS_BEFORE = 761")
rep("READS_AFTER = 761","READS_AFTER = 743")
rep("datetime(2026,10,17,8,9,tzinfo","datetime(2026,10,17,9,12,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_kimmel': 'trend_kimmel.txt', 'trend_heartbeat': 'trend_heartbeat.txt', 'trend_pflchicago': 'trend_pflchicago.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_lingorm': 'trend_lingorm.txt', 'trend_monica': 'trend_monica.txt', 'trend_violet': 'trend_violet.txt',""")
rep("""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_kimmel','trend.Kimmel'),('trend_heartbeat','trend.Heartbeat'),('trend_pflchicago','trend.#PFLChicago'),""",
"""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_lingorm','trend.#LingOrmBetweenUsConcertD1'),('trend_monica','trend.Mónica'),('trend_violet','trend.Violet'),""")
rep("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2'):",2)
rep("        if str(_x)=='trend.Kimmel': return 'entertainment'\n","        if str(_x)=='trend.Kimmel': return 'entertainment'\n        if str(_x) in ('trend.#LingOrmBetweenUsConcertD1','trend.THE WORLD BETWEEN LINGORM D1'): return 'entertainment'\n")
rep("for a,b in [('Kimmel','Johnny Carson'),","for a,b in [('#LingOrmBetweenUsConcertD1','THE WORLD BETWEEN LINGORM D1'),('THE WORLD BETWEEN LINGORM D1','#LingOrmBetweenUsConcertD1'),('Kimmel','Johnny Carson'),")
rep("and, as 08Z is a fourth hour, the rest of the last 24 hours slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(09Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
rep("08Z is a fourth hour, so the slow tier was included; under","09Z is not a fourth hour, so no slow tier; under")
OLD='''trend names Kimmel, Heartbeat, #PFLChicago (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0703Z were "Mónica", "Johnny Carson", Kimmel, Heartbeat, #LaGranjaTraicion, #PFLChicago and Purdue; Kimmel and "Johnny Carson" are one event, a post asking whether Johnny Carson was better than Jimmy Kimmel; Heartbeat is BTS performing the song Heartbeat live; #PFLChicago is the PFL Chicago MMA card; "Mónica", #LaGranjaTraicion and Purdue not read for the overnight budget)'''
TN='''trend names #LingOrmBetweenUsConcertD1, Mónica, Violet (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0806Z were #LingOrmBetweenUsConcertD1, "THE WORLD BETWEEN LINGORM D1", #PerthSantaFMinMacau, "PERTHSANTA LOST IN LOVE", Mónica, "You Can See Everything" and Violet; #LingOrmBetweenUsConcertD1 and "THE WORLD BETWEEN LINGORM D1" are one event, day one of the LingOrm concert; Mónica is no single event, mostly unrelated posts mentioning the name; Violet is the Deadlock game hero; the PerthSanta pair and "You Can See Everything" were read in 0703Z and not again for the overnight budget)'''
rep(OLD,TN)
rep(OLD.replace('(each','(3 reads; each'),TN.replace('(each','(3 reads; each'))
rep("quote/repost words this/is + you;","quote/repost words and/my + it;")
rep("quote/repost words this/is + you (2+1)",'''quote/repost words and/my + it (2+1; the unquoted and query was refused by X as ambiguous and cost one read, then re-run with "and" quoted)''')
rep('''common words "this", "is" and "you": "this lang:en is:quote -is:retweet", "is lang:en is:quote -is:retweet", "you lang:en is:retweet"''','''common words "and", "my" and "it": "and" quoted, ""and" lang:en is:quote -is:retweet", "my lang:en is:quote -is:retweet", "it lang:en is:retweet"''')
rep("Overnight run at 4:06 AM ET (08:06 UTC Oct 17;","Overnight run at 5:07 AM ET (09:07 UTC Oct 17;")
rep("all cut for the overnight budget; defense, disaster, business not due","and four-hour defense, disaster, business due since 09:06Z, all cut for the overnight budget")
rep("            reason = 'not due this run (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z)'",
    "            reason = 'due (last ok 2026-10-17T0506Z; four-hour desk, due 09:06Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'")
rep("out_path = f'{REPO}/capture/2026/10/17/0806Z.json'","out_path = f'{REPO}/capture/2026/10/17/0907Z.json'")
rep("skipped_nsfw = []\n","skip_nsfw |= {'2111207821769327038'}  # 0907Z: pornographic spam text in the Mónica stream\nskipped_nsfw = []\n")
open('build_capture.py','w').write(s); print('ok')
