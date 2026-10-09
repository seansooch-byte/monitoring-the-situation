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
