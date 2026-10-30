s=open('build_capture.py').read()
L=s.split('\n')
def setline(prefix,new):
    idx=[i for i,l in enumerate(L) if l.startswith(prefix)]
    assert len(idx)==1,(prefix,idx); L[idx[0]]=new
LEFT='2110913438293647789, 2111005738306789584, 2111164055054426351, 2112273011504226337, 2112293785472225568, 2112988488379273237, 2113175048433369137, 2113455120692195588, 2113656547834487022, 2114085789139140865, 2114425377338634392'
TR=('trend names "#BladeRunnerLovesPPGsCowDung" and "#BeijingMustInvestigatePPGNow" ("<name> lang:en is:retweet", newest first, 25 each; top-ten US names with no posts attached in 1211Z; '
    '"#BladeRunnerLovesPPGsCowDung" (third, new) and "#BeijingMustInvestigatePPGNow" (fifth, new) are one fan campaign against Papergames (PPG, maker of Love and Deepspace) over a Blade Runner collaboration, and "#中国北京彻查上海叠纸" (fourth, new) is the same campaign in Chinese, its posts carrying all three tags, so it was not searched separately; '
    '"Good Tuesday" (first) and "Taco Tuesday" (second, new) are greetings; "Noah Wyle" (sixth), "#GMMTVNEXT" (ninth), "$SOFI" (seventh), "Flamengo" (tenth) had posts attached earlier today; "Eagles y Cowboys" (eighth, new) was not searched for the budget)')
setline("    'sources: references followed one hop",
 "    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors culture/sports/online (one read each); "+TR.replace("'","\\'")+"; quote/repost words and/my + it (quoted); hourly desks politics/entertainment/sports/internet; three screening reads by id: 100, then 13, then 23 unread referenced, reply-parent and media-source posts, most pointed-at first, including the second-hop posts; 9 third-hop posts left unread for the budget; story clusters not read for the budget; screened by id with global floor/pace',")
setline("            f'Morning run (8:11 AM ET",
 "            f'Morning run (8:59 AM ET Oct 27 / 12:59 UTC Oct 27, the 13Z slot; 12:00-05:00 UTC band, up to 42; kept to about 20 to pace the day): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 1211Z ended at 726, so no reads went elsewhere in between), parallel batches of up to 12, no 429 refusals. '")
setline("            f'Watch {len(watch_returned)} of {len(watch_ids)} (",
 "            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 13Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 533 ids, so the 400 cap left out the 95 last six-hour posts, the 27 slowest-growing still-gaining posts and 11 story-cited posts not on the pulse ("+LEFT+"; 2113455120692195588 was read in screening as a referenced post); no pulse-cited post was left out; 4 reads); trends US (1 read; worldwide not read for the budget); '")
setline("            f'trend names \"Sexiest", "            f'"+TR.replace("'","\\'")+" (2 reads); '")
setline("            f'quote/repost words this/is",
 "            f'quote/repost words and/my + it (3 reads, each word quoted; 1211Z used this/is + you); sensors culture/sports/online (3 reads; news/money/science read 1211Z, so culture/sports/online were next in rotation); '")
setline("            f'4 desk reads: hourly",
 "            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and seventy-fifth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and seventy-second run, both for the budget; '")
setline("            f'two screening reads by id:",
 "            f'three screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first (99 returned; 2114713627408335125 Authorization Error), then 13 more (all returned; 2108062331095908717 Not Found again, pointed at as a referenced post), then 23 second-hop posts (all returned); 9 third-hop posts were left unread for the budget (ids left out earlier as likely paid or sexual were not read again); in watch, 2111373522711060505 and 2113098076411892194 came back Not Found and 2111821497434046875 Authorization Error, as in 2026-10-26T1204Z through 2026-10-27T1211Z, and 2114708561196372415 (MadridXtra post of Mbappé naming his favourite meme, cited on the pulse and in watch.json) came back Not Found for the second run running; story clusters (search_news) not read for the budget. '")
setline("            f'Request r-2026-10-27-01 (filed",
 "            f'No new request: r-2026-10-27-01 was answered in 1211Z, r-2026-10-26-01 in 0306Z, r-2026-10-23-02 in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '")
setline("            f'Not read: culture/sports/online",
 "            f'Not read: news/money/science sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '")
open('build_capture.py','w').write('\n'.join(L)); print('ok')
