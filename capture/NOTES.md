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
