s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b,1)
rep("(18Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads;",
    "(19Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads;")
import re
i=s.index("sweeps.append(sweep('viral.global','discovery',None,")
j=s.index("24,'ok',None, viral_core))")
s=s[:i]+"""sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "AJ Brown", Steelers, "Cam Ward", "Daniel Jones", Panthers (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names, these had no posts attached in 1807Z or were new; Texans and Jags are the Texans v Jaguars game, read through two of its names in 1709Z, so they were not read again; AJ Brown, Steelers and Mike McCarthy are one event, the Pittsburgh Steelers game, read through two of its names); quote/repost words is/my/what + that; sensors culture/sports/online; desks politics/entertainment/sports/internet/science/ideas/life; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',
    """+s[j:]
i=s.index("sweeps.append(sweep('rising.global','discovery',None,")
j=s.index("6,'ok',None, rising_ids[:30]))")
s=s[:i]+"""sweeps.append(sweep('rising.global','discovery',None,
    '3 quote pages + 1 repost page, common words "is", "my", "what" and "that": (is lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (what lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each',
    """+s[j:]
i=s.index("        'reason': (")
j=s.index("        'grabber': {")
s=s[:i]+"""        'reason': (
            f'Daytime run at 3:04 PM ET (19:04 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 1807Z run ended at 474, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 19Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names "AJ Brown", Steelers, "Cam Ward", "Daniel Jones", Panthers (5 reads; each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; Texans and Jags, the Texans v Jaguars game, were read through two of its names in 1709Z and not read again; "Mike McCarthy" is the same Steelers game as "AJ Brown" and Steelers and was not read separately); quote/repost words is/my/what + that (3+1); '
            f'sensors culture/sports/online (3 reads); 7 desks due (hourly politics, entertainment, sports, internet; four-hour science, ideas, life, last read in 1501Z, due 19:01Z); two-hour world, justice, markets, ai, tech, medicine read in 1807Z and music, gaming, offbeat read in 1709Z (due 19:09Z) not due; four-hour defense, disaster, business read in 1709Z not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-01 in 1807Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '
            f'{EXTRA_NOTE} '
            f'Skipped sexual or graphic ids are in exclude_ids.json in the work folder.'
        ),
"""+s[j:]
open('build_capture.py','w').write(s); print('ok')
