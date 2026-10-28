# requests/

Written by the editor, read by the grabber at the start of every run. The grabber never edits these files.

- `open.json`: asks for the next run. Each has an `id`, a `kind` and an `ask` in plain words.
  Kinds: `lookup` (one post, given as a url in `post`), `origin` (find the first post of a thing),
  `context` (the most liked replies and quote posts of the post in `post`), `search` (a query described in `ask`),
  `notice` (the editor changed something in `contract/`; read what `ask` points at and answer `ok`).
  The grabber answers each one once, in the `answers` array of its capture, by `id`.
- `watch.json`: post ids to re-read every run until the editor removes them.
- `plan.json`: the next run's read list, in order, with a budget line each. Written by
  `tools/plan-reads.mjs` after every capture and after every editor pass, never by hand. The
  grabber executes it; the format is `contract/PLAN.md`.
