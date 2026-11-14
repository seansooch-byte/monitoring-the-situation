# The Newsletter

One letter a day by Soochiebot, on the day before, from that day's edition (`contract/PAPER.md`) and nothing
else. It is the other way to read the paper: a switch under the nameplate turns every page between **The Paper**
and **The Newsletter**. The Paper prints the letter's closing read in its band and links the whole letter.

Soochiebot is a program set to sound like Sean Sooch, kept by grokbot. It writes one file; the site builds the
letter, its letterhead, its sign-off and its references. This document is the whole contract between them.

## Who does what

| | Does | Never does |
|---|---|---|
| Soochiebot | Reads the day's edition. Writes `newsletter/<day>.json`. Sends it as a pull request. | Writes HTML. Types a web address or a reference. Types a number into a sentence. Reads anything private. |
| The build | Checks the letter against this page and against the day's edition, sets it as a letter, writes the Harvard references from ids. | Publishes a letter that breaks a rule: the edition is refused, naming the file and every rule. |
| Sean | Reads the pull request. Merges or closes it. | |

The writer's input is the edition and `contract/VOICE.md`, nothing else: no texts, no
mail, no calendar, no vault. The page says a program wrote it; the letter does not need to say so.

## The file

`newsletter/2026-11-12.json` is the letter about 12 November 2026. One a day; the file name is the day.

```json
{
  "schema": "mts.letter/1",
  "date": "2026-11-12",
  "published": "2026-11-13",
  "model": "the model that wrote it",
  "subject": "The Re: line, 20 to 90 characters",
  "summary": "One sentence after Dear reader, at most 220 characters.",
  "lead": { "desk": "business", "head": "A heading", "text": ["One to three paragraphs.", "A figure: {views}."], "cites": ["merger"] },
  "notes": [
    { "desk": "ai", "head": "A heading", "text": "One paragraph, at most 120 words.", "cites": ["meetings"] },
    { "desk": "sports", "head": "A heading", "text": "One paragraph.", "cites": ["nba"] }
  ],
  "read": { "text": ["One or two paragraphs: what the day adds up to, one call."], "cites": [] },
  "sources": {
    "merger": { "story": "2026-11-12-spacex-tesla-merger-talks" },
    "meetings": { "story": "2026-11-12-claude-meetings-beta" },
    "nba": { "post": "2121083956724408551", "handle": "NBA" }
  },
  "figures": { "views": { "value": "52", "of": "points Cade Cunningham scored", "source": "nba" } }
}
```

No other key is read, and a key this page does not name stops the build.

## The shape

- **The subject** is the letter's Re: line. **The summary** is the one sentence after "Dear reader,".
- **The lead**: the day's largest story or the one that matters most to the argument. One to three paragraphs.
- **Notes**: two to four other desks than the lead's, one paragraph each, no desk twice.
- **The read**: one or two paragraphs, one call on what the day adds up to. The Paper prints it.
- 200 to 800 words in all. The build adds "Yours, Soochiebot" and the line saying what it is.

## Sources and references

- A source is a story in that day's edition (`story`: its id) or a post X confirmed that the record holds and may
  show (`post`: its id, and `handle`: the account). Nothing else can be cited. Run the edition (below) to see
  what is there.
- The build writes the references in the Harvard style (Cite Them Right): a story as `Monitoring the Situation
  (2026a) Title. Available at: <address> (Accessed: <published>).`, a post as `Name [@handle] (2026) Post on X,
  12 November. Available at: <address> (Accessed: <published>).` In the text, each block ends with its
  citations: `(Monitoring the Situation, 2026a; NBA, 2026)`. One author in one year more than once takes a, b, c in
  the order of the list, which is alphabetical. The writer types none of this.
- The lead cites at least one source and so does each note. Every source is cited somewhere.

## Numbers

A sentence holds no number of its own. A number is a figure: `figures` gives it a `value`, says what it is
`of`, and names the `source` it was read from; the sentence asks for it with `{its_key}`. The letter prints each
figure in its place, and again under Figures with its citation.

- Refused in a sentence: `35.7M`, `12%`, `$40B`, `31-17`, `3x`, `7th`, `~40%`, `+12`, `12-point`, `40-year-old`,
  `98mph`, a count after an ordinary word (`about 40 people`), and a number before a scale word (`Tesla 40 billion`).
- Allowed: a year (`2026`, `the 2020s`); a name with digits in it (`GPT-5`, `F-35`, `COVID-19`, `49ers`, `5G`,
  `9/11`); a plain version or ordinal straight after a capitalised name (`Gemini 4`, `Game 7`, `November 12`).
- Small counts are words: three, a dozen. The subject and the summary may not ask for a figure.
- A figure's `value` is a number as a reader writes one: `35.7M`, `12%`, `-3.2%`, `$1.2T`, `$40 billion`,
  `31-17`, `3x`, `1977-78`. The rule is a net, not a proof; do not look for its holes.

## Words

- No quotation marks, double or single (an apostrophe is fine). Say what was said in your own words and cite it.
- No em dash, en dash or double hyphen. No emoji or pictographs. No web addresses. No markup; `**bold**` is the
  one mark a sentence may carry.
- Nothing that reads as a dose, anywhere. No private person, no minor, nothing about Sean's school, schedule,
  friends or family. No advice: not what to buy, take or bet.
- On the news desks describe and attribute; keep the argument for the read. The letter never adds a fact its
  sources do not hold.

## Writing and sending a letter

1. After the Eastern day ends: `node tools/edition.mjs --day <day> --out /tmp/edition`, and read the edition.
2. Write `newsletter/<day>.json`. Run the same command again: it exits 1 and names every rule broken, and writes
   nothing. Fix the letter, never the rules.
3. `npm test`. The site's build reads every letter, so a broken one would stop the hourly ship.
4. On a branch `newsletter/<day>`, one commit whose message begins `newsletter:`, touching only that file. Open a
   pull request. Sean reviews it; once merged, the next hourly ship publishes it. CI refuses a `newsletter:`
   commit that touches anything else. A letter is corrected by another `newsletter:` commit to the same file.

## The board

Each letter starts and ends on the board, channel `newsletter`: read
https://agents.seansooch.dev/channels/newsletter.md once, then, for every letter, begin with
`node tools/board.mjs inbox --as grokbot --channel newsletter` and end with its report there once the
pull request is open. Claude answers that report with its review; Sean merges.
