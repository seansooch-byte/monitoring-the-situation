# Reply to grokbot after the third capture, and the editor routine

Sean pastes the block below to grokbot once. The durable parts are in `GRABBER.md`, `EDITOR.md`
and `EDITOR-BRIEF.md`.

---

The gather is now doing what it was built to do. From your own scoreboard for today: 494 posts
kept, 44 over a million views, 12 over five million, 7 over ten million, the largest at 44
million. Yesterday's method topped out at 3.4 million. And every one of those posts was checked
against X independently: 492 confirmed, 2 withheld by X behind a login, none missing, none with
different words. Nothing in three captures was invented.

The site is live at https://situation.seansooch.dev and is built from your captures.

**Answers to what you asked and reported.** All of these are now written into
`contract/GRABBER.md`; pull and re-read Finding posts, Volume and Context on request.

- **Pace floor: yes, wait fifteen minutes.** Under fifteen minutes a pace is noise. Two more
  limits: a post kept on pace must already have a tenth of the floor in views, and an account
  whose `kind` is `news` is screened on totals only, never on pace. That removes the Reuters
  headlines read minutes after posting.
- **`x_stories` is optional.** You were right not to retype X's text. Leave the array out while
  the tool only returns it inline, and stop marking runs partial for it.
- **`-is:retweet` on the quote stream:** correct, keep it.
- **Early windows are now the standard for reactions.** First twenty minutes, one read for
  replies and one for quote posts, five most liked of each. Drop the two hour window.
- **A post's own history.** Quote and reply counts work; take them for each post on
  `requests/watch.json` once, a few per run, and refresh only while the post is still gaining.
  Test repost counts once on a post under a day old and drop that series if it is still zeros.
- **The For You ranking cheat sheet.** Fine as a guide to where to look. Put it at
  `capture/RANKING.md` so the editor can read it. It must not change what goes into a capture:
  a capture still holds what X returned and no judgement of it.

**Your plan for one routine is right. Here it is with four changes.**

You proposed: capture each hour, then start a Claude editor pass from the same run. Keep that
shape. Sean has also said you may use Cloudflare for this project, so the pipeline does not have
to stop at the push.

1. **Most hours need no model.** After your capture is pushed, run `./tools/refresh.sh`. It is a
   plain script: it asks X about any post not yet checked, records the answers, and ships the
   site, so the numbers follow your newest capture. It costs nothing and it is the whole hourly
   job on the editor's side. It writes one file, `verified/posts.json`, and only through the tool;
   you do not edit that file by hand.

2. **The editor's pass runs four times a day**, after the captures of 11:00, 16:00, 21:00 and
   02:00 UTC (about 7 AM, noon, 5 PM and 10 PM Eastern). This is the only step that uses Claude:
   it researches and writes the stories. It does everything itself, including `./tools/ship.sh`.

3. **The prompt is a file, passed word for word.** Not a prompt you write. Read
   `contract/EDITOR-BRIEF.md` fresh from the repository at the time of each pass and pass exactly
   that. Add nothing: no summary of the capture, no suggested stories, no instructions of your
   own. The procedure is `contract/EDITOR.md`, which the agent reads itself. One correction to
   your summary of it: the editor does not run Gate 1, which is your check. It runs the second
   one, asking X whether each post exists and matches, and that step is why the brief cannot be
   paraphrased.

4. **Give the editor its own working copy and a short list of tools.** A separate clone from
   yours, so the two never share a working tree. Allow it shell (git, node, npm, the scripts in
   `tools/`), reading and writing files inside that clone, and web search and fetch. Nothing else.
   Keep your hard turn limit, stop a pass that runs past forty minutes, and never run two at once.

**Model.** Start on Claude Sonnet 5.5 (`claude-sonnet-5-5`). Never a Grok model for the editor:
the gatherer and the checker must be different. The main editor will review the first day of
stories and Sean will decide then whether to stay on Sonnet.

**Cost.** Run Claude Code with JSON output and record, for every pass, its total cost, turns and
duration as one line in `capture/EDITOR-RUNS.md`. Say in your report which login or key the runs
use, because that decides whether a pass costs dollars or draws on Sean's subscription limits.

**Stay out of each other's files.** You never edit `moments/`, `requests/`, `editor/` or
anything else outside `capture/`. The editor agent never edits `capture/`. The repository's
checks fail a commit that crosses that line in either direction.

**Do it in this order.**

1. Run `./tools/refresh.sh` once by hand and tell Sean what it printed. If `wrangler` is not
   signed in where you run, say so and stop; Sean will sign it in.
2. Run one editor pass by hand with the brief, and send Sean the agent's five line report
   unchanged, with its cost, turns and duration.
3. Then add both to your hourly routine: the refresh every hour after the capture, the editor's
   pass at the four hours above.
4. Keep your skip switch, and tell Sean where it is.

**Tell Sean only what needs him.** Relay at once when X could not find a post or returned
different words, when `ship.sh` refused or the live audit found a difference, or when an editor
report has a line for Sean. Otherwise one line a day: passes run, stories added, what they cost.

The existing 7:03 AM briefing and feed.seansooch.dev stay as they are until Sean says otherwise.

**Report back to Sean in six lines:** what `refresh.sh` printed; the trial pass's own five line
report; its cost, turns, duration and which login or key it used; the schedule you set; where the
skip switch is; anything you need from him.
