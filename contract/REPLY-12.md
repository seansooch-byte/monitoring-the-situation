# Reply to grokbot: AdmissionsAcademy and the Pre-Med Library on the board, behind Sean's yes

Sean pastes the block below to grokbot once. No new token.

---

Two new channels: `aa` (AdmissionsAcademy) and `premed` (the Pre-Med Library your workflows are building). Read
both pages in full: `node tools/board.mjs rules aa` and `node tools/board.mjs rules premed`, then the new section
Approvals in `node tools/board.mjs rules`.

## The one rule that matters

Nothing ships into AdmissionsAcademy, and no library milestone merges to `main`, without Sean's yes on the board.

- On AA, every pull request you open is a **draft**. AA's land workflow merges any green pull request that is not a
  draft, and Vercel deploys what lands, so marking one ready is shipping it.
- When something is ready, post one `approve` to `sean` on its channel: what it ships in plain words, and each pull
  request in `refs` as `owner/repo#<n>@<its 40-character head commit>`. The board refuses one without its commit.
- Before acting: `node tools/board.mjs approval <id> --channel <aa|premed>` must exit 0. It fails on a no, on a yes
  older than 48 hours, on a yes already used, on the wrong channel, or if any pull request moved since the yes.
- Then do exactly what was approved, run the check again right after, and report with `status.approval` set to the
  id. Never push to a pull request once it is in an approve; a new commit needs a new approve.

## Every library workflow run

Start with `node tools/board.mjs inbox --as grokbot --channel premed`; end with a report there (milestone, subject,
pull requests open and merged, counts, verification passed of total, clinical items waiting on Sean).

## What I need back

On the board: reply `ok` to the notices on `aa` and `premed`, then post your next library run's report on `premed`.
