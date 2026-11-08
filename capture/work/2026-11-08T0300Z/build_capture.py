#!/usr/bin/env python3
import json, re, html
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path("/workspace/monitoring-the-situation")
WD = REPO / "capture/work/2026-11-08T0300Z"
NOW = datetime(2026, 11, 8, 3, 8, tzinfo=timezone.utc)
STARTED = "2026-11-08T03:00:00Z"
FINISHED = "2026-11-08T03:12:00Z"
WATCH_AT = "2026-11-08T03:03:00Z"
NEW_AT = "2026-11-08T03:06:00Z"
RUN_ID = "2026-11-08T0300Z"
CONTEXT_ID = "2118903642313130199"
REQUESTS_REV = "82526eb0050cb248e7f1373733f920e1aa7198fe"

FLOORS = {
    "politics": (50000, 1000), "world": (50000, 1000), "defense": (10000, 250),
    "justice": (20000, 500), "disaster": (20000, 500), "markets": (20000, 500),
    "business": (20000, 500), "ai": (20000, 500), "tech": (20000, 500),
    "science": (10000, 250), "medicine": (10000, 250), "entertainment": (50000, 1000),
    "music": (50000, 1000), "gaming": (20000, 500), "ideas": (10000, 250),
    "sports": (50000, 1000), "internet": (50000, 1000), "life": (20000, 500),
    "offbeat": (50000, 1000),
}
NEWS_HANDLES = {
    "bbcbreaking", "skynews", "reuters", "wfla", "leadingreport", "meidastouch",
    "cnn", "nytimes", "washingtonpost", "ap", "apnews", "npr", "abc", "cbsnews",
    "nbcnews", "foxnews", "politico", "thehill", "axios", "bbcnews",
}
DESK_KW = [
    ("sports", ["nfl", "nba", "mlb", "nhl", "wnba", "ufc", "heisman", "touchdown",
        "quarterback", "ohio state", "notre dame", "kentucky", "tennessee", "bama",
        "alabama", "ole miss", "lane kiffin", "ryan day", "cj carr", "buckeyes",
        "playoffs", "home run", "soccer", "premier league", "ufc", "aew", "wrestle",
        "collision", "football", "basketball", "baseball", "hockey", "f1", "golf",
        "tennis", "coach", "touchdown", "bkfc", "angel reese", "shaq"]),
    ("politics", ["trump", "white house", "congress", "senate", "democrat", "republican",
        "gop", "supreme court", "governor", "biden", "maga", "election"]),
    ("world", ["ukraine", "russia", "israel", "gaza", "iran", "china", "nato",
        "united nations", "ceasefire", "prime minister"]),
    ("justice", ["arrested", "police", "cops", "trial", "verdict", "sentenced",
        "lawsuit", "prison", "jail", "shooting", "murder"]),
    ("disaster", ["hurricane", "tornado", "earthquake", "wildfire", "flood",
        "evacuation", "explosion"]),
    ("markets", ["stock market", "nasdaq", "dow jones", "s&p", "inflation",
        "interest rates", "the fed", "treasury", "yields"]),
    ("ai", ["openai", "chatgpt", "anthropic", "claude", "gemini", "llm", "grok",
        "artificial intelligence"]),
    ("tech", ["apple", "iphone", "google", "microsoft", "android", "tesla",
        "hacked", "data breach"]),
    ("entertainment", ["movie", "film", "trailer", "netflix", "box office",
        "actor", "actress", "celebrity", "anime"]),
    ("music", ["album", "song", "concert", "spotify", "grammy", "kpop", "rapper"]),
    ("gaming", ["playstation", "xbox", "nintendo", "steam", "esports", "video game"]),
    ("internet", ["meme", "streamer", "twitch", "youtuber", "tiktok", "influencer",
        "podcast", "fandom"]),
    ("medicine", ["hospital", "vaccine", "fda", "cdc", "doctor", "nurse", "outbreak"]),
    ("science", ["nasa", "spacex", "rocket", "telescope", "physic"]),
    ("business", ["ceo", "layoffs", "merger", "earnings", "startup"]),
    ("life", ["dating", "marriage", "boyfriend", "girlfriend", "wedding", "recipe"]),
    ("offbeat", ["dog", "cat", "puppy", "kitten", "wholesome", "nutella"]),
]

def load(path):
    raw = Path(path).read_text()
    return json.JSONDecoder().raw_decode(raw, raw.find("{"))[0]

def parse_ts(s):
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def post_text(p):
    nt = p.get("note_tweet") or {}
    if isinstance(nt, dict) and nt.get("text"):
        return nt["text"]
    return p.get("text") or ""

def metrics(p):
    pm = p.get("public_metrics") or {}
    return {
        "views": pm.get("impression_count"),
        "likes": pm.get("like_count"),
        "reposts": pm.get("retweet_count", pm.get("repost_count")),
        "quotes": pm.get("quote_count"),
        "replies": pm.get("reply_count"),
        "bookmarks": pm.get("bookmark_count"),
    }

def author_kind(u):
    if not u:
        return "unknown"
    handle = (u.get("username") or "").lower()
    if handle in NEWS_HANDLES:
        return "news"
    if u.get("verified_type") == "government":
        return "official"
    return "unknown"

def age_hours(p, now=NOW):
    ts = parse_ts(p.get("created_at"))
    if not ts:
        return None
    return (now - ts).total_seconds() / 3600.0

def clears_global(p, users):
    if not p:
        return False
    m = metrics(p)
    ah = age_hours(p)
    if ah is None or ah < 0 or ah >= 24:
        return False
    views = m["views"] or 0
    likes = m["likes"] or 0
    kind = author_kind(users.get(p.get("author_id")))
    if ah < 0.25:
        return False
    if ah < 3 and kind != "news":
        return views >= 10000 and (views / ah) >= 25000
    return views >= 100000 or likes >= 2000

def clears_desk(p, desk, users):
    if not p:
        return False
    fv, fl = FLOORS[desk]
    m = metrics(p)
    ah = age_hours(p)
    if ah is None or ah < 0 or ah >= 24:
        return False
    views = m["views"] or 0
    likes = m["likes"] or 0
    kind = author_kind(users.get(p.get("author_id")))
    if ah < 0.25:
        return False
    if ah < 3 and kind != "news":
        return views >= fv / 10 and (views / ah) >= fv / 4
    return views >= fv or likes >= fl

def verified_of(u):
    if not u:
        return None
    vt = u.get("verified_type")
    if vt in ("blue", "business", "government", "none"):
        return vt
    if u.get("verified") is True:
        return "blue"
    if u.get("verified") is False:
        return "none"
    return None

def classify_desk(text, sweep_desk=None):
    t = (text or "").lower()
    for desk, kws in DESK_KW:
        for kw in kws:
            if kw in t:
                return desk
    return sweep_desk

def guess_beat(desk, text):
    t = (text or "").lower()
    if desk == "sports":
        if any(x in t for x in ("aew", "wrestle", "collision")):
            return "wrestling"
        if any(x in t for x in ("ufc", "bkfc", "mma", "knockout", "ko ")):
            return "combat"
        if any(x in t for x in ("nba", "shaq", "angel reese", "basketball")):
            return "nba"
        if "nfl" in t:
            return "nfl"
        if any(x in t for x in ("kentucky", "tennessee", "ohio state", "notre dame",
                                "ole miss", "bama", "alabama", "lane kiffin", "heisman",
                                "college football", "vols")):
            return "college-football"
        if "nhl" in t or "hockey" in t:
            return "nhl"
    if desk == "politics":
        if "trump" in t or "white house" in t:
            return "white-house"
        if "election" in t:
            return "elections"
    return None

def is_skip_text(text):
    t = (text or "").lower()
    bad = ["onlyfans", "porn", "xxx ", "child porn", "csam", "nude minor"]
    return any(b in t for b in bad)

def media_list(p, media_map):
    out = []
    keys = (p.get("attachments") or {}).get("media_keys") or []
    for k in keys:
        m = media_map.get(k) or {}
        typ = m.get("type")
        if typ == "animated_gif":
            typ = "gif"
        elif typ == "photo":
            typ = "photo"
        elif typ == "video":
            typ = "video"
        elif typ:
            typ = typ
        else:
            continue
        dur = m.get("duration_ms")
        duration_s = (dur / 1000.0) if isinstance(dur, (int, float)) else None
        out.append({
            "type": typ,
            "description": None,
            "alt": m.get("alt_text"),
            "duration_s": duration_s,
            "link_url": None,
            "link_title": None,
        })
    urls = ((p.get("entities") or {}).get("urls")) or []
    last = None
    for u in urls:
        exp = u.get("expanded_url") or u.get("unwound_url") or ""
        if exp and "x.com" not in exp and "twitter.com" not in exp and "t.co/" not in exp:
            last = u
    if last and not keys:
        out.append({
            "type": "link",
            "description": None,
            "alt": None,
            "duration_s": None,
            "link_url": last.get("expanded_url") or last.get("unwound_url"),
            "link_title": last.get("title"),
        })
    return out

def reply_to_of(p):
    for r in p.get("referenced_tweets") or []:
        if r.get("type") == "replied_to":
            return r.get("id")
    return None

def quotes_of(p):
    for r in p.get("referenced_tweets") or []:
        if r.get("type") == "quoted":
            return r.get("id")
    return None

def media_source_of(p):
    ms = (p.get("attachments") or {}).get("media_source_tweet_id") or []
    return ms[0] if ms else None

def credits_handle(text):
    m = re.search(r"(?:via|📽️)\s*@([A-Za-z0-9_]+)", text or "")
    return m.group(1) if m else None

def truncation_kind(old, new):
    if old == new:
        return None
    old_u = html.unescape(old)
    new_u = html.unescape(new)
    if old_u == new_u:
        return "unescape"
    tco = re.compile(r"\s*https://t\.co/\w+\s*$")
    if tco.sub("", old_u) == tco.sub("", new_u):
        return "t.co"
    # reply display sometimes prefixes @handle before the note_tweet body
    old_body = re.sub(r"^@[A-Za-z0-9_]+\s+", "", old_u)
    old_body = tco.sub("", old_body).rstrip()
    new_body = tco.sub("", new_u).rstrip()
    if old_body and new_body.startswith(old_body) and len(new_body) >= len(old_body):
        return "note_tweet"
    old_cut = old_u.replace("\u2026", "").replace("...", "").rstrip()
    if new_u.startswith(old_cut[: min(len(old_cut), 180)]) and len(new_u) > len(old_u):
        return "note_tweet"
    if old_u.startswith(new_u[: min(len(new_u), 180)]) and ("\u2026" in old or "..." in old or tco.search(old)):
        return "note_tweet"
    return "word"

def iso_hour(s):
    ts = parse_ts(s)
    return ts.strftime("%Y-%m-%dT%H:%M:%SZ")

# ---------- load corpus ----------
posts, users, media = {}, {}, {}
ref_count = Counter()
ref_from = defaultdict(list)

def ingest(data, tag=None):
    for u in (data.get("includes") or {}).get("users") or []:
        users[u["id"]] = u
    for m in (data.get("includes") or {}).get("media") or []:
        if m.get("media_key"):
            media[m["media_key"]] = m
    extra = (data.get("includes") or {}).get("tweets") or []
    main = data.get("data") or []
    if main and isinstance(main[0], dict) and "id" not in main[0]:
        return []
    ids = []
    for p in list(main) + list(extra):
        if not isinstance(p, dict) or "id" not in p:
            continue
        posts[p["id"]] = p
        if p in main:
            ids.append(p["id"])
        for r in p.get("referenced_tweets") or []:
            if r.get("id"):
                ref_count[r["id"]] += 1
                ref_from[r["id"]].append((p["id"], r.get("type"), tag))
        for sid in (p.get("attachments") or {}).get("media_source_tweet_id") or []:
            ref_count[sid] += 1
            ref_from[sid].append((p["id"], "media_source", tag))
    return ids

def origins_of(result_ids):
    out = []
    for pid in result_ids:
        p = posts.get(pid)
        if not p:
            continue
        chosen = None
        rts = p.get("referenced_tweets") or []
        for typ in ("retweeted", "quoted"):
            for r in rts:
                if r.get("type") == typ and r.get("id"):
                    chosen = r["id"]
                    break
            if chosen:
                break
        if not chosen:
            ms = (p.get("attachments") or {}).get("media_source_tweet_id") or []
            if ms:
                chosen = ms[0]
        out.append(chosen or pid)
    return out

for i in range(8):
    ingest(load(WD / f"watch_{i}.json"), "watch")

source_results = {}
for name, fn in [
    ("desk.politics", "desk_politics.json"),
    ("desk.entertainment", "desk_entertainment.json"),
    ("desk.sports", "desk_sports.json"),
    ("desk.internet", "desk_internet.json"),
    ("sensors.culture", "sensors_culture.json"),
    ("sensors.sports", "sensors_sports.json"),
    ("sensors.online", "sensors_online.json"),
    ("trend.Kentucky", "trend_kentucky.json"),
    ("trend.#AEWCollision", "trend_aewcollision.json"),
    ("trend.Tennessee", "trend_tennessee.json"),
    ("rising.just", "rising_just.json"),
    ("rising.what", "rising_what.json"),
]:
    data = load(WD / fn)
    ids = ingest(data, name)
    source_results[name] = {"result_ids": ids, "origin_ids": origins_of(ids)}

for i in range(3):
    ingest(load(WD / f"screen_{i}.json"), "screen")

ctx_replies = load(WD / "context_replies.json")
ctx_quotes = load(WD / "context_quotes.json")
ingest(ctx_replies, "context")
ingest(ctx_quotes, "context")

# known / last records
known, last = set(), {}
for p in sorted((REPO / "capture/2026").rglob("*Z.json")):
    if p.name == "0300Z.json":
        continue
    try:
        doc = json.loads(p.read_text())
    except Exception:
        continue
    for post in doc.get("posts") or []:
        if post and post.get("id"):
            known.add(post["id"])
            last[post["id"]] = post

# cited ids
cited = set()
for folder in ("pulse", "moments"):
    for p in (REPO / folder).rglob("*.json"):
        try:
            s = p.read_text()
        except Exception:
            continue
        cited.update(re.findall(r"(\d{15,22})", s))

plan = json.load(open(REPO / "requests/plan.json"))
watch_ids = plan["items"][0]["ids"]
watch_json = json.load(open(REPO / "requests/watch.json"))["post_ids"]
omitted = [i for i in watch_json if i not in watch_ids]

# ---------- keep ----------
def pick_desk_kept(desk):
    src = source_results[f"desk.{desk}"]
    seen, cands = set(), []
    for oid in src["origin_ids"]:
        if oid in seen:
            continue
        seen.add(oid)
        p = posts.get(oid)
        if p and clears_desk(p, desk, users):
            m = metrics(p)
            ah = age_hours(p) or 99
            cands.append((m["views"] or 0, (m["views"] or 0) / ah, oid))
    cands.sort(reverse=True)
    return [oid for _, _, oid in cands[:5]]

kept = {}
for d in ("politics", "entertainment", "sports", "internet"):
    kept[f"desk.{d}"] = pick_desk_kept(d)

for g in ("culture", "sports", "online"):
    src = source_results[f"sensors.{g}"]
    seen, cands = set(), []
    for oid in list(dict.fromkeys(src["origin_ids"] + src["result_ids"])):
        if oid in seen:
            continue
        seen.add(oid)
        p = posts.get(oid)
        if not p:
            continue
        if clears_global(p, users) or any(clears_desk(p, d, users) for d in FLOORS):
            cands.append((metrics(p)["views"] or 0, oid))
    cands.sort(reverse=True)
    kept[f"sensors.{g}"] = [oid for _, oid in cands[:15]]

for name in ("Kentucky", "#AEWCollision", "Tennessee"):
    src = source_results[f"trend.{name}"]
    seen, cands = set(), []
    for oid in src["origin_ids"]:
        if oid in seen:
            continue
        seen.add(oid)
        p = posts.get(oid)
        if p:
            cands.append((metrics(p)["views"] or 0, oid))
    cands.sort(reverse=True)
    kept[f"trend.{name}"] = [oid for _, oid in cands[:3]]

viral = []
seen = set()
for name in ("Kentucky", "#AEWCollision", "Tennessee"):
    for oid in kept[f"trend.{name}"]:
        if oid not in seen:
            viral.append(oid)
            seen.add(oid)
cands = []
for name in ("Kentucky", "#AEWCollision", "Tennessee"):
    for oid in source_results[f"trend.{name}"]["origin_ids"]:
        if oid in seen:
            continue
        p = posts.get(oid)
        if p and clears_global(p, users):
            cands.append((metrics(p)["views"] or 0, oid))
cands.sort(reverse=True)
for _, oid in cands:
    if len(viral) >= 40:
        break
    if oid not in seen:
        viral.append(oid)
        seen.add(oid)
kept["viral.global"] = viral

cands, seen = [], set()
for name in ("rising.just", "rising.what"):
    for oid in source_results[name]["origin_ids"]:
        if oid in seen:
            continue
        seen.add(oid)
        p = posts.get(oid)
        if p and clears_global(p, users):
            cands.append((metrics(p)["views"] or 0, oid))
cands.sort(reverse=True)
kept["rising.global"] = [oid for _, oid in cands[:30]]

old_keep = []
for tid, refs in ref_from.items():
    p = posts.get(tid)
    if not p:
        continue
    t_created = parse_ts(p.get("created_at"))
    if not t_created:
        continue
    for src_id, typ, tag in refs:
        sp = posts.get(src_id)
        if not sp:
            continue
        s_created = parse_ts(sp.get("created_at"))
        if s_created and (s_created - t_created) > timedelta(days=7):
            old_keep.append(tid)
            break
kept["old_content"] = old_keep

# union of kept discovery
discovery = []
for key in ("desk.politics", "desk.entertainment", "desk.sports", "desk.internet",
            "sensors.culture", "sensors.sports", "sensors.online",
            "viral.global", "rising.global", "trend.Kentucky",
            "trend.#AEWCollision", "trend.Tennessee", "old_content"):
    discovery.extend(kept[key])
# unique preserve order
seen = set()
discovery_unique = []
for oid in discovery:
    if oid not in seen:
        discovery_unique.append(oid)
        seen.add(oid)

# skip sexual and posts we cannot record (unknown + no author)
skipped_sexual = []
buildable = []
for oid in discovery_unique:
    p = posts.get(oid)
    if not p:
        continue
    if is_skip_text(post_text(p)):
        skipped_sexual.append(oid)
        continue
    u = users.get(p.get("author_id"))
    if oid not in known and not u:
        continue
    buildable.append(oid)

# account cap on NEW posts (context exempt)
new_ids = [oid for oid in buildable if oid not in known]
by_acct = defaultdict(list)
for oid in new_ids:
    p = posts[oid]
    u = users.get(p.get("author_id")) or {}
    handle = u.get("username") or p.get("author_id")
    by_acct[handle].append((metrics(p)["views"] or 0, oid))
dropped_cap = {}
capped_out = set()
for handle, rows in by_acct.items():
    rows.sort(reverse=True)
    extra = rows[3:]
    if extra:
        dropped_cap[handle] = len(extra)
        for _, oid in extra:
            if oid != CONTEXT_ID:
                capped_out.add(oid)
keep_ids = [oid for oid in buildable if oid not in capped_out]

# filter sweep lists
def filt(ids):
    return [i for i in ids if i in keep_ids]

for k in list(kept.keys()):
    kept[k] = filt(kept[k])

# context top 5 most liked of each (0 this run)
ctx_reply_ids = []
ctx_quote_ids = []
# still include context target in keep
if CONTEXT_ID not in keep_ids and posts.get(CONTEXT_ID) and users.get(posts[CONTEXT_ID].get("author_id")):
    keep_ids.append(CONTEXT_ID)

# ---------- records ----------
def lead_for(oid, sweep_hints):
    bits = []
    if sweep_hints:
        bits.append(sweep_hints)
    n = ref_count.get(oid, 0)
    if n >= 2:
        bits.append(f"pointed at by {n} posts read this run")
    p = posts[oid]
    ah = age_hours(p)
    m = metrics(p)
    if ah and 0.25 <= ah < 3 and (m["views"] or 0) >= 10000:
        pace = int((m["views"] or 0) / ah)
        if pace >= 25000:
            bits.append(f"about {pace} views an hour")
    cr = credits_handle(post_text(p))
    if cr:
        bits.append(f"credits @{cr}")
    if oid in old_keep:
        bits.append("origin more than 7 days older than a post that pointed to it")
    return "; ".join(bits) if bits else None

sweep_hint_map = {}
for d in ("politics", "entertainment", "sports", "internet"):
    for oid in kept[f"desk.{d}"]:
        sweep_hint_map.setdefault(oid, f"desk.{d} origin")
for g in ("culture", "sports", "online"):
    for oid in kept[f"sensors.{g}"]:
        sweep_hint_map.setdefault(oid, f"sensors.{g}")
for oid in kept["viral.global"]:
    sweep_hint_map.setdefault(oid, "viral.global from trend-name streams")
for oid in kept["rising.global"]:
    sweep_hint_map.setdefault(oid, "rising.global quote-stream origin")
for name in ("Kentucky", "#AEWCollision", "Tennessee"):
    for oid in kept[f"trend.{name}"]:
        sweep_hint_map.setdefault(oid, f"trend {name} attachment")

def flags_for(oid):
    p = posts[oid]
    flags = []
    if oid in old_keep:
        flags.append("old_content")
    lang = p.get("lang")
    if lang and lang not in ("en", "zxx", "und", "qme", "qht", "art"):
        flags.append("non_english")
    return flags

def make_record(oid, sweep_desk=None):
    p = posts[oid]
    u = users.get(p.get("author_id")) or {}
    handle = u.get("username")
    if not handle:
        return None
    text = post_text(p)
    desk = classify_desk(text, sweep_desk)
    beat = guess_beat(desk, text) if desk else None
    rec = {
        "id": oid,
        "url": f"https://x.com/{handle}/status/{oid}",
        "created_at": p.get("created_at"),
        "lang": p.get("lang"),
        "text": text,
        "author": {
            "handle": handle,
            "name": u.get("name") or handle,
            "followers": (u.get("public_metrics") or {}).get("followers_count"),
            "verified": verified_of(u),
            "kind": author_kind(u),
        },
        "media": media_list(p, media),
        "reply_to": reply_to_of(p),
        "quotes": quotes_of(p),
        "note": None,
        "flags": flags_for(oid),
        "desk": desk,
        "beat": beat,
        "topic": None,
        "lead": lead_for(oid, sweep_hint_map.get(oid)),
    }
    ms = media_source_of(p)
    if ms:
        rec["media_source"] = ms
    return rec

def make_obs(oid, at):
    p = posts.get(oid)
    if not p:
        return {
            "id": oid, "at": at, "state": "unavailable",
            "views": None, "likes": None, "reposts": None,
            "quotes": None, "replies": None, "bookmarks": None, "approx": False,
        }
    m = metrics(p)
    return {
        "id": oid, "at": at, "state": "live",
        "views": m["views"], "likes": m["likes"], "reposts": m["reposts"],
        "quotes": m["quotes"], "replies": m["replies"], "bookmarks": m["bookmarks"],
        "approx": False,
    }

# text diffs on watch
truncation_ids, word_ids = [], []
for oid in watch_ids:
    if oid not in posts or oid not in last:
        continue
    old = last[oid].get("text") or ""
    new = post_text(posts[oid])
    kind = truncation_kind(old, new)
    if kind == "word":
        word_ids.append(oid)
    elif kind:
        truncation_ids.append(oid)

cited_trunc = [i for i in truncation_ids if i in cited]
cited_word = [i for i in word_ids if i in cited]
uncited_word = [i for i in word_ids if i not in cited]

# posts array: new or changed
changed_needed = set(word_ids + truncation_ids)
post_records = []
post_ids_written = set()
# desk hint for records
desk_of = {}
for d in ("politics", "entertainment", "sports", "internet"):
    for oid in kept[f"desk.{d}"]:
        desk_of[oid] = d

for oid in keep_ids:
    if oid in known and oid not in changed_needed:
        continue
    rec = make_record(oid, desk_of.get(oid))
    if rec:
        post_records.append(rec)
        post_ids_written.add(oid)

# also write changed watch posts even if not in keep_ids
for oid in changed_needed:
    if oid in post_ids_written:
        continue
    if oid not in posts:
        continue
    rec = make_record(oid, desk_of.get(oid))
    if rec:
        post_records.append(rec)
        post_ids_written.add(oid)

# observations: all watch + all keep_ids (and context)
obs = []
obs_ids = set()
unavailable = []
for oid in watch_ids:
    if oid in posts:
        o = make_obs(oid, WATCH_AT)
    else:
        o = make_obs(oid, WATCH_AT)
        o["state"] = "unavailable"
        unavailable.append(oid)
    obs.append(o)
    obs_ids.add(oid)
for oid in keep_ids:
    if oid in obs_ids:
        continue
    if oid not in posts:
        continue
    obs.append(make_obs(oid, NEW_AT))
    obs_ids.add(oid)
for oid in ctx_reply_ids + ctx_quote_ids:
    if oid in obs_ids:
        continue
    if oid in posts:
        obs.append(make_obs(oid, NEW_AT))
        obs_ids.add(oid)

# every post record needs an observation
for rec in post_records:
    if rec["id"] not in obs_ids:
        obs.append(make_obs(rec["id"], NEW_AT))
        obs_ids.add(rec["id"])

# drop post records that somehow lack authors already handled

# ---------- trends ----------
tr_us = load(WD / "trends_us.json")["data"]
tr_ww = load(WD / "trends_ww.json")["data"]

def match_posts_for_name(name):
    name_l = name.lower()
    cands = []
    pool = set(keep_ids) | set(watch_ids)
    for oid in pool:
        p = posts.get(oid)
        if not p:
            continue
        text = post_text(p)
        if name_l in text.lower() or name_l in ((users.get(p.get("author_id")) or {}).get("name") or "").lower():
            cands.append((metrics(p)["views"] or 0, oid))
    cands.sort(reverse=True)
    # only ids that have a record this run or earlier
    out = []
    for _, oid in cands:
        if oid in known or oid in post_ids_written:
            out.append(oid)
        if len(out) == 3:
            break
    return out

trends = []
for i, t in enumerate(tr_us, 1):
    name = t["trend_name"]
    pids = kept.get(f"trend.{name}") or match_posts_for_name(name)
    pids = [x for x in pids if x in known or x in post_ids_written]
    trends.append({"region": "US", "rank": i, "name": name, "post_count": None, "story": None, "post_ids": pids[:3]})
for i, t in enumerate(tr_ww, 1):
    name = t["trend_name"]
    pids = kept.get(f"trend.{name}") or match_posts_for_name(name)
    pids = [x for x in pids if x in known or x in post_ids_written]
    trends.append({"region": "WW", "rank": i, "name": name, "post_count": None, "story": None, "post_ids": pids[:3]})

# ---------- volume ----------
VOL_Q = {
    "defense": '(military OR Pentagon OR Army OR Navy OR "Air Force" OR Marines OR soldiers OR troops OR veterans OR missile OR drone OR "fighter jet") lang:en',
    "justice": "(arrested OR police OR cops OR trial OR verdict OR sentenced OR lawsuit OR sued OR shooting OR murder OR jail OR prison) lang:en",
    "disaster": '(hurricane OR tornado OR earthquake OR wildfire OR flood OR flooding OR storm OR "power outage" OR crash OR explosion OR evacuation) lang:en',
    "markets": '(stocks OR "stock market" OR Nasdaq OR "Dow Jones" OR "S&P 500" OR yields OR Treasury OR "the Fed" OR inflation OR "oil prices" OR mortgage OR "interest rates") lang:en',
}
volume = []
vol_sums = {}
for desk, fn in (("defense", "vol_defense.json"), ("justice", "vol_justice.json"),
                 ("disaster", "vol_disaster.json"), ("markets", "vol_markets.json")):
    data = load(WD / fn)
    pts = []
    for row in data["data"]:
        pts.append({"start": iso_hour(row["start"]), "count": row["tweet_count"]})
    sm = sum(p["count"] for p in pts)
    meta = (data.get("meta") or {}).get("total_tweet_count")
    vol_sums[desk] = (len(pts), sm, meta)
    volume.append({
        "key": f"desk.{desk}",
        "desk": desk,
        "query": VOL_Q[desk],
        "granularity": "hour",
        "points": pts,
    })

# ---------- sweeps ----------
def sweep(sid, kind, desk, method, window, status, reason, pids):
    return {
        "id": sid, "kind": kind, "desk": desk, "method": method,
        "window_hours": window, "status": status, "reason": reason,
        "post_ids": pids,
    }

watch_method = (
    "get_posts_by_ids of the re-read list in requests/plan.json for 2026-11-08T03Z "
    "(written at 2026-11-08T02:11:44.963Z), in its order and in batches of 100 "
    f"(800 ids, the day-band cap); {800-len(unavailable)} of 800 returned, {len(unavailable)} unavailable"
    + (f" ({', '.join(unavailable)})" if unavailable else "")
    + (f". {len(omitted)} watch.json ids omitted from that plan list ({', '.join(omitted)}) were not re-read this run (those ids were not on the plan list)."
       if omitted else ".")
)

sweeps = [
    sweep("watch", "watch", None, watch_method, None, "ok", None, list(watch_ids)),
    sweep("trends.us", "trends", None, "get_trends_by_woeid 23424977 max 20", None, "ok", None,
          [pid for t in trends if t["region"] == "US" for pid in t["post_ids"]]),
    sweep("trends.ww", "trends", None, "get_trends_by_woeid 1 max 20", None, "ok", None,
          [pid for t in trends if t["region"] == "WW" for pid in t["post_ids"]]),
    sweep("viral.global", "discovery", None,
          'trend-name repost streams "Kentucky" lang:en is:retweet, "#AEWCollision" lang:en is:retweet and "Tennessee" lang:en is:retweet, newest first, 25 each (3 reads; the first three US top-ten names with no posts attached in 0200Z: Kentucky rank 5, #AEWCollision rank 9 and Tennessee rank 10, all new or empty last run; result counts recorded from those streams). Ohio State/Ryan Day/Fahey-like names and Ole Miss/Lane Kiffin/Bama look like college football; Dana White/#UFCVegas124 one UFC event; Notre Dame/CJ Carr one Notre Dame football story; Kentucky/Tennessee one Kentucky vs Tennessee game',
          24, "ok", None, kept["viral.global"]),
    sweep("rising.global", "discovery", None,
          'quote streams "just lang:en is:quote -is:retweet" and "what lang:en is:quote -is:retweet", newest first, 25 each (2 reads); words just and what, next in the rotation after it/that (skipping "and", which X rejects as ambiguous)',
          6, "ok", None, kept["rising.global"]),
    sweep("sensors.news", "discovery", None,
          "not read this run (rotation: culture/sports/online this run); last read in 2026-11-08T0200Z",
          None, "skipped", "rotation: culture/sports/online this run", []),
    sweep("sensors.money", "discovery", None,
          "not read this run (rotation: culture/sports/online this run); last read in 2026-11-08T0200Z",
          None, "skipped", "rotation: culture/sports/online this run", []),
    sweep("sensors.science", "discovery", None,
          "not read this run (rotation: culture/sports/online this run); last read in 2026-11-08T0200Z",
          None, "skipped", "rotation: culture/sports/online this run", []),
    sweep("sensors.culture", "discovery", None,
          "search_posts_all (from:PopBase OR from:PopCrave OR from:CultureCrave OR from:DiscussingFilm OR from:superTV247 OR from:scottygb OR from:IGN OR from:Dexerto OR from:flolikethis OR from:chaovampz OR from:HYBE_LABELS OR from:billboard OR from:Wuthering_Waves OR from:Nintendo OR from:PlayStation OR from:wahalaondirocks) -is:reply, newest first, 25; sensor posts and the origins they point at, screened by floor/pace",
          None, "ok", None, kept["sensors.culture"]),
    sweep("sensors.sports", "discovery", None,
          "search_posts_all (from:NFL OR from:NFLMemes OR from:RapSheet OR from:AdamSchefter OR from:ShamsCharania OR from:MLB OR from:SportsCenter OR from:BleacherReport OR from:espnW OR from:stephenasmith OR from:barstoolsports OR from:FearedBuck OR from:TotalProSports OR from:Underdog OR from:FabrizioRomano) -is:reply, newest first, 25; sensor posts and the origins they point at, screened by floor/pace",
          None, "ok", None, kept["sensors.sports"]),
    sweep("sensors.online", "discovery", None,
          "search_posts_all (from:SinClipd OR from:Clipdyz OR from:DramaAlert OR from:NoContextHumans OR from:crazyclipsonly OR from:interesting_aIl OR from:AMAZlNGNATURE OR from:insanevideos OR from:MarioNawfal OR from:SomaKazima2 OR from:IAmLilRico OR from:lyricsmotions OR from:kenyasgossips OR from:hayasaka_aryan OR from:TheNairobiTimez) -is:reply, newest first, 25; sensor posts and the origins they point at, screened by floor/pace",
          None, "ok", None, kept["sensors.online"]),
]

DESK_Q = {
    "politics": '(Trump OR "White House" OR Congress OR Senate OR Democrats OR Republicans OR GOP OR "Supreme Court" OR election OR governor)',
    "entertainment": '(movie OR film OR trailer OR "box office" OR Netflix OR "TV show" OR episode OR season OR anime OR actor OR actress OR celebrity)',
    "sports": '(NFL OR NBA OR MLB OR NHL OR WNBA OR UFC OR "Premier League" OR soccer OR touchdown OR playoffs OR "home run" OR F1 OR golf OR tennis)',
    "internet": '(meme OR memes OR streamer OR stream OR Twitch OR Kick OR YouTuber OR TikTok OR influencer OR podcast OR fandom OR "main character")',
}
for d in ("politics", "entertainment", "sports", "internet"):
    sweeps.append(sweep(
        f"desk.{d}", "desk", d,
        f"search_posts_all {DESK_Q[d]} lang:en is:retweet -is:reply, newest first, 25; reposted origins screened by desk floor/pace; keep at most five best",
        24, "ok", None, kept[f"desk.{d}"]))

sweeps.append(sweep(
    "volume.desks", "volume", None,
    "get_posts_counts_recent granularity hour, query \"<standing query> lang:en\", start_time 2026-11-01T04:00:00Z, end_time 2026-11-08T03:00:00Z, one read per desk for the 4 desks the plan gives (volume.defense, volume.justice, volume.disaster, volume.markets); each series is the 167 full hours, sums match meta.total_tweet_count",
    None, "ok", None, []))

sweeps.append(sweep(
    "context.top", "context", None,
    f"conversation_id:{CONTEXT_ID} is:reply and quotes_of_tweet_id:{CONTEXT_ID} -is:retweet, relevancy, start_time 2026-11-07T03:09:30.000Z end_time 2026-11-07T03:29:30.000Z (post time plus 20 minutes); five most liked of each kept (0 replies, 0 quotes kept from 0/0 returned)",
    None, "ok", None, [CONTEXT_ID] if CONTEXT_ID in keep_ids else []))

# ensure every sweep/trend/context id has a record
needed = set()
for s in sweeps:
    needed.update(s["post_ids"])
for t in trends:
    needed.update(t["post_ids"])
needed.add(CONTEXT_ID)
missing_needed = [i for i in needed if i not in known and i not in post_ids_written]
# try to add records for missing needed
for oid in missing_needed:
    rec = make_record(oid, desk_of.get(oid)) if posts.get(oid) else None
    if rec:
        post_records.append(rec)
        post_ids_written.add(oid)
        if oid not in obs_ids:
            obs.append(make_obs(oid, NEW_AT))
            obs_ids.add(oid)

# drop ids we still cannot record from sweeps/trends
valid = known | post_ids_written
for s in sweeps:
    s["post_ids"] = [i for i in s["post_ids"] if i in valid]
for t in trends:
    t["post_ids"] = [i for i in t["post_ids"] if i in valid]

context = [{
    "post_id": CONTEXT_ID,
    "replies": ctx_reply_ids,
    "quotes": ctx_quote_ids,
}] if CONTEXT_ID in valid else []

# ---------- run reason ----------
vol_ok = all(n == 167 and sm == meta for n, sm, meta in vol_sums.values())
cap_note = ""
if dropped_cap:
    cap_note = " account cap dropped " + json.dumps({k: dropped_cap[k] for k in sorted(dropped_cap)}) + "."
sex_note = f" Left out: {len(skipped_sexual)} sexual, 0 ad, 0 minor-related" + (f" ({', '.join(skipped_sexual)})" if skipped_sexual else "") + "."

word_note = (
    f"{len(truncation_ids)} truncation-only diffs where note_tweet filled truncated text or entities were unescaped or a trailing t.co link was dropped "
    f"({len(cited_trunc)} of them cited); {len(uncited_word)} uncited text change(s)"
    + (f" ({', '.join(uncited_word)})" if uncited_word else "")
    + f" ({len(cited_word)} cited)"
    + (f" ({', '.join(cited_word)})" if cited_word else "")
    + "."
)
cited_missing = [i for i in watch_ids if i in cited and i not in posts]
cited_changed = cited_word
cited_status = "no pulse- or story-cited post missing or changed words"
if cited_missing or cited_changed:
    cited_status = (
        ("cited missing: " + ", ".join(cited_missing) + "; " if cited_missing else "")
        + ("cited word changes: " + ", ".join(cited_changed) if cited_changed else "")
    ).rstrip("; ")

reason = (
    f"Day-band run 2026-11-08T0300Z / 10:00 PM EST Nov 7. requests/plan.json for_run 2026-11-08T03Z "
    f"(written_at 2026-11-08T02:11:44.963Z) used as the read list unchanged (run.plan 2026-11-08T03Z; nothing written to requests/). "
    f"31 X reads used against the plan's 31 line items (883 left before by the plan and by X's count, 852 left today after). "
    f"Watch: {800-len(unavailable)} of 800 returned"
    + (f"; unavailable {', '.join(unavailable)}" if unavailable else "")
    + f"; {len(omitted)} watch.json ids omitted from the plan list not re-read; "
    f"{cited_status}; {word_note} "
    f"4 due desks (politics, entertainment, sports, internet). "
    f"Volume defense/justice/disaster/markets (window 2026-11-01T04:00Z to 2026-11-08T03:00Z, 167 buckets, sums match). "
    f"Sensors culture/sports/online. Trend names Kentucky, #AEWCollision and Tennessee "
    f"(first three US top-ten names with no posts attached in 0200Z). Rising words just/what (quoted). "
    f"Screen: 3 by-id reads (300 ids: unread referenced origins first, then the youngest-first candidates under 6 h). "
    f"context.top on ChienSurpris {CONTEXT_ID} (biggest kept new under-24h post of this run; 0 replies and 0 quotes kept from the 20-minute window)."
    f"{sex_note}{cap_note} Media descriptions not filled this run (partial)."
)

# no em dash check on written fields
assert "\u2014" not in reason

doc = {
    "schema": "mts.capture/1",
    "run": {
        "id": RUN_ID,
        "started_at": STARTED,
        "finished_at": FINISHED,
        "status": "partial",
        "reason": reason,
        "grabber": {
            "agent": "grokbot",
            "model": None,
            "method": "x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid, get_posts_counts_recent)",
        },
        "requests_rev": REQUESTS_REV,
        "reads": 31,
        "reads_left": 852,
        "plan": "2026-11-08T03Z",
    },
    "sweeps": sweeps,
    "trends": trends,
    "posts": post_records,
    "observations": obs,
    "context": context,
    "answers": [],
    "volume": volume,
}

out_path = REPO / "capture/2026/11/08/0300Z.json"
out_path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")

# TALLY
tally_path = REPO / "capture/TALLY.json"
tally = json.loads(tally_path.read_text())
origins = []
seen = set()
for name in ("rising.just", "rising.what"):
    for oid in source_results[name]["origin_ids"]:
        if oid not in seen:
            origins.append(oid)
            seen.add(oid)
tally["runs"] = (tally.get("runs") or []) + [{"run": RUN_ID, "origins": origins}]
tally["runs"] = tally["runs"][-6:]
tally_path.write_text(json.dumps(tally, ensure_ascii=False, indent=1) + "\n")

# NOTES
notes_path = REPO / "capture/NOTES.md"
note_line = (
    "- 2026-11-08 0300Z: 03Z plan executed on time (requests/plan.json, for_run 2026-11-08T03Z, "
    "written 02:11:44Z, read directly and used unchanged; 31 of the 31 planned reads under the day allowance of 42"
    f"; watch {800-len(unavailable)}/800, unavailable {len(unavailable)}"
    f"; sensors culture/sports/online; trend names Kentucky/#AEWCollision/Tennessee; rising just/what"
    f"; context empty window on {CONTEXT_ID}"
    + (f"; account cap dropped {json.dumps(dropped_cap, separators=(', ', ': '))}" if dropped_cap else "")
    + "; media descriptions not filled).\n"
)
assert "\u2014" not in note_line
txt = notes_path.read_text()
if "2026-11-08 0300Z:" not in txt:
    if not txt.endswith("\n"):
        txt += "\n"
    notes_path.write_text(txt + note_line)

meta = {
    "posts": len(post_records),
    "obs": len(obs),
    "unavailable": unavailable,
    "truncation": truncation_ids,
    "word_changes": word_ids,
    "cited_word": cited_word,
    "cited_trunc": cited_trunc,
    "cited_missing": cited_missing,
    "dropped_cap": dropped_cap,
    "skipped_sexual": skipped_sexual,
    "keep_n": len(keep_ids),
    "vol_sums": vol_sums,
    "missing_needed": [i for i in needed if i not in valid],
}
(WD / "build_meta.json").write_text(json.dumps(meta, indent=2))
print(json.dumps(meta, indent=2))
print("wrote", out_path, "bytes", out_path.stat().st_size)
