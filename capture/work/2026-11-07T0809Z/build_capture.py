#!/usr/bin/env python3
"""Build capture/2026/11/07/0809Z.json from saved X outputs (overnight 08Z plan)."""
import json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

W = Path('/workspace/monitoring-the-situation/capture/work/2026-11-07T0809Z')
REPO = Path('/workspace/monitoring-the-situation')
RUN_ID = '2026-11-07T0809Z'
STARTED = '2026-11-07T08:09:00Z'
FINISHED = '2026-11-07T08:16:00Z'
OBS_AT = '2026-11-07T08:12:00Z'
REQUESTS_REV = (W/'requests_rev.txt').read_text().strip()
READS_USED = 20  # 747 -> 727 (18 planned + Bond trend-name + by-id screen)
READS_LEFT = 727

PLAN = json.load(open(W/'plan08.json'))
WATCH_IDS = PLAN['items'][0]['ids']
WATCH_SET = set(WATCH_IDS)
CITED = set(json.load(open(W/'cited.json')))
PRIOR_TEXTS = json.load(open(W/'prior_texts.json'))

# Known ids from recent captures (no new record if already captured recently)
PREV_IDS = set()
for cap in sorted((REPO/'capture/2026/11/07').glob('*.json')):
    if cap.name >= '0809Z.json':
        continue
    d = json.load(open(cap))
    PREV_IDS |= {p['id'] for p in d.get('posts') or []}
    PREV_IDS |= {o['id'] for o in d.get('observations') or []}

NEWS = {'BBCBreaking','Reuters','SkyNews','AP','CNN','nytimes','washingtonpost','FoxNews','ABC','CBSNews','NBCNews','WSJ','WFLA','APNews'}
ORG = {'NFL','NBA','MLB','NHL','UFC','SpaceX','NASA','WhiteHouse','DOJ','FBI','SecKennedy','CDCgov','NASAAdmin','PopBase','PopCrave','Dexerto','Variety','MacRumors','Cointelegraph','BitcoinMagazine','IGN','DiscussingFilm','SportsCenter','BleacherReport','FabrizioRomano','Tesla','PeteHegseth','cspan','Nintendo','PlayStation','billboard','HYBE_LABELS','espnW','Underdog','TotalProSports','BleacherReport'}
AGG = {'EricLDaugh','atrupar','LeadingReport','CollinRugg','visegrad24','rawsalerts','WatcherGuru','cryptorover','AshCrypto','BitcoinArchive','PopBase','PopCrave','CultureCrave','MeidasTouch','unusual_whales','MarioNawfal','EndWokeness','NFLMemes','DramaAlert','NoContextHumans','crazyclipsonly','interesting_aIl','insanevideos','SinClipd','Clipdyz'}
OFFICIAL = {'CAgovernor','WhiteHouse','POTUS','VP','DOJgov','FBI','SecDef','SecState','NASA','SpaceX'}

SEX_RE = re.compile(r'(onlyfans|nsfw|porn|xxx|hentai|nude|nudes|\banal\b|boobs|pussy|cock\b|fansly|🔞)', re.I)
AD_RE = re.compile(r'(#ad\b|giveaway|airdrop|memecoin|promo code|paid partnership|#sponsored)', re.I)

DESK_FLOOR = {
  'politics': (50000, 1000), 'entertainment': (50000, 1000),
  'sports': (50000, 1000), 'internet': (50000, 1000),
}
GLOBAL_FLOOR = (100000, 2000)

def load_raw(name):
    raw = (W/name).read_text()
    raw = re.sub(r'</?cursor_untrusted[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data_redacted[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data[^>]*>', '', raw)
    if 'X reads left' in raw:
        raw = raw[:raw.rfind('X reads left')]
    start = raw.find('{'); end = raw.rfind('}')
    j = json.loads(raw[start:end+1])
    if isinstance(j.get('data'), dict) and isinstance(j['data'].get('data'), list):
        inner = j['data']
        return {'data': inner.get('data') or [], 'includes': inner.get('includes') or {}, 'errors': inner.get('errors') or [], 'meta': inner.get('meta') or {}}
    return j

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
    if handle in OFFICIAL: return 'official'
    if handle in NEWS: return 'news'
    if handle in AGG: return 'aggregator'
    if handle in ORG: return 'org'
    return 'unknown'

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
            'link_url': exp, 'link_title': u.get('title'),
        })
        break
    return out

def age_h(created, at=OBS_AT):
    c = datetime.fromisoformat(created.replace('Z','+00:00'))
    a = datetime.fromisoformat(at.replace('Z','+00:00'))
    return max((a-c).total_seconds()/3600.0, 0.001)

users = {}
media_by_key = {}
tweets = {}
errors_by_file = {}

def ingest(name):
    obj = load_raw(name)
    for u in (obj.get('includes') or {}).get('users') or []:
        users[u['id']] = u
    for m in (obj.get('includes') or {}).get('media') or []:
        media_by_key[m['media_key']] = m
    for p in (obj.get('includes') or {}).get('tweets') or []:
        tweets.setdefault(p['id'], p)
    for p in obj.get('data') or []:
        if isinstance(p, dict) and 'id' in p and ('text' in p or 'author_id' in p or 'public_metrics' in p):
            tweets[p['id']] = p
    errors_by_file[name] = obj.get('errors') or []
    return obj

POST_FILES = [
    'watch-0.raw.txt','watch-1.raw.txt','watch-2.raw.txt','watch-3.raw.txt',
    'desk-politics.raw.txt','desk-entertainment.raw.txt','desk-sports.raw.txt','desk-internet.raw.txt',
    'sensor-news.raw.txt','sensor-money.raw.txt','sensor-science.raw.txt',
    'trend-bond.raw.txt',
]
if (W/'screen.raw.txt').exists():
    POST_FILES.append('screen.raw.txt')
for fname in POST_FILES:
    ingest(fname)

# Watch returned / missing
watch_err_ids = set()
for name in ['watch-0.raw.txt','watch-1.raw.txt','watch-2.raw.txt','watch-3.raw.txt']:
    for e in errors_by_file.get(name) or []:
        rid = str(e.get('resource_id') or e.get('value') or '')
        # only count as missing if the requested id itself is missing
        if e.get('title') in ('Not Found Error','Authorization Error') and e.get('parameter') in (None,'ids','id'):
            watch_err_ids.add(rid)
        # also when detail says Could not find post with ids
        if 'Could not find post with IDs' in (e.get('detail') or '') or (e.get('parameter')=='ids'):
            watch_err_ids.add(rid)

watch_returned = []
watch_missing = []
for wid in WATCH_IDS:
    if wid not in tweets:
        watch_missing.append(wid)
    else:
        watch_returned.append(wid)

# Truncation / change detection vs prior texts
trunc_diffs = []
changed_cited = []
missing_cited = []
for wid in WATCH_IDS:
    if wid in watch_missing:
        if wid in CITED:
            missing_cited.append(wid)
        continue
    p = tweets[wid]
    cur = text_of(p)
    short = p.get('text') or ''
    prior = PRIOR_TEXTS.get(wid)
    if prior and cur and prior != cur:
        # truncation-only if prior is prefix of cur or cur starts with prior truncated
        if prior.startswith(cur[:20]) or cur.startswith(prior[:20]) or short in cur or (prior in cur):
            trunc_diffs.append(wid)
        else:
            if wid in CITED:
                changed_cited.append(wid)
            trunc_diffs.append(wid)  # still note

# Reference counts
ref_counts = Counter()
for name in POST_FILES:
    obj = load_raw(name)
    for p in (obj.get('data') or []) + ((obj.get('includes') or {}).get('tweets') or []):
        for r in p.get('referenced_tweets') or []:
            ref_counts[r['id']] += 1
        src = (p.get('attachments') or {}).get('media_source_tweet_id') or []
        if isinstance(src, str): src = [src]
        for mid in src:
            ref_counts[mid] += 1

def clears_floor(p, floor_views, floor_likes, news_totals_only=False):
    m = metrics(p)
    views = m['views'] or 0
    likes = m['likes'] or 0
    created = p.get('created_at')
    if not created:
        return False, None
    ah = age_h(created)
    handle = (users.get(p.get('author_id')) or {}).get('username') or ''
    is_news = handle in NEWS or kind_guess(handle)=='news'
    if ah < 0.25:  # under 15 min
        return False, 'too_young'
    if ah <= 3 and not (is_news or news_totals_only):
        # pace: views/h >= quarter floor, and already >= tenth of floor
        pace = views / ah
        if pace >= floor_views * 0.25 and views >= floor_views * 0.1:
            return True, f'pace {int(pace)}/h'
        return False, None
    # totals
    if views >= floor_views or likes >= floor_likes:
        return True, None
    return False, None

def origin_of(p):
    """Prefer retweeted/quoted/media_source origin over the carrier."""
    refs = p.get('referenced_tweets') or []
    for typ in ('retweeted','quoted'):
        for r in refs:
            if r.get('type')==typ and r['id'] in tweets:
                return tweets[r['id']], r['id'], typ
    msrc = (p.get('attachments') or {}).get('media_source_tweet_id')
    if isinstance(msrc, list): msrc = msrc[0] if msrc else None
    if msrc and msrc in tweets:
        return tweets[msrc], msrc, 'media_source'
    return p, p['id'], 'self'

left_out = []
account_new = Counter()
new_post_ids = []
posts_out = []
obs_out = []
seen_post = set()
sweep_posts = defaultdict(list)  # sweep_id -> [post ids kept]

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

def make_post(pid, desk=None, lead=None, force=False, skip_cap=False):
    if pid in seen_post: return None
    p = tweets.get(pid)
    if not p: return None
    if pid in PREV_IDS and not force:
        return None
    full = text_of(p)
    short = p.get('text') or full
    if SEX_RE.search(full):
        left_out.append((pid, 'sexual')); return None
    if AD_RE.search(full):
        left_out.append((pid, 'ad')); return None
    a = author_obj(p)
    if not force and not skip_cap and a['handle'] != 'unknown':
        if account_new[a['handle']] >= 3:
            left_out.append((pid, f'cap:{a["handle"]}'))
            return None
        account_new[a['handle']] += 1
    reply_to = None; quotes = None
    for r in p.get('referenced_tweets') or []:
        if r.get('type') == 'replied_to': reply_to = r['id']
        if r.get('type') == 'quoted': quotes = r['id']
    note = None
    if full and full != short:
        note = {'text': full}
    flags = []
    created = p.get('created_at')
    # old_content: origin more than 7 days older than referring post - checked by caller via lead
    if created and age_h(created) > 24*7:
        # only mark if we know it was reached via a young reference; for now flag if >7d from now
        # Contract: more than 7 days older than the post that led to it. Without carrier age, skip auto.
        pass
    lang = p.get('lang')
    lead_bits = []
    if lead: lead_bits.append(lead)
    if ref_counts.get(pid, 0) >= 2:
        lead_bits.append(f'pointed at by {ref_counts[pid]} posts read this run')
    msrc = (p.get('attachments') or {}).get('media_source_tweet_id')
    if isinstance(msrc, list): msrc = msrc[0] if msrc else None
    post = {
        'id': pid,
        'url': f"https://x.com/{a['handle']}/status/{pid}",
        'created_at': created,
        'lang': lang,
        'text': short,
        'author': a,
        'media': media_list(p, media_by_key),
        'reply_to': reply_to,
        'quotes': quotes,
        'note': note,
        'flags': flags,
        'desk': desk,
        'beat': None,
        'topic': None,
        'lead': '; '.join(lead_bits) if lead_bits else None,
    }
    seen_post.add(pid)
    posts_out.append(post)
    new_post_ids.append(pid)
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
    return {
        'id': pid, 'at': at, 'state': 'live',
        'views': m['views'], 'likes': m['likes'], 'reposts': m['reposts'],
        'quotes': m['quotes'], 'replies': m['replies'], 'bookmarks': m['bookmarks'],
        'approx': False,
    }

def collect_origins(raw_name, max_n=50):
    """From a search of retweets/posts, collect origin tweets with metrics."""
    obj = load_raw(raw_name)
    origins = []
    seen = set()
    for p in obj.get('data') or []:
        op, oid, how = origin_of(p)
        if oid in seen: continue
        seen.add(oid)
        origins.append((oid, op, how, p))
    # also include self posts that are not retweets (sensors)
    for p in obj.get('data') or []:
        refs = p.get('referenced_tweets') or []
        if not any(r.get('type')=='retweeted' for r in refs):
            if p['id'] not in seen:
                seen.add(p['id'])
                origins.append((p['id'], p, 'self', p))
    return origins

# --- Trend tops (no floor) ---
trend_posts = {}  # name -> [ids]
for name, fname, desk in [('Bond','trend-bond.raw.txt','entertainment')]:
    origins = collect_origins(fname)
    # rank by views
    scored = []
    for oid, op, how, carrier in origins:
        m = metrics(op)
        scored.append((m['views'] or 0, oid, op))
    scored.sort(reverse=True)
    top = []
    for views, oid, op in scored:
        if oid in top: continue
        # skip sexual
        if SEX_RE.search(text_of(op)):
            left_out.append((oid,'sexual')); continue
        top.append(oid)
        if len(top) >= 3: break
    trend_posts[name] = top
    for oid in top:
        lead = f'top post for trend "{name}" (no floor)'
        if oid not in PREV_IDS:
            make_post(oid, desk=desk, lead=lead)
        sweep_posts['trends.us'].append(oid)

# --- Desk sweeps ---
DESK_FILES = {
    'politics': 'desk-politics.raw.txt',
    'entertainment': 'desk-entertainment.raw.txt',
    'sports': 'desk-sports.raw.txt',
    'internet': 'desk-internet.raw.txt',
}
for desk, fname in DESK_FILES.items():
    fv, fl = DESK_FLOOR[desk]
    origins = collect_origins(fname)
    kept = []
    for oid, op, how, carrier in origins:
        if oid in PREV_IDS or oid in seen_post: continue
        ok, pace_lead = clears_floor(op, fv, fl)
        if not ok: continue
        # also check global-ish for desk max 5
        lead = pace_lead
        # old_content if origin much older than carrier
        if how != 'self' and op.get('created_at') and carrier.get('created_at'):
            if age_h(op['created_at'], carrier['created_at']) > 24*7:
                # will set flag after make
                pass
        post = make_post(oid, desk=desk, lead=lead)
        if post:
            if how != 'self' and op.get('created_at') and carrier.get('created_at'):
                if age_h(op['created_at'], carrier['created_at']) > 24*7:
                    post['flags'] = list(post.get('flags') or []) + ['old_content']
            kept.append(oid)
        if len(kept) >= 5: break
    sweep_posts[f'desk.{desk}'] = kept

# --- Sensors ---
SENSOR_FILES = {
    'news': 'sensor-news.raw.txt',
    'money': 'sensor-money.raw.txt',
    'science': 'sensor-science.raw.txt',
}
for group, fname in SENSOR_FILES.items():
    origins = collect_origins(fname)
    kept = []
    for oid, op, how, carrier in origins:
        if oid in PREV_IDS or oid in seen_post: continue
        ok, pace_lead = clears_floor(op, *GLOBAL_FLOOR)
        if not ok:
            # sensors can also clear a lower bar for following - still require global for viral keep
            continue
        desk = None
        if group=='news': desk='politics'
        elif group=='money': desk='markets'
        elif group=='science': desk='science'
        post = make_post(oid, desk=desk, lead=pace_lead)
        if post:
            kept.append(oid)
        if len(kept) >= 15: break
    sweep_posts[f'sensors.{group}'] = kept

# --- Viral.global from references (pointed-at) ---
# Screen most pointed-at refs by global floor
ref_candidates = sorted(ref_counts.items(), key=lambda x: -x[1])
viral_extra = []
for oid, cnt in ref_candidates:
    if cnt < 2: break
    if oid in PREV_IDS or oid in seen_post: continue
    op = tweets.get(oid)
    if not op: continue
    ok, pace_lead = clears_floor(op, *GLOBAL_FLOOR)
    if not ok: continue
    lead = pace_lead
    post = make_post(oid, desk=None, lead=lead)
    if post:
        viral_extra.append(oid)
    if len(viral_extra) >= 20: break
sweep_posts['viral.global'] = list(dict.fromkeys(sweep_posts['viral.global'] + viral_extra))[:40]

# Observations: all watch + new posts
for wid in WATCH_IDS:
    obs_out.append(make_obs(wid))
for pid in new_post_ids:
    if pid not in WATCH_SET:
        obs_out.append(make_obs(pid))

# Trends lists
us_trends_raw = load_raw('trends-us.raw.txt').get('data') or []
ww_trends_raw = load_raw('trends-ww.raw.txt').get('data') or []
# attach posts: Luka/#LakeShow/#Lakers share Luka posts; Miller gets Miller; Adou gets Adou
name_map = {
    'Bond': 'Bond', 'Pattinson': 'Bond',
}
trends_out = []
us_attached = []
for i, t in enumerate(us_trends_raw[:20], 1):
    name = t.get('trend_name') or t.get('name')
    key = name_map.get(name)
    pids = list(trend_posts.get(key) or [])[:3] if key else []
    trends_out.append({
        'region': 'US', 'rank': i, 'name': name,
        'post_count': None, 'story': None, 'post_ids': pids,
    })
    us_attached.extend(pids)
for i, t in enumerate(ww_trends_raw[:20], 1):
    name = t.get('trend_name') or t.get('name')
    trends_out.append({
        'region': 'WW', 'rank': i, 'name': name,
        'post_count': None, 'story': None, 'post_ids': [],
    })

def volume_from(name, key, desk, query):
    obj = load_raw(name)
    data = obj.get('data') or []
    points = []
    for b in data:
        st = b['start']
        if st.endswith('.000Z'): st = st.replace('.000Z','Z')
        elif st.endswith('+00:00'): st = st.replace('+00:00','Z')
        points.append({'start': st, 'count': b['tweet_count']})
    return {'key': key, 'desk': desk, 'query': query, 'granularity': 'hour', 'points': points}

VOL_Q = {
    'business': (W/'vol-business-q.txt').read_text().strip(),
    'ai': (W/'vol-ai-q.txt').read_text().strip(),
    'tech': (W/'vol-tech-q.txt').read_text().strip(),
    'science': (W/'vol-science-q.txt').read_text().strip(),
    'medicine': (W/'vol-medicine-q.txt').read_text().strip(),
}
volumes = [
    volume_from('vol-business.raw.txt', 'desk.business', 'business', VOL_Q['business']),
    volume_from('vol-ai.raw.txt', 'desk.ai', 'ai', VOL_Q['ai']),
    volume_from('vol-tech.raw.txt', 'desk.tech', 'tech', VOL_Q['tech']),
    volume_from('vol-science.raw.txt', 'desk.science', 'science', VOL_Q['science']),
    volume_from('vol-medicine.raw.txt', 'desk.medicine', 'medicine', VOL_Q['medicine']),
]

def sweep(sid, kind, method, status='ok', reason=None, post_ids=None, desk=None, window_hours=None):
    return {
        'id': sid, 'kind': kind, 'desk': desk, 'method': method,
        'window_hours': window_hours, 'status': status, 'reason': reason,
        'post_ids': post_ids or [],
    }

sweeps = []
sweeps.append(sweep('watch', 'watch',
    f"get_posts_by_ids of the re-read list from requests/plan.json (written_at 2026-11-07T07:18:46.840Z, for_run 2026-11-07T08Z), in its order and in batches of 100 ({len(WATCH_IDS)} ids, the overnight cap; its left_out counts {PLAN['left_out']['rereads']['slowed']} slowed, {PLAN['left_out']['rereads']['over_cap']} over the cap and {PLAN['left_out']['rereads']['unavailable']} unavailable); nothing added, dropped or reordered; {len(WATCH_IDS)} ids read, {len(watch_returned)} returned, {len(watch_missing)} unavailable, 4 reads; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id,referenced_tweets.id.author_id",
    post_ids=watch_returned))

trend_reason = (
    'US top-ten names with no posts attached in 0708Z and not read as names in the last three captures: '
    'Bond (1 spare read; Pattinson is the same James Bond casting event). '
    'Luka/#LakeShow/#Lakers keep their 0708Z attachments unrepeated (streamed last hour). '
    'Blazers and Rhule were read as names in 0506Z; Miller and Adou in 0708Z; Nebraska/#Huskers pair with Rhule. '
    'Sonny Dykes and Noah Fifita are new to the top ten with no posts attached, left unread after the single spare.'
)
sweeps.append(sweep('trends.us', 'trends',
    'get_trends_by_woeid 23424977 max_trends 20; Luka, #LakeShow and #Lakers are one Lakers/Doncic event; Rhule, Nebraska and #Huskers are one Nebraska football event; Bond and Pattinson are one James Bond casting event',
    reason=trend_reason, post_ids=list(dict.fromkeys(us_attached))))
sweeps.append(sweep('trends.ww', 'trends', 'get_trends_by_woeid 1 max_trends 20', post_ids=[]))

sweeps.append(sweep('viral.global', 'discovery',
    'not read, cut by the overnight plan (trend-name Bond stream used the 1 spare under the allowance of 20 and is recorded on trends.us)',
    status='skipped', reason='cut by the standing orders for the overnight band (allowance 20; plan cut viral.global)',
    window_hours=24, post_ids=[]))

sweeps.append(sweep('rising.global', 'discovery',
    'quote and repost streams: not read, cut by the standing orders (08Z plan cut rising.global)',
    status='skipped', reason='cut by the standing orders for the overnight band (allowance 20; plan cut rising.global)',
    window_hours=6, post_ids=[]))

SENSOR_Q = {
    'news': (W/'sensor-news-q.txt').read_text().strip(),
    'money': (W/'sensor-money-q.txt').read_text().strip(),
    'science': (W/'sensor-science-q.txt').read_text().strip(),
}
for g in ['news','money','science']:
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        f"search_posts_all {SENSOR_Q[g]} newest first, 25 results; reposts followed to origin; screened by global floor/pace",
        window_hours=6, post_ids=list(dict.fromkeys(sweep_posts[f'sensors.{g}']))[:15]))

for g in ['culture','sports','online']:
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        'not read this run (rotation: news/money/science this run); last read in 2026-11-07T0708Z',
        status='skipped', reason='not in this run\'s three-group rotation; last read in 2026-11-07T0708Z', post_ids=[]))

DESK_Q = {
  'politics': (W/'desk-politics-q.txt').read_text().strip(),
  'entertainment': (W/'desk-entertainment-q.txt').read_text().strip(),
  'sports': (W/'desk-sports-q.txt').read_text().strip(),
  'internet': (W/'desk-internet-q.txt').read_text().strip(),
}
DUE = ['politics','entertainment','sports','internet']
ALL_DESKS = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']
CUT_DESKS = [c.replace('desk.','') for c in PLAN['cut'] if c.startswith('desk.')]
NOT_DUE = PLAN['left_out']['desks_not_due']
for d in ALL_DESKS:
    if d in DUE:
        sweeps.append(sweep(f'desk.{d}', 'desk',
            f"search_posts_all {DESK_Q[d]} newest first, 25 results; reposted origins screened by desk floor/pace; keep at most five best per desk",
            desk=d, window_hours=24, post_ids=list(dict.fromkeys(sweep_posts[f'desk.{d}']))[:10]))
    elif d in CUT_DESKS:
        sweeps.append(sweep(f'desk.{d}', 'desk',
            f'cut by the overnight plan (not in the 08Z read list)',
            status='skipped', reason='cut by the standing orders for the overnight band', desk=d, post_ids=[]))
    else:
        sweeps.append(sweep(f'desk.{d}', 'desk',
            f'not due this hour (plan desks_not_due); last read recently',
            status='skipped', reason='not due this hour (plan: desks_not_due)', desk=d, post_ids=[]))

sweeps.append(sweep('volume.desks', 'volume',
    'get_posts_counts_recent granularity hour, query "<standing query> lang:en", start_time 2026-10-31T09:00:00Z, end_time 2026-11-07T08:00:00Z (167 full hours) for business, ai, tech, science, medicine (5 reads)',
    post_ids=[]))

sweeps.append(sweep('context.top', 'context',
    'not read, cut by the overnight plan',
    status='skipped', reason='cut by the standing orders for the overnight band (plan cut context.top)', post_ids=[]))

# Cap / sex summary
cap_drops = Counter()
sex_ids = []; ad_ids = []
for pid, why in left_out:
    if why == 'sexual': sex_ids.append(pid)
    elif why == 'ad': ad_ids.append(pid)
    elif isinstance(why,str) and why.startswith('cap:'):
        cap_drops[why[4:]] += 1

trunc_note = f"{len(trunc_diffs)} truncation-only diffs where note_tweet filled truncated text" if trunc_diffs else "no text diffs"
cited_note = "no pulse- or story-cited post missing or changed words"
if missing_cited or changed_cited:
    cited_note = f"CITED issues: missing={missing_cited} changed={changed_cited}"

reason = (
    f"Overnight-band run 2026-11-07T0809Z / 3:09 AM EST Nov 7. 08Z plan from requests/plan.json "
    f"(written_at 2026-11-07T07:18:46.840Z, for_run 2026-11-07T08Z, allowance 20, total 18) used as the read list (run.plan null; nothing written to requests/). "
    f"{READS_USED} X reads used ({READS_LEFT} left today by X's count; 747 at start). "
    f"Watch: {len(watch_returned)} of {len(WATCH_IDS)} returned, {len(watch_missing)} unavailable"
    f"{(' ('+', '.join(watch_missing)+')') if watch_missing else ''}; {cited_note} ({trunc_note}). "
    f"4 desks due (politics, entertainment, sports, internet; others not due or cut per the plan). "
    f"Volume business/ai/tech/science/medicine (window 2026-10-31T09:00Z to 2026-11-07T08:00Z, 167 buckets each; sums checked against meta.total_tweet_count). "
    f"Sensors news/money/science. Trends US+WW. Trend-name stream Bond (1 spare; Pattinson same James Bond casting event). "
    f"One by-id re-read of new kept posts (1 spare). No rising.global, viral.global, context.top, or story clusters (cut by the overnight plan). "
    f"Left out: {len(sex_ids)} sexual/doubtful ({', '.join(sex_ids[:5])}); {len(ad_ids)} ad; account cap dropped {dict(cap_drops) if cap_drops else {}}. "
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
    'context': [],
    'answers': [],
    'volume': volumes,
}

out_path = REPO / 'capture/2026/11/07/0809Z.json'
json.dump(doc, open(out_path,'w'), indent=2, ensure_ascii=False)

# TALLY: no stream origins this run (rising cut); keep last 6, drop oldest, add empty origins run
tally_path = REPO / 'capture/TALLY.json'
tally = json.load(open(tally_path))
tally['runs'] = [r for r in (tally.get('runs') or []) if r.get('run') != RUN_ID] + [{'run': RUN_ID, 'origins': []}]
tally['runs'] = tally['runs'][-6:]
json.dump(tally, open(tally_path,'w'), indent=2, ensure_ascii=False)

print('wrote', out_path, 'posts', len(posts_out), 'obs', len(obs_out))
print('watch', len(watch_returned), '/', len(WATCH_IDS), 'missing', watch_missing)
print('trunc', len(trunc_diffs), 'missing_cited', missing_cited, 'changed_cited', changed_cited)
print('left_out', Counter(w for _,w in left_out), 'sample', left_out[:12])
print('volume points', [len(v['points']) for v in volumes])
print('NEW_IDS', json.dumps(new_post_ids))
json.dump(new_post_ids, open(W/'new_ids.json','w'))
print('sweep sizes', {k:len(v) for k,v in sweep_posts.items()})
print('trends US with posts', [(t['rank'],t['name'],t['post_ids']) for t in trends_out if t['region']=='US' and t['post_ids']])
print('ok sweeps', {s['id']: (s['status'], len(s['post_ids'])) for s in sweeps if s['status']=='ok'})
