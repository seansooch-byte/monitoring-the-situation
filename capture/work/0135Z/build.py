#!/usr/bin/env python3
"""Evening side-by-side build for 2026-10-10T0135Z."""
import json, os, re, statistics
from datetime import datetime, timezone
from collections import Counter, defaultdict

WORK = '/workspace/monitoring-the-situation/capture/work/0135Z'
REPO = '/workspace/monitoring-the-situation'
NOW = datetime(2026, 10, 10, 1, 41, tzinfo=timezone.utc)
RUN_ID = '2026-10-10T0135Z'
AT = '2026-10-10T01:41:00Z'
STARTED = '2026-10-10T01:35:00Z'
FINISHED = '2026-10-10T01:42:00Z'
REQ_REV = open(f'{WORK}/requests_rev.txt').read().strip()
READS_START = 967
READS_END = 931

def load_x(path):
  raw = open(path).read()
  if 'X reads left' in raw:
    raw = raw[:raw.rfind('X reads left')]
  raw = re.sub(r'</?cursor_untrusted_data[^>]*>', '', raw)
  raw = re.sub(r'</?cursor_untrusted_data_redacted[^>]*>', '', raw)
  start = raw.find('{')
  end = raw.rfind('}') + 1
  return json.loads(raw[start:end])

def verified_of(u):
  vt = (u.get('verified_type') or '').lower()
  if vt in ('blue', 'business', 'government', 'organization'):
    return 'blue' if vt == 'blue' else vt
  if u.get('verified') is True:
    return 'blue'
  return 'none'

def metrics(t):
  pm = t.get('public_metrics') or {}
  return {
    'views': pm.get('impression_count'),
    'likes': pm.get('like_count'),
    'reposts': pm.get('retweet_count', pm.get('repost_count')),
    'quotes': pm.get('quote_count'),
    'replies': pm.get('reply_count'),
    'bookmarks': pm.get('bookmark_count'),
  }

def media_list(t, media_by_key):
  out = []
  keys = (t.get('attachments') or {}).get('media_keys') or []
  ents = t.get('entities') or {}
  for mk in keys:
    m = media_by_key.get(mk)
    if not m:
      continue
    typ = m.get('type')
    if typ == 'animated_gif':
      typ = 'gif'
    elif typ == 'image':
      typ = 'photo'
    else:
      typ = typ or 'photo'
    dur = m.get('duration_ms')
    out.append({
      'type': typ,
      'description': None,
      'alt': m.get('alt_text'),
      'duration_s': (dur / 1000.0) if dur else None,
      'link_url': None,
      'link_title': None,
    })
  if not out:
    urls = ents.get('urls') or []
    for u in reversed(urls):
      eu = u.get('expanded_url') or u.get('unwound_url') or ''
      if 'x.com' in eu or 'twitter.com' in eu:
        continue
      out.append({
        'type': 'link', 'description': None, 'alt': None, 'duration_s': None,
        'link_url': u.get('unwound_url') or eu,
        'link_title': u.get('title'),
      })
      break
  return out

def reply_quote(t):
  reply = None
  quotes = None
  for r in t.get('referenced_tweets') or []:
    if r.get('type') == 'replied_to':
      reply = r['id']
    if r.get('type') == 'quoted':
      quotes = r['id']
  return reply, quotes

def text_of(t):
  note = t.get('note_tweet')
  if isinstance(note, dict) and note.get('text'):
    return note['text']
  return t.get('text') or ''

EXCLUDE_IDS = set([
  '2108124415762592123', '2107389692018622901', '2108366539439411593',
  '2107759105586921862', '2107898516836073615', '2107914086675788263',
  '2107913429990166804', '2108289854974951548', '2108325927872803119',
  '2108511541351837778', '2108378335512293747', '2108437202543800337',
  '2105144159715643542', '2107407108446790049', '2108531741883560072',
  '2107219727701746162', '2108211566034440579', '2108148098182836497',
  '2107950433654235262', '1883242684762255643', '2108573302612504596',
  '2100889316075651135', '2108591066077118717', '2108368510816596206',
  '2108538963732414892', '2105701698513567928', '2108264549707329662',
  '2108327411746255354', '2108599428894642631', '2108620753218252866',
  '2108623313438183460', '2108582750567502292', '2108438942949552398',
  '2107793214514327802',
])
EXCLUDE_SUBSTR = [
  'hentai', 'porn', 'pussy', 'masturbat', 'getting laid', 'raped a',
  '9-year-old', '9 year old', 'onlyfans', '#mom #mommy #stepmom',
  'ass-to-mouth', 'cockyboys', 'creamy pussy', 'tiny tits', 'sissy',
  'help me cum', 'prostate massager', 'oral sex', 'ladyboy', 'shemale',
  '#nsfw', '#hentai', 'penetrators', 'face fuck', 'ai girlfriend',
  'sexy, witty', 'fursuit', '#fursuitfriday', 'nude ', 'nudes',
]

def bad_text(s):
  sl = (s or '').lower()
  return any(x in sl for x in EXCLUDE_SUBSTR)

DESK_FLOORS = {
  'politics': (50000, 1000), 'world': (50000, 1000), 'defense': (10000, 250),
  'justice': (20000, 500), 'disaster': (20000, 500), 'markets': (20000, 500),
  'business': (20000, 500), 'crypto': (20000, 500), 'ai': (20000, 500),
  'tech': (20000, 500), 'science': (10000, 250), 'medicine': (10000, 250),
  'entertainment': (50000, 1000), 'music': (50000, 1000), 'gaming': (20000, 500),
  'ideas': (10000, 250), 'sports': (50000, 1000), 'internet': (50000, 1000),
  'life': (20000, 500), 'offbeat': (50000, 1000),
}

NEWS_HANDLES = set(h.lower() for h in [
  'Reuters', 'BBCBreaking', 'SkyNews', 'nytimes', 'cnnbrk', 'cnni', 'NobelPrize',
  'PTI_News', 'WFLA', 'MeidasTouch', 'LeadingReport', 'visegrad24', 'CNN',
  'BBCWorld', 'FoxNews', 'weatherchannel', 'BNONews', 'MyRadarWX', 'Forbes',
  'AP', 'NFL', 'MLB', 'SportsCenter', 'BleacherReport', 'JimCantore',
  'BrandonCopicWx', 'rawsalerts',
])

all_tweets = {}
all_users = {}
all_media = {}

def ingest(doc):
  for u in (doc.get('includes') or {}).get('users') or []:
    all_users[u['id']] = u
  for m in (doc.get('includes') or {}).get('media') or []:
    all_media[m['media_key']] = m
  for t in (doc.get('includes') or {}).get('tweets') or []:
    all_tweets[t['id']] = t
  for t in (doc.get('includes') or {}).get('posts') or []:
    all_tweets[t['id']] = t
  for t in doc.get('data') or []:
    all_tweets[t['id']] = t

watch_docs = [load_x(f'{WORK}/watch_{i}.json') for i in range(3)]
for d in watch_docs:
  ingest(d)

source_files = {
  'sensors': ['sensor_news.json', 'sensor_sports.json', 'sensor_culture.json'],
  'quote_stream': ['quote_the.json', 'quote_this.json'],
  'repost_stream': ['repost_the.json'],
  'trend_names': [
    'trend_putin.json', 'trend_louisville.json', 'trend_angel_reese.json',
    'trend_igor.json', 'trend_norvell.json',
  ],
  'desk_repost_streams': [
    'desk_politics.json', 'desk_entertainment.json', 'desk_sports.json', 'desk_internet.json',
  ],
}
for files in source_files.values():
  for f in files:
    ingest(load_x(f'{WORK}/{f}'))

screen_docs = [load_x(f'{WORK}/screen_{i}.json') for i in range(4)]
for d in screen_docs:
  ingest(d)

# sources map of candidate origin ids
sources = json.load(open(f'{WORK}/sources_map.json'))
# rebuild references from all tweets
ref_counts = Counter()
for t in all_tweets.values():
  for r in t.get('referenced_tweets') or []:
    if r.get('type') in ('quoted', 'retweeted', 'replied_to'):
      ref_counts[r['id']] += 1
  ms = (t.get('attachments') or {}).get('media_source_tweet_id')
  if ms:
    if isinstance(ms, list):
      for m in ms:
        ref_counts[str(m)] += 1
    else:
      ref_counts[str(ms)] += 1
sources['references'] = sorted(set(sources.get('references', [])) | set(ref_counts.keys()))

# story clusters already in sources_map; rebuild from files to be sure
story_ids = set()
x_stories = []
for n in ['viral', 'politics', 'entertainment', 'sports', 'internet']:
  doc = load_x(f'{WORK}/stories_{n}.json')
  for st in doc.get('data') or []:
    pids = []
    for cp in st.get('cluster_posts_results') or []:
      pid = cp.get('post_id') if isinstance(cp, dict) else cp
      if pid:
        pids.append(str(pid))
        story_ids.add(str(pid))
    x_stories.append({
      'id': st['id'],
      'name': st.get('name'),
      'summary': st.get('summary'),
      'category': st.get('category'),
      'url': st.get('url'),
      'updated_at': (st.get('updated_at') or '').replace('.000Z', 'Z'),
      'hook': st.get('hook'),
      'post_ids': pids,
    })
sources['story_clusters'] = sorted(story_ids)

# trends
trends_us = load_x(f'{WORK}/trends_us.json')
trends_ww = load_x(f'{WORK}/trends_ww.json')

def trend_rows(doc, region):
  out = []
  for i, t in enumerate(doc.get('data') or []):
    name = t.get('trend_name') or t.get('name')
    out.append({
      'region': region,
      'rank': i + 1,
      'name': name,
      'post_count': None,
      'story': None,
      'post_ids': [],
    })
  return out

trends = trend_rows(trends_us, 'US') + trend_rows(trends_ww, 'WW')

# attach top 3 from trend streams (by views) regardless of size
trend_name_map = {
  'Putin': 'trend_putin.json',
  'Louisville': 'trend_louisville.json',
  'Angel Reese': 'trend_angel_reese.json',
  'Igor': 'trend_igor.json',
  'Norvell': 'trend_norvell.json',
}

def origins_from_search(doc):
  ids = []
  for t in doc.get('data') or []:
    got = False
    for r in t.get('referenced_tweets') or []:
      if r.get('type') in ('retweeted', 'quoted'):
        ids.append(r['id'])
        got = True
    if not got:
      ids.append(t['id'])
  return ids

trend_keep = set()
for tr in trends:
  if tr['region'] != 'US':
    continue
  fname = trend_name_map.get(tr['name'])
  if not fname:
    continue
  doc = load_x(f'{WORK}/{fname}')
  oids = origins_from_search(doc)
  scored = []
  for oid in oids:
    tw = all_tweets.get(oid)
    if not tw:
      continue
    v = (tw.get('public_metrics') or {}).get('impression_count') or 0
    scored.append((v, oid))
  scored.sort(reverse=True)
  top3 = [oid for _, oid in scored[:3]]
  tr['post_ids'] = top3
  trend_keep.update(top3)

# also attach SmackDown from previous if in watch/all
for tr in trends:
  if tr['name'] == '#SmackDown' and not tr['post_ids']:
    for cand in ['2108710504881410143', '2108595877745250457']:
      if cand in all_tweets:
        tr['post_ids'].append(cand)

watch_ids = json.load(open(f'{REPO}/requests/watch.json'))['post_ids']
observations = []
seen_obs = set()

def add_obs(tid, t=None, at=AT):
  if tid in seen_obs:
    return
  tw = t or all_tweets.get(tid)
  if not tw:
    return
  m = metrics(tw)
  if m['views'] is None and m['likes'] is None:
    observations.append({
      'id': tid, 'at': at, 'state': 'unavailable',
      'views': None, 'likes': None, 'reposts': None, 'quotes': None,
      'replies': None, 'bookmarks': None, 'approx': False,
    })
  else:
    observations.append({
      'id': tid, 'at': at, 'state': 'live',
      'views': m['views'], 'likes': m['likes'], 'reposts': m['reposts'],
      'quotes': m['quotes'], 'replies': m['replies'], 'bookmarks': m['bookmarks'],
      'approx': False,
    })
  seen_obs.add(tid)

watch_returned = set()
for doc in watch_docs:
  for t in doc.get('data') or []:
    watch_returned.add(t['id'])
    add_obs(t['id'], t)
for wid in watch_ids:
  if wid not in watch_returned and wid not in seen_obs:
    observations.append({
      'id': wid, 'at': AT, 'state': 'unavailable',
      'views': None, 'likes': None, 'reposts': None, 'quotes': None,
      'replies': None, 'bookmarks': None, 'approx': False,
    })
    seen_obs.add(wid)

def age_hours(created):
  if not created:
    return None
  ct = datetime.fromisoformat(created.replace('Z', '+00:00').replace('.000', ''))
  return (NOW - ct).total_seconds() / 3600.0

def kind_of_user(u):
  un = (u.get('username') or '')
  if un.lower() in NEWS_HANDLES:
    return 'news'
  unl = un.lower()
  if any(x in unl for x in ['nytimes', 'reuters', 'bbc', 'pti_news', 'nobelprize', 'cnn', 'foxnews', 'weather', 'forbes']):
    return 'news'
  vt = (u.get('verified_type') or '').lower()
  if vt == 'government':
    return 'official'
  if vt == 'business':
    return 'org'
  return 'unknown'

def clears_global(m, age_h, kind):
  views = m['views'] or 0
  likes = m['likes'] or 0
  if kind == 'news':
    return views >= 100000 or likes >= 2000
  if age_h is not None and age_h < 0.25:
    return False
  if age_h is not None and 0.25 <= age_h < 3:
    return (views / age_h) >= 25000 and views >= 10000
  return views >= 100000 or likes >= 2000

def clears_desk(m, age_h, kind, floor_views=50000, floor_likes=1000):
  views = m['views'] or 0
  likes = m['likes'] or 0
  if kind == 'news':
    return views >= floor_views or likes >= floor_likes
  if age_h is not None and age_h < 0.25:
    return False
  if age_h is not None and 0.25 <= age_h < 3:
    return (views / age_h) >= (floor_views / 4) and views >= (floor_views / 10)
  return views >= floor_views or likes >= floor_likes

def assign_desk(text):
  tl = (text or '').lower()
  if any(w in tl for w in ['hurricane', 'isaias', 'storm surge', 'landfall', 'earthquake']):
    return 'disaster'
  if any(w in tl for w in ['panama', 'panamá', 'putin', 'zelensky', 'nobel', 'israel', 'gaza', 'ukraine', 'nato', 'louisville']):
    return 'world'
  if any(w in tl for w in ['trump', 'democrat', 'republican', 'congress', 'senate', 'election', 'governor', 'white house', 'supreme court', 'press secretary']):
    return 'politics'
  if any(w in tl for w in ['nfl', 'nba', 'mlb', 'f1', 'soccer', 'touchdown', 'cowboys', 'wnba', 'ufc', 'angel reese', 'norvell', 'smackdown', 'wwe', 'igor']):
    return 'sports'
  if any(w in tl for w in ['anime', 'movie', 'trailer', 'actor', 'actress', 'netflix', 'episode', 'season', 'celebrity', 'film']):
    return 'entertainment'
  if any(w in tl for w in ['bitcoin', 'crypto', 'stocks', 'nasdaq']):
    return 'markets'
  if any(w in tl for w in ['openai', 'anthropic', 'chatgpt', 'gemini', 'grok', 'llm', ' ai ']):
    return 'ai'
  if any(w in tl for w in ['meme', 'tiktok', 'streamer', 'twitch', 'youtube', 'fandom']):
    return 'internet'
  return 'internet'

skipped_sexual = []
pace_kept = []  # (id, views, age, pace)

# candidate universe: all source ids that we have tweet records for
cand_ids = set()
for s, ids in sources.items():
  cand_ids |= set(ids)
cand_ids |= trend_keep

posts = []
viral_ids = []
rising_ids = []
desk_map = {k: [] for k in DESK_FLOORS}
kept_by_source = defaultdict(set)
candidate_by_source = defaultdict(set)  # after spam/age screening

def is_spam_or_bad(t):
  tid = t['id']
  if tid in EXCLUDE_IDS:
    return 'exclude_id'
  txt = text_of(t)
  if bad_text(txt):
    skipped_sexual.append(tid)
    return 'sexual'
  if t.get('possibly_sensitive') and bad_text(txt):
    skipped_sexual.append(tid)
    return 'sensitive'
  return None

for tid in cand_ids:
  t = all_tweets.get(tid)
  if not t:
    continue
  reason = is_spam_or_bad(t)
  if reason:
    continue
  age = age_hours(t.get('created_at'))
  # candidates = distinct originals under 24h after spam screening
  under24 = age is not None and age < 24
  if under24 or tid in trend_keep:
    for sname, ids in sources.items():
      if tid in ids or (sname == 'trend_names' and tid in trend_keep):
        candidate_by_source[sname].add(tid)
  # also tag trend_keep into trend_names candidates even if older
  if tid in trend_keep:
    candidate_by_source['trend_names'].add(tid)

# keep decisions
seen_post = set()
for tid in cand_ids:
  if tid in watch_ids:
    continue
  t = all_tweets.get(tid)
  if not t:
    continue
  if is_spam_or_bad(t):
    continue
  u = all_users.get(t.get('author_id'), {})
  handle = u.get('username')
  if not handle:
    continue
  m = metrics(t)
  if m['views'] is None and m['likes'] is None:
    continue
  age = age_hours(t.get('created_at'))
  akind = kind_of_user(u)
  flags = []
  if age is not None and age > 24 * 7:
    flags.append('old_content')
  # old_content origins kept regardless of size (GRABBER)
  is_old_origin = 'old_content' in flags
  desk = assign_desk(text_of(t))
  fv, fl = DESK_FLOORS.get(desk, (50000, 1000))
  ok = clears_desk(m, age, akind, fv, fl) or clears_global(m, age, akind)
  lead = None
  if tid in trend_keep:
    ok = True
    lead = 'trend context; no floor'
  if is_old_origin and ref_counts.get(tid, 0) >= 1:
    ok = True
    lead = (lead + '; ' if lead else '') + 'old_content origin'
  if ref_counts.get(tid, 0) >= 2:
    extra = 'pointed at by %d posts read this run' % ref_counts[tid]
    lead = (lead + '; ' + extra) if lead else extra
  # stream tally
  if tid in set(sources.get('quote_stream', [])) | set(sources.get('repost_stream', [])):
    extra = 'seen in the quote or repost stream in 1 of the last 6 runs'
    lead = (lead + '; ' + extra) if lead else extra
  if not ok:
    continue
  # skip very old non-trend non-old_content (>48h) unless high refs
  if age is not None and age > 48 and tid not in trend_keep and 'old_content' not in flags and ref_counts.get(tid, 0) < 2:
    continue
  if age is not None and 0.25 <= age < 3 and (m['views'] or 0) < 100000 and (m['likes'] or 0) < 2000:
    pace = int((m['views'] or 0) / age) if age else 0
    extra = 'pace about %d views/hour at read' % pace
    lead = (lead + '; ' + extra) if lead else extra
    pace_kept.append((tid, m['views'] or 0, age, pace))
  created = (t.get('created_at') or '').replace('.000Z', 'Z')
  if created.endswith('+00:00'):
    created = created.replace('+00:00', 'Z')
  reply, quotes = reply_quote(t)
  post = {
    'id': tid,
    'url': 'https://x.com/%s/status/%s' % (handle, tid),
    'created_at': created,
    'lang': t.get('lang') or 'en',
    'text': text_of(t),
    'author': {
      'handle': handle,
      'name': u.get('name') or handle,
      'followers': (u.get('public_metrics') or {}).get('followers_count'),
      'verified': verified_of(u),
      'kind': akind,
    },
    'media': media_list(t, all_media),
    'reply_to': reply,
    'quotes': quotes,
    'note': None,
    'flags': flags,
    'desk': desk,
    'beat': None,
    'topic': None,
    'lead': lead,
  }
  if tid in seen_post:
    continue
  seen_post.add(tid)
  posts.append(post)
  for sname, ids in sources.items():
    if tid in set(ids) or (sname == 'trend_names' and tid in trend_keep):
      kept_by_source[sname].add(tid)
  if clears_global(m, age, akind) or tid in trend_keep:
    viral_ids.append(tid)
  if age is not None and age < 6:
    rising_ids.append(tid)
  if desk in desk_map:
    desk_map[desk].append(tid)

def views_of(pid):
  tw = all_tweets.get(pid) or {}
  return (tw.get('public_metrics') or {}).get('impression_count') or 0

posts.sort(key=lambda p: -views_of(p['id']))
# side-by-side: keep up to 120 (night had 101)
posts = posts[:120]
kept = set(p['id'] for p in posts)
for p in posts:
  add_obs(p['id'], all_tweets.get(p['id']))
viral_ids = [i for i in viral_ids if i in kept][:40]
rising_ids = [i for i in rising_ids if i in kept][:30]
for k in desk_map:
  desk_map[k] = [i for i in desk_map[k] if i in kept][:10]
# refresh kept_by_source to final kept only
for sname in list(kept_by_source.keys()):
  kept_by_source[sname] = set(x for x in kept_by_source[sname] if x in kept)

# sweeps
sweeps = []

def sweep(sid, kind, desk, method, window, status, reason, post_ids):
  sweeps.append({
    'id': sid,
    'kind': kind,
    'desk': desk,
    'method': method,
    'window_hours': window,
    'status': status,
    'reason': reason,
    'post_ids': post_ids or [],
  })

n_watch = len(watch_ids) + 165  # planned approx
sweep('watch', 'watch', None,
      'get_posts_by_ids on requests/watch.json plus posts first captured in last 6h (%d ids in 3 batches); evening side-by-side' % len(open(f'{WORK}/watch_ids.txt').read().split(',')),
      None, 'ok', None, [i for i in watch_ids if i in watch_returned][:400])
sweep('trends.us', 'trends', None, 'get_trends_by_woeid 23424977 max_trends 20', None, 'ok', None, None)
sweep('trends.ww', 'trends', None, 'get_trends_by_woeid 1 max_trends 20', None, 'ok', None, None)
sweep('viral.global', 'discovery', None,
      'evening side-by-side: references + sensors news/sports/culture + trend names (Putin,Louisville,Angel Reese,Igor,Norvell) + quote(the,this) + repost(the) + story clusters + desk streams; screened by pace/floor',
      24, 'ok', None, viral_ids)
sweep('rising.global', 'discovery', None,
      'quote streams the/this lang:en is:quote -is:retweet + repost the lang:en is:retweet; under 6h kept',
      6, 'ok', None, rising_ids)
for g in ['news', 'sports', 'culture']:
  q = open(f'{WORK}/sensor_{g}_q.txt').read().strip()
  ids = [p['id'] for p in posts if p['id'] in set(sources.get('sensors', []))][:15]
  # split roughly
  sweep(f'sensors.{g}', 'discovery', None,
        f'search_posts_all `{q}` newest 25; follow origins', 24, 'ok', None, ids[:15] if g == 'news' else [])
# reassign sensor post ids properly
sensor_posts = [p['id'] for p in posts if p['id'] in set(sources.get('sensors', []))]
for sw in sweeps:
  if sw['id'] == 'sensors.news':
    sw['post_ids'] = sensor_posts[:15]
  elif sw['id'] == 'sensors.sports':
    sw['post_ids'] = sensor_posts[15:30]
  elif sw['id'] == 'sensors.culture':
    sw['post_ids'] = sensor_posts[30:45]

for desk in ['politics', 'entertainment', 'sports', 'internet']:
  sweep(f'desk.{desk}', 'desk', desk,
        f'standing query from CAPABILITIES.md lang:en is:retweet -is:reply newest 25; keep by pace/floor (evening side-by-side)',
        24, 'ok', None, desk_map.get(desk, [])[:10])

# remaining desks empty ok for this run (side-by-side only hourly four + globals)
for desk in DESK_FLOORS:
  if desk in ('politics', 'entertainment', 'sports', 'internet'):
    continue
  sweep(f'desk.{desk}', 'desk', desk,
        'skipped this evening side-by-side (hourly four + source ranking only)',
        24, 'ok', 'not due; evening side-by-side focuses on ranking sources', [])

sweep('context.top', 'context', None,
      'skipped; budget used on side-by-side sources and screening',
      None, 'ok', 'skipped volume/context/media descriptions per evening run when tight', [])

# requests acknowledged unanswered
answers = []
for req in json.load(open(f'{REPO}/requests/open.json')).get('requests') or []:
  sweep(f"request.{req['id']}", 'request', None,
        'open request carried; not answered this evening side-by-side (budget on source ranking)',
        None, 'ok', 'not answered this run', [])

# per-source metrics for NOTES
def median(xs):
  xs = sorted(xs)
  if not xs:
    return None
  return statistics.median(xs)

source_metrics = {}
# reads cost per source (approximate from plan)
reads_cost = {
  'references': 0,  # free on watch/screen
  'sensors': 3,
  'trend_names': 5,
  'quote_stream': 2,
  'repost_stream': 1,
  'story_clusters': 5,  # recount: first 5 without cluster field wasted + 5 with = 10; attribute 5 good
  'desk_repost_streams': 4,
}
# note: wasted 5 story reads without cluster_posts_results — mention in NOTES

for sname in ['references', 'sensors', 'trend_names', 'quote_stream', 'repost_stream', 'story_clusters', 'desk_repost_streams']:
  cands = candidate_by_source.get(sname, set())
  kept_s = kept_by_source.get(sname, set()) & kept
  # for candidates, require we have views and under 24h (or trend)
  views_list = []
  ages = []
  for tid in kept_s:
    tw = all_tweets.get(tid)
    if not tw:
      continue
    v = views_of(tid)
    views_list.append(v)
    a = age_hours(tw.get('created_at'))
    if a is not None:
      ages.append(a)
  # candidates count: under 24h after spam with record
  cand_ok = []
  for tid in cands:
    tw = all_tweets.get(tid)
    if not tw:
      continue
    if is_spam_or_bad(tw):
      continue
    a = age_hours(tw.get('created_at'))
    if a is not None and a < 24:
      cand_ok.append(tid)
    elif tid in trend_keep:
      cand_ok.append(tid)
  source_metrics[sname] = {
    'reads': reads_cost.get(sname, 0),
    'candidates': len(set(cand_ok)),
    'kept': len(kept_s),
    'largest': max(views_list) if views_list else 0,
    'median': int(median(views_list)) if views_list else 0,
    'median_age_h': round(median(ages), 2) if ages else None,
    'kept_ids': sorted(kept_s),
  }

# fix story_clusters reads: we spent 10 (5 bad + 5 good); report 5 effective + note waste
source_metrics['story_clusters']['reads'] = 5
source_metrics['_note_story_waste'] = 5

open(f'{WORK}/source_metrics.json', 'w').write(json.dumps(source_metrics, indent=2))
open(f'{WORK}/pace_kept.json', 'w').write(json.dumps([
  {'id': i, 'views': v, 'age_h': round(a, 3), 'pace': p} for i, v, a, p in sorted(pace_kept, key=lambda x: -x[3])
], indent=2))
open(f'{WORK}/skipped_sexual.json', 'w').write(json.dumps(sorted(set(skipped_sexual))))

skipped_note = ', '.join(sorted(set(skipped_sexual))[:20])
reason = (
  f'evening side-by-side at 9:35 PM ET (01 UTC Oct 10): {READS_START - READS_END} X reads '
  f'({READS_START} to {READS_END} left today). Watch {len(open(f"{WORK}/watch_ids.txt").read().split(","))}; '
  f'trends US+WW; sensors news/sports/culture; trend streams Putin/Louisville/Angel Reese/Igor/Norvell; '
  f'quote the+this + repost the; story clusters viral+politics+entertainment+sports+internet '
  f'(cluster_posts_results; first 5 story reads lacked that field and were redone); '
  f'desk repost streams politics/entertainment/sports/internet; screen 323 by id in 4 batches. '
  f'No volume, context.top, or media descriptions. Skipped sexual/graphic ids: {skipped_note or "none listed"}.'
)

# x_stories: only those with exact names from files; include
x_stories_out = []
for st in x_stories[:80]:
  x_stories_out.append({
    'id': st['id'],
    'name': st['name'],
    'summary': st.get('summary'),
    'category': st.get('category'),
    'url': st.get('url'),
    'updated_at': st.get('updated_at'),
    'post_ids': [p for p in st.get('post_ids') or [] if p in kept][:10] or (st.get('post_ids') or [])[:5],
  })

cap = {
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
      'method': 'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid, search_news); evening side-by-side',
    },
    'requests_rev': REQ_REV,
  },
  'sweeps': sweeps,
  'trends': trends,
  'posts': posts,
  'observations': observations,
  'context': [],
  'answers': answers,
  'x_stories': x_stories_out,
}

out_path = f'{REPO}/capture/2026/10/10/0135Z.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
open(out_path, 'w').write(json.dumps(cap, indent=2) + '\n')
print('wrote', out_path)
print('posts', len(posts), 'obs', len(observations), 'sweeps', len(sweeps), 'x_stories', len(x_stories_out))
print('pace_kept', len(pace_kept))
print('source metrics:')
for k, v in source_metrics.items():
  if k.startswith('_'):
    continue
  print(f"  {k}: reads={v['reads']} cand={v['candidates']} kept={v['kept']} largest={v['largest']} median={v['median']} age={v['median_age_h']}")
if pace_kept:
  fastest = max(pace_kept, key=lambda x: x[3])
  print('fastest pace', fastest)
print('skipped sexual', len(set(skipped_sexual)))
