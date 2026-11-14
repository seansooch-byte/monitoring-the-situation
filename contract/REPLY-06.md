# Reply to grokbot: the site is a newspaper, and Soochiebot writes its opinion

Sean pastes the block below to grokbot once. It covers what changed on 13 and 14 November 2026 in
`seansooch-byte/monitoring-the-situation` and `seansooch-byte/seansooch-byte.github.io`, and what
changes for grokbot. The durable rules are in `contract/PAPER.md`; nothing here says more than it does.

---

Pull both repos: `monitoring-the-situation` (main) and `seansooch-byte.github.io` (main). Then read
`contract/PAPER.md` in the situation repo. It is new, and it is the whole contract for the paper.

## Patch notes

**13 November: Field Notes on seansooch.dev.** `/notes/` launched with its own design. Your first post
(12 November, PR 47) and your voice notes (PR 46) were merged and went live on 14 November. Your
change to `tools/edition_test.py` in PR 47 was right: a test required the "no posts yet" sentence to
appear somewhere, which cannot hold once a post exists.

**14 November: Monitoring the Situation became a daily newspaper** (Edition 3, "The Broadsheet"), live
at https://situation.seansooch.dev.

- The front page is yesterday's edition: one Eastern day, midnight to midnight, ranked by the views
  each story's posts gained that day. Nobody chooses the order. On 13 November the FAA ground stop led
  with 20.5M views on the day across four posts.
- Posts the editor described that no story cites are printed as "Big on X, not yet a story" (news,
  money, science) or "What the internet watched" (the rest), so the gaps in the reporting show.
- New pages: `/edition/<day>/` (every day of the record), `/section/<group>/` (six), `/opinion/`,
  `/archive/` (back issues). Internet Pulse moved from `/` to `/pulse/`, as the paper's wire, unchanged.
- New files: `contract/PAPER.md`, `contract/paper.json`, `tools/edition.mjs`,
  `tools/lib/edition.mjs`, `tools/lib/opinion.mjs`, `tools/lib/pulse-history.mjs`.
- `npm test` now runs test files one at a time (two of them rebuild the same demo).
- CI now admits an `opinion:` commit that touches one `opinion/<day>.json` and nothing else.
- **Nothing in `GRABBER.md`, `CAPTURE.md` or your hourly routine changed.** Captures, the ledger, the
  pulse and the stories work exactly as before.

**14 November: seansooch.dev.** The situation's entry now says Edition 3 and its plate was retaken.
Every plate is now asked for by a stamp of its bytes (`/plates/<name>.webp?v=<md5 first 10>`), so a
retaken plate shows at once. After you retake a plate, run `python3 tools/build.py`: until you do, the
pages are stale and `tools/stage.sh` refuses.

## What changes for you

**1. Soochiebot moves from Field Notes to the paper's opinion.** Stop writing new Field Notes posts in
`seansooch-byte.github.io/notes/posts/`. Instead, one editorial a day in the situation repo:
`opinion/<day>.json`, schema `mts.opinion/1`. Its rules are in `contract/PAPER.md` under "The
opinion". What is different from Field Notes:

- It is one argued call on the day, not a recap. The paper already recaps the day around it.
- `head` (20 to 100 characters) and `text` (one to four paragraphs, 120 to 400 words). No title, no
  dek, no sections.
- **No number of its own, at all**: no figures and no braces. A year and a name that starts with a
  letter (GPT-5) are allowed. The page prints the numbers beside it.
- `cites` holds ids from that day's edition only: story ids, the ids of their posts, and the ids in
  `unreported` and `watched`. At least one.
- No quotation marks, no em or en dashes, no emoji, no web addresses, no markup, nothing that reads as
  a dose. No advice. On the news sections it may argue what a story means; it never adds a fact the
  story does not hold.
- The page already says a program wrote it and that the site is built with Claude and Grok. Do not
  repeat that line; in the 12 November post it appeared three times.
- The voice guide is still `notes/VOICE.md` in the seansooch.dev repo.

**2. How to write and send one.** After midnight Eastern, and before 7 AM Eastern:

1. `node tools/edition.mjs --day <yesterday> --out /tmp/edition` and read `/tmp/edition/<day>.json`.
2. Write `opinion/<day>.json`. Run the same command again. It exits 1, names every rule broken and
   writes nothing. Fix the opinion, never the rules.
3. `npm test`. The site's build reads every opinion, so a broken one would stop the hourly ship.
4. On a branch `opinion/<day>`, one commit whose message begins `opinion:`, touching only that file.
   Open a pull request. Sean reviews it; once merged, the next hourly ship publishes it. Never commit
   an opinion straight to main.

**3. Field Notes stays as it is.** `seansooch.dev/notes/` keeps its one post until Sean decides what
becomes of it (the likely end is a redirect to the paper's opinion page). Add nothing there.

**4. The Lab: one lesson is missing a file.** `lab/spirometry-lung-volumes/` (14 November) shipped
without `plan.json`. It answers 404 on the live site and the site's browser walk reports it. Add it,
following the plan schema in `lab/FORMAT.md` (seansooch.dev repo), in a pull request.

**5. Desk labels.** The paper's six sections count posts by your desk labels, and some were wrong on
13 November: a Fox News post on the ground stop filed under markets, Secretary Duffy's ground stop post
under offbeat, an ESPN trade report under business, an Avengers teaser under medicine. Check each
label against the desk's `scope` and `not_here` in `contract/desks.json`. A post you record only as a
reference for a story is often captured with no desk at all; give it one when you can tell.

## What I need back

- The model name to print on opinions (the 12 November post said "Grok Bot").
- The first opinion, as a pull request, for the day you choose.
- The Lab pull request for the missing `plan.json`.
- A line in `capture/NOTES.md` on the desk labels: what you changed and how you will check it.
