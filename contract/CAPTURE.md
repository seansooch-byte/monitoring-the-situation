# The capture file

A capture is what the grabber read from X during one run. It is the only thing the grabber writes.
It holds what X returned and nothing else: no summaries, no opinions, no guesses.

`tools/check-capture.mjs` is the definition of a valid capture. This page explains it; if the two ever
disagree, the checker wins. `contract/example.capture.json` is a small synthetic example that the test
suite checks, so it always matches the checker. It is not real data.

```
node tools/check-capture.mjs capture/2026/10/09/0600Z.json     prints PASS, or every error with its path
```

## Where it goes

`capture/YYYY/MM/DD/HHMMZ.json`, named for the minute the run started, in UTC.
Example: a run that started at 06:00 UTC on 9 October 2026 is `capture/2026/10/09/0600Z.json`
and its `run.id` is `2026-10-09T0600Z`.

Every scheduled run leaves a file, including a run that failed (see `run.status` below). A missing
file means the grabber did not run at all, and that is the only thing a missing file may mean.

## Three rules that decide most questions

1. **Ids are strings.** `"2108047268167274883"`, never a number. A JSON number that long has already
   lost its last digits by the time anything reads it.
2. **A number is a whole number or `null`.** Never `"1.2M"`, never an estimate. If X showed you an
   abbreviated figure, write `1200000` and set `approx: true` on that observation. If you could not
   read a figure, write `null`.
3. **Verbatim means verbatim.** Post text, display names, community notes, trend names and X story
   text are copied exactly as X returned them: same spelling, same emoji, same line breaks, same
   links. Do not translate, trim, tidy or complete them.

## Top level

| Field | What it holds |
|---|---|
| `schema` | Exactly `"mts.capture/1"`. |
| `run` | The run ledger entry (below). |
| `sweeps` | One entry per sweep attempted, including sweeps that failed or were skipped. |
| `trends` | X's trending list as read this run. |
| `posts` | Full records, for posts seen for the first time, and for posts whose record changed (a community note appeared, the text was edited). |
| `observations` | One row of numbers per post read this run. This is the time series. |
| `context` | For the biggest posts: which replies and quote posts are the most liked. |
| `answers` | Replies to the editor's open requests in `requests/open.json`. |

All six arrays are always present, even when empty.

## run

| Field | What it holds |
|---|---|
| `id` | `YYYY-MM-DDTHHMMZ`, the UTC minute the run started. Matches `started_at` and the file path. |
| `started_at`, `finished_at` | UTC, like `2026-10-09T06:00:00Z`. |
| `status` | `ok` (every sweep ran), `partial` (some did not), `down` (nothing usable was read). |
| `reason` | Required unless `status` is `ok`: one plain sentence on what went wrong. |
| `grabber.agent` | Who ran it, for example `grokbot`. |
| `grabber.model` | The model that ran it, or `null`. |
| `grabber.method` | How X was read this run (the tool or API by name). |
| `requests_rev` | The git commit of `requests/` that this run read, or `null`. |

A `down` run has empty arrays and is still a valid file. It is how a failure is recorded as data.

## sweeps[]

| Field | What it holds |
|---|---|
| `id` | A stable name: `watch`, `trends.us`, `trends.ww`, `viral.global`, `rising.global`, `desk.<desk>`, `context.top`, `request.<request id>`. |
| `kind` | `discovery`, `desk`, `trends`, `watch`, `context` or `request`. |
| `desk` | A desk id from `contract/desks.json`, or `null`. |
| `method` | The exact query, filter or tool call used, so the selection can be audited and repeated. |
| `window_hours` | How far back the sweep looked, or `null`. |
| `status` | `ok`, `partial`, `down` or `skipped`. |
| `reason` | Required unless `status` is `ok`. |
| `post_ids` | The ids this sweep returned, best first. |

The desks are listed in `contract/desks.json`, each with its scope, its beats, how often to sweep
it and its floor. That file is the only list; nothing here repeats it.

## trends[]

| Field | What it holds |
|---|---|
| `region` | `US` or `WW`. |
| `rank` | Position in the list as shown, from 1. |
| `name` | The trend exactly as X shows it. |
| `post_count` | The count X shows, or `null`. |
| `story` | `{ url, title, text }` for X's own story on the trend, copied exactly, or `null`. |
| `post_ids` | The top posts under the trend that you captured. May be empty. |

## posts[]

| Field | What it holds |
|---|---|
| `id` | The status id, as a string. |
| `url` | `https://x.com/<handle>/status/<id>`, with the same id and handle as the record. |
| `created_at` | UTC time the post was created, as X returned it. The checker compares this with the time encoded in the id and rejects a mismatch of more than two seconds. |
| `lang` | Language code, or `null`. |
| `text` | The post exactly as written. `""` for a post with no text. |
| `author.handle` | Without the `@`. |
| `author.name` | Display name as shown. |
| `author.followers` | Whole number or `null`. |
| `author.verified` | `blue`, `business`, `government`, `none`, or `null` if unknown. |
| `author.kind` | Your best label: `person`, `creator`, `news`, `org`, `brand`, `official`, `parody`, `aggregator`, `unknown`. |
| `media[]` | One entry per attachment: `type` (`photo`, `video`, `gif`, `link`, `poll`), `description`, `alt`, `duration_s`, `link_url`, `link_title`. Unknown fields are `null`. |
| `reply_to`, `quotes` | The id of the post this one replies to or quotes, or `null`. |
| `note` | `{ text }` if the post carries a community note, copied exactly. Otherwise `null`. |
| `flags` | Any of `nsfw`, `graphic`, `private_individual`, `minor`, `ad`, `engagement_bait`, `ai_media_suspected`, `old_content`, `non_english`. Usually empty. |
| `desk` | The one desk the post is most about (an id from `contract/desks.json`), or `null` if none fits. |
| `beat` | Optional. One of that desk's beats from the same file, or `null`. A beat needs a desk. |
| `topic` | A short neutral noun phrase naming what the post is about, so related posts can be grouped. No opinion in it. Or `null`. |
| `lead` | Optional. Something you noticed that the editor should check, written as an unverified lead. Or `null`. |

`media[].description` is the one place you describe rather than copy: say plainly what is visible
(who or what, doing what, any on-screen text), in one sentence, with no interpretation. The editor
cannot see the media and relies on this.

A post that appears in `posts` must also have a row in `observations` in the same file.

## observations[]

| Field | What it holds |
|---|---|
| `id` | The post. It must have a full record in this capture or an earlier one. |
| `at` | UTC time you read the numbers. Inside the run. |
| `state` | `live`, `deleted` (X says it was deleted) or `unavailable` (protected, withheld, suspended, or you could not tell). |
| `views`, `likes`, `reposts`, `quotes`, `replies`, `bookmarks` | Whole numbers, or `null` for any you could not read. |
| `approx` | `true` if any figure in the row came from an abbreviated display, `false` if all are exact. |

Observations are how speed is measured: the same post read at two times. Re-reading tracked posts
every run matters more than finding new ones.

## context[]

`{ post_id, replies: [ids], quotes: [ids] }`: the most liked replies and quote posts of a big post,
best first. Each id listed needs its own record in `posts`.

## answers[]

`{ request_id, status, post_ids, note }`. `status` is `ok`, `not_found` (X has no such post, or
nothing matched) or `unable` (you could not check). `not_found` lists no posts. Never answer a
lookup from memory: if X does not return the post in this run, the answer is `not_found`.

## What the checker rejects

Wrong schema tag. An id that is not a string of digits. A `created_at` that disagrees with the id.
A url for a different id or handle. A post with no observation. An observation for a post nobody
recorded. A metric that is not a whole number or `null`. A live observation with no numbers. A time
outside the run, in the future, or before the post existed. Any id referenced from `sweeps`,
`trends`, `context` or `answers` without a record. A value outside a closed list, including a desk that is not in `contract/desks.json` or a beat that
is not one of its desk's beats. A link that is not
`https`. A failed run or sweep with no reason. An `ok` run with no posts. A duplicate record. An em
dash in any string you wrote yourself (verbatim fields are exempt). More than 400 posts or 1,500
observations in one file.

It warns, without failing, on numbers that look odd, such as fewer views than likes. Report what
you saw; do not adjust it to silence a warning.

## What happens after the checker

Passing the checker does not publish anything. Before a post reaches the site the editor confirms,
against X directly, that the post exists and that its author and text match the record. A record
that X does not confirm is discarded and counted against the run that produced it.
