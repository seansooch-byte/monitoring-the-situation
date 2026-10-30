s=open('build_capture.py').read()
import re
OLDTN=re.findall(r'three of the top-ten US names with no posts attached in 1207Z.*?had posts attached in 1207Z',s)[0]
TN=open('tn.txt').read().strip()
print('oldtn count',s.count(OLDTN))
s=s.replace('trend names "Blessed Sunday", "la liga mx" and "#AskFFT"','trend names "#PITvsNO", "Jaylen Warren" and "#TTPatEFW26ICONSIAM"').replace(OLDTN,TN)
R=[
("Build capture/2026/10/25/1301Z.json","Build capture/2026/10/25/1404Z.json"),
("work/2026-10-25T1301Z'","work/2026-10-25T1404Z'"),
("RUN_ID = '2026-10-25T1301Z'","RUN_ID = '2026-10-25T1404Z'"),
("STARTED = '2026-10-25T13:01:00Z'","STARTED = '2026-10-25T14:04:00Z'"),
("OBS_AT = '2026-10-25T13:02:00Z'","OBS_AT = '2026-10-25T14:05:00Z'"),
("READS_BEFORE = 737","READS_BEFORE = 717"),
("datetime(2026,10,25,13,3,tzinfo=timezone.utc).timestamp()  # 1301Z (","datetime(2026,10,25,14,5,tzinfo=timezone.utc).timestamp()  # 1404Z (1301Z used 13:03, "),
("'quote_this': 'quote_this.txt', 'quote_is': 'quote_is.txt',","'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt',"),
("'repost_you': 'repost_you.txt',","'repost_it': 'repost_it.txt',"),
("'trend_blessedsunday': 'trend_blessedsunday.txt', 'trend_ligamx': 'trend_ligamx.txt', 'trend_askfft': 'trend_askfft.txt',","'trend_pitvsno': 'trend_pitvsno.txt', 'trend_jaylenwarren': 'trend_jaylenwarren.txt', 'trend_ttpat': 'trend_ttpat.txt',"),
("'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',","'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"),
("('quote_this','quote'),('quote_is','quote'),('repost_you','repost'),","('quote_and','quote'),('quote_my','quote'),('repost_it','repost'),"),
("('trend_blessedsunday','trend.Blessed Sunday'),('trend_ligamx','trend.la liga mx'),('trend_askfft','trend.#AskFFT'),","('trend_pitvsno','trend.#PITvsNO'),('trend_jaylenwarren','trend.Jaylen Warren'),('trend_ttpat','trend.#TTPatEFW26ICONSIAM'),"),
("('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),","('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"),
("if _c.endswith('1301Z.json') and '/25/' in _c: continue","if _c.endswith('1404Z.json') and '/25/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'culture','sports','online'}","SENSOR_READ = {'news','money','science'}"),
("_last = '2026-10-25T1207Z'","_last = '2026-10-25T1301Z'"),
("rotation: culture/sports/online read this run","rotation: news/money/science read this run"),
('common words "this", "is" and "you", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("is" lang:en is:quote -is:retweet), ("you" lang:en is:retweet)',
 'common words "and", "my" and "it", each quoted so X does not reject a bare stopword: ("and" lang:en is:quote -is:retweet), ("my" lang:en is:quote -is:retweet), ("it" lang:en is:retweet)'),
("one hundred and twenty-seventh run","one hundred and twenty-eighth run"),
("one hundred and twenty-fifth run","one hundred and twenty-sixth run"),
("one hundred and twenty-third run","one hundred and twenty-fourth run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1301Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/1404Z.json'"),
("sensors culture/sports/online (one read each)","sensors news/money/science (one read each)"),
("# 5) request picks (1301Z: none read)","# 5) request picks (1404Z: none read)"),
("(this 13Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 574 long, so the 400 cap left out the 43 last six-hour posts and the 131 slowest-growing still-gaining posts, and no cited post)",
 "(this 14Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 567 long, so the 400 cap left out the 23 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post)"),
("quote/repost words this/is + you (quoted)","quote/repost words and/my + it (quoted)"),
("then 27 (the 9 remaining plus 18 second-hop posts) in the second read; 7 third-hop posts left unread for the budget)","then 31 (the 2 remaining plus 29 second-hop posts) in the second read; 13 third-hop posts left unread for the budget)"),
("        if str(_x)=='trend.#AskFFT': return 'sports'  # 1301Z: fantasy-football advice hashtag\n","        if str(_x)=='trend.#PITvsNO': return 'sports'  # 1404Z: Steelers v Saints, NFL Paris game\n        if str(_x)=='trend.Jaylen Warren': return 'sports'  # 1404Z: same game\n        if str(_x)=='trend.#TTPatEFW26ICONSIAM': return 'entertainment'  # 1404Z: Thai actors at ELLE Fashion Week\n        if str(_x)=='trend.#AskFFT': return 'sports'  # 1301Z: fantasy-football advice hashtag\n"),
("for a,b in [('la liga mx','Rayados'),","for a,b in [('#PITvsNO','Jaylen Warren'),('Jaylen Warren','#PITvsNO'),('#PITvsNO','#HereWeGo'),('#PITvsNO','Patrick Queen'),('#PITvsNO','Justin Reid'),('#TTPatEFW26ICONSIAM','TEETEEPOR HOOKS EFW26'),('la liga mx','Rayados'),"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Morning run (9:01 AM ET"):
    lines[k]="            f'Morning run (10:04 AM ET Oct 25 / 14:04 UTC Oct 25, the 14Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to pace the daily budget): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1301Z ended at 717, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 14Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 567 ids, so the 400 cap left out the 23 last six-hour posts and the 144 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'quote/repost words this/is"):
    lines[k]="            f'quote/repost words and/my + it (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 1301Z, so news/money/science were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 31 (the 2 remaining plus 29 second-hop posts) (ids left out earlier as likely paid or sexual were not read again; 13 third-hop posts left unread for the budget); 130 returned; 2108062331095908717 came back Not Found again in both reads, as in 1105Z through 1301Z; story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 1301Z (watch.json dropped 2113798038586282014, 2113796755837866482, 2113661771986669791 and 2113641118483001432 and added 2114130103756325057); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: news/money/science sensors"):
    lines[k]="            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
