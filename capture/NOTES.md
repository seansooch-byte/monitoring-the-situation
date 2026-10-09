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

## Daily scoreboard

One line per UTC day, appended in the last run before 00:00 UTC. Counted over all captures of the
day with duplicates removed; views are at each post's last reading; age is at first capture.
Sources are the sweep families each post was listed under (a post can count for several).

Format: `date | reads used | posts kept | >1M | >5M | >10M | largest | median | median age (h) | per source: largest / median`

- 2026-10-09 (partial, through run 0702Z) | 147 | 494 | 44 | 12 | 7 | 44,168,298 (2108187065687118261) | 95,060 | 10.2 | global sweeps 44,168,298 / 655,426; stream.global.quote 44,168,298 / 230,404; desk streams and clusters 2,125,674 / 85,244; trends 2,125,674 / 241,537; sensors 9,191,949 / 81,146; context 832,635 / 4,970; requests 39,941,861 / 614
