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

## Daily scoreboard

One line per UTC day, appended in the last run before 00:00 UTC. Counted over all captures of the
day with duplicates removed; views are at each post's last reading; age is at first capture.
Sources are the sweep families each post was listed under (a post can count for several).

Format: `date | reads used | posts kept | >1M | >5M | >10M | largest | median | median age (h) | per source: largest / median`

- 2026-10-09 (partial, through run 1906Z) | ~376 | update at day end
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
