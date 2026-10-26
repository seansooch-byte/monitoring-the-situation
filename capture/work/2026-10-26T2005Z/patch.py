s=open('build_capture.py').read()
def R(a,b):
    global s
    n=s.count(a); assert n==1, (n,a[:90]); s=s.replace(a,b)
R('"""Build capture/2026/10/26/1902Z.json','"""Build capture/2026/10/26/2005Z.json')
R("work/2026-10-26T1902Z'","work/2026-10-26T2005Z'")
R("RUN_ID = '2026-10-26T1902Z'","RUN_ID = '2026-10-26T2005Z'")
R("STARTED = '2026-10-26T19:02:00Z'","STARTED = '2026-10-26T20:05:00Z'")
R("OBS_AT = '2026-10-26T19:03:00Z'","OBS_AT = '2026-10-26T20:06:00Z'")
R("READS_BEFORE = 619","READS_BEFORE = 598")
R("datetime(2026,10,26,19,3,tzinfo=timezone.utc).timestamp()  # 1902Z (1800Z used 18:01,","datetime(2026,10,26,20,6,tzinfo=timezone.utc).timestamp()  # 2005Z (1902Z used 19:03, 1800Z used 18:01,")
R("""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_koenig': 'trend_koenig.txt', 'trend_comey': 'trend_comey.txt', 'trend_gronk': 'trend_gronk.txt', 'trend_terra': 'trend_terra.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""",
"""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_ballondor': 'trend_ballondor.txt', 'trend_microsoft': 'trend_microsoft.txt', 'trend_verizon': 'trend_verizon.txt', 'trend_kane': 'trend_kane.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""")
R("""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_koenig','trend.Walter Koenig'),('trend_comey','trend.Maurene Comey'),('trend_gronk','trend.Gronk'),('trend_terra','trend.GPT-6.1 Terra'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""",
"""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_ballondor','trend.#BallonDor'),('trend_microsoft','trend.Microsoft'),('trend_verizon','trend.Verizon'),('trend_kane','trend.Harry Kane'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""")
R("""        if str(_x)=='trend.GPT-6.1 Terra': return 'ai'  # 1902Z""","""        if str(_x) in ('trend.#BallonDor','trend.Harry Kane'): return 'sports'  # 2005Z
        if str(_x)=='trend.Microsoft': return 'tech'  # 2005Z
        if str(_x)=='trend.Verizon': return 'tech'  # 2005Z
        if str(_x)=='trend.GPT-6.1 Terra': return 'ai'  # 1902Z""")
R("if _c.endswith('1902Z.json') and '/26/' in _c: continue","if _c.endswith('2005Z.json') and '/26/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}")
R("""        _last = '2026-10-26T1800Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online read this run;""",
"""        _last = '2026-10-26T1902Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science read this run;""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1902Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/2005Z.json'")
CAPTXT="(this 20Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last, the list was 651 long, so the 400 cap left out the 57 last six-hour posts, the 133 slowest-growing still-gaining posts and 61 of the 69 fourth-hour posts, and no cited post)"
R("(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 606 long, so the 400 cap left out the 71 last six-hour posts and the 135 slowest-growing still-gaining posts, and no cited post)",CAPTXT)
TN=('trend names "#BallonDor", "Microsoft", "Verizon" and "Harry Kane" ("<name> lang:en is:retweet", newest first, 25 each; "#BallonDor" (fifth, new), "Microsoft" (sixth, new), "Verizon" (ninth, new) and "Harry Kane" (tenth, new) are the top-ten US names with no posts attached in 1902Z; "Walter Koenig" (first), "Star Trek" (third), "Chekov" (fourth), "Brazil" (seventh) and "GPT-6.1 Terra" (eighth) had posts attached in 1902Z, and "#Fallout76Giveaway" (second) is a giveaway)')
i=s.index("'sources: references followed one hop"); j=s.index("quote/repost words the/this + is (quoted)",i)
s=s[:i]+"'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); "+TN+"; "+s[j:]
R("quote/repost words the/this + is (quoted)","quote/repost words you/and + my (quoted)")
R("two screening reads by id: 100 then 7 unread referenced","two screening reads by id: 100 then 8 unread referenced")
R("""'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each'""",
  """'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each'""")
# run.reason
R("f'Afternoon run (3:00 PM ET Oct 26 / 19:02 UTC Oct 26, the 19Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1800Z ended at 619, so no reads",
  "f'Afternoon run (4:05 PM ET Oct 26 / 20:05 UTC Oct 26, the 20Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1902Z ended at 598, so no reads")
R("unavailable; 19Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 606 ids, so the 400 cap left out the 71 last six-hour posts and the 135 slowest-growing still-gaining posts, and no cited post; 4 reads)",
  "unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours; 651 ids, so the 400 cap left out the 57 last six-hour posts, the 133 slowest-growing still-gaining posts and 61 of the 69 fourth-hour posts, and no cited post; 4 reads)")
a=s.index("""            f'trend names "Walter Koenig", "Maurene Comey", "Gronk" and "GPT-6.1 Terra" (4 reads;"""); b=s.index("\n",a)
s=s[:a]+"""            f'trend names "#BallonDor", "Microsoft", "Verizon" and "Harry Kane" (4 reads; "<name> lang:en is:retweet", newest first, 25; all four are new top-ten US names with no posts attached in 1902Z; "Walter Koenig", "Star Trek", "Chekov", "Brazil" and "GPT-6.1 Terra" had posts attached in 1902Z and "#Fallout76Giveaway" (second) is a giveaway); '"""+s[b:]
R("f'quote/repost words the/this + is (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1800Z, so culture/sports/online were next in rotation); '",
  "f'quote/repost words you/and + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1902Z, so news/money/science were next in rotation); '")
R("cut for the one hundred and fifty-seventh run","cut for the one hundred and fifty-eighth run")
R("cut for the one hundred and fifty-fourth run","cut for the one hundred and fifty-fifth run")
R("two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 7 left over, including the second-hop posts (all returned but 2110165104713183485, quoted by 2110222071229989249, which did not come back);",
  "two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 8 left over, including the second-hop posts (all returned);")
R("as in 1204Z through 1800Z;","as in 1204Z through 1902Z;")
R("f'Not read: news/money/science sensors,","f'Not read: culture/sports/online sensors,")
open('build_capture.py','w').write(s); print('ok')
