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

**A new job: you run the clock for the editor too.**

Sean wants one schedule, yours. After a capture is pushed, you recruit a Claude agent to do the
editor's pass: check your posts against X, research, write the stories, and publish. The split
between us does not change, and the routine is built so that it cannot: the agent takes its
orders from the repository, not from you.

Do this in order.

1. **Check what a recruited Claude agent can do**, and tell Sean before scheduling anything. In
   a clone of the repository, can it: run shell commands and Node 18 or later; search and fetch
   the web; reach `publish.x.com`; commit and push to `main` (your safety check stopped a push
   once; a pass pushes `moments/`, `requests/`, `verified/posts.json` and `editor/LOG.md`); and
   run `./tools/ship.sh`, which needs `wrangler` signed in to Sean's Cloudflare account? If it
   cannot deploy, the routine still works: the agent pushes and stops, and shipping is done
   elsewhere. Say which of these is missing.

2. **Use this brief, exactly.** The brief is the content of `contract/EDITOR-BRIEF.md`, read
   fresh from the repository at the time of each pass. Pass it word for word and add nothing:
   no summary of the capture, no suggested stories, no instructions of your own. The agent's
   procedure is `contract/EDITOR.md`, which it reads itself.

3. **Use a Claude model for this role, the most capable one you can recruit.** The work is
   judgement about real people and real claims. Never a Grok model for the editor: the point of
   the split is that the gatherer and the checker are different.

4. **Run one trial pass now**, by hand, and send Sean the agent's five line report unchanged,
   with how long it took and what it cost if you can see that.

5. **Then schedule it.** One pass after the capture of every even hour (UTC), except 06:00 and
   08:00, so ten a day. One agent at a time: if the previous pass has not finished, skip this
   one. Stop an agent that runs past forty minutes. If a pass fails, do not retry it; the next
   one picks up from the log.

6. **Stay out of each other's files.** You never edit `moments/`, `requests/`, `verified/`,
   `editor/` or anything else outside `capture/`. The editor agent never edits `capture/`. The
   repository's checks fail a commit that crosses that line in either direction.

7. **Tell Sean only what needs him.** Relay an editor report at once when it says X could not
   find a post or returned different words, when `ship.sh` refused or the live audit found a
   difference, or when it has a line for Sean. Otherwise one line a day: passes run, stories
   added, anything left out worth knowing.

**Report back to Sean in six lines:** what a recruited Claude agent can and cannot do from the
list in step 1; which model it runs on; the trial pass's own five line report; how long it took
and what it cost; the schedule you set; anything you need from him.
