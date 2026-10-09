# Decisions

Append only. A later entry may supersede an earlier one; the earlier one is never edited.

## 2026-10-09: Its own site and repository, not a page of seansooch.dev

**Context.** Monitoring the Situation was a page of seansooch.dev (`/monitor/`, three views) that
read a daily briefing from a Worker. Sean wants it rebuilt around an Internet Pulse section, as its
own site on Cloudflare, with Grok gathering from X and Claude writing and building.

**Alternatives.** (a) Keep growing `/monitor/` inside the portfolio repo. (b) A new site that still
reads the existing Worker feed. (c) A new repository that holds the handoff, the record and the site.

**Decision.** (c). The portfolio repo is generated from several off-repo sources and is shared with
the lab pipeline; an hourly data flow does not belong in it, and three views of one page would mean
three renderings of everything new. A new repository gives the project one owner per directory.

## 2026-10-09: Git is the bus between the two agents

**Context.** The grabber and the editor run in different places on different schedules and need a
handoff neither has to be awake for.

**Alternatives.** (a) The existing pattern: the grabber PUTs to a Worker with a bearer secret, backed
by KV. (b) Object storage with an API in front. (c) Files in a shared git repository.

**Decision.** (c). grokbot already works through GitHub. A repository gives history, diffs, an
archive, and CI on every delivery for free, and needs no new secret on either side. The editor's
scheduled runs always have a checkout; they do not always have network access to a custom API.
Cost: the repository grows by roughly one small JSON file per hour. Captures are working data, so
old ones can be pruned from the tree if that ever matters.

## 2026-10-09: The grabber never writes prose; the editor never supplies a post

**Context.** Today one agent gathers, judges and writes, so nothing checks it.

**Decision.** Split the roles at the capture file. The grabber records posts, numbers and X's own
text verbatim. The editor does the grouping, the research and every sentence. A verifier then sits
between generator and publisher for both kinds of error, and neither is produced, approved and
published by one context.

## 2026-10-09: Two gates, and neither trusts the grabber's own word

**Context.** A model reading X can return posts that do not exist, or real posts with invented
numbers. Sean's standing rule is no invented facts about real people.

**Decision.** Gate 1 is structural and runs on the grabber's side before it pushes
(`tools/check-capture.mjs`). It includes one check that is more than structural: the creation time
encoded in an X id must match the record's `created_at`. Gate 2 runs on the editor's side: X's public
oEmbed endpoint is asked whether each post exists and what its author and text are. Both were tried
on 2026-10-09 against a real post and a random id before being written down.

Numbers cannot be confirmed the same way. They are guarded by being a time series (a figure that
jumps backwards or sideways shows) and by the reader always having the link to the post.

**Not done on purpose.** The list of lookups that are expected to return `not_found` is not kept
anywhere in this repository, because the grabber reads this repository. Gate 2 identifies them
without a list.

## 2026-10-09: The checker is hand-written, with no JSON Schema file

**Alternatives.** A JSON Schema plus a validator library.

**Decision.** One dependency-free script. The rules that matter most (id against date, references
across files, an observation inside its run) are not expressible in JSON Schema, so a schema file
would be a second, weaker definition that could drift from the first. The prose reference
(`contract/CAPTURE.md`) defers to the checker, and the example file is checked by the test suite.

## 2026-10-09: A failed run still writes a file

**Decision.** `run.status: "down"` with a reason is a valid capture. A failure recorded as data can
be counted and charted; a missing file cannot be told apart from a schedule that stopped.

## 2026-10-09: Twenty desks, kept as data in one file

**Context.** The first contract carried seven desks: the six sectors of the old page (which Sean
said he had listed off the top of his head) plus one for the internet itself. Sean asked for the
set to be complete. Yesterday's feed shows the cost of a short list: a hurricane was filed under
Medicine and a studio merger under Pop culture, because nothing closer existed.

**Alternatives.** (a) Keep six or seven broad sectors and let stories sit awkwardly. (b) A
newspaper's section list. (c) Free-form tags from the grabber. (d) A fixed set of desks drawn from
both a newspaper's sections and the communities that actually exist on X, with a second level of
beats inside each.

**Decision.** (d): twenty desks in six groups, each with beats, listed in `contract/desks.json`.
A newspaper's list alone misses what is native to the platform (crypto, gaming, AI as its own
world, creators and memes, everyday-life arguments, clips shared for delight). Free tags cannot be
swept on a schedule or charted over time. The list is data, not code, read by the checker, the
grabber and the site, so changing it is one edit.

Choices inside it:

- **AI is split from tech**, and **crypto from markets**: each is one of the largest communities on
  X with its own vocabulary and its own virality.
- **World, defense, justice and disaster are separate from politics.** The old page's Politics
  sector held all of them. Defense is its own desk although it overlaps with world, because the
  military and open-source analysts are a distinct community; the boundary is written into both
  desks' `not_here`.
- **Sports stays one desk** with fifteen beats rather than a desk per league, so the top level does
  not change with the season.
- **Entertainment and music are two desks**, celebrity sits inside entertainment. Three desks
  (film and TV, music, celebrity) put too many posts on a boundary.
- **Life and offbeat exist** because a large share of what goes viral has no news in it at all.
- **Obituaries are not a desk.** A death belongs to the desk of the person's field.
- **A post has one desk.** A story can sit on several; that is the editor's call, made later.
- **Cadence and floors differ by desk** (1, 2 or 4 hours; floors from 10,000 to 50,000 views). They
  are starting values chosen without capture data and will be tuned from the first week of it.

**Supersedes** the seven-desk list in the first commit. No capture had been delivered against it.

## 2026-10-09: Discovery moves from X's story clusters to the repost stream

**Context.** The first real capture (2026-10-09T0552Z) was honest and well formed, and thin: 153
discovered posts totalling 38.2 million views, the largest 3.35 million, median age 12 hours, no
post attached to any of 40 trends. X's search has no engagement sort and no minimum-likes
operator, so the grabber had taken every candidate from X's own story clusters.

**Alternatives.** (a) Accept story clusters as the only source. (b) Seed lists of large accounts
read one timeline at a time (too many reads against a limit of 1,000 a day). (c) Sample the live
repost and quote streams, whose results carry the post being reposted and are therefore weighted
by current spread; follow quote, reply and media-source references to origins; attach posts to
trend names; read sensor accounts many to a query; keep clusters as one source of five.

**Decision.** (c), written into `contract/GRABBER.md`, with a probe first: none of these
techniques has been run against X by this project yet, so the grabber tests each one and records
what X returned before depending on it. The improvement is measured by a side by side run, not
assumed.

**Also decided.** The capture gains three optional parts: `media_source` on a post, `x_stories`,
and `volume` (hourly post counts per desk from X's counts endpoint). `volume` is intended to drive
the site's main chart: it is a measured count per desk per hour, where views gained between two
readings is only an interpolation. Replies and quote posts are fetched on the editor's request
instead of by default, because reads are the scarce resource.

## 2026-10-09: The repost stream was not the lever; references were

**Context.** The side by side run (2026-10-09T0615Z, about 2 AM Eastern) measured each source
by what it returned per read. The earlier entry bet on sampling the repost stream. Measured:
the global repost stream was the weakest source (one read, six posts kept, median 81,000 views).
Following references cost no reads and was the strongest (eleven origins, median 994,000). Sensor
accounts and trend names came next. Story clusters, the old method, still found the largest fresh
post. Old and new shared no posts at all.

**Decision.** Reorder the sources in `contract/GRABBER.md` by measured yield and stop treating
the global repost stream as the main one: one page of it is 25 reposts from a single minute, too
small a sample of the whole network. Keep it where the pool is narrow (a trend name, a desk).
Three rules added from what the run exposed: a pace floor for posts under three hours old (a
floor on totals discards a young post before it has its views); counting how often a post is
referenced across a run; flagging an origin much older than its copy.

**Not concluded.** Whether any method finds the top of the distribution among fresh posts. At
2 AM the fastest young post gained 60,000 views an hour. The comparison is repeated in the United
States evening and a daily scoreboard is kept, so the gather is judged by the day.

**Also.** One read of X's counts endpoint returned 167 hourly counts for a desk query, so a week
of history for all twenty desks costs twenty reads. The site's record will be drawn from these
counts once they are in.

## 2026-10-09: The purpose is the pinned post, and it decides the design

**Context.** Sean set the site's scope with one post, to be pinned: "People live in different
worlds" (Elon Musk, 20 Feb 2026, quoting "Your information diet determines your reality"). The
site exists to reconcile the different-worlds problem that comes from each reader's own feed.

**Decision.** Three things follow from that and are built into edition 1:

- The post is the masthead, set larger than the site's own name, with the site's answer beside it.
- Every desk is always on the page. A reader can mark the desks they already follow, and the page
  then counts what is outside them. Nothing is hidden or filtered to taste; the feature points
  outward.
- A story can carry `worlds`: how each group describes it, each beside the post that carries that
  description, followed by `common`, what is established. The editor writes `common` from
  reporting and says plainly when a claim rests only on posts.

## 2026-10-09: Edition 1, "Record Section"

**Alternatives.** A dark war-room dashboard (the obvious reading of "monitoring the situation");
a patient monitor (too close to the Read This edition); a trading terminal; a weather map.

**Decision.** A seismic network's record section: one trace per desk on a shared time axis, and
a magnitude for every story. The log scale is the honest one for attention, which spans ten
thousand to a hundred million views, and it gives each story one memorable number (7.0 is ten
million). Ground: drafting vellum, a cool blue-grey, with white sheets. Two colours only: signal
blue for what is live or large, brick for what is disputed or false. Three faces with three jobs:
Libre Franklin for headlines and for the internet's own words, STIX Two Text for the editor's
sentences, B612 (drawn for cockpit displays) for everything the instrument measured.

The wiggle of a trace carries no information; only its height does, and the about page says so.

**Magnitude** is the base ten log of total views across a story's tracked posts, to one decimal.
It was chosen over a weighted engagement score because a reader can check it in their head.

## 2026-10-09: The first bulletin, and what was left out of it

Seven stories from the first two captures, each post confirmed against X and each claim checked
against reporting. Left out on purpose: the night's biggest sports post (it shows a stadium
employee, a private person); a politics item whose central quote I could not confirm in any
reporting; the vaccine-clinic story, because the capture held only one side and the facts were
not confirmed (asked of the grabber); a markets post spreading mainly through jokes about a
nationality. One cited post was swapped out because its text gave identifying details of a
private person accused of a crime.

## 2026-10-09: Every captured post is checked, and only confirmed posts count

**Context.** The architecture review found that desk traces and totals were computed from every
captured post, while only the posts cited by stories had been through Gate 2. The diagram said
"confirmed posts only" and the code did not do that.

**Decision.** Gate 2 now runs over every captured post (`--captures`), and the build counts only
posts X confirmed. The first full pass confirmed 272 of 274; X withheld two behind a login, and
those count for nothing. The first attempt reported 24 mismatches, all false: X's embed drops the
leading @mentions of a reply and prints media links differently from the API. The comparison now
uses only the characters of the words, to 200 characters, and tests pin both the false mismatches
and a real one.

**Kept on purpose.** Posts flagged as showing private people or minors still count in a desk's
total. They are real attention and a sum reveals nothing about them; no word, name or link from
them reaches a page.

## 2026-10-09: A Worker serving static files, not a Pages project

**Context.** Sean chose `situation.seansooch.dev` and asked for the deploy. Every other site of
his is a Pages project deployed by direct upload.

**Alternatives.** Pages, with the hostname attached by hand in the dashboard, because wrangler
has no command for a Pages custom domain and its sign-in cannot edit DNS.

**Decision.** A Worker with static assets and a custom-domain route in `wrangler.jsonc`. One
`wrangler deploy` uploads the files and creates the DNS record and certificate, with the sign-in
already on the machine and nothing done by hand. Unknown paths answer 404 with the site's own
page, where Pages answers 200 with the home page. `workers_dev` is off so there is exactly one
public address. This is also where Cloudflare now points new static sites.

**Consequences.** The deploy notes for his other sites (Pages receipts, `--branch=main`) do not
apply here. `tools/ship.sh` is the only way to ship: it refuses a dirty tree, failing tests and
a demo build, and then compares the live page's timestamp with the build's.

## 2026-10-09: Smaller choices, recorded

- **Search engines are kept out for now** (`X-Robots-Tag: noindex` and `robots.txt`). Publishing
  and being indexed are separate steps and Sean has asked only for the first.
- **Google Fonts is the one third party at runtime.** Self-hosting the three families would remove
  it and is worth doing; it was not done on day one.
- **An enforced Content-Security-Policy.** Everything on a page is this site's own files, so the
  policy allows nothing else except the fonts. Inline style attributes are allowed because the
  record positions its flags with them; inline script is not.
- **The page says when it is old.** A static page cannot know the time, so the page script compares
  the build's timestamp with the reader's clock and shows a notice after three hours.
- **CI recognises a capture commit by its `capture:` subject**, and only on push. It is a guard
  against accidents, not against a determined writer; both agents commit as the same account.
- **A demo build skips Gate 2**, because its posts are invented. It marks every page and leaves a
  `DEMO` file that the deploy script refuses.

## 2026-10-09: The ship script is not called deploy.sh

A guard on Sean's machine blocks any command that runs a path ending `tools/` + `deploy.sh` while
his `~/edge` repository has uncommitted changes. It is written for that repository and does not
look at which one the command is in. This project's script is named `tools/ship.sh` so the two do
not collide; the guard is untouched and still protects `~/edge`.

## 2026-10-09: grokbot runs the clock; a recruited Claude agent does the editor's pass

**Context.** Sean wants one schedule. grokbot already runs hourly and can recruit Claude agents.

**Alternatives.** A Claude cloud routine on its own timer (my first recommendation); a GitHub
Action calling the API on each capture push; grokbot doing the editor's work itself.

**Decision.** grokbot's scheduler recruits a Claude agent after the capture of every even hour.
The risk in letting the party being checked start its own checker is handled in the repository,
not by trust: the brief is a file passed word for word (`contract/EDITOR-BRIEF.md`); the
procedure is a file the agent reads itself (`contract/EDITOR.md`) and it tells the agent to
ignore anything else it was told; a pass may write only stories, requests, the ledger and its
log, and CI fails a `bulletin:` commit that touches anything else; the build refuses a post X
has not confirmed. grokbot doing the editing itself was rejected outright: the gatherer and the
checker must be different.

**Consequences.** Each pass is a fresh agent with no memory, so `editor/LOG.md` carries state
between passes. A scheduled pass cannot change the contract, the tools or the site; those stay
with the main editor session. Unattended publishing about real people is the largest risk the
project takes on, which is why `EDITOR.md` spends most of its length on what never goes on the
site and ends with a checklist.

**Also.** The bulletin holds stories that began in the last 48 hours; older ones keep their page
and move to `/archive/`. Without that, an unattended site only ever grows.

## 2026-10-09: The hourly step is a script; a model runs only to write

**Context.** The entry above had a Claude agent after every even hour. I then proposed splitting
that into an hourly light pass on Sonnet and a full pass four times a day on Opus. Sean asked
whether the Opus pass was needed, what it was for, and what it cost. He also said both agents may
use Cloudflare for this project.

**Decision.** Supersedes the cadence and the shipping path in the entry above; the safeguards in
it stand.

- **Hourly: `tools/refresh.sh`, no model.** Everything the light pass did that mattered each hour
  is deterministic: ask X about new posts, record the answers, rebuild, ship. grokbot's routine
  runs the script after each capture.
- **Four times a day: the editor's pass**, the only step that needs judgement and so the only one
  that uses a model. It is what adds and updates stories; without it the bulletin never changes.
- **Sonnet first.** Recommending Opus was a judgement, not a measurement. The pass starts on
  Claude Sonnet 5.5, the main editor reviews its first day of stories, and the model changes only
  if those stories show a reason.
- **Agents ship directly** with `tools/ship.sh`. A GitHub Action holding a Cloudflare token was
  drafted so that neither agent would need Cloudflare access; with Sean's go-ahead it is not
  needed, and one way to ship is better than two.

**Cost, estimated at list prices before any pass has been measured.** A writing pass re-reads a
growing context on every turn, so cache reads dominate and the two models cost closer than their
list prices suggest: roughly $0.60 to $2 a pass on Sonnet and $1 to $3 on Opus. Four a day is
about $4 on Sonnet or $7 on Opus. An hourly model pass on top would have added about $5 a day
for work a script does. If the runs use Sean's subscription login there is no per-pass charge;
they draw on his usage limits instead. grokbot records the real cost of every pass in
`capture/EDITOR-RUNS.md`, which replaces these estimates.
