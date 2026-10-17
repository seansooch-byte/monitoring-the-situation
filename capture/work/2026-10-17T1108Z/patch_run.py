s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70]); s=s.replace(a,b)
rep("Build capture/2026/10/17/0959Z.json","Build capture/2026/10/17/1108Z.json")
rep("work/2026-10-17T0959Z'","work/2026-10-17T1108Z'")
rep("RUN_ID = '2026-10-17T0959Z'","RUN_ID = '2026-10-17T1108Z'")
rep("STARTED = '2026-10-17T09:59:00Z'","STARTED = '2026-10-17T11:08:00Z'")
rep("OBS_AT = '2026-10-17T10:00:00Z'","OBS_AT = '2026-10-17T11:09:00Z'")
rep("READS_BEFORE = 743","READS_BEFORE = 718")
rep("READS_AFTER = 726","READS_AFTER = 701")
rep("datetime(2026,10,17,10,3,tzinfo","datetime(2026,10,17,11,13,tzinfo")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_keonho': 'trend_keonho.txt', 'trend_nol': 'trend_nol.txt', 'trend_hogan': 'trend_hogan.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_goodsat': 'trend_goodsat.txt', 'trend_lingorm': 'trend_lingorm.txt', 'trend_fourth': 'trend_fourth.txt',""")
rep("""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_keonho','trend.KEONHO CAPTIVATES THE LENS'),('trend_nol','trend.NOL Festival'),('trend_hogan','trend.HOGAN EFFECT'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_goodsat','trend.Good Saturday'),('trend_lingorm','trend.#LingOrmBetweenUsConcertD1'),('trend_fourth','trend.KEEP GOING AMAZING FOURTH'),""")
rep("        if str(_x)=='trend.Kimmel': return 'entertainment'\n","        if str(_x)=='trend.Kimmel': return 'entertainment'\n        if str(_x)=='trend.Good Saturday': return 'life'\n        if str(_x)=='trend.KEEP GOING AMAZING FOURTH': return 'entertainment'\n")
rep("(10Z is not a fourth hour, so no slow tier); {len(watch_ids)}","(11Z is not a fourth hour, so no slow tier); {len(watch_ids)}")
OLD='''trend names "KEONHO CAPTIVATES THE LENS", "NOL Festival", "HOGAN EFFECT" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0907Z were "KEONHO CAPTIVATES THE LENS", "NOL Festival", IKEONIC, "ACEKEON MAKNAE", "5TH GEN IT BOY", "HOGAN EFFECT" and "Good Saturday"; the first six are one event, fan hashtag campaigns for CORTIS member Keonho and other acts at NOL Festival 2026 (#CORTIS_NOLFest2026), so IKEONIC, "ACEKEON MAKNAE" and "5TH GEN IT BOY" were not searched separately; "Good Saturday" not read for the overnight budget)'''
TN='''trend names "Good Saturday", #LingOrmBetweenUsConcertD1, "KEEP GOING AMAZING FOURTH" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0959Z were "Good Saturday", #LingOrmBetweenUsConcertD1, "THE WORLD BETWEEN LINGORM D1" and "KEEP GOING AMAZING FOURTH"; #LingOrmBetweenUsConcertD1 and "THE WORLD BETWEEN LINGORM D1" are one event, day one of the LingOrm concert, so the second was not searched separately; "Good Saturday" is no single event, mostly weekend-greeting posts; "KEEP GOING AMAZING FOURTH" is a fan campaign for day two of the concert by actor Fourth Nattawat (#FourthConcertD2))'''
rep(OLD,TN)
rep(OLD.replace('(each','(3 reads; each'),TN.replace('(each','(3 reads; each'))
rep("quote/repost words that/just + what;","quote/repost words the/this + is;")
rep('''quote/repost words that/just + what (2+1)''','''quote/repost words the/this + is (2+1)''')
rep('''common words "that", "just" and "what": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet)''','''common words "the", "this" and "is": (the lang:en is:quote -is:retweet), (this lang:en is:quote -is:retweet), (is lang:en is:retweet)''')
rep("Overnight run at 5:59 AM ET (09:59 UTC Oct 17;","Overnight run at 7:08 AM ET (11:08 UTC Oct 17;")
rep("10Z is not a fourth hour, so no slow tier; under","11Z is not a fourth hour, so no slow tier; under")
rep("out_path = f'{REPO}/capture/2026/10/17/0959Z.json'","out_path = f'{REPO}/capture/2026/10/17/1108Z.json'")
open('build_capture.py','w').write(s); print('ok')
