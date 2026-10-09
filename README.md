# Monitoring the Situation

A website about what the internet is paying attention to, made by two agents with a strict line
between them.

- **Grok (through grokbot) is the grabber.** It reads X, finds what is going viral, records it
  exactly, and re-reads it every hour so growth can be measured. It writes `capture/` and nothing else.
- **Claude is the editor.** It checks the captures, groups posts into stories, researches and writes
  every word, and builds and ships the site.

Start here:

| If you are | Read |
|---|---|
| The grabber | `contract/GRABBER.md`, then `contract/CAPTURE.md` |
| Changing how the pieces fit | `ARCHITECTURE.md` |
| Wondering why something is the way it is | `DECISIONS.md` |

```
npm test                                              the contract, as tests
node tools/check-capture.mjs capture/2026/10/09/0600Z.json     check one capture
```

When it is live, the site will replace the Monitoring page at seansooch.dev/monitor/.
