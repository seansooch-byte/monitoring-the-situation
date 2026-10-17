s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70]); s=s.replace(a,b)
rep("Build capture/2026/10/17/0703Z.json","Build capture/2026/10/17/0806Z.json")
rep("work/2026-10-17T0703Z'","work/2026-10-17T0806Z'")
rep("RUN_ID = '2026-10-17T0703Z'","RUN_ID = '2026-10-17T0806Z'")
rep("STARTED = '2026-10-17T07:03:00Z'","STARTED = '2026-10-17T08:06:00Z'")
rep("OBS_AT = '2026-10-17T07:04:00Z'","OBS_AT = '2026-10-17T08:07:00Z'")
rep("READS_BEFORE = 796","READS_BEFORE = 779")
rep("READS_AFTER = 779","READS_AFTER = 761")
rep("datetime(2026,10,17,7,6,tzinfo","datetime(2026,10,17,8,9,tzinfo")
rep("""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_perthsanta': 'trend_perthsanta.txt', 'trend_smackdown': 'trend_smackdown.txt', 'trend_youcanseeeverything': 'trend_youcanseeeverything.txt',""",
"""    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',
    'repost_you': 'repost_you.txt',
    'trend_kimmel': 'trend_kimmel.txt', 'trend_heartbeat': 'trend_heartbeat.txt', 'trend_pflchicago': 'trend_pflchicago.txt',""")
rep("""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_perthsanta','trend.PERTHSANTA LOST IN LOVE'),('trend_smackdown','trend.#SmackDown'),('trend_youcanseeeverything','trend.You Can See Everything'),""",
"""    ('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),
    ('trend_kimmel','trend.Kimmel'),('trend_heartbeat','trend.Heartbeat'),('trend_pflchicago','trend.#PFLChicago'),""")
rep("for batch in ('watch0','watch1','watch2'):","for batch in ('watch0','watch1','watch2','watch3'):",2)
rep("        if str(_x) in ('trend.PERTHSANTA LOST IN LOVE','trend.#PerthSantaFMinMacau'): return 'entertainment'\n","        if str(_x) in ('trend.PERTHSANTA LOST IN LOVE','trend.#PerthSantaFMinMacau'): return 'entertainment'\n        if str(_x)=='trend.Kimmel': return 'entertainment'\n")
rep("for a,b in [('PERTHSANTA LOST IN LOVE',","for a,b in [('Kimmel','Johnny Carson'),('Johnny Carson','Kimmel'),('PERTHSANTA LOST IN LOVE',")
rep("(07Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;",
    "and, as 08Z is a fourth hour, the rest of the last 24 hours slowest growing last; {len(watch_ids)} unique ids, under the 400 cap, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;")
rep("07Z is not a fourth hour, so no slow tier; under","08Z is a fourth hour, so the slow tier was included; under")
TN='''trend names Kimmel, Heartbeat, #PFLChicago (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0703Z were "Mónica", "Johnny Carson", Kimmel, Heartbeat, #LaGranjaTraicion, #PFLChicago and Purdue; Kimmel and "Johnny Carson" are one event, a post asking whether Johnny Carson was better than Jimmy Kimmel; Heartbeat is BTS performing the song Heartbeat live; #PFLChicago is the PFL Chicago MMA card; "Mónica", #LaGranjaTraicion and Purdue not read for the overnight budget)'''
OLD='''trend names "PERTHSANTA LOST IN LOVE", #SmackDown, "You Can See Everything" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0600Z were "PERTHSANTA LOST IN LOVE", #PerthSantaFMinMacau, #PFLChicago, #SmackDown, "You Can See Everything", Heartbeat, Kessler and "ash trevino"; "PERTHSANTA LOST IN LOVE" and #PerthSantaFMinMacau are one event, the PerthSanta fan meeting in Macau; #PFLChicago, Heartbeat, Kessler and "ash trevino" not read for the overnight budget)'''
rep(OLD,TN)
rep(OLD.replace('(each','(3 reads; each'),TN.replace('(each','(3 reads; each'))
rep("quote/repost words just/what + the;","quote/repost words this/is + you;")
rep("quote/repost words just/what + the (2+1)","quote/repost words this/is + you (2+1)")
rep('''common words "just", "what" and "the": "just lang:en is:quote -is:retweet", "what lang:en is:quote -is:retweet", "the lang:en is:retweet"''','''common words "this", "is" and "you": "this lang:en is:quote -is:retweet", "is lang:en is:quote -is:retweet", "you lang:en is:retweet"''')
rep("Overnight run at 3:03 AM ET (07:03 UTC Oct 17;","Overnight run at 4:06 AM ET (08:06 UTC Oct 17;")
rep("two-hour world, justice, markets, ai, tech, medicine due since 06:03Z but cut again for the overnight budget; music, gaming, offbeat, defense, disaster, business, science, ideas, life not due",
    "two-hour world, justice, markets, ai, tech, medicine due since 06:03Z, two-hour music, gaming, offbeat due since 07:06Z and four-hour science, ideas, life due since 07:08Z, all cut for the overnight budget; defense, disaster, business not due")
rep("            reason = 'not due this run (last ok 2026-10-17T0506Z; two-hour desk, due 07:06Z)'",
    "            reason = 'due (last ok 2026-10-17T0506Z; two-hour desk, due 07:06Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'")
rep("            reason = 'not due this run (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z)'",
    "            reason = 'due (last ok 2026-10-17T0308Z; four-hour desk, due 07:08Z) but cut for the overnight read budget (06:00-11:00 UTC, up to 20 reads)'")
rep("out_path = f'{REPO}/capture/2026/10/17/0703Z.json'","out_path = f'{REPO}/capture/2026/10/17/0806Z.json'")
rep("skipped_nsfw = []\n","skip_nsfw |= {'2111365980270256455'}  # 0806Z: follower-boost spam in the #PFLChicago stream\nskipped_nsfw = []\n")
open('build_capture.py','w').write(s); print('ok')
