# The paper

Monitoring the Situation is becoming a daily newspaper of the internet: you open it and learn what is
going on. This document is the backbone every page of it is built on, whichever design it wears. It
changes nothing about how the record is made (`GRABBER.md`, `EDITOR.md`); it says how a day of the
record becomes an edition, and where the one opinion in it comes from.

## Who writes what

| Part of the paper | Written by | Rule |
|---|---|---|
| The numbers (views, counts, rank, sections) | Grok reads them from X; `tools/lib/edition.mjs` computes everything else | Nobody types a number. |
| The news (stories, the pulse's lines) | Claude, the editor | Describes and attributes; never an opinion. Unchanged. |
| The order of the front page | The edition builder, from the numbers | No hand ranks a story. The largest story leads. |
| The opinion ("The Read") | Soochiebot, kept by grokbot | One editorial a day, `opinion/<day>.json`, labelled as a program's opinion, set apart from the news. |

Soochiebot writes words, which the grabber does not: this is Sean's decision of 2026-11-14 and is
held to one folder (`opinion/`) and the rules below.

## An edition

An edition is one Eastern day, midnight to midnight, published the next morning. It is a pure
function of the record: the same captures, ledger, stories, pulse history and opinion give the same
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

**Stories.** Every story in `moments/` with views on the day, or begun that day. Its reach is the
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

## The opinion

`opinion/<day>.json`, one per day, written by Soochiebot from that day's edition and nothing else:

```json
{
  "schema": "mts.opinion/1",
  "date": "2026-11-13",
  "published": "2026-11-14",
  "model": "Grok Bot",
  "head": "The editorial's headline, 20 to 100 characters",
  "text": ["One to four paragraphs, 120 to 400 words in all."],
  "cites": ["2026-11-13-faa-nationwide-ground-stop"]
}
```

- `cites` names stories or posts that are in that day's edition, at least one. The page links them.
- No number of its own: no digit except a year (`2026`, `the 1990s`) or in a name that starts with
  a letter (`GPT-5`, `F-35`). The figures are on the page beside it, from the record.
- No quotation marks, no em or en dash, no emoji or pictograph, no web address, no markup, nothing
  that reads as a dose.
- No financial, medical or legal advice. Nothing about a private person or a minor. On the news
  sections it may argue about what a story means; it never adds a fact the story does not hold.
- A key this page does not name is refused. A broken opinion stops the edition with a sentence
  naming each rule it breaks; the edition is never published without saying so.

## What is left to the design

Everything visual. All three directions drawn on 2026-11-14 (the Broadsheet, the Wire, the Record)
read the same edition. The design picked becomes the site's next edition (`site/`); the old pages'
addresses keep working.
