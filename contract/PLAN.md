# The plan: `requests/plan.json`

The next run's read list, in order, with a budget line for each read. The grabber executes it top
to bottom and records what it did. The cut order lives in the tool that writes it, where Sean can
read it, and not in the grabber's judgement. Schema tag: `mts.plan/1`.

## Who writes it, and when

`tools/plan-reads.mjs`, a tool and never a person. It runs after every capture (in
`tools/refresh.sh`) and at the end of every editor pass that changes `requests/watch.json`, so the
file in the repository is always for the hour after the newest capture. It is deterministic: the
same captures, requests, desks, `contract/budget.json` and clock give the same file, so the plan
any run was given can be regenerated with `node tools/plan-reads.mjs --at <time> --print`.

The grabber never edits it. If it is missing, or its `for_run` is not the hour being run, follow
the standing orders in `GRABBER.md` and say so in `run.reason`.

## Fields

| Field | What it holds |
|---|---|
| `for_run` | The UTC hour the plan is for, `YYYY-MM-DDTHHZ`. Record it in `run.plan`. |
| `band` | `day` or `overnight`, from `contract/budget.json`. |
| `day` | `date`; `reads_left_before`, the reads left in the UTC day before this run (from the last run's `run.reads_left`); `hours_left`, runs left in the day including this one; `short`, whether the day is short; `rule`, where the allowance came from. |
| `allowance` | The reads this run may spend: the band's cap, or on a short day the reads left spread over the runs left. |
| `total_reads` | The sum of the items' `reads`. |
| `over_budget` | `true` when even the re-read list and the counts exceed the allowance. Read them anyway; they are never cut. |
| `items[]` | The reads, in order. Each has `n`, `sweep` (a sweep id from `GRABBER.md`), `reads` (how many reads it is allowed) and often `why`. The `watch` item carries `ids`, the re-read list in order: read it in batches of `ids_per_read`. `desk.<desk>` items carry `every`. |
| `cut` | The sweeps cut to fit the allowance, in the order they were cut. |
| `left_out` | `rereads.slowed` (flat posts waiting for their sixth run), `rereads.over_cap`, `rereads.unavailable`, all counting only posts outside `watch.json`, which is always in the `watch` item in full, first; `desks_not_due`; `requests_waiting` (unanswered but over this run's share); `requests_stale` (older than three days, the editor's to prune). |
| `inputs` | How many captures the plan was computed from and which, and the sizes of the request files. |

## How to execute it

1. `git pull --rebase origin main`, then read `requests/plan.json`. Check `for_run`.
2. Go down `items` in order. Spend at most `reads` on each. The `watch` item is the whole re-read
   list: do not add to it, do not reorder it, do not drop from it; a post on it that X no longer
   returns gets its `unavailable` observation as the standing orders say.
3. `screen` is the one item you size yourself: reads by id to screen candidates the discovery
   sweeps turned up. When it was cut, screen with what the discovery reads returned.
4. Record every item as a sweep in the capture, with `ok`, `partial` or `skipped` and a reason,
   exactly as before. A sweep the plan did not list is recorded the same way if you ran it, and the
   reason says why.
5. Write `run.reads`, `run.reads_left` and `run.plan`.

The plan can ask for less than the standing orders would; it never asks for more than the day
can afford. A run that follows the plan and spends what it lists is `ok`.
