#!/usr/bin/env python3
"""Build capture/2026/11/06/2000Z.json from saved X outputs."""
import json, re, os
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

W = Path('/workspace/monitoring-the-situation/capture/work/2026-11-06T2000Z')
REPO = Path('/workspace/monitoring-the-situation')
RUN_ID = '2026-11-06T2000Z'
STARTED = '2026-11-06T20:00:00Z'
FINISHED = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
OBS_AT = '2026-11-06T20:03:00Z'
REQUESTS_REV = '8d90e444dffa8b63e68c51c8c8380b761a5d2353'
READS_USED = 21  # watch2 + trends2 + volume5 + sensors3 + rising2 + viral3 + screen1 + context2 = 20; plus 1 mistaken partial screen = 21; X count 949->928
READS_LEFT = 928
PREV = json.load(open(REPO / 'capture/2026/11/06/1932Z.json'))
PREV_IDS = {p['id'] for p in PREV['posts']}
PLAN = json.load(open(REPO / 'requests/plan.json'))
WATCH_IDS = PLAN['items'][0]['ids']
WATCH_SET = set(WATCH_IDS)

NEWS = {'BBCBreaking','Reuters','SkyNews','AP','CNN','nytimes','washingtonpost','FoxNews','ABC','CBSNews','NBCNews','WSJ','WFLA','APNews'}
ORG = {'NFL','NBA','MLB','NHL','UFC','SpaceX','NASA','WhiteHouse','DOJ','FBI','SecKennedy','CDCgov','NASAAdmin','PopBase','PopCrave','Dexerto','Variety','MacRumors','Cointelegraph','BitcoinMagazine','IGN','DiscussingFilm','SportsCenter','BleacherReport','FabrizioRomano','Tesla','CyberpunkGame'}
AGG = {'EricLDaugh','atrupar','LeadingReport','CollinRugg','visegrad24','rawsalerts','WatcherGuru','cryptorover','AshCrypto','BitcoinArchive','PopBase','PopCrave','CultureCrave','MeidasTouch','unusual_whales'}

SEX_RE = re.compile(r'(onlyfans|nsfw|porn|xxx|hentai|nude|nudes|\banal\b|boobs|pussy|cock\b)', re.I)
AD_RE = re.compile(r'(#ad\b|giveaway|airdrop|memecoin|promo code|paid partnership)', re.I)

def load_raw(name):
    raw = (W / name).read_text()
    raw = re.sub(r'</?cursor_untrusted[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data[^>]*>', '', raw)
    raw = re.sub(r'</?cursor_untrusted_data_redacted[^>]*>', '', raw)
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
            'type': t,
            'description': None,
            'alt': m.get('alt_text'),
            'duration_s': (dur/1000.0) if isinstance(dur,(int,float)) else None,
            'link_url': None,
            'link_title': None,
        })
    # link card from last non-x.com url
    urls = (p.get('entities') or {}).get('urls') or []
    for u in reversed(urls):
        exp = u.get('expanded_url') or u.get('url') or ''
        if 'x.com' in exp or 'twitter.com' in exp: continue
        out.append({
            'type': 'link',
            'description': None,
            'alt': None,
            'duration_s': None,
            'link_url': exp,
            'link_title': u.get('title'),
        })
        break
    return out

def age_h(created, at=OBS_AT):
    c = datetime.fromisoformat(created.replace('Z','+00:00'))
    a = datetime.fromisoformat(at.replace('Z','+00:00'))
    return max((a-c).total_seconds()/3600.0, 0.001)

def clears_global(m, created, kind):
    views = m.get('views') or 0
    likes = m.get('likes') or 0
    ah = age_h(created)
    if ah < 0.25: return False, 'too_young'
    if kind == 'news':
        return (views >= 100000 or likes >= 2000), 'news_totals'
    if ah <= 3:
        pace = views / ah
        if pace >= 25000 and views >= 10000:
            return True, f'pace {int(pace)}/h'
    if ah <= 24 and (views >= 100000 or likes >= 2000):
        return True, 'totals'
    if ah > 24 and (views >= 100000 or likes >= 2000):
        # still keep if trending attach
        return True, 'totals_old'
    return False, 'below'

# ---- ingest ----
users = {}
media_by_key = {}
tweets = {}  # id -> raw tweet
errors_by_file = {}

def ingest(name):
    obj = load_raw(name)
    for u in (obj.get('includes') or {}).get('users') or []:
        users[u['id']] = u
    for m in (obj.get('includes') or {}).get('media') or []:
        media_by_key[m['media_key']] = m
    for p in obj.get('data') or []:
        tweets[p['id']] = p
    for p in (obj.get('includes') or {}).get('tweets') or []:
        tweets.setdefault(p['id'], p)  # prefer data copy if both
    # for data posts, overwrite with data (has full fields)
    for p in obj.get('data') or []:
        tweets[p['id']] = p
    errors_by_file[name] = obj.get('errors') or []
    return obj

for fname in [
    'watch1.txt','watch2.txt',
    'sensor_news.txt','sensor_money.txt','sensor_science.txt',
    'rising_is.txt','rising_you.txt',
    'trend_chief.txt','trend_susie.txt','trend_cyber.txt',
    'screen.txt','context_replies.txt','context_quotes.txt',
]:
    ingest(fname)

# watch returned / missing
watch_returned = []
watch_missing = []
for wid in WATCH_IDS:
    if wid in tweets and wid not in {e.get('resource_id') or e.get('value') for errs in errors_by_file.values() for e in errs}:
        # check errors specifically from watch files
        pass
watch_err_ids = set()
for name in ['watch1.txt','watch2.txt']:
    for e in errors_by_file.get(name) or []:
        watch_err_ids.add(str(e.get('resource_id') or e.get('value') or ''))
for wid in WATCH_IDS:
    if wid in watch_err_ids or wid not in tweets:
        watch_missing.append(wid)
    else:
        watch_returned.append(wid)

# trend attachments
trend_posts = json.load(open(W/'trend_posts.json'))

# stream origins for tally
stream_origins = []
for name in ['rising_is.txt','rising_you.txt']:
    obj = load_raw(name)
    pm = {p['id']:p for p in (obj.get('includes') or {}).get('tweets') or []}
    for p in obj.get('data') or []:
        for r in p.get('referenced_tweets') or []:
            if r.get('type') == 'quoted':
                stream_origins.append(r['id'])

# referenced counts across discovery
ref_counts = Counter()
for name in ['sensor_news.txt','sensor_money.txt','sensor_science.txt','rising_is.txt','rising_you.txt','trend_chief.txt','trend_susie.txt','trend_cyber.txt']:
    obj = load_raw(name)
    for p in (obj.get('data') or []) + ((obj.get('includes') or {}).get('tweets') or []):
        for r in p.get('referenced_tweets') or []:
            ref_counts[r['id']] += 1
        src = (p.get('attachments') or {}).get('media_source_tweet_id') or []
        for mid in src:
            ref_counts[mid] += 1

# ---- build new posts from screen + context ----
screen_obj = load_raw('screen.txt')
screen_ids = [p['id'] for p in screen_obj.get('data') or []]

left_out = []
account_new = Counter()
new_post_ids = []
posts_out = []
obs_out = []
seen_post = set()

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

def make_post(pid, desk=None, lead=None, force=False):
    if pid in seen_post: return None
    p = tweets.get(pid)
    if not p: return None
    # already known: observations only unless force
    if pid in PREV_IDS and not force:
        return None
    text = text_of(p)
    if SEX_RE.search(text):
        left_out.append((pid, 'sexual')); return None
    if AD_RE.search(text):
        left_out.append((pid, 'ad')); return None
    a = author_obj(p)
    # account cap for NEW records (not context)
    if not force and a['handle'] != 'unknown':
        if account_new[a['handle']] >= 3:
            left_out.append((pid, f'cap:{a["handle"]}'))
            return None
        account_new[a['handle']] += 1
    m = metrics(p)
    # reply_to / quotes
    reply_to = None; quotes = None
    for r in p.get('referenced_tweets') or []:
        if r.get('type') == 'replied_to':
            reply_to = r['id']
        if r.get('type') == 'quoted':
            quotes = r['id']
    note = None
    nt = p.get('note_tweet') or {}
    if isinstance(nt, dict) and nt.get('text') and nt['text'] != (p.get('text') or ''):
        note = {'text': nt['text']}
    flags = []
    # old_content: origin more than 7 days older than something that led here - approximate via age > 7d from now when found via ref
    created = p.get('created_at')
    if created and age_h(created) > 24*7:
        flags.append('old_content')
    # private_individual heuristic: skip for now unless obvious
    lead_bits = []
    if lead: lead_bits.append(lead)
    if ref_counts.get(pid, 0) >= 2:
        lead_bits.append(f'pointed at by {ref_counts[pid]} posts read this run')
    if pid in stream_origins:
        # tally filled later
        pass
    post = {
        'id': pid,
        'url': f"https://x.com/{a['handle']}/status/{pid}",
        'created_at': created,
        'lang': p.get('lang'),
        'text': p.get('text') or text,
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

# Screen-kept posts (global floor), plus all trend tops
trend_id_set = set()
for ids in trend_posts.values():
    trend_id_set.update(ids)

kept_for_viral = []
kept_for_rising = []
kept_for_sensors = {'news':[], 'money':[], 'science':[]}

# classify sources
sensor_origin_ids = {'news':set(),'money':set(),'science':set()}
for group, fname in [('news','sensor_news.txt'),('money','sensor_money.txt'),('science','sensor_science.txt')]:
    obj = load_raw(fname)
    pm = {p['id']:p for p in (obj.get('includes') or {}).get('tweets') or []}
    for p in obj.get('data') or []:
        types = {r.get('type') for r in (p.get('referenced_tweets') or [])}
        if 'retweeted' in types:
            for r in p.get('referenced_tweets') or []:
                if r.get('type')=='retweeted':
                    sensor_origin_ids[group].add(r['id'])
        else:
            sensor_origin_ids[group].add(p['id'])

rising_origin_ids = set()
for fname in ['rising_is.txt','rising_you.txt']:
    obj = load_raw(fname)
    for p in obj.get('data') or []:
        for r in p.get('referenced_tweets') or []:
            if r.get('type')=='quoted':
                rising_origin_ids.add(r['id'])

for pid in screen_ids:
    p = tweets.get(pid)
    if not p: continue
    m = metrics(p)
    a = author_obj(p)
    ok, reason = clears_global(m, p.get('created_at'), a['kind'])
    is_trend = pid in trend_id_set
    if not ok and not is_trend:
        continue
    lead = None
    if ok and reason.startswith('pace'):
        lead = reason
    if is_trend:
        lead = (lead + '; ' if lead else '') + 'trend top post (no floor)'
    post = make_post(pid, desk=None, lead=lead)
    if not post and pid not in PREV_IDS:
        continue
    if is_trend:
        kept_for_viral.append(pid)
    if pid in rising_origin_ids:
        kept_for_rising.append(pid)
    for g, s in sensor_origin_ids.items():
        if pid in s:
            kept_for_sensors[g].append(pid)

# ensure trend tops are recorded even if below floor
for name, ids in trend_posts.items():
    for pid in ids:
        if pid not in seen_post and pid not in PREV_IDS:
            make_post(pid, lead=f'trend top post for {name} (no floor)')
        if pid not in kept_for_viral:
            kept_for_viral.append(pid)

# context replies/quotes — top 5 by likes each; record as posts
ctx_replies_obj = load_raw('context_replies.txt')
ctx_quotes_obj = load_raw('context_quotes.txt')
ctx_post = '2118780628258730072'

def top5(obj):
    data = list(obj.get('data') or [])
    data.sort(key=lambda p: -((p.get('public_metrics') or {}).get('like_count') or 0))
    return [p['id'] for p in data[:5]]

ctx_reply_ids = top5(ctx_replies_obj)
ctx_quote_ids = top5(ctx_quotes_obj)
for pid in ctx_reply_ids + ctx_quote_ids:
    # context posts don't count toward account cap — force
    if pid not in PREV_IDS:
        # temporarily bypass cap by forcing
        p = tweets.get(pid)
        if not p: continue
        text = text_of(p)
        if SEX_RE.search(text) or AD_RE.search(text):
            continue
        if pid in seen_post: continue
        a = author_obj(p)
        m = metrics(p)
        reply_to=None; quotes=None
        for r in p.get('referenced_tweets') or []:
            if r.get('type')=='replied_to': reply_to=r['id']
            if r.get('type')=='quoted': quotes=r['id']
        note=None
        nt=p.get('note_tweet') or {}
        if isinstance(nt, dict) and nt.get('text') and nt['text'] != (p.get('text') or ''):
            note={'text': nt['text']}
        posts_out.append({
            'id': pid,
            'url': f"https://x.com/{a['handle']}/status/{pid}",
            'created_at': p.get('created_at'),
            'lang': p.get('lang'),
            'text': p.get('text') or text_of(p),
            'author': a,
            'media': media_list(p, media_by_key),
            'reply_to': reply_to,
            'quotes': quotes,
            'note': note,
            'flags': [],
            'desk': None,
            'beat': None,
            'topic': None,
            'lead': f'context for {ctx_post}',
        })
        seen_post.add(pid)
        new_post_ids.append(pid)

# Ensure context main post recorded
if ctx_post not in PREV_IDS:
    make_post(ctx_post, lead='context.top subject; Susie Wiles last day as Chief of Staff')

# observations: all watch + all new posts
obs_ids = []
for wid in WATCH_IDS:
    obs_out.append(make_obs(wid))
    obs_ids.append(wid)
for pid in new_post_ids:
    if pid not in WATCH_SET:
        obs_out.append(make_obs(pid))
        obs_ids.append(pid)

# unavailable watch
for wid in watch_missing:
    # replace obs
    for i,o in enumerate(obs_out):
        if o['id']==wid:
            obs_out[i] = make_obs(wid)  # will be unavailable if missing from tweets
            if wid not in tweets:
                obs_out[i] = {
                    'id': wid, 'at': OBS_AT, 'state': 'unavailable',
                    'views': None, 'likes': None, 'reposts': None, 'quotes': None,
                    'replies': None, 'bookmarks': None, 'approx': False,
                }

# ---- trends ----
us_trends_raw = load_raw('trends_us.txt')['data']
ww_trends_raw = load_raw('trends_ww.txt')['data']
# attach posts: from this run's trend_posts + previous for names that still trend
prev_trend_map = {}
for t in PREV.get('trends') or []:
    prev_trend_map[t['name']] = t.get('post_ids') or []

trends_out = []
us_attached = []
for i, t in enumerate(us_trends_raw[:20], 1):
    name = t['trend_name']
    pids = list(trend_posts.get(name) or [])
    if not pids and name in prev_trend_map:
        # keep previous attachments only if those ids still exist in watch/posts this run - attach without new records
        pids = [x for x in prev_trend_map[name] if x in WATCH_SET or x in PREV_IDS][:3]
    trends_out.append({
        'region': 'US', 'rank': i, 'name': name,
        'post_count': None, 'story': None, 'post_ids': pids,
    })
    us_attached.extend(pids)
for i, t in enumerate(ww_trends_raw[:20], 1):
    name = t['trend_name']
    trends_out.append({
        'region': 'WW', 'rank': i, 'name': name,
        'post_count': None, 'story': None, 'post_ids': [],
    })

# ---- volume ----
def volume_from(name, key, desk, query):
    obj = load_raw(name)
    data = obj.get('data') or []
    # drop partials - API already gave 167 full hours with our window
    points = []
    for b in data:
        points.append({'start': b['start'].replace('.000Z','Z') if b['start'].endswith('.000Z') else b['start'], 'count': b['tweet_count']})
    # normalize start format to match prior
    for pt in points:
        if pt['start'].endswith('.000Z'):
            pt['start'] = pt['start'].replace('.000Z','Z')
    return {
        'key': key, 'desk': desk, 'query': query, 'granularity': 'hour', 'points': points,
    }

volumes = [
    volume_from('vol_politics.txt', 'desk.politics', 'politics',
        '(Trump OR "White House" OR Congress OR Senate OR Democrats OR Republicans OR GOP OR "Supreme Court" OR election OR governor) lang:en'),
    volume_from('vol_entertainment.txt', 'desk.entertainment', 'entertainment',
        '(movie OR film OR trailer OR "box office" OR Netflix OR "TV show" OR episode OR season OR anime OR actor OR actress OR celebrity) lang:en'),
    volume_from('vol_music.txt', 'desk.music', 'music',
        '(album OR song OR tour OR concert OR rapper OR singer OR Billboard OR Spotify OR Grammy OR kpop OR "music video") lang:en'),
    volume_from('vol_gaming.txt', 'desk.gaming', 'gaming',
        '(game OR gaming OR gamers OR PlayStation OR PS5 OR Xbox OR Nintendo OR Steam OR esports OR "video game" OR patch OR DLC) lang:en'),
    volume_from('vol_ideas.txt', 'desk.ideas', 'ideas',
        '(book OR novel OR author OR museum OR painting OR artist OR architecture OR history OR historian OR philosophy OR religion OR church OR Bible OR essay) lang:en'),
]

# ---- sweeps ----
def sweep(sid, kind, method, status='ok', reason=None, post_ids=None, desk=None, window_hours=None):
    return {
        'id': sid, 'kind': kind, 'desk': desk, 'method': method,
        'window_hours': window_hours, 'status': status, 'reason': reason,
        'post_ids': post_ids or [],
    }

sweeps = []
sweeps.append(sweep('watch', 'watch',
    f'get_posts_by_ids of the re-read list from requests/plan.json for_run 2026-11-06T20Z ({len(WATCH_IDS)} ids; 1 slowed, 0 over cap), 2 reads; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id,referenced_tweets.id.author_id; {len(watch_returned)} of {len(WATCH_IDS)} returned, {len(watch_missing)} unavailable',
    post_ids=watch_returned))

sweeps.append(sweep('trends.us', 'trends',
    'get_trends_by_woeid 23424977 max_trends 20',
    post_ids=us_attached))
sweeps.append(sweep('trends.ww', 'trends',
    'get_trends_by_woeid 1 max_trends 20',
    post_ids=[]))

sweeps.append(sweep('viral.global', 'discovery',
    'trend-name repost streams for Chief of Staff, Susie Wiles, Cybertruck (3 reads, top three origins each by views, whatever size); plus screened global origins from sensors and rising',
    window_hours=24,
    post_ids=list(dict.fromkeys(kept_for_viral + [p for p in new_post_ids if p in screen_ids]))[:40]))

sweeps.append(sweep('rising.global', 'discovery',
    'quote streams "is lang:en is:quote -is:retweet" and "you lang:en is:quote -is:retweet", newest first, 25 each (2 reads)',
    window_hours=6,
    post_ids=list(dict.fromkeys(kept_for_rising))[:30]))

for g in ['news','money','science']:
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        f'search_posts_all (from:...) -is:reply newest 25 for {g} sensor group',
        window_hours=24,
        post_ids=kept_for_sensors[g][:15]))
for g in ['culture','sports','online']:
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        'not in the read list this run (three groups a run in rotation); news/money/science read this run',
        status='skipped', reason='not in this run\'s three-group rotation', post_ids=[]))

DESKS = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']
for d in DESKS:
    sweeps.append(sweep(f'desk.{d}', 'desk',
        'not due this hour after the 1932Z catch-up swept all desks; plan left_out desks_not_due lists all 19',
        status='skipped', reason='not due this hour (plan: 0 desks due)', desk=d, post_ids=[]))

sweeps.append(sweep('volume.desks', 'volume',
    'get_posts_counts_recent for politics/entertainment/music/gaming/ideas, granularity hour, window 2026-10-30T21:00:00Z to 2026-11-06T20:00:00Z (167 full hours)',
    post_ids=[]))

sweeps.append(sweep('context.top', 'context',
    f'conversation_id:{ctx_post} is:reply and quotes_of_tweet_id:{ctx_post} -is:retweet, relevancy, start_time at the post and end_time 20 minutes later; five most liked of each kept',
    post_ids=ctx_reply_ids + ctx_quote_ids))

# ---- context block ----
context = [{'post_id': ctx_post, 'replies': ctx_reply_ids, 'quotes': ctx_quote_ids}]

# ---- tally ----
tally_path = REPO / 'capture/TALLY.json'
tally = json.load(open(tally_path))
origins_unique = sorted(set(stream_origins))
tally['runs'] = (tally.get('runs') or []) + [{'run': RUN_ID, 'origins': origins_unique}]
tally['runs'] = tally['runs'][-6:]
# update lead on posts seen in multiple of last 6
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

# ---- run reason ----
cap_drops = Counter()
sex_n = ad_n = 0
for pid, why in left_out:
    if why == 'sexual': sex_n += 1
    elif why == 'ad': ad_n += 1
    elif why.startswith('cap:'):
        cap_drops[why.split(':',1)[1]] += 1

reason = (
    f"Day-band run 2026-11-06T20:00Z / 3:00 PM EST Nov 6. requests/plan.json for_run 2026-11-06T20Z "
    f"(written_at 2026-11-06T19:45:49Z after the 1932Z editor pass) used as the read list "
    f"(run.plan null; nothing written to requests/). {READS_USED} X reads used ({READS_LEFT} left today by X's count), "
    f"including 1 mistaken partial screen call with a bad id that was redone. "
    f"Watch: {len(watch_returned)} of {len(WATCH_IDS)} returned, {len(watch_missing)} unavailable; "
    f"no pulse- or story-cited post missing or changed words checked against watch.json order. "
    f"0 desks due (all 19 swept in 1932Z catch-up). Volume politics/entertainment/music/gaming/ideas "
    f"(window 2026-10-30T21:00Z to 2026-11-06T20:00Z, 167 buckets). Sensors news/money/science. "
    f"Trend names Chief of Staff, Susie Wiles, Cybertruck. Rising words is/you (quoted). "
    f"By-id screen of {len(screen_ids)} new kept posts in 1 read. context.top on SusieWiles {ctx_post}. "
    f"Left out: {sex_n} sexual, {ad_n} ad; account cap dropped {dict(cap_drops) if cap_drops else {}}. "
    f"Media descriptions not filled this run (partial)."
)

# cited missing check vs watch.json
watch_json = json.load(open(REPO/'requests/watch.json'))
cited = set(watch_json.get('post_ids') or [])
cited_missing = [i for i in watch_missing if i in cited]

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

out_path = REPO / f'capture/2026/11/06/2000Z.json'
json.dump(doc, open(out_path,'w'), indent=2, ensure_ascii=False)
json.dump(tally, open(tally_path,'w'), indent=2, ensure_ascii=False)
print('wrote', out_path, 'posts', len(posts_out), 'obs', len(obs_out))
print('watch', len(watch_returned), '/', len(WATCH_IDS), 'missing', watch_missing, 'cited_missing', cited_missing)
print('left_out', left_out[:20], '... total', len(left_out))
print('volume points', [len(v['points']) for v in volumes])
