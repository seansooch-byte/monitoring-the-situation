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
