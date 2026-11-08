import re
s = open('build_capture.py').read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n >= 1, ("missing", old[:80])
    if count == 1: assert n == 1, ("multi", old[:80], n)
    s = s.replace(old, new)

DESKS17 = '("politics", "world", "defense", "justice", "disaster", "markets", "business", "ai", "tech", "science", "medicine", "entertainment", "music", "gaming", "sports", "internet", "offbeat")'
rep('WD = REPO / "capture/work/2026-11-08T0300Z"', 'WD = REPO / "capture/work/2026-11-08T0400Z"')
rep('NOW = datetime(2026, 11, 8, 3, 8, tzinfo=timezone.utc)', 'NOW = datetime(2026, 11, 8, 4, 5, tzinfo=timezone.utc)')
rep('STARTED = "2026-11-08T03:00:00Z"', 'STARTED = "2026-11-08T04:00:00Z"')
rep('FINISHED = "2026-11-08T03:12:00Z"', 'import sys\nFINISHED = sys.argv[1] if len(sys.argv) > 1 else "2026-11-08T04:15:00Z"')
rep('WATCH_AT = "2026-11-08T03:03:00Z"', 'WATCH_AT = "2026-11-08T04:03:00Z"')
rep('NEW_AT = "2026-11-08T03:06:00Z"', 'NEW_AT = "2026-11-08T04:05:00Z"')
rep('RUN_ID = "2026-11-08T0300Z"', 'RUN_ID = "2026-11-08T0400Z"')
rep('CONTEXT_ID = "2118903642313130199"', 'CONTEXT_ID = sys.argv[2] if len(sys.argv) > 2 else None')
rep('REQUESTS_REV = "82526eb0050cb248e7f1373733f920e1aa7198fe"', 'REQUESTS_REV = "343c21b5947f68770f8d7444f0868b004763291e"')

# sources
old_src = s[s.index('for name, fn in [\n    ("desk.politics"'):s.index(']:\n    data = load(WD / fn)')]
new_src = 'for name, fn in [\n' + ''.join(f'    ("desk.{d}", "desk_{d}.json"),\n' for d in eval(DESKS17)) + '''    ("sensors.news", "sensors_news.json"),
    ("sensors.money", "sensors_money.json"),
    ("sensors.science", "sensors_science.json"),
    ("trend.Michigan", "trend_michigan.json"),
    ("trend.Miami", "trend_miami.json"),
    ("trend.Beck", "trend_beck.json"),
    ("rising.the", "rising_the.json"),
    ("rising.this", "rising_this.json"),
'''
s = s.replace(old_src, new_src)
rep('''for i in range(3):
    ingest(load(WD / f"screen_{i}.json"), "screen")

ctx_replies = load(WD / "context_replies.json")
ctx_quotes = load(WD / "context_quotes.json")
ingest(ctx_replies, "context")
ingest(ctx_quotes, "context")''', '''import os
if CONTEXT_ID and os.path.exists(WD / "context_replies.json"):
    ctx_replies = load(WD / "context_replies.json")
    ctx_quotes = load(WD / "context_quotes.json")
    ctx_reply_new = ingest(ctx_replies, "context")
    ctx_quote_new = ingest(ctx_quotes, "context")
else:
    ctx_replies = ctx_quotes = {}
    ctx_reply_new = ctx_quote_new = []''')
rep('if p.name == "0300Z.json":', 'if p.name == "0400Z.json" and "/11/08/" in str(p):')
rep('for d in ("politics", "entertainment", "sports", "internet"):\n    kept[f"desk.{d}"]', f'for d in {DESKS17}:\n    kept[f"desk.{{d}}"]')
s = s.replace('for g in ("culture", "sports", "online"):', 'for g in ("news", "money", "science"):')
s = s.replace('for name in ("Kentucky", "#AEWCollision", "Tennessee"):', 'for name in ("Michigan", "Miami", "Beck"):')
s = s.replace('for name in ("rising.just", "rising.what"):', 'for name in ("rising.the", "rising.this"):')
rep('''for key in ("desk.politics", "desk.entertainment", "desk.sports", "desk.internet",
            "sensors.culture", "sensors.sports", "sensors.online",
            "viral.global", "rising.global", "trend.Kentucky",
            "trend.#AEWCollision", "trend.Tennessee", "old_content"):''',
f'''for key in [f"desk.{{d}}" for d in {DESKS17}] + ["sensors.news", "sensors.money", "sensors.science",
            "viral.global", "rising.global", "trend.Michigan",
            "trend.Miami", "trend.Beck", "old_content"]:''')
s = s.replace('for d in ("politics", "entertainment", "sports", "internet"):\n    for oid in kept', f'for d in {DESKS17}:\n    for oid in kept')
open('build_capture.py','w').write(s)
print("ok")
