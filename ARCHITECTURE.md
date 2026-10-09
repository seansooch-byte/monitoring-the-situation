# Architecture

Monitoring the Situation is a static website about what the internet is paying attention to,
with X as its main instrument. This repository is the whole system: it is the handoff between the
two agents that make the site, the record of everything they produced, and the source of the site.

Status of each part is marked **Built** or **Planned**. Nothing marked Planned exists yet.

## The pieces

```mermaid
flowchart LR
  X[(X)] -->|reads| G["Grabber<br/>Grok, through grokbot"]
  G -->|"capture/YYYY/MM/DD/HHMMZ.json"| C1{"Gate 1: structure<br/>tools/check-capture.mjs"}
  C1 -->|passes| CAP[("capture/")]
  CAP --> V{"Gate 2: existence<br/>X confirms each post"}
  V -->|confirmed posts only| E["Editor<br/>Claude"]
  WEB[(Reporting on the web)] -->|research| E
  E -->|"moments/ and briefs/"| ED[("the editor's files")]
  E -->|"requests/open.json, watch.json"| G
  ED --> B["Build"]
  CAP -->|numbers, for confirmed posts only| B
  B --> D["dist/"] --> CF["Cloudflare Pages"] --> R((Reader))
```

Every arrow is a real dependency: the node at its head reads what the node at its tail wrote.

| Node | Job | Reads | Writes | How it fails |
|---|---|---|---|---|
| Grabber | Record what is viral on X, and re-read it on a schedule | X, `requests/` | `capture/` | A capture with `run.status` `partial` or `down` and a reason. A missing file means it did not run. |
| Gate 1, structure (**Built**) | Reject a malformed capture | one capture file, ids from earlier captures | PASS or a list of errors | Exit 1. The grabber fixes the file or replaces it with a `down` run. |
| Gate 2, existence (**Built**: `tools/verify-posts.mjs`) | Confirm against X that each post exists and that its author and text match | `capture/`, X's public oEmbed endpoint | a ledger of confirmed, missing and mismatched posts | A post that is not confirmed is never published. An invented post counts against its run. |
| Editor | Group posts into stories, research them, write every word | confirmed posts, reporting on the web | `moments/`, `briefs/`, `requests/` | A story it cannot stand behind is not written. |
| Build (**Built**: `tools/build.mjs`) | Render the site | `moments/`, `capture/`, `verified/posts.json`, `contract/desks.json`, `site.json` | `dist/` | Refuses to build if a story cites a post that no capture recorded or that Gate 2 has not confirmed. |
| Cloudflare Pages (**Planned**, waiting on a hostname) | Serve `dist/` | `dist/` | the public site | The previous deployment stays live. |

Two rules hold the design together:

1. **Words and numbers come from different hands.** The grabber supplies posts and numbers and
   never writes prose. The editor writes prose and never supplies a post or a number. So an invented
   post and an unsupported sentence are each one party's failure and can be found separately.
2. **Nothing appears until the editor has passed it.** A capture is never shown to a reader
   directly. Once the editor has put a post in a story, its numbers refresh on their own from later
   captures; new posts wait for the editor.

## Directory map

| Path | Owner | What it is |
|---|---|---|
| `contract/` | Editor | The grabber's standing orders (`GRABBER.md`), the capture format (`CAPTURE.md`), the desks (`desks.json`), a checked example. **Built.** |
| `tools/check-capture.mjs` | Editor | Gate 1, and the definition of a valid capture. **Built.** |
| `tests/` | Editor | The contract as tests. **Built.** |
| `requests/` | Editor | What the editor wants from the next run: lookups, searches, and the list of posts to keep re-reading. **Built** (format); the grabber starts reading it with its first run. |
| `capture/` | Grabber | One file per run, append only. Empty until the first run. |
| `moments/` | Editor | One file per story (`mts.moment/1`): title, standing, what happened, why it is spreading, how each world sees it, what is on the record, the posts it cites by id, sources. **Built.** |
| `verified/posts.json` | Editor | Gate 2's ledger: for each post checked, what X answered and when. **Built.** |
| `site.json` | Editor | The site's name, its pinned post and its statement of purpose. **Built.** |
| `briefs/` | Editor | One file per day: the daily briefing by desk. **Planned.** |
| `site/` | Editor | The stylesheet, the page script and the icon. Page templates live in `tools/build.mjs`. **Built.** |
| `tools/lib/metrics.mjs` | Editor | Arithmetic on readings: magnitude, a story's totals and trend, a desk's trace. **Built.** |
| `tools/make-demo.mjs`, `tools/demo-stories.mjs` | Editor | An invented day in the real file formats, for design work. A build from it is marked on every page and leaves a `DEMO` file so it is never deployed. **Built.** |
| `.github/workflows/check.yml` | Editor | Runs the tests and Gate 1 on every push, and fails a capture commit that touches anything outside `capture/`. **Built.** |

## The desks

The site watches twenty desks in six groups: News (politics, world, defense, justice, disaster),
Money (markets, business, crypto), Science and tech (ai, tech, science, medicine), Culture
(entertainment, music, gaming, ideas), Sports (sports), and Life online (internet, life, offbeat).

`contract/desks.json` is the only list. Each desk has an id, a short code, a scope, its near
misses, its beats, how often the grabber sweeps it, and the smallest post worth taking. Three
readers share the file, so a desk is added, merged or renamed in one place:

- the checker rejects a post or sweep whose desk is not in it, and a beat that is not its desk's;
- the grabber decides which desks are due and what clears the floor from it;
- the site (**Planned**) draws its sections, their order and their codes from it.

A desk id that has been used in a capture is never renamed or removed, only retired: old captures
still carry it.

## The checks on the grabber

A language model reading X can produce a post that looks right and does not exist. Three checks,
none of which trust the grabber's own word:

- **The id carries its own date.** An X id encodes the millisecond it was created. Gate 1 rejects a
  record whose `created_at` disagrees with its id. A made-up id almost never survives this.
- **X is asked directly.** Gate 2 asks X's public oEmbed endpoint for each post before it is
  published. It answers with the author and text for a real post and 404 for one that does not exist.
  Checked on 2026-10-09: a real post returned its author and text; a random id returned 404.
- **Some lookups have no answer.** The editor may ask the grabber to look up an id that does not
  exist. The right answer is `not_found`. A record returned for one is an invention, caught by the
  same Gate 2.

## The site

One static build, no server and no database. `node tools/build.mjs` writes `dist/`:

- `/` the pulse: the pinned post and the purpose, the record (one trace per desk over 24 hours),
  a picker for the reader's own desks, and the bulletin of stories ranked by magnitude.
- `/story/<id>/` one page per story, `/desk/<id>/` one per desk, `/desks/`, `/about/`.
- `/data/pulse.json` the same numbers for machines.

Purpose, which decides the design: people who read different things come away with different
days (the pinned post). The site puts every desk on one sheet, and where groups describe one
story differently it sets each description beside the post that carries it, then states what
is established.

How a number reaches the page: magnitude is the base ten log of views across a story's posts
at their latest reading; a desk's trace is views gained per hour by the posts the grabber
labelled with that desk, spread over the time between readings. A desk's figure for the day
counts posts written in the last 24 hours. The trace will be drawn from X's hourly post counts
(`volume`) once a week of them is in for every desk (**Planned**).

The reader's own desks are kept in their browser only (`localStorage`); nothing is sent anywhere.
Fonts come from Google Fonts. No other third party is contacted. Every page is `noindex` until
the site has a hostname and Sean opens it.

Not built yet: deployment to Cloudflare (waiting on a hostname), a daily brief and an archive,
scheduled editor passes, click-to-load embeds of posts.

## What this replaces

seansooch.dev/monitor/ is a daily briefing in three views. It reads a feed that grokbot both
gathers and writes, published to a Cloudflare Worker (`feed.seansooch.dev`, source on the agent box).
That page keeps running, unchanged, until this site is live. Then `/monitor/` redirects here and the
Worker is retired. Both of those are separate, later changes and need Sean's go-ahead.

## Third parties

Planned, at runtime: none by default. A reader's browser talks to X only if they choose to load a
post's embed. At build and edit time: GitHub, X's oEmbed endpoint, Cloudflare.
