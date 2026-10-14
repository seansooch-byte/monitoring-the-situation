# Notes from the grabber

Append one dated line when something outside `capture/` looks wrong, or when the contract cannot
express something you saw. The editor reads this file on every pass.

- 2026-10-09: `npm test` fails on Node 20.19 ("Could not find .../tests/*.test.mjs") because Node 20's `--test` does not expand globs; package.json says node >=18. `node --test tests/check-capture.test.mjs` and Node 22 both pass 34 of 34.
- 2026-10-09: X gives no community notes, no trend post counts, no trend-to-story link, no engagement sort and no min likes operator; deleted and never-existing ids return the same Not Found Error. Details in capture/CAPABILITIES.md.
- 2026-10-09: KICKOFF step 4 says start the hourly schedule; the grabber was told by Sean's main agent not to create it, so the schedule is not running yet. The steps are in capture/RUNBOOK.md.
- 2026-10-09: side by side, run 2026-10-09T0615Z (about 2 AM ET, so all numbers are night numbers). Run total 25 reads (951 to 926 left today). "Candidates" for streams is distinct originals after spam and age screening; each stream call returned 25 results. Views and ages read 06:16 to 06:17Z.
- 2026-10-09: old, story clusters (search_news viral, politics, entertainment, sports, internet): 5 search reads plus about 2 of the 3 by-id reads; candidates 193; kept 28; largest 5,331,401; median 92,739; median age 14.7h. Politics clusters kept 0 of 30.
- 2026-10-09: new, global repost stream: 1 read; candidates 25; kept 6; largest 884,660; median 81,339; median age 10.7h.
- 2026-10-09: new, global quote stream: 1 read; candidates 23; kept 6; largest 462,781; median 278,108; median age 11.5h.
- 2026-10-09: new, desk repost streams (politics, entertainment, sports, internet): 4 reads; candidates 44; kept 44; largest 1,643,594; politics median 62,707, entertainment 78,513, sports 66,094, internet 40,449; median ages 9.3h to 18.4h.
- 2026-10-09: new, trend names (Cowboys, Bucs repost streams): 2 reads; candidates 21 (one excluded as sexual); kept 20; largest 2,026,595; Cowboys median 106,708, Bucs median 71,941; median age 3.0h and 2.9h.
- 2026-10-09: new, sensors (30 account probe): 1 read; candidates 2; kept 2; largest 1,701,269; median 1,200,158; median age 13.9h.
- 2026-10-09: new, references (media_source and the pinned quote): 0 extra search reads, part of the by-id reads; candidates 11; kept 11 as origins; largest 39,941,861; median 994,172; median age 35.3h (origins are often older than 24h).
- 2026-10-09: new, volume: 1 read; 1 desk (politics), 167 full hours. Old method has no volume.
- 2026-10-09: verdict for this night run: no overlap between old and new kept posts (0 shared ids). New finds fresher posts (median age 9.1h vs 14.7h) at about the same median views (78,268 vs 92,739); the old method still found the biggest fresh post (5.3M AI acrobat clip via the viral story). Run both until a daytime comparison exists.
- 2026-10-09: x_stories is missing from 0615Z: the search_news outputs were read inline and not saved, and story names must be exact, so I left them out rather than retype them. Next run saves every story output to a file first.
- 2026-10-09: excluded 2108381183340151072 (Cowboys trend, 574k views) because its image is sexual.
- 2026-10-09: run 2026-10-09T0629Z: 58 reads (926 to 868 left today): 19 for the desk backfill, 39 for the run (cap 45). All 20 desks now have 167 full hours of volume (2026-10-02T07:00Z to 2026-10-09T05:00Z); politics is the series from run 0615Z, the other 19 were read this run and each matched meta.total_tweet_count.
- 2026-10-09: pace floor, run 0629Z: 64 kept posts were under 3 hours old when read, 49 of them kept only on pace (under 100k views and 2k likes). Fastest: FabrizioRomano 2108443593064972573, 262,154 views at 12 minutes old, about 1.34 million an hour. Many of the 49 are wire headlines read a few minutes after posting (Reuters at 7 minutes); a pace taken from a post under 15 minutes old is noisy, and the rule may need a minimum age.
- 2026-10-09: the global quote stream this run returned 69 reposts in 75 results because `is:quote` also matches reposts of quote posts; the runbook now adds `-is:retweet`. The exact query strings of those three reads were not saved with the outputs, so their sweep says so.
- 2026-10-09: most pointed-at posts this run (distinct posts referencing them): 2108238077294432434 (SecKennedy, NIH clinic) 27; 2107803696058822742 (p_rabtsevich, planet) 9; 2093450039649784060 (betr, from August, captured as old_content) 6; 2108373440054825211 (fliff) 6; 2108369630150660244 (luvis1and) 5.
- 2026-10-09: left out this run: three posts with slurs (2108396838655062441, 2108344047442243962, 2108425752978837618); a drone video X marks possibly_sensitive that looks like a strike on a person (2108181323730878707); three posts whose author X did not return.
- 2026-10-09: x_stories is empty again in 0629Z: search_news came back inline twice and cannot be saved as a file.

- 2026-10-09: run 2026-10-09T0702Z overnight thrift (3 AM ET): 15 reads (868 to 853 left today). Watch 200/400; trends US+WW; quote+repost word you; culture sensors; hourly desks politics/entertainment/sports/internet; Dak Prescott trend stream; no volume/stories/context/media descriptions. Excluded sexual or minor-related posts including 2108366539439411593 and 2108378335512293747. Notice r-2026-10-09-11 acknowledged.

- 2026-10-09: run 2026-10-09T0804Z lean overnight (4 AM ET): about 23 X reads (853 to 830 left today). Watch 400; trends US+WW; quote/repost word "and" (bare and rejected, quoted works); sensors sports/online/news; hourly desks; trend streams #PPHALLOWEENPARTY/New Yorker/CeeDee. Excluded giveaway 2108437202543800337 and under-15-minute FabrizioRomano 2108468759350358134. No volume/stories/context/media descriptions.

- 2026-10-09: run 2026-10-09T0901Z lean overnight (5 AM ET): about 24 X reads (830 to 806 left today). Watch ~400; trends US+WW; quote/repost word "my" (2 quote pages + 1 repost); sensors science/culture (money inline unsaved); hourly desks politics/sports/internet (entertainment inline unsaved); trend stream #AvatarSevenHavens; screen 35 by id. No volume/stories/context/media descriptions. Excluded NSFW/slur/giveaway pattern ids.

- 2026-10-09: run 2026-10-09T1102Z lean overnight (7 AM ET / 11 UTC): 13 X reads (791 to 778 left today). Watch 121; trends US+WW; quote/repost word "that"; hourly desks; trend stream Cowboys; screen 95 by id. No volume/stories/sensors/context/media descriptions. SKIP_ALL still set on pipeline so editor will not run after this push.

- 2026-10-09: run 2026-10-09T1212Z daytime (8 AM ET / 12 UTC): 22 X reads (770 to 748 left today). Watch 400; trends US+WW; quote/repost word "just"; sensors news/money/science; hourly desks; trend streams Good Friday + Navi Pillay/Nobel; screen 100 by id. No volume/stories/context/media descriptions. Excluded sexual Good Friday id 2108511541351837778. Non-hourly desks skipped. SKIP_ALL still set on pipeline so editor will not run after this push.

- 2026-10-09: run 2026-10-09T1318Z daytime (9 AM ET / 13 UTC): 19 X reads counted (748 to 729 left today; 3 shared-access 429s burned reads with no data). Watch 171; trends US+WW; quote/repost word "what" (1+1); sensors culture/sports/online; hourly desks; trend streams Category 3 + Hurricane Isaias; screen 100 by id. No volume/stories/context/media descriptions. Disaster desk swept as big hour (Isaias Cat 3). SKIP_ALL still set on pipeline so editor will not run after this push.

- 2026-10-09: run 2026-10-09T1432Z daytime (10 AM ET / 14 UTC): 17 X reads (729 to 712 left today; 1 invalid-id probe burned a read). Watch 200; trends US+WW; quote/repost word "the" (1+1); sensors news/money/science; hourly desks; trend streams New Yorker + Charlie Kirk; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP_ALL still set on pipeline so editor will not run after this push.

- 2026-10-09: run 2026-10-09T1528Z daytime (11 AM ET / 15 UTC): 20 X reads (712 to 692 left today; includes 1 wrong watch batch and 3 re-fetches of inline results). Watch 227; trends US+WW; quote/repost word "this" (1+1); sensors culture/sports/online; hourly desks; trend stream Mike Ditka; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP_ALL still set on pipeline so editor will not run after this push.

- 2026-10-09: run 2026-10-09T1619Z daytime (12 PM ET / 16 UTC): 17 X reads (692 to 675 left today; includes 1 re-fetch of inline watch batch 2). Watch 220; trends US+WW; quote/repost word "is" (1+1); sensors news/money/science; hourly desks; trend stream Da Bears (Ditka); screen 59 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP_ALL still set on pipeline so editor will not run after this push.

- 2026-10-09: run 2026-10-09T1721Z daytime (1:21 PM ET / 17 UTC): 16 X reads (675 to 659 left today). Watch 226; trends US+WW; quote/repost word "you" (1+1); sensors culture/sports/online; hourly desks; trend stream Charlie Kirk; screen 44 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.
- 2026-10-09: run 2026-10-09T1808Z daytime (2:08 PM ET / 18 UTC): 17 X reads (659 to 642 left today). Watch 293; trends US+WW; quote/repost word "and" (2+1); sensors news/money/science; hourly desks; trend stream McBride; screen 35 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.

- 2026-10-09: run 2026-10-09T1906Z daytime (3:06 PM ET / 19 UTC): 18 X reads (642 to 624 left today). Watch 372; trends US+WW; quote/repost word "my" (2+1); sensors culture/sports/online; hourly desks; trend stream Panama; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.

- 2026-10-09: run 2026-10-09T2010Z daytime (4:10 PM ET / 20 UTC): 18 X reads (624 to 606 left today). Watch 383; trends US+WW; quote/repost word "it" (2+1); sensors news/money/science; hourly desks; trend stream Katie Zacharia; screen 99 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.
- 2026-10-09: run 2026-10-09T2110Z daytime (5:10 PM ET / 21 UTC): 18 X reads (606 to 588 left today). Watch 399; trends US+WW; quote/repost word "that" (2+1); sensors culture/sports/online; hourly desks; trend stream Press Secretary; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.

- 2026-10-09: run 2026-10-09T2205Z daytime (6:05 PM ET / 22 UTC): 19 X reads (588 to 569 left today). Watch 372; trends US+WW; quote/repost word "just" (2+1); sensors news/money/science; hourly desks; trend stream Nancy; screen 100 by id + Nancy by-id. No volume/stories/context/media descriptions. Non-hourly desks skipped. Skipped sexual/graphic TMZ Jane Doe posts. SKIP/SKIP_ALL absent on pipeline.

- 2026-10-09: run 2026-10-09T2303Z daytime (7:03 PM ET / 23 UTC): 17 X reads (569 to 552 left today). Watch 236; trends US+WW; quote/repost word "what" (2+1); sensors culture/sports/online; hourly desks; trend stream Putin; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.

- 2026-10-10: run 2026-10-10T0000Z evening (8:00 PM ET / 00 UTC): 17 X reads (1000 to 983 left today). Watch 273; trends US+WW; quote/repost word "the" (2+1); sensors news/money/science; hourly desks; trend stream Louisville; screen 36 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline. Finalized 2026-10-09 daily scoreboard.

## Daily scoreboard

One line per UTC day, appended in the last run before 00:00 UTC. Counted over all captures of the
day with duplicates removed; views are at each post's last reading; age is at first capture.
Sources are the sweep families each post was listed under (a post can count for several).

Format: `date | reads used | posts kept | >1M | >5M | >10M | largest | median | median age (h) | per source: largest / median`

- 2026-10-10 (partial, through 0135Z) | 71 | 256 | 54 | 11 | 2 | 54254931 | 257313 | 12.13 | references: 54254931 / 235543; sensors: 8887990 / 125100; trend names: 434872 / 62093; quote and repost streams: 54254931 / 497267; story clusters: 1038552 / 89131; desk streams: 1015039 / 162660; context and requests: n/a
- 2026-10-09 | 448 | 1078 | 177 | 26 | 13 | 52440874 | 255895 | 10.37 | references: n/a; sensors: 9903955 / 340744; trend names: 752096 / 752096; quote and repost streams: 52440874 / 377540; story clusters: n/a; desk streams: 40895900 / 254587; context and requests: 39941900 / 758
- 2026-10-09: run 2026-10-09T1011Z lean overnight (6 AM ET): 15 X reads (806 to 791 left today). Watch 400; trends US+WW; quote/repost word "it"; hourly desks; trend stream Navi Pillay (Nobel Peace Prize). No volume/stories/sensors/context/media descriptions. Excluded NSFW/sexual/minor/piracy ids including 2108124415762592123 and 2108366539439411593.

## Request from Sean (2026-10-09, 1:48 PM ET), for the editor

Sean asked for two changes. Both live in files the grabber may not edit (`contract/`, `pulse/`), so they are
passed here for the editor to decide and make:

1. **Drop the crypto desk.** `crypto` is one of the twenty in `contract/desks.json` (also named in
   `contract/GRABBER.md` under "Money"). Until the contract changes, the grabber keeps sweeping it
   because the checker expects twenty desks. Once the contract says nineteen, the grabber stops
   gathering and counting it and removes its standing query from `capture/CAPABILITIES.md`.
2. **Keep one account from crowding the feed.** Sean notes Elon Musk's posts have the most views and
   fill the pulse. He wants a limit per author on the pulse (the editor's choice of number; the
   X ranking guide in `capture/RANKING.md` describes X's own author penalty: x1, x0.625, x0.44, floor
   x0.25 for each extra post by the same author). The grabber's capture still records every post
   X returned, with no cap, because a capture holds what X returned and no judgement of it. If the
   editor wants a gather-side cap (for example at most N kept posts per author per capture), say so
   in `contract/GRABBER.md` and the grabber will follow it.

- 2026-10-10: run 2026-10-10T0101Z evening (9:01 PM ET / 01 UTC): 17 X reads (983 to 966 left today). Watch 239; trends US+WW; quote/repost word "this" (2+1); sensors culture/sports/online; hourly desks; trend stream #SmackDown; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. Skipped sexual/graphic ids. SKIP/SKIP_ALL absent on pipeline.

## Evening side-by-side 2026-10-10T0135Z

- 2026-10-10: evening side-by-side, run 2026-10-10T0135Z (about 9:35 PM ET / 01 UTC). Run total 38 X reads (967 to 929 left today). "Candidates" = distinct originals under 24h after spam screening (with a saved record). Views/ages at ~01:41Z. Watch + trends first; sensors news/sports/culture; trend streams for Putin/Louisville/Angel Reese/Igor/Norvell (prior capture empty); quote `the`+`this` + repost `the`; story clusters viral+four hourly desks; desk repost streams for those desks. Skipped volume/context/media descriptions. First 5 `search_news` calls lacked `cluster_posts_results` (wasted +5 reads) and were redone; referenced origins often lack authors until a by-id pass (trend tops +1, clearing repost origins +1).
- Table (a post found by several sources counts for each):

| Source | Reads | Candidates | Kept | Largest | Median | Median age (h) |
|---|---|---|---|---|---|---|
| references | 0 | 329 | 120 | 54,254,931 | 235,543 | 8.66 |
| sensors | 3 | 70 | 22 | 8,887,990 | 125,100 | 1.35 |
| trend names | 6 | 97 | 20 | 434,872 | 62,093 | 1.55 |
| quote stream | 2 | 32 | 3 | 54,254,931 | 905,811 | 7.55 |
| repost stream | 2 | 19 | 6 | 412,545 | 88,723 | 7.42 |
| story clusters | 5 | 50 | 12 | 1,038,552 | 89,131 | 20.75 |
| desk repost streams | 4 | 86 | 11 | 1,015,039 | 162,660 | 5.48 |

- Comparison vs night run 2026-10-09T0615Z: overlap of kept ids = 2 (2024898302035067174, 2108376131108041026). Biggest fresh under-24h post this evening: 54,254,931 views (elonmusk 2108604227643719745, age 8.63h) via references, quote stream. Night's biggest fresh was 5.3M via story clusters (old method). GRABBER.md ranking (refs → sensors → trends → quote → repost → stories → desks) only partly holds at this busy hour: quote stream has the highest median; references still find the biggest and a strong median; sensors still strong; trend names still freshest (median age 1.55h) but lower median views; story clusters weaker on under-24h kept (median age 20.75h, only 12 kept after screening budget); desk streams mid; repost stream recovered after author by-id. Run both methods until more evening samples exist.
- 2026-10-10: run 2026-10-10T0135Z evening side-by-side (9:35 PM ET / 01 UTC): 38 X reads (967 to 929 left today). Watch 246; trends US+WW; sensors news/sports/culture; trend streams Putin/Louisville/Angel Reese/Igor/Norvell; quote the+this + repost the; story clusters (5+5 reads); desk streams four hourly; screen 323 + trend/repost author by-id. No volume/context/media descriptions. Skipped sexual/graphic ids including 2108586677908435200 (Charlie Kirk murder video) and prior EXCLUDE list ids. Checker PASS (190 posts, 415 observations).
- Pace floor this run: 23 kept posts under 3 hours old that cleared on pace (<100k views and <2k likes). Fastest: DiscussingFilm 2108722243249258618, 66,415 views at 0.812h, about 81,741 views/hour.
- 2026-10-10: run 2026-10-10T0206Z evening (10:06 PM ET / 02 UTC): 17 X reads (929 to 912 left today). Watch 300; trends US+WW; quote/repost word "is" (2+1); sensors news/money/science; hourly desks; trend stream Angel Reese; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.
- 2026-10-10: run 2026-10-10T0308Z evening (11:08 PM ET / 03 UTC): 18 X reads (912 to 894 left today). Watch 300; trends US+WW; quote/repost word "you" (2+1); sensors culture/sports/online; hourly desks; trend stream Mike Norvell; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. Skipped sexual/graphic ids 2108300852171583897, 2108575873175847080. SKIP/SKIP_ALL absent on pipeline.
- 2026-10-10: run 2026-10-10T0405Z evening (12:05 AM ET / 04 UTC): 20 X reads (894 to 874 left today). Watch 300; trends US+WW; quote/repost word "and" (2+1); sensors news/money/science; hourly desks; trend stream Angel Reese; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. Skipped sexual/graphic id 2096899547066736718. SKIP/SKIP_ALL absent on pipeline.

- 2026-10-10: run 2026-10-10T0506Z overnight (1:06 AM ET / 05 UTC): 17 X reads (874 to 857 left today). Watch 300; trends US+WW; quote/repost word "my" (2+1); sensors culture/sports/online; hourly desks; trend stream Valkyries; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline. Skipped sexual/graphic id 2108125158816768148.
- 2026-10-10: run 2026-10-10T0606Z overnight (2:06 AM ET / 06 UTC): 17 X reads (857 to 840 left today). Watch 300; trends US+WW; quote/repost word "it" (2+1); sensors news/money/science; hourly desks; trend stream Angel Reese; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. Skipped sexual/graphic ids 2089812075073909217, 2107990748406722737. SKIP/SKIP_ALL absent on pipeline.
- 2026-10-10: run 2026-10-10T0705Z overnight (3:05 AM ET / 07 UTC): 17 X reads (840 to 823 left today). Watch 300; trends US+WW; quote/repost word "that" (2+1); sensors culture/sports/online; hourly desks; trend stream Valkyries; screen 100 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.
- 2026-10-10: run 2026-10-10T0805Z overnight (4:05 AM ET / 08 UTC): 17 X reads (823 to 806 left today). Watch 300; trends US+WW; quote/repost word "just" (2+1); sensors news/money/science; hourly desks; trend stream Ukraine; screen 99 by id. No volume/stories/context/media descriptions. Non-hourly desks skipped. SKIP/SKIP_ALL absent on pipeline.

## 2026-10-10T1005Z
Overnight (06-11 UTC budget): 17 X reads (789→772 left). Watch 300; trends US+WW; quote/repost word "the" (2+1); sensors news/money/science; hourly desks; trend stream George Russell; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched.

## 2026-10-10T1105Z
Overnight (06-11 UTC budget): 17 X reads (772→755 left). Watch 300; trends US+WW; quote/repost word "this" (2+1); sensors culture/sports/online; hourly desks; trend stream Norris; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic id 2079166859488759952.

## 2026-10-10T1207Z
Daytime (12:00-05:00 UTC budget): 17 X reads (743→726 left). Watch 300; trends US+WW; quote/repost word "is" (2+1); sensors news/money/science; hourly desks; trend stream Ukraine; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched.
2026-10-10T1302Z: daytime capture ok (partial). 17 X reads (726 to 709). Sensors culture/sports/online; stream word "you"; trend Arsenal. Skipped 1 nsfw id in screen. No volume/context/media.

## 2026-10-10T1403Z
Daytime (12:00-05:00 UTC budget): 18 X reads (709→691 left; includes 1 burned empty pagination_token). Watch 300; trends US+WW; quote/repost word "and" (2+1); sensors news/money/science; hourly desks; trend stream Saka; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched.

## 2026-10-10T1502Z
Daytime (12:00-05:00 UTC budget): 17 X reads (691→674 left). Watch 300; trends US+WW; quote/repost word "my" (2+1); sensors culture/sports/online; hourly desks; trend stream Ukraine; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic ids 2079166859488759952, 2108837453251371419.

## 2026-10-10T1603Z
Daytime (12:00-05:00 UTC budget): 17 X reads (674→657 left). Watch 300; trends US+WW; quote/repost word "it" (2+1); sensors news/money/science; hourly desks; trend stream Marv; screen 100. No volume/context/media. Checker PASS partial (40 posts, 339 obs). Standing crypto-desk/author-cap untouched.

## 2026-10-10T1708Z
Daytime (12:00-05:00 UTC budget): 17 X reads (657→640 left). Watch 300; trends US+WW; quote/repost word "that" (2+1); sensors culture/sports/online; hourly desks; trend stream Ukraine; screen 100. No volume/context/media. Checker PASS partial (38 posts, 338 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic id 2108812467568865699.

## 2026-10-10T1808Z
Daytime (12:00-05:00 UTC budget): 17 X reads (640→623 left). Watch 300; trends US+WW; quote/repost word "just" (2+1); sensors news/money/science; hourly desks; trend stream Nebraska; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic id 2107834547752816718.

## 2026-10-10T1907Z
Daytime (12:00-05:00 UTC budget): 17 X reads (623→606 left). Watch 300; trends US+WW; quote/repost word "what" (2+1); sensors culture/sports/online; hourly desks; trend stream Zelensky; screen 100. No volume/context/media. Checker PASS partial (40 posts, 340 obs). Standing crypto-desk/author-cap untouched.

## 2026-10-10T2002Z
Daytime (12:00-05:00 UTC budget): 18 X reads (606→588 left). Watch 300; trends US+WW; quote/repost word "the" (2+1); sensors news/money/science; hourly desks; trend stream Nebraska; screen 100 + 2 nebraska author by-id. No volume/context/media. Checker PASS partial (40 posts, 308 obs). Standing crypto-desk/author-cap untouched.

## 2026-10-10T2107Z
Daytime (12:00-05:00 UTC budget): 19 X reads (588→569 left). Watch 300; trends US+WW; quote/repost word "this" (2+1); sensors culture/sports/online; hourly desks; trend stream Ukraine; screen 100 by id. No volume/context/media. Checker PASS partial (37 posts, 321 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic ids from exclude list.

## 2026-10-10T2200Z
Daytime (12:00-05:00 UTC budget): 16 X reads (569→553 left). Watch 177; trends US+WW; quote/repost word "is" (2+1); sensors news/money/science; hourly desks; trend stream UCLA; screen 100. No volume/context/media. Checker PASS partial (40 posts, 194 obs). Standing crypto-desk/author-cap untouched. Skipped possibly_sensitive ids from screen/sensors.

## 2026-10-10T2306Z
Daytime (12:00-05:00 UTC budget): 18 X reads (553→535 left). Watch 197; trends US+WW; quote/repost word "you" (2+1); sensors culture/sports/online; hourly desks; trend stream Arch Manning; screen 100. No volume/context/media. Checker PASS partial (40 posts, 229 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic ids from screen/exclude list. One wasted watch call on bad ids early in run counted in the 18.

## 2026-10-11T0005Z
Evening (12:00-05:00 UTC budget, new X day): 19 X reads (1000→981 left). Watch 197; trends US+WW; quote/repost word "and" (2+1); sensors news/money/science; hourly desks; trend stream #MITB; screen 100. No volume/context/media. Checker PASS partial (40 posts, 229 obs). Standing crypto-desk/author-cap untouched. Three wasted reads (bad watch ids once; unquoted and-stream twice). Skipped possibly_sensitive/NSFW ids from screen/exclude list.


## 2026-10-11T0101Z
Evening (12:00-05:00 UTC budget): 16 X reads (981→965 left). Watch 135; trends US+WW; quote/repost word "my" (2+1); sensors culture/sports/online; hourly desks; trend stream Arch; screen 66. No volume/context/media. Checker PASS partial (38 posts, 176 obs). Standing crypto-desk/author-cap untouched. Skipped sexual/graphic ids including 2109011084795584706 and FearedBuck private-drama clips. Sensor JSON saved via screen by-id only (inline sensor pages not re-saved as files).

## 2026-10-11T0202Z
Evening (12:00-05:00 UTC budget): 16 X reads (965→949 left). Watch 138; trends US+WW; quote/repost word "it" (2+1); sensors news/money/science; hourly desks; trend stream Penta; screen 100. No volume/context/media. Checker PASS partial (40 posts, 179 obs). Standing crypto-desk/author-cap untouched. Crypto desk retired_at 02:00Z so no desk.crypto sweep. Author-cap dropped: sciencegirl x2, ericldaugh x2, discussingfilm x1, atrupar x1. Skipped possibly_sensitive/NSFW ids from screen/exclude list.

## 2026-10-11T0301Z
Evening (12:00-05:00 UTC budget): 17 X reads (949→932 left). Watch 140; trends US+WW; quote/repost word "that" (2+1); sensors culture/sports/online; hourly desks; trend stream Kentucky; screen 100 (+1 wasted screen on bad id list). No volume/context/media. Checker PASS partial (40 posts, 179 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped: marionawfal x9, mlb x2, discussingfilm x1. Skipped possibly_sensitive ids from screen/exclude list.


## 2026-10-11T0403Z
Evening (12:00-05:00 UTC budget): 17 X reads (932→915 left). Watch 129; trends US+WW; quote/repost word "just" (2+1); sensors news/money/science; hourly desks; trend stream Bama; screen 100 + 1 Bama by-id. No volume/context/media. Checker PASS partial (40 posts, 178 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped: sciencegirl x2, atrupar x1. Skipped possibly_sensitive/NSFW ids from screen/exclude list.

## 2026-10-11T0558Z
Evening (12:00-05:00 UTC budget, late evening ~1:58 AM ET): 17 X reads (898→881 left). Watch 200; trends US+WW; quote/repost word "the" (2+1); sensors news/money/science; hourly desks; trend stream Georgia; screen 100 by id. No volume/context/media. Checker PASS partial (40 posts, 179 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped: sciencegirl x2. One wasted screen call on bad id list counted in the 17. Skipped possibly_sensitive/NSFW ids from screen/exclude list.

## 2026-10-11T0704Z
Overnight (06:00-11:00 UTC budget): 16 X reads (881→865 left). Watch 200; trends US+WW; quote/repost word "this" (2+1); sensors culture/sports/online; hourly desks; trend stream Bama; screen 100. No volume/context/media. Checker PASS partial (40 posts, 240 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped none.

## 2026-10-11T0802Z
Overnight (06:00-11:00 UTC budget): 16 X reads (865→849 left). Watch 200; trends US+WW; quote/repost word "is" (2+1); sensors news/money/science; hourly desks; trend stream Stein; screen 100. No volume/context/media. Checker PASS partial (33 posts, 233 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped none. Skipped possibly_sensitive/NSFW id 2108603994276847942.

## 2026-10-11T1206Z
Evening (12:00-05:00 UTC budget, ~8:06 AM ET): 16 X reads (790→774 left). Watch 200; trends US+WW; quote/repost word "it" (2+1); sensors news/money/science; hourly desks; trend stream Kyrie; screen 100. No volume/context/media. Checker PASS partial (40 posts, 231 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped: elonmusk x8, nba x3, cryptorover x1. Skipped possibly_sensitive/NSFW ids from exclude list.

## Daily scoreboard (partial 2026-10-11 UTC)
Running: after 0005Z+0101Z+0202Z+0301Z+0403Z+0507Z+0558Z+0704Z+0802Z+0900Z+1008Z+1105Z+1206Z — 226 reads used; posts kept this capture 40. Full day line at last run before 00:00 UTC.
2026-10-11T0507Z: partial evening run, 17 X reads (915→898). Watch 197; trends; quote/repost word what; sensors culture/sports/online; hourly desks; Kentucky trend stream; screen 100. No volume/story clusters/context.top/media. Author-cap dropped: barstoolsports x12, mlb x4, popbase x9, marionawfal x11, popcrave x1. Crypto desk retired untouched.
2026-10-11T0558Z: partial evening run, 17 X reads (898→881). Watch 200; trends; quote/repost word the; sensors news/money/science; hourly desks; Georgia trend stream; screen 100. No volume/story clusters/context.top/media. Author-cap dropped: sciencegirl x2. Crypto desk retired untouched.
2026-10-11T0704Z: partial overnight run, 16 X reads (881→865). Watch 200; trends; quote/repost word this; sensors culture/sports/online; hourly desks; Bama trend stream; screen 100. No volume/story clusters/context.top/media. Author-cap dropped none. Crypto desk retired untouched.
2026-10-11T0802Z: partial overnight run, 16 X reads (865→849). Watch 200; trends; quote/repost word is; sensors news/money/science; hourly desks; Stein trend stream; screen 100. No volume/story clusters/context.top/media. Author-cap dropped none. Crypto desk retired untouched.
2026-10-11T0900Z: partial overnight run, 16 X reads (849→833). Watch 200; trends; quote/repost word you; sensors culture/sports/online; hourly desks; Bama trend stream; screen 100. No volume/story clusters/context.top/media. Author-cap dropped none. Crypto desk retired untouched.

## 2026-10-11T1008Z
Overnight (06:00-11:00 UTC budget): 19 X reads (833→814 left; includes 3 wasted on unquoted "and" stream). Watch 200; trends US+WW; quote/repost word "and" (2+1); sensors news/money/science; hourly desks; trend stream Kentucky; screen 97. No volume/context/media. Checker PASS partial (40 posts, 236 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped: sciencegirl x3, cryptorover x2. Skipped possibly_sensitive/NSFW ids from exclude list.
2026-10-11T1008Z: partial overnight run, 19 X reads (833→814). Watch 200; trends; quote/repost word and (quoted); sensors news/money/science; hourly desks; Kentucky trend stream; screen 97. No volume/story clusters/context.top/media. Author-cap dropped: sciencegirl x3, cryptorover x2. Crypto desk retired untouched.

## 2026-10-11T1105Z
Overnight (06:00-11:00 UTC budget, ~7:05 AM ET): 17 X reads (814→797 left; includes 1 wasted on bad watch ids). Watch 200; trends US+WW; quote/repost word "my" (2+1); sensors culture/sports/online; hourly desks; trend stream Bama; screen 99. No volume/context/media. Checker PASS partial (40 posts, 238 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped none. Skipped possibly_sensitive/NSFW ids from exclude list.
2026-10-11T1105Z: partial overnight run, 17 X reads (814→797). Watch 200; trends; quote/repost word my; sensors culture/sports/online; hourly desks; Bama trend stream; screen 99. No volume/story clusters/context.top/media. Author-cap dropped none. Crypto desk retired untouched.
2026-10-11T1206Z: partial evening run, 16 X reads (790→774). Watch 200; trends; quote/repost word it; sensors news/money/science; hourly desks; Kyrie trend stream; screen 100. No volume/story clusters/context.top/media. Author-cap dropped: elonmusk x8, nba x3, cryptorover x1. Crypto desk retired untouched.
2026-10-14T1209Z: partial morning run, 22 X reads (1000→978; the X day had no reads before this run). First capture since 2026-10-11T1206Z, so there is a gap of about 72 hours in every watch series; capture/work/2026-10-11T1304Z is an unfinished work folder from Oct 11 (queries and id lists only, no X output, no capture file). Watch 67 of 67 unique watch.json ids returned (watch.json lists 69 ids with 2 duplicates); trends; trend names Starshield, Stolas, Hochul; quote/repost word that (1+1); sensors culture/sports/online; desks politics, world, justice, markets, ai, tech, medicine, entertainment, sports, internet; screen 100. No volume/story clusters/context.top/media; open requests deferred. Author-cap dropped: MarioNawfal x11, FabrizioRomano x10, DiscussingFilm x1, RNCResearch x1.
2026-10-14T1303Z: partial morning run, 27 X reads (978→951). Watch 41 of 41 (19 watch.json ids plus the 40 posts of 1209Z, 18 overlapping); trends; trend names Core CPI and September CPI (one event); quote/repost words just and what (2+1); sensors news/money/science; desks politics, defense, disaster, business, science, entertainment, music, gaming, ideas, sports, internet, life, offbeat, and markets out of turn for the CPI hour; screen 200 by id. No volume/story clusters/context.top/media; open requests deferred. Author-cap dropped: elonmusk x2. Left out as ad: 2086794573297361074 (kotakneo). Left out: 2110073014973051067 (sexual violence against a child alleged). private_individual set on 2008193557673488846, 2110135850361291059, 2110057477236789447. Crypto desk retired untouched.
2026-10-14T1406Z: partial morning run, 26 X reads (951→925). Watch 78 of 78 (34 watch.json ids plus the posts of 1209Z and 1303Z); trends; trend names Starshield, Wegmans, Ann Li, #NationalDessertDay, Hot CPI (Hot CPI is one event with September CPI and Core CPI); quote/repost words the, this, is (3+1); sensors culture/sports/online; desks politics, world, justice, ai, tech, medicine, entertainment, sports, internet (the 2-hour desks taken as due 1 h 57 min after 1209Z); screen 118 by id. Trend context posts (15) kept on top of the 40 global posts, so the file holds 55. No volume/story clusters/context.top; media description only for the Six Flags video pair; open requests deferred. Author-cap dropped: MarioNawfal x10, RapSheet x2, DiscussingFilm x2, IGN x1. private_individual set on 2110041731949576244, 2110066955634012367 (named ride victim), 2110050933283668252, plus the carried 1303Z ids. Crypto desk retired untouched.

## 2026-10-14T1509Z
Morning (12:00-05:00 UTC budget, ~11:09 AM ET): 27 X reads (925→898; includes 1 wasted on invalid PLACEHOLDER ids). Watch 132; trends US+WW; trend names Good Wednesday, Hump Day, Happy Hump, Don Mattingly, September CPI (Hump Day/Happy Hump NSFW-heavy, left out; CPI one event); quote/repost words you/"and"/my (3+1); sensors news/money/science; desks politics, entertainment, sports, internet, markets; screen ~200 by id. No volume/story clusters/context.top/media; open requests deferred; music/gaming/offbeat due but cut. Checker PASS partial (45 posts, 176 obs). Standing crypto-desk/author-cap untouched. Author-cap dropped none. Skipped possibly_sensitive/NSFW ids from exclude list.

## 2026-10-14T1607Z
Midday (12:00-05:00 UTC budget, ~12:07 PM ET): 29 X reads (898→869). Watch 176 of 176 (51 watch.json ids plus the posts of 1209Z-1509Z); trends US+WW; trend names Starshield, #OverflowingLoveForEVAN (one event with #아로새겨_시작될_에반의_날), Richard Heart, Stolas, Martha Plimpton; quote/repost words it/that/just (3+1); sensors culture/sports/online; desks politics, entertainment, sports, internet, world, justice, ai, tech, medicine, music; screen 225 by id (incl. 25 second-hop origins). No volume/story clusters/context.top/media; open requests deferred; gaming/offbeat and 4-hour desks cut for the 10-desk cap. Checker PASS partial (53 posts, 226 obs). Left out as ad: 2110223317416423775 (Starlink promo, 2.6M views, 287 likes). Left out: 2110338474394173951 (Stolas sexual reference). private_individual set on 2110109803305656826 (named ride victim), 2110076763799986523, 2110077784148316301, 2110228564717015082, 2110295825859420526. Author-cap dropped: MarioNawfal x6, billboard x3, RapSheet x1, NFL x1. Crypto desk retired untouched.
