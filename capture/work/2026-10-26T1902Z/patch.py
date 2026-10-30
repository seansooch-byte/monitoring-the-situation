s=open('build_capture.py').read()
def R(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n>=1, ('missing',a[:80])
    if cnt==1: assert n==1, ('multi',a[:80],n)
    s=s.replace(a,b)
R('"""Build capture/2026/10/26/1800Z.json','"""Build capture/2026/10/26/1902Z.json')
R("work/2026-10-26T1800Z'","work/2026-10-26T1902Z'")
R("RUN_ID = '2026-10-26T1800Z'","RUN_ID = '2026-10-26T1902Z'")
R("STARTED = '2026-10-26T18:00:00Z'","STARTED = '2026-10-26T19:02:00Z'")
R("OBS_AT = '2026-10-26T18:01:00Z'","OBS_AT = '2026-10-26T19:03:00Z'")
R("READS_BEFORE = 639","READS_BEFORE = 619")
R("datetime(2026,10,26,18,1,tzinfo=timezone.utc).timestamp()  # 1800Z (1705Z","datetime(2026,10,26,19,3,tzinfo=timezone.utc).timestamp()  # 1902Z (1800Z used 18:01, 1705Z")
R("""    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'trend_basetrack': 'trend_basetrack.txt', 'trend_lula': 'trend_lula.txt', 'trend_sherman': 'trend_sherman.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""",
"""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',
    'repost_is': 'repost_is.txt',
    'trend_koenig': 'trend_koenig.txt', 'trend_comey': 'trend_comey.txt', 'trend_gronk': 'trend_gronk.txt', 'trend_terra': 'trend_terra.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_online': 'sensor_online.txt', 'sensor_sports': 'sensor_sports.txt',""")
R("""    ('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('trend_basetrack','trend.Base Track'),('trend_lula','trend.Lula'),('trend_sherman','trend.Sherman'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""",
"""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_koenig','trend.Walter Koenig'),('trend_comey','trend.Maurene Comey'),('trend_gronk','trend.Gronk'),('trend_terra','trend.GPT-6.1 Terra'),
    ('sensor_culture','sensors.culture'),('sensor_online','sensors.online'),('sensor_sports','sensors.sports'),""")
R("""        if str(_x)=='trend.Lula': return 'world'  # 1800Z""","""        if str(_x)=='trend.GPT-6.1 Terra': return 'ai'  # 1902Z: OpenAI model name trending
        if str(_x)=='trend.Lula': return 'world'  # 1800Z""")
R("if _c.endswith('1800Z.json') and '/26/' in _c: continue","if _c.endswith('1902Z.json') and '/26/' in _c: continue")
R("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}",
  "SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}")
R("""        _last = '2026-10-26T1705Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science read this run;""",
"""        _last = '2026-10-26T1800Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online read this run;""")
R("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1800Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/26/1902Z.json'")
# watch sweep text
R("(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 602 long, so the 400 cap left out the 70 last six-hour posts and the 132 slowest-growing still-gaining posts, and no cited post)",
  "(this 19Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 606 long, so the 400 cap left out the 71 last six-hour posts and the 135 slowest-growing still-gaining posts, and no cited post)")
TN = ('trend names "Walter Koenig", "Maurene Comey", "Gronk" and "GPT-6.1 Terra" ("<name> lang:en is:retweet", newest first, 25 each; "Walter Koenig" (first; his death, one event with "Chekov" (third), "Star Trek" (fifth), "Babylon 5" (seventh) and "Bester" (tenth), and with "Shatner" and "Takei"), "Maurene Comey" (eighth) and "Gronk" (ninth) are top-ten US names with no posts attached in 1800Z; "GPT-6.1 Terra" (eleventh, new) was read in place of the rest: "#Fallout76Giveaway" (second) is a giveaway and "#DestinyFashion" (sixth) a game hashtag, and "Brazil" (fourth) had posts attached in 1800Z)')
import re
i=s.index("'sources: references followed one hop"); j=s.index("quote/repost words just/what + the (quoted)",i)
s=s[:i]+"'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "+TN+"; "+s[j:]
R("quote/repost words just/what + the (quoted)","quote/repost words the/this + is (quoted)")
R("""two screening reads by id: 100 then 2 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts (all returned); no first""","""two screening reads by id: 100 then 7 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; no first""")
R("""'2 quote pages + 1 repost page (budget), common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet), newest first, 25 each'""",
  """'2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet), newest first, 25 each'""")
open('build_capture.py','w').write(s)
print('ok')
