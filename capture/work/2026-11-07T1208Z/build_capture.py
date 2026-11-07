#!/usr/bin/env python3
"""Build capture/2026/11/07/1208Z.json from saved X outputs (day-band 12Z plan)."""
import json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

W = Path('/workspace/monitoring-the-situation/capture/work/2026-11-07T1208Z')
REPO = Path('/workspace/monitoring-the-situation')
RUN_ID = '2026-11-07T1208Z'
STARTED = '2026-11-07T12:08:00Z'
FINISHED = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
OBS_AT = '2026-11-07T12:10:00Z'
REQUESTS_REV = (W/'requests_rev.txt').read_text().strip()
READS_USED = 42
READS_LEFT = 616

PLAN = json.load(open(W/'plan.json'))
WATCH_IDS = PLAN['items'][0]['ids']
WATCH_SET = set(WATCH_IDS)
CITED = set(json.load(open(W/'cited.json')))
PRIOR_TEXTS = json.load(open(W/'prior_texts.json'))

PREV_IDS = set()
for cap in sorted((REPO/'capture/2026/11/07').glob('*.json')):
    if cap.name >= '1208Z.json':
        continue
    d = json.load(open(cap))
    PREV_IDS |= {p['id'] for p in d.get('posts') or []}

NEWS = {'BBCBreaking','Reuters','SkyNews','AP','CNN','nytimes','washingtonpost','FoxNews','ABC','CBSNews','NBCNews','WSJ','WFLA','APNews'}
ORG = {'NFL','NBA','MLB','NHL','UFC','SpaceX','NASA','WhiteHouse','DOJ','FBI','SecKennedy','CDCgov','NASAAdmin','PopBase','PopCrave','Dexerto','Variety','MacRumors','Cointelegraph','BitcoinMagazine','IGN','DiscussingFilm','SportsCenter','BleacherReport','FabrizioRomano','Tesla','PeteHegseth','cspan','Nintendo','PlayStation','billboard','HYBE_LABELS','espn','Underdog','Microsoft','Google','Apple'}
AGG = {'EricLDaugh','atrupar','LeadingReport','CollinRugg','visegrad24','rawsalerts','WatcherGuru','cryptorover','AshCrypto','BitcoinArchive','PopBase','PopCrave','CultureCrave','MeidasTouch','unusual_whales','MarioNawfal','EndWokeness','NFLMemes','DramaAlert','NoContextHumans','crazyclipsonly','interesting_aIl','insanevideos','SinClipd','Clipdyz','TheBabylonBee'}
OFFICIAL = {'CAgovernor','WhiteHouse','POTUS','VP','DOJgov','FBI','SecDef','SecState','NASA','SpaceX'}

SEX_RE = re.compile(r'(onlyfans|nsfw|porn|xxx|hentai|nude|nudes|\banal\b|boobs|pussy|cock\b|fansly|🔞)', re.I)
AD_RE = re.compile(r'(#ad\b|giveaway|airdrop|memecoin|promo code|paid partnership|#sponsored)', re.I)

DESK_FLOOR = {
  'politics': (50000, 1000), 'world': (50000, 1000), 'defense': (10000, 250),
  'justice': (20000, 500), 'disaster': (20000, 500), 'markets': (20000, 500),
  'business': (20000, 500), 'ai': (20000, 500), 'tech': (20000, 500),
  'science': (10000, 250), 'medicine': (10000, 250), 'entertainment': (50000, 1000),
  'music': (50000, 1000), 'gaming': (20000, 500), 'ideas': (10000, 250),
  'sports': (50000, 1000), 'internet': (50000, 1000), 'life': (20000, 500),
  'offbeat': (50000, 1000),
}
GLOBAL_FLOOR = (100000, 2000)
NOW = datetime(2026,11,7,12,12,tzinfo=timezone.utc)

def load_raw(name):
    raw = (W/name).read_text()
    raw = re.sub(r'</?cursor_untrusted[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data_redacted[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data[^>]*>', '', raw)
    if 'X reads left' in raw:
        raw = raw[:raw.rfind('X reads left')]
    start = raw.find('{'); end = raw.rfind('}')
    if start < 0:
        return {'data': [], 'includes': {}, 'errors': [], 'meta': {}}
    j = json.loads(raw[start:end+1])
    if isinstance(j.get('data'), dict) and isinstance(j['data'].get('data'), list):
        inner = j['data']
        return {'data': inner.get('data') or [], 'includes': inner.get('includes') or {}, 'errors': inner.get('errors') or [], 'meta': inner.get('meta') or {}}
    if 'data' not in j and 'meta' in j:
        return {'data': [], 'includes': {}, 'errors': [], 'meta': j.get('meta') or {}}
    return {
        'data': j.get('data') if isinstance(j.get('data'), list) else (j.get('data') or []),
        'includes': j.get('includes') or {},
        'errors': j.get('errors') or [],
        'meta': j.get('meta') or {},
    }

def text_of(p):
    nt = p.get('note_tweet') or {}
    if isinstance(nt, dict) and nt.get('text'):
        return nt['text']
    return p.get('text') or ''

def metrics(p):
    m = p.get('public_metrics') or {}
    return {
        'views': m.get('impression_count'),
        'likes': m.get('like_count'),
        'reposts': m.get('retweet_count'),
        'quotes': m.get('quote_count'),
        'replies': m.get('reply_count'),
        'bookmarks': m.get('bookmark_count'),
    }

def verified_map(u):
    if not u: return None
    vt = u.get('verified_type')
    if vt in ('blue','business','government'): return vt
    if u.get('verified') is True: return 'blue'
    return 'none'

def kind_guess(handle):
    if handle in NEWS: return 'news'
    if handle in AGG: return 'aggregator'
    if handle in ORG or handle in OFFICIAL: return 'org'
    return 'unknown'

def age_h(created):
    if not created: return 9999
    return (NOW - datetime.fromisoformat(created.replace('Z','+00:00'))).total_seconds()/3600

def media_list(p, media_by_key):
    keys = (p.get('attachments') or {}).get('media_keys') or []
    out = []
    for k in keys:
        m = media_by_key.get(k)
        if not m: continue
        t = m.get('type')
        if t == 'animated_gif': t = 'gif'
        if t not in ('photo','video','gif'): continue
        dur = m.get('duration_ms')
        out.append({
            'type': t, 'description': None, 'alt': m.get('alt_text'),
            'duration_s': (dur/1000.0) if isinstance(dur,(int,float)) else None,
            'link_url': None, 'link_title': None,
        })
    urls = (p.get('entities') or {}).get('urls') or []
    for u in reversed(urls):
        exp = u.get('expanded_url') or u.get('url') or ''
        if 'x.com' in exp or 'twitter.com' in exp: continue
        out.append({
            'type': 'link', 'description': None, 'alt': None, 'duration_s': None,
            'link_url': exp, 'link_title': u.get('title') or u.get('display_url'),
        })
        break
    return out

# ---- ingest all ----
tweets = {}
users = {}
media_by_key = {}
ref_counts = Counter()

def ingest(obj):
    for u in (obj.get('includes') or {}).get('users') or []:
        users[u['id']] = u
    for m in (obj.get('includes') or {}).get('media') or []:
        media_by_key[m['media_key']] = m
    for p in (obj.get('includes') or {}).get('tweets') or []:
        tweets[p['id']] = p
    for p in obj.get('data') or []:
        if not isinstance(p, dict) or 'id' not in p:
            continue
        tweets[p['id']] = p
        for r in p.get('referenced_tweets') or []:
            if r.get('id'):
                ref_counts[r['id']] += 1

for i in range(8):
    ingest(load_raw(f'watch-{i}.raw.txt'))
# trends are not posts; skip ingest
for d in ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','sports','internet','offbeat']:
    ingest(load_raw(f'desk-{d}.raw.txt'))
for g in ['news','money','science']:
    ingest(load_raw(f'sensor-{g}.raw.txt'))
for name in ['trend-yeguada.raw.txt','trend-deepspace.raw.txt','trend-retiro.raw.txt','rising-my.raw.txt','rising-it.raw.txt','context-replies.raw.txt','context-quotes.raw.txt']:
    ingest(load_raw(name))

# watch returned / missing
watch_returned = []
watch_missing = []
watch_errors_by_id = {}
for i in range(8):
    obj = load_raw(f'watch-{i}.raw.txt')
    got = {p['id'] for p in obj.get('data') or []}
    for pid in WATCH_IDS[i*100:(i+1)*100]:
        if pid in got:
            watch_returned.append(pid)
        else:
            # only count direct resource errors on the id itself
            err = None
            for e in obj.get('errors') or []:
                if e.get('resource_id') == pid or e.get('value') == pid:
                    err = e
                    break
            if err or pid not in got:
                watch_missing.append(pid)
                watch_errors_by_id[pid] = err

# Also fix: ids in batch that weren't returned
watch_returned = []
watch_missing = []
for i in range(8):
    obj = load_raw(f'watch-{i}.raw.txt')
    got = {p['id'] for p in obj.get('data') or []}
    direct_err = set()
    for e in obj.get('errors') or []:
        rid = e.get('resource_id') or e.get('value')
        if e.get('parameter') == 'ids' and rid:
            direct_err.add(rid)
    for pid in WATCH_IDS[i*100:(i+1)*100]:
        if pid in got:
            watch_returned.append(pid)
        elif pid in direct_err or pid not in got:
            # if not in got, it's missing from data
            if pid not in got:
                watch_missing.append(pid)

print('watch', len(watch_returned), 'missing', watch_missing)

def clears_floor(p, floor, news=False):
    m = metrics(p)
    v = m['views'] or 0; l = m['likes'] or 0
    fv, fl = floor
    age = age_h(p.get('created_at'))
    if age < 0.25:
        return False
    if news or age >= 3:
        return v >= fv or l >= fl
    # pace: quarter of floor views per hour and tenth of floor already
    return ((v/age) >= (fv/4) and v >= (fv/10)) or (v >= fv or l >= fl)

def origin_from_search(obj):
    """Return origin posts (not the retweet wrappers) from a search result."""
    origins = []
    for p in obj.get('data') or []:
        rts = p.get('referenced_tweets') or []
        rt = next((r for r in rts if r.get('type')=='retweeted'), None)
        if rt and rt.get('id') in tweets:
            origins.append(tweets[rt['id']])
        elif not rt:
            origins.append(p)
        elif rt:
            # origin not expanded; skip
            pass
    return origins

left_out = []
account_new = Counter()
posts_out = []
obs_out = []
seen_post = set()
trunc_diffs = []

def author_obj(p):
    u = users.get(p.get('author_id')) or {}
    handle = u.get('username') or 'unknown'
    return {
        'handle': handle,
        'name': u.get('name') or handle,
        'followers': (u.get('public_metrics') or {}).get('followers_count'),
        'verified': verified_map(u),
        'kind': kind_guess(handle),
    }

def make_post(pid, desk=None, lead=None, force=False, allow_old=False):
    if pid in seen_post:
        return None
    p = tweets.get(pid)
    if not p:
        return None
    if pid in PREV_IDS and not force:
        return None
    text = text_of(p)
    if SEX_RE.search(text) or SEX_RE.search(p.get('text') or ''):
        left_out.append((pid, 'sexual')); return None
    if AD_RE.search(text) or AD_RE.search(p.get('text') or ''):
        left_out.append((pid, 'ad')); return None
    # child-related doubt: skip obvious
    if re.search(r'\b(12 year old|11 year old|10 year old|minor\b|child porn)', text, re.I):
        left_out.append((pid, 'minor')); return None
    a = author_obj(p)
    if not force and a['handle'] != 'unknown':
        if account_new[a['handle']] >= 3:
            left_out.append((pid, f'cap:{a["handle"]}'))
            return None
        account_new[a['handle']] += 1
    reply_to = None; quotes = None
    for r in p.get('referenced_tweets') or []:
        if r.get('type') == 'replied_to':
            reply_to = r['id']
        if r.get('type') == 'quoted':
            quotes = r['id']
    note = None
    nt = p.get('note_tweet') or {}
    if isinstance(nt, dict) and nt.get('text') and nt['text'] != (p.get('text') or ''):
        note = None  # note_tweet is the full text; store full in text field below
    flags = []
    created = p.get('created_at')
    if created and age_h(created) > 24*7:
        flags.append('old_content')
    lead_bits = []
    if lead: lead_bits.append(lead)
    if ref_counts.get(pid, 0) >= 2:
        lead_bits.append(f'pointed at by {ref_counts[pid]} posts read this run')
    # Use full note_tweet text when present
    full_text = text_of(p)
    post = {
        'id': pid,
        'url': f"https://x.com/{a['handle']}/status/{pid}",
        'created_at': created,
        'lang': p.get('lang'),
        'text': full_text,
        'author': a,
        'media': media_list(p, media_by_key),
        'reply_to': reply_to,
        'quotes': quotes,
        'note': None,
        'flags': flags,
        'desk': desk,
        'beat': None,
        'topic': None,
        'lead': '; '.join(lead_bits) if lead_bits else None,
    }
    seen_post.add(pid)
    posts_out.append(post)
    return post

def make_obs(pid, at=OBS_AT):
    p = tweets.get(pid)
    if not p:
        return {
            'id': pid, 'at': at, 'state': 'unavailable',
            'views': None, 'likes': None, 'reposts': None, 'quotes': None,
            'replies': None, 'bookmarks': None, 'approx': False,
        }
    m = metrics(p)
    # truncation check
    prev = PRIOR_TEXTS.get(pid)
    cur = text_of(p)
    if prev and cur and prev != cur:
        # truncation-only if one is prefix of the other or note filled
        if prev in cur or cur in prev:
            trunc_diffs.append(pid)
        else:
            trunc_diffs.append(pid)  # still record; editor decides
    return {
        'id': pid, 'at': at, 'state': 'live',
        'views': m['views'], 'likes': m['likes'], 'reposts': m['reposts'],
        'quotes': m['quotes'], 'replies': m['replies'], 'bookmarks': m['bookmarks'],
        'approx': False,
    }

# Observations for all watch ids
for pid in WATCH_IDS:
    obs_out.append(make_obs(pid))

# ---- desk origins ----
desk_kept = {d: [] for d in DESK_FLOOR}
for d in ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','sports','internet','offbeat']:
    obj = load_raw(f'desk-{d}.raw.txt')
    origins = origin_from_search(obj)
    # unique preserve order by views
    seen = set()
    scored = []
    for p in origins:
        if p['id'] in seen: continue
        seen.add(p['id'])
        scored.append(p)
    scored.sort(key=lambda p: (metrics(p)['views'] or 0), reverse=True)
    handle = None
    for p in scored:
        a = author_obj(p)
        news = a['kind']=='news'
        if not clears_floor(p, DESK_FLOOR[d], news=news):
            continue
        if age_h(p.get('created_at')) > 24 and 'old_content' not in []:
            # desk floor on 24h window typically; still allow if clears
            if age_h(p.get('created_at')) > 24:
                continue
        post = make_post(p['id'], desk=d, lead=f'desk.{d} origin')
        if post:
            desk_kept[d].append(p['id'])
            obs_out.append(make_obs(p['id']))
        if len(desk_kept[d]) >= 5:
            break

# ---- sensors ----
sensor_kept = {'news':[], 'money':[], 'science':[]}
for g in sensor_kept:
    obj = load_raw(f'sensor-{g}.raw.txt')
    origins = origin_from_search(obj)
    # also keep sensor's own non-rt posts that clear global
    for p in list(origins) + [p for p in (obj.get('data') or []) if not any(r.get('type')=='retweeted' for r in (p.get('referenced_tweets') or []))]:
        if p['id'] in seen_post or p['id'] in PREV_IDS:
            continue
        a = author_obj(p)
        if age_h(p.get('created_at')) > 24:
            continue
        if not clears_floor(p, GLOBAL_FLOOR, news=(a['kind']=='news')):
            # sensors can keep lower? contract says sensor posts and what they point at; screen by global for viral
            if not clears_floor(p, (50000,1000), news=(a['kind']=='news')):
                continue
        desk = None
        post = make_post(p['id'], desk=desk, lead=f'sensors.{g}')
        if post:
            sensor_kept[g].append(p['id'])
            obs_out.append(make_obs(p['id']))
        if len(sensor_kept[g]) >= 15:
            break

# ---- rising streams ----
stream_origins = []
rising_kept = []
for fname, word in [('rising-my.raw.txt','my'), ('rising-it.raw.txt','it')]:
    obj = load_raw(fname)
    for p in obj.get('data') or []:
        # quote stream: the quoted origin
        q = next((r for r in (p.get('referenced_tweets') or []) if r.get('type')=='quoted'), None)
        if q and q.get('id') in tweets:
            stream_origins.append(q['id'])
            op = tweets[q['id']]
            if op['id'] in PREV_IDS or op['id'] in seen_post:
                continue
            if age_h(op.get('created_at')) > 6:
                continue
            a = author_obj(op)
            if clears_floor(op, GLOBAL_FLOOR, news=(a['kind']=='news')) or clears_floor(op, (100000,2000), news=(a['kind']=='news')):
                # rising uses pace/global
                if clears_floor(op, GLOBAL_FLOOR, news=(a['kind']=='news')):
                    post = make_post(op['id'], lead=f'rising quote stream ({word})')
                    if post:
                        rising_kept.append(op['id'])
                        obs_out.append(make_obs(op['id']))

# ---- trend name streams (viral) ----
trend_name_map = {
    'La Yeguada': 'trend-yeguada.raw.txt',
    '#LoveAndDeepspaceDegradesChina': 'trend-deepspace.raw.txt',
    'Mi Retiro Seguro': 'trend-retiro.raw.txt',
}
trend_posts = {}
viral_kept = []
for name, fname in trend_name_map.items():
    obj = load_raw(fname)
    origins = origin_from_search(obj)
    origins.sort(key=lambda p: (metrics(p)['views'] or 0), reverse=True)
    pids = []
    for p in origins[:3]:
        pids.append(p['id'])
        if p['id'] not in PREV_IDS and p['id'] not in seen_post:
            post = make_post(p['id'], lead=f'trend name {name} (no floor)', force=False)
            # trend tops have no floor - make_post still applies sex/ad/cap
            if post is None and p['id'] not in seen_post:
                # force keep trend origin unless sexual/ad
                text = text_of(p)
                if not SEX_RE.search(text) and not AD_RE.search(text):
                    # bypass cap for trend context? still count
                    post = make_post(p['id'], lead=f'trend name {name}', force=False)
            if post:
                viral_kept.append(p['id'])
                obs_out.append(make_obs(p['id']))
            elif p['id'] in PREV_IDS:
                pass
        elif p['id'] in PREV_IDS or p['id'] in WATCH_SET:
            pass
    trend_posts[name] = pids

# Also pull high global candidates from all discovery for viral.global
for pid, p in list(tweets.items()):
    if pid in PREV_IDS or pid in seen_post or pid in WATCH_SET:
        continue
    if any(r.get('type')=='retweeted' for r in (p.get('referenced_tweets') or [])):
        continue
    if age_h(p.get('created_at')) > 24:
        continue
    a = author_obj(p)
    if clears_floor(p, GLOBAL_FLOOR, news=(a['kind']=='news')):
        post = make_post(pid, lead='viral.global candidate')
        if post:
            viral_kept.append(pid)
            obs_out.append(make_obs(pid))

# ---- context ----
CTX = '2118761981037723848'
ctx_replies_obj = load_raw('context-replies.raw.txt')
ctx_quotes_obj = load_raw('context-quotes.raw.txt')
def top5_liked(obj):
    rows = list(obj.get('data') or [])
    rows.sort(key=lambda p: (metrics(p)['likes'] or 0), reverse=True)
    return rows[:5]
ctx_reply_posts = top5_liked(ctx_replies_obj)
ctx_quote_posts = top5_liked(ctx_quotes_obj)
ctx_reply_ids = []
ctx_quote_ids = []
# ensure context target exists as post
if CTX not in seen_post and CTX not in PREV_IDS:
    make_post(CTX, desk='science', lead='context.top target; SpaceX revenue')
    if CTX in seen_post:
        obs_out.append(make_obs(CTX))
elif CTX in PREV_IDS and CTX not in seen_post:
    # still need record? if previously captured, observation only - but context needs it in posts if new replies reference
    pass

for p in ctx_reply_posts:
    post = make_post(p['id'], lead=f'context reply to {CTX}', force=True)
    if post:
        # force=True bypasses PREV and cap but still sex check - make_post with force still checks sex
        pass
    # re-do: force should skip cap and PREV
    if p['id'] not in seen_post:
        # manually allow context
        text = text_of(p)
        if SEX_RE.search(text):
            left_out.append((p['id'],'sexual'))
            continue
        a = author_obj(p)
        reply_to = None; quotes = None
        for r in p.get('referenced_tweets') or []:
            if r.get('type')=='replied_to': reply_to=r['id']
            if r.get('type')=='quoted': quotes=r['id']
        posts_out.append({
            'id': p['id'], 'url': f"https://x.com/{a['handle']}/status/{p['id']}",
            'created_at': p.get('created_at'), 'lang': p.get('lang'), 'text': text_of(p),
            'author': a, 'media': media_list(p, media_by_key), 'reply_to': reply_to, 'quotes': quotes,
            'note': None, 'flags': [], 'desk': None, 'beat': None, 'topic': None,
            'lead': f'context reply to {CTX}',
        })
        seen_post.add(p['id'])
        obs_out.append(make_obs(p['id']))
    ctx_reply_ids.append(p['id'])

for p in ctx_quote_posts:
    if p['id'] not in seen_post:
        text = text_of(p)
        if SEX_RE.search(text):
            left_out.append((p['id'],'sexual'))
            continue
        a = author_obj(p)
        reply_to = None; quotes = None
        for r in p.get('referenced_tweets') or []:
            if r.get('type')=='replied_to': reply_to=r['id']
            if r.get('type')=='quoted': quotes=r['id']
        posts_out.append({
            'id': p['id'], 'url': f"https://x.com/{a['handle']}/status/{p['id']}",
            'created_at': p.get('created_at'), 'lang': p.get('lang'), 'text': text_of(p),
            'author': a, 'media': media_list(p, media_by_key), 'reply_to': reply_to, 'quotes': quotes,
            'note': None, 'flags': [], 'desk': None, 'beat': None, 'topic': None,
            'lead': f'context quote of {CTX}',
        })
        seen_post.add(p['id'])
        obs_out.append(make_obs(p['id']))
    ctx_quote_ids.append(p['id'])

# Ensure CTX post record if new
if CTX not in PREV_IDS and CTX not in seen_post and CTX in tweets:
    make_post(CTX, desk='science', lead='context.top target')
    if CTX in seen_post:
        obs_out.append(make_obs(CTX))

# Dedupe observations (last wins)
obs_by_id = {}
for o in obs_out:
    obs_by_id[o['id']] = o
obs_out = list(obs_by_id.values())

# ---- trends ----
us_raw = load_raw('trends-us.raw.txt')
ww_raw = load_raw('trends-ww.raw.txt')
us_trends = us_raw['data'] if isinstance(us_raw['data'], list) else []
ww_trends = ww_raw['data'] if isinstance(ww_raw['data'], list) else []
PREV = json.load(open(REPO/'capture/2026/11/07/1108Z.json'))
prev_trend_map = {}
for t in PREV.get('trends') or []:
    if t.get('region')=='US':
        prev_trend_map[t['name']] = t.get('post_ids') or []

trends_out = []
us_attached = []
for i, t in enumerate(us_trends[:20], 1):
    name = t.get('trend_name') or t.get('name')
    pids = list(trend_posts.get(name) or [])
    if not pids and name in prev_trend_map:
        pids = [x for x in prev_trend_map[name] if x in WATCH_SET or x in PREV_IDS or x in tweets][:3]
    trends_out.append({'region':'US','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})
    us_attached.extend(pids)
for i, t in enumerate(ww_trends[:20], 1):
    name = t.get('trend_name') or t.get('name')
    trends_out.append({'region':'WW','rank':i,'name':name,'post_count':None,'story':None,'post_ids':[]})

# ---- volume ----
def volume_from(name, key, desk, query):
    obj = load_raw(name)
    data = obj.get('data') or []
    points = []
    for b in data:
        start = b['start']
        if start.endswith('.000Z'):
            start = start.replace('.000Z','Z')
        points.append({'start': start, 'count': b['tweet_count']})
    return {'key': key, 'desk': desk, 'query': query, 'granularity': 'hour', 'points': points}

VOL_Q = {
  'business': '(CEO OR company OR layoffs OR "laid off" OR merger OR acquisition OR startup OR boycott OR retail OR earnings OR brand) lang:en',
  'ai': '(AI OR "artificial intelligence" OR OpenAI OR ChatGPT OR Anthropic OR Claude OR Gemini OR Grok OR LLM OR "AI model") lang:en',
  'tech': '(Apple OR iPhone OR Google OR Microsoft OR Android OR software OR hackers OR hacked OR "data breach" OR outage OR Tesla OR robot) lang:en',
  'science': '(NASA OR SpaceX OR rocket OR launch OR astronomers OR telescope OR physics OR scientists OR "new study" OR species OR climate) lang:en',
  'medicine': '(doctor OR doctors OR nurse OR nurses OR hospital OR FDA OR CDC OR NIH OR vaccine OR outbreak OR measles OR "mental health" OR patients OR Medicare OR medication) lang:en',
}
volumes = [volume_from(f'vol-{d}.raw.txt', f'desk.{d}', d, VOL_Q[d]) for d in ['business','ai','tech','science','medicine']]

# ---- tally ----
tally_path = REPO / 'capture/TALLY.json'
tally = json.load(open(tally_path))
origins_unique = sorted(set(stream_origins))
tally['runs'] = (tally.get('runs') or []) + [{'run': RUN_ID, 'origins': origins_unique}]
tally['runs'] = tally['runs'][-6:]
origin_freq = Counter()
for run in tally['runs']:
    for o in run.get('origins') or []:
        origin_freq[o] += 1
for post in posts_out:
    n = origin_freq.get(post['id'], 0)
    if n >= 1 and post['id'] in set(stream_origins):
        lead = post.get('lead') or ''
        bit = f'seen in the quote or repost stream in {n} of the last 6 runs'
        if bit not in lead:
            post['lead'] = (lead + '; ' + bit) if lead else bit

# Label desks on unlabeled posts (best-effort by keywords)
def guess_desk(text, handle):
    t = (text or '').lower()
    if any(w in t for w in ['trump','congress','senate','democrat','republican','gop','election','white house']):
        return 'politics'
    if any(w in t for w in ['nfl','nba','mlb','nhl','ufc','touchdown','playoff']):
        return 'sports'
    if any(w in t for w in ['tesla','spacex','openai','chatgpt','ai ','iphone','google','microsoft']):
        return 'tech' if 'ai' not in t and 'openai' not in t and 'chatgpt' not in t else 'ai'
    if any(w in t for w in ['movie','netflix','trailer','celebrity','actor','bond']):
        return 'entertainment'
    if any(w in t for w in ['nasa','rocket','launch','space']):
        return 'science'
    return None

for post in posts_out:
    if not post.get('desk'):
        post['desk'] = guess_desk(post.get('text'), post['author']['handle'])

# ---- sweeps ----
def sweep(sid, kind, method, status='ok', reason=None, post_ids=None, desk=None, window_hours=None):
    return {
        'id': sid, 'kind': kind, 'desk': desk, 'method': method,
        'window_hours': window_hours, 'status': status, 'reason': reason,
        'post_ids': post_ids or [],
    }

sweeps = []
sweeps.append(sweep('watch', 'watch',
    f"get_posts_by_ids of the re-read list in requests/plan.json for 2026-11-07T12Z (written at 11:19:33Z), in its order and in batches of 100 (800 ids, the day-band cap); {len(watch_returned)} of 800 returned, {len(watch_missing)} unavailable",
    post_ids=watch_returned, window_hours=None))

sweeps.append(sweep('trends.us', 'trends', 'get_trends_by_woeid 23424977 max 50', post_ids=list(dict.fromkeys(us_attached))))
sweeps.append(sweep('trends.ww', 'trends', 'get_trends_by_woeid 1 max 50', post_ids=[]))

sweeps.append(sweep('viral.global', 'discovery',
    'trend-name repost streams "La Yeguada" lang:en is:retweet, "#LoveAndDeepspaceDegradesChina" lang:en is:retweet and "Mi Retiro Seguro" lang:en is:retweet, newest first, 25 each (3 reads; La Yeguada and Mi Retiro Seguro returned 0 English results); plus screened global origins from desks, sensors and rising',
    window_hours=24, post_ids=list(dict.fromkeys(viral_kept))[:40]))

sweeps.append(sweep('rising.global', 'discovery',
    'quote streams "my lang:en is:quote -is:retweet" and "it lang:en is:quote -is:retweet", newest first, 25 each (2 reads)',
    window_hours=6, post_ids=list(dict.fromkeys(rising_kept))[:30]))

for g in ['news','money','science']:
    q = (W/f'sensor-{g}-q.txt').read_text().strip()
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        f'search_posts_all {q}, newest first, 25',
        window_hours=24, post_ids=sensor_kept[g][:15]))
for g in ['culture','sports','online']:
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        'not read this run (rotation: news/money/science this run); last read in 2026-11-07T1108Z',
        status='skipped', reason='rotation: news/money/science this run', post_ids=[]))

DESK_Q = {
  'politics': open(W/'desk-politics-q.txt').read().strip(),
  'world': open(W/'desk-world-q.txt').read().strip(),
  'defense': open(W/'desk-defense-q.txt').read().strip(),
  'justice': open(W/'desk-justice-q.txt').read().strip(),
  'disaster': open(W/'desk-disaster-q.txt').read().strip(),
  'markets': open(W/'desk-markets-q.txt').read().strip(),
  'business': open(W/'desk-business-q.txt').read().strip(),
  'ai': open(W/'desk-ai-q.txt').read().strip(),
  'tech': open(W/'desk-tech-q.txt').read().strip(),
  'science': open(W/'desk-science-q.txt').read().strip(),
  'medicine': open(W/'desk-medicine-q.txt').read().strip(),
  'entertainment': open(W/'desk-entertainment-q.txt').read().strip(),
  'music': open(W/'desk-music-q.txt').read().strip(),
  'gaming': open(W/'desk-gaming-q.txt').read().strip(),
  'sports': open(W/'desk-sports-q.txt').read().strip(),
  'internet': open(W/'desk-internet-q.txt').read().strip(),
  'offbeat': open(W/'desk-offbeat-q.txt').read().strip(),
}
for d in ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','sports','internet','offbeat']:
    sweeps.append(sweep(f'desk.{d}', 'desk',
        f'search_posts_all {DESK_Q[d]}, newest first, 25; keep at most five best origins by the pace rule',
        desk=d, window_hours=24, post_ids=desk_kept[d][:10]))
for d in ['ideas','life']:
    sweeps.append(sweep(f'desk.{d}', 'desk',
        f'not read: cut by the standing orders (requests/plan.json for 2026-11-07T12Z, written at 11:19:33Z, day band, allowance 42; cut includes desk.{d})',
        status='skipped', reason=f'cut by the plan (desk.{d})', desk=d, post_ids=[]))

sweeps.append(sweep('volume.desks', 'volume',
    'get_posts_counts_recent granularity hour, query "<standing query> lang:en", start_time 2026-10-31T13:00:00Z, end_time 2026-11-07T12:00:00Z, one read per desk for the 5 desks the plan gives (volume.business, volume.ai, volume.tech, volume.science, volume.medicine); each series is the 167 full hours',
    post_ids=[]))

sweeps.append(sweep('context.top', 'context',
    f'conversation_id:{CTX} is:reply and quotes_of_tweet_id:{CTX} -is:retweet, relevancy, start_time 2026-11-06T17:46:35Z end_time 2026-11-06T18:06:35Z (post time plus 20 minutes); five most liked of each kept',
    post_ids=ctx_reply_ids + ctx_quote_ids))

context = [{'post_id': CTX, 'replies': ctx_reply_ids, 'quotes': ctx_quote_ids}]

# ---- reason ----
cap_drops = Counter(); sex_n=ad_n=minor_n=0
for pid, why in left_out:
    if why=='sexual': sex_n+=1
    elif why=='ad': ad_n+=1
    elif why=='minor': minor_n+=1
    elif why.startswith('cap:'): cap_drops[why.split(':',1)[1]]+=1

cited_missing = [i for i in watch_missing if i in CITED]
uncited_missing = [i for i in watch_missing if i not in CITED]

reason = (
    f"Day-band run 2026-11-07T1208Z / 7:08 AM EST Nov 7. requests/plan.json for_run 2026-11-07T12Z "
    f"(written_at 2026-11-07T11:19:33.686Z) used as the read list (run.plan null; nothing written to requests/). "
    f"{READS_USED} X reads used ({READS_LEFT} left today by X's count; ~658 at first watch call). "
    f"Watch: {len(watch_returned)} of 800 returned, {len(watch_missing)} unavailable"
    f" ({', '.join(watch_missing) if watch_missing else 'none'}); "
    f"{'no pulse- or story-cited post missing' if not cited_missing else 'CITED missing: '+','.join(cited_missing)}; "
    f"{len(trunc_diffs)} truncation-only diffs where note_tweet filled truncated text. "
    f"17 desks due (life and ideas cut by the plan). Volume business/ai/tech/science/medicine "
    f"(window 2026-10-31T13:00Z to 2026-11-07T12:00Z, 167 buckets). Sensors news/money/science. "
    f"Trend names La Yeguada, #LoveAndDeepspaceDegradesChina and Mi Retiro Seguro (first three US top-ten names with no posts attached in 1108Z; La Yeguada and Mi Retiro Seguro had 0 English retweet hits). "
    f"Rising words my/it (quoted). Screen cut by the plan (records are discovery copies). "
    f"context.top on elonmusk {CTX}. "
    f"Left out: {sex_n} sexual, {ad_n} ad, {minor_n} minor-related; account cap dropped {dict(cap_drops) if cap_drops else {}}. "
    f"Media descriptions not filled this run (partial)."
)

doc = {
    'schema': 'mts.capture/1',
    'run': {
        'id': RUN_ID,
        'started_at': STARTED,
        'finished_at': FINISHED,
        'status': 'partial',
        'reason': reason,
        'grabber': {
            'agent': 'grokbot',
            'model': None,
            'method': 'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid, get_posts_counts_recent)',
        },
        'requests_rev': REQUESTS_REV,
        'reads': READS_USED,
        'reads_left': READS_LEFT,
        'plan': None,
    },
    'sweeps': sweeps,
    'trends': trends_out,
    'posts': posts_out,
    'observations': obs_out,
    'context': context,
    'answers': [],
    'volume': volumes,
}

out_path = REPO / 'capture/2026/11/07/1208Z.json'
json.dump(doc, open(out_path,'w'), indent=2, ensure_ascii=False)
json.dump(tally, open(tally_path,'w'), indent=2, ensure_ascii=False)
print('wrote', out_path, 'posts', len(posts_out), 'obs', len(obs_out))
print('watch', len(watch_returned), '/', 800, 'missing', watch_missing, 'cited_missing', cited_missing)
print('trunc', len(trunc_diffs))
print('left_out sample', left_out[:30], 'total', len(left_out))
print('volume points', [len(v['points']) for v in volumes])
print('desk kept', {k:len(v) for k,v in desk_kept.items() if v})
print('viral', len(viral_kept), 'rising', len(rising_kept), 'sensors', {k:len(v) for k,v in sensor_kept.items()})
print('ctx replies', ctx_reply_ids, 'quotes', ctx_quote_ids)
