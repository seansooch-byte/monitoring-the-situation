#!/usr/bin/env python3
"""Build capture/2026/11/06/2101Z.json from saved X outputs."""
import json, re, os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

W = Path('/workspace/grabber-work/2026-11-06T2101Z')
REPO = Path('/workspace/monitoring-the-situation')
RUN_ID = '2026-11-06T2101Z'
STARTED = '2026-11-06T21:01:00Z'
FINISHED = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
OBS_AT = '2026-11-06T21:07:00Z'
REQUESTS_REV = open(W/'requests_rev.txt').read().strip()
READS_USED = 25  # 928 -> 903
READS_LEFT = 903
PREV = json.load(open(REPO / 'capture/2026/11/06/2000Z.json'))
PREV_IDS = {p['id'] for p in PREV['posts']} | {o['id'] for o in PREV['observations']}
# also 1932Z posts
PREV1932 = json.load(open(REPO / 'capture/2026/11/06/1932Z.json'))
PREV_IDS |= {p['id'] for p in PREV1932['posts']}
PLAN = json.load(open(W / 'plan.json'))
WATCH_IDS = PLAN['items'][0]['ids']
WATCH_SET = set(WATCH_IDS)
SEL = json.load(open(W / 'sel.json'))

NEWS = {'BBCBreaking','Reuters','SkyNews','AP','CNN','nytimes','washingtonpost','FoxNews','ABC','CBSNews','NBCNews','WSJ','WFLA','APNews'}
ORG = {'NFL','NBA','MLB','NHL','UFC','SpaceX','NASA','WhiteHouse','DOJ','FBI','SecKennedy','CDCgov','NASAAdmin','PopBase','PopCrave','Dexerto','Variety','MacRumors','Cointelegraph','BitcoinMagazine','IGN','DiscussingFilm','SportsCenter','BleacherReport','FabrizioRomano','Tesla','PeteHegseth','cspan'}
AGG = {'EricLDaugh','atrupar','LeadingReport','CollinRugg','visegrad24','rawsalerts','WatcherGuru','cryptorover','AshCrypto','BitcoinArchive','PopBase','PopCrave','CultureCrave','MeidasTouch','unusual_whales','MarioNawfal','EndWokeness'}

SEX_RE = re.compile(r'(onlyfans|nsfw|porn|xxx|hentai|nude|nudes|\banal\b|boobs|pussy|cock\b)', re.I)
AD_RE = re.compile(r'(#ad\b|giveaway|airdrop|memecoin|promo code|paid partnership)', re.I)

DESK_FLOOR = {
  'politics': (50000, 1000), 'entertainment': (50000, 1000),
  'sports': (50000, 1000), 'internet': (50000, 1000),
}

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
        tweets[p['id']] = p
    errors_by_file[name] = obj.get('errors') or []
    return obj

for fname in [
    'watch1.txt','watch2.txt',
    'desk_politics.txt','desk_entertainment.txt','desk_sports.txt','desk_internet.txt',
    'sensor_culture.txt','sensor_sports.txt','sensor_online.txt',
    'rising_my.txt','rising_it.txt',
    'trend_alcaraz.txt','trend_tyler.txt','trend_trump_op.txt',
    'screen1.txt','screen2.txt','context_replies.txt','context_quotes.txt',
]:
    ingest(fname)

watch_err_ids = set()
for name in ['watch1.txt','watch2.txt']:
    for e in errors_by_file.get(name) or []:
        watch_err_ids.add(str(e.get('resource_id') or e.get('value') or ''))
watch_returned = []
watch_missing = []
for wid in WATCH_IDS:
    if wid in watch_err_ids or wid not in tweets:
        watch_missing.append(wid)
    else:
        watch_returned.append(wid)

# stream origins for tally
stream_origins = []
for name in ['rising_my.txt','rising_it.txt']:
    obj = load_raw(name)
    for p in obj.get('data') or []:
        for r in p.get('referenced_tweets') or []:
            if r.get('type') == 'quoted':
                stream_origins.append(r['id'])

ref_counts = Counter()
for name in ['desk_politics.txt','desk_entertainment.txt','desk_sports.txt','desk_internet.txt',
             'sensor_culture.txt','sensor_sports.txt','sensor_online.txt',
             'rising_my.txt','rising_it.txt','trend_alcaraz.txt','trend_tyler.txt','trend_trump_op.txt',
             'watch1.txt','watch2.txt']:
    obj = load_raw(name)
    for p in (obj.get('data') or []) + ((obj.get('includes') or {}).get('tweets') or []):
        for r in p.get('referenced_tweets') or []:
            ref_counts[r['id']] += 1
        src = (p.get('attachments') or {}).get('media_source_tweet_id') or []
        for mid in src:
            ref_counts[mid] += 1

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
    # long text stored in note (repo convention)
    note = None
    if full and full != short:
        note = {'text': full}
    flags = []
    created = p.get('created_at')
    if created and age_h(created) > 24*7:
        flags.append('old_content')
    lang = p.get('lang')
    if lang and lang not in ('en', 'und', None) and 'non_english' not in flags:
        # keep but flag
        if lang not in ('en',):
            flags.append('non_english')
    lead_bits = []
    if lead: lead_bits.append(lead)
    if ref_counts.get(pid, 0) >= 2:
        lead_bits.append(f'pointed at by {ref_counts[pid]} posts read this run')
    # media_source
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
    if msrc:
        post['media_source'] = msrc
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

# map pid -> desk from sel sweeps
pid_desk = {}
for sw, ids in SEL.get('sweeps', {}).items():
    if sw.startswith('desk.'):
        for i in ids:
            pid_desk[i] = sw[5:]

trend_posts = SEL.get('trend') or {}
trend_id_set = set()
for ids in trend_posts.values():
    trend_id_set.update(ids)

# Build posts from sel.kept in ranked order
for pid in SEL.get('ranked') or SEL.get('kept') or []:
    desk = pid_desk.get(pid)
    lead = None
    p = tweets.get(pid)
    if p:
        m = metrics(p)
        ah = age_h(p['created_at']) if p.get('created_at') else 99
        if 0.25 <= ah <= 3 and (m['views'] or 0) >= 10000:
            pace = int((m['views'] or 0) / ah)
            if pace >= 25000:
                lead = f'pace {pace}/h'
        if pid in trend_id_set:
            for n, ids in trend_posts.items():
                if pid in ids:
                    lead = (lead + '; ' if lead else '') + f'top post for trend "{n}"'
                    break
    make_post(pid, desk=desk, lead=lead)

# ensure all trend tops recorded
for name, ids in trend_posts.items():
    for pid in ids[:3]:
        if pid not in seen_post and pid not in PREV_IDS:
            make_post(pid, lead=f'top post for trend "{name}" (no floor)')
        elif pid not in seen_post and pid in PREV_IDS:
            pass  # attach without new record

# context
ctx_post = open(W/'context_id.txt').read().strip()
ctx_replies_obj = load_raw('context_replies.txt')
ctx_quotes_obj = load_raw('context_quotes.txt')

def top5(obj):
    data = list(obj.get('data') or [])
    data.sort(key=lambda p: -((p.get('public_metrics') or {}).get('like_count') or 0))
    return [p['id'] for p in data[:5]]

ctx_reply_ids = top5(ctx_replies_obj)
ctx_quote_ids = top5(ctx_quotes_obj)
for pid in ctx_reply_ids + ctx_quote_ids:
    if pid in PREV_IDS or pid in seen_post: continue
    p = tweets.get(pid)
    if not p: continue
    full = text_of(p)
    if SEX_RE.search(full) or AD_RE.search(full): continue
    make_post(pid, lead=f'context for {ctx_post}', skip_cap=True)

if ctx_post not in PREV_IDS and ctx_post not in seen_post:
    make_post(ctx_post, desk='politics', lead='context.top subject; Pete Hegseth "Patriots in control"')

# observations: watch + new posts
for wid in WATCH_IDS:
    obs_out.append(make_obs(wid))
for pid in new_post_ids:
    if pid not in WATCH_SET:
        obs_out.append(make_obs(pid))

# fix unavailable
for i,o in enumerate(obs_out):
    if o['id'] in watch_missing:
        obs_out[i] = {
            'id': o['id'], 'at': OBS_AT, 'state': 'unavailable',
            'views': None, 'likes': None, 'reposts': None, 'quotes': None,
            'replies': None, 'bookmarks': None, 'approx': False,
        }

# trends
us_trends_raw = load_raw('trends_us.txt')['data']
ww_trends_raw = load_raw('trends_ww.txt')['data']
prev_trend_map = {}
for t in PREV.get('trends') or []:
    if t['region']=='US':
        prev_trend_map[t['name']] = t.get('post_ids') or []

trends_out = []
us_attached = []
seen_us_names = set()
rank = 0
for t in us_trends_raw[:30]:
    name = t['trend_name']
    # skip exact duplicate consecutive names? keep both ranks as X shows
    rank += 1
    if rank > 20: break
    pids = list(trend_posts.get(name) or [])[:3]
    if not pids and name in prev_trend_map:
        pids = [x for x in prev_trend_map[name] if x in WATCH_SET or x in PREV_IDS][:3]
    trends_out.append({
        'region': 'US', 'rank': rank, 'name': name,
        'post_count': None, 'story': None, 'post_ids': pids,
    })
    us_attached.extend(pids)
for i, t in enumerate(ww_trends_raw[:20], 1):
    trends_out.append({
        'region': 'WW', 'rank': i, 'name': t['trend_name'],
        'post_count': None, 'story': None, 'post_ids': [],
    })

def volume_from(name, key, desk, query):
    obj = load_raw(name)
    data = obj.get('data') or []
    points = []
    for b in data:
        st = b['start']
        if st.endswith('.000Z'): st = st.replace('.000Z','Z')
        points.append({'start': st, 'count': b['tweet_count']})
    return {'key': key, 'desk': desk, 'query': query, 'granularity': 'hour', 'points': points}

volumes = [
    volume_from('vol_sports.txt', 'desk.sports', 'sports',
        '(NFL OR NBA OR MLB OR NHL OR WNBA OR UFC OR "Premier League" OR soccer OR touchdown OR playoffs OR "home run" OR F1 OR golf OR tennis) lang:en'),
    volume_from('vol_internet.txt', 'desk.internet', 'internet',
        '(meme OR memes OR streamer OR stream OR Twitch OR Kick OR YouTuber OR TikTok OR influencer OR podcast OR fandom OR "main character") lang:en'),
    volume_from('vol_life.txt', 'desk.life', 'life',
        '(dating OR boyfriend OR girlfriend OR husband OR wife OR marriage OR parents OR kids OR restaurant OR recipe OR wedding OR rent OR tipping OR college OR habit) lang:en'),
    volume_from('vol_offbeat.txt', 'desk.offbeat', 'offbeat',
        '(dog OR cat OR puppy OR kitten OR animal OR wildlife OR bird OR satisfying OR wholesome OR "wait for it") lang:en'),
    volume_from('vol_world.txt', 'desk.world', 'world',
        '(Ukraine OR Russia OR Israel OR Gaza OR Iran OR China OR "prime minister" OR president OR protesters OR protest OR migrants OR refugees OR ceasefire OR NATO OR "United Nations") lang:en'),
]

def sweep(sid, kind, method, status='ok', reason=None, post_ids=None, desk=None, window_hours=None):
    return {
        'id': sid, 'kind': kind, 'desk': desk, 'method': method,
        'window_hours': window_hours, 'status': status, 'reason': reason,
        'post_ids': post_ids or [],
    }

sweeps = []
sweeps.append(sweep('watch', 'watch',
    f'get_posts_by_ids of the re-read list from requests/plan.json for_run 2026-11-06T21Z ({len(WATCH_IDS)} ids; plan left_out 1 slowed, 0 over cap), 2 reads; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id,referenced_tweets.id.author_id; {len(watch_returned)} of {len(WATCH_IDS)} returned, {len(watch_missing)} unavailable',
    post_ids=watch_returned))

trend_reason = (
    'US top-ten names with no posts attached in 2000Z and not read as names in the last three captures: '
    'Alcaraz, Tyler Perry, Trump Political Operation (3 viral.global reads). '
    'Stephen Miller/#RTXON/Azzi were read as names in 1932Z; Susie Wiles and Cybertruck had posts attached in 2000Z. '
    'Duplicate Stephen Miller rows kept as X returned them.'
)
sweeps.append(sweep('trends.us', 'trends', 'get_trends_by_woeid 23424977 max_trends 20',
    reason=trend_reason, post_ids=list(dict.fromkeys(us_attached))))
sweeps.append(sweep('trends.ww', 'trends', 'get_trends_by_woeid 1 max_trends 20', post_ids=[]))

viral_ids = list(dict.fromkeys(
    (SEL.get('sweeps') or {}).get('viral.global', []) +
    [i for ids in trend_posts.values() for i in ids] +
    [p for p in new_post_ids if p not in WATCH_SET]
))[:40]
sweeps.append(sweep('viral.global', 'discovery',
    'trend-name repost streams for Alcaraz, Tyler Perry, Trump Political Operation (3 reads, top three origins each by views, whatever size); plus screened global origins from references, sensors and rising',
    window_hours=24, post_ids=viral_ids))

rising_ids = list(dict.fromkeys((SEL.get('sweeps') or {}).get('rising.global', [])))[:30]
sweeps.append(sweep('rising.global', 'discovery',
    'quote streams "my lang:en is:quote -is:retweet" and "it lang:en is:quote -is:retweet", newest first, 25 each (2 reads); words after is/you in the rotation (and skipped as X rejects it)',
    window_hours=6, post_ids=rising_ids))

for g in ['news','money','science']:
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        'not in the read list this run (three groups a run in rotation); culture/sports/online read this run',
        status='skipped', reason='not in this run\'s three-group rotation', post_ids=[]))
for g in ['culture','sports','online']:
    ids = list(dict.fromkeys((SEL.get('sweeps') or {}).get(f'sensors.{g}', [])))[:15]
    sweeps.append(sweep(f'sensors.{g}', 'discovery',
        f'search_posts_all sensor group {g} (from:...) -is:reply newest 25; reposts followed to origin; screened by global floor/pace',
        window_hours=6, post_ids=ids))

DUE = ['politics','entertainment','sports','internet']
NOTDUE = PLAN['left_out']['desks_not_due']
DESK_Q = {
  'politics': '(Trump OR "White House" OR Congress OR Senate OR Democrats OR Republicans OR GOP OR "Supreme Court" OR election OR governor) lang:en is:retweet -is:reply',
  'entertainment': '(movie OR film OR trailer OR "box office" OR Netflix OR "TV show" OR episode OR season OR anime OR actor OR actress OR celebrity) lang:en is:retweet -is:reply',
  'sports': '(NFL OR NBA OR MLB OR NHL OR WNBA OR UFC OR "Premier League" OR soccer OR touchdown OR playoffs OR "home run" OR F1 OR golf OR tennis) lang:en is:retweet -is:reply',
  'internet': '(meme OR memes OR streamer OR stream OR Twitch OR Kick OR YouTuber OR TikTok OR influencer OR podcast OR fandom OR "main character") lang:en is:retweet -is:reply',
}
ALL_DESKS = ['politics','world','defense','justice','disaster','markets','business','ai','tech','science','medicine','entertainment','music','gaming','ideas','sports','internet','life','offbeat']
for d in ALL_DESKS:
    if d in DUE:
        ids = list(dict.fromkeys((SEL.get('sweeps') or {}).get(f'desk.{d}', [])))[:10]
        sweeps.append(sweep(f'desk.{d}', 'desk',
            f'search_posts_all {DESK_Q[d]} newest first, 25 results; reposted origins screened by desk floor/pace; keep at most five best per desk',
            desk=d, window_hours=24, post_ids=ids))
    else:
        sweeps.append(sweep(f'desk.{d}', 'desk',
            f'not due this hour (plan desks_not_due); last read in 2026-11-06T1932Z catch-up',
            status='skipped', reason='not due this hour (plan: desks_not_due)', desk=d, post_ids=[]))

sweeps.append(sweep('volume.desks', 'volume',
    'get_posts_counts_recent for sports/internet/life/offbeat/world, granularity hour, window 2026-10-30T22:00:00Z to 2026-11-06T21:00:00Z (167 full hours each)',
    post_ids=[]))

sweeps.append(sweep('context.top', 'context',
    f'conversation_id:{ctx_post} is:reply and quotes_of_tweet_id:{ctx_post} -is:retweet, relevancy, start_time 2026-11-06T19:27:50Z end_time 2026-11-06T19:47:50Z; five most liked of each kept',
    post_ids=ctx_reply_ids + ctx_quote_ids))

context = [{'post_id': ctx_post, 'replies': ctx_reply_ids, 'quotes': ctx_quote_ids}]

# tally
tally_path = REPO / 'capture/TALLY.json'
tally = json.load(open(tally_path))
origins_unique = sorted(set(stream_origins))
tally['runs'] = (tally.get('runs') or []) + [{'run': RUN_ID, 'origins': origins_unique}]
tally['runs'] = tally['runs'][-6:]
origin_freq = Counter()
for run in tally['runs']:
    for o in set(run.get('origins') or []):
        origin_freq[o] += 1
for post in posts_out:
    n = origin_freq.get(post['id'], 0)
    if n >= 1 and post['id'] in set(stream_origins):
        lead = post.get('lead') or ''
        bit = f'seen in the quote or repost stream in {n} of the last 6 runs'
        if bit not in lead:
            post['lead'] = (lead + '; ' + bit) if lead else bit

cap_drops = Counter()
sex_n = ad_n = 0
for pid, why in left_out + [(a,b) for a,b in (SEL.get('left_out') or [])]:
    if why == 'sexual' or why == 'sexual/graphic': sex_n += 1
    elif why == 'ad': ad_n += 1
    elif isinstance(why,str) and why.startswith('cap'):
        cap_drops[why] += 1

# also account caps from sel
for h,n in (SEL.get('capdrops') or {}).items():
    if isinstance(n, int) and n > 3:
        cap_drops[h] = n - 3

reason = (
    f"Day-band run 2026-11-06T21:01Z / 4:01 PM EST Nov 6. requests/plan.json for_run 2026-11-06T21Z "
    f"(written_at 2026-11-06T20:07:53Z after the 2000Z editor pass) used as the read list "
    f"(run.plan null; nothing written to requests/). {READS_USED} X reads used ({READS_LEFT} left today by X's count); "
    f"screen used 2 of its 3 planned reads. "
    f"Watch: {len(watch_returned)} of {len(WATCH_IDS)} returned, {len(watch_missing)} unavailable; "
    f"no pulse- or story-cited post missing or changed words (5 truncation-only diffs where note_tweet filled truncated text; "
    f"watch.json id 2024917454301065480 is the 1 slowed post left out of this run's re-read list per the plan). "
    f"4 desks due (politics, entertainment, sports, internet). Volume sports/internet/life/offbeat/world "
    f"(window 2026-10-30T22:00Z to 2026-11-06T21:00Z, 167 buckets). Sensors culture/sports/online. "
    f"Trend names Alcaraz, Tyler Perry, Trump Political Operation. Rising words my/it (quoted). "
    f"By-id screen of {len(SEL.get('kept') or [])} candidates in 2 reads. context.top on PeteHegseth {ctx_post}. "
    f"Left out: {sex_n} sexual/graphic; account cap dropped {dict(cap_drops) if cap_drops else {}}. "
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

out_path = REPO / f'capture/2026/11/06/2101Z.json'
json.dump(doc, open(out_path,'w'), indent=2, ensure_ascii=False)
json.dump(tally, open(tally_path,'w'), indent=2, ensure_ascii=False)
print('wrote', out_path, 'posts', len(posts_out), 'obs', len(obs_out))
print('watch', len(watch_returned), '/', len(WATCH_IDS), 'missing', watch_missing)
print('left_out sample', left_out[:15], 'total', len(left_out))
print('volume points', [len(v['points']) for v in volumes])
print('context', ctx_post, 'replies', ctx_reply_ids, 'quotes', ctx_quote_ids)
print('trends US with posts', [(t['rank'],t['name'],t['post_ids']) for t in trends_out if t['region']=='US' and t['post_ids']])
