#!/usr/bin/env python3
"""Build capture/2026/10/16/0201Z.json from saved X outputs."""
import json, re, os, time
from collections import Counter, defaultdict
from datetime import datetime, timezone

W = '/tmp/grab-0201Z'
REPO = '/workspace/monitoring-the-situation'
RUN_ID = '2026-10-16T0201Z'
STARTED = '2026-10-16T02:01:00Z'
FINISHED = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
OBS_AT = '2026-10-16T02:03:00Z'
REQUESTS_REV = open(f'{W}/requests_rev.txt').read().strip()
READS_BEFORE = 943
READS_AFTER = 911
READS_USED = READS_BEFORE - READS_AFTER
FORCE_REREC = {'2110626732269289912','2110768977508978962'}

def load_raw(name):
    raw = open(f'{W}/{name}').read()
    raw = re.sub(r'</?cursor_untrusted[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data_redacted[^>]*>', '', raw)
    if 'X reads left' in raw:
        raw = raw[:raw.rfind('X reads left')]
    start = raw.find('{')
    end = raw.rfind('}')
    if start < 0:
        raise ValueError(f'no json in {name}')
    j = json.loads(raw[start:end+1])
    # unwrap write_to_file / MCP wrappers that nest data
    if isinstance(j.get('data'), dict) and isinstance(j['data'].get('data'), list):
        inner = j['data']
        return {'data': inner.get('data') or [], 'includes': inner.get('includes') or {}, 'errors': inner.get('errors') or j.get('errors') or [], 'meta': inner.get('meta') or {}}
    return j

def snowflake_ts(pid):
    return ((int(pid) >> 22) + 1288834974657) / 1000.0

def age_hours(pid, at_ts=None):
    at_ts = at_ts or datetime(2026,10,16,2,3,tzinfo=timezone.utc).timestamp()
    return (at_ts - snowflake_ts(pid)) / 3600.0

def verified_map(u):
    if not u:
        return None
    vt = u.get('verified_type')
    if vt in ('blue', 'business', 'government'):
        return vt
    if u.get('verified') is True:
        return 'blue'
    if u.get('verified') is False:
        return 'none'
    return None

NEWS_HANDLES = {
    'BBCBreaking','Reuters','SkyNews','AP','CNN','nytimes','washingtonpost',
    'FoxNews','ABC','CBSNews','NBCNews','WSJ','FT','guardian','WFLA','APNews'
}
ORG_HANDLES = {
    'NFL','NBA','MLB','NHL','UFC','SpaceX','NASA','WhiteHouse','DOJ','FBI',
    'SecKennedy','CDCgov','NASAAdmin','PopBase','PopCrave','Dexerto','Variety',
    'MacRumors','Cointelegraph','BitcoinMagazine','IGN','DiscussingFilm','SportsCenter',
    'BleacherReport','espnW','FabrizioRomano','ChampionsLeague','realmadrid'
}

def kind_guess(u, handle):
    if handle in NEWS_HANDLES:
        return 'news'
    if handle in ORG_HANDLES:
        return 'org'
    return 'unknown'

def metrics(p):
    m = p.get('public_metrics') or {}
    return {
        'views': m.get('impression_count'),
        'likes': m.get('like_count'),
        'reposts': m.get('repost_count', m.get('retweet_count')),
        'quotes': m.get('quote_count'),
        'replies': m.get('reply_count'),
        'bookmarks': m.get('bookmark_count'),
    }

def is_retweet(p):
    return any(rt.get('type') == 'retweeted' for rt in (p.get('referenced_tweets') or []))

def quote_id(p):
    for rt in p.get('referenced_tweets') or []:
        if rt.get('type') == 'quoted':
            return rt['id']
    return None

def reply_id(p):
    for rt in p.get('referenced_tweets') or []:
        if rt.get('type') == 'replied_to':
            return rt['id']
    return None

def media_source_id(p):
    att = p.get('attachments') or {}
    ids = att.get('media_source_tweet_id') or []
    return ids[0] if ids else None

def text_of(p):
    nt = p.get('note_tweet') or {}
    if isinstance(nt, dict) and nt.get('text'):
        return nt['text']
    return p.get('text') or ''

def build_media(p, media_by_key):
    att = p.get('attachments') or {}
    keys = att.get('media_keys') or []
    out = []
    for k in keys:
        md = media_by_key.get(k) or {}
        t = md.get('type')
        typ = 'photo' if t == 'photo' else ('video' if t == 'video' else ('gif' if t == 'animated_gif' else None))
        if typ is None:
            continue
        dur = md.get('duration_ms')
        out.append({
            'type': typ,
            'description': None,
            'alt': md.get('alt_text'),
            'duration_s': (round(dur/1000, 1) if isinstance(dur, (int, float)) else None),
            'link_url': None,
            'link_title': None,
        })
    ents = p.get('entities') or {}
    urls = ents.get('urls') or []
    link = None
    for u in urls:
        exp = u.get('expanded_url') or u.get('url') or ''
        if 'x.com' in exp or 'twitter.com' in exp:
            continue
        link = u
    if link:
        out.append({
            'type': 'link',
            'description': None,
            'alt': None,
            'duration_s': None,
            'link_url': (lambda u: u if isinstance(u, str) and u.startswith('https://') else None)(link.get('expanded_url') or link.get('url')),
            'link_title': (link.get('title') if isinstance(link.get('title'), str) else None) or None,
        })
    return out

files = {
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_that': 'quote_that.txt', 'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt',
    'repost_the': 'repost_the.txt',
    'sensors_culture': 'sensors_culture.txt', 'sensors_sports': 'sensors_sports.txt', 'sensors_online': 'sensors_online.txt',
    'trend_seahawks': 'trend_seahawks.txt', 'trend_teslaroadster': 'trend_teslaroadster.txt', 'trend_samdarnold': 'trend_samdarnold.txt',
    'trend_oregon': 'trend_oregon.txt', 'trend_shaheed': 'trend_shaheed.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
DUE = ['politics','world','justice','markets','ai','tech','medicine','entertainment','music','gaming','sports','internet','offbeat']
for _d in DUE: files['desk_'+_d] = f'desk_{_d}.txt'
raw = {k: load_raw(v) for k,v in files.items()}

posts_by_id = {}
users_by_id = {}
media_by_key = {}
errors_missing = {}  # id -> title
post_src = {}
import os as _os
def file_minute(tag):
    ts = _os.path.getmtime(f'{W}/' + files[tag]) if tag in files else None
    return datetime.fromtimestamp(ts, timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z') if ts else OBS_AT


def ingest(j, tag):
    for u in (j.get('includes') or {}).get('users') or []:
        users_by_id[u['id']] = u
    for m in (j.get('includes') or {}).get('media') or []:
        media_by_key[m['media_key']] = m
    def _put(t):
        prev = posts_by_id.get(t['id'])
        if prev and prev.get('note_tweet') and not t.get('note_tweet'):
            t = dict(t); t['note_tweet'] = prev['note_tweet']
        posts_by_id[t['id']] = t
        post_src[t['id']] = tag
    for key in ('tweets', 'posts'):
        for t in (j.get('includes') or {}).get(key) or []:
            _put(t)
    for t in j.get('data') or []:
        if isinstance(t, dict) and 'id' in t:
            _put(t)
    for e in j.get('errors') or []:
        rid = e.get('resource_id') or e.get('value')
        if rid:
            errors_missing[str(rid)] = e.get('title') or 'error'

for k,j in raw.items():
    if k.startswith('trends_'):
        continue
    ingest(j, k)

prior_meta = json.load(open(f'{W}/prior_posts.json'))
known = set(prior_meta.keys()) | set(open(f'{W}/known_posts.txt').read().split())
watch_ids = [x for x in open(f'{W}/reread_ids.txt').read().split() if x]
watch_set = set(watch_ids)
watch_json = set(open(f'{W}/watch_json_ids.txt').read().split())
private_ids = set(open(f'{W}/private_ids.txt').read().split())
pulse_ids = set(open(f'{W}/pulse_ids.txt').read().split())
story_ids = set(open(f'{W}/story_ids.txt').read().split())

ref_counts = Counter()
stream_origins = set()
source_of = defaultdict(set)

def collect_refs(j, source):
    for p in j.get('data') or []:
        if not isinstance(p, dict):
            continue
        for rt in p.get('referenced_tweets') or []:
            rid = rt['id']
            ref_counts[rid] += 1
            if rt['type'] in ('quoted', 'retweeted'):
                source_of[rid].add(source)
                if source.startswith('quote') or source == 'repost':
                    stream_origins.add(rid)
        ms = media_source_id(p)
        if ms:
            ref_counts[ms] += 1
            source_of[ms].add(source + '.media')
        if not is_retweet(p):
            source_of[p['id']].add(source)

for fname, src in [
    ('quote_that','quote'),('quote_just','quote'),('quote_what','quote'),('repost_the','repost'),
    ('sensors_culture','sensors.culture'),('sensors_sports','sensors.sports'),('sensors_online','sensors.online'),
    ('trend_seahawks','trend.Seahawks'),
    ('trend_teslaroadster','trend.Tesla Roadster'),
    ('trend_samdarnold','trend.Sam Darnold'),
    ('trend_oregon','trend.Oregon'),
    ('trend_shaheed','trend.Shaheed'),
] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:
    collect_refs(raw[fname], src)

tally = json.load(open(f'{REPO}/capture/TALLY.json'))
tally_runs = tally.get('runs') or []

def tally_count(pid, new_origins):
    runs = tally_runs[-5:] + [{'run': RUN_ID, 'origins': sorted(new_origins)}]
    runs = runs[-6:]
    return sum(1 for r in runs if pid in set(r.get('origins') or []))

desks = json.load(open(f'{REPO}/contract/desks.json'))
desk_floor = {d['id']: d['floor'] for d in desks['desks']}

def clears_global(p, author_kind):
    m = metrics(p)
    v = m['views'] or 0
    l = m['likes'] or 0
    age = age_hours(p['id'])
    if age < 0.25:
        return False, 'too_young'
    if author_kind == 'news':
        return (v >= 100000 or l >= 2000), 'news_totals'
    if age >= 3:
        return (v >= 100000 or l >= 2000), 'totals'
    pace = v / age if age > 0 else 0
    if pace >= 25000 and v >= 10000:
        return True, f'pace {int(pace)}/h'
    return (v >= 100000 or l >= 2000), 'totals'

def clears_desk(p, desk, author_kind):
    floor = desk_floor.get(desk) or {'views': 50000, 'likes': 1000}
    m = metrics(p)
    v = m['views'] or 0
    l = m['likes'] or 0
    age = age_hours(p['id'])
    if age < 0.25:
        return False, 'too_young'
    if author_kind == 'news':
        return (v >= floor['views'] or l >= floor['likes']), 'news_totals'
    if age >= 3:
        return (v >= floor['views'] or l >= floor['likes']), 'totals'
    pace_need = floor['views'] / 4
    tenth = floor['views'] / 10
    pace = v / age if age > 0 else 0
    if pace >= pace_need and v >= tenth:
        return True, f'pace {int(pace)}/h'
    return (v >= floor['views'] or l >= floor['likes']), 'totals'

def guess_desk(text, sources):
    t = (text or '').lower()
    for s in sources:
        if s.startswith('desk.'):
            return s.split('.')[1]
    for _x in sources:
        if str(_x) in ('trend.Seahawks','trend.Sam Darnold','trend.Shaheed'): return 'sports'
        if str(_x)=='trend.Tesla Roadster': return 'tech'
        if str(_x)=='trend.Oregon': return 'justice'
        if str(_x) in ('trend.Bend, Oregon','trend.Bend Oregon','trend.Silver Rail Elementary School'): return 'justice'
        if str(_x) in ('trend.Broncos','trend.JT Miller','trend.Thursday Night Football'): return 'sports'
        if str(_x)=='trend.#911onABC': return 'entertainment'
        if str(_x)=='trend.Roger Waters': return 'music'
        if str(_x)=='trend.Soderbergh': return 'entertainment'
        if str(_x)=='trend.Carl Thomas': return 'music'
        if str(_x)=='trend.#LightningStrikes': return 'sports'
        if str(_x)=='trend.Reeves': return 'entertainment'
        if str(_x)=='trend.chappell': return 'music'
        if str(_x)=='trend.Dustin May': return 'sports'
        if str(_x)=='trend.Athena': return 'entertainment'
        if str(_x)=='trend.Meek': return 'sports'
    _tmap = {"trend.Ruth's Chris":'life','trend.Roger Waters':'music','trend.McAfee':'sports','trend.Bend, Oregon':'justice','trend.Silver Rail Elementary School':'justice','trend.Reeves':'entertainment','trend.Soderbergh':'entertainment','trend.Carl Thomas':'music','trend.Meek':'sports','trend.#LightningStrikes':'sports','trend.Europeans':'world'}
    _trs = [x for x in sources if str(x).startswith('trend.')]
    sports_kw = ['nfl','nba','mlb','nhl','ufc','soccer','touchdown','playoffs','football','basketball','goal','roma','real madrid','mbappe','enzo','champions league','aikman','vini','endrick','mourinho','donnarumma','aew','dynamite','wrestl','yankees','kevin long','espi','soccer','fc ','dodgers','brewers','nlcs','alcs','snell','chourio','home run','baseball','uribe','gasser','joe davis','edman','pat murphy']
    polit_kw = ['trump','biden','congress','senate','white house','election','governor','democrat','republican']
    ent_kw = ['movie','film','trailer','netflix','celebrity','actor','actress','anime','episode','survivor','abbott','chicago med']
    world_kw = ['ukraine','zelensky','putin','russia','israel','gaza','war ','missile']
    defense_kw = ['starshield','pentagon','military']
    if any(k in t for k in defense_kw): return 'defense'
    internet_kw = ['meme','streamer','twitch','tiktok','influencer','podcast']
    ai_kw = ['openai','anthropic','grok','chatgpt','llm','ai model']
    tech_kw = ['starlink','apple','google','iphone']
    if any(k in t for k in world_kw): return 'world'
    if any(k in t for k in sports_kw): return 'sports'
    if any(k in t for k in polit_kw): return 'politics'
    if any(k in t for k in ai_kw): return 'ai'
    if any(k in t for k in tech_kw): return 'tech'
    if any(k in t for k in ent_kw): return 'entertainment'
    if any(k in t for k in internet_kw): return 'internet'
    for _x in _trs:
        if _tmap.get(_x): return _tmap[_x]
    for s in sources:
        if s.startswith('sensors.'):
            return {'sensors.sports':'sports','sensors.culture':'entertainment','sensors.online':'internet','sensors.news':None,'sensors.money':'markets','sensors.science':'science'}.get(s)
    return None

# NSFW / graphic skip
skip_nsfw = set(json.load(open(f'{W}/exclude_ids.json')))
skipped_nsfw = []
SEX_WORDS = ('onlyfans','would you fuck','want to fuck','be my pillow',' nsfw','porn','xxx ')

REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()
# no request source tags this run
candidates = []
for pid, p in posts_by_id.items():
    if is_retweet(p):
        continue
    if pid in REQ_ONLY:
        continue
    if p.get('possibly_sensitive') and pid not in known and pid not in watch_json:
        skipped_nsfw.append(pid)
        skip_nsfw.add(pid)
        continue
    if pid in skip_nsfw:
        skipped_nsfw.append(pid)
        continue
    tx = (text_of(p) or '').lower()
    if pid not in known and any(w in tx for w in SEX_WORDS):
        skipped_nsfw.append(pid)
        continue
    # Stolas often NSFW - skip if trend context and sexual
    if 'stolas' in tx and pid not in known:
        skipped_nsfw.append(pid)
        continue
    candidates.append(pid)

obs_ids_order = []
obs_seen = set()

def add_obs(pid, p=None, state='live'):
    if pid in obs_seen:
        return
    obs_seen.add(pid)
    if state == 'unavailable' or p is None:
        obs_ids_order.append({
            'id': pid, 'at': OBS_AT, 'state': 'unavailable',
            'views': None, 'likes': None, 'reposts': None, 'quotes': None,
            'replies': None, 'bookmarks': None, 'approx': False
        })
        return
    m = metrics(p)
    obs_ids_order.append({
        'id': pid, 'at': file_minute(post_src.get(pid)), 'state': 'live',
        'views': m['views'], 'likes': m['likes'], 'reposts': m['reposts'],
        'quotes': m['quotes'], 'replies': m['replies'], 'bookmarks': m['bookmarks'],
        'approx': False
    })

watch_returned = set()
watch_unavailable = []
for batch in ('watch0','watch1','watch2'):  # noqa keep
    j = raw[batch]
    for p in j.get('data') or []:
        watch_returned.add(p['id'])
        add_obs(p['id'], p)
    for e in j.get('errors') or []:
        rid = str(e.get('resource_id') or e.get('value') or '')
        if rid and rid in watch_set:
            add_obs(rid, None, 'unavailable')
            watch_unavailable.append(rid)

# Evaluate candidates
score_rows = []
for pid in candidates:
    p = posts_by_id.get(pid)
    if not p:
        continue
    u = users_by_id.get(p.get('author_id')) or {}
    handle = u.get('username') or 'unknown'
    if handle == 'unknown' or not re.match(r'^[A-Za-z0-9_]{1,15}$', handle):
        continue
    ak = kind_guess(u, handle)
    srcs = source_of.get(pid) or set()
    desk = guess_desk(text_of(p), srcs)
    from_desk = any(s.startswith('desk.') for s in srcs)
    from_trend = any(s.startswith('trend.') for s in srcs)
    if from_trend:
        ok, reason = True, 'trend_context'
    elif from_desk:
        ok, reason = clears_desk(p, desk if desk in desk_floor else 'internet', ak)
    else:
        ok, reason = clears_global(p, ak)
    if not ok and ref_counts.get(pid,0) >= 2:
        ok2, r2 = clears_global(p, ak)
        if ok2:
            ok, reason = ok2, r2
    m = metrics(p)
    v = m['views'] or 0
    if ok:
        score_rows.append((v, pid, desk, reason, ak, handle, srcs))

score_rows.sort(reverse=True)

MAX_NEW = 40
selected = []
selected_ids = set()
author_new_count = Counter()
author_dropped = Counter()
desk_taken = Counter()

def take(row, count_author=True):
    v, pid, desk, reason, ak, handle, srcs = row
    if pid in selected_ids:
        return False
    is_new = pid not in known
    _only_desk = srcs and all(str(x).startswith('desk.') for x in srcs) and ref_counts.get(pid,0) < 2
    if is_new and _only_desk:
        _dk = sorted(srcs)[0]
        if desk_taken[_dk] >= 5:
            return False
    # author cap: at most 3 NEW posts per account (requests/context exempt - none here)
    if is_new and count_author and author_new_count[handle] >= 3:
        author_dropped[handle] += 1
        return False
    selected.append(row)
    selected_ids.add(pid)
    if is_new and count_author:
        author_new_count[handle] += 1
    if is_new and _only_desk:
        desk_taken[_dk] += 1
    return True

# 1) trend context
_trend_taken = Counter()
for row in score_rows:
    _tn = [str(x) for x in row[6] if str(x).startswith('trend.')]
    if _tn and any(_trend_taken[t] < 3 for t in _tn):
        if take(row, count_author=False):
            for t in _tn: _trend_taken[t] += 1  # trend context posts don't fill the capture the same way but still count? contract: requests/context don't count. Trend context is context-like. Don't count toward cap.

# 2) new posts
for row in score_rows:
    if row[1] not in known:
        take(row)
    if sum(1 for r in selected if r[1] not in known) >= 28:
        break

# 3) ensure source coverage
for src in ['desk.'+_d for _d in DUE] + ['sensors.culture', 'sensors.sports', 'sensors.online', 'quote', 'repost']:
    for row in score_rows:
        if src in row[6] or any(str(s).startswith(src) for s in row[6]):
            take(row)
            break

# 4) fill
for row in score_rows:
    take(row)
    if len(selected) >= MAX_NEW + 15:  # room for trend context
        break

# 5) request picks (none this run)
for _r,_ids in REQ_PICKS.items():
    for _i in _ids:
        _p = posts_by_id[_i]
        _u = users_by_id.get(_p.get('author_id')) or {}
        _h = _u.get('username')
        take(((metrics(_p)['views'] or 0), _i, None, 'request', kind_guess(_u,_h), _h, source_of[_i]), count_author=False)

# Re-recorded: watch posts whose text now differs from prior stored text
rerecorded = []
for pid in watch_returned:
    if pid not in prior_meta:
        continue
    p = posts_by_id.get(pid)
    if not p:
        continue
    new_text = text_of(p)
    old_text = prior_meta[pid].get('text') or ''
    if new_text and old_text and new_text != old_text and (len(new_text) > len(old_text) or pid in FORCE_REREC):
        # full note_tweet now available
        rerecorded.append(pid)
        if pid not in selected_ids:
            u = users_by_id.get(p.get('author_id')) or {}
            handle = u.get('username') or prior_meta[pid].get('handle') or 'unknown'
            ak = kind_guess(u, handle)
            desk = guess_desk(new_text, source_of.get(pid) or set())
            selected.append(((metrics(p)['views'] or 0), pid, desk, 're-recorded', ak, handle, source_of.get(pid) or set()))
            selected_ids.add(pid)

EXTRA_PRIVATE = {'2086317046493520240','2110808191126892978','2110626732269289912','2110009515290599884','2110324218655076676','2110736011320025241','2110740447568056363'}
import glob as _glob
PRIOR_DESK = {}
for _c in sorted(_glob.glob(f'{REPO}/capture/2026/10/*/*.json')):
    if _c.endswith('1709Z.json') and '/15/' in _c: continue
    for _p in json.load(open(_c))['posts']:
        PRIOR_DESK[_p['id']] = _p.get('desk')
DESK_OVERRIDE = {
    '1996248066714907092':'sports','2110376019068874993':'business','2110506786747011202':'ai',
    '2110371582153748942':'tech','2110676305100615719':'gaming','2110418544223826227':'ideas',
    '2107480459659591692':'ideas','2110761197783945668':'ideas','2110009188365591038':'tech',
    '2110774405286736026':'justice','2068425887612359110':'music','2072214077372518657':'tech',
    '1686109285342670849':'offbeat','2089570265713737987':'offbeat','2086317046493520240':'life',
    '2110267525141328095':'sports','2110547758658531568':'offbeat','2107778804894834987':'internet','2110429006331875770':'internet',
    '2109607852134510958':'music','2107074581148340589':'sports','2110567340069003542':'ai',
    '2110585384379752814':'music','1826102870896422965':'politics','2110440211096179145':'entertainment',
    '2110578527573614725':'music','2090977161708507603':'gaming','2110695927312777466':'ai',
    '2110424792314851704':'sports','2109870933217583476':'entertainment','2110311433430827008':'politics',
    '2110709911764279502':'markets',
    '2110724957797826831':'markets','2110717537964953810':'gaming','2110726705094795592':'gaming',
    '2110717891058565269':'gaming','2110257167517519990':'music','2110712657858953702':None,
    '2110712557719920909':'markets','2110021865020547132':'markets','2110542006124748814':'ai',
    '2110717329575190935':'entertainment','2110222071229989249':'science',
    '2110794015348011464':'justice','2110521416236011727':'internet','2110637036944388511':'internet','2109898152442806328':None,
    '2055678699962355825':'internet','2101401254643544392':'entertainment','2110402156104700129':None,
}


def make_post(pid, desk, reason, ak, srcs):
    p = posts_by_id[pid]
    u = users_by_id.get(p.get('author_id')) or {}
    handle = u.get('username')
    name = u.get('name') or handle
    followers = (u.get('public_metrics') or {}).get('followers_count')
    text = text_of(p)
    created = p.get('created_at')
    if created and created.endswith('+00:00'):
        created = created.replace('+00:00','Z')
    if created and '.' in created and created.endswith('Z'):
        # keep as-is or trim ms? prior keeps with Z; X returns with .000Z sometimes
        pass
    flags = []
    age_d = age_hours(pid) / 24.0
    _refby = [q for q in posts_by_id.values() if pid in [r['id'] for r in (q.get('referenced_tweets') or [])] + list((q.get('attachments') or {}).get('media_source_tweet_id') or [])]
    _old_ref = any((snowflake_ts(q['id']) - snowflake_ts(pid)) > 7*86400 for q in _refby)
    if (age_d > 7 and (ref_counts.get(pid,0) >= 1 or _old_ref)) or 'old_content' in (prior_meta.get(pid,{}).get('flags') or []):
        flags.append('old_content')
    if pid in private_ids or pid in EXTRA_PRIVATE:
        flags.append('private_individual')
    lead_parts = []
    if pid in rerecorded:
        lead_parts.append('re-recorded')
    tc = tally_count(pid, stream_origins)
    if pid in stream_origins and tc >= 1:
        lead_parts.append(f'seen in the quote or repost stream in {tc} of the last 6 runs')
    rc = ref_counts.get(pid, 0)
    if rc >= 2:
        lead_parts.append(f'pointed at by {rc} posts read this run')
    if reason and isinstance(reason, str) and reason.startswith('pace'):
        lead_parts.append(reason)
    for pat in (r'via\s+@([A-Za-z0-9_]+)', r'📽️\s*@([A-Za-z0-9_]+)'):
        m = re.search(pat, text, re.I)
        if m:
            lead_parts.append(f'credits @{m.group(1)}')
            break
    lead = '; '.join(lead_parts) if lead_parts else None
    media = build_media(p, media_by_key)
    # normalize created_at to match checker (ISO with Z)
    if created and not created.endswith('Z') and '+' not in created:
        created = created + 'Z'
    rec = {
        'id': pid,
        'url': f'https://x.com/{handle}/status/{pid}',
        'created_at': created,
        'lang': p.get('lang'),
        'text': text,
        'author': {
            'handle': handle,
            'name': name,
            'followers': followers,
            'verified': verified_map(u),
            'kind': ak,
        },
        'media': media,
        'reply_to': reply_id(p),
        'quotes': quote_id(p),
        'note': None,
        'flags': flags,
        'desk': desk if desk in desk_floor else (desk if desk else None),
        'beat': None,
        'topic': None,
        'lead': lead,
    }
    if desk not in desk_floor and desk is not None:
        rec['desk'] = None if desk == 'null' else (desk if desk in desk_floor else 'internet')
    if pid in DESK_OVERRIDE:
        rec['desk'] = DESK_OVERRIDE[pid]
    elif pid in PRIOR_DESK and rec['desk'] is None and PRIOR_DESK[pid] in desk_floor:
        rec['desk'] = PRIOR_DESK[pid]
    ms = media_source_id(p)
    if ms:
        rec['media_source'] = ms
    return rec

posts_out = []
viral_ids = []
rising_ids = []
sensor_posts = defaultdict(list)
desk_posts = defaultdict(list)
trend_posts = defaultdict(list)

for row in selected:
    v, pid, desk, reason, ak, handle, srcs = row
    if pid in skip_nsfw:
        continue
    rec = make_post(pid, desk, reason, ak, srcs)
    # validate desk
    if rec['desk'] not in desk_floor and rec['desk'] is not None:
        rec['desk'] = 'internet'
    posts_out.append(rec)
    add_obs(pid, posts_by_id[pid])
    if reason == 'request':
        continue
    viral_ids.append(pid)
    age = age_hours(pid)
    if age is not None and age < 6:
        rising_ids.append(pid)
    for s in srcs:
        if s.startswith('sensors.'):
            sensor_posts[s].append(pid)
        if s.startswith('desk.'):
            desk_posts[s.split('.',1)[1]].append(pid)
        if s.startswith('trend.'):
            trend_posts[s.split('.',1)[1]].append(pid)

def views_of(pid):
    p = posts_by_id.get(pid) or {}
    return (metrics(p)['views'] or 0)

viral_ids = sorted(set(viral_ids), key=views_of, reverse=True)
rising_ids = sorted(set(rising_ids), key=views_of, reverse=True)[:30]
# Cap viral at 40 but keep trend context extras like prior runs
viral_core = viral_ids[:40]
posts_by_sel = {p['id']: p for p in posts_out}
# Prefer viral_core order for posts, then remaining selected
ordered_ids = list(viral_core)
for pid in viral_ids:
    if pid not in ordered_ids:
        ordered_ids.append(pid)
for _r,_ids in REQ_PICKS.items():
    for _i in _ids:
        if _i not in ordered_ids: ordered_ids.append(_i)
posts_out = [posts_by_sel[i] for i in ordered_ids if i in posts_by_sel]

# Attach trend post_ids: top 3 by views matching name (word boundary)
def match_trend(name, text):
    if not text:
        return False
    # word boundary for short names
    return re.search(r'(?i)(?<![A-Za-z0-9_])' + re.escape(name) + r'(?![A-Za-z0-9_])', text) is not None

def best_for_trend(name, limit=3):
    # prefer streamed trend origins
    keyed = trend_posts.get(name) or []
    scored = []
    for pid in set(list(keyed) + viral_ids):
        p = posts_by_id.get(pid)
        if not p:
            continue
        if match_trend(name, text_of(p)) or pid in keyed:
            scored.append((views_of(pid), pid))
    scored.sort(reverse=True)
    return [pid for _,pid in scored[:limit] if pid in posts_by_sel or True]

# Only attach ids that are in this capture's posts
def parse_trends(j, region):
    out = []
    for i, t in enumerate(j.get('data') or [], 1):
        name = t.get('trend_name') or t.get('name')
        pids = []
        if region == 'US':
            candidates_t = best_for_trend(name, 5)
            # for event clusters, also try related
            for pid in candidates_t:
                if pid in posts_by_sel:
                    pids.append(pid)
                if len(pids) >= 3:
                    break
            # also from trend stream source
            for pid in (trend_posts.get(name) or []):
                if pid in posts_by_sel and pid not in pids:
                    pids.append(pid)
                if len(pids) >= 3:
                    break
        out.append({
            'region': region,
            'rank': i,
            'name': name,
            'post_count': None,
            'story': None,
            'post_ids': pids[:3],
        })
    return out

trends = parse_trends(raw['trends_us'], 'US') + parse_trends(raw['trends_ww'], 'WW')

def sweep(id_, kind, desk, method, window, status, reason, post_ids):
    return {
        'id': id_, 'kind': kind, 'desk': desk, 'method': method,
        'window_hours': window, 'status': status, 'reason': reason,
        'post_ids': post_ids or []
    }

watch_ordered = []
seenw=set()
for batch in ('watch0','watch1','watch2'):
    for p in raw[batch].get('data') or []:
        if isinstance(p,dict) and p.get('id') and p['id'] not in seenw:
            seenw.add(p['id']); watch_ordered.append(p['id'])
for rid in watch_unavailable:
    if rid not in seenw:
        seenw.add(rid); watch_ordered.append(rid)

DESK_Q = {}
due_desks = list(DUE)
import re as _re
_cap = open(f'{REPO}/capture/CAPABILITIES.md').read()
for _d in [d['id'] for d in desks['desks']]:
    _m = _re.search(r'^\| ' + _d + r' \| `([^`]+)` \|', _cap, _re.M)
    DESK_Q[_d] = (_m.group(1) if _m else _d) + ' lang:en is:retweet -is:reply'
SWEPT_DESKS = set(DUE)
sweeps = []
sweeps.append(sweep('watch','watch',None,
    f'get_posts_by_ids of requests/watch.json ({len(watch_json)} ids), every post first captured in the last 6 hours and under 24 hours old, posts first captured 6 to 24 hours ago that gained at least 2 percent between their last two readings; 02Z is not a fourth hour; under the 400 cap: {len(watch_ids)} unique ids, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id,referenced_tweets.id.author_id',
    None,'ok',None, watch_ordered))
sweeps.append(sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max 20',None,'ok',None,[]))
sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))
sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; sensors culture/sports/online; trend names "Seahawks lang:en is:retweet", "\"Tesla Roadster\" lang:en is:retweet", "\"Sam Darnold\" lang:en is:retweet", "Oregon lang:en is:retweet" and "Shaheed lang:en is:retweet" (newest first, 25 each; Seahawks, Broncos, Sam Darnold, Shaheed and Bo Nix one event, Seahawks at Broncos on Thursday Night Football; Oregon mostly the Bend, Oregon school shooting, with a Portland stabbing); quote/repost words that/just/what + the; desks politics/world/justice/markets/ai/tech/medicine/entertainment/music/gaming/sports/internet/offbeat; two screening reads by id of unread referenced posts; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '3 quote pages + 1 repost page, common words "that", "just", "what" and "the": "that lang:en is:quote -is:retweet", "just lang:en is:quote -is:retweet", "what lang:en is:quote -is:retweet", "the lang:en is:retweet", newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
SQ = {g: open(f'{W}/sensor_query_{g}.txt').read().strip() for g in ['culture','sports','online']}
for g in ['culture','sports','online']:
    pids = [x for x in (sensor_posts.get(f'sensors.{g}') or []) if x in posts_by_sel][:15]
    sweeps.append(sweep(f'sensors.{g}','discovery',None,
        f'search_posts_all {SQ[g]} newest first, 25 results; reposts followed to origin',
        6,'ok',None, pids))
for g in ['news','money','science']:
    sweeps.append(sweep(f'sensors.{g}','discovery',None,'sensor rotation: news/money/science were read in 2026-10-16T0101Z; this run reads culture/sports/online',6,'skipped','sensor rotation; read in 2026-10-16T0101Z, due next run',[]))
all_desks = [d['id'] for d in desks['desks']]
for d in all_desks:
    pids = [x for x in (desk_posts.get(d) or []) if x in posts_by_sel]
    for p in posts_out:
        if p['desk']==d and p['id'] not in pids and f'desk.{d}' in (source_of.get(p['id']) or set()):
            pids.append(p['id'])
    if d in SWEPT_DESKS:
        sweeps.append(sweep(f'desk.{d}','desk',d,
            f'search_posts_all {DESK_Q[d]} newest first, 25 results; reposted origins screened by desk floor/pace; keep at most five best',
            24,'ok',None, pids[:5]))
    else:
        if d in ('defense','disaster','business','ideas'):
            reason = 'not due: four-hour desk, last ok sweep started 2026-10-15T23:08:00Z, 2 h 53 min before this run'
        else:
            reason = 'not due: four-hour desk, last ok sweep started 2026-10-16T00:01:00Z, 2 h before this run'
        sweeps.append(sweep(f'desk.{d}','desk',d, DESK_Q.get(d) or d, 24,'skipped', reason, []))
sweeps.append(sweep('context.top','context',None,'cut for the read budget',None,'skipped','cut for the read budget',[]))
open_reqs = json.load(open(f'{REPO}/requests/open.json'))['requests']
REQ_Q = {
    'r-2026-10-10-01': 'search_posts_all ("intelligence sharing" OR "new president") Ukraine (refinery OR refineries OR Trump OR Zelensky) lang:en -is:retweet -is:reply, start_time 2026-10-09T00:00:00Z, relevancy, 25 results',
    'r-2026-10-09-12': 'search_posts_all "Marble Hill" (ICE OR DHS OR NYPD OR shooting OR shot) -is:retweet -is:reply, start_time 2026-10-08T00:00:00Z, relevancy, 25 results',
    'r-2026-10-09-13': 'search_posts_all (PERM OR "labor certification") (Microsoft OR Adobe OR Infosys OR Tata OR Wipro OR HCL OR Cognizant OR Capgemini OR "Labor Department" OR "Department of Labor") -is:retweet -is:reply, start_time 2026-10-08T00:00:00Z, relevancy, 25 results',
}
ANSWERED_EARLIER = {'r-2026-10-15-01':'2026-10-15T2059Z','r-2026-10-10-01':'2026-10-15T2200Z','r-2026-10-09-12':'2026-10-15T2200Z','r-2026-10-09-13':'2026-10-15T2200Z','r-2026-10-09-05':'2026-10-09T0629Z','r-2026-10-09-08':'2026-10-09T0629Z','r-2026-10-09-09':'2026-10-09T0629Z','r-2026-10-09-10':'2026-10-09T0629Z'}
for r in open_reqs:
    if r['id'] in REQ_PICKS:
        sweeps.append(sweep(f"request.{r['id']}",'request',None,REQ_Q.get(r['id']) or 'request',None,'ok',None,[i for i in REQ_PICKS[r['id']] if i in posts_by_sel]))
    elif r['id'] in ANSWERED_EARLIER:
        sweeps.append(sweep(f"request.{r['id']}",'request',None,'not read: answered in capture '+ANSWERED_EARLIER[r['id']]+'; watched ids re-read in watch',None,'skipped','answered in capture '+ANSWERED_EARLIER[r['id']]+'; a request is answered once',[]))
    else:
        sweeps.append(sweep(f"request.{r['id']}",'request',None,'deferred this run; watched ids re-read in watch',None,'skipped','deferred this run for the read budget',[]))

# Pulse/story text mismatch check
mismatches = []
missing_pulse = []
for pid in (pulse_ids | story_ids) & watch_set:
    if pid in errors_missing or pid in watch_unavailable:
        missing_pulse.append(pid)
        continue
    p = posts_by_id.get(pid)
    if not p:
        missing_pulse.append(pid)
        continue
    if pid in prior_meta:
        old = prior_meta[pid].get('text') or ''
        new = text_of(p)
        if old and new and old != new:
            # only flag if different words and not a re-record lengthening
            if not (pid in rerecorded and new.startswith(old[:200])):
                mismatches.append(pid)

prior_known = set(known)
here_ids = {p['id'] for p in posts_out}
def ok_ref(rid):
    return rid is None or rid in here_ids or rid in prior_known or rid in watch_returned
for p in posts_out:
    if not ok_ref(p.get('reply_to')):
        p['reply_to'] = None
    if not ok_ref(p.get('quotes')):
        p['quotes'] = None
    if 'media_source' in p and not ok_ref(p.get('media_source')):
        del p['media_source']

for p in posts_out:
    if p['id'] not in obs_seen:
        add_obs(p['id'], posts_by_id[p['id']])

# Observations: watch + selected posts (and any unavailable)
obs_ids_order = [o for o in obs_ids_order if o['id'] in here_ids or o['id'] in prior_known or o['id'] in watch_set or o['id'] in watch_returned]

author_drop_note = ', '.join(f'{h} x{c}' for h,c in author_dropped.most_common() if c) or 'none'

capture = {
    'schema': 'mts.capture/1',
    'run': {
        'id': RUN_ID,
        'started_at': STARTED,
        'finished_at': FINISHED,
        'status': 'partial',
        'reason': (
            f'Evening run at 10:01 PM ET (02:01 UTC Oct 16; 12:00-05:00 UTC budget, up to 42): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 02Z is not a fourth hour); trends US+WW; '
            f'trend names Seahawks, Tesla Roadster, Sam Darnold, Oregon, Shaheed (5 reads; Seahawks, Broncos, Sam Darnold, Shaheed and Bo Nix are one event, Seahawks at Broncos on Thursday Night Football; Oregon is mostly the Bend, Oregon school shooting; chappell, #911onABC and Dustin May had posts attached in 0101Z); sensors culture/sports/online; quote/repost words that, just, what + the (3+1); '
            f'all 13 due desks swept: hourly politics, entertainment, sports, internet and 2-hour world, justice, markets, ai, tech, medicine, offbeat (last ok 0001Z), music, gaming (last ok 2308Z); 4-hour desks last ok 2308Z/0001Z, not due; '
            f'two screening reads by id of {len(open(f"{W}/screen_ids.txt").read().split())} unread second-hop, reply-parent and media-source posts. '
            f'Open requests all answered in earlier captures; none read. '
            f'Not read for the budget: story clusters, volume, context.top, media descriptions; x_stories omitted. '
            f'Skipped sexual or graphic ids are in exclude_ids.json in the work folder.' 
        ),
        'grabber': {
            'agent': 'grokbot',
            'model': None,
            'method': 'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid)'
        },
        'requests_rev': REQUESTS_REV,
    },
    'sweeps': sweeps,
    'trends': trends,
    'posts': posts_out,
    'observations': obs_ids_order,
    'context': [],
    'answers': [],
}

out_path = f'{REPO}/capture/2026/10/16/0201Z.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
json.dump(capture, open(out_path,'w'), indent=2, ensure_ascii=False)
open(out_path,'a').write('\n')
print('wrote', out_path)
print('posts', len(posts_out), 'obs', len(obs_ids_order))
print('skipped_nsfw', len(set(skipped_nsfw)), list(set(skipped_nsfw))[:8])
print('viral', len(viral_core), 'rising', len(rising_ids))
print('author_dropped', dict(author_dropped))
print('rerecorded', rerecorded)
print('watch_unavailable', watch_unavailable)
print('pulse_missing', missing_pulse)
print('pulse_mismatches', mismatches)
print('stream_origins', len(stream_origins))

json.dump(sorted(set(skipped_nsfw)|set(json.load(open(f'{W}/exclude_ids.json')))), open(f'{W}/exclude_ids.json','w'))
meta = {
  'author_dropped': dict(author_dropped),
  'rerecorded': rerecorded,
  'watch_unavailable': watch_unavailable,
  'pulse_missing': missing_pulse,
  'pulse_mismatches': mismatches,
  'reads': [READS_BEFORE, READS_AFTER],
}
json.dump(meta, open(f'{W}/build_meta.json','w'), indent=2)

# Update TALLY
new_runs = (tally_runs + [{'run': RUN_ID, 'origins': sorted(stream_origins)}])[-6:]
tally['runs'] = new_runs
json.dump(tally, open(f'{REPO}/capture/TALLY.json','w'), indent=2, ensure_ascii=False)
open(f'{REPO}/capture/TALLY.json','a').write('\n')
print('tally updated', [r['run'] for r in new_runs])
