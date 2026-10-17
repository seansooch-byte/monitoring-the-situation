import re
s=open('build_capture.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)
rep("not read this run (rotation: news/money/science this hour)","not read this run (rotation: culture/sports/online this hour)")
TN='trend names "Jeremiah Smith", Sayin, "Arch Manning", Sark, "Jay Timmons" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; the five top-ten US names with no posts attached in 1807Z; Jeremiah Smith, Sayin and Jay Timmons belong to the Ohio State v Indiana college football game, one event with Julian Sayin, Ohio State, Ryan Day and Indiana; Arch Manning and Sark belong to the Texas v Florida game, one event with Gators and #HookEm)'
lines=s.split('\n')
for i,l in enumerate(lines):
    if l.startswith("    'sources: references followed two hops"):
        lines[i]="    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; "+TN+"; quote/repost words is/you/that + it; sensors culture/sports/online; desks politics/entertainment/music/gaming/sports/internet/offbeat; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',"
    if l.startswith("    '3 quote pages + 1 repost page"):
        lines[i]="    '3 quote pages + 1 repost page, common words \"is\", \"you\", \"that\" and \"it\": (is lang:en is:quote -is:retweet), (you lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (it lang:en is:retweet), newest first, 25 each',"
    if "f'Daytime run at 2:07 PM ET" in l:
        lines[i]="            f'Daytime run at 3:06 PM ET (19:06 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1807Z run ended at 486, so nothing else read in between). '"
    if l.startswith("            f'Watch {len(watch_returned)}"):
        lines[i]=l.replace('18Z is not','19Z is not')
    if l.startswith("            f'trend names \"Ryan Day\""):
        lines[i]="            f'"+TN.replace("'","\\'")+" (5 reads); quote/repost words is/you/that + it (3+1); '"
    if l.startswith("            f'sensors news/money/science; 13 desk reads"):
        lines[i]="            f'sensors culture/sports/online; 7 desk reads: the hourly desks politics, entertainment, sports, internet and the two-hour desks music, gaming, offbeat (last ok 1706Z, due 19:06Z); world, justice, markets, ai, tech, medicine were swept in 1807Z and are next due at 20:07Z; '"
s='\n'.join(lines)
open('build_capture.py','w').write(s); print('ok')
