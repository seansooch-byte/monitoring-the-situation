s=open('build_capture.py').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70]); s=s.replace(a,b)
rep("Build capture/2026/10/17/0907Z.json","Build capture/2026/10/17/0959Z.json")
rep("work/2026-10-17T0907Z'","work/2026-10-17T0959Z'")
rep("RUN_ID = '2026-10-17T0907Z'","RUN_ID = '2026-10-17T0959Z'")
rep("STARTED = '2026-10-17T09:07:00Z'","STARTED = '2026-10-17T09:59:00Z'")
rep("OBS_AT = '2026-10-17T09:09:00Z'","OBS_AT = '2026-10-17T10:00:00Z'")
rep("READS_BEFORE = 761","READS_BEFORE = 743")
rep("READS_AFTER = 743","READS_AFTER = 726")
rep("datetime(2026,10,17,9,12,tzinfo","datetime(2026,10,17,10,3,tzinfo")
rep("""    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',
    'repost_it': 'repost_it.txt',
    'trend_lingorm': 'trend_lingorm.txt', 'trend_monica': 'trend_monica.txt', 'trend_violet': 'trend_violet.txt',""",
"""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',
    'repost_what': 'repost_what.txt',
    'trend_keonho': 'trend_keonho.txt', 'trend_nol': 'trend_nol.txt', 'trend_hogan': 'trend_hogan.txt',""")
rep("""    ('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),
    ('trend_lingorm','trend.#LingOrmBetweenUsConcertD1'),('trend_monica','trend.Mónica'),('trend_violet','trend.Violet'),""",
"""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_keonho','trend.KEONHO CAPTIVATES THE LENS'),('trend_nol','trend.NOL Festival'),('trend_hogan','trend.HOGAN EFFECT'),""")
KN=['KEONHO CAPTIVATES THE LENS','NOL Festival','IKEONIC','ACEKEON MAKNAE','5TH GEN IT BOY','HOGAN EFFECT']
rep("        if str(_x)=='trend.Kimmel': return 'entertainment'\n","        if str(_x)=='trend.Kimmel': return 'entertainment'\n        if str(_x) in "+repr(tuple('trend.'+k for k in KN))+": return 'music'\n")
pairs=[(a,b) for a in KN for b in KN if a!=b]
rep("for a,b in [('#LingOrmBetweenUsConcertD1',","for a,b in "+repr(pairs)[:-1]+",('#LingOrmBetweenUsConcertD1',")
rep("(09Z is not a fourth hour, so no slow tier); {len(watch_ids)}","(10Z is not a fourth hour, so no slow tier); {len(watch_ids)}")
OLD='''trend names #LingOrmBetweenUsConcertD1, Mónica, Violet (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0806Z were #LingOrmBetweenUsConcertD1, "THE WORLD BETWEEN LINGORM D1", #PerthSantaFMinMacau, "PERTHSANTA LOST IN LOVE", Mónica, "You Can See Everything" and Violet; #LingOrmBetweenUsConcertD1 and "THE WORLD BETWEEN LINGORM D1" are one event, day one of the LingOrm concert; Mónica is no single event, mostly unrelated posts mentioning the name; Violet is the Deadlock game hero; the PerthSanta pair and "You Can See Everything" were read in 0703Z and not again for the overnight budget)'''
TN='''trend names "KEONHO CAPTIVATES THE LENS", "NOL Festival", "HOGAN EFFECT" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; top-ten US names with no posts attached in 0907Z were "KEONHO CAPTIVATES THE LENS", "NOL Festival", IKEONIC, "ACEKEON MAKNAE", "5TH GEN IT BOY", "HOGAN EFFECT" and "Good Saturday"; the first six are one event, fan hashtag campaigns for CORTIS member Keonho and other acts at NOL Festival 2026 (#CORTIS_NOLFest2026), so IKEONIC, "ACEKEON MAKNAE" and "5TH GEN IT BOY" were not searched separately; "Good Saturday" not read for the overnight budget)'''
rep(OLD,TN)
rep(OLD.replace('(each','(3 reads; each'),TN.replace('(each','(3 reads; each'))
rep("quote/repost words and/my + it;","quote/repost words that/just + what;")
rep('''quote/repost words and/my + it (2+1; the unquoted and query was refused by X as ambiguous and cost one read, then re-run with "and" quoted)''','''quote/repost words that/just + what (2+1)''')
rep('''common words "and", "my" and "it": ("and" lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:retweet)''','''common words "that", "just" and "what": (that lang:en is:quote -is:retweet), (just lang:en is:quote -is:retweet), (what lang:en is:retweet)''')
rep("Overnight run at 5:07 AM ET (09:07 UTC Oct 17;","Overnight run at 5:59 AM ET (09:59 UTC Oct 17;")
rep("09Z is not a fourth hour, so no slow tier; under","10Z is not a fourth hour, so no slow tier; under")
rep("out_path = f'{REPO}/capture/2026/10/17/0907Z.json'","out_path = f'{REPO}/capture/2026/10/17/0959Z.json'")
open('build_capture.py','w').write(s); print('ok')
