s=open('build_capture.py').read()
def rep(a,b,count=1):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,count)
rep('capture/2026/10/27/1416Z.json from','capture/2026/10/27/1503Z.json from')
rep("work/2026-10-27T1416Z'","work/2026-10-27T1503Z'")
rep("RUN_ID = '2026-10-27T1416Z'","RUN_ID = '2026-10-27T1503Z'")
rep("STARTED = '2026-10-27T14:16:00Z'","STARTED = '2026-10-27T15:03:00Z'")
rep("OBS_AT = '2026-10-27T14:17:00Z'","OBS_AT = '2026-10-27T15:04:00Z'")
rep("READS_BEFORE = 706","READS_BEFORE = 688")
rep("datetime(2026,10,27,14,17,tzinfo=timezone.utc).timestamp()  # 1416Z (","datetime(2026,10,27,15,4,tzinfo=timezone.utc).timestamp()  # 1503Z (1416Z used 14:17, ")
rep("""    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt',""","""    'quote_the': 'quote_the.txt', 'quote_this': 'quote_this.txt',""")
rep("""    'repost_what': 'repost_what.txt',""","""    'repost_is': 'repost_is.txt',""")
rep("""    'trend_shawnhatosy': 'trend_shawnhatosy.txt',""","""    'trend_ericswalwell': 'trend_ericswalwell.txt', 'trend_beverlyhills': 'trend_beverlyhills.txt', 'trend_maozedong': 'trend_maozedong.txt',""")
rep("""    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',""","""    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',""")
rep("""    ('quote_that','quote'),('quote_just','quote'),('repost_what','repost'),
    ('trend_shawnhatosy','trend.Shawn Hatosy'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),""","""    ('quote_the','quote'),('quote_this','quote'),('repost_is','repost'),
    ('trend_ericswalwell','trend.Eric Swalwell'),('trend_beverlyhills','trend.Beverly Hills'),('trend_maozedong','trend.Mao Zedong'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),""")
rep("""        if str(_x) in ('trend.Shawn Hatosy',): return 'entertainment'  # 1416Z: actor on The Pitt""","""        if str(_x) in ('trend.Eric Swalwell','trend.Beverly Hills'): return 'justice'  # 1503Z: FBI search of a Beverly Hills mansion in the Eric Swalwell investigation (one event)
        if str(_x) in ('trend.Mao Zedong',): return 'sports'  # 1503Z: Kylian Mbappé apology and sponsor fallout over the Mao Zedong meme
        if str(_x) in ('trend.Shawn Hatosy',): return 'entertainment'  # 1416Z: actor on The Pitt""")
rep("if _c.endswith('1416Z.json') and '/27/' in _c: continue","if _c.endswith('1503Z.json') and '/27/' in _c: continue")
rep("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}")
rep("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}")
rep("_last = '2026-10-27T1259Z'","_last = '2026-10-27T1416Z'")
rep("not read this run (rotation: news/money/science read this run;","not read this run (rotation: culture/sports/online read this run;")
rep("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1416Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/27/1503Z.json'")
rep("one hundred and seventy-third run (kept","one hundred and seventy-fourth run (kept")
rep("one hundred and seventy-sixth run (kept","one hundred and seventy-seventh run (kept")
rep('2 quote pages + 1 repost page (budget), common words "that", "just" and "what", each quoted so X does not reject a bare stopword: ("that" lang:en is:quote -is:retweet), ("just" lang:en is:quote -is:retweet), ("what" lang:en is:retweet)',
    '2 quote pages + 1 repost page (budget), common words "the", "this" and "is", each quoted so X does not reject a bare stopword: ("the" lang:en is:quote -is:retweet), ("this" lang:en is:quote -is:retweet), ("is" lang:en is:retweet)')
# text sections
L=s.split('\n')
def setline(prefix,new):
    idx=[i for i,l in enumerate(L) if l.startswith(prefix)]
    assert len(idx)==1,(prefix,idx); L[idx[0]]=new
LEFT='2110913107094606330, 2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
WATCHDESC=("this 15Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 525 long, so the 400 cap left out the 91 last six-hour posts, the 22 slowest-growing still-gaining posts and 12 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post), because the 301 watch.json ids plus the cited ids came to more than 400; no pulse-cited post was left out")
i=[k for k,l in enumerate(L) if l.startswith("    f'get_posts_by_ids of requests/watch.json")]; assert len(i)==1
l=L[i[0]]; a=l.index('(this 14Z run'); b=l.index('); {len(watch_ids)} ids read')
L[i[0]]=l[:a]+'('+WATCHDESC+l[b:]
TR=('trend names "Eric Swalwell", "Beverly Hills" and "Mao Zedong" ("<name> lang:en is:retweet", newest first, 25 each; the top-ten US names with no posts attached earlier today that are not greetings: "Eric Swalwell" (second, new) and "Beverly Hills" (fifth, new) are one event, the FBI search of a Beverly Hills mansion in the Eric Swalwell investigation; "Mao Zedong" (tenth, new) is the Kylian Mbappé apology over the Mao Zedong meme; '
    '"Good Tuesday" (first) and "Taco Tuesday" (sixth) are greetings; "#BladeRunnerLovesPPGsCowDung" (fourth), "#中国北京彻查上海叠纸" (seventh) and "#BeijingMustInvestigatePPGNow" (eighth) had posts attached in 1259Z; "Noah Wyle" (third) and "$SOFI" (ninth) had posts attached earlier today)')
setline("    'sources: references followed one hop",
 "    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "+TR.replace("'","\\'")+"; quote/repost words the/this + is (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id: 100, then 21 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; no third-hop post was left unread; story clusters not read for the budget; screened by id with global floor/pace',")
setline("            f'Morning run (10:16 AM ET",
 "            f'Morning run (11:03 AM ET Oct 27 / 15:03 UTC Oct 27, the 15Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1416Z ended at 688, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '")
setline("            f'Watch {len(watch_returned)} of {len(watch_ids)} (",
 "            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 15Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 525 ids, so the 400 cap left out the 91 last six-hour posts, the 22 slowest-growing still-gaining posts and 12 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '")
setline("            f'trend name \"Shawn Hatosy\"", "            f'"+TR.replace("'","\\'")+" (3 reads); '")
setline("            f'quote/repost words that/just",
 "            f'quote/repost words the/this + is (3 reads, each word quoted; 1416Z used that/just + what); sensors culture/sports/online (3 reads; news/money/science read 1416Z, so culture/sports/online were next in rotation); '")
setline("            f'two screening reads by id:",
 "            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (100 returned; 2108062331095908717 Not Found again, pointed at as a referenced post), then 21 second-hop posts (all returned; 2108062331095908717 not read again); no third-hop post was left unread (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1416Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, cited on the pulse and in watch.json) came back Not Found for the fourth run running; the same quote is still up from theMadridZone (2114708299644023175, already captured), and the Mao Zedong trend stream this run is about the fallout (Mbappé apology, Chinese sponsors); story clusters (search_news) not read for the budget. '")
setline("            f'Not read: culture/sports/online sensors",
 "            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '")
open('build_capture.py','w').write('\n'.join(L)); print('ok')
