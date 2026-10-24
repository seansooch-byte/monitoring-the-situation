s=open('build_capture.py').read()
import re
TN='three of the top-ten US names with no posts attached in 2159Z: "Iowa" (third; Minnesota beating No. 15 Iowa 13-10 on a field goal as time expired; the stream also carries Iowa election posts), "Cheesecake Factory" (seventh; Barack Obama in Ohio saying Trump has the White House looking like Saddam Hussein opened a Cheesecake Factory) and "Scott Frost" (ninth; UCF, coached by Scott Frost, against No. 2 BYU); "#UFC333" (first), "Volk" (second, attached in 2159Z), "Merab" (fourth) and "Petr Yan" (tenth) are UFC 333, attached in 2103Z and 2159Z, "Michigan" (sixth) had posts attached in 1807Z and "Marcel Reed" (eighth) in 2007Z, and "Dan Lanning" (fifth) was not read to keep to about 20 reads'
# old TN in sweep string
i=s.index('trend names "Volk", "Beck" and "Texas Tech" ("<name> lang:en is:retweet", newest first, 25 each; ')
j=s.index('); quote/repost words it/that + just (quoted)',i)
s=s[:i]+'trend names "Iowa", "Cheesecake Factory" and "Scott Frost" ("<name> lang:en is:retweet", newest first, 25 each; '+TN+s[j:]
R=[
("Build capture/2026/10/24/2159Z.json","Build capture/2026/10/24/2300Z.json"),
("work/2026-10-24T2159Z'","work/2026-10-24T2300Z'"),
("RUN_ID = '2026-10-24T2159Z'","RUN_ID = '2026-10-24T2300Z'"),
("STARTED = '2026-10-24T21:59:00Z'","STARTED = '2026-10-24T23:00:00Z'"),
("OBS_AT = '2026-10-24T22:00:00Z'","OBS_AT = '2026-10-24T23:01:00Z'"),
("READS_BEFORE = 550","READS_BEFORE = 530"),
("datetime(2026,10,24,22,1,tzinfo=timezone.utc).timestamp()  # 2159Z (","datetime(2026,10,24,23,2,tzinfo=timezone.utc).timestamp()  # 2300Z (2159Z used 22:01, "),
("'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',","'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',"),
("'repost_just': 'repost_just.txt',","'repost_this': 'repost_this.txt',"),
("'trend_volk': 'trend_volk.txt', 'trend_beck': 'trend_beck.txt', 'trend_texastech': 'trend_texastech.txt',","'trend_iowa': 'trend_iowa.txt', 'trend_cheesecake': 'trend_cheesecake.txt', 'trend_frost': 'trend_frost.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),","('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),"),
("('trend_volk','trend.Volk'),('trend_beck','trend.Beck'),('trend_texastech','trend.Texas Tech'),","('trend_iowa','trend.Iowa'),('trend_cheesecake','trend.Cheesecake Factory'),('trend_frost','trend.Scott Frost'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('2159Z.json') and '/24/' in _c: continue","if _c.endswith('2300Z.json') and '/24/' in _c: continue"),
("for g in ('news','money','science')}","for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-24T2103Z'","_last = '2026-10-24T2159Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet)',
 'common words "what", "the" and "this", each quoted so X does not reject a bare stopword: ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet)'),
("one hundred and twelfth run","one hundred and thirteenth run"),
("one hundred and tenth run","one hundred and eleventh run"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/2159Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/24/2300Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("# 5) request picks (2159Z: none read)","# 5) request picks (2300Z: none read)"),
("two screening reads by id (100 unread referenced posts, most pointed-at first, then the 32 second-hop and remaining posts in the second read)","two screening reads by id (100 unread referenced posts, most pointed-at first, then the 37 second-hop and remaining posts in the second read)"),
("quote/repost words it/that + just (quoted)","quote/repost words what/the + this (quoted)"),
("(this 22Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 568 long, so the 400 cap left out the 41 last six-hour posts and the 127 slowest-growing still-gaining posts, and no cited post)",
 "(this 23Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 565 long, so the 400 cap left out the 30 last six-hour posts and the 135 slowest-growing still-gaining posts, and no cited post)"),
("        if str(_x) in ('trend.Volk','trend.Beck'): return 'sports'  # 2159Z: UFC 333 (Volkanovski), Michigan quarterback Jason Beck in Indiana v Michigan\n",
 "        if str(_x) in ('trend.Volk','trend.Beck'): return 'sports'  # 2159Z: UFC 333 (Volkanovski), Michigan quarterback Jason Beck in Indiana v Michigan\n        if str(_x) in ('trend.Iowa','trend.Scott Frost'): return 'sports'  # 2300Z: Minnesota v Iowa, UCF v BYU\n        if str(_x)=='trend.Cheesecake Factory': return 'politics'  # 2300Z: Obama remark on Trump's White House\n"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Early-evening run (5:59 PM ET"):
    lines[k]="            f'Evening run (7:00 PM ET Oct 24 / 23:00 UTC Oct 24, the 23Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 2159Z ended at 530, so no read went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 22Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 23Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 565 ids, so the 400 cap left out the 30 last six-hour posts and the 135 slowest-growing still-gaining posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Volk\""):
    lines[k]="            f'trend names \"Iowa\", \"Cheesecake Factory\" and \"Scott Frost\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words it/that"):
    lines[k]="            f'quote/repost words what/the + this (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 2159Z, so culture/sports/online were next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 37 in the second read (the 15 left from the first list and the second-hop posts they led to; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again in the first read, as in 1105Z through 2159Z, and 2114016597249810808 returned Not Found in the first read, so neither was read in the second; 8 third-hop ids left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'No new request:"):
    lines[k]="            f'No new request: requests/open.json changed only its updated_at since 2159Z (watch.json gained two ids, 2114083967238275298 and 2114101812676411873, both read); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
