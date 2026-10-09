# Notes from the grabber

Append one dated line when something outside `capture/` looks wrong, or when the contract cannot
express something you saw. The editor reads this file on every pass.

- 2026-10-09: `npm test` fails on Node 20.19 ("Could not find .../tests/*.test.mjs") because Node 20's `--test` does not expand globs; package.json says node >=18. `node --test tests/check-capture.test.mjs` and Node 22 both pass 34 of 34.
- 2026-10-09: X gives no community notes, no trend post counts, no trend-to-story link, no engagement sort and no min likes operator; deleted and never-existing ids return the same Not Found Error. Details in capture/CAPABILITIES.md.
- 2026-10-09: KICKOFF step 4 says start the hourly schedule; the grabber was told by Sean's main agent not to create it, so the schedule is not running yet. The steps are in capture/RUNBOOK.md.
