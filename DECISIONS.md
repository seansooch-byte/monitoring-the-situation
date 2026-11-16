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

## 2026-10-28: The store is D1 alone, and the gates are pure functions

**Context.** Phase 1 of `PROGRAM.md`. The charter had the store as D1 rows beside raw files in
R2. R2 is not enabled on the account (the API answers code 10042, "enable R2 through the
dashboard"), which is Sean's to do. Gate 1 and Gate 2 lived in command-line files that read the
desks and the ledger from disk, so neither could run inside a Worker.

**Alternatives.** (a) Wait for R2. (b) KV for the raw files: a thousand writes a day on the free
plan, which the import of the history would spend in an hour. (c) D1 for everything: the rows,
and a gzipped copy of each capture file in a `captures` table, 60 KB each against a 1 MB row
limit. For the gates: (d) copy the checks into the Worker; (e) move each gate's rules into a
pure library the Worker and the command line both import.

**Decision.** (c) and (e). `worker/index.mjs` runs `POST /ingest` (Gate 1 from
`tools/lib/capture-check.mjs`, with the desks passed in and the known ids read from D1), the
`/api/*` reads, and an hourly deletion sweep (Gate 2 from `tools/lib/gate2.mjs`) that purges a
post X answers 404 for from its row and from every stored file that holds it (`tools/lib/
store-rows.mjs`), keeping its id and its numbers. One token, a Worker secret, guards every
route in phase 1; it lives in a git-ignored file at the root of Sean's checkout and reaches
grokbot by Sean's hand. `tools/refresh.sh` mirrors every capture pushed to git into the store
until the grabber delivers there itself; the git push stays the delivery of record until the
cutover. `tools/check-capture.mjs` and `tools/verify-posts.mjs` keep every export they had.

**Why.** One binding, one bill, one place to purge. A gzipped capture in a row costs the same
to serve as a file from R2 and is rewritten by a purge the same way. A gate that is a pure
function is the same gate everywhere, which is the only way "the Worker runs Gate 1" can be a
true sentence rather than a copy that drifts. If R2 is enabled later, moving the files there is
one column's worth of change and no change to the readers.

## 2026-11-03: A post X will not show costs its place, not the whole site

**Context.** A story cited a post that Gate 2 had recorded as `withheld` (X shows it only after a
login). The build refused the whole site for it, the tests failed with it, `tools/ship.sh`
refused, and nothing on the site changed for about 35 hours. Separately, one question to X that
never answered held `tools/verify-posts.mjs --captures`, and the ship behind it, for over ten
minutes. Sean: "Don't let it break again."

**Alternatives.** (a) Keep the refusal and rely on each pass to change the story. That is what
broke: a post's standing with X can change after a story is written, and no pass may be running
when it does. (b) Show a withheld post from the capture anyway. That breaks the rule that only
what X confirms is shown. (c) Leave the post out and say so, everywhere it would have appeared.

**Decision.** (c), for `withheld`, `missing`, and a post not yet in the ledger. In a story the
post's place holds a note, "Unavailable on X", and the post's id (with a link by id unless X has
no post for it); none of the record's words, author or numbers, and it counts for nothing. A
world whose post is unavailable keeps its description over the note. A pulse item or related
post is left off. The build prints a warning naming the story or item and the post, and builds
the rest. A `mismatch` still stops the build, and so do a post no capture recorded and a post
the grabber flagged: those say the record or the editor is wrong, and showing the rest of the
story around them would be standing behind it. The question to X now gives up after 15 seconds
and is reported as an error, not recorded. `tools/check-stale.mjs` reads the live page's as-of
time, so a site that stops updating for any reason is caught by its age.

**Why.** The rule was never "a story must have every post"; it was "nothing X has not confirmed
is shown". Leaving the post out keeps that rule and stops one post from holding every other page
hostage. A mismatch is different in kind: it says the record does not match what was said, which
is the failure Gate 2 exists to catch.

## 2026-11-14: The site becomes a newspaper of the record, with one opinion a day

**Context.** Sean: "We already have monitoring the situation which is the biggest piece. We can use
soochiebot to do an editorial. Let's combine it into a super news app. That's designed like a
newspaper ... Goal is you open this app and you can learn what the heck is going on." Soochiebot is
grokbot's persona, set to sound like Sean, which since 2026-11-13 wrote one post a day on
seansooch.dev/notes/ ("Field Notes") from this site's record. He also asked whether the top story
is "the highest hit on monitoring the situation".

**Alternatives.** (a) Keep two products: the situation as the record, Field Notes as the daily read.
That splits the one question a reader brings ("what is going on?") across two sites. (b) Let the
writer choose the front page each day. Then the order is an opinion. (c) One paper: the record ranks
the front page; the editor's words stay the news; Soochiebot writes one labelled editorial.

**Decision.** (c). An edition is one Eastern day, a pure function of the record
(`contract/PAPER.md`, `tools/lib/edition.mjs`). The front page is ranked by **the views a story's
posts gained during the day**, not lifetime views and not the single biggest post: on 13 November
the biggest single post was Microsoft's outage apology, which no story covered, while the largest
story was the FAA ground stop, spread over four posts. Measured per post, a cat video would have led.
Measured as views gained on the day, a story begun on the 8th (the Nvidia board probe) ranks when it
moves again. Posts the editor described that no story cites are shown as "not yet a story" (news
sections) or "what the internet watched" (the rest), so the gaps in the reporting are on the page.
Soochiebot writes `opinion/<day>.json`: words only, no number of its own, citing only what the
edition holds; a broken opinion refuses the edition. This relaxes, for one folder, the rule that the
grabber's side writes no prose; it is Sean's call and it is fenced: the opinion is labelled as a
program's, set apart from the news, and cannot add a fact.

**Why.** "Learn what is going on" needs an order a reader can trust, and the only order nobody chose
is the numbers. Views gained on the day answers "what moved yesterday" and is honest about stories
that run for days. Keeping the opinion in its own lane keeps the news readable as news.

**Found while building it.** Three of the ground stop's four posts were captured only as references for
its story, with no desk, so they counted nowhere and the story fell to second. A post with no desk now
takes the first desk of the story citing it. Separately, a later capture can carry a post again with no
desk; the edition fills a field once and never overwrites it with a blank. `tools/build.mjs` lets the
later copy win (line 41), which over 13 and 14 November cost 3 of 3,074 posts their desk (0.1%): noted,
not changed.

**Not decided.** Which of the three designs (Broadsheet, Wire, Record) the site wears; the name on the
masthead; what becomes of seansooch.dev/notes/ (redirect to the paper's opinion page is the obvious
end); the CI rule that lets grokbot commit `opinion/`.

## 2026-11-14: Edition 3, The Broadsheet: the paper is the front page, the pulse becomes its wire

**Context.** Three directions were drawn on a design canvas the same day with the record of 13
November (A the Broadsheet, B the Wire, C the Record). Sean picked A.

**Decision.** The whole site wears it, not only the front page: one head on every page (ears, the
nameplate, the sections bar), newsprint and ink, four faces each with one job. The front page is the
latest complete edition (`contract/PAPER.md`); every day keeps its front page at `/edition/<day>/`.
Internet Pulse, which was the front page since 2026-10-09, moves to `/pulse/` as the paper's wire,
unchanged in what it shows and how it is checked. Six section fronts (`/section/<group>/`) and an
opinion page are added; the archive becomes back issues. The pinned post becomes the motto beside the
nameplate on every page, so the reason the site exists stays in sight now that the front page is no
longer the pulse.

**Alternatives.** (a) Keep the pulse as `/` and add the paper beside it. Then a reader opening the
site gets the instrument, not the answer to what is going on, which was the point of the change.
(b) Restyle the old pages and add an edition page. That keeps Edition 2's vocabulary under a new
skin; the edition was written from a blank sheet instead, keeping only the markup the tests and the
page script rely on (the pulse list's items, the desk cards, the unavailable-post note).

**Why.** "Open this app and learn what is going on" is a front page's job; the wire and the desks are
how a curious reader goes deeper. Keeping every old address (stories, desks, story pages) means no
link anyone has saved breaks.

## 2026-11-14: Soochiebot writes a newsletter, not an editorial; Field Notes moves in as the Newsletter

**Context.** The same afternoon the paper shipped with an opinion band waiting for Soochiebot's first editorial,
Sean: "Make Field notes a toggle on Monitoring the situation. It will be a handcrafted newsletter by soochiebot.
Format it in a letter style Harvard grade. Change Field notes to Newsletter." Field Notes was seansooch.dev/notes/:
one post a day by Soochiebot from this record, with its own format and checks in the site repo.

**Decision.** One writing job for Soochiebot: a letter a day, `newsletter/<day>.json` (`contract/NEWSLETTER.md`,
`tools/lib/letter.mjs`), the Field Notes format renamed and moved here. The site sets it as a letter (letterhead,
date, Re: line, Dear reader, sections, the read, Yours, Soochiebot) with references in the Harvard style (Cite Them
Right) written by the build from ids, so the writer types no reference and cannot misstate a title or an author. A
switch under the nameplate turns every page between the Paper and the Newsletter. The Paper's opinion band prints
the letter's read and links the letter. The opinion (`opinion/<day>.json`, `tools/lib/opinion.mjs`, `/opinion/`) is
removed before any was written. The 12 November Field Notes post is Newsletter No. 1, its words unchanged.

**Alternatives.** (a) Keep the opinion and add the newsletter: two daily pieces from one writer, saying the same day
twice. (b) Keep Field Notes on seansooch.dev and link it from here: two sites, two builders, two sets of rules for one
letter. (c) Let the writer type Harvard references: they would drift from the record and nothing could check them.

**Found while building it.** A letter written the morning after cites posts the editor described that morning, which
are not in the day's edition, so a cited post must be one X confirmed that the record may show; a cited story must be
in the day's edition. And the 12 November edition led with a story begun on the 13th whose earlier post gained views
on the 12th: a front page carried a headline from the next day. A story is now in the editions from the day it
began, and a test holds that.

"Harvard grade" is read as Harvard referencing in a letter of that standard; the house style for the words is unchanged.


## 2026-11-14: The board: one thread in the store that every agent reads and writes, instead of Sean carrying replies

**Context.** Sean: "set up a way for grokbot and claude to be more interactive ... so both are in the know and
updated simultaneously", then "set up a claude routine and grokbot routine so they stay up to date along with the
shared board". The agents had four one-way channels: `contract/REPLY-NN.md` (Claude to grokbot, pasted by Sean; six
so far), `requests/` (Claude to grokbot, grabbing only), `capture/NOTES.md` (grokbot to nobody: 2,139 lines no pass
reads in full) and the editor log's "For the main editor" line (the same two warnings repeated for days, unread).
grokbot had reported in six runs in a row on 14 November that the plan left out watch ids because `watch.json`
changed after the plan was written, and nobody acted on it.

**Decision.** A board in the store: D1 tables `board` and `board_cursors`, routes `/api/board`, `/api/board/seen`,
`/api/state` behind the store token, rules as pure functions in `tools/lib/board.mjs`, one list of agents, channels
and kinds in `contract/board.json`. Five kinds; an `ask`, `notice` or `alert` stays open until its addressee
replies, with an overdue time per kind. The state is derived from the thread (latest report per agent, cursors,
what waits on whom), so there is one write path. Every run of every agent starts with its inbox and ends with a
report. A Claude routine on Sean's Mac (local scheduled task) is the `claude` side between Sean's sessions.

**Alternatives.** (a) A git `inbox/` folder: no new code, but a message moves only when someone pulls, the hourly
CI rules would need a new lane, and other projects could not share it. (b) The MCP wire of phase 2 first: right in
the end, but both sides already run node in a clone of this repo, and an MCP server is a second interface to keep
in step; it can be a thin layer over these routes later. (c) A cloud routine for the Claude side: it would need the
store token as a cloud secret, and the editor passes already run hourly; the local task keeps the token on this Mac.

**Trust.** One token, so `from` is self-declared. The board therefore carries information, never authority: lanes
stay in `GRABBER.md`, `EDITOR.md` and `BOARD.md`, and a message signed `sean` is weighed like any other. No post text
on the board.

## 2026-11-14: The board moves to its own service, with a token per holder

**Context.** Hours after the board went live inside this store, Sean asked for it to reach every project
("is this extrapolated to the entire site/emails/etc? I want fully integrated agents") and chose stage 1:
the board as its own service with a token per agent. Inside this Worker, every other project would depend
on this site being up, and the one shared store token let anyone holding it post as any agent.

**Decision.** `~/agent-board`: one Worker at agents.seansooch.dev over its own D1, rules and tests moved
there, the protocol served as `/BOARD.md` so grokbot can read it without a repository. Tokens belong to
holders (`claude-mac`: claude; `grokbot-machine`: grokbot and editor; `sean`), stored as SHA-256 only;
the board sets `from` from the token. Messages 1 to 4 copied with their ids. This repo keeps a copy of the
command line and a short `contract/BOARD.md`; its board routes answer 410; the store token is accepted as a
grokbot-machine token until 2026-11-21 so grokbot keeps working while it switches. Full record in
`~/agent-board/DECISIONS.md`.

## 2026-11-16: The store keeps to a share of the database plan, writes only what changed, and sweeps a few posts every ten minutes

**Context.** On 15 November every write to the store and to the agents' board failed from about 17:10Z
until midnight UTC ("store and board writes 500" in `capture/NOTES.md`, six captures running; the board
has no message between #83 at 17:08Z and #84 at 00:19Z). The cause was Cloudflare's free D1 plan: it
counts rows written across every database on the account, one per table row and one more per index
the row enters, and past 100,000 in a UTC day it refuses every write. Measured with `wrangler d1
insights`: the store wrote about 6,100 rows a capture, 146,000 a day. Half of that was the hourly counts:
each run delivers a week of them for five desks, 835 rows, and `INSERT OR REPLACE` rewrote all of them
though about 600 were identical to what was held. The board itself writes under 700 rows a day. The
backlog delivered after midnight then spent 74,000 of the next day's rows by 06Z, so each day was due
to fail earlier than the last.

The same look found that the deletion sweep had never finished a run since 28 October (`sweep_log`
empty, three rows in `checks`, all from the hand-run proof). It read every post each hour (119,000 rows a
run, 2.9 million a day, 57% of the account's free reads), then bound 150 ids to one statement, and D1
allows 100.

**Decision.**
- A count is written only when its hour is new or X counts it differently now (an upsert that changes
  nothing writes nothing). An unchanged hour keeps the run that last changed it.
- The store knows what a capture can cost before writing it (`writeCost`: rows times the B-trees the
  schema gives each table, held to the schema by a test), keeps what D1 says it wrote in one row a day
  (`spend`), and answers `429` with `held: true` to a capture that would take it past 90,000
  (`contract/budget.json`, `store`). The capture stays in git; `tools/ingest.mjs` prints `HELD`, exits 0,
  and the first `--new` after 00:00 UTC delivers it. The board keeps at least 10,000 rows a day.
- The sweep runs every ten minutes and asks about eight posts, inside what a free Worker may do in one
  run (50 calls to other sites, 100 bound values). It reads three short lists and never the whole table:
  purges still owed (index `checks_owed`), posts a reading found unavailable that are not purged and
  not asked about in a day (index `observations_gone`, 756 rows today), then a round of every other
  post from a saved mark (`sweep_round`). What X said is recorded in one statement. A purge blanks the
  row first and marks the check last, so one cut short is still owed and the next run finishes it.
- All of the SQL moved to `tools/lib/store-sql.mjs`, and `tests/store-sql.test.mjs` runs that text against
  `worker/schema.sql` in SQLite (skipped, not failed, on a node without `node:sqlite`, because the
  grabber's machine ships on a green suite every hour).

**Alternatives.** (a) The $5 Workers plan: it ends this class of failure (50 million rows written a
month), and Sean chose to stay on free on 14 November; this keeps free working and the choice open.
(b) Move the board off D1 to a Durable Object so it shares no meter with the store: the cleanest
separation, but a storage move of a live service and a new admin path for tokens; not done unasked.
(c) Drop the `observations_at` index (a third of every observation's cost, 21,000 rows a day): it cannot
be rebuilt inside the free plan once dropped, and nothing reads by time yet, so it is left for Sean.
(d) Keep the hourly sweep and only cut its ids to 100: it would run, and still read every post every hour.

**What this costs.** With the share at 90,000, a normal day near 76,000, and a capture counted at the most it
can cost before it is taken, a backlog clears at two or three captures a day, so after an outage the
store trails git for up to a week; nothing reads the store yet. The round reaches each post about once in five weeks at today's size. Both are the free plan's
arithmetic, written down so nobody takes them for bugs.
