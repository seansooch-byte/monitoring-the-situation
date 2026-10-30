s=open('build_capture.py').read()
SH='#中国上海停止纵容姚润昊'
TN=('three of the eight top-ten US names with no posts attached in 1107Z: "#PapergamesTramplesHumanRights" and "'+SH+'" (new; one event, the fan campaign against Papergames (Infold) and the Love and Deepspace community over harassment, tagging the Blade Runner rights holders; the same posts carry both tags) and "GMMTV ACCOUNTABILITY" (the Myanmar fan-club campaign over Burmese dress in Scarlet Heart Thailand, attached in 1007Z as #RespectMyanmarCulture); "Good Thursday", "Happy Friday Eve" and "#ThankfulThursday" (greetings), "Yaxel" (the Warriors at Lakers game attached in 1107Z as Luka) and "#CreditOurHeritage" (the same campaign as GMMTV ACCOUNTABILITY) left out')
R=[
("Build capture/2026/10/22/1107Z.json","Build capture/2026/10/22/1201Z.json"),
("work/2026-10-22T1107Z'","work/2026-10-22T1201Z'"),
("RUN_ID = '2026-10-22T1107Z'","RUN_ID = '2026-10-22T1201Z'"),
("STARTED = '2026-10-22T11:07:00Z'","STARTED = '2026-10-22T12:01:00Z'"),
("OBS_AT = '2026-10-22T11:07:00Z'","OBS_AT = '2026-10-22T12:01:00Z'"),
("READS_BEFORE = 779","READS_BEFORE = 749"),
("datetime(2026,10,22,11,10,tzinfo=timezone.utc).timestamp()  # 1107Z (","datetime(2026,10,22,12,4,tzinfo=timezone.utc).timestamp()  # 1201Z (1107Z used 11:10, "),
("'quote_this': 'quote_this.txt', 'quote_you': 'quote_you.txt',","'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',"),
("'repost_and': 'repost_and.txt',","'repost_that': 'repost_that.txt',"),
("'trend_eala': 'trend_eala.txt', 'trend_kidnapped': 'trend_kidnapped.txt', 'trend_luka': 'trend_luka.txt',","'trend_papergames': 'trend_papergames.txt', 'trend_shanghai': 'trend_shanghai.txt', 'trend_gmmtv': 'trend_gmmtv.txt',"),
("'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',","'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"),
("('quote_this','quote'),('quote_you','quote'),('repost_and','repost'),","('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),"),
("('trend_eala','trend.Eala'),('trend_kidnapped','trend.Kidnapped'),('trend_luka','trend.Luka'),","('trend_papergames','trend.#PapergamesTramplesHumanRights'),('trend_shanghai','trend."+SH+"'),('trend_gmmtv','trend.GMMTV ACCOUNTABILITY'),"),
("('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),","('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"),
("if _c.endswith('1107Z.json') and '/22/' in _c: continue","if _c.endswith('1201Z.json') and '/22/' in _c: continue"),
("for g in ('news','money','science')}\nSENSOR_READ = {'news','money','science'}","for g in ('culture','sports','online')}\nSENSOR_READ = {'culture','sports','online'}"),
("rotation: news/money/science read this run;","rotation: culture/sports/online read this run;"),
("_last = '2026-10-22T1007Z'","_last = '2026-10-22T1107Z'"),
("(this 11Z-slot run is not a fourth hour, so the rest of the last 24 hours was not added; with every pulse- and story-cited post placed right after the watch.json ids the list was 446 long, so the 400 cap left out the 46 slowest-growing still-gaining posts and no cited post)",
 "(this 12Z-slot run is a fourth hour, so the rest of the last 24 hours was added, slowest growing last; with every pulse- and story-cited post placed right after the watch.json ids the list was 519 long, so the 400 cap left out the 119 slowest-growing still-gaining and fourth-hour posts and no cited post)"),
("out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1107Z.json'","out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/22/1201Z.json'"),
('\'2 quote pages + 1 repost page (budget), common words "this", "you" and "and", each quoted so X does not reject a bare stopword: ("this" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each\'',
 '\'2 quote pages + 1 repost page (budget), common words "my", "it" and "that", each quoted so X does not reject a bare stopword: ("my" lang:en is:quote -is:retweet), ("it" lang:en is:quote -is:retweet), ("that" lang:en is:retweet), newest first, 25 each\''),
("        if str(_x) in ('trend.Eala','trend.Luka'): return 'sports'  # 1107Z",
 "        if str(_x) in ('trend.#PapergamesTramplesHumanRights','trend."+SH+"'): return 'gaming'  # 1201Z: fan campaign against Papergames (Love and Deepspace) over harassment\n        if str(_x) in ('trend.Eala','trend.Luka'): return 'sports'  # 1107Z"),
("but cut for the fifty-second run (the 06:00-11:00 UTC band allows up to 20 reads; four-hour desks are cut first)","but cut for the fifty-third run (kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42; four-hour desks are cut first)"),
("cut for the fifty-fourth run (the 06:00-11:00 UTC band allows up to 20 reads)'","cut for the fifty-fifth run (kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42)'"),
("'cut for the read budget (the 06:00-11:00 UTC band allows up to 20 reads)'","'cut for the read budget (kept to about 20 reads per the scheduling instruction although the 12:00-05:00 UTC band allows up to 42)'"),
("(rotation: culture/sports/online read this run; the 06:00-11:00 UTC band allows up to 20 reads)","(rotation: culture/sports/online read this run; kept to about 20 reads per the scheduling instruction)"),
("(the 06:00-11:00 UTC band allows up to 20 reads); last read in","(kept to about 20 reads per the scheduling instruction); last read in"),
]
for a,b in R:
  n=s.count(a)
  if n==0: print('MISSING',a[:90])
  s=s.replace(a,b)
lines=s.split('\n'); hit=0
for i,l in enumerate(lines):
  st=l.lstrip()
  if st.startswith("'sources: references followed two hops"):
    lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); trend names \"#PapergamesTramplesHumanRights\", \""+SH+"\" and \"GMMTV ACCOUNTABILITY\" (\"<name> lang:en is:retweet\", newest first, 25 each, names quoted; "+TN+"); quote/repost words my/it + that (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced first-hop, then 23 more, first-hop and second-hop); story clusters not read for the budget; screened by id with global floor/pace',"; hit+=1
  elif st.startswith("f'Morning run (7:07 AM ET"):
    lines[i]="            f'Morning run (8:01 AM ET / 12:01 UTC Oct 22, the 12Z slot; 12:00-05:00 UTC band, up to 42, kept to about 20 per the scheduling instruction): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1107Z ended at 759, so 10 reads went elsewhere in between), parallel batches of up to 9, no 429 refusals. '"; hit+=1
  elif st.startswith("f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 11Z"):
    lines[i]="            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 12Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers, then the rest of the last 24 hours slowest growing last; 519 ids, so the 400 cap left out the 119 slowest-growing still-gaining and fourth-hour posts and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget, last read 0001Z); '"; hit+=1
  elif st.startswith("f'trend names \"Eala\""):
    lines[i]="            f'trend names \"#PapergamesTramplesHumanRights\", \""+SH+"\" and \"GMMTV ACCOUNTABILITY\" (3 reads; \"<name> lang:en is:retweet\", newest first, 25; "+TN+"); '"; hit+=1
  elif st.startswith("f'quote/repost words this/you"):
    lines[i]="            f'quote/repost words my/it + that (3 reads, each word quoted); sensors culture/sports/online (3 reads; news/money/science last read 1107Z, next in rotation); '"; hit+=1
  elif st.startswith("f'4 desk reads: hourly"):
    lines[i]="            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the fifty-fifth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the fifty-third run, both for the budget; '"; hit+=1
  elif st.startswith("f'two screening reads by id: 87 unread"):
    lines[i]="            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 23 more (the 3 first-hop that did not fit and 20 second-hop first seen in that read; 2108062331095908717 came back Not Found as an expansion and was not read again; 9 third-hop left unread); story clusters (search_news) not read for the budget. '"; hit+=1
  elif st.startswith("f'Not read: culture/sports/online sensors"):
    lines[i]="            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '"; hit+=1
print('line hits',hit)
open('build_capture.py','w').write('\n'.join(lines))
