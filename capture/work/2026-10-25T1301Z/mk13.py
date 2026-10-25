s=open('build_capture.py').read()
import re
OLDTN=re.findall(r'three of the top-ten US names with no posts attached in 1107Z.*?had posts attached in 1107Z',s)[0]
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
s=s.replace('trend names "Good Sunday", "#BladeRunnerMurderforcash" and "Lunin"','trend names "Blessed Sunday", "la liga mx" and "#AskFFT"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1207Z.json","Build capture/2026/10/25/1301Z.json"),
("work/2026-10-25T1207Z'","work/2026-10-25T1301Z'"),
("RUN_ID = '2026-10-25T1207Z'","RUN_ID = '2026-10-25T1301Z'"),
("STARTED = '2026-10-25T12:07:00Z'","STARTED = '2026-10-25T13:01:00Z'"),
("OBS_AT = '2026-10-25T12:08:00Z'","OBS_AT = '2026-10-25T13:02:00Z'"),
("READS_BEFORE = 757","READS_BEFORE = 737"),
("datetime(2026,10,25,12,9,tzinfo=timezone.utc).timestamp()  # 1207Z (","datetime(2026,10,25,13,3,tzinfo=timezone.utc).timestamp()  # 1301Z (1207Z used 12:09, "),
("'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',","'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',"),
("'repost_the': 'repost_the.txt',","'repost_you': 'repost_you.txt',"),
("'trend_goodsunday': 'trend_goodsunday.txt', 'trend_bladerunner': 'trend_bladerunner.txt', 'trend_lunin': 'trend_lunin.txt',","'trend_blessedsunday': 'trend_blessedsunday.txt', 'trend_ligamx': 'trend_ligamx.txt', 'trend_askfft': 'trend_askfft.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),","('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),"),
("('trend_goodsunday','trend.Good Sunday'),('trend_bladerunner','trend.#BladeRunnerMurderforcash'),('trend_lunin','trend.Lunin'),","('trend_blessedsunday','trend.Blessed Sunday'),('trend_ligamx','trend.la liga mx'),('trend_askfft','trend.#AskFFT'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1207Z.json') and '/25/' in _c: continue","if _c.endswith('1301Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-25T1107Z'","_last = '2026-10-25T1207Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "just", "what" and "the", each quoted so X does not reject a bare stopword: ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:retweet)',
 'common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)'),
("one hundred and twenty-sixth run","one hundred and twenty-seventh run"),
("one hundred and twenty-fourth run","one hundred and twenty-fifth run"),
("one hundred and twenty-second run","one hundred and twenty-third run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1207Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1301Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (1207Z: none read)","# 5) request picks (1301Z: none read)"),
("(this 12Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 567 long, so the 400 cap left out the 31 last six-hour posts and the 136 slowest-growing still-gaining posts, and no cited post)",
 "(this 13Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 574 long, so the 400 cap left out the 43 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x)=='trend.Blessed Sunday': return 'life'  # 1107Z\n","        if str(_x)=='trend.Blessed Sunday': return 'life'  # 1107Z\n        if str(_x)=='trend.#AskFFT': return 'sports'  # 1301Z: fantasy-football advice hashtag\n        if str(_x)=='trend.la liga mx': return 'sports'  # 1301Z: Liga MX (empty lang:en stream)\n"),
("for a,b in [('Lunin','Courtois'),","for a,b in [('la liga mx','Rayados'),('Lunin','Courtois'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (8:07 AM ET"):
    lines[k]="            f'Morning run (9:01 AM ET Oct 25 / 13:01 UTC Oct 25, the 13Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1207Z ended at 737, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 574 ids, so the 400 cap left out the 43 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words just/what"):
    lines[k]="            f'quote/repost words this/is + you (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1207Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 27 (the 9 remaining plus 18 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 7 third-hop posts left unread for the budget); 124 returned; 2108062331095908717 came back Not Found again, as in 1105Z through 1207Z, and 2113761748192841920 came back Not Found in both reads; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 1207Z (watch.json dropped 2113776971603689874, 2113786051009696177 and 2113772307663458640 and added 2113661771986669791, 2113944605888819292 and 2113641118483001432); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
