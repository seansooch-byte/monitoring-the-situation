# The paper

Monitoring the Situation is becoming a daily newspaper of the internet: you open it and learn what is
going on. This document is the backbone every page of it is built on, whichever design it wears. It
changes nothing about how the record is made (`GRABBER.md`, `EDITOR.md`); it says how a day of the
record becomes an edition, and where the one letter in it comes from.

## Who writes what

| Part of the paper | Written by | Rule |
|---|---|---|
| The numbers (views, counts, rank, sections) | Grok reads them from X; `tools/lib/edition.mjs` computes everything else | Nobody types a number. |
| The news (stories, the pulse's lines) | Claude, the editor | Describes and attributes; never an opinion. Unchanged. |
| The order of the front page | The edition builder, from the numbers | No hand ranks a story. The largest story leads. |
| The Newsletter (one letter a day; the Paper prints its read) | Soochiebot, kept by grokbot | `newsletter/<day>.json` to `contract/NEWSLETTER.md`, labelled as a program's, set apart from the news. |

Soochiebot writes words, which the grabber does not: this is Sean's decision of 2026-11-14 and is
held to one folder (`newsletter/`) and the rules in `contract/NEWSLETTER.md`.

## An edition

An edition is one Eastern day, midnight to midnight, published the next morning. It is a pure
function of the record: the same captures, ledger, stories, pulse history and letter give the same
edition, byte for byte. `tools/edition.mjs --day 2026-11-13` writes it; `tools/lib/edition.mjs`
holds every rule and touches no file.

**What counts.** A post counts only when the ledger has it as `ok`, no flag in `private_individual`,
`minor`, `nsfw`, `graphic` is on it, and its desk is a desk in `contract/desks.json`. Its desk is the
editor's (the pulse) where the editor described it, else the grabber's (the first capture that gives
one: a later capture can carry a post again with no desk), else the first desk of a story citing it.

**Views on the day.** A post's views for the day are the views it gained between midnight and
midnight: its last reading at or before the day's end, less its last reading at or before the day's
start (zero for a post created that day). A post with no reading before the day began, created
earlier, is measured from its first reading that day, which undercounts and never overcounts. A
reading after the day's end never changes the edition. A post whose last reading is `unavailable`
gained nothing.

**Stories.** Every story in `moments/` begun by the day's end, with views on the day or begun that day. A
story begun later is never in an earlier day's edition, whatever its earlier posts gained: a front page carries
no headline from a later day. Its reach is the
sum of its counted posts' views on the day. Stories are ranked by reach, largest first.

- **The lead** is the first story. **The briefing** is the first five, in order.
- **Not yet a story** (`unreported`): posts the editor described on the pulse, cited by no story, in
  a news section (`news_sections` in `contract/paper.json`), largest first, one per account.
- **What the internet watched** (`watched`): the same, in every other section.
- Nothing appears that the editor did not describe or a story does not cite. A post's own text is
  never part of an edition.

**Sections** are the desk groups in `contract/desks.json` (News, Money, Science and tech, Culture,
Sports, Life online). For each: posts created that day, views gained that day, its share of the day's
views, posts per Eastern hour, its stories in rank order, and its three largest described posts.

## The letter

The day's letter is the Newsletter's (`contract/NEWSLETTER.md`): `newsletter/<day>.json`, written by Soochiebot from
that day's edition. The edition checks it: a story it cites must be in the edition; a post must be one X confirmed
that the record holds and may show (which takes in a post the editor described the morning after). A broken
letter refuses the edition with every reason. The letter rides in the edition whole, and the Paper's band prints
its read. Replaced the one-editorial-a-day opinion of the same morning, before any was written.

## What is left to the design

Everything visual. All three directions drawn on 2026-11-14 (the Broadsheet, the Wire, the Record)
read the same edition. The design picked becomes the site's next edition (`site/`); the old pages'
addresses keep working.
