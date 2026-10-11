# Reply to grokbot: crypto is retired, one account cannot fill a capture, and fifteen desks are going unswept

Sean pastes the block below to grokbot once. It answers the request grokbot passed on in
`capture/NOTES.md` (commit 69fe4ab). The durable parts are in `desks.json`, `GRABBER.md` and
`EDITOR.md`; nothing here says more than they do.

---

Both of Sean's changes are made. Pull, then re-read `contract/desks.json` and two parts of
`contract/GRABBER.md`: number 5 under What "viral" means here, and A retired desk under The desks.

**1. Crypto is retired.** It has moved from `desks` to a new `retired` list in
`contract/desks.json`, with `retired_at` 2026-10-11T02:00:00Z. `desks` now holds nineteen.

- From the first run that starts at or after 02:00 UTC on 11 October: no `desk.crypto` sweep, no
  post or sweep labelled `crypto`, no `desk.crypto` volume series. The checker refuses the id in
  any capture started at or after that time, and says so in the error.
- Take its standing query out of `capture/CAPABILITIES.md`, and drop any sensor account you
  follow only for coin talk from `capture/SENSORS.md`.
- Leave every earlier capture exactly as it is. The checker still passes them.
- Do not go looking for coin and token posts. One that reaches a global sweep on its own numbers
  is labelled like any other post: `markets` when it is a market event, `business` when it is a
  company's story, otherwise `null`. Coin promotion is still an ad and is left out.
- If you send a fresh full record for a post you once labelled `crypto`, give it its desk by
  that rule.
- Read `contract/desks.json` before every run from now on. A desk can be retired again.

**2. One account cannot fill a capture.** Of the posts new to a run, keep at most three from any
one account: its most viewed. Your 16:03 UTC run on 10 October kept thirteen from one account
out of forty.

- Posts a request names, and replies and quote posts kept as context, do not count.
- Nothing else changes: re-read every post already on the list, and follow references from
  every candidate whether or not you keep it.
- When the limit drops posts, say so in `capture/NOTES.md`: the account and how many.
- The pulse has its own rule, which is not yours to apply: an account holds one place there,
  and the build enforces it. Keep recording what X returns without judging it.

**3. Fifteen desks are not being swept.** This is not a new rule; it is what the captures show.
In the 24 runs from 2026-10-10T0135Z to 2026-10-11T0005Z, `politics`, `entertainment`, `sports`
and `internet` were swept 24 times each. Every other desk was swept once and skipped 23 times,
with the reason "non-hourly desk skipped after cut order". Those runs used 16 to 19 reads
against a daytime allowance of 42, and 10 October ended near 465 reads of the 850 allowed. Your
notes show the same pattern since 12:12 UTC on 9 October, along with no volume, no context and
no media descriptions.

- The cut order is for a day that is running short of reads. These days were not.
- From the next daytime run, sweep every desk that is due, as The desks says: about ten desk
  sweeps a run, inside the 42.
- If something other than X reads is limiting a run (time, your own usage allowance, a tool
  that fails), say exactly what in `capture/NOTES.md`. That is a different problem and it needs
  a different answer than cutting desks, so do not solve it silently.

This matters more than either change above. A front page drawn from four desks and the global
sweeps is mostly the largest accounts, whatever limit is put on them.

In your next notes entry, confirm in one line each: crypto's query removed, the first run that
applied the three-an-account limit, and what was holding the runs to the four hourly desks.
