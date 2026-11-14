# Reply to grokbot: the site is a newspaper, and Soochiebot writes its Newsletter

Sean pastes the block below to grokbot once. It covers what changed on 13 and 14 November 2026 in
`seansooch-byte/monitoring-the-situation` and `seansooch-byte/seansooch-byte.github.io`, and what changes for
grokbot. The durable rules are in `contract/PAPER.md` and `contract/NEWSLETTER.md`; nothing here says more.

---

Pull both repos: `monitoring-the-situation` (main) and `seansooch-byte.github.io` (main). Then read
`contract/NEWSLETTER.md` in the situation repo. It is new, and it is the whole contract for Soochiebot's writing.

## Patch notes

**13 November: Field Notes on seansooch.dev.** Your first post (12 November, PR 47) and your voice notes (PR 46)
were merged and went live. Your change to `tools/edition_test.py` in PR 47 was right.

**14 November: Monitoring the Situation became a daily newspaper**, live at https://situation.seansooch.dev.

- **The Paper.** The front page is yesterday's edition: one Eastern day, ranked by the views each story's posts
  gained that day. Nobody chooses the order. On 13 November the FAA ground stop led with 20.5M views on the day.
  Posts the editor described that no story cites are printed as "Big on X, not yet a story" (news, money,
  science) or "What the internet watched" (the rest). New pages: `/edition/<day>/`, `/section/<group>/`,
  `/archive/` (back issues). Internet Pulse moved from `/` to `/pulse/`, as the paper's wire, unchanged.
- **The Newsletter.** A switch under the nameplate turns every page between the Paper and the Newsletter. The
  Newsletter is Soochiebot's letter a day, set as a letter (letterhead, date, Re: line, Dear reader, the read,
  Yours, Soochiebot) with Harvard references the site writes itself. The Paper prints the letter's read and
  links it. https://situation.seansooch.dev/newsletter/
- **Field Notes moved there.** It is no longer on seansooch.dev: every `/notes/` address answers 301 at
  `situation.seansooch.dev/newsletter/`, day for day, and your 12 November post is Newsletter No. 1, its words
  unchanged.
- New files in the situation repo: `contract/PAPER.md`, `contract/NEWSLETTER.md`, `contract/VOICE.md` (your voice
  file, moved from seansooch.dev), `contract/paper.json`, `tools/edition.mjs`, `tools/lib/edition.mjs`,
  `tools/lib/letter.mjs`, `tools/lib/pulse-history.mjs`. `npm test` runs test files one at a time.
- CI admits a `newsletter:` commit that touches one `newsletter/<day>.json` and nothing else.
- **Nothing in `GRABBER.md`, `CAPTURE.md` or your hourly routine changed.** Captures, the ledger, the pulse and
  the stories work exactly as before.

**14 November: seansooch.dev.** The situation's entry says Edition 3 and its plate was retaken. Every plate is now
asked for by a stamp of its bytes (`/plates/<name>.webp?v=<md5 first 10>`), so a retaken plate shows at once.
After you retake a plate, run `python3 tools/build.py`: until you do, the pages are stale and `tools/stage.sh`
refuses.

## What changes for you

**1. Soochiebot writes the Newsletter, in the situation repo.** One letter a day: `newsletter/<day>.json`, schema
`mts.letter/1`. Write nothing more under `notes/` in seansooch.dev; that folder is gone. The format is the Field
Notes one you know, with these changes (all in `contract/NEWSLETTER.md`):

- Renamed: `title` is `subject` (the Re: line), `dek` is `summary` (the sentence after Dear reader), `take` is
  `read` (the closing call, which the Paper prints).
- A source is ids only, with no `label`: a story by its id, or a post by its id and handle. The site writes the
  Harvard references itself (titles from the stories, authors from the record, the dates), so you type none.
- A story you cite must be in that day's edition. A post must be one X confirmed that the record holds; a post the
  editor described the morning after is fine.
- 200 to 800 words in all; a note up to 120 words. The figure rules are unchanged: no number typed in a sentence.
- The page already says a program wrote it and that the site is built with Claude and Grok. Do not repeat that
  line; the 12 November post said it three times.
- The voice guide is `contract/VOICE.md` in the situation repo. Propose changes to it by pull request.

**2. How to write and send one.** After midnight Eastern, and before 7 AM Eastern:

1. `node tools/edition.mjs --day <yesterday> --out /tmp/edition` and read `/tmp/edition/<day>.json`: its stories,
   their posts, and what is not yet a story.
2. Write `newsletter/<day>.json`. Run the same command again. It exits 1, names every rule broken and writes
   nothing. Fix the letter, never the rules.
3. `npm test`. The site's build reads every letter, so a broken one would stop the hourly ship.
4. On a branch `newsletter/<day>`, one commit whose message begins `newsletter:`, touching only that file. Open a
   pull request. Sean reviews it; once merged, the next hourly ship publishes it. Never commit a letter
   straight to main.

**3. The Lab: one lesson is missing a file.** `lab/spirometry-lung-volumes/` (14 November) shipped without
`plan.json`. It answers 404 on the live site and the site's browser walk reports it. Add it, following the plan
schema in `lab/FORMAT.md` (seansooch.dev repo), in a pull request.

**4. Desk labels.** The Paper's six sections count posts by your desk labels, and some were wrong on 13
November: a Fox News post on the ground stop filed under markets, Secretary Duffy's ground stop post under
offbeat, an ESPN trade report under business, an Avengers teaser under medicine. Check each label against the
desk's `scope` and `not_here` in `contract/desks.json`. A post you record only as a reference for a story is often
captured with no desk at all; give it one when you can tell.

## What I need back

- The model name to print on letters (No. 1 says "Grok Bot").
- The first letter, as a pull request, for the day you choose.
- The Lab pull request for the missing `plan.json`.
- A line in `capture/NOTES.md` on the desk labels: what you changed and how you will check it.
