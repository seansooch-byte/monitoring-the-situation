s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70]); s=s.replace(a,b)
rep("Build capture/2026/10/17/0600Z.json","Build capture/2026/10/17/0703Z.json")
rep("work/2026-10-17T0600Z'","work/2026-10-17T0703Z'")
rep("RUN_ID = '2026-10-17T0600Z'","RUN_ID = '2026-10-17T0703Z'")
rep("STARTED = '2026-10-17T06:00:00Z'","STARTED = '2026-10-17T07:03:00Z'")
rep("OBS_AT = '2026-10-17T06:01:00Z'","OBS_AT = '2026-10-17T07:04:00Z'")
rep("READS_BEFORE = 813","READS_BEFORE = 796")
rep("READS_AFTER = 796","READS_AFTER = 779")
rep("datetime(2026,10,17,6,2,tzinfo","datetime(2026,10,17,7,6,tzinfo")
rep("""    'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_johnnycarson': 'trend_johnnycarson.txt', 'trend_purdue': 'trend_purdue.txt', 'trend_memphis': 'trend_memphis.txt',""",
"""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_perthsanta': 'trend_perthsanta.txt', 'trend_smackdown': 'trend_smackdown.txt', 'trend_youcanseeeverything': 'trend_youcanseeeverything.txt',""")
rep("""    ('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_johnnycarson','trend.Johnny Carson'),('trend_purdue','trend.Purdue'),('trend_memphis','trend.Memphis'),""",
"""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_perthsanta','trend.PERTHSANTA LOST IN LOVE'),('trend_smackdown','trend.#SmackDown'),('trend_youcanseeeverything','trend.You Can See Everything'),""")
rep("        if str(_x)=='trend.YK Osiris': return 'internet'\n","        if str(_x)=='trend.YK Osiris': return 'internet'\n        if str(_x) in ('trend.PERTHSANTA LOST IN LOVE','trend.#PerthSantaFMinMacau'): return 'entertainment'\n")
rep("for a,b in [('Mamu','Kessler'),","for a,b in [('PERTHSANTA LOST IN LOVE','#PerthSantaFMinMacau'),('#PerthSantaFMinMacau','PERTHSANTA LOST IN LOVE'),('Mamu','Kessler'),")
rep("(06Z is not a fourth hour, so no slow tier)","(07Z is not a fourth hour, so no slow tier)")
rep("06Z is not a fourth hour, so no slow tier; under","07Z is not a fourth hour, so no slow tier; under")
TN='''trend names "PERTHSANTA LOST IN LOVE", #SmackDown, "You Can See Everything" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0600Z were "PERTHSANTA LOST IN LOVE", #PerthSantaFMinMacau, #PFLChicago, #SmackDown, "You Can See Everything", Heartbeat, Kessler and "ash trevino"; "PERTHSANTA LOST IN LOVE" and #PerthSantaFMinMacau are one event, the PerthSanta fan meeting in Macau; #PFLChicago, Heartbeat, Kessler and "ash trevino" not read for the overnight budget)'''
OLD='''trend names "Johnny Carson", Purdue, Memphis (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0506Z were Purdue, #SmackDown, "Johnny Carson", Memphis and Tulane; Memphis and Tulane are one event, the Memphis at Tulane college football game; #SmackDown and Tulane not read for the overnight budget)'''
rep(OLD,TN)
OLD2=OLD.replace('(each','(3 reads; each')
rep(OLD2,TN.replace('(each','(3 reads; each'))
rep("quote/repost words my/it + that;","quote/repost words just/what + the;")
rep("quote/repost words my/it + that (2+1)","quote/repost words just/what + the (2+1)")
rep('''common words "my", "it" and "that": "my lang:en is:quote -is:retweet", "it lang:en is:quote -is:retweet", "that lang:en is:retweet"''','''common words "just", "what" and "the": "just lang:en is:quote -is:retweet", "what lang:en is:quote -is:retweet", "the lang:en is:retweet"''')
rep("Overnight run at 2:00 AM ET (06:00 UTC Oct 17;","Overnight run at 3:03 AM ET (07:03 UTC Oct 17;")
rep("two-hour world, justice, markets, ai, tech, medicine due 06:03Z but cut","two-hour world, justice, markets, ai, tech, medicine due since 06:03Z but cut again")
rep("out_path = f'{REPO}/capture/2026/10/17/0600Z.json'","out_path = f'{REPO}/capture/2026/10/17/0703Z.json'")
rep("NO_REREC = {'2111143320311243129'}","NO_REREC = {'2111143320311243129'}\nSKIP_NEW = set()")
open('build_capture.py','w').write(s); print('ok')
