# Daily briefing routine prompt (verbatim)

Runs every day at 7:03 AM Detroit time.

> Put together Sean's morning 'Monitoring the Situation' briefing covering what happened in roughly the last 24 hours, in six sections: finance and markets, politics, pop culture, sports, tech and AI, and medicine (favor what matters to a DO med student headed for Emergency Medicine: FDA actions, major trials, CMS, residency and Match news, public health). Aim for 3 to 5 items per section. Use public X data (posts, news, trends) alongside reputable web coverage, cross-check items, and give every item at least one real link you actually retrieved. Never invent facts, numbers, quotes, or URLs; flag developing stories; skip repeats from yesterday unless there's a real update. Save Markdown + JSON under /workspace/briefings/YYYY-MM-DD, publish the JSON via /workspace/monitor-feed/publish.sh, confirm https://feed.seansooch.dev/v1/feed.json shows today's generated_at, send the briefing to Sean.

`build_2026-10-08.py` in this folder is the script that wrote the 2026-10-08 briefing JSON.
