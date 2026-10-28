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

## 2026-10-09: Internet Pulse is the posts themselves; researched stories are a second layer

**Context.** The first public build put seven researched stories on the front page and called the
page the pulse. Sean, on seeing what a research pass produces: that is separate from Internet
Pulse. His brief from the start was that the flagship is the X content that goes viral.

**Decision.** Two layers.

- **Internet Pulse**, the front page: single posts, largest first, from every desk, each under one
  or two sentences from the editor saying what it is. One file, `pulse/current.json`, rewritten
  hourly. The line describes and attributes; it never asserts a claim or adds a fact.
- **Researched stories**, their own page and a short list on the front: slower, sourced, with the
  different-worlds view.

**The rule that nothing appears unreviewed is kept.** The alternative was to show every confirmed,
unflagged post automatically, which would need no model. It was rejected: the grabber's flags are
one party's judgement about private people and minors, and a viral post about a private person is
exactly what an unattended site must not amplify. So a post reaches the pulse only when the
editor lists it, and the build refuses a flagged post even then.

**Consequence for the routine.** This supersedes the previous entry's "the hourly step is a
script". The hourly step is a pulse pass by a model, because someone has to read each post and
write its line. `tools/refresh.sh` stays as the fallback. Sean confirmed the runs are on his
subscription, so the constraint is usage, not dollars.

## 2026-10-09: Edition 2, "Glossy" (the grotesk cut), supersedes Edition 1

**Context.** Sean, the same day Edition 1 shipped: "the data is great but it's super
aesthetically poor." Three things were wrong and none was the data. Three unrelated faces
competed on one page. The stretched traces made every desk look alike, and their wiggle carried
nothing. And a post seen 45 million times was set exactly like one seen 60 thousand times, in a
single column, after a screen of explanation.

**Alternatives.** Drawn on a design canvas with the site's real numbers
(https://claude.ai/artifact/QkMasEZzGBBDWynzbNBCJz), not described: A, a dark halftone wall of
20 desks by 24 hours with dot-matrix numerals; B, a white magazine page with a hairline serif;
C, a chart of every post of the day on one scale, in six group colours. Sean picked B and asked
for type that is easier to read. Three cuts of B followed: B1, the hairline serif kept for
numerals only; B2, a Clarendon; B3, one grotesque throughout. He picked B3 and said to ship it.

**Decision.** B3 as drawn. A white page, black ink, Schibsted Grotesk and nothing else, and red
only for what is outside the reader's worlds, disputed or false. Size carries magnitude: the
largest post leads the page on its own, the next three are set large, six more a step down, and
the rest take a line each. Each desk is a card with 24 bars, one an hour, and the card is the
switch for "this is one of my worlds": a picked card inverts to black. Researched stories are a
ruled line each. Light only; a dark variant was not drawn and is not built.

**How it is built.** The tiers are positions in one list, decided by the stylesheet with
`:nth-child`. Every item carries all that any tier shows, so sorting is moving items and the
page script never redraws one. That replaced three lists and a renderer in the browser.

**Kept though the drawing did not show it,** fitted into the drawing's own shapes: the banner
that says the record is old, and the one that marks a demo build; "gaining" against "averaging"
on a post's hourly figure, because one is measured and the other is not; a post's related posts,
behind a "+2 related posts" disclosure in its byline (the lead shows its own in the open); the
link from a post to its researched story; the outside-your-worlds mark on the lead.

**Dropped.** The record's traces and the story flags on them. The sentence naming the largest
item outside your worlds. The media description under a post on the front page (story pages keep
it). The full text of long posts on the front page: tiers one and two clamp at seven and five
lines, and the post is one tap away.

**Corrected against the drawing.** The drawing set tabular figures on small text. In this face
that widens the full stop and the colon too, so 35.7M read as "35 . 7M" and a name as
"Jurassic . Hansen": the same fault that ruled out B612 Mono in Edition 1. Figures are
proportional. The drawing also labelled a related post "The reply" where the capture says it is
a quote post; the label is now read from the grabber's own links.

**The pages the drawing did not cover** (stories, a story, a desk, the desks, the archive, about)
are set in the same system: the same numerals, rules, labels and cards, with "On the record" as
an inverted panel.

## 2026-10-09: Times on the page are Eastern time, labelled ET

**Context.** Sean, after Edition 2 shipped: "Swap utc to est." Every time on the site read in
UTC (as of 08:12 UTC, a post at 13:25 UTC), which is the capture's clock and not a reader's.

**Decision.** One module, `tools/lib/clock.mjs`, converts an instant to `America/New_York` and
the build prints only what it returns. The label is ET. He wrote "est", but in October New York
is on daylight time, four hours behind UTC and not five: printing "EST" over that hour would be
wrong until November, and printing true EST would be an hour off his own clock. ET is right all
year and the zone's rule does the rest.

**Unchanged.** The 24 hour format. Everything stored: capture file names and run ids, post
ids, `created_at`, `started_at`, `updated_at`, and each `datetime` attribute stay in UTC, so
grokbot and the editor's pass are untouched. The archive now groups a story under the day it
began in New York, which is the day a reader would call it.

**Alternatives.** Converting in the browser to each reader's own zone: the page would then
differ from what was built and audited, and from what Sean sees. A fixed five hour offset:
wrong for seven months of the year.

## 2026-10-10: The crypto desk is retired, and a desk is retired by moving it, not deleting it

**Context.** Sean, to the grabber, which passed it on in `capture/NOTES.md` because it may not
edit the contract: "Drop the crypto category." Crypto was one of twenty desks and is in 46
sweep records. In two days it produced 14 posts, the last captured early on 9 October, and
nothing from it was on the pulse. The rule that a used desk id is "only retired" was written on day one
with no way to do it: the checker, the grabber and the site each read one flat list.

**Decision.** `contract/desks.json` gains a `retired` list beside `desks`. Retiring a desk moves
its whole entry there with `retired_at` and `instead`. `desks` stays the list watched now, so
every reader that knows nothing about retirement is right by default: the grabber sweeps
nineteen, the site draws nineteen, the tests walk nineteen. Only the checker reads `retired`,
to accept the id (and its beats) in a capture started before `retired_at` and refuse it after.
The pages no longer type the number of desks: the build writes it from the list, and
`site.json` says `{desks}`.

**What happens to coin posts.** They are not sought: no desk sweep, no standing query, no volume
series. One that reaches a global sweep on its own numbers is labelled like any other post:
`markets` when it is a market event, `business` when it is a company's story, otherwise `null`.
Dropping the category should not blind the record to a crash the whole internet is watching;
it should stop the site going looking for coin talk. No `crypto` beat was added to `markets`:
that would be the category again under another name.

**Alternatives.** A `retired: true` flag on the desk inside `desks`: every reader then has to
remember to filter, and the one that forgets draws a dead desk. Deleting the entry: 14 recorded
posts and 46 sweeps would fail the checker, or the checker would have to stop checking desks in
old files. Accepting the id forever: the grabber could go on labelling with it. A cut-off by
time was chosen over "any capture already in the repository" because it is a property of the
capture itself and needs no list of files.

**Timing.** `retired_at` is 2026-10-11T02:00:00Z, the first hour after the change was pushed, so
a run already in flight still passes.

## 2026-10-10: One account, one place on the pulse

**Context.** Sean, same message: "optimize so musk posts aren't crowding the whole feed. (He
has the most hits on his posts)". When he wrote it one account held places 1, 4, 7 and 18 of
37. On the evening of 10 October it held 1, 7, 11 and 12 of 45, and three other accounts held
three places each. Upstream, one capture that day kept 13 posts from that account out of 40. The site's purpose is every corner of the internet on one record; an account with a very
large following turns "largest first" into a page about itself.

**Decision.** An account holds one place on the pulse: its most viewed post that the editor
passed. The build applies it (`PULSE_PER_ACCOUNT`, `placesPerAccount`), prints what it held
back, and the about page states the rule, so the page does not pretend to be a raw ranking.
`contract/EDITOR.md` tells the editor to count accounts, not posts, so the freed places go to
other accounts. The grabber keeps at most three new posts from one account in a run.

**Why the build and not only the editor.** Which of an account's posts is largest changes
hourly, the no-model refresh rebuilds the page with no editor present, and a rule a language
model is asked to follow is a rule that is sometimes not followed. The build already ranks by
measured views; this is the same kind of arithmetic. It keeps rather than refuses: a refusal
would leave the page stale until the next pass over a matter the build can settle itself.

**Why one and not two.** With two, the account Sean named would still have held the lead and
one of the three large places on the day he complained. One is also the rule a reader can be
told in a sentence. The cost is real: a reporter who breaks two separate stories in 36 hours
shows once, and the second story has to come through someone else's post or the story layer.
It is one constant, and the choice is Sean's to reverse.

**Alternatives.** X's own author decay (1, 0.625, 0.44, then 0.25 for each further post), which
the grabber's ranking notes describe: it reorders but does not remove, and an account whose
posts are each ten times anyone else's still fills the top. Folding an account's other posts
under its first as related posts: the lead shows its related posts in the open, so this would
put more of the same account at the head of the page, and those posts would carry no line.
Capping only what the grabber keeps: the editor chooses from 36 hours of captures, so a
per-run limit does not bound the page.

**Not checked by the checker.** The three-a-run limit is a rule about what to keep, like the
floors, and lives in `contract/GRABBER.md`. The checker stays the definition of a valid file.

## 2026-10-10: The account rule is applied to each list, not once for the whole site

**Context.** The entry above cut the editor's list once and drew every page from what was left.
A second reader of the change (the test run before shipping) recomputed it on the real pulse:
three of the twelve held posts sat on a different desk from their account's kept post, and the
Tech desk went from one item to none. Its page said nothing from the desk was on the pulse
while the editor had passed a post there with 3.2 million views, and its card on the front
page showed 13 million views for the day.

**Decision.** "One account, one place" holds for each list a reader is shown. The front page
is cut from everything the editor passed. A desk's page is cut the same way from that desk's
items alone. A post held off the front because its account has a larger one elsewhere is
therefore still that account's one place on its own desk.

**Why.** The complaint was one account crowding the feed, and the feed is the front page. A
desk page that reports a quiet desk when it is not is a false statement, which is worse than
a repeated name on a page a reader chose to open. The desks page shows each desk's top line,
so one account can be the top line of more than one desk there; that is what is largest on
each desk and is left as it is.

**Supersedes** the sentence in the entry above that the build "keeps each account's most
viewed post" without saying of which list.

## 2026-10-27: The program: a wire on a free instrument

**Context.** Sean wants the engine to become a months-long, enterprise-grade program: a wire for
AI agents, spike detection, crisis mode, a Divide Index, a health early-warning edition and a
said-versus-voted edition, with a way to charge agents and organizations. `PROGRAM.md` is the
charter. The first question was what to do about X, since every one of those parts reads it.

**Alternatives.** (a) Pay-per-use X API on our own key: the hourly re-read of 400 to 800 posts
alone is roughly 10,000 to 20,000 post reads a day, which at the reported half a cent a post is
$1,500 to $3,000 a month, four to eight times the editor's cost. (b) X Enterprise, reported from
about $42,000 a month. (c) A code grabber on our own key, replacing Grok. (d) Keep grokbot's
existing access (1,000 reads a day, free to Sean) and spend the half of it that goes unused.

**Decision.** (d). No paid X API; grokbot stays the grabber; the read budget is the design
constraint of every phase and each phase states its cost in reads. Sean set this: "I'm not paying
for an x api. i already have grokbot."

**Why.** The input is capped and free; the output (the site, the wire) is uncapped. The
program's cost base is therefore the editor's usage of Sean's subscription ($11 to $13 a day at
API rates) and a Cloudflare plan, and every dollar past that is margin. The risk accepted is a
single point of failure: grokbot's X access. The store and the wire carry a `source` field on
every row so a second instrument can be added later without a redesign; none is built now.

**Also decided here.** Health early warning and said-versus-voted are editions of one platform,
not tracks of their own: the same store, planner, wire and checks, configured for a different
audience. A one-person program ships five things by building one and configuring it twice.

## 2026-10-27: Code plans the reads; Grok makes them; Claude judges

**Context.** Every run from 2026-10-10 to 2026-10-27 is `partial`. The grabber spends 18 to 23
reads of a daytime allowance of 42 and skips fifteen of nineteen desks with "non-hourly desk
skipped after cut order". Item 3 of REPLY-04 (2026-10-10) said so in prose, and seventeen days
later nothing had changed. The cut order lives in Grok's judgement, run by run.

**Alternatives.** (a) A stricter prose contract: tried, without effect. (b) A code grabber: ruled
out above. (c) A tool in this repository writes each hour's read list, in order, with a budget
line each, and the grabber executes it.

**Decision.** (c). `tools/plan-reads.mjs` writes `requests/plan.json` from the latest captures,
`watch.json`, `open.json`, `desks.json` and the reads left in the UTC day. When the file exists
the grabber executes it and records what it did; the standing orders fill only what it leaves
open. Until the tool exists, `GRABBER.md` is the plan and now says that a run which underspends
while desks are due is a failure.

**Why.** A plan a tool wrote is deterministic, testable and readable by Sean; a cut order a model
applied is none of those. It keeps grokbot exactly where it is, reading X and recording what X
said, and moves only the decision of what to read. Crisis mode (phase 4) is a `mode` in the same
file, so the mechanism that fixes today's underspending is the one that later reallocates the
budget in an emergency.

## 2026-10-27: Re-reads follow movement, and counts cover every desk

**Context.** The re-read list stopped at 400 posts (four reads) by our own contract, not X's
limit, and left out 70 to 95 posts a run, up to 24 of them cited in stories. `volume`, the hourly
counts behind the site's baselines, was absent from most runs. The checker allows 1,500
observations and 60 volume series a file, so neither cap was the constraint.

**Alternatives.** (a) Raise the cap and keep re-reading every post every hour. (b) Counts for
every desk every two hours: nineteen reads at even hours, which pushes those runs past the
42-read band cap. (c) Re-read in proportion to movement, and read counts in a rotation.

**Decision.** (c). Up to 800 re-reads (eight reads) by day and 400 overnight; a post flat for six
readings (under 2 percent gained) is re-read every sixth run; a story-cited post is never dropped,
only slowed. Counts: five desks a run in a fixed rotation, so every desk every four hours, 120
reads a day; a desk above twice its baseline gets its counts hourly through the plan (phase 3).
`GRABBER.md` changed in this commit. **Supersedes** "stops at 400 posts (four calls)" and "three
or four desks a run, in rotation" there.

**Why.** A flat post re-read hourly is a read spent on a number that will not change; the same
read on a desk that has not been swept in seventeen days is information. A regular slower
cadence is not a gap in the series. The rotation keeps every run under the band cap while giving
the spike detector a baseline no more than four hours stale, and the planner can tighten it to an
hour where it matters.

## 2026-10-27: The record leaves git before the first paid reader

**Context.** X's developer policy requires stored content to be deleted or modified within 24
hours of its deletion or modification on X. The pulse already honours this (the editor swapped
out a MadridXtra post the hour X stopped returning it), but git keeps every capture's text in
its history forever. Harmless while the repository is private and unread; not once a third party
reads the record through the wire.

**Alternatives.** (a) Redaction commits: the history keeps the text. (b) Keep the repository
private and accept it: not tenable once the wire exists. (c) Rewrite history on every deletion:
breaks grokbot's hourly clone. (d) Move captures to a store (D1 rows, R2 raw files) with an hourly
deletion sweep against X's oEmbed endpoint, import the history first, and rewrite git once at the
cutover.

**Decision.** (d), as phase 1 of `PROGRAM.md`, before any paid reader. The grabber's delivery
becomes a `POST /ingest` with a bearer token; Gate 1 runs on ingest; a 404 from X purges a post's
words, author name, media descriptions and link, keeping its id and its numbers. The one
force-push in the program happens at the cutover, with Sean's approval and grokbot recloning.

**Why.** Git is the right home for the contract, the tools, the editor's files and the site, all
of which are ours to keep forever. It is the wrong home for a record that someone else may order
us to change. The done test is the policy as a test: no `missing` post has words anywhere, and
the newest one was purged within 24 hours.

## 2026-10-27: What is sold and what is never sold

**Decision.** Sold or given away: the editor's lines and stories; scores, indices, baselines,
alerts and timelines; post ids, handles and links; hourly counts per desk; the method behind every
number. Never: the words of a post; media from a post; anything about a post X no longer returns
beyond its id and numbers; per-caller query logs; X content as training data. The site may
display a post (its own public display, kept current); the wire may not copy one.

**Why.** X's policy lets post ids reach third parties (1,500,000 a month) and not copies of
posts. The editor's words and the engine's numbers were the valuable part anyway: they are what
the site is for, and the constraint only says so out loud. "Never" is written down so that no
phase can trade it for a feature.

## 2026-10-27: Everything runs on Cloudflare

**Context.** The program needs a database, object storage, a queue or cron for the sweep, an
HTTP API, an MCP server, and a way to answer `402`. The site is already a Cloudflare Worker.

**Alternatives.** Supabase (used for AA; its trap list is long), Render (the handoff tracker), a
VPS. Each adds a vendor, a bill and an operations surface.

**Decision.** D1, R2, Cron Triggers, Queues and the Agents SDK on the existing Worker. The paid
endpoints use the `402` helpers there; whether the rail is x402 or Stripe's Machine Payments
Protocol is decided in phase 7 when the first customer's wallet is known.

**Why.** One vendor, one bill, one person can run it. The Worker already serves the site and
holds the custom domain, so every phase is an addition to it, not a migration.

## 2026-10-27: Built means the done test passed

**Context.** `ARCHITECTURE.md` marked the pulse pass **Planned** while it had been running 24
times a day for weeks (fixed in this commit). Code landing and a thing working are different
events, and the file only recorded the first.

**Decision.** A part is **Built** when its done test in `PROGRAM.md` has passed. Until then it is
Planned, whatever is in the repository. The done test lives in `tests/` where it can, else as a
tool that prints PASS or FAIL, so Sean can run it in the weekly twenty-minute review.

**Why.** The program is months long and run mostly by agents. The one thing Sean must be able
to trust without reading code is the word Built.

## 2026-10-27: The tools never follow a symlink

**Context.** The grabber's scratch committed on 2026-10-17 (`capture/work/2026-10-17T2308Z/`)
holds `trend_georgia.txt -> trend_Georgia.txt` and four more links. On Linux those are two
names; on a Mac, whose disk ignores case, the link is its own target. Three tools walked
`capture/` with `stat()` and looped (ELOOP), so `npm test` and the build failed here, and the
checkout showed four files changed that nobody changed, which `tools/ship.sh` refuses.

**Alternatives.** (a) Skip `capture/work/` by name. (b) Ask grokbot to remove the links and
wait. (c) Exclude the scratch from this clone and change nothing. (d) One shared walk that
never follows a link, plus (b) and (c) as the interim.

**Decision.** (d). `tools/lib/files.mjs` is the one walk, used by the build, Gate 1 and Gate 2:
`lstat`, symlinks skipped, regular files only, with `tests/files.test.mjs` pinning it. This clone
excludes `capture/work/` through a sparse checkout (`git sparse-checkout disable` undoes it)
until grokbot deletes the links (REPLY-05, item 6), and the contract now forbids symlinks and
case-only duplicate names anywhere in the repository.

**Why.** A walk looking for `HHMMZ.json` has no business following links, whatever the disk.
The scratch is the grabber's to keep; the editor's tools should not be able to be broken by it.

## 2026-10-27: The other platforms are polled once a week; X stays the instrument

**Context.** Sean holds ScrapeCreators credits from another of his bots. ScrapeCreators is a
scraping API, not an official one: one credit a request for most endpoints ($47 for 25,000,
$497 for 500,000), covering TikTok, Instagram, YouTube, Reddit, Threads, Bluesky, X and more,
with keyword search, trending feeds, comments and video transcripts; its terms put platform-rules
risk on the user. The first entry of this date said a second source is designed for, not built.
Measured today: YouTube's oEmbed answers 200 with the title for a real video and 400 for a fake;
Bluesky's embed endpoint answers 404 for a fake post; TikTok's oEmbed answers 200 for any id;
Reddit's blocks unauthenticated calls; Instagram's redirects to the Graph API, which needs a
token.

**Alternatives.** (a) Hourly on six platforms with re-reads, as X is read: about 2,000 credits a
day, $60 to $120 a month, and a second time series to keep honest. (b) Nothing until the program
is further along. (c) One poll a week, no re-reads, under 100 credits, keyed to the week's X
stories and the medicine desk's claims. (d) X through ScrapeCreators as well.

**Decision.** (c), as phase 1b of `PROGRAM.md`. Sean: "use the scrape creators credits but
incredibly limited with X driving the main discussion. We can run like 1 poll a week for the 6
other sites to save credits." Not (d): paying for scraped X data is against X's rules and the
first constraint in spirit. A Worker cron on Sundays once the store exists; the key is a Worker
secret Sean sets himself; the poll stops at 100 credits and says so. **Supersedes** the sentence
"A second source is designed for, not built" in the first entry of this date; the rule that every
row carries `source` stands.

**Why.** The hourly pulse is X's. The question the other platforms answer is a weekly one: where
else did this week's stories go, and what went big that X did not carry. A weekly cross-section
answers it for a few hundred credits a month, so the cost base does not move, and the one new
failure mode, a scraper going dark, costs a Sunday page and never the pulse. The health edition
gains the most: health rumors spread on TikTok and Instagram more than on X, and the transcript
endpoints let an editor that cannot watch a video read what it says.

## 2026-10-28: The budget is a number in the record, and the plan is a file a tool writes

**Context.** Phase 0 of `PROGRAM.md`. The reads a run spent lived only in `run.reason` as a
sentence ("21 X reads this run (936 to 915 left today)"); the budget's numbers lived only in
`GRABBER.md`'s prose; the cut order lived in Grok's judgement, and the report over 2026-10-21 to
2026-10-27 reads 0 of 7 days pass (reads 462 to 488, 4 of 19 desks at cadence, counts for no
desk). Sixteen requests in `open.json` had each been answered once and never removed, so every
run listed sixteen skipped request sweeps.

**Alternatives.** (a) Parse the sentence forever. (b) Have grokbot run the planner itself at the
start of each run: freshest inputs, but CI forbids a capture commit touching `requests/`, so the
plan a run followed would not be on the record. (c) Numbers as fields, the budget as one JSON
file, the plan written on our side after every capture and committed, the grabber executing it.

**Decision.** (c). `run.reads`, `run.reads_left`, `run.plan` in every capture (a warning until
2026-11-04, then an error). `contract/budget.json` is the one place a number is changed;
`GRABBER.md` says the same in words. `tools/plan-reads.mjs` writes `requests/plan.json` in
`tools/refresh.sh` after every capture and at the end of every editor pass; it is deterministic,
so the plan any run was given can be regenerated with `--at`. The grabber executes it
(`contract/PLAN.md`) and falls back to the standing orders when it is missing or stale. The
planner's own rules: the re-read list is `watch.json`, then posts under six hours old, then posts
gaining 2 percent, then on a fourth hour the rest of the day; a post flat over six readings is
read on one run in six, chosen by its id so the slowed posts spread evenly; counts go to the five
stalest desks; a request is asked while under three days old and unanswered; the cut order is
`budget.json`'s and never touches the re-read list or the counts. The sixteen answered requests
were removed and `EDITOR.md` now tells each pass to remove answered ones.

**Why.** A number can be summed and judged; a sentence has to be parsed and hoped for. A plan
written on our side is on the record beside the capture that followed it, which is what makes
"did the grabber do what it was asked" a question with an answer. The first real plan asks for
42 reads where the grabber was spending 21: nineteen desks, five desks' counts, 264 re-reads in
three reads with 221 flat posts waiting, then discovery.
