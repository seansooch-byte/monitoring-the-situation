# Reply to grokbot: spend the budget

Sean pastes the block below to grokbot once. It carries the contract changes made on 2026-10-27
in `contract/GRABBER.md` (Re-reads, Volume, The read budget, Schedule and budget, Requests from
the editor) and asks two questions for later phases of `PROGRAM.md`. The durable parts are in
`GRABBER.md`; nothing here says more than it does.

---

Pull, then read `contract/PLAN.md` (new) and re-read four parts of `contract/GRABBER.md`:
Re-reads, Volume, The read budget, and Schedule and budget. `PROGRAM.md` at the root is new and
says where this is going; it is for reading, not orders.

**1. The budget is there to be spent.** From your own captures, 2026-10-21 to 2026-10-27: every
run `partial`; 18 to 23 reads a run against a daytime allowance of 42; days ending with about
500 of 850 unused; fifteen of nineteen desks skipped since 2026-10-10 with "non-hourly desk
skipped after cut order"; no run reporting a 429. From the next run: a daytime run that spends
under 30 reads while desks are due is a failure, reported as `partial` with that reason. A day
should end between 600 and 850. `run.status` is `ok` only when every due desk was swept and the
re-read list was read in full. The cut order still exists, but it applies only when the day is
short: fewer reads left than 30 times the hours left before 00:00 UTC.

**2. Re-reads: up to 800 by day, and flat posts every sixth run.** The list is built in the same
order and now stops at 800 posts (eight reads) in the 12:00 to 05:00 UTC band, 400 overnight. A
post that gained under 2 percent in views across its last six readings is re-read every sixth
run instead of every run, whichever list put it there; a story-cited post is never dropped, only
slowed the same way. The checker allows 1,500 observations a file, so nothing else changes. Say
in `capture/NOTES.md` how many posts the list held, how many it left out, and which of those
were story-cited; the target is none.

**3. Volume: every desk every four hours.** Five desks a run in a fixed rotation (list it in
`capture/CAPABILITIES.md`), so each desk's week of hourly counts is never more than four hours
old. One read each, 120 a day. This is the signal behind the site's baselines, and it is never
cut.

**4. `requests/plan.json` is live: execute it.** From your next run, after `git pull`, read
`requests/plan.json` (format and how to execute it: `contract/PLAN.md`). It is the run's read
list in order with a budget line for each read: the re-read ids in batches of 100, the desks
due, the five desks whose counts are due, the open requests, then discovery. A tool writes it
after every capture from your own captures, the editor's requests and `contract/budget.json`,
and cuts it to what the day can afford, so the cut order is no longer yours to apply. Execute it
top to bottom and record what you did; the standing orders fill only what it leaves open; never
edit it. If its `for_run` is not the hour you are running, say so in `run.reason` and follow the
standing orders. The first plan, for 05Z on 28 October, asks for 42 reads: all nineteen desks
(fifteen have not been swept since 10 October), five desks' counts, 264 re-reads in three reads
with 221 flat posts waiting for their sixth run, then discovery. The sixteen requests in
`open.json` were all answered once and have been removed; the request sweeps stop with them.

**5. Three numbers in every run from now on.** `run.reads` (the reads this run spent),
`run.reads_left` (the reads left in the UTC day after it, as the API reports them) and
`run.plan` (the plan's `for_run` you executed, or `null`). The checker warns when the first two
are missing today and refuses the file from 4 November. The budget is a number in the record,
not a sentence.

**6. Two questions, answered in `capture/NOTES.md`.** (a) Can your scheduler run a ten-minute
trigger while `requests/plan.json` says `mode: crisis`, for a few hours at a time? If not, what
is the shortest regular interval it can run? (b) When the editor is ready, can the hourly run
deliver a capture by `POST` with a bearer token to a URL on situation.seansooch.dev instead of
a git push, and keep pushing `NOTES.md`, `CAPABILITIES.md` and the rest as now?

**7. Five symlinks in your scratch break the Mac checkout.** `capture/work/2026-10-17T2308Z/`
holds `trend_georgia.txt -> trend_Georgia.txt`, the same for Gunner, Michigan and Tennessee, and
`trend_rocco.txt`. On Sean's Mac the disk ignores case, so each of those links points at itself
and anything that walks `capture/` loops. The editor's tools no longer follow links, but the
checkout still shows the four pairs as changed and the ship script refuses a changed tree.
Delete the five links in your next capture commit. From now on, commit no symlinks and no two
names that differ only by case, anywhere in the repository.

**8. The store is live; deliver there too once you have the token.** GRABBER.md, Delivery:
after each push, `POST https://situation.seansooch.dev/ingest` with `Authorization: Bearer
<token>` and the capture as the JSON body. The answer is the checker's verdict. Sean will give
you the token; until then the editor mirrors your pushes into the store every hour, and the git
push stays the delivery of record either way until the editor says the cutover is done. This
answers your question (b) above in advance: yes, and here is how.

**9. For Sean, not for you:** the 7:03 AM briefing shares this budget and nothing reads it. If
Sean retires it, the ceiling moves from 850 to 900 and the contract will say so. The store's
token is in `store.local.token` at the root of Sean's checkout, ignored by git; it goes to
grokbot by a channel of Sean's choosing, never through this repository.
