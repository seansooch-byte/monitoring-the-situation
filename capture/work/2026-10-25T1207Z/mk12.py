s=open('build_capture.py').read()
import re
OLDTN=re.findall(r'three of the top-ten US names with no posts attached in 1002Z.*?had posts attached in 1002Z',s)[0]
TN=open('tn.txt').read().strip()
assert s.count(OLDTN)>=1, 'oldtn'
s=s.replace('trend names "Cheesecake Factory", "Courtois" and "Blessed Sunday"','trend names "Good Sunday", "#BladeRunnerMurderforcash" and "Lunin"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1107Z.json","Build capture/2026/10/25/1207Z.json"),
("work/2026-10-25T1107Z'","work/2026-10-25T1207Z'"),
("RUN_ID = '2026-10-25T1107Z'","RUN_ID = '2026-10-25T1207Z'"),
("STARTED = '2026-10-25T11:07:00Z'","STARTED = '2026-10-25T12:07:00Z'"),
("OBS_AT = '2026-10-25T11:08:00Z'","OBS_AT = '2026-10-25T12:08:00Z'"),
("READS_BEFORE = 781","READS_BEFORE = 757"),
("READS_USED = 20  # 781-757=24 but 4 reads went to the 7:03 AM ET briefing during this run","READS_USED = READS_BEFORE - READS_AFTER"),
("datetime(2026,10,25,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (","datetime(2026,10,25,12,9,tzinfo=timezone.utc).timestamp()  # 1207Z (1107Z used 11:10, "),
("'quote_and': 'quote_and.txt', 'quote_it': 'quote_it.txt',","'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',"),
("'repost_that': 'repost_that.txt',","'repost_the': 'repost_the.txt',"),
("'trend_cheesecake': 'trend_cheesecake.txt', 'trend_courtois': 'trend_courtois.txt', 'trend_blessedsunday': 'trend_blessedsunday.txt',","'trend_goodsunday': 'trend_goodsunday.txt', 'trend_bladerunner': 'trend_bladerunner.txt', 'trend_lunin': 'trend_lunin.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_and','quote'),('quote_it','quote'),('repost_that','repost'),","('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),"),
("('trend_cheesecake','trend.Cheesecake Factory'),('trend_courtois','trend.Courtois'),('trend_blessedsunday','trend.Blessed Sunday'),","('trend_goodsunday','trend.Good Sunday'),('trend_bladerunner','trend.#BladeRunnerMurderforcash'),('trend_lunin','trend.Lunin'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1107Z.json') and '/25/' in _c: continue","if _c.endswith('1207Z.json') and '/25/' in _c: continue"),
("for g in ('culture','sports','online')}","for g in ('news','money','science')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T1002Z'","_last = '2026-10-25T1107Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "and", "it" and "that", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet)',
 'common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)'),
("one hundred and twenty-fifth run","one hundred and twenty-sixth run"),
("one hundred and twenty-third run","one hundred and twenty-fourth run"),
("one hundred and twenty-first run","one hundred and twenty-second run"),
("kept to about 20 reads to pace the daily budget in the 06:00-11:00 UTC band, up to 20","kept to about 20 reads to pace the daily budget; 12:00-05:00 UTC band, up to 42"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1207Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1107Z: none read)","# 5) request picks (1207Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then 35 (the 9 remaining plus 26 second-hop posts) in the second read; 21 third-hop posts left unread for the budget)","two screening reads by id (100 unread referenced posts, most pointed-at first, then 41 (the 18 remaining plus 23 second-hop posts) in the second read; 16 third-hop posts left unread for the budget)"),
("quote/repost words and/it + that (quoted)","quote/repost words just/what + the (quoted)"),
("(this 11Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 562 long, so the 400 cap left out the 34 last six-hour posts and the 128 slowest-growing still-gaining posts, and no cited post)",
 "(this 12Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 567 long, so the 400 cap left out the 31 last six-hour posts and the 136 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.Blessed Sunday': return 'life'  # 1107Z\n","        if str(_x)=='trend.Blessed Sunday': return 'life'  # 1107Z\n        if str(_x)=='trend.Lunin': return 'sports'  # 1207Z: Lunin starts in El Clasico for Courtois\n        if str(_x)=='trend.#BladeRunnerMurderforcash': return 'gaming'  # 1207Z: Love and Deepspace (Papergames) fan campaign\n"),
("for a,b in [('Niners','Commanders'),","for a,b in [('Lunin','Courtois'),('Courtois','Lunin'),('#BladeRunnerMurderforcash','#BladeRunnerEatsPPGsCowDung'),('Niners','Commanders'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (7:07 AM ET"):
    lines[k]="            f'Morning run (8:07 AM ET Oct 25 / 12:07 UTC Oct 25, the 12Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1107Z ended at 757, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 567 ids, so the 400 cap left out the 31 last six-hour posts and the 136 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words and/it"):
    lines[k]="            f'quote/repost words just/what + the (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1107Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 41 (the 18 remaining plus 23 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 16 third-hop posts left unread for the budget); 141 returned; 2108062331095908717 came back Not Found again as an expansion error, as in 1105Z through 1107Z, and 2113507644690583691 as an Authorization Error expansion; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 1107Z (watch.json dropped 2113756498861944954 and 2113762242327892456 and added 2114294862120104201); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
