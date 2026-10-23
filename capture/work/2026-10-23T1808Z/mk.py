import re
s=open('build_capture.py').read()
TN='two of the top-ten US names with no posts attached in 1659Z: "Dan Sullivan" (new) and "Ethan Klein" (last read in 1459Z); "Devils" and "Winnipeg" are one event with "Hellebuyck", "Mercer" and "Command" (the Jets-Devils Hellebuyck trade, read in 1602Z and 1659Z) and "Hila" is one h3h3 event with "Ethan Klein", so those were skipped; the "Dan Sullivan" stream is about the Justice Department suit to block certification of the Alaska Senate race if Sen. Dan Sullivan loses, citing a second candidate with the same name on the ballot'
R=[
("Build capture/2026/10/23/1659Z.json","Build capture/2026/10/23/1808Z.json"),
("work/2026-10-23T1659Z'","work/2026-10-23T1808Z'"),
("RUN_ID = '2026-10-23T1659Z'","RUN_ID = '2026-10-23T1808Z'"),
("STARTED = '2026-10-23T16:59:00Z'","STARTED = '2026-10-23T18:08:00Z'"),
("OBS_AT = '2026-10-23T16:59:00Z'","OBS_AT = '2026-10-23T18:08:00Z'"),
("READS_BEFORE = 658","READS_BEFORE = 636"),
("datetime(2026,10,23,17,1,tzinfo=timezone.utc).timestamp()  # 1659Z (","datetime(2026,10,23,18,10,tzinfo=timezone.utc).timestamp()  # 1808Z (1659Z used 17:01, "),
("'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',","'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',"),
("'repost_and': 'repost_and.txt',\n    'req_talarico': 'req_r-2026-10-23-01.txt', 'req_oleshky': 'req_r-2026-10-23-02.txt',","'repost_just': 'repost_just.txt',\n    'req_oleshky': 'req_r-2026-10-23-02.txt',"),
("'trend_mercer': 'trend_mercer.txt', 'trend_lassie': 'trend_lassie.txt', 'trend_jarmo': 'trend_jarmo.txt',","'trend_dansullivan': 'trend_dansullivan.txt', 'trend_ethanklein': 'trend_ethanklein.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("'screen0': 'screen0.txt', 'screen1': 'screen1.txt',","'screen0': 'screen0.txt',"),
("('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_it','quote'),('quote_that','quote'),('repost_just','repost'),"),
("('trend_mercer','trend.Mercer'),('trend_lassie','trend.Lassie'),('trend_jarmo','trend.Jarmo'),","('trend_dansullivan','trend.Dan Sullivan'),('trend_ethanklein','trend.Ethan Klein'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1659Z.json') and '/23/' in _c: continue","if _c.endswith('1808Z.json') and '/23/' in _c: continue"),
("SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}","SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}"),
("SENSOR_READ = {'news','money','science'}","SENSOR_READ = {'culture','sports','online'}"),
("_last = '2026-10-23T1602Z'","_last = '2026-10-23T1659Z'"),
("rotation: news/money/science read this run","rotation: culture/sports/online read this run"),
('\'2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "it", "that" and "just", each quoted so X does not reject a bare stopword: ("it" lang:en is:quote -is:retweet), ("that" lang:en is:quote -is:retweet), ("just" lang:en is:retweet), newest first, 25 each\''),
("eighty-fourth run","eighty-fifth run"),
("eighty-second run","eighty-third run"),
("(this 17Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 514 long, so the 400 cap left out 114, the slowest-growing","(this 18Z run is not a fourth hour; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour and still-gaining tiers, the list was 511 long, so the 400 cap left out 111, the slowest-growing"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1659Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/23/1808Z.json'"),
("sensors news/money/science (one read each)","sensors culture/sports/online (one read each)"),
("        if str(_x) in ('trend.Mercer','trend.Lassie','trend.Jarmo'): return 'sports'  # 1659Z","        if str(_x) in ('trend.Mercer','trend.Lassie','trend.Jarmo'): return 'sports'  # 1659Z\n        if str(_x)=='trend.Dan Sullivan': return 'politics'  # 1808Z: DOJ suit over the Alaska Senate race"),
("ANSWERED_EARLIER = {","ANSWERED_EARLIER = {'r-2026-10-23-01':'2026-10-23T1659Z',"),
("# 5) request picks (1659Z: r-2026-10-23-01 and r-2026-10-23-02)","# 5) request picks (1808Z: r-2026-10-23-02 re-read once after the editor rewrote the ask)"),
]
for a,b in R:
  if s.count(a)==0: print('MISSING',a[:100])
  s=s.replace(a,b)
# viral method trend text
i=s.find('trend names "Mercer", "Lassie" and "Jarmo" ("<name> lang:en is:retweet", newest first, 25 each;')
j=s.find(')',s.find('skipped',i))
seg=s[i:j]
print('VIRAL SEG',seg[-200:])
s=s[:i]+'trend names "Dan Sullivan" and "Ethan Klein" ("<name> lang:en is:retweet", newest first, 25 each; '+TN.replace("'","\\'")+s[j:]
PICKS=['2113666873434988939','2113674177349644661','2113668905088774618','2113637651496456648','2113668504406646925','2113669073972129882']
a=s.find("REQ_PICKS = {"); b=s.find("ADDED_STORY = ",a)
s=s[:a]+"REQ_PICKS = {'r-2026-10-23-02': "+repr(PICKS)+"}\nREQ_FILES = {'r-2026-10-23-02': 'req_oleshky'}\nREQ_ONLY = {t['id'] for t in (raw['req_oleshky'].get('data') or [])} - set(REQ_PICKS['r-2026-10-23-02'])\n"+s[b:]
REQQ="    'r-2026-10-23-02': 'search_posts_all Oleshky (ceasefire OR truce OR humanitarian) (Zelensky OR Ukrainian OR Ukraine OR \"General Staff\" OR \"Southern Defense Forces\" OR Pletenchuk OR Yermak OR Sybiha OR \"27 October\" OR \"29 October\" OR \"October 27\" OR \"October 29\") -is:retweet -is:reply, start_time 2026-10-23T12:00:00Z, relevancy, 25 results (1808Z re-read after the ask was rewritten; 1659Z used a narrower query from 2026-10-22T12:00Z); posts showing or naming residents not kept',\n"
a=s.find("    'r-2026-10-23-02': 'search_posts_all Oleshky"); b=s.find("\n",a)+1
s=s[:a]+REQQ+s[b:]
NOTE=("Re-read once at 1808Z because the ask was rewritten to look for a Ukrainian statement on the start date: one search from 2026-10-23T12:00Z (relevancy, 25 results). "
"Again no post from Zelensky, the Ukrainian presidential office, the General Staff of Ukraine or the Southern Defense Forces was returned, so no Ukrainian statement on the start date was found. "
"Kept six posts not kept in 1659Z: the four most liked new ones, wartranslated (2113666873434988939, Russian General Staff \\\"quiet regime\\\" on the Kherson front from 4am Moscow time on 27 October), MilitarySummary (2113674177349644661, quotes Gerasimov), KyivPost (2113668905088774618, reports the Russian announcement of a localized \\\"silence regime\\\" from 27 October) and ln24_intl (2113637651496456648, says Melania Trump helped secure the ceasefire); vick55top (2113668504406646925, same Gerasimov statement); and aurabora_invest (2113669073972129882), whose text is a headline credited to CNN saying the start date is in dispute, Russia saying 27 October and the First Lady office 29 October. "
"Posts still giving 29 October (White House) in this result include IndianExpress, Belsat_Eng and ARNNewsCentre. No post showing or naming residents was kept.")
a=s.find("ANSWERS = [{"); b=s.find("}]\ncapture = {",a)
s=s[:a]+"ANSWERS = [{\n    'request_id': 'r-2026-10-23-02',\n    'status': 'ok',\n    'post_ids': REQ_PICKS['r-2026-10-23-02'],\n    'note': \""+NOTE+"\"\n"+s[b:]
lines=s.split('\n'); hit=0
for k,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("f'Midday run (12:59 PM ET"):
    lines[k]="            f'Afternoon run (2:08 PM ET Oct 23 / 18:08 UTC Oct 23, the 18Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1659Z ended at 636, so no reads went elsewhere in between), parallel batches of up to 13, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 17Z"):
    lines[k]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 18Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 511 ids, so the 400 cap left out 111 slowest-growing still-gaining posts in order and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '"; hit+=1
  elif st.startswith("f'trend names \"Mercer"):
    lines[k]="            f'trend names \"Dan Sullivan\" and \"Ethan Klein\" (2 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN.replace("'","\\'")+"); '"; hit+=1
  elif st.startswith("f'quote/repost words is/you"):
    lines[k]="            f'quote/repost words it/that + just (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1659Z, next in rotation); '"; hit+=1
  elif st.startswith("f'two screening reads by id: 100"):
    lines[k]="            f'one screening read by id: the 100 unread referenced, reply-parent and media-source posts, most pointed-at first (ids left out earlier as likely paid or sexual were not read again); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Two new requests read once each"):
    lines[k]="            f'Request r-2026-10-23-02 read once more (search_posts_all, relevancy, 25 results) because the editor rewrote the ask to look for a Ukrainian statement on the start date: none from the Ukrainian president office, General Staff or southern command was returned; six posts not kept before are kept, including a headline credited to CNN on the 27 versus 29 October dispute. r-2026-10-23-01 was answered in 1659Z and not read again; earlier requests were answered in earlier captures. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[k]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
