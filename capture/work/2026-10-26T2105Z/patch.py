s=open('build_capture.py').read()
def R(a,b):
    global s
    n=s.count(a); assert n==1, (n,a[:90]); s=s.replace(a,b)
R('"""Build capture/2026/10/26/2005Z.json','"""Build capture/2026/10/26/2105Z.json')
R("work/2026-10-26T2005Z'","work/2026-10-26T2105Z'")
R("RUN_ID = '2026-10-26T2005Z'","RUN_ID = '2026-10-26T2105Z'")
R("STARTED = '2026-10-26T20:05:00Z'","STARTED = '2026-10-26T21:05:00Z'")
R("OBS_AT = '2026-10-26T20:06:00Z'","OBS_AT = '2026-10-26T21:06:00Z'")
R("READS_BEFORE = 598","READS_BEFORE = 577")
R("datetime(2026,10,26,20,6,tzinfo=timezone.utc).timestamp()  # 2005Z (1902Z used 19:03,","datetime(2026,10,26,21,6,tzinfo=timezone.utc).timestamp()  # 2105Z (2005Z used 20:06, 1902Z used 19:03,")
R("""    'quote_you': 'quote_you.txt', 'quote_and': 'quote_and.txt',
    'repost_my': 'repost_my.txt',
    'trend_ballondor': 'trend_ballondor.txt', 'trend_microsoft': 'trend_microsoft.txt', 'trend_verizon': 'trend_verizon.txt', 'trend_kane': 'trend_kane.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_just': 'repost_just.txt',
    'trend_koenig': 'trend_koenig.txt', 'trend_scal': 'trend_scal.txt', 'trend_terra': 'trend_terra.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""")
R("""    ('quote_you','quote'),('quote_and','quote'),('repost_my','repost'),
    ('trend_ballondor','trend.#BallonDor'),('trend_microsoft','trend.Microsoft'),('trend_verizon','trend.Verizon'),('trend_kane','trend.Harry Kane'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),
    ('trend_koenig','trend.Walter Koenig'),('trend_scal','trend.Scal'),('trend_terra','trend.GPT-6.1 Terra'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""")
R("""        if str(_x) in ('trend.#BallonDor','trend.Harry Kane'): return 'sports'  # 2005Z""","""        if str(_x)=='trend.Walter Koenig': return 'entertainment'  # 2105Z
        if str(_x) in ('trend.#BallonDor','trend.Harry Kane'): return 'sports'  # 2005Z""")
R("if _c.endswith('2005Z.json') and '/26/' in _c: continue","if _c.endswith('2105Z.json') and '/26/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("""        _last = '2026-10-26T1902Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science read this run;""",
"""        _last = '2026-10-26T2005Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online read this run;""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/2005Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/2105Z.json'")
CAPTXT="(this 21Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 597 long, so the 400 cap left out the 78 last six-hour posts and the 119 slowest-growing still-gaining posts, and no cited post)"
R("(this 20Z run is a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last, the list was 651 long, so the 400 cap left out the 57 last six-hour posts, the 133 slowest-growing still-gaining posts and 61 of the 69 fourth-hour posts, and no cited post)",CAPTXT)
TN=('trend names "Walter Koenig", "Scal" and "GPT-6.1 Terra" ("<name> lang:en is:retweet", newest first, 25 each; "Walter Koenig" (second), "Scal" (fifth, new) and "GPT-6.1 Terra" (tenth) are the top-ten US names with no posts attached in 2005Z; "Star Trek" (sixth) and "Chekov" (eighth) are one event with "Walter Koenig" (his death) and were not searched separately; "#BallonDor" (first), "Harry Kane" (fourth), "Microsoft" (seventh) and "Verizon" (ninth) had posts attached in 2005Z, and "#Fallout76Giveaway" (third) is a giveaway)')
i=s.index("'sources: references followed one hop"); j=s.index("quote/repost words you/and + my (quoted)",i)
s=s[:i]+"'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/online/sports (one read each); "+TN+"; "+s[j:]
R("quote/repost words you/and + my (quoted)","quote/repost words it/that + just (quoted)")
R("two screening reads by id: 100 then 8 unread referenced","two screening reads by id: 100 then 37 unread referenced")
R("including the second-hop posts; no first- or second-hop post was left over;","including the second-hop posts; 13 third-hop posts left unread for the budget;")
R("""'2 quote pages + 1 repost page (budget), common words "you", "and" and "my", each quoted so X does not reject a bare stopword: ("you" lang:en is:quote -is:retweet), ("and" lang:en is:quote -is:retweet), ("my" lang:en is:retweet), newest first, 25 each'""",
  """'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each'""")
R("f'Afternoon run (4:05 PM ET Oct 26 / 20:05 UTC Oct 26, the 20Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1902Z ended at 598, so no reads",
  "f'Evening run (5:05 PM ET Oct 26 / 21:05 UTC Oct 26, the 21Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2005Z ended at 577, so no reads")
R("unavailable; 20Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours; 651 ids, so the 400 cap left out the 57 last six-hour posts, the 133 slowest-growing still-gaining posts and 61 of the 69 fourth-hour posts, and no cited post; 4 reads)",
  "unavailable; 21Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 597 ids, so the 400 cap left out the 78 last six-hour posts and the 119 slowest-growing still-gaining posts, and no cited post; 4 reads)")
a=s.index("""            f'trend names "#BallonDor", "Microsoft", "Verizon" and "Harry Kane" (4 reads;"""); b=s.index("\n",a)
s=s[:a]+"""            f'trend names "Walter Koenig", "Scal" and "GPT-6.1 Terra" (3 reads; "<name> lang:en is:retweet", newest first, 25; the top-ten US names with no posts attached in 2005Z; "Star Trek" and "Chekov" are one event with "Walter Koenig" (his death) and were not searched separately; "#BallonDor", "Harry Kane", "Microsoft" and "Verizon" had posts attached in 2005Z and "#Fallout76Giveaway" (third) is a giveaway); '"""+s[b:]
R("f'quote/repost words you/and + my (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1902Z, so news/money/science were next in rotation); '",
  "f'quote/repost words it/that + just (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2005Z, so culture/sports/online were next in rotation); '")
R("cut for the one hundred and fifty-eighth run","cut for the one hundred and fifty-ninth run")
R("cut for the one hundred and fifty-fifth run","cut for the one hundred and fifty-sixth run")
R("two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 8 left over, including the second-hop posts (all returned); no first- or second-hop post was left over (ids left out earlier as likely paid or sexual were not read again);",
  "two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then the 37 left over, including the second-hop posts (all returned but 2108062331095908717, Not Found again); 13 third-hop posts were left unread for the budget (ids left out earlier as likely paid or sexual were not read again);")
R("as in 1204Z through 1902Z;","as in 1204Z through 2005Z;")
R("f'Not read: culture/sports/online sensors,","f'Not read: news/money/science sensors,")
open('build_capture.py','w').write(s); print('ok')
