#!/usr/bin/env python3
"""Build capture/2026/10/25/0003Z.json from saved X outputs."""
import json, re, os, time
from collections import Counter, defaultdict
from datetime import datetime, timezone

W = '/workspace/monitoring-the-situation/capture/work/2026-10-25T0003Z'
REPO = '/workspace/monitoring-the-situation'
RUN_ID = '2026-10-25T0003Z'
STARTED = '2026-10-25T00:03:00Z'
FINISHED = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
OBS_AT = '2026-10-25T00:04:00Z'
REQUESTS_REV = open(f'{W}/requests_rev.txt').read().strip()
READS_BEFORE = 1000
READS_AFTER = int(open(f'{W}/reads_after.txt').read().strip())
READS_USED = READS_BEFORE - READS_AFTER  # this run's X calls; no 429 refusals
FORCE_REREC = set()
NO_REREC = {'2111143320311243129','2112744960453734800'}  # 0705Z: 2112744960453734800 full text shows a paid post (#ad, paid partnership with @EagleCorp); not re-recorded
SKIP_NEW = set()  # full text now names his children and brother (private family information)
EXTRA_NOTE = open(f'{W}/extra_note.txt').read().strip() if os.path.exists(f'{W}/extra_note.txt') else ''

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
    at_ts = at_ts or datetime(2026,10,25,0,6,tzinfo=timezone.utc).timestamp()  # 0003Z (2300Z used 23:02, 2159Z used 22:01, 2103Z used 21:05, 2007Z used 20:09, 1907Z used 19:08, 1807Z used 18:08, 1700Z used 17:01, 1604Z used 16:06, 1505Z used 15:06, 1404Z used 14:06, 1307Z used 13:09, 1204Z used 12:05, 1105Z used 11:07, 1003Z used 10:04, 0905Z used 09:06, 0804Z used 08:05, 0704Z used 07:06, 0602Z used 06:04, 0507Z used 05:08, 0400Z used 04:02, 0303Z used 03:04, 0200Z used 02:01, 0103Z used 01:05, 0000Z used 00:01, 2305Z used 23:07, 2107Z used 21:11, 2005Z used 20:08, 1905Z used 19:07, 1808Z used 18:10, 1659Z used 17:01, 1602Z used 16:05, 1459Z used 15:02, 1401Z used 14:04, 1303Z used 13:05, 1200Z used 12:03, 1107Z used 11:10, 0959Z used 10:01, 0905Z used 09:07, 0801Z used 08:03, 0707Z used 07:11, 0606Z used 06:09, 0458Z used 05:01, 0403Z used 04:06, 0303Z used 03:05, 0205Z used 02:07, 0059Z used 01:01, 0002Z used 00:05, 2307Z used 23:10, 2201Z used 22:03, 2107Z used 21:10, 2007Z used 20:10, 1902Z used 19:05, 1804Z used 18:07, 1706Z used 17:09, 1612Z used 16:20, 1501Z used 15:06, 1409Z used 14:13, 1307Z used 13:12, 1201Z used 12:04, 1107Z used 11:10, 1007Z used 10:10, 0904Z used 09:07, 0800Z used 08:04, 0706Z used 07:10, 0607Z used 06:10, 0502Z used 05:04, 0408Z used 04:09, 0300Z used 03:01, 0206Z used 02:09, 0103Z used 01:05, 0001Z used 00:04, 2301Z used 23:04, 2203Z used 22:06, 2107Z used 21:10, 2008Z used 20:11, 1900Z used 19:03, 1808Z used 18:12, 1709Z used 17:14, 1604Z used 16:08, 1500Z used 15:03, 1402Z used 14:05, 1302Z used 13:05, 1204Z used 12:06, 1107Z used 11:10, 1007Z used 10:10, 0906Z used 09:10, 0804Z used 08:07, 0705Z used 07:08, 0559Z used 06:02, 0507Z used 05:10, 0403Z used 04:06, 0308Z used 03:12, 0203Z used 02:06, 0059Z used 01:03, 0006Z used 00:09, 2258Z used 23:02, 2207Z used 22:11, 2059Z used 21:02, 2007Z used 20:10, 1905Z used 19:08, 1804Z used 18:07, 1705Z used 17:08, 1600Z used 16:03, 1502Z used 15:06, 1401Z 14:04): the time of this run's reads (1310Z still used 12:02)
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
    ids = att.get('media_source_tweet_id')
    if isinstance(ids, list):
        return ids[0] if ids else None
    if isinstance(ids, str):
        return ids
    return None

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
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',
    'quote_is': 'quote_is.txt', 'quote_you': 'quote_you.txt',
    'repost_and': 'repost_and.txt',
    'trend_tennessee': 'trend_tennessee.txt', 'trend_big12': 'trend_big12.txt', 'trend_lanning': 'trend_lanning.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt',
    'trends_us': 'trends_us.txt',
}
DUE = [d['id'] for d in json.load(open(f'{REPO}/contract/desks.json'))['desks'] if d['id'] in ('politics','entertainment','sports','internet')]
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
    ('quote_is','quote'),('quote_you','quote'),('repost_and','repost'),
    ('trend_tennessee','trend.Tennessee'),('trend_big12','trend.Big 12'),('trend_lanning','trend.Dan Lanning'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),
] + [('desk_'+_d, 'desk.'+_d) for _d in DUE]:
    collect_refs(raw[fname], src)

tally = json.load(open(f'{W}/TALLY.before.json'))
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
    if 'wwtrend.jpquake' in sources or 'wwtrend.jpquake.media' in sources: return 'disaster'
    for _x in sources:
        if str(_x) in ('trend.49ers','trend.#WorldSeries'): return 'sports'  # 0501Z: 49ers (Monday Night Football); Brewers v Rays World Series
        if str(_x) in ('trend.Fred Warner','trend.Rays','trend.Niners','trend.Commanders'): return 'sports'  # 0308Z: 49ers v Commanders MNF (Fred Warner helmet hit, Niners, Commanders); Rays clinch the AL pennant
        if str(_x) in ('trend.Jayden Daniels','trend.Dan Quinn','trend.Mike Evans','trend.Angel Reese','trend.#WWERaw'): return 'sports'  # 0200Z: Commanders at 49ers on Monday Night Football; Mike Evans; Angel Reese; WWE Raw (wrestling beat)
        if str(_x) == 'trend.#EndSARS': return 'world'  # 0906Z: EndSARS anniversary in Nigeria
        if str(_x) == 'trend.Ten Hag': return 'sports'  # 1103Z: Ten Hag (football manager)
        if str(_x) == 'trend.#TINATUESDAY': return 'music'  # 1705Z: Megan Thee Stallion freestyle series
        if str(_x) == 'trend.76ers': return 'sports'  # 1600Z: NBA opening week, 76ers
        if str(_x) in ('trend.LeBron','trend.Brunson'): return 'sports'  # 0203Z: NBA opening week (LeBron; Brunson is the Knicks opener)
        if str(_x) in ('trend.Chet','trend.Wemby','trend.Spurs','trend.Shai'): return 'sports'  # 0308Z: NBA opening week (Thunder and Spurs)
        if str(_x) in ('trend.Mara','trend.Thunder','trend.Sixers'): return 'sports'  # 0403Z: Aday Mara of the Thunder (Thunder and Spurs game); Sixers (76ers at Knicks)
        if str(_x) in ('trend.#ThunderUp','trend.Jared McCain'): return 'sports'  # 0507Z: Thunder fan tag (Thunder and Spurs game); Jared McCain (Thunder)
        if str(_x) == 'trend.#dwts': return 'entertainment'  # 0559Z: Dancing with the Stars
        if str(_x) == 'trend.#VisionQuest': return 'entertainment'  # 0705Z: Marvel VisionQuest series episode
        if str(_x) in ('trend.#BladeRunnerSupportsRacist','trend.#PapergamesIsRacist'): return 'gaming'  # 1204Z: fan campaign against Papergames over alleged racism and harassment in its game community, tagging the Blade Runner rights holders
        if str(_x) == 'trend.We Demand Action': return 'entertainment'  # 1204Z: Myanmar fans' campaign against GMMTV over Burmese dress in Scarlet Heart Thailand
        if str(_x) in ('trend.Hila',): return 'internet'  # 0905Z: Hila Klein (h3h3), one event with Ethan Klein
        if str(_x) == 'trend.GMMTV RESPECT OUR CULTURE': return 'entertainment'  # 0801Z: Myanmar fan campaign about GMMTV
        if str(_x) == 'trend.Ethan Klein': return 'internet'  # 0707Z: h3h3 podcaster
        if str(_x) == 'trend.Dear JT': return 'music'  # 0707Z
        if str(_x) in ('trend.Bears','trend.Patriots','trend.Maye'): return 'sports'  # 0606Z: Patriots at Bears TNF
        if str(_x) in ('trend.Jokic','trend.Shai','trend.Jaylon Johnson'): return 'sports'  # 0458Z: NBA (Nuggets, Thunder) and Patriots at Bears TNF
        if str(_x) in ('trend.Ben Johnson','trend.Caleb','trend.Cairo Santos'): return 'sports'  # 0403Z: Patriots at Bears TNF
        if str(_x) in ('trend.Drake Maye','trend.Sixers'): return 'sports'  # 0303Z: Patriots at Bears TNF; Cavaliers v 76ers
        if str(_x) in ('trend.Jaylon Johnson',): return 'sports'  # 0205Z: Patriots at Bears TNF
        if str(_x) in ('trend.#VERZUZ',): return 'music'  # 0205Z: Verzuz battle
        if str(_x) in ('trend.Josh McDaniels','trend.Swift'): return 'sports'  # 0059Z: Patriots at Bears TNF
        if str(_x) in ('trend.#911onABC',): return 'entertainment'  # 0059Z: ABC 9-1-1 episode
        if str(_x) in ('trend.Cavs',): return 'sports'  # 0002Z: Cavaliers v 76ers
        if str(_x) in ('trend.Vanity Fair',): return 'politics'  # 2307Z: Vanity Fair Kushner excerpt
        if str(_x) in ('trend.Tom Skerritt',): return 'entertainment'  # 2307Z: actor dies at 93
        if str(_x) in ('trend.Marines',): return 'politics'  # 2201Z: Iwo Jima statue at Quantico damaged
        if str(_x) in ('trend.Marnie',): return 'entertainment'  # 2201Z: Halloweentown 5 casting
        if str(_x) in ('trend.Iwo Jima',): return 'politics'  # 2107Z: Iwo Jima statue at Quantico damaged
        if str(_x) in ('trend.Cenk',): return 'politics'  # 2107Z: Cenk Uygur claims about Lindsey Graham
        if str(_x) in ('trend.Tom Skerritt',): return 'entertainment'  # 2007Z: actor Tom Skerritt death
        if str(_x) in ('trend.LeBron James',): return 'sports'  # 2007Z
        if str(_x) in ('trend.AIPAC',): return 'politics'  # 1902Z: AIPAC endorsement change
        if str(_x) in ('trend.Panamá',): return 'disaster'  # 1902Z: Panama earthquake
        if str(_x) in ('trend.#TrumpsCrimesOnYourDime',): return 'politics'  # 1902Z: hashtag campaign
        if str(_x) in ('trend.Josh Simmons',): return 'sports'  # 1804Z: Chiefs LT Josh Simmons to IR
        if str(_x) in ('trend.$MRNA',): return 'markets'  # 1804Z: Moderna stock drop
        if str(_x) in ('trend.Virginia',): return 'politics'  # 1804Z: Louise Lucas indictment
        if str(_x) in ('trend.Bond',): return 'entertainment'  # 1706Z: James Bond casting
        if str(_x) in ('trend.Luka',): return 'sports'  # 1706Z
        if str(_x) in ('trend.Jack Lowden',"trend.Josh O'Connor",'trend.Callum Turner'): return 'entertainment'  # 1612Z: James Bond casting finalists
        if str(_x) in ('trend.Louise Lucas','trend.Lindsey Graham'): return 'politics'  # 1501Z: Virginia state senator arrested; Graham allegations
        if str(_x) in ('trend.#NINGNINGShines24ever',): return 'music'  # 1501Z: aespa Ningning birthday
        if str(_x) in ('trend.RIP Ron','trend.WNBA'): return 'sports'  # 1409Z: Ron Duguay (Rangers) death; WNBA Finals
        if str(_x) in ('trend.Happy Birthday Doc',): return 'entertainment'  # 1307Z: Christopher Lloyd (Doc Brown) birthday
        if str(_x) in ('trend.#PapergamesTramplesHumanRights','trend.#中国上海停止纵容姚润昊'): return 'gaming'  # 1201Z: fan campaign against Papergames (Love and Deepspace) over harassment
        if str(_x) in ('trend.Eala','trend.Luka'): return 'sports'  # 1107Z: Alex Eala at the Ningbo Open; Warriors at Lakers
        if str(_x) in ('trend.Kidnapped',): return 'politics'  # 1107Z: mostly the ICE-kidnapping claim and murder charge
        if str(_x) in ('trend.Warriors',): return 'sports'  # 1007Z: Warriors at Lakers (NBA opening week)
        if str(_x) in ('trend.#RespectMyanmarCulture',): return 'entertainment'  # 1007Z: Myanmar fan clubs and GMMTV
        if str(_x) in ('trend.Bellucci',): return 'internet'  # 1007Z: Monica Bellucci and Tim Burton meme
        if str(_x) in ('trend.Walker Kessler','trend.Ty Jerome','trend.Lakers'): return 'sports'  # 0904Z: Warriors at Lakers (NBA opening week)
        if str(_x) in ('trend.#CreditOurHeritage','trend.GMMTV ACCOUNTABILITY'): return 'entertainment'  # 0800Z: Myanmar fan clubs asking GMMTV (Scarlet Heart TH) to credit Myanmar costumes
        if str(_x) in ('trend.Luka',): return 'sports'  # 0800Z
        if str(_x) in ('trend.Warriors','trend.Draymond','trend.#LakeShow'): return 'sports'  # 0706Z: Warriors at Lakers (NBA opening week)
        if str(_x) in ('trend.Lakers','trend.Blazers','trend.Suns'): return 'sports'  # 0607Z: NBA opening week (Warriors at Lakers; Blazers; Suns)
        if str(_x) in ('trend.Steph','trend.Ty Jerome','trend.Giannis'): return 'sports'  # 0502Z: NBA opening week (Warriors at Lakers; Ty Jerome; Giannis/Bucks)
        if str(_x) in ('trend.Luka','trend.Yaxel','trend.Kessler'): return 'sports'  # 0408Z: Warriors at Lakers (NBA opening week)
        if str(_x) in ('trend.Blazers','trend.Suns','trend.Angel Reese'): return 'sports'  # 0300Z: Suns at Trail Blazers (NBA opening week); Angel Reese WNBA Finals
        if str(_x) in ('trend.Anthony Edwards','trend.Mavs'): return 'sports'  # 0206Z: NBA opening week (Timberwolves v Heat; Mavericks at Rockets)
        if str(_x) == 'trend.Kilby': return 'entertainment'  # 0206Z: Survivor 51 contestant
        if str(_x) in ('trend.#AEWDynamite','trend.Ty Jerome'): return 'sports'  # 0103Z: AEW Dynamite (wrestling beat); Ty Jerome NBA opening week
        if str(_x) == 'trend.#Survivor51': return 'entertainment'  # 0103Z: CBS Survivor season 51
        if str(_x) in ('trend.Giannis','trend.Lamelo','trend.Anthony Davis'): return 'sports'  # 0001Z: NBA opening-week games
        if str(_x) == 'trend.Haiti': return 'world'  # 2301Z: Bukele military operation in Haiti
        if str(_x) == 'trend.Ilhan Nur': return 'politics'  # 2301Z: DOJ warrant filing names Ilhan Omar as Ilhan Nur Said Elmi
        if str(_x) == 'trend.Kenan': return 'entertainment'  # 2203Z: Kenan Thompson on the Shane Gillis SNL monologue
        if str(_x) == 'trend.Claude Duet': return 'ai'  # 2203Z: Anthropic Claude Duet research preview
        if str(_x) == 'trend.Diomande': return 'sports'  # 2107Z: Yan Diomande goal and assist for Real Madrid
        if str(_x) == 'trend.Harry Kane': return 'sports'  # 2008Z: football match (FabrizioRomano Kane assist post)
        if str(_x) == 'trend.Glee': return 'entertainment'  # 1900Z: Glee reboot series order at Disney+ and Hulu
        if str(_x) == 'trend.BioWare': return 'gaming'  # 1808Z: BioWare games studio (Mass Effect, Dragon Age, Anthem, KOTOR trend with it)
        if str(_x) == 'trend.Carrick': return 'sports'  # 1808Z: Manchester United (Man U, Manchester United trend with it)
        if str(_x) == 'trend.Nico Paz': return 'sports'  # 1709Z: Como footballer, Champions League goal against Manchester United
        if str(_x) == 'trend.Mike Locksley': return 'sports'  # 1604Z: college football coach
        if str(_x) == 'trend.Cashman': return 'sports'  # 1604Z: Yankees general manager Brian Cashman
        if str(_x) == 'trend.Glee': return 'entertainment'  # 1500Z: the TV show Glee
        if str(_x) == 'trend.GMMTV': return 'entertainment'  # 1500Z: Thai TV studio GMMTV; mostly the #RespectMyanmarCulture campaign about Scarlet Heart Thailand
        if str(_x) == 'trend.Abolish': return 'politics'  # 1402Z: mostly reposts of an 'Abolish ICE.' post, with other 'Abolish ...' slogans
        if str(_x) == 'trend.Witkoff': return 'world'  # 1302Z: Witkoff meets Putin in St Petersburg; one event with the Stephen Hubbard release
        if str(_x) == 'trend.Stephen Hubbard': return 'world'  # 1107Z: Russia frees US citizen Stephen Hubbard (Steve Witkoff escorting him home)
        if str(_x) == 'trend.#LNGSHOT_SWISH': return 'music'  # 1107Z: LNGSHOT Masterpiece music video release
        if str(_x) in ('trend.#RespectMyanmar','trend.#HelluvaBossSpoilers'): return 'entertainment'  # 1007Z: fan campaign over Burmese dress in Scarlet Heart Thailand; Helluva Boss season 3 spoilers
        if str(_x) == 'trend.Wemby': return 'sports'  # 1007Z: Thunder and Spurs NBA game
        if str(_x) in ('trend.Vassago','trend.#MyanmarCulture','trend.#TheDropFX'): return 'entertainment'  # 0906Z: Helluva Boss season 3 episode (Vassago); fan campaign over Burmese dress in the GMMTV series Scarlet Heart Thailand; the FX series The Drop
        if str(_x) == 'trend.#中国叠纸践踏人权': return 'gaming'  # 1600Z: one event with the Blade Runner tags (Love and Deepspace / Papergames fan campaign)
        if str(_x) == 'trend.Vivek': return 'politics'  # 1502Z: Vivek Ramaswamy, Ohio governor race
        if str(_x) == 'trend.Celtics': return 'sports'  # 1502Z: NBA opening week
        if str(_x) == 'trend.Jay Z': return 'music'  # 1502Z: Jay-Z Super Bowl halftime report
        if str(_x) in ('trend.Embiid','trend.Drummond'): return 'sports'  # 0006Z: 76ers NBA opener (Embiid, Drummond)
        if str(_x) == 'trend.EAGLE-4': return 'ai'  # 0006Z: EAGLE-4 speculative-decoding release (LLM inference speed)
        if str(_x) in ('trend.#dwts','trend.Ezra','trend.Tatyana','trend.Amber','trend.Maura'): return 'entertainment'  # 0059Z: Dancing with the Stars episode (Ezra Frech, Tatyana, Amber, Maura are contestants)
        if str(_x) == 'trend.Knicks': return 'sports'  # 1401Z: NBA opening day, 76ers at Knicks
        if str(_x) == 'trend.Bullhorn': return 'politics'  # 1401Z: argument over a protester's bullhorn and a punch
        if str(_x) == 'trend.Jay-Z': return 'music'  # 1310Z: Puck report that Jay-Z picked himself for the 2027 Super Bowl halftime show
        if str(_x) == 'trend.#throwtheballup': return 'sports'  # 1310Z: Philadelphia 76ers hashtag on NBA opening day
        if str(_x) in ('trend.Planet Fitness','trend.Amy Acton'): return 'politics'  # 1200Z: Wisconsin Planet Fitness ICE-jacket video; Ohio governor race (Amy Acton's mother ad)
        if str(_x) == 'trend.#BladeRunnerStandsWithBullies': return 'gaming'  # 1200Z: Love and Deepspace (Papergames) fan campaign against the Blade Runner 2049 collab
        if str(_x) == 'trend.#CyberpunkEdgerunners2': return 'entertainment'  # 0906Z: Cyberpunk Edgerunners 2 anime
        if str(_x) in ('trend.Monday Night Football','trend.Kittle'): return 'sports'  # 0004Z: Commanders at 49ers on Monday Night Football
        if str(_x) in ('trend.Ted Nugent',): return 'politics'  # 0004Z: Ted Nugent speaking at the Trump rally in Kansas
        if str(_x) in ('trend.Shawn',): return 'internet'  # 0004Z: mostly the Shawn Ryan Show podcast dispute
        if str(_x) in ('trend.Knecht',): return 'sports'  # 2300Z: Lakers waive Dalton Knecht, one event with Bronny
        if str(_x) in ('trend.Davante Adams','trend.Brandon Miller'): return 'sports'  # 2209Z: Davante Adams hamstring injury; Brandon Miller Hornets extension
        if str(_x) in ('trend.New Mexico',): return 'politics'  # 2100Z: the New America renaming call
        if str(_x) in ('trend.Bronny','trend.Dalton Knecht','trend.#COYS'): return 'sports'  # 2100Z: Lakers waive Dalton Knecht; Tottenham win
        if str(_x) in ('trend.New America',): return 'politics'  # 2000Z: Trump calls for New Mexico to be renamed New America
        if str(_x) in ('trend.Howie','trend.Maddison'): return 'sports'  # 2000Z: Howie Roseman and the Eagles Jalen Hurts presser; James Maddison goal for Tottenham
        if str(_x) in ('trend.Bungie',): return 'gaming'  # 2000Z: Star Wars Battlefront 3 developer rumour
        if str(_x) in ('trend.Eagles',): return 'sports'  # 1909Z: Eagles QB Jalen Hurts out for the season
        if str(_x) in ('trend.Kim Jong Un',): return 'world'  # 1909Z
        if str(_x) in ('trend.Zuffa','trend.Buckner'): return 'sports'  # 1803Z
        if str(_x) in ('trend.Tiny Desk',): return 'music'  # 1803Z: NPR Tiny Desk concerts
        if str(_x) in ('trend.Leslie',): return 'politics'  # 1710Z: the stream is mostly posts naming Leslie Stahl of 60 Minutes on non-citizen voting
        if str(_x) in ('trend.Michael Robinson','trend.#HardRockBet'): return 'sports'  # 1620Z: NFL Network analyst on Jalen Hurts; sportsbook promo hashtag
        if str(_x) in ('trend.Jalen','trend.Chris Bosh','trend.Dwight Powell'): return 'sports'  # 1519Z
        if str(_x) in ('trend.Chris Ballard','trend.Carlie','trend.#IDontWantToOverreactBUT','trend.Colts'): return 'sports'  # 1410Z: Colts fire GM Chris Ballard (Carlie Irsay-Gordon statement); McAfee show hashtag
        if str(_x) in ('trend.#PapergamesIsCyberMurderer',): return 'gaming'  # 1410Z: Love and Deepspace (Papergames) fan campaign
        if str(_x) in ('trend.#MondayMotivation',): return 'life'  # 1410Z
        if str(_x) in ('trend.Victory Monday',): return 'sports'  # 1302Z: NFL teams' Victory Monday posts
        if str(_x) in ('trend.Reparations',): return 'politics'  # 1302Z
        if str(_x) in ('trend.JPM Coin',): return 'business'  # 1302Z: JPMorgan deposit token (a company's story; crypto retired)
        if str(_x) in ('trend.jeonghan',): return 'music'  # 1000Z: SEVENTEEN member Jeonghan
        if str(_x) in ('trend.Jerry',): return 'sports'  # 0603Z: Jerry Jones, Cowboys v Packers
        if str(_x) in ('trend.#LaGranjaGala',): return 'entertainment'  # 0509Z: La Granja VIP reality show gala
        if str(_x) in ('trend.Pickens','trend.Jerry Jones'): return 'sports'  # 0404Z: Cowboys v Packers
        if str(_x) in ('trend.Rams',): return 'sports'  # 0304Z: Rams (NFL)
        if str(_x) in ('trend.Cowboys','trend.Packers','trend.Green Bay','trend.#DALvsGB','trend.Dak Prescott','trend.Schotty'): return 'sports'  # 0200Z: Cowboys v Packers SNF
        if str(_x) in ('trend.Jordan Love','trend.Dee Winters','trend.Matthew Golden','trend.#DallasCowboys','trend.#GoPackGo','trend.Ben Simmons'): return 'sports'  # 0106Z: Cowboys v Packers SNF; Ben Simmons Achilles
        if str(_x) in ('trend.Kylie','trend.Megan'): return 'life'  # 0106Z: Kylie Jenner and Megan Thee Stallion at the Victoria's Secret Fashion Show (fashion is life)
        if str(_x) in ('trend.Raiders','trend.McVay','trend.Herbert','trend.#RaiderNation','trend.Harbaugh','trend.Tre Tucker','trend.Aaron Donald','trend.Tate'): return 'sports'  # 0006Z
        if str(_x) in ('trend.#VSFashionShow','trend.#VictoriasSecretFashionShow','trend.#VSFS2026'): return 'life'  # 0006Z: Victoria's Secret Fashion Show (fashion is life)
        if str(_x) in ('trend.World Series','trend.David Hamilton','trend.Dodgers','trend.Brewers','trend.Bo Nix'): return 'sports'
        if str(_x) in ('trend.Seahawks','trend.Sam Darnold','trend.Shaheed'): return 'sports'
        if str(_x) in ('trend.Tesla Roadster','trend.Tesla'): return 'tech'
        if str(_x)=='trend.#OlandriaxWWW20': return 'life'
        if str(_x) in ('trend.RED Friday','trend.Good Friday'): return 'life'
        if str(_x)=='trend.James Dolan': return 'sports'  # 1107Z: Knicks owner
        if str(_x) in ('trend.#AlconMustEndPPGcollab','trend.#BladeRunnerCollabswithRacist','trend.#GenshinSpecialProgram'): return 'gaming'  # 1200Z: Love and Deepspace (Papergames) fan campaign; Genshin Impact 7.2 Special Program
        if str(_x) in ('trend.#LastFourWatched','trend.#LetterboxdFriday'): return 'entertainment'
        if str(_x)=='trend.Oregon': return 'justice'  # 1004Z: the stream's top posts are the Bend, Oregon school shooting
        if str(_x)=='trend.Good Sunday': return 'life'  # 1004Z
        if str(_x) in ('trend.OH MY BEST DAY WITH FOURTH','trend.#FourthConcertD3'): return 'entertainment'  # 1101Z
        if str(_x)=='trend.Tommy': return 'politics'  # 1200Z: the stream is mostly the Abdul El-Sayed 'This is Tommy' clip
        if str(_x)=='trend.#sundayvibes': return 'life'  # 1200Z
        if str(_x)=='trend.Slotkin': return 'politics'  # 1303Z
        if str(_x)=='trend.Blessed Sunday': return 'life'  # 1303Z
        if str(_x) in ('trend.#YaoRunhaoRuinsPapergames','trend.#BladeRunnerStandsWithAbuser','trend.#全球请辞中国叠纸姚润昊'): return 'gaming'  # 1406Z: Love and Deepspace (Papergames) fan campaign against the Blade Runner 2049 collab
        if str(_x) in ('trend.Brighton','trend.Nico Collins','trend.Najee','trend.#HTownMade'): return 'sports'  # 1406Z
        if str(_x) in ('trend.Carrick',): return 'sports'  # 1600Z
        if str(_x) in ('trend.Caleb Williams','trend.Boswell','trend.Mike Hughes','trend.Colston Loveland','trend.Kyler Gordon','trend.Cairo Santos','trend.#Steelers','trend.Frank Reich','trend.Braelon Allen','trend.Nolan Smith','trend.AJ Brown'): return 'sports'  # 1807Z
        if str(_x) in ('trend.Goku','trend.#DEATHBATTLE'): return 'entertainment'  # 1807Z
        if str(_x) in ('trend.AJ Brown','trend.Steelers','trend.Cam Ward','trend.Daniel Jones','trend.Panthers','trend.Mike McCarthy','trend.Travis Hunter','trend.#Jets','trend.#DaBears','trend.Aaron Glenn','trend.Charlie Jones','trend.Deshaun Watson'): return 'sports'  # 1904Z
        if str(_x) in ('trend.Browns','trend.Falcons','trend.Colts','trend.Titans','trend.Jets','trend.Saints','trend.JJ McCarthy','trend.Kyler Gordon','trend.Jameis','trend.Huntley','trend.#DawgPound','trend.Aaron Rodgers'): return 'sports'  # 2005Z
        if str(_x) in ('trend.Steelers','trend.Browns','trend.Colts','trend.JJ McCarthy','trend.Giants','trend.Titans','trend.Falcons','trend.Kyler Gordon','trend.Saints','trend.AJ Brown','trend.Jameis','trend.#HereWeGo','trend.Bucs','trend.Jets','trend.Daniel Jones','trend.Panthers','trend.Huntley','trend.Jalen Ramsey','trend.Ballard','trend.#TitanUp'): return 'sports'  # 2102Z
        if str(_x) in ('trend.Bears','trend.Steelers','trend.Colts','trend.Titans','trend.Saints','trend.Browns','trend.CJ Gardner Johnson','trend.CJGJ','trend.Harbaugh','trend.Kenneth Walker','trend.#DaBears','trend.#Saints','trend.#ForTheShoe'): return 'sports'  # 2203Z
        if str(_x) in ('trend.Rams','trend.Cardinals','trend.Chargers','trend.Ben Simmons','trend.Chiefs','trend.McVay','trend.Justin Herbert','trend.#BillsMafia','trend.Bowers','trend.Kirk Cousins','trend.Butker','trend.Herbert'): return 'sports'  # 2306Z
        if str(_x) in ('trend.Cam Little','trend.Jaguars','trend.Go Birds','trend.Texans','trend.Jags','trend.#HOUvsJAX','trend.#DUUUVAL','trend.Liam Coen','trend.Fairbairn'): return 'sports'  # 1709Z
        if str(_x) in ('trend.Jaylin Noel','trend.Tuten','trend.Trevor Lawrence','trend.Reed Blankenship','trend.Parker Washington','trend.CJ Stroud','trend.#Texans','trend.Travis Hunter'): return 'sports'  # 1501Z: Texans v Jaguars
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
        if str(_x)=='trend.iPhone Duo': return 'tech'
        if str(_x)=='trend.Joe Milton': return 'sports'
        if str(_x) in ('trend.Scaramucci','trend.Katie Zacharia','trend.Press Secretary','trend.Scott Jennings','trend.Hannity','trend.Mooch'): return 'politics'
        if str(_x)=='trend.Happy Friyay': return 'life'
        if str(_x)=='trend.Oleshky': return 'world'  # 1401Z: White House says Melania Trump secured a localized Russia-Ukraine ceasefire in Oleshky
        if str(_x)=='trend.#FridayVibes': return 'life'  # 1401Z
        if str(_x)=='trend.Fat Albert': return 'internet'  # 1401Z
        if str(_x)=='trend.Ethan Klein': return 'internet'  # 1459Z
        if str(_x)=='trend.#LetterboxdFriday': return 'entertainment'  # 1459Z
        if str(_x) in ('trend.Hellebuyck','trend.Chad Patrick'): return 'sports'  # 1602Z
        if str(_x) in ('trend.Mercer','trend.Lassie','trend.Jarmo'): return 'sports'  # 1659Z
        if str(_x) in ('trend.Skye','trend.Jesse Legree'): return 'sports'  # 2005Z: Skye Blakely world all-around title; Oregon State WR Jesse Legree re-signs
        if str(_x) in ('trend.Bulls','trend.Norman Powell','trend.Cleetus'): return 'sports'  # 2107Z: Bucks at Bulls; Talladega truck race crash
        if str(_x) in ('trend.#ValkoIsInnocent',): return 'gaming'  # 2107Z: Love and Deepspace character Valko
        if str(_x) in ('trend.Caleb Wilson','trend.Tyler Herro','trend.Sammy Smith'): return 'sports'  # 2305Z: Bulls beat Bucks; Talladega truck race
        if str(_x) in ('trend.Byron',): return 'politics'  # 2305Z: Byron Donalds at the Fort Myers rally
        if str(_x) in ('trend.Luka Garza','trend.Mason Williams','trend.Bulls'): return 'sports'  # 0000Z: NBA (Luka Garza; Mason Williams; Bulls v Bucks)
        if str(_x) in ('trend.#SmackDown','trend.Pacers','trend.Yelich'): return 'sports'  # 0103Z: WWE SmackDown; Pacers game; Yelich (World Series)
        if str(_x) in ('trend.BANGTAN',): return 'entertainment'  # 0103Z: BTS
        if str(_x) in ('trend.Tatum','trend.Mikal'): return 'sports'  # 0200Z: Celtics game (Jayson Tatum); Knicks game (Mikal Bridges)
        if str(_x) in ('trend.#TheLastDriveIn',): return 'entertainment'  # 0200Z: Joe Bob Briggs horror show
        if str(_x) in ('trend.Brook Lopez','trend.Contreras','trend.Paul Reed'): return 'sports'  # 0303Z: NBA and MLB games
        if str(_x) in ('trend.Megill','trend.#WinOurWay','trend.DeLuca'): return 'sports'  # 0400Z: World Series Game 1 (Brewers v Rays)
        if str(_x) in ('trend.Thompson','trend.Wemby','trend.Sengun','trend.Warriors'): return 'sports'  # 0507Z: Rockets v Spurs and Grizzlies v Warriors
        if str(_x)=='trend.#TheLastDriveIn': return 'entertainment'  # 0507Z: Shudder horror show
        if str(_x) in ('trend.Spurs','trend.Grizzlies'): return 'sports'  # 0602Z: Rockets v Spurs and Grizzlies v Warriors
        if str(_x)=='trend.#CulturalCreditMatters': return 'entertainment'  # 0602Z: Myanmar fan campaign about Scarlet Heart Thailand
        if str(_x)=='trend.#AlconMustStopPPGCollab': return 'gaming'  # 1204Z: Love and Deepspace (Papergames) fan campaign against the Blade Runner collab
        if str(_x)=='trend.Guehi': return 'sports'  # 1204Z: Aston Villa v Manchester City
        if str(_x)=='trend.#YouManiacSeriesEP9': return 'entertainment'  # 1204Z: GMMTV series episode hashtag
        if str(_x)=='trend.Donnarumma': return 'sports'  # 1307Z: Aston Villa v Manchester City
        if str(_x)=='trend.#NIKKE4thAnniversary': return 'gaming'  # 1307Z: NIKKE game anniversary countdown
        if str(_x)=='trend.StubHub': return 'sports'  # 1404Z: Brewers World Series ticket complaints
        if str(_x)=='trend.Maresca': return 'sports'  # 1404Z: Aston Villa v Manchester City
        if str(_x)=='trend.#UFC333': return 'sports'  # 1505Z: UFC 333 fight night
        if str(_x)=='trend.#20YearsOfTaylorSwift': return 'music'  # 1505Z: Taylor Swift debut album anniversary
        if str(_x)=='trend.#MrFanboyEP9': return 'entertainment'  # 1505Z: Mr Fanboy series episode 9
        if str(_x)=='trend.Malkoun': return 'sports'  # 1604Z: UFC 333 bout
        if str(_x)=='trend.#EternalDiamondLeeKnow': return 'music'  # 1604Z: Stray Kids Lee Know birthday
        if str(_x)=='trend.Sam Leavitt': return 'sports'  # 1700Z: LSU v Auburn
        if str(_x)=='trend.Mallory': return 'sports'  # 1700Z: Miami running back Javian Mallory
        if str(_x)=='trend.Thicknesse': return 'sports'  # 1700Z: UFC 333 bout
        if str(_x)=='trend.Michigan': return 'politics'  # 1807Z: Michigan sheriff party switch
        if str(_x)=='trend.Malachi Toney': return 'sports'  # 1807Z: Miami v Pitt
        if str(_x)=='trend.Texas Tech': return 'sports'  # 1807Z: Cincinnati v Texas Tech
        if str(_x) in ('trend.Josh Hoover','trend.Chelsea','trend.Volkov'): return 'sports'  # 1907Z: Indiana v Michigan, Tottenham v Chelsea, UFC 333
        if str(_x) in ('trend.Marcel Reed','trend.Dijon Lee','trend.Kavanagh'): return 'sports'  # 2007Z: Alabama v Texas A&M, UFC 333
        if str(_x) in ('trend.Merab','trend.Petr Yan','trend.Indiana'): return 'sports'  # 2103Z: UFC 333 main event, Indiana v Michigan
        if str(_x) in ('trend.Volk','trend.Beck'): return 'sports'  # 2159Z: UFC 333 (Volkanovski), Michigan quarterback Jason Beck in Indiana v Michigan
        if str(_x) in ('trend.Iowa','trend.Scott Frost'): return 'sports'  # 2300Z: Minnesota v Iowa, UCF v BYU
        if str(_x)=='trend.Cheesecake Factory': return 'politics'  # 2300Z: Obama remark on Trump's White House
        if str(_x) in ('trend.Tennessee','trend.Big 12','trend.Dan Lanning'): return 'sports'  # 0003Z: South Carolina v Tennessee, UCF v BYU and the Big 12, Oregon after losing to Illinois
        if str(_x)=='trend.#MCRLA2': return 'music'  # 0704Z: My Chemical Romance Los Angeles show
        if str(_x)=='trend.Dan Sullivan': return 'politics'  # 1808Z: DOJ suit over the Alaska Senate race
        if str(_x) in ('trend.Mozzy','trend.Spitta'): return 'music'
        if str(_x)=='trend.Porsche': return 'tech'
        if str(_x) in ('trend.#The24thBloomOfPor','trend.POR 24TH BIRTHDAY'): return 'entertainment'
        if str(_x)=='trend.#FursuitFriday': return 'internet'
        if str(_x)=='trend.Kaylub Giamanco': return 'justice'
        if str(_x) in ('trend.#NorteFire','trend.San Clemente'): return 'disaster'
        if str(_x)=='trend.Violet': return 'gaming'
        if str(_x)=='trend.Albion': return 'gaming'
        if str(_x)=='trend.Josh Jacobs': return 'sports'
        if str(_x) in ('trend.#SmackDown','trend.Nikki Bella','trend.Purdue'): return 'sports'
        if str(_x)=='trend.#OPLive': return 'entertainment'
        if str(_x) in ('trend.Memphis','trend.Marcus Stokes','trend.Sixers','trend.Baron Corbin'): return 'sports'
        if str(_x)=='trend.Heartbeat': return 'music'
        if str(_x) in ('trend.ash trevino','trend.Adin Ross'): return 'internet'
        if str(_x) in ('trend.#Dateline','trend.Johnny Carson'): return 'entertainment'
        if str(_x) in ('trend.#PFLChicago','trend.Mamu','trend.Kessler'): return 'sports'
        if str(_x)=='trend.YK Osiris': return 'internet'
        if str(_x) in ('trend.PERTHSANTA LOST IN LOVE','trend.#PerthSantaFMinMacau'): return 'entertainment'
        if str(_x)=='trend.Kimmel': return 'entertainment'
        if str(_x)=='trend.Good Saturday': return 'life'
        if str(_x) in ('trend.JAMES THE ULTIMATE PHENOMENON','trend.IDEA BANK','trend.#CORTIS_NOLFest2026','trend.CHAOWESOME','trend.#JAMESUnparalleled'): return 'music'
        if str(_x)=='trend.Everton': return 'sports'
        if str(_x) in ('trend.Isak','trend.Munoz','trend.Barcola','trend.#BRELIV'): return 'sports'
        if str(_x) in ('trend.Julian Sayin','trend.Hoover','trend.Ohio State','trend.#GoBucks','trend.#iufb','trend.Lamine','trend.Ryan Niblett'): return 'sports'
        if str(_x) in ('trend.Brentford','trend.Gameday'): return 'sports'
        if str(_x)=='trend.No Kings': return 'politics'
        if str(_x) in ('trend.Ryan Day','trend.Arthur Smith','trend.Betis','trend.Gators','trend.Indiana'): return 'sports'
        if str(_x) in ('trend.Jeremiah Smith','trend.Sayin','trend.Arch Manning','trend.Sark','trend.Jay Timmons','trend.Indiana','trend.Nick Marsh','trend.Texas','trend.Fahey','trend.Charlie Becker','trend.Nick Marsh','trend.Gus Johnson'): return 'sports'
        if str(_x) in ('trend.Macron','trend.Paris','trend.The French'): return 'world'
        if str(_x) in ('trend.Arch','trend.Marsh'): return 'sports'
        if str(_x) in ('trend.Notre Dame','trend.CJ Carr','trend.Provo','trend.Kentucky','trend.#AEWWrestleDream','trend.BYU','trend.Mateer'): return 'sports'
        if str(_x) in ('trend.Miami','trend.Florida State','trend.Stein','trend.Utah','trend.Clockwork Carnage'): return 'sports'  # 0506Z
        if str(_x) in ('trend.Brock Thomas','trend.Dan Lanning','trend.Raiola','trend.Isaac Wilson'): return 'sports'  # 0600Z
        if str(_x) in ('trend.Nebraska','trend.#GoDucks','trend.Rhule','trend.#Huskers','trend.Colorado','trend.Utes'): return 'sports'  # 0707Z
        if str(_x) in ('trend.Auburn','trend.Gunner','trend.Bryce Underwood','trend.Tommy Carr','trend.Michigan','trend.Rhyne','trend.#WNBAfinals','trend.Gabby Williams','trend.Georgia','trend.Tennessee','trend.Rocco Becht','trend.WAR DAMN EAGLE','trend.War Eagle','trend.Grubb','trend.DeBoer','trend.#AEWWrestleDream','trend.#UFCEdmonton','trend.War Damn Eagle','trend.Go Vols','trend.Kromah','trend.Notre Dame'): return 'sports'
        if str(_x) in ('trend.#MrFanboyEP8','trend.MR FANBOY CHAPTER 8'): return 'entertainment'
        if str(_x)=='trend.GAME DAY': return 'sports'
        if str(_x) in ('trend.#Caturday','trend.Caturday'): return 'offbeat'
        if str(_x) in ('trend.#EVECHE','trend.Emi Martinez','trend.Pedro Neto','trend.Caicedo','trend.Hato','trend.Paul Tierney'): return 'sports'
        if str(_x)=='trend.KEEP GOING AMAZING FOURTH': return 'entertainment'
        if str(_x) in ('trend.KEONHO CAPTIVATES THE LENS', 'trend.NOL Festival', 'trend.IKEONIC', 'trend.ACEKEON MAKNAE', 'trend.5TH GEN IT BOY', 'trend.HOGAN EFFECT'): return 'music'
        if str(_x) in ('trend.#LingOrmBetweenUsConcertD1','trend.THE WORLD BETWEEN LINGORM D1','trend.#LingOrmBetweenUsConcertD2','trend.THE WORLD BETWEEN LINGORM D2'): return 'entertainment'
    _tmap = {'trend.#PFLChicago':'sports','trend.Mamu':'sports','trend.Kessler':'sports','trend.YK Osiris':'internet','trend.ash trevino':'internet','trend.Adin Ross':'internet','trend.#Dateline':'entertainment','trend.Johnny Carson':'entertainment','trend.Memphis':'sports','trend.Marcus Stokes':'sports','trend.Tulane':'sports','trend.Sixers':'sports','trend.Baron Corbin':'sports','trend.Heartbeat':'music','trend.#SmackDown':'sports','trend.Nikki Bella':'sports','trend.#OPLive':'entertainment','trend.Purdue':'sports','trend.Scott Jennings':'politics','trend.Neera':'politics','trend.Josh Jacobs':'sports','trend.Red Rising':'entertainment',"trend.Ruth's Chris":'life','trend.Roger Waters':'music','trend.McAfee':'sports','trend.Bend, Oregon':'justice','trend.Silver Rail Elementary School':'justice','trend.Reeves':'entertainment','trend.Soderbergh':'entertainment','trend.Carl Thomas':'music','trend.Meek':'sports','trend.#LightningStrikes':'sports','trend.Europeans':'world'}
    _trs = [x for x in sources if str(x).startswith('trend.')]
    sports_kw = ['nfl','nba','mlb','nhl','ufc','soccer','touchdown','playoffs','football','basketball','goal','roma','real madrid','mbappe','enzo','champions league','aikman','vini','endrick','mourinho','donnarumma','aew','dynamite','wrestl','yankees','kevin long','espi','soccer','fc ','dodgers','brewers','nlcs','alcs','snell','chourio','home run','baseball','uribe','gasser','joe davis','edman','pat murphy']
    polit_kw = ['press secretary','zacharia','trump','biden','congress','senate','white house','election','governor','democrat','republican']
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
skip_nsfw |= {'2110098465485365422','2029621707548332377','2111137684106207238','2111049763944845621','2110641860418871433','2038868284150308952','1758175200640663829','1758264759776891200','2110729506403082544','2110560665605738660','2110448198615761177','2108746705524903987','2110968888200470933','2110587535604719649','2102731792323416389'}
skip_nsfw |= {'2088878824234848762','2091622627236516180','2010384005770953199','2111143271921766844'}
skip_nsfw |= {'2109340767135084750','2110755325989319001','2111094939043979370','2110494037023367580','2110351915217232063'}
skip_nsfw |= {'2111037603357266409','2110959637415809373'}
skip_nsfw |= {'2096936668901376022','2110588618813083839','2110920477694959812','2110925619240546771','2111084128095687120','2111143963134685204','2110704673640595917','2110827940913033488','2111223736066331035','2111199376274346419'}  # 2303Z (2111199376274346419: on-screen caption gives the street address range of a home): likely paid Sugar Daddy promos; likely paid swim-photo/rug-video pair; engagement bait; sexual text with slurs; two posts whose media was not returned; KTLA photo caption names a resident  # 2110959637415809373: media not returned, could not be screened; finger-gun-to-head image with splatter (self-harm imagery)
skip_nsfw |= {'2110732430277525730','2109630335130771706','2100706266477731875','2111042643891253729'}  # 0003Z: adult-performer promo account (sexual); likely paid MV promo (522 followers, 4.8M views, 652 likes, 0 replies)
skip_nsfw |= {'2110810041813270557','2110942612391657587','2110738716612231271','2110466393577779339','2110397503375868200','2110211240433971350','2110957251242406369','2111004272435589175'}  # 0105Z (2111004272435589175: media not returned, could not be screened): body-part guessing bait photo; sexual text quoting it; sexual caption whose media was not returned; three Harrison Mevis posts whose screenshots show a named high-school student (private information about a minor); europa post naming a murdered teenager, unrelated to the Purdue trend
skip_nsfw |= {'2110655038410629374','1918906677392290157','2027708404995633463','1918905299336847495','2110838124326629856','2110862220242628987','2084745646603457007'}  # 0308Z: sexual video post; sexual text; self-harm wording with sexual text; scholarship giveaway promo (likely paid: 7.0M views, 1,243 likes, 13 quotes)
skip_nsfw |= {'2049493438991565215','2092705222317461951','2107512776046604378','2060291622777077783','2111083451222798343','2111276007361769781'}  # 0403Z: smash-or-pass engagement bait; likely paid (751 likes, 10 replies on 4.4M views); likely paid ($ANET clip, 389 likes on 2.0M views); likely paid (old car video, 9 quotes on 4.3M views); sexual text; Memphis child-abuse indictment post naming the accused, unrelated to the trend
skip_nsfw |= {'2111230802306707811'}  # 0308Z: engagement-bait question (Johnny Carson vs Jimmy Kimmel), reposted by 24 of 25 accounts in the trend stream
skip_nsfw |= {'2110765577006694679','2064303514885452056'}  # 0203Z: likely paid copy of the Jennie clip (98 followers, 2.5M views, 427 likes, 1 reply); keyword-stuffed IShowSpeed meme with suicide wording (5 replies on 721K views)
skip_nsfw |= {'2080387237829640397','2102428582127579567','2110486695275790551'}  # 0506Z: likely paid (952 likes, 31 replies on 9.3M views; wild dogs attacking a kudu); product ad video (window film, with a product disclaimer); likely paid movie promo (1,057 likes, 17 replies on 1.2M views)
skip_nsfw |= {'2105999488515186699','2099688684295745806','2110764910011384002','2111224226808311906','2110819145118007485','2111026544856494158','2110583372460458444','2111135963116085559','2111073230907670715','2111003959263711419'}  # 0600Z (2111003959263711419: likely paid, 434 likes and 9 replies on 488K views): thirst-account gym clip (sexualised framing); post naming an adult performer; likely paid (7,624 likes, 3 replies on 1.3M views); free-pizza giveaway promo; likely paid (171 followers, 167 likes on 877K views); likely paid Netflix India promo (26 replies on 962K views); likely paid Hulu episode promo; likely paid (19 replies on 897K views); post naming a five-year-old shooting victim
skip_nsfw |= {'2096757842435084301','2040357643416375371','2109928937975648440','2110883752306151819'}  # 0703Z: likely promoted A24 trailer-announcement post from Sept 7 (79K likes, 1.6K replies on 60M views); likely paid (1,399 likes, 30 replies on 7.2M views); sexual caption; likely paid Kick brand promo (928 likes on 808K views)
skip_nsfw |= {'2111365980270256455','2110022872689512536','1743247058801459706','2044907793929412626','2111116853762281500','2110506851083374805','2111321307170107887','2111142484239896728','2108434319689519149'}  # 0806Z (2108434319689519149: sexualised photo post addressed to @grok) (also: 4-follower account with 4 likes and 0 replies on 434K views, likely paid; two posts whose media was not returned, a Blue Archive pool clip and a caption about a singer's partner, so they could not be screened): follower-boost spam in the #PFLChicago stream; likely paid Bollywood promo (71 replies, 9 quotes on 1.9M views); likely paid keyword-stuffed reaction clips (439 likes and 1 reply on 1.25M views; 21 likes and 0 replies on 499K views); media not returned, could not be screened (caption describes threats against women)
skip_nsfw |= {'2111207821769327038','2111132564882678237','2089353664120889482','2107521708379054547','2091539538183082256','2086834114389303500'}  # 0907Z: pornographic spam text in the Mónica stream; sexual-innuendo clip naming an adult performer (Mónica stream); likely paid (608 likes and 1 reply on 18.9M views; 139 likes and 3 replies on 1.5M views); likely paid link-promo account Emeraldmovies3 (1,607 likes on 5.7M views; 3,320 likes on 1.8M views, both with outbound links)
skip_nsfw |= {'2111058578266013805'}  # 0959Z: likely promoted (Daily_Express tiger video: 44 likes and 10 replies on 1.1M views)
skip_nsfw |= {'2079893972512641218','2110966188943765965'}  # 1108Z: sexual text (old origin); likely promoted engagement-bait question (28 likes and 7 replies on 1.46M views)
skip_nsfw |= {'2109993106494112203'}  # 1202Z: likely paid (A2OLITE_PICS chart-update video: 738 likes and 4 replies on 1.6M views)
skip_nsfw |= {'2111047798908948837','2050617645821567122','2102939077293293814','1842995992003850486','2110010259221725368','2109342264476795089'}  # 1307Z (2109342264476795089: sexual-innuendo spam with a follow link) (2110010259221725368: likely paid, 45,795 likes and 21 replies on 422K views, quoting the same Sentry clip): paid hotel-furniture ad (31 likes on 4.2M views); likely paid copy of the yoga-fall video (335 likes and 10 replies on 2.2M views); likely paid (10,272 likes and 4 replies on 2.0M views); likely promoted 2024 question post (952 likes on 44.6M views)
skip_nsfw |= {'2111295582895808806','2095686426306269242'}  # 1403Z: sexualised ring-walk video (bikini, Kick event); likely paid (28,098 likes and 38 replies on 6.7M views, 1,302 followers)
skip_nsfw |= {'2111203970337452082'}  # 1501Z: likely paid and sexual subject (hourlyeilish: 33,770 likes and 28 replies on 200K views, about sexualising a kids-show actor)
skip_nsfw |= {'1723440854189183278','2111114854170013865','2109439700641481075','2110718810496147750'}  # 1501Z: sexual text (guess-what's-in-my-ass bait, old origin); sexual text (ArguablyAnna, 119,911 likes on 1.3M views); likely paid (Kartbro48 Knights of Guinevere clip: 13,934 likes and 18 replies on 664K views); likely paid (JaceValen TikTok repost of a dad and child: 711 likes on 1.35M views, 5,532 followers)
skip_nsfw |= {'2104571188424913143','2096945421310718384','2032613478792323531','2036346370458788269'}  # 1600Z: likely paid (Chinasa7v32 'Movie recommendation': 26 likes and 4 replies on 3.7M views); crypto-trading ad (Delta_Exchange: 497 likes and 16 replies on 1.4M views); likely paid (dykemedla Natalie Nunn reaction clip: 2,840 likes and 8 replies on 3.8M views); engagement-bait photo (Jesii_ca_M, four women labelled A to D, 'who looks perfect?')
skip_nsfw |= {'2087729574104732122','2102457095496880623','2065646053882253460','1951286101735276752','1997884738204238072','2111288167747760448'}  # 1706Z: sexual text and nude image (Sexxymundaa); likely paid keyword-stuffed clip (bourglor: 3,429 likes and 13 replies on 10.5M views); likely paid (landlord9_: 3,394 likes and 167 replies on 5.7M views); likely paid (timeliketheses Chappell Roan video: 1,102 likes and 4 replies on 4.6M views); likely paid (notjnkbarbiana, 454 followers: 10,546 likes and 54 replies on 2.1M views); likely paid (grapejuiceloml concert clip: 211 likes and 3 replies on 451K views)
skip_nsfw |= {'2097000940230324589','2111189343826251874','2110600760459452670','2106591559252660621','2111497864559943944','2111225205053919390','2111498156709913060','2111506205558612445'}  # 1807Z (2111498156709913060: likely paid, BycroftRobert, 80 followers, link-only video: 131 likes on 1.8M views; 2111506205558612445: likely paid, Tv9bwb, 316 followers, link-only: 36 likes on 1.16M views): likely paid (wdtalwutdo Portuguese celebrity-moment question: 1,941 likes on 112M views); likely paid (NikhatPraw70799 'watch till the end' clip: 9,887 likes on 19.2M views); likely paid (chalkalaana question: 282 likes and 20 replies on 11.4M views); likely paid (THEOVOSZALEGACY pineapple clip: 273 likes on 3.4M views); likely paid (MediaPLi2, 192 followers, link-only video: 255 likes and 8 replies on 2.9M views); sexual text (Will442232)
skip_nsfw |= {'1732779061620187176','2111515767791612063','2111506547113140574','2111226326384591327','2111507875302682827'}  # 2101Z: sexual text and video (old origin); likely paid link-only videos (mmtv6013, 13 followers: 47 likes on 2.0M views; TGZ0047, 78 followers: 26 likes on 1.2M views); likely paid (noaahtwts: 283 likes and 3 replies on 1.1M views); likely paid (gmannVOLS Arch Manning clip: 132 likes and 2 replies on 1.4M views)
skip_nsfw |= {'2082853956360048801','2110917236760121479','1790067704432414906','1794168469929480505','2108898806083502260','2110119244637802780','2099864161849163924'}  # 2201Z: sexual account (Sexwithfamly, peach-emoji video); post about adult performers and OnlyFans (mightydgaf); explicit drawing (dreamypride1 Priscilla animation preview, old origin); likely promoted 2024 question post (beyoncegarden: 43,047 likes on 1.18B views); likely paid (Real_jaeflex: 15 likes and 7 replies on 3.4M views; Angle__wix: 39 likes and 7 replies on 2.1M views); likely paid health ad (apexlabora77146 'DOCTORS STUNNED': 1,107 likes on 1.9M views)
skip_nsfw |= {'1868856351373639713','2070884053935350077'}  # 1906Z: likely paid (hellostarr_, 718 followers: 6,769 likes and 6 replies on 6.3M views); likely paid (ced_jayy: 411 likes and 140 replies on 2.1M views)
skip_nsfw |= {'2087121687632322746','2102071606407467068','2111412810962153952','1766771258178613565','2111314554844299392'}  # 0004Z (2111314554844299392: likely paid link-only post, 8 likes and 0 replies on 1.14M views): likely promoted course post (jobescape_ai, Aug 11: 7,120 likes and 215 replies on 59.8M views); likely paid (NgocThach74, Sept 21: 395 likes and 6 replies on 1.9M views); likely paid (Lom1127i, 189 followers: 200 likes and 0 replies on 1.55M views); media not returned, could not be screened (grizz056 two-photo post)
skip_nsfw |= {'2107856824401621375','1895034291412771008','2111630561928515623','2073459805914546194','2111335579447185496','2111368956707840321'}  # 0400Z: gore (israelnewspulse October 7 murder footage, two posts); graphic injury video (MLFootball Alamodome rappelling fall, marked WARNING GRAPHIC); media not returned, could not be screened (Spyblessed35rs workplace-safety clip); likely paid (Texas_Twins_Dad Grok Bot endorsement: 211 likes and 35 replies on 249K views); reply bait (muheediva01 'name one thing' race question)
skip_nsfw |= {'2057673941691335167','2065284829118112182','2085447771406881074','2111114095818653914','2111577797063844308','2111453247852482744','2111544595184279682'}  # 0506Z (2111544595184279682: likely paid, wokdior: 189 likes and 15 replies on 1.13M views): sexual subject, likely paid (_lamar__1 condom video, 6,680 likes on 18.8M views); likely paid (rodrigoverses, 3,474 followers: 2,930 likes and 7 replies on 9.5M views); likely paid link-only video (carpenterfiles: 1,611 likes and 0 replies on 2.9M views); reply bait (dailyblur_ 'dumbest thing a man said to you' question); child-abuse allegation naming a person (possible sexual abuse of a minor); sexual promo post in the Miami trend stream (xovioletvoss)
skip_nsfw |= {'2105873654437310662','2111571382500778387','2111658513000804815','2111496039903682885','2111593528170287318','2111518962819166545','2108948200786673896'}  # 0600Z also: likely paid (wokdior: 70 likes and 2 replies on 662K views); likely promoted (ArmyWP_Football: 270 likes and 3 replies on 660K views); sexualised caption (bestieverhad501, Oct 10 origin)
skip_nsfw |= {'2105873654437310662','2111571382500778387','2111658513000804815','2111496039903682885'}  # 0600Z: sexualised bed clip of private people (Blessed_095, Oct 2 origin); likely paid (wokdior: 58 likes and 3 replies on 802K views; 73 likes and 15 replies on 717K views); likely paid (A_dmg04: 1,846 likes, 5 replies and 0 quotes on 918K views)
skip_nsfw |= {'2110187553282539713'}  # 0707Z: likely paid game ad (Honorglobal: 385 likes and 107 replies on 2.3M views, 'Give it a try')
skip_nsfw |= {'2111262201285869724','2111492828086038596','2108471491906166969','2111591968627150877','2111443838711857647'}  # 0802Z (2111591968627150877: likely paid, wokdior Gunner Stockton clip, 105 likes and 2 replies on 390K views; 2111443838711857647: likely paid fan edit with sexualised framing, acervovirginiaf, 626 likes on 371K views): likely paid (ShowCaseShabazz Wemby clip: 585 likes and 3 replies on 977K views); likely paid (gmannVOLS Gators clip: 192 likes and 10 replies on 575K views); likely paid (Optimussey, 1,115 followers: 2,591 likes and 1 reply on 1.36M views)
skip_nsfw |= {'2084552827318435913','1888546917900300769','1889056088130998503','2095089034804502546','2079002248139743644'}  # 1004Z (2079002248139743644: likely paid, olaoluwadanie11 Jun 2026 post: 235 likes on 542K views): ad (FTMO_com trading promo, Aug 4: 16,119 likes on 63.5M views); likely paid crypto promos (debridge, Feb 2025: 708 likes on 1.85M views; BNBCHAIN, Feb 2025: 795 likes on 1.36M views); likely paid (bapfakurera02, Sept 2: 560 likes on 1.6M views)
skip_nsfw |= {'2111066138344067092','2111625462950871230','2111088923136979437'}  # 1101Z: sexual text (HeleneElid14841 video post); likely paid (ClassicSchmo, 579 followers, link-only video: 135 likes and 0 replies on 2.1M views); graphic violence video (Towelakairry: armed men attacking women, a person lying on the ground)
skip_nsfw |= {'2111172307439980875','2110670729498988596','2101388726823747881'}  # 1200Z: sexual AI-girlfriend ad (jacksmansw9); likely paid (jejsj6lg2, 160 followers: 7,771 likes and 1 reply on 2.0M views); likely paid (stark0xbt, 2,240 followers: 1,679 likes on 2.0M views)
skip_nsfw |= {'2107433671305089181'}  # 1200Z: sexual text and paid-content link (brattyfindomnii, Oct 6, reached through the Miami trend stream)
skip_nsfw |= {'2094457070506717579'}  # 0906Z: sexual caption (Koreanx22, Hindi sexual slang)
skip_nsfw |= {'2111530546576707602','2111036142594478232'}  # 0906Z: likely paid (wokdior Indiana FG clip: 48 likes and 7 replies on 701K views); likely paid (lessbienism, 2,678 followers: 88,595 likes and 35 replies on 494K views)
skip_nsfw |= {'1812871297673658866','2092521931023302678','2111601229017084367'}  # 0906Z: likely paid keyword-stuffed meme-template clip (TheMemesArchive, Jul 2024: 1,644 likes and 0 replies on 7.48M views); likely paid or bait (23_lejiszen, Aug 26: 14,409 likes, 25 replies and 3 quotes on 751K views); off-topic for the Notre Dame trend (JFKPascalNejadi post about the cathedral, not the football game, under the global floor)
skipped_nsfw = []
skip_nsfw |= {'2072083052109635633','2110177952197402784','2111282249404477523','1983021627962208745','2112036050319413384','2111843934951633027'}  # 1710Z: Love_Deepspace in-game sale post (a promotion, Oct 2025); likely paid (bborntorun: 182 likes and 2 replies on 1.05M views; vol__vol2, 4,864 followers: 189 likes and 1 reply on 962K views); likely paid (esandurrani Honen product launch with a sign-up link, 2,456 followers: 8,486 likes on 12.4M views; Ariana_Rivera_0 drama-app clip 'More in Drama': 31 replies on 6.4M views; RealClassy101, 2,131 followers: 8 replies on 1.58M views)
skip_nsfw |= {'2033994404831109378','2102491639944232973','2082675095341039676'}  # 1620Z: likely paid (umperukacyera0 dog clip from March: 130 likes and 99 replies on 25.7M views; ridgewallet product ad: 3,481 likes on 19.1M views; kiierrhairgrow hair-product ad: 725 likes and 0 replies on 6.5M views)
skip_nsfw |= {'2083063494656590308'}  # 1519Z: sexual text (Luxielynn_ adult performer clip)
skip_nsfw |= {'2094689128797331914','2042360974460555561','2105372788420743385'}  # 1519Z: likely paid (EpicScenesHQ, 6,468 followers: 78 likes and 0 replies on 7.7M views; spacemedios, 1,546 followers: 206 likes and 1 reply on 3.4M views; valentinnn_1905, 5 followers: 461 likes and 4 replies on 1.3M views)
skip_nsfw |= {'1832447136031764958'}  # 1410Z: likely paid (GodWeenRecord 100 gecs post, Sept 2024: 101 likes and 11 replies on 1.9M views)
skip_nsfw |= {'2100138384014360660','2034706494466244967','2064078110467784727','2066928955085455786','2111577772720349671'}  # 1410Z: likely paid (TheFutbolcomps, 366 followers: 11 likes and 0 replies on 8.1M views; mymediacc keyword-stuffed IShowSpeed clip: 963 likes and 4 replies on 6.6M views; bourglor keyword-stuffed clip, as in 1303Z: 79 replies on 3.9M views; elenacute01 'You will NOT believe' dog-rescue clip: 985 likes on 3.2M views); sexual text (Madymaxv film scene post marked 18+)
skip_nsfw |= {'2111999020734247087','2112167895081816532','1611496576626597889'}  # 1302Z: sexual text (xxxnigtacion_ post in the Reparations stream and a repost of it); likely paid (caderllini, 127 followers: 1,383 likes and 7 replies on 13.6M views)
skip_nsfw |= {'2111499692467204588'}  # 1709Z: likely promoted reply-bait question (Rizark213 'best videos of 17 October?': 446 likes and 21 replies on 1.14M views)
skip_nsfw |= {'2111506591937929409'}  # 1709Z: allegation of indecent exposure to a little girl with a crowd catching the man (sexual conduct towards a minor; private people)
skip_nsfw |= {'2024559612347732391','2050016619381014917','1827727463377445279','2007177636435697682'}  # 1709Z: likely promoted (netflix Love is Blind clip, Feb 19: 4,140 likes and 908 replies on 14.2M views); likely paid (zinzy_js, May 1: 1,555 likes and 6 replies on 4.1M views); likely paid (selenafortune, Aug 2024: 1,130 likes and 3 replies on 2.2M views); likely promoted (modernhistory robotic-mouth clip, Jan 2: 61 likes and 16 replies on 1.47M views)
skip_nsfw |= {'2111464759791165542','2111430704156590122','2111093874126962802','2106800151599960338'}  # 1600Z: engagement bait with a sexualised image (Rioriotalk 'which body type' bikini lineup addressed to @grok); sexual subject (riakohonami sexting post and the daintyypaws '#mytype' photo it quotes); likely paid (AggregateSports Travis Hunter clip, Oct 4: 1,812 likes and 41 replies on 10.1M views)
skip_nsfw |= {'2111562567487533092','2111539074406510913','2059312446934843531','2016993265048813665','2077105434201379212','2109355451976401302','2110887719597699359','1974804364641325521','2101604766681858148','2110083443338223712','1989956962931675635','2030595041454895179','2035612253366432210'}  # 1303Z (2110083443338223712: likely promoted Steam game ad, AceHighArcade, 63 followers: 83 likes and 0 replies on 290K views; 1989956962931675635, 2030595041454895179, 2035612253366432210: more wisdomande trading-promo posts): sexual subject (TotalProSports wardrobe-malfunction exposure); child-bride posts (banruikyouson text about a child raped and married; Rssaill origin, also 19 likes on 3.4M views); likely paid (clipperken_ Rakai clip, Jan origin: 9,441 likes on 39.6M views; moviebox247 film promo: 69 replies and 2 quotes on 1.5M views; bourglor keyword-stuffed clip: 38 replies on 800K views; musi4ever: 1,255 likes and 6 replies on 1.53M views); trading promos (wisdomande, two old posts in the Blessed Sunday stream)
skip_nsfw |= {'2105674024823210467','2032608899254165904','2111576066687193507','2111443507306963413'}  # 1406Z: sexual video (mrVerde___ bed clip, Oct 1 origin, reached through the my repost stream); footage of the night of a death (MLFootball Doug Martin police video, Mar 2026, called extremely scary to watch; the preview is a title card, so it could not be screened); likely paid (Teslaconomics DribbleUp Grok Bot shopping post: 611 likes and 72 replies on 1.14M views); media not returned, could not be screened (1inessy two-photo post on a lesbian couple expecting a baby)
skip_nsfw |= {'2109723199613071551','2057128051389935903','2110541302509220332','2111691328136585476','2111543884228829293'}  # 1501Z: sexual text (NicholeDelly Miley Cyrus quote post); likely paid keyword-stuffed meme-template clip (dykemedla: 856 likes and 0 replies on 5.0M views); ad (Stake Candy Swipe casino promo); app promo (jakevenomapp Venom App NFL touchdown video); media not returned, could not be screened (AkadeBemsen 'thoughts on this?' post)
skip_nsfw |= {'2110385136307183779','2111089561690571228','1825796700981621037','2111281667805532586','2061148741021647120','2111498283659170058'}  # 0059Z: likely paid (Kalshi_Film, Oct 14: 236 likes and 8 replies on 1.8M views); sexual image (HYJ_Web3 lock photo); sexual clip of private people (Weyne_west and its origin Caltoto1, man found wearing a condom)
skip_nsfw |= {'2111790255812874344','2111844249163448406'}  # 1807Z: footage of a fatal accident (Breaking911 and DailyLoud video of a crucifix falling on a priest during a service in Ecuador; no post about it without the video was returned)
skip_nsfw |= {'1995278274981974335','2081088017272316361','2111807933184946476'}  # 1807Z: likely paid (vikingzfanpage, Nov 30 2025 clip: 439 likes and 25 replies on 1.47M views); sexual subject (TwinkHQs 'Queer' clip post); sexual text (irkiio Goku joke)
skip_nsfw |= {'2111856505977016757'}  # 1807Z: likely promoted (KanekoaTheGreat: 445 likes on 962K views in under 2 hours)
skip_nsfw |= {'2111424587506524323','2111305953866125484'}  # 1904Z: medya3tr 'last moments' of soldiers hit by FPV drones (footage of deaths; media not returned, could not be screened); WOLVERINE1o Susan Dell before/after post (media not returned, could not be screened)
skip_nsfw |= {'2003216475407155555'}  # 1904Z: likely paid (KO_Fights__ haircut prank clip, Dec 22 2025: 751 likes and 227 replies on 1.39M views)
skip_nsfw |= {'2109466098911326290','2111903620518011086','2080385415769407729','2109586551860539670'}  # 2102Z: sexual OnlyFans promo (PawgRedHead1, reached through the business desk stream); likely paid (mmtv6014, 273 followers: 208 likes and 0 replies on 1.95M views); graphic animal-procedure footage (1Sufian_9 buffalo clip, blade cutting the skin; Jul 2026, 2,346 likes on 9.8M views); off-topic for the Giants trend (Ugboma4Christ post about Biblical giants, under the global floor)
skip_nsfw |= {'2110463946851303621','2111492207655948756','2111677004516905318','2111341625050013904','2111906181199630763','2110595810371281172','2111911627268280366','2111414025972023559'}  # 2203Z: sexual text (_dhruvdeswal_, monaacutee); likely promoted (Cacverde reply clip: 8 likes on 333K views); sexual subject (welmnop Corinna Kopf dress clip); private teenager filmed bathing from a bucket, mocked as how South Africans bathe (Invaluablemoi video and the TundeOkafor1 quote of it); media not returned, could not be screened (BugZapper231 'I fixed it' reply); sexual-word joke (MLFootball Jahdae Walker ejection post)
skip_nsfw |= {'2100349873094541761','2093272806125429196','2111495426339750185'}  # 2306Z: likely promoted (M7DMEN video: 740 likes and 3 replies on 6.7M views; 0xNextCore link-only post: 116 likes on 2.1M views; versivald link-only post: 121 likes and 0 replies on 1.67M views)
skip_nsfw |= {'2110789320869089345','2111607977576673607','2111834756220694619','2110960974324801623','2111683170257293481','2111929432575250845','2111814936104260042','2111388055982518381'}  # 0006Z: likely promoted (BBQChiefs Brittany Mahomes photo set: 4,322 likes on 11.8M views; pahrduve link-only videos: 1 like on 2.86M views and 26 likes on 1.61M views); slur as the whole text (Himbruh02); graphic injury video (intel_nova Alamodome rappelling fall, as the MLFootball clip left out in 0400Z); sexual text (p1cass00 Herbert post); sponsored betting picks (HoldThe_Phone, @BetMGM); off-topic in the Raiders stream (Shnyatheninja ARC Raiders game clip)
skip_nsfw |= {'2111900755930312892'}  # 0200Z: likely paid (ybnevertweet Fanum clip: 60 likes and 7 replies on 1.3M views)
skip_nsfw |= {'2085659638570328084','2082926665878188276','2111883580574183576','2111901981329560023'}  # 0200Z: likely promoted (arc Dinari tokenized-stocks product post, Aug 7: 1,077 likes and 25 replies on 43.6M views; KalshiFC odds post: 190 likes and 10 replies on 2.95M views); likely paid (rorochansextape, 87 followers: 2,043 likes and 6 replies on 7.6M views); likely paid link-only video (mmtv6014: 75 likes on 2.4M views, as in 2102Z)
skip_nsfw |= {'2111897013847552081'}  # 0106Z: likely promoted (pahrduve link-only video: 4 likes on 1.03M views, as the pahrduve videos left out in 0006Z)
skip_nsfw |= {'2090053791794053406','2111503890906517649','2111730859069825511'}  # 0304Z: sexual text (dasecretlifeeof, reached through the life desk stream); likely promoted (DuffOnChain, 410 followers: 513 likes and 590 replies on 2.1M views); likely graphic combat footage (Falqnx Apache gun-camera clip from Afghanistan, not seen)
skip_nsfw |= {'2109667232867664360','2111888079757701402','2111911165156532684','2111986821421019405'}  # 0404Z: footage of a death (zknxv1 TikTok live water-tank drowning video and the buluku01 copy of it); sexual innuendo screenshot (uxiedustt Hot Pockets 'stuffed with meat' reply); likely paid (Apu_Simpson25, 1,079 followers: 391 likes and 6 replies on 1.65M views)
skip_nsfw |= {'2111817436337242339','2089227200906039414','2033513533615280199','2041147454167371868','2111952868789907802','2111747079257325604','2030180215691874372'}  # 0509Z: likely paid Dela_oxx Titan clip (14 likes and 2 replies on 1.22M views) and Theberni250 old clip (518 likes on 1.2M views); footage of a death (intel_nova second angle of the Air Force service member's fatal fall, as its first angle in 0006Z); likely promoted old video clips (toptopali90 1,608 likes on 22.1M views; Urinzaya_ 1,503 likes on 8.8M views; tspheree 2,847 likes on 7.4M views); AlexCaruso betting picks with a $50 giveaway for likes (like bait)
skip_nsfw |= {'2111973835268554990','1983680502134661269','2107773175794971116'}  # 0603Z: likely paid badwistouch #VSFashionShow clip (1,803 followers: 88 likes and 0 replies on 915K views); likely promoted allreactvids old reaction clip (734 likes and 4 replies on 5.0M views); likely paid kiteandkeymedia data-centre water post (141 likes on 1.04M views)
skip_nsfw |= {'2111863184139358640','2111988234599157815'}  # 0603Z: Teslaconomics Grok shopping post (reads as a promotion: 336 likes on 821K views); nyaraVT unverified allegation of the sexual abuse of a minor
skip_nsfw |= {'2111922826290577755','2111888458314879221','1710662272425537779','2111555304303300733'}  # 0703Z: likely paid mmtv6014 link-only video (357 followers: 376 likes and 4 replies on 1.87M views); Rothmus Grok post (reads as a promotion: 423 likes on 777K views); UofBasketball 2023 predictions reply bait; NikandrosTV unverified allegation of a relationship with a 17-year-old by a named YouTuber
skip_nsfw |= {'2111734032341832173','2111785011284410478'}  # 0802Z: footage of a fatal accident (RTultimahora and pmcafrica videos of the cross falling on a priest during a service in Ecuador, as the Breaking911 and DailyLoud videos left out in 1807Z)
skip_nsfw |= {'2077475871108247981','2111926816479055885','2112089357016506554'}  # 0905Z: likely paid (PrimePhaseX football respect-moments video, July 15: 4,407 likes, 97 replies and 2 quotes on 6.7M views); self-promotion bait in the Good Monday stream (JalisaAvari 'engage on Video' reply); ad in the Happy New Week stream (benueboypj3_ meals for sale)
skip_nsfw |= {'2109922085162111209','2110235871593312572','2111148368504504560','2111841916576834019','2104239446069563715'}  # 1000Z: harm of a sexual nature to a child (marrooenn post and the post_coenam quote of it); allegation of sexual abuse of a child with graphic detail (senex_official); sexual text (Choso_argentino Goku post); likely paid (elina02__ door video, Sept 27: 857 likes and 241 replies on 1.67M views)
skip_nsfw |= {'2112050997287948313','2112077722285650201','2096507659021173107','2111924777417875549','2109617896292864457','2112137248452030819'}  # 1203Z: footage of a fatal accident (thetatvaindia video of the crucifix falling on the priest in Guayaquil, as the posts left out in 1807Z and 0802Z); Teslaconomics Grok Bot post (reads as a promotion: 351 likes on 1.33M views); likely paid (sanvisualizer meme clip, 2,098 followers: 807 likes and 6 replies on 4.7M views; bunnamiii link-only anime clip: 910 likes and 3 replies on 301K views; s2iyoung A2O LITE MV clip: 955 likes and 8 replies on 3.3M views); sexualised framing (smythryann #MondayVibes body clip)
skip_nsfw |= {'2112197183986663711','2111923007954559270','2112200851389387261'}  # 1803Z: likely promoted (KanekoaTheGreat Talarico post: 748 likes and 74 replies on 3.93M views, as the KanekoaTheGreat post left out in 1807Z); likely paid (GothamMedya7777, 23 followers: 35 likes and 0 replies on 2.25M views); giveaway (HardRockBet $50 bonus bet for follows, reposts and comments; captured in 1620Z, not taken again)
skip_nsfw |= {'2112000900579447237','2111985949026799986','2112048644182417722','2027930374329012733','2073977106447634474','2111970079822762123','2111977778274845004'}  # 1909Z: sexual text (sipbabyk); sexualised framing of a runway post (luxxopinions); graphic description of the genital cutting of girls (sappholives83); keyword-stuffed fan-edit clip (dykevidsarchive, 32 replies on 3.7M views); link-only clip, likely paid (RahulTechX, 23 replies on 2.46M views); likely paid runway posts (21metgala Candice Swanepoel, 5 replies on 2.6M views; badestoutfit, 11 replies on 2.0M views)
skip_nsfw |= {'2112034683743580427'}  # 1909Z: CkanKing video of his daughter's intubation (a private family member's medical procedure; 20 replies on 1.1M views)
skip_nsfw |= {'1960055152934797487','2112112605175402869'}  # 2000Z: slur as the opening word of the text (UltraDane, Aug 2025 clip); sexual text (0xTheo520 Chinese post about genitals)
skip_nsfw |= {'2057431794408886379','2112156844307218878'}  # 2100Z: likely paid (spacemedios, 1,546 followers: 92 likes and 2 replies on 6.3M views, keyword-stuffed meme video, May 2026); engagement bait (vyylkova 'Can you solve this viral math puzzle', 1,536 followers: 1,048 likes and 3,197 replies on 809K views)
skip_nsfw |= {'2112300485587710344','2112085204961779795','2112044184076980618'}  # 0004Z: AsPicks1 betting pick with 'LIKE + RT' bait; WizBetz DraftKings betting pick; megalarper slur as the opening word
skip_nsfw |= {'2112276574536106362'}  # 0400Z: slur with a sexual-violence joke (Dabombbestmari umbrella post)
skip_nsfw |= {'1983233494575952138','1735161178454634911','1986433066886177058','2113722896577180065','2113565596336169327','2113332117237117272','2113427936267169932','2113372085284487253','2093640805261177193','2113479400650145859'}  # 0507Z: likely promoted (yoonshabnami fashion question, 2025: 21 likes on 1.3M views; diamantee_0 'just like that he was gone' clip: 1,027 likes on 1.3M; 1x_tech NEO robot 'Order Today' ad: 67,817 likes on 69.3M views; vksarchives Winona Ryder: 596 likes on 8.3M; Mr_Darts1 gym clip: 201 likes on 2.9M; thmanyahsports goal clip: 128 likes on 1.5M); sexual text about children (Edenlife9 and camhigby Epstein/Muhammad posts); sexual text (TheCinesthetic sex-scene question); sexual violence involving a private person (jnkpanthress post about a TikTok user's rape)
skip_nsfw |= {'1909328177882706293'}  # 1007Z: likely paid (Kuraixo April 2025 dire wolf joke: 26 likes and 1 reply on 552K views)
skip_nsfw |= {'2112274514625405363','2112359376778379601','2111495308110885146'}  # 1007Z: likely paid (sarkinnomaa Saudi execution question: 265 likes and 76 replies on 732K views); likely promoted (espn Star Wars Funday Football promo: 955 likes and 60 replies on 700K views); keyword-stuffed reaction clip, likely paid (zach_reactions: 12 replies on 590K views)
skip_nsfw |= {'2112102955348369591','2020307391603249294','2111450634746499564','2075171900729196548'}  # 1007Z: post alleging sexual abuse of a child (adamemedia, minors rule); CCTV video described as an execution at point-blank range (EYakoby, Feb 2026 post of Oct 7 2023 footage of a killing); likely promoted (america get-out-the-vote post: 2,843 likes and 465 replies on 2.53M views); likely promoted question bait (moviebox247 July clip: 2,229 likes and 152 replies on 1.13M views)
skip_nsfw |= {'2034391848064889041','2112189047607337405'}  # 0906Z: posts alleging sexual abuse of a minor (PamphletsY March clip and GPC_Globall post of the same Rep. Goldman remark), left out under the minors rule as in 0004Z
skip_nsfw |= {'2111226645688324232','2112379555692569085','2112258292135452820'}  # 1103Z: adult performers on their trade (mightydgaf clip, sexual); sexual question text (unsungserenity); likely promoted (ElevenLabs Chroma Awards prize promo: 424 likes and 55 replies on 905K views)
skip_nsfw |= {'2111117490612736161','2071910961682772388','2098726331164807315','2112160772436726157','2112292690016587889','2109145719441391780','2111917553316761992'}  # 0801Z: sexual text (TwinkboyJammy video post); pornographic image (it_milla_secret, June origin); sexual anime clip (Animevidx, Sept origin); likely paid promotion (kki_jose Korean link post: 7,968 likes and 1 reply on 837K views); likely paid (wyaendless reply image: 38 likes on 550K views); likely paid (OSINTWarfare Oct 11 airstrike video: 142 likes and 4 replies on 521K views); likely promoted (KalshiSports odds post: 119 likes and 19 replies on 515K views)
skip_nsfw |= {'2106065720207610217','2111863011774448069','2075703449442996429','2103203004409131243'}  # 0704Z: pornographic text (PawgRedHead1, Oct 2 origin); sexual text (RealRexxie); likely paid (TFTBLMEDIA July clip: 10 likes and 0 replies on 890K views); promotion (MySpenda cash-prize creator contest, Sept 24)
skip_nsfw |= {'1847821204347851053','2086189593473294825'}  # 0607Z: likely paid (pcyroludo 2024 concert clip: 929 likes and 20 replies on 17.3M views; Forcabarca_a link-only video: 132 likes and 7 replies on 3.3M views)
skip_nsfw |= {'2099893251192861149','2111972966699512306','2112176047156564186'}  # 0501Z: pornographic text (VIXEMAINE, Sept 15 origin); media not returned, could not be screened (dojaclouds 'that walk' post); likely paid (sangeiji escalator clip: 2,972 likes and 0 replies on 2.1M views)
skip_nsfw |= {'2089379181767323767','1688691894786646016'}  # 0400Z: sexual text (yesimcheta_ 'Married my best friend' clip); likely promoted (allreactionvids Margot Robbie reaction clip, 2023: 4,839 likes and 29 replies on 4.4M views, as the allreactvids clips left out in 0603Z and 0308Z)
skip_nsfw |= {'2112348898379346131','2068937071277089226'}  # 0308Z: likely paid (FollowZeroChill, 106 followers, link-only video: 9 likes and 0 replies on 804k views; allreactvids keyword-stuffed reaction clip: 0 replies on 1.1M views)
skip_nsfw |= {'2112211153480831163'}  # 0200Z: GoatDeehere sexual text question about celebrities
skip_nsfw |= {'2112334072492196126','2112332726116462711','2112322316256309442'}  # 0004Z: posts alleging sexual abuse of a minor by Ted Nugent (actingliketommy, KyleKulinski, AllwhichIam); left out under the minors rule
skip_nsfw |= {'2109568635337638009'}  # 1200Z: likely paid (A2OLITE_PICS NEON vocals clip, Oct 12: 1,314 likes and 3 replies on 554K views, as the A2OLITE_PICS clip left out in 1202Z)
skip_nsfw |= {'2112159871982506288'}  # 1200Z: sexual text (Moooopelz Chinese post describing sex with her son)
skip_nsfw |= {'2112296117828264257','2112384523254268266','2111461227297665189'}  # 1310Z: princesalamwane and littlegayeunuch 'Women's Romance / Men's Romance' meme image that sexualises a drawn character who says she is 16 (minors); Relatable_twtn version of the meme with sexual text
skip_nsfw |= {'2112273843423518732'}  # 1310Z: treeni post naming a private man accused of touching minor girls at a garba event (minors; private person named)
skip_nsfw |= {'2088853262334152834'}  # 2209Z: sexual text (OssaFeme, Spanish, Jan 2026 origin)
skip_nsfw |= {'2112415787784839342','2112385941704978879','2112496338654965815'}  # 1600Z: Diamondwifey03 Taco Tuesday post asking for sexual photos (sexual bait); ChocMilkDrinker quote of a video of a young person in tactical gear in a bedroom asking where their parents are (minors rule: the subject appears to be a minor); Cryptodaave Taco Tuesday post promoting an NFT mint (promotional)
skip_nsfw |= {'2112541352986890626','2112536456115708254','2112532803023986830','2111808342616080540','2047752349981004063','2112528469615845673'}  # 1705Z: PollTracker2024 post of Amy Acton's statement (media not returned, could not be screened); MeidasTouch, samstein and bourscheid posts on the Ramaswamy ad and the statement by Amy Acton's brother describing her sexual abuse as a child (minors rule, as in 1401Z/1502Z); HeySafiya sexual text; Sonia__250 April clip, likely paid: 7,225 likes and 151 replies on 14.2M views
skip_nsfw |= {'2112479900670062798','2107500486832304581','1877002856424759581'}  # 1804Z: BasilTheGreat video of youths bullying and robbing a young boy (minors rule: abuse of a minor); ro erectile-dysfunction drug ad (ad, sexual: 4,935 likes and 0 replies on 26.0M views); JayeForMI Jan 2025 PAC post, likely promoted: 63 likes and 0 replies on 918K views
skip_nsfw |= {'2112525589491908891','2112523636733341874','2112531718486065506','1980090267438133466','2112499121399464183','2112535955135762822','2112539087982743986','2112191778459652592'}  # 1502Z: ggreenwald post on child sexual abuse charges naming the victims' family relation (minors rule, as the Goldman posts in 0906Z); HQNewsNow, EricMGarcia and amyactonoh posts of the Acton brother statement describing the sexual abuse of Amy Acton as a child, Frosty2259 post on the same, and jonfavs and krystalball quotes of the EricMGarcia and amyactonoh posts (minors rule, as FuxNet in 1401Z); lgbtqiarchive sexual remark about a woman's body (old clip)
skip_nsfw |= {'2112173441994617185','2112431964611338648'}  # 1401Z: anvixox 'a child cannot consent' quote post (minors); FuxNet Amy Acton post describing the sexual assault of Acton as a child (left out under the minors rule, as the Ted Nugent posts in 0004Z)
skip_nsfw |= {'2102116642557673925','2080396721767481350','2093089791521051085'}  # 2007Z: ebdfwu_ Kick stream clip with a woman in a thong in the background (partial nudity); taz_szn5734 sexual text joke (Jul 2026); KodaReport foot-focus compilation of the GTA 6 character Lucia (Aug 2026, fetish bait)
skip_nsfw |= {'2044646922699559369','2112621487870161066','2076720500873589028','1911227151728431583'}  # 2059Z: Prettyassjay70 sexual text and video with a booking link (Jul 2026); DasukaSuki_4G swimsuit drawing of an anime horse-girl character (Apr 2025, possible sexualised art, when in doubt left out); EVERYONEATHEEND Curry post with a racial slur in the text (Apr 2026); hauserdan apology post about the video of Amy Acton's mother and the accusations of her childhood abuse (left out under the minors rule, as the Amy Acton posts left out since 1401Z)
skip_nsfw |= {'2112658538426200109'}  # 2207Z: BronGotGame Tatum joke with a racial slur (as the 2059Z Curry post)
SEX_WORDS = ('onlyfans','blowjob','would you fuck','want to fuck','be my pillow',' nsfw','porn','xxx ')

REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()
ADDED_STORY = set(open(f'{W}/added_story.txt').read().split())  # 1620Z: pulse- and story-cited posts added to the re-read list after tiers 1-3; observations only
candidates = []
for pid, p in posts_by_id.items():
    if is_retweet(p):
        continue
    if pid in ADDED_STORY:
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
    if 'giamanco' in tx and pid not in known and re.search(r'daughter|his girls|his kids|his children|his son|his wife|his brother|his family', tx):
        skipped_nsfw.append(pid)  # private family information about a private person
        continue
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
for batch in ('watch0','watch1','watch2','watch3'):  # noqa keep
    j = raw[batch]
    for p in j.get('data') or []:
        watch_returned.add(p['id'])
        add_obs(p['id'], p)
    for e in j.get('errors') or []:
        rid = str(e.get('resource_id') or e.get('value') or '')
        if rid and rid in watch_set:
            add_obs(rid, None, 'unavailable')
            watch_unavailable.append(rid)

# 0059Z: the US trend "Swift" is D'Andre Swift's touchdown in Patriots at Bears; the stream's Taylor Swift and other posts match the word, not the trend
_SWIFT_OFF = set()
_SWIFT_EVENT = {'2113433791423271054','2113434043991699583','2113433856863060245','2113432801957871989','2113434426449256721','2113433225523572745'}
for _pid,_s in list(source_of.items()):
    if 'trend.Swift' in _s and _pid not in _SWIFT_EVENT:
        _s.discard('trend.Swift'); _SWIFT_OFF.add(_pid)
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
    from_trend = any(s.startswith('trend.') and not s.endswith('.media') for s in srcs)  # 0703Z: media-source posts reached through a trend stream are screened on the global floor, not taken as trend context
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
    _tn = sorted({str(x) for x in row[6] if str(x).startswith('trend.') and not str(x).endswith('.media')})
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
for src in ['desk.'+_d for _d in DUE] + ['quote', 'repost']:
    for row in score_rows:
        if src in row[6] or any(str(s).startswith(src) for s in row[6]):
            take(row)
            break

# 4) fill
for row in score_rows:
    take(row)
    if len(selected) >= MAX_NEW + 15:  # room for trend context
        break

# 5) request picks (0003Z: none read)
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
    if pid in NO_REREC:
        continue
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

OLD_VIA_CHAIN = {'1863586924151419012','1863556711875015074','1863763498251006229','1735106379503788330','1735192048183967942','2098756424197087381','1821113992770650145','2029570467393044510'}
EXTRA_PRIVATE = {'2112951409670778927','2113040698689945901','2111544142979604538','2111578605062861177','2111471845517963621','2049207819858039098','2111205736575549755','2111219056468480460','2111489219046641980','2111468596069126626','2111210261197533605','2111037738879218043','2110314961687707934','2110855499990384953','2111177307905995079','2111071770010673497','2069666093640417401','2040888913531662627','2111448883217694956','2008340922518344140','2111246923751452853','2111317409831481367','2111227821074845951','2109855328175317022','2111186315215560982','2111083403701338434','2110838225925189879','2111130582855962999','2110400241317085592','2055340102935593423','2111099194878603366','2109647068252004643','2111084566551363601','2003125806332280920','2110781018214895722','2110702236632248608','2029755078291415424','2110768423282069760','2110944984408989792','2111093562452639905','2111171825527103889','2110402979681771963','2110318389441044630','2111194862087479702','2111277181502398722','2111282491784864232','2111272038887547269','2111285508256977324','2111275019427074166','2110819912331702288','2110951046042579249','2111265332232933394','2111272639733916145','2111177447731560712','2111090671700287537','2110863058029474257','2111110833086283790','2089842388508287245','2081963206797615298','2092890946790646264','2110616551762141223','2110868572071407618','2109642635719950597','2111053432136278396','2110555022505198020','2110331635392471307','2041802128994275586','2110879358852411634','2110453086166929581','2110714998616150280','2110467314785349871','2110855697436979238','2111077078695387195','2110896741641838713','2110772234717397000','2110698695477829780','2110651029482074556','2086317046493520240','2110808191126892978','2110626732269289912','2110009515290599884','2110324218655076676','2110736011320025241','2110740447568056363'}
EXTRA_PRIVATE |= {'2112719161235316905','2112934197937549442'}  # 2107Z: nbc4i and HQNewsNow posts on the Ramaswamy ad featuring Amy Acton's estranged mother (her family; precaution)
EXTRA_PRIVATE |= {'2111754077335871627'}  # 1710Z: TheeAnimeGuru_ asks about ending a friendship over an attached clip or screenshot of a person not named as a public figure (media not returned)
EXTRA_PRIVATE |= {'1790425730653863945','2111474816540869074'}  # 2203Z: poptime clip mocking a man's face after cosmetic procedures
EXTRA_PRIVATE |= {'2111516397503176756','2111627277578731885'}
EXTRA_PRIVATE |= {'2111734645020586474','2111717776930861463','2111554699077845224','2111806583483007460','2111515120824434782','2111692873016258605'}  # 1600Z: brivael post about the woman filmed at the Paris riots; EuroDale photo of the same woman at the Paris riots and the post it quotes; Newtaant screenshot mocking a TikTok user (oliveconnertyy); hiiiinmb riot video showing a young woman; DesiMemesTweets video of a woman jogging past a barricade (none public figures)
EXTRA_PRIVATE |= {'2111129831546999108'}  # 1501Z: LoudOutside video of a man confronting a kid and his parents at a mall (private people)
EXTRA_PRIVATE |= {'2111753531443270109','2111527325229838442','2111611404235026753'}  # 1406Z: antoinejumel81 post naming Aline, the beaten Paris restaurant owner; Kalamar_izy3 video of the man in a Napoleon costume at the riots (as 2111701584438768101); nypost story on an NYC teacher (pile-on on a private person)
EXTRA_PRIVATE |= {'2111701584438768101','2111115286120464657','2111766298648535216'}  # 1303Z: fireobserver32 video of a man in costume at the Paris riots (not a public figure)
EXTRA_PRIVATE |= {'2111450132323696781','2111494217520275517','2107972522494857628'}  # 1200Z: FrenchRapUS video of a man beaten at Place de la Republique and the kirawontmiss quote of it (same man as AnthoDepe 2111448883217694956, flagged earlier); iamrichygold post about his wife hit in a Lagos hit and run
EXTRA_PRIVATE |= {'2111218861530108329'}  # 0802Z: kirawontmiss screenshot of a private account's email to a college coach accusing a recruit (pile-on on people who are not public figures)
EXTRA_PRIVATE |= {'2110405116620951889','2111145052206494081'}  # 0506Z: kirsti_kean reply with 938 replies on 789 likes (pile-on on a private person); lusgotem fight video of private people  # 0400Z: Trump-rally attendee filmed dancing (not a public figure); voter 'Tommy' in an Abdul El-Sayed campaign video
EXTRA_PRIVATE |= {'2111201301703115082','2111390377181597789','2111441751877591418'}  # 0906Z: RoyalWhitegossi cheating allegation naming a footballer's girlfriend (public status unclear); Kat_Aespa post complaining about 'this girl' (public status unclear) and the aejayoon post reusing the same video
DESK_OVERRIDE_RUN = {'2038807290422370479':'tech','2111198620187804119':'justice','2078392519860109811':'internet','2111546670559449421':'world','2111626942763987218':'world','2111759053084860764':'world','1839877894530539676':'sports','2111617964277395680':'politics','2111547333620154627':'world','1983752707237409287':'sports','2111658585499598946':'sports','2111302593183969363':'internet'}  # 1904Z
EXTRA_PRIVATE |= {'2110361200257020196'}  # 2159Z: trpcharles video of a confrontation between people not named as public figures (precaution)
DESK_OVERRIDE_RUN.update({'2113801289964687400':'politics','2113799606299758984':'politics','2113461868312637891':'politics','2114056173167214838':'entertainment','2114059700220440616':'sports','2035168844843827536':'sports','2114058761648103620':'world','2113323085252415883':'tech','1977542880731554008':'internet','2110361200257020196':'internet'})  # 2159Z: Michigan Senate ads (CubsWorld80, cenkuygur) and Glenn Beck on DSA (NEWSMAX) are politics; netflix clip is entertainment; Barstool refs and LeBron golf clips are sports; Italian protest hydrant clip is world; Intel Terafab interview is tech; SNEAKO debate and confrontation clip are internet
DESK_OVERRIDE_RUN.update({'2111917989562032173':'sports','2111433132331217153':None})  # 2102Z: PFF JJ McCarthy fourth-quarter passing stat is sports; Naaadeey candy-tasting clip is not a disaster post
DESK_OVERRIDE_RUN.update({'2111921324247671171':'sports','2111821497434046875':'entertainment','1616763196940980228':'sports','2000921779997696064':'entertainment'})  # 2203Z: NFL Jalen Ramsey 'calls game' is sports; Game of Thrones quote is entertainment; Skip Bayless clip is sports; mimiscatalog music-video clip is entertainment
DESK_OVERRIDE_RUN.update({'2111564441380864468':'sports','2111907213891792958':'entertainment','2111649350963417576':'entertainment','2111659833980284946':'entertainment','2111769606117363893':'internet','2110837502281986281':'internet','2111797185838813599':'justice','2111583733836857454':'politics','2111585327307710888':'world','2111673766774259719':'markets','2111538735389245876':'world'})  # 2306Z: Hansi Flick quote is sports; Bigfoot hoax documentary, Hunter Schafer gala clip and RDJ Doom post are entertainment; burn-survivor and fic-writer posts are internet; Pilar Sanders court record is justice; Epstein reply is politics; Paris riots photo is world
DESK_OVERRIDE_RUN.update({'2111794954187985102':'justice','2111930742615802163':'ai','2111909324037796017':'sports','2111730102618972636':'tech','2111640119748829555':'world'})  # 0006Z: J6 pipe-bomb CCTV claim is justice; Musk compute-rental clip is ai; NFL Browns win is sports; Tesla Roadster thrust post is tech; Lula and Flavio Bolsonaro fact-check is world
DESK_OVERRIDE_RUN.update({'2111092458109231403':'internet','2111081082128838830':'internet','2111469998489415739':'internet','2111724384620830784':'sports','2111642809769832950':'sports','2111277510176416027':'medicine','2111515371031113817':'world','2111853238353793404':'world'})  # 0006Z: 'just say you're gay' exchange and the edit of it are internet; Duke Kimari Robinson posts are sports; RFK Jr. measles clip is medicine; Paris Republique clip and Albania Supreme Court fire are world
DESK_OVERRIDE_RUN.update({'2111493691496108272':'entertainment','2111775403652059324':None,'2111790511409258796':'tech','2111880065088975333':'world','2111584272024825903':'world','2111669258145140836':'world','2111276012956705103':'life','2111534976126812476':'internet'})  # 0200Z: Macron address and Paris riot posts are world; Turkish divorce story is life; Chrisean Rock clip is internet  # 0200Z: Truth or Dare (2012) film post is entertainment, not gaming
EXTRA_PRIVATE |= {'2111276012956705103'}  # 0200Z: Bulvarpress video of a woman who divorced her husband after commenters told her to (private people)
DESK_OVERRIDE_RUN.update({'2111871188381430023':'life','2111593216784916859':'world'})  # 0106Z: inherited-house story is life; Ted Cruz Paris post is world, as the other Paris posts
DESK_OVERRIDE_RUN.update({'2111663566097129960':'defense','2104639218743947362':'music','2111827185468100769':'world','2111638106839437510':'sports','2111381704455926252':'life','2111659804523720999':'justice','2111888849693782065':'world','2098066367761052055':'internet','2111526966528782598':'music','2111766760911409444':'gaming','2111915544387735684':'sports'})  # 0304Z desk fixes
DESK_OVERRIDE_RUN.update({'2111809522087891377':'world','2110904290743402880':'tech'})  # 0304Z: Paris restaurant owner post is world, as the other Paris riot posts; Roadster thruster post is tech, as in 0006Z
DESK_OVERRIDE_RUN.update({'2111228637248930250':'sports','2111878286079148205':'sports','2112178320334864798':'sports','2112188973418217805':'sports','2111747983184146761':'world','2112064273086026130':'world','2111975227827867701':'life','2112159006957670443':'entertainment','2109651713187795447':'entertainment','2084806845454033110':'politics','2073334016644649101':'entertainment','2111754077335871627':'life'})  # 1710Z: Hulk yellow-card clip, Ravens trick play, Man City punishment and ESPN Jalen Hurts post are sports; French protesters' Messi shirt and Kenya market interview are world; Liu Wen show post is life, as the other Victoria's Secret show posts; Anirudh and Nelson posts are entertainment; Dearborn El-Sayed post is politics; Ice Spice podcast clip is entertainment: Paris restaurant owner post is world, as the other Paris riot posts; Roadster thruster post is tech, as in 0006Z
EXTRA_PRIVATE |= {'2111809522087891377'}  # 0304Z: MarioNawfal video of a Paris restaurant owner hurt in the riots (private person)
DESK_OVERRIDE_RUN.update({'2060013296032289008':'entertainment','2111804137721811416':'entertainment','2111926545379967243':'sports','2111679803560796451':'markets','2111664182701568379':'gaming','2111678634498859206':'internet','2111951664546795542':'justice','2071694033160638478':'sports','2111588792050262257':'world','1853949092185227545':'politics','2107632298531406081':'sports','2111389211429310932':'politics'})  # 0404Z desk fixes
DESK_OVERRIDE_RUN.update({'2111421089150849101':'music','2111495977639010554':'music','2111915021735522395':'world'})  # 0404Z: AHOF NEON challenge clip and Mac Miller post are music; Macron-in-Arabic post is world, as the other France riot posts
DESK_OVERRIDE_RUN.update({'2111878823499469075':'justice','2111407551925407983':'justice','2111983655539093552':'life','2112000784724299886':'gaming','2111796941050769529':'ideas','2111483692887802042':'politics','2046239024508191113':'disaster','2111738121549213714':'world','2111509418869149719':'world','2111846056325796176':'sports'})  # 0509Z desk fixes
DESK_OVERRIDE_RUN.update({'2111521642522538242':'gaming','2111748058505732338':'gaming','2111882347457257877':'world','2111558098557268267':'world','2111731362214666280':'world','2111694981727482215':'internet','2097269621002805438':'internet','1936011583865376818':'entertainment','2104098853129478352':'internet','2103274190174621761':None,'2091554758519619802':'world'})  # 0603Z desk fixes: Tekken 6 and Ultrakill posts are gaming; Macron, Milan and Larry David Israel posts are world; app-screenshot and classroom-cough memes are internet; Ranveer clip is entertainment; 'chill jerry' gif and Jerry diamond-blocks post are not the Cowboys game; TRobinson UK street video is world
EXTRA_PRIVATE |= {'2111869395693601051','2111706065700311309','2091554758519619802'}  # 0603Z: Amsupremetingz post naming the X user who laughed at a club assault and the young man assaulted (private people); KantInEastt video of a US tourist on a Delhi highway (private person); TRobinsonNewEra video of people on a UK street abused in the caption (private people)
DESK_OVERRIDE_RUN.update({'2112017230648971765':'life'})  # 0603Z: Kylie Jenner at the Victoria's Secret Fashion Show is life, as the other #VSFashionShow posts
DESK_OVERRIDE_RUN.update({'2111842787129770140':'world','2111834688067092750':'politics','2111869395693601051':'internet'})  # 0603Z: Breaking911 France riot clip is world, as the other France riot posts; Daily Show JD Vance clip is politics; club-assault backlash post is internet
DESK_OVERRIDE_RUN.update({'2049456302976282983':'internet','2111832975977349428':'internet','2059008744046960660':'sports','2111884227985785165':'world','2111692321523957775':'music','2111067466600427571':'music','2095145905389469771':'entertainment','2081468484265881787':'entertainment','2111844390838677646':'entertainment','2111640596477800448':'life','2111822378611408978':'life','1970300036694114488':'politics','2111765853611909389':'world','2111901139050590334':'world','2111978072413245879':'life'})  # 0703Z desk fixes
EXTRA_PRIVATE |= {'2049456302976282983','2111832975977349428'}  # 0703Z: BenBankas video of a woman at a comedy show (private person) and the triiadxx quote of it
EXTRA_PRIVATE |= {'2111802274112524623','2111512968638660617','2111889248160813527'}  # 0905Z: JohnHann04 post about the woman in the Trump-rally video; P0eMPieDinges video of a Syrian man livestreaming the Paris riots; cpasdeslol_X video of a masked youth throwing an iron bar at police (none public figures)
EXTRA_PRIVATE |= {'2111748525969002834','2111736618529042487','2111529197911130589','2069352274523267105'}  # 1000Z: aisha47864 story about a man she messaged; chastiefoul post about a married couple in a shop; jon_delorraine video of a man climbing the Joan of Arc statue in Paris; indicmawntee reaction video of people who are not identified (none public figures)
DESK_OVERRIDE_RUN.update({'2111748525969002834':'life','2111736618529042487':'life','2111529197911130589':'world','2111864477876703252':'world','2111669202176086523':'world','2111234734521192648':'world','2111510726095319233':'justice','2112110182230856024':'entertainment','2111863617813696543':'entertainment','2111873409751896068':'entertainment','2106776239897792559':'offbeat','2112091428633583759':None,'2111860935002562944':'gaming','2111903537961779488':'entertainment'})  # 1000Z desk fixes
DESK_OVERRIDE_RUN.update({'2111247627748565091':'ai','2111512968638660617':'world','2111880301710630939':'internet','2111316522098733078':'science','2111889248160813527':'world','1985050234213294345':'life','2111911798622581175':'entertainment','2111884967978643726':'offbeat','2111569977803174059':'world','2111805021432004830':'music','2112080500361760920':'sports','2111944472443404566':'sports','2111802274112524623':'politics','2111933949911892413':'sports','2111997816763535372':'entertainment','2111804500373836189':'tech'})  # 0905Z desk fixes
EXTRA_PRIVATE |= {'2109930144236277916','2110117316549808302'}  # 0802Z: NotAvgLiberal video of a woman attacked at a Trump rally and the ProudSocialist post reusing it (private person)
DESK_OVERRIDE_RUN.update({'2111871743594049640':'entertainment','2111113648089547186':'entertainment','2111771125323796608':'gaming','2111776452211359934':'sports','2111862377163407395':'world','2111816123800780994':'politics','2110117316549808302':'politics','2112070071401238607':'ai','2111931469933207665':'sports','2111895137345577317':'internet','2111601256003150156':'life','2111796810889204064':'tech','2109569855435555106':'music','2111840030193029461':'justice'})  # 0802Z desk fixes
EXTRA_PRIVATE |= {'2111267743471407426'}  # 0404Z: tIefirstone clip mocking a couple kissing on TikTok live (not public figures)
OLD_VIA_CHAIN |= {'2071694033160638478'}  # 0404Z: June 29 Shams post reached through a June 29 reply and quote chain from a post read this run
EXTRA_PRIVATE |= {'2111724384620830784','2111642809769832950'}  # 0006Z: Duke medical staff member shoved by a player (not a public figure) and the player himself (college athlete, public status unclear)
EXTRA_PRIVATE |= {'2111198620187804119','2111546670559449421','2111302593183969363'}  # 1904Z: nypost photo of the dead college student (private person); BradBeringer video of a woman in her family's store in France (same video as 2111544142979604538, flagged earlier)
OLD_VIA_CHAIN |= {'2038807290422370479'}  # 1904Z: March 31 axios post reached through a March 31 quote and reply chain from a post read this run
DESK_OVERRIDE_1807 = {'2111856962044416268':'sports','2111734532483207284':'justice','2111525848310521868':'world','2111562104784519183':'world','2111683964721037767':'tech','2111842588126818619':'tech','2111278766152700208':'ai','2111503434008731795':'gaming','2111180818542698889':'sports','2111624429474136101':'music','2111751793386438949':'sports','2111578871921274962':'justice','2111861770444739018':'defense','2111652303854076191':'defense','2111689401051103636':'defense'}
DESK_OVERRIDE_RUN.update({'1987550101703909532':'politics','2111836745956196455':'entertainment','2112133876755972376':'world','2109621234363138380':'music','2111896370726514827':'life','2111200984005558653':'life','2112002495723487605':'politics','2112328475852095678':'music'})  # 1200Z desk fixes: DataRepublican State Department thread is politics; Odyssey box office is entertainment; Paris cafe protest clip is world; ianprin Music Core clip and EXO Suho story are music; Saladino travel and Yoruba gele photo posts are life; Texas trans student mailer is politics
EXTRA_PRIVATE |= {'2112401158488686875','2112483747169730946','2112318424596770880','2112133876755972376','2112388948563554668','2112384143283892720'}  # 1200Z: Planet Fitness member and staff in Wisconsin (WallStreetApes, GuntherEagleman) and gym staff (ImMeme0); WelcomeTheGulag video of protesters at a Paris cafe; Amy Acton's mother in the campaign ad (wcdispatch, still_hustling), public status unclear
EXTRA_PRIVATE |= {'2112340739476918543'}  # 1310Z: nicksortor video of protesters at the Kansas rally (not public figures)
DESK_OVERRIDE_RUN.update({'2112229171649028401':'sports','2111815190475833797':'internet','2112243445687321081':'ai','2112476496283775135':'ai','2111864861281952076':'politics','2112248629797031960':'sports','2112340739476918543':'politics','2112211785566843225':'disaster'})  # 1310Z desk fixes
EXTRA_PRIVATE |= {'2112524102871195680','2112377799306608912','2112394437657846018','2112347348756246798','2112372595823935746','2112110146197291483','2063905475670769894'}  # 1401Z: samstein post on Amy Acton's mother (public status unclear, as in 1200Z); Gitmo99 bullhorn video and the 4AlphaZulu reply naming the man punched (people not public figures); viewsceo and FearedBuck videos of the unnamed Kick streamer being hit; NotFarLeftAtAll video of UK police officers; celtic_jaime video of children
DESK_OVERRIDE_RUN.update({'2112095823832170792':'entertainment','2111919880458895373':'sports','2111954155967569934':'sports','2112401161940529303':'gaming','2111085682441789487':'internet','2104741684118470865':'sports','2112484178230976672':'sports','2063905475670769894':'life','2111862469308318028':'life','2112110146197291483':'world','2048414778645709117':'internet','2112318290194289144':'internet'})  # 1401Z desk fixes (pinkponypearl Minecraft YouTuber post to internet): Jadeeslike Avengers gif to entertainment; geglobo and livesfoot Neymar clips, espn Jalen Hurts hit and ballondor vote post to sports; Umamusume concert cancellation to gaming; South Park drawing meme and SomaKazima2 airport clip to internet; kids cardboard game and one-sided love posts to life; UK police video to world
EXTRA_PRIVATE |= {'2112341856256409759','2112528922533617763','2112466882695708933','2112326710817419527'}  # 1502Z: nicksortor post naming a Kansas man arrested over a threat (pile-on); OhioCrawler and RonFilipkowski posts of the Ramaswamy ad featuring Amy Acton's mother (public status unclear, as in 1200Z/1401Z); TimesNow video of a child nearly swept away by waves
DESK_OVERRIDE_RUN.update({'2112351525418971527':'sports','2111992958245560476':'sports','1657868448876179462':'sports','1751005013931966797':'sports','2112349532734533893':'sports','2111820034485948922':'internet','2111860585285501121':'life','2112040304341598312':'world','2112341856256409759':'politics','2112428493166289231':'music','1972837043735793926':'internet','2112466882695708933':'offbeat','2112364654991409339':'politics','2112502543947325773':'science'})  # 1502Z desk fixes
EXTRA_PRIVATE |= {'2112267540109971635','2112350913138733283','2112505876292468997'}  # 1600Z: hoodwild_ video of two people who are not public figures; NBA video showing Steph Curry's young daughter (a minor)
DESK_OVERRIDE_RUN.update({'2112267540109971635':'internet','1979529935732752513':'music','2112274609231843785':'world','2112314341626368200':'offbeat','2111977713040773632':'life','2111977981593960742':'life','2112256851937231275':'world','2112015249448812708':'internet','2112204171118321728':'world','2001704140284522778':'entertainment','2112483018719851001':'entertainment','2111954251316691297':'world','2112434308258386086':'music'})  # 1600Z desk fixes
EXTRA_PRIVATE |= {'2069089007372259330','2112216476572590130','2112469093882183755','2112318129481097374'}  # 1705Z: dudeetalks rock-paper-scissors video with a stranger; ImtiazMadmood and visegrad24 videos of a French woman threatened during the riots (not a public figure; the activist answering her may not be one either); CNN post showing and naming a 1-year-old boy (a minor)
DESK_OVERRIDE_RUN.update({'2069089007372259330':'offbeat','2108438196086345909':'world','2111787520900112759':'world','2112469093882183755':'world','2112216476572590130':'world','2112402935611044277':'world','2112198022255768028':'gaming','2112521717251739732':'gaming','2112484218014237122':'gaming','2112515545270567223':'gaming','2112442741925773530':'gaming','2112318129481097374':'justice','2112416097131528475':'music','2112386084118364627':'sports','2112283824717750401':'markets','2110564479742120079':'business','2112583304738210216':None,'2112557237508169956':'world','1732574492763840759':'politics'})  # 1705Z desk fixes
EXTRA_PRIVATE |= {'2112260000676810851','1616029260308951045','2103928595332960378','2112248723715629158','2112368033759207526','2112554718673203323','2112601213711602137','2112600118646001896'}  # 1804Z: Eng_china5 and tomato044apd videos of a 10-year-old boy in a youth sumo match (a minor); gwskays video of fast-food workers set to a Tinashe song; MarieGentric shop CCTV of the Paris riot looting; KaleiRenay screenshot of a Threads post by a private account; caroljayyyy screenshot of a group chat naming a friend; BrownSugarTae and treyoctober photos of themselves for the #MillionDollarFIT watch party (none public figures)
DESK_OVERRIDE_RUN.update({'2112260000676810851':'sports','1616029260308951045':'sports','2103928595332960378':'music','2112248723715629158':'world','2112554718673203323':'music','2112601213711602137':'entertainment','2112600118646001896':'entertainment','2112598550106222774':'entertainment','2112198138744451469':'music','2112300237511696666':'music','2112527917804642583':'world','2112589222855217167':'world','2112559638579499258':'business','2112539349359435960':'entertainment','2112546472461750486':'world','2112266824276652250':'world','2112420020672504209':'gaming','2112272574826832117':'sports','1890725905338933484':'entertainment','2052188806065816018':'entertainment','2046396157752910046':None,'2107203497037070823':'internet'})  # 1804Z desk fixes
EXTRA_PRIVATE |= {'2112568191616516521','2112546621036913012'}  # 1905Z: libsoftiktok post naming a private schoolteacher and the school that now employs her; knafaesque screenshot of a private Reddit user's post about his marriage (none public figures)
DESK_OVERRIDE_RUN.update({'2112593866461216942':'politics','2112523919282573650':'politics','2112282717845098608':'world','2112593187139416244':'world','2112600761762717997':'music','2112603906723487744':'tech','2112607002367000966':'music','2029383266642608395':'entertainment','2029383377569358010':'entertainment','2111725991164797094':'world','2112546621036913012':'life','2112371354607739311':'life'})  # 1905Z desk fixes
EXTRA_PRIVATE |= {'2106845140228985007'}  # 2007Z: sleezedown reaction clip of a woman exhaling smoke (not a public figure; when in doubt, flag)
DESK_OVERRIDE_RUN.update({'2092481904763429262':'tech','2112287023444709845':'world','2112544044123402724':'gaming','2112529983206019246':'gaming','2111951892716703924':'entertainment','2112281656266559956':'medicine','2108940648267284671':'sports','2112231064663887996':'entertainment','2112154870061076917':'sports','2106845140228985007':'internet','1873587927600812164':'sports','2112351075546050760':'sports','2072703253192544616':'sports','2112625600846508438':'sports','2112625296541372714':'sports','2112627608546631779':'sports','2112629693501354127':'sports','2112630274974523883':'sports','2112630041985131000':'sports','2112587890001674414':'world','2108941893971161361':'sports'})  # 2007Z desk fixes
EXTRA_PRIVATE |= {'1848792641011335395','2110265839773679693','2112111102653804870'}  # 2059Z: BrukeFasil post about his aunt waking from a coma (private family member); SharronMcKenna5 auditingcops video of a police officer (not a public figure); springfield1952 photo of the Paris shop owner during the looting (private person, as the MarieGentric CCTV post)
DESK_OVERRIDE_RUN.update({'2112378472823763384':'sports','2112533057991262562':'life','2112282913291018550':'politics','2102105172008645094':'offbeat','2112111102653804870':'world','2110265839773679693':'justice','2112528089297117401':'entertainment','2112529264826265679':'sports','2112310167639650805':'entertainment','2112306851597447456':'internet','2112584983000858809':'business','2112571545688093157':'politics','2112544764729909718':'entertainment','2112649648641065013':'sports','2112637057768345893':'sports','2112499290191110373':'sports','2112649692404453819':'sports','2112644599256666578':'sports','2112643771339096316':'sports','2112641331294060879':'sports','1848792641011335395':'life','2095633520978743400':'politics','2112578522673774963':'politics'})  # 2059Z desk fixes
EXTRA_PRIVATE |= {'2112076035172839532'}  # 2207Z: ThereSofie post on credit cards (not clearly a public figure; when in doubt, flag)
DESK_OVERRIDE_RUN.update({'2095487220195135551':'offbeat','2092753734753223145':'sports','2092967568214528158':'sports','2101076358038433954':'sports','2112232220114997700':'entertainment','2112501779317600412':'world','2112239978751377419':'justice','2112302784397627616':'gaming','2112549388102828055':'sports','2112503744898400401':'world','2112270563171270737':'sports','2112076035172839532':'business','2111287863908413683':'internet','2112587112176398808':'entertainment','2112616322169213297':'politics','2112659327211229668':'sports','2112655024396616145':'sports','2112654559403503940':'sports','2112655390525493654':'sports','2112653099500286299':'sports'})  # 2207Z desk fixes
skip_nsfw |= {'2112452474598768874','2112467291455594610','2112644950324133893','2112115881006575910'}  # 2258Z: likely paid (hasibiro_maga Kim Jong Un coma claim: 3,573 likes and 98 replies on 8.5M views); sexual text (rae_chloe133 HIV question); lledrok Paul George joke with a racial slur (as the 2207Z BronGotGame post); isfjcutebear 'skin this color' caption on a private person's selfie (racial mockery of a private person)
DESK_OVERRIDE_RUN.update({'2112455164607049814':'world','2112245886776672428':'internet','2111168500672729583':'internet','2111945177266840055':'entertainment','2108797791791436061':'tech','2112619988926300257':'entertainment','2112634886070919426':'ai','2112531698458018020':'entertainment','2112605839659823372':'sports','2112008762366230548':'music','2112666467712073815':'business','2112659348031955309':'sports','2112624312968691976':'sports','2112645105383587889':'sports','2112657794084254173':'sports','2112658810271899694':'sports'})  # 2258Z desk fixes
skip_nsfw |= {'2074522898883125567','2026806142089691397','2112255669764252103','2086943981934346474','2111861115508420917'}  # 0006Z: DeadMansRequiem quote post that pulls out and repeats a racial slur (as the earlier slur skips); PlayboiMontana1 sexual text; msertii post promoting explicit sexual film scenes (Drummond stream); likely paid (acervonicoo Aug clip of a private woman: 6,477 likes and 17 replies on 5.4M views); ad (FatKidDeals Top Golf promo-code deal)
skip_nsfw |= {'2112626642803642478'}  # 0006Z: PopBase post on the Ramaswamy ad describing Amy Acton's sexual abuse as a child, left out under the minors rule as in 1705Z
DESK_OVERRIDE_RUN.update({'1754149811526524934':'sports','2095188850767282357':'politics','2074501740339118180':'sports','2112264330288734349':'music','2111935197084029420':'world','2112246941983903909':'internet','1737812664968233067':'entertainment','2112161273676804575':'internet','2112591790536569131':'world','2112415434784084139':'internet','2112589692377939991':'tech','2112259990199107975':'music'})  # 0006Z desk fixes: Shaq clip and Celeste Amarilla/Mbappe post to sports; WearForbidden Conservative Inc clip to politics; Cardi B Tiny Desk post and Mr. Eazi rent quote to music; danwootton BBC/France riots post and Sky News antisemitism report to world; miyarah_ meme, FamouslyGarnet AI clip and Stevetweetzz1 Grok-bait image to internet; One Piece cosplay to entertainment; Dexerto Spotify family-plan post to tech
skip_nsfw |= {'2112526015570567609'}  # 0059Z: Iam_xolietoxic post about a girl who dumped her 10-year-old son, left out under the minors rule
skip_nsfw |= {'2089422978102513798'}  # 0303Z: TroTwink 'Testing My Limits' video from an adult-content account (sexual, old origin in the "is" repost stream)
skip_nsfw |= {'2066462864441770395'}  # 0458Z: you_me620 sexual bait post with explicit wording (old origin, sexual)
skip_nsfw |= {'2113343621164310867','1746547721153241250'}  # 0606Z: drhossamsamy65 'Warning 18+' post on Aaron Bushnell's self-immolation (self-harm, graphic); avadamidia old Lil Nas X MONTERO video post, likely paid (650 followers: 192 likes and 3 replies on 2.46M views)
skip_nsfw |= {'2113502808507040081'}  # 0707Z: Teslaconomics Grok Bot post, likely paid or promoted (567 likes and 86 replies on 17.8M views), as the 1203Z Teslaconomics post
skip_nsfw |= {'1783463875498721583','1881090083996172648','2113414527106843129'}  # 0801Z: TOP_GUYS_ 'picking up rich influencer ... bringing him back home' clip (sexual bait); ParisEighty '3 Strikes Full Movie' (likely spam or paid: 481 likes and 8 replies on 5.1M views); Teslaconomics Grok Bot order post (likely paid or promoted: 326 likes on 587K views, as the 0707Z Teslaconomics post)
skip_nsfw |= {'1914163204516725198','2112969377515807047','2113473131914445206','2080307444790566994'}  # 0905Z: PR0T0WH0RE lingerie thread (sexual, explicit display name); catainvda 'Claim your $15' airdrop (crypto spam); minchoi Grok Bot '10 wild examples' post (likely paid or promoted: 298 likes and 52 replies on 625K views, as the Teslaconomics posts); HorowitzCenter election survey solicitation from July (likely paid, reached through the Patriots trend)
EXTRA_PRIVATE |= {'2112938649675526443'}  # 0801Z: krougee post about a private family's child flexing on TikTok (private person)
skip_nsfw |= {'2113333542256066592'}  # 0403Z: men_who_yearn '[🔞]' adult fan-fiction post in the "Caleb" trend stream (sexual)
EXTRA_PRIVATE |= {'1862223974970601746'}  # 0059Z: allreactionvids video of a child crying at a Thanksgiving table (not a public figure)
DESK_OVERRIDE_RUN.update({'2112623974614180322':'justice','2112141670015754265':'entertainment','2073117294046199889':'entertainment','2102250268377420039':'world','2102244051231842385':'world','2011862588557263119':'music','2112550220865110427':'politics','2112320365523530073':'internet','2105417746225799604':'world'})  # 0059Z: rawsalerts duct-tape arrest is justice; Baahubali clips are entertainment; Japanese PM New York arrival posts are world; PinkPantheress/Zara Larsson video is music; JD Vance midterms clip is politics; bookmarks joke is internet; Foreign Policy Trump/Xi piece is world
skip_nsfw |= {'2092368960167551120','2111920560196538742'}  # 0203Z: sexualised body-paint mirror clip (angelferxoxo 'new movie coming soon', Aug 2026 origin, old_content); sexual text (MouchettesCuck cuckold compilation post)
skip_nsfw |= {'2112659061183315977','2112702928049824118'}  # 0308Z: likely paid (JEJTron, 318 followers: 12 likes and 1 reply on 695K views, re-upload of an NBA Central clip); likely paid (ShowCaseShabazz, 26,873 followers: 281 likes and 9 replies on 761K views in under 3 hours)
EXTRA_PRIVATE |= {'2112332941418545314','2112426982809940160','2112525993478889604'}  # 0203Z: DrewPavlou screenshot of a non-public user's post on the Paris scalding-water video and the thesoypill quote of it (pile-on on a person not a public figure); visegrad24 post naming a French activist from a TV debate (not clearly a public figure)
DESK_OVERRIDE_RUN.update({'2103947562395005061':'sports','2112003272403730727':'sports','2111929012079542489':'sports','2112575909706559809':'sports','2112702994999644654':'sports','2112426982809940160':'world','2112332941418545314':'world','2112308977493008844':'entertainment','2112578558421787104':'sports','2110174042603057376':'sports','2112525993478889604':'world','2112676648751411649':'sports','2112656917000774019':'sports','2112683007392051566':'sports','2112617835738325354':'politics','2112702308102414741':'gaming'})  # 0203Z desk fixes
import glob as _glob
DESK_OVERRIDE_RUN.update({'2112589946762756428':'gaming','2111422046668210622':'sports'})  # 0308Z desk fixes: LeagueOfLegends Mel update to gaming; AdamSchefter Jalen Hurts post to sports
PRIOR_DESK = {}
for _c in sorted(_glob.glob(f'{REPO}/capture/2026/10/*/*.json')):
    if _c.endswith('0003Z.json') and '/25/' in _c: continue
    for _p in json.load(open(_c))['posts']:
        PRIOR_DESK[_p['id']] = _p.get('desk')
DESK_OVERRIDE = {'1863556711875015074':'politics','1863586924151419012':'politics','1863763498251006229':None,
    '2111546989280186852':'sports','2111507158215057620':'tech','2111171211254190393':'entertainment','2069374923190182098':'music','1815122486645924270':'politics','2108838028777005102':'world','2111484581845311694':'world','2111219056468480460':None,'2070878721368858750':'entertainment','2111079839352402226':'gaming','2111481025289441471':'world',
    '2111072036089131094':'sports','1604764832754171905':'music','2110462362343866599':'sports','2111506579128480242':'sports','2071357848861147244':None,
    '2111037738879218043':'life','2099543565777195438':'music','2109271552378220789':'tech','2109116746753880192':'tech','2110635620330811758':'life','2111328130069889351':'life','2111076953382150189':'politics','2111319909594718624':'entertainment','2110862266593677675':'world','2111027214011519094':'world','2111147613814960514':'entertainment',
    '2111493774753058898':'sports','2110789095257747679':'internet','2027402738292691197':'internet','2111082742771286359':'music','2110286618519011391':'ideas','2110684832804331913':'ideas','2110244744362185107':'politics','2111430430369206288':None,
    '2111177307905995079':'justice','2111393640366936204':None,
    '2110960095597142265':None,'2111209208012210409':'ai','2111131677351432197':'tech','2111087026330374516':'entertainment','2111094888033132859':'gaming','2111449904984056138':'world','2111462671878918556':'music','2110752265846091881':'politics','2111008131501170884':'life','2110703535423922663':'entertainment','2111136203496116704':'internet','2110744206952075514':'music','2111071770010673497':'world',
    '2111375640717033777':'ai','2111142161584628060':'ai','2111080152197476739':'gaming','2110803630022422950':'entertainment','2110349551022248244':'gaming','2111295582895808806':'internet','2111207677527310645':'ideas','2111360445642596678':'tech','2110977536897528137':'music','1895010422689866009':'entertainment','2111227821074845951':'life','2111091095258169786':'entertainment','2110924190362595396':'internet','2110796301420159124':'politics','2074167715460165757':'ai','2110752082399555799':'politics',
    '2111148091378409488':'tech','2111297643754275002':'world','2015835655012508016':'world','1993051980982632828':'politics','2110694702747934965':'sports','2110739170041991379':'sports','2110639247744975208':'music','2111354746548433173':'tech','2111354696854114702':'tech','2110805296662614448':'world','2110536137961771506':'world','2111081480822940046':'entertainment','2111000798972846279':'entertainment',
    '2056835812772196578':'sports',
    '2110402979681771963':None,'2111044250351878534':'entertainment','2111284146894942653':'music','2110318389441044630':'internet','2110789807248912648':'internet','2111045153565626645':'gaming','2111162211318067638':'politics','2111189453880406301':'entertainment','2110903725116014610':'tech','2110441463599542506':'politics','2110398367201145273':'politics','2110803056606720218':'internet','2111058554878853430':'sports','2111276969690038485':'politics',
    '2111218408759136514':'politics','2111075443176825233':'world','2110511855731159239':'tech','2110483188174946476':'tech','2110942875290935307':'disaster','2111279949336179053':'sports','2111262985360740675':'internet','2111304230162329908':'internet',
    '2110574422663053327':'gaming','2005744130287129071':'music','2097755300841345509':'gaming','2097760872374628405':'gaming','2111145709231595603':'justice',
    '2110941338107609441':'sports','2108734997280477436':'sports','2111147643267338289':'sports','2110847290277797952':'entertainment','2110830556565148135':'entertainment',
    '2109931620195041418':'entertainment','2110863058029474257':'internet',
    '2110759922430513248':'sports','2001049424370225656':'sports','2111031006090104892':'sports','2110933466053562557':'tech','2110821237517959503':'internet','2108874034264133904':'music','2110619179900424489':'music','2110282178638831645':'music','2110884776400097494':'music','2111156654850847230':'defense','2111199331437207758':'disaster','2111217414297784660':'disaster','2111034471025684619':'gaming',
    '2081684964131684716':'science','1901277993336492346':'science','2106238793942466598':'sports','2109810478692376934':'entertainment','2111165738836717980':'ai','2111170548038324695':None,'2110743912885489960':'tech','2104344921322733831':'sports','2110919752134906074':'music','2111156124997263405':'defense',
    '2089842388508287245':'internet','2110003290805313596':'entertainment','2110781791166472415':'sports','2111030861655064724':'sports',
    '2110834423583404430':'entertainment','2098333859020484669':'internet','1814150160831619537':'music','2110810888433500323':'politics','2110932051235115120':'tech','2110910422358561071':'tech','2110808771291152562':'internet','1630727685021265920':'internet',
    '2110450339128430774':'entertainment','2110754049490665911':'sports','2110050615552327790':'entertainment','2110909653206942082':'internet','2109631263711629483':'gaming','2111114739460051062':'sports','2110818982924341270':'entertainment','2111127940742476115':'sports','2111131160348688395':'business','2111131436191199660':'tech',
    '2110954913694130378':'entertainment','2110825417066377510':None,'2110537880108216801':'politics','2110763927953121660':'music','2110940230622892414':'music','2110477345270169664':'entertainment','2111049689491480719':'tech','2110907035571401174':'tech','2062739940178551251':'world','2110879358852411634':None,'2041802128994275586':None,'2110435719865061380':'tech','2111122942230749379':None,'2110845021394264338':'politics','2110971985417441512':'ai',
    '2110772234717397000':'life','2110906114602635463':'tech','2110936798172229880':'tech','2110972416751186421':'world','2110467314785349871':'music','2110920330139038106':'tech','2110570657339834695':'politics',
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
    '2110913107094606330':'science','2109667487650619713':'music','2110926164306931860':'tech','2110905474484940939':'tech',
    '2110948640281800882':'life','2110741566545608796':'entertainment','1695939486415307058':'entertainment','2110837879794524263':'justice','2110651029482074556':'life','2110761858231935251':'business','2110904608398934084':'tech','2110780938435379238':'politics','2110676456690811083':'internet','2110360011205730708':'world','2109310806005596521':'ai',
    '2110594098352800162':'ai','2110400563934294425':None,'2110462043103113320':'gaming','2110565847576310226':'sports',
    '2110874498668884187':'sports','2110830102959554851':'entertainment','2110761364352598079':'entertainment','2110666080578404535':'world',
    '2110921873722868066':'tech','2110902370234450271':'tech','2110867093201781106':'ai','2110771542825304257':'ai','2110679031469560261':'gaming',
    '2110768815420080472':'internet',
    '2110928280912081212':'tech','2110917099648381383':'tech','2110472677823807767':'entertainment','2110773545131495781':'entertainment','2110836428100014157':'world','2110664107007631421':'music','2110369698831536172':'gaming','2110469707581346138':'gaming','2106567984575877137':'sports','2110027949302821067':'sports','2110887296606052440':'world','2110655209823424942':'entertainment',
    '2110906012857454976':'politics','2110883461116379287':'gaming','2110440330793504853':'gaming','2110768301437550990':'music',
}
DESK_OVERRIDE.update({"2111516397503176756":"politics"})
DESK_OVERRIDE.update({'2111399477370077668':'world','2111415364710256755':'gaming','2111602332257472627':'justice','2110591412639240317':'music','2111600390567498207':'world','2111627951691182339':'world','2111680761770180960':'world','2110379121431937028':'politics','2111488658037453132':'disaster','2111158614845202586':'business','2109565462803894752':None,'2111383925062807655':None,'1998040874551501112':'entertainment'})  # 1101Z
DESK_OVERRIDE.update({'2111623932792947099':'sports','2111491975316734378':'world','2111493912422453407':'world','2111584497921642726':'justice','2110827917420982707':'justice','2111573432827527557':'justice','2111444320846798871':'justice','2110844715964813348':'life','2111516482199052374':'sports','2111689302090604611':'music','2111304937380753802':'politics'})  # 1004Z
DESK_OVERRIDE.update({'2111625583662637329':'politics','2111522760774066415':'politics','2109587133283316124':None})  # 1200Z
DESK_OVERRIDE.update({'2111736037710164229':'sports','2111615865435173342':'politics'})  # 1406Z
DESK_OVERRIDE.update({'2111560885013471381':'sports','2111698792944656488':'gaming','2111540297893122538':'entertainment','2111582845667856388':'world','2111540790463697380':'world','2110780634473873622':'entertainment'})  # 1303Z
DESK_OVERRIDE.update({"2111201301703115082":"sports","2111441751877591418":"music","2111390377181597789":"music","2111512574818750759":"world","2111544230170722708":"world","2110850007620534323":"ai","2109397852543979896":"sports"})  # 0906Z
DESK_OVERRIDE.update({"2111629620164329812":"justice","2111654304104812706":"sports","2111513816399819124":"sports"})  # 0506Z: Wichita soccer-game vehicle incident (driver identified by police); ESPN ACC replay-centre clip (was gaming in an earlier capture, corrected); Harry Kane goals  # 0400Z: Trump rally in Kentucky, reached through the Kentucky trend stream

DESK_OVERRIDE.update({'2111610602921861120':'sports','2111123479471030752':None,'2110915161049706686':'disaster','2111253074509705350':'science','2111252844171162082':'science','2111263086648926574':'sports','2111471081429025238':'sports','2111415316588744815':'sports','2111581135499411662':'world','2111591844496720039':'world','2111549041855410443':'world','2006432716632604832':'entertainment','2111611563417252190':'life','2111218861530108329':'sports','2111162532031517139':'world','2110021742106120550':'internet','2111143997770973227':'politics'})  # 0802Z
DESK_OVERRIDE.update({"2111628885683052685":"sports","2111435501836120075":"sports","1990795167096541422":"sports","2111597900849676463":"sports","2111294913208107075":"internet","2111145630059868671":"entertainment","2111585628336918796":"world","2111462326452834484":"world","2111536449107665153":"world","2111623892477313136":"sports","2111448202146721855":"world"})  # 0600Z

DESK_OVERRIDE.update({'2111598298033176659':'justice','2111223161337561568':'sports','2111621671476207670':'sports','2110812372009189612':'world','2111500353338269801':'life','2111557892406902930':'world','2049640265900605908':'entertainment','2110114878685921775':'offbeat'})  # 1709Z: Kansas soccer-game truck crash (was gaming by keyword); NFL primetime post; RGIII on a Duke football injury; Lula photo joke (Brazil); power-outage household clip

EXTRA_PRIVATE |= {'2111927284324295025'}  # 1203Z: RafaelSereti video of two tourists caught in the Paris riots (private people)
DESK_OVERRIDE_RUN.update({'2111927284324295025':'world','2111905094543524003':'world','2111904110693810595':'world','2111574144265629958':'world','2111865681658687737':'politics','2111477585461039241':'tech','2112080069732479400':'internet','2067322220452421929':'music','2111568935271174470':'internet','2111921509929464029':'politics','2112110832502882566':'entertainment','2112113841517535479':'entertainment','2112109435770536418':'entertainment','2112087262531854542':'sports','2112107146124956079':'sports','2112113784177201154':'entertainment','2111905772942897164':'entertainment','2112032898408910934':'entertainment','2112122081966276678':'life','2112102326903169370':'life','2112127156482424892':'life','2112055824176579021':'life'})  # 1203Z desk fixes
DESK_OVERRIDE_RUN.update({'2111536361790734699':'world','2112076928098181448':None,'2111591935521718517':'politics','2112071991700107756':'offbeat'})  # 1203Z desk fixes (2)
EXTRA_PRIVATE |= {'2111894041201651785','2111418123861782625'}  # 1302Z: A_Oberdorff video of Paris residents defending a shop during the riots; RabbiJeffx post about a woman and her mother (private people)
DESK_OVERRIDE_RUN.update({'2110324984740487346':'sports','1750627602648219996':'sports','2110350253467812268':'sports','2111829939624300698':'ai','2111797049826185627':'world','2102491056306819124':'entertainment','2111807417029976192':'life','2111164698544779507':'life','2111205980201795738':'life','1979628118194430361':'politics','2111894041201651785':'world','2111916007732166793':'life','2111979993857474861':'life','2111966404031205401':'life','2111976813866226076':'life','2111942730540814731':None})  # 1302Z desk fixes
EXTRA_PRIVATE |= {'2111974892694306919','2112114636002644055'}  # 1410Z: merveesuyu dietitian post doubting that a woman gave birth (pile-on on a person who is not a public figure)
DESK_OVERRIDE_RUN.update({'2111974892694306919':'internet','2110571012546773445':'gaming','2112016006331945286':'gaming','2111453539029712975':'tech','2111968079630545126':'life','2111599659307225492':'internet','2085172962018353363':'politics','1732149328779571313':'gaming','1861338962448859299':'music','2112114636002644055':'world','2111216488367685684':'gaming','2112166891208753234':'music'})  # 1410Z desk fixes (LucAuffret video of tourists at the Louvre blockade is world, flagged private: tourists and students are not public figures): Uma Musume concert visa notice is gaming; Barbara Palvin Victoria's Secret runway clip is life, as the other #VSFashionShow posts; the 'French people' clip is an Assassin's Creed Unity cinematic used as a meme (internet); GTA VI Trailer 1 is gaming
EXTRA_PRIVATE |= {'2111883542955282746'}  # 1519Z: ATmediaa video of a Paris shop owner asking rioters to stop (person who is not a public figure)
DESK_OVERRIDE_RUN.update({'2112044977937387771':'music','2105371838897668294':'sports','2112187727399489688':'sports','2055330663608295794':'world','2110836751937728713':'world','2111883542955282746':'world','2008712361272877184':'politics','2112072540147355711':'world','2111857588858147149':'markets','2111612653106053321':'music'})
EXTRA_PRIVATE |= {'2112141825284923755','2077108750347821550','2111522024359071852'}  # 1620Z: CISFHQrs video of a metro passenger apprehended; ABC clip of a Texas woman whose pole flooded her flat; QuantumGuard17 clip of a man subdued at a Senate hearing (people who are not public figures)
DESK_OVERRIDE_RUN.update({'2112186983389028561':'sports','2112184806213931268':'sports','2112188049576939927':'sports','2111979753188311343':'sports','2111850399762141328':'politics','2111910209060819202':'politics','2112139042535911513':'world','2111804043857457377':'world','2112141825284923755':'justice','2077108750347821550':'offbeat','1606877397197983745':'entertainment','2111518835794731469':'ai'})
EXTRA_PRIVATE |= {'2111583405716672749','2111396689747616021','2112135848275620236'}  # 1803Z: DrewPavlou video of a video game shop owner attacked by rioters in France; lu9jcg 'no hope for women' video mocking women who are not named; Cfc_Sean7 photos of Cole Palmer's sister from her TikTok (public status unclear)
DESK_OVERRIDE_RUN.update({'2112217914673959115':'politics','2112111545933267288':'entertainment','2111966024257978556':'life','2112034756108104173':'life','2112232199177068907':'sports','2111396689747616021':'internet','2111583405716672749':'world','2111959595081990509':'internet','2111888011831202274':'internet','2111982959276478703':'world','2112135848275620236':'sports'})  # 1803Z desk fixes: Musk Talarico post is politics; GMMTV events post is entertainment; Bella Hadid show post is life, as the other Victoria's Secret show posts; PopBase Evaluate Your Life Day is life; Ronaldo suspension and Cole Palmer's sister are sports; joint timelapse and its quote, and the women video, are internet; France shop owner video and Ro Khanna youth-protest post are world
EXTRA_PRIVATE |= {'2112106419235508545'}  # 1803Z: GeNimco video asking why a man treated a woman that way (people not named as public figures)
DESK_OVERRIDE_RUN.update({'2112106419235508545':'internet','2111850986604003575':'entertainment'})  # 1803Z: Bleach character post is entertainment
DESK_OVERRIDE_RUN.update({'2087652244837818677':'sports','2087619460404273603':'sports','2111977266523586834':'life','2112187824875196890':'sports','2111946609814536367':'gaming','2111996266087428308':'gaming','2112238252564554081':'entertainment'})  # 1909Z desk fixes: Michael Penix doctor posts are sports; Kylie Jenner runway post is life, as the other Victoria's Secret show posts; AzPetrich football-death post is sports; PC gaming posts are gaming; Netflix FROM post is entertainment
DESK_OVERRIDE_RUN.update({'2111873161826308150':'internet','2112194302478819343':'internet','2112134620212764884':'world','2112187914314567715':'sports'})  # 1909Z: Pokimane France protest post is internet; CourtneeHendrix clip is internet; Paris shop manager video is world, as the other France riot posts; SleeperNFL Jalen Hurts post is sports
EXTRA_PRIVATE |= {'2112194302478819343','2112134620212764884'}  # 1909Z: CourtneeHendrix video of a man who 'might get fired' (not named as a public figure); ThaisEscufon video of a shop manager during the France riots
DESK_OVERRIDE_RUN.update({'2111746714734403748':'offbeat'})  # 1909Z: haunted-house cats cartoon is offbeat
DESK_OVERRIDE_RUN.update({'2111810683763654971':'sports','1974849468232343585':'politics','2111989703780315648':'world','2111830186274488453':'entertainment','2111107062511837328':'gaming','2112227588538036712':'sports','2112204973199045050':'entertainment','2112203711305154613':'justice','2111919217733779683':'justice','2112231563811561851':'politics','2112184651594740103':'world'})  # 2000Z desk fixes (TruthTrumpPost Macron Gulf tour post is world, as the other France posts): sports-popularity chart and Jalen Hurts timeline are sports; Acyn Johnson-Brennan clip is politics; Gen Z protests clip is world; Whalefall box office and James Gunn DCU casting are entertainment; PC gaming post is gaming; Kansas soccer-game truck posts are justice, as in 1709Z; Ken Paxton rally post is politics
EXTRA_PRIVATE |= {'2112231563811561851','2112203711305154613','2111919217733779683'}  # 2000Z: CattardSlim post about a TikTok influencer removed from a Paxton rally (public status unclear); MattWalshBlog and TMZ posts about the Kansas mother whose truck hit a youth soccer game (private person)
DESK_OVERRIDE_RUN.update({'1787980745748754838':'internet','2092281095693774887':'life','2112083831159505078':'life','1863594151155036299':'sports','2111692144251748815':'internet','2111277768172548212':'science','1994770561051070791':'music','2112182806122021255':'sports','2112076531506041286':'gaming','2112038533401551203':'world','2111977872416006380':'sports','2111856689167147042':'medicine','2112192954378961335':'politics','2111949798697840769':'entertainment'})  # 2100Z desk fixes: Family Guy clip entertainment; Peter Parker meme internet; chef onion clip life; Chad Johnson and Shannon Sharpe clip sports; POV meme internet; Sun surface image science; G-DRAGON MAMA award music; Lamine and Messi comparison sports; Cyberpunk Kojima post gaming; French shop owner during the riots world; Caleb Williams sports; AAP RICO lawsuit medicine; East Potomac golf course hearing politics
EXTRA_PRIVATE |= {'2112038533401551203','2111529300390535364','2111951101247287642','2112076855608324395'}  # 2100Z: InternetH0F photo of an anime game shop owner during the France riots (not a public figure); Tina23667422279 post and the piss_kirby_ quote mocking her (a pile-on against an account that is not a public figure); veri12121212 'my mother's past' post, link only, media not returned (subject unclear)
EXTRA_PRIVATE |= {'2112225054927044709'}  # 2209Z: MeidasTouch post about the influencer removed from a Paxton rally (same person as 2112231563811561851 in 2000Z, public status unclear)
DESK_OVERRIDE_RUN.update({'2104505157396713624':'internet','2111391235352953046':None,'2111174769710084198':None,'2111363942627115425':'internet','2112140880618635585':None,'2112175639726026896':'sports','2111904232379150543':'music','2111853084087316576':'world','2111966729425633392':'life','2111978227732254752':'life','2111980242659156008':'entertainment','2111864893007651110':'entertainment','2111962805599650209':'justice','2112107738272604577':'justice','2111478337856242061':'world','2111934392105042412':'world','2112225054927044709':'politics','2111838678146281750':'gaming'})  # 2209Z desk fixes
EXTRA_PRIVATE |= {'2110753875930321204','2111992062262268028','2111707198829289984'}  # 2300Z: lusgotem bathroom fight clip (private people); iamthelmalouise video of being asked to leave a Texas Republican event (the influencer of 2112231563811561851, public status unclear); Amelia181672271 video of a man on the Kaohsiung metro (private person)
DESK_OVERRIDE_RUN.update({'2076019400612762008':'politics','2111916665160278366':'business','2003876371815403633':'ideas','2111707198829289984':'world','2112222867857576292':'entertainment','2111611618861969749':'world','2112285618973880798':'sports','1701122117616701802':'entertainment','2106704368192151896':'internet','2111992062262268028':'politics','2111454951499354303':'life'})  # 2300Z
EXTRA_PRIVATE |= {'2111894582413898065','2109652649763033227','2110482968766460280','2112281537475453336','2112200010146492818','2112262193496383617'}  # 0200Z: InsaneContext video of a pit bull attacking a toddler and a bystander; BVoltaire and posttmodern videos of a French police officer beaten by high school students; instablog9ja woman crying over a seat swap; mattvanswol Italian woman shouting at police; atrupar protester behind Vance (none public figures)
DESK_OVERRIDE_RUN.update({'2109652649763033227':'world','2110482968766460280':'world','2112200010146492818':'world','2112196290645832062':'sports','1876753074091638809':'politics','2112262193496383617':'politics','2054805910636351522':'offbeat','2108251074637213843':'internet'})  # 0200Z: France and Italy police videos to world; Eagles medical staff joke to sports; Watters Canada clip and Vance protester to politics; cats chattering to offbeat; waist meme to internet
DESK_OVERRIDE_RUN.update({'2111933887622582513':'entertainment','2111940251526762889':'gaming','2112276675996024870':'internet','2112160305635897609':'sports','2112116545295986960':'tech','2111881742034608303':'entertainment','2112214060192190692':'music','2112323704822636895':'music','2112190389943722435':'internet','2112246067739984319':'justice','2112361800335565107':'life','2112249571741188233':'internet'})  # 0906Z desk fixes (milfinstyle 2020-nostalgia meme to internet): South Park clip and Premalu 2 post to entertainment; game-piracy post to gaming; conversation and win memes to internet; figure skating post to sports; casino fish-tank hack to tech; Tim McGraw and carterefe music video to music; Atlanta Technical College shooting to justice; Indonesian compliment story to life
EXTRA_PRIVATE |= {'2112274962379641222'}  # 1007Z: ZainabOfficial6 post on the couple executed in Saudi Arabia
DESK_OVERRIDE_RUN.update({'2112274962379641222':'world','2112292761764278695':'music'})  # 1007Z: Saudi execution posts to world as in 0308Z
EXTRA_PRIVATE |= {'2112288176333082677','2112300576478265823','2111970689594896436','2111945096807481566'}  # 1007Z: DefiantLs video of a bystander and a pit bull that bit a toddler (same video as 2111894582413898065); sarkinnomaa post on the two people executed in Saudi Arabia; mymixtapez post on the deaths of two lookalikes; lucidstreak screenshot of an exchange between private accounts
OLD_VIA_CHAIN |= {'2019573027063668819','2020172649972879648'}  # 1007Z: Feb 2026 WBCBaseball post and the Palestine_UN quote of it, reached through a Feb 2026 chain from a post read this run
EXTRA_PRIVATE |= {'2112173990169248117','2112242408637493462'}  # 1103Z: AMuseInLove screenshots of a dating-app chat with a private man; libsoftiktok video of high school football players (private people, minors)
DESK_OVERRIDE_RUN.update({'2112173339896648158':'politics','2111802080176349231':'entertainment','2112077184445653360':'ideas','2112264840937189768':'ideas','2111929538557235480':'life','2112173990169248117':'life','2112075450185072740':'gaming','2112357292444385405':'music','2112162166681833911':'internet','2010675877579796615':'sports'})  # 1103Z desk fixes
DESK_OVERRIDE_RUN.update({'2112300576478265823':'world','2112288176333082677':'offbeat','2111970689594896436':'music','1909228793048277480':'science','2109046739495944476':'entertainment','2109046877576413313':'entertainment','2019573027063668819':'sports','2111945096807481566':'internet','2112288022578471167':'internet','2112262772470042626':'internet','2112472771930509600':'sports'})  # 1007Z desk fixes: pit bull video to offbeat as in 2026-10-20; lookalike deaths post to music; TIME dire wolf cover to science; NARUTO manga posts to entertainment; WBCBaseball roster to sports; screenshot and headlight memes to internet; Ten Hag on Ronaldo to sports
EXTRA_PRIVATE |= {'2111684930644390323','2112041190707388581'}  # 0801Z: Whoiamyours video of a couple at a car showroom (private people); SamSiff post on the same video mocking the man (private people)
DESK_OVERRIDE_RUN.update({'2111684930644390323':'offbeat','2112041190707388581':'internet','1979301859040071782':'sports','2111116191267688712':'music','2112008869610475934':'sports','2111923714967076943':'entertainment','2112204610991522240':'world','2112295254598787433':'world','2112356818202878242':'sports','2106299896831844380':'world','2112206658223091898':'world','2111950600816459816':'world','2111933524412453207':'life','2112312888153284774':'politics','2112342832706990578':'sports','2112310323134759109':'politics','2077530563502657841':'entertainment'})  # 0801Z desk fixes: car-showroom couple posts to offbeat and internet; YanGlazer2 UFC clip and Shams Cason Wallace and ShowCaseShabazz Angel Reese posts to sports; Rain_MakeFair2 animated song to music; Succession clip to entertainment; German France-riots shop post, UK parking-fines post, Indian National Congress post, Uduaghan tribute and Alex Jones France-riots post to world; esisoverthis relationships post to life; Acyn Hume clip and Ryan_Parkerrr Ukraine-report post to politics; second ShowCaseShabazz Angel Reese clip to sports
DESK_OVERRIDE_RUN.update({'2113508214243573866':'politics','2112569484183843245':'politics','2113250973745357253':'internet'})  # 0905Z: elonmusk Talarico post is politics; Michael Knowles Amy Acton post is politics; Caleb Hammer clip is internet (not the Bears QB)
EXTRA_PRIVATE |= {'2111852303779017201','2112187818646626502','2112062941935935950'}  # 0704Z: Rainmaker1973 video of an Amish couple dating (private people); shortmagsmle post on the same video remarking on the girl's speech (private person); MiddleEast_24 photo of a couple at the Kaaba (private people)
DESK_OVERRIDE_RUN.update({'2111615352257843443':'gaming','2112187818646626502':'internet','2111852303779017201':'offbeat','2112215717848461612':'life','2112062941935935950':'world','2112210657995272355':'world','2112090404711485931':'world','2111635331217006627':'world','2111921002196123884':'business','2015504294062051459':'sports','2015451824669466839':'sports','2015500166158016952':'sports','2015501436554035249':'sports'})  # 0704Z desk fixes: DXFromYT Castlevania/Hades post to gaming; Amish dating video posts to offbeat, internet and life; Kaaba photo, Albania, Macron and Africa-aid posts to world; hiring post to business; Amad Diallo and cagiago_ January exchange to sports
EXTRA_PRIVATE |= {'2079207083405439455','2030661522364481751','2112200357636137073'}  # 0607Z: Aslam_rt_17 video of a couple on a boat (private people); opsylojay1 video of an old man on a plane (private person); metronaija post on a video of a child being flogged (a minor)
DESK_OVERRIDE_RUN.update({'1965129615841919211':'sports','2097536989729816627':'sports','2112356322364858763':'sports','2112367568031797527':'sports','2112323157143290081':'sports','2112223398491283679':'sports','2112122016723812701':'music','2112302051481018521':'music','2112109209105883240':'world','2112234803793953186':'world','2112138969819324736':'entertainment','2079207083405439455':'offbeat','2030661522364481751':'offbeat','1875807611473555845':'offbeat','2112200357636137073':'internet','2112321828979093684':'politics','2112249924909756654':'business'})  # 0607Z desk fixes: Acyn Ted Nugent clip to politics; FOS Polymarket athlete-market post to business; TDISportsClips Dwayne Rudd clips, Angel Reese, WWE Roman Reigns, Hansi Flick and Lane Johnson posts to sports; kpop twt post and BNXN post to music; Lagos governor dinner and Albania court fire posts to world; Avatar post to entertainment; boat, plane and village-cooking clips to offbeat; Maraji parenting post to internet
EXTRA_PRIVATE |= {'2112177541859738008','2111136722998501763','2112014034308636969'}  # 0501Z: Jizhengguang video of a group of youths beating a girl (private people, possibly minors); CHOCOLATE_6840 video of two young women in Osaka (private people); SeeRacists video of a woman in blackface on TikTok (pile-on on a person not named as a public figure)
DESK_OVERRIDE_RUN.update({'2112177541859738008':'world','2111136722998501763':'world','2112080505600368998':'world','2066087031009067467':'offbeat','2067246943634329813':'offbeat','2028279728592007656':'offbeat','2069266716551508221':'sports','2112120461312045136':'internet','2112151357096428015':'internet','2112129810260791804':'life','2112373713937084809':'tech','2112260605885267998':'politics'})  # 0501Z desk fixes: atrupar Vance clip to politics; China bullying video, Osaka video and Nigeria tax clip to world; orangutan and lion-hippo clips to offbeat; Shams Giannis trade post to sports; parent-quote memes to internet; Victoria's Secret show video to life; Musk timeline-ranking post to tech
EXTRA_PRIVATE |= {'2071655688405987677','2112092642020655155','2111854258588959211'}  # 0400Z: Clip_Master__ and sadngkid copies of a video of a police officer (not a public figure); RT_com video of a woman on holiday in Paris (private person)
DESK_OVERRIDE_RUN.update({'2112341245800399204':'sports'})  # 0400Z: ShowCaseShabazz Angel Reese clip to sports
DESK_OVERRIDE_RUN.update({'2071655688405987677':'internet','2112092642020655155':'internet','2111854258588959211':'world','2111975516362215750':'life','2112006570242425257':'life','2112161257054675296':'sports','2112176027426283551':'sports','2112287176184529168':'sports','2111938370935132451':'sports','2112257738335998448':'entertainment','2111405602660286719':'entertainment','2112171234406338803':'world','2107799903095476591':'world','2112212586464973180':'gaming','2048923523075219587':'music','2112121546185605596':'music','2111985862384783771':'politics','2112189751235138018':'politics','2110749968436732258':'internet','2111363567329103975':'internet','2067555872004342093':'offbeat','2112135083654267286':'offbeat'})  # 0400Z desk fixes: Paris holiday video and Rwanda, Rahul Gandhi posts to world; Victoria's Secret show posts to life; football, Harden and Tottenham posts to sports; TMZ Hunter Schafer and Helluva Boss posts to entertainment; Deadlock clip to gaming; Dua Lipa posts to music; Air Force One and Jubilee clip to politics; cartoon memes and badge clip to internet; dachshund agility clips to offbeat
EXTRA_PRIVATE |= {'2112085314256720355','2111918884857020567'}  # 0308Z: TrendingEx post naming two Bangladeshi nationals reported executed in Saudi Arabia (private people); AryanBundles post mocking an unnamed man in photos (private person)
DESK_OVERRIDE_RUN.update({'2112085314256720355':'world','2111804709074043369':'world','2112214366737010864':'world','2109559502840508514':'entertainment','2111942044222419453':'entertainment','2111918884857020567':'internet','2112102322507534767':'offbeat','2112323120380129562':'politics','2112286669508694289':'politics','2112256359022362891':'politics','2112227716183277635':'business','2112211740884975910':'business'})  # 0308Z desk fixes: Saudi executions, Paris photos and Kim Jong Un rumour to world; Allu Arjun film update and Little Witch Academia post to entertainment; Goku-shirt man post to internet; survival clip to offbeat; Trump Accounts request posts to politics and business
skip_nsfw |= {'2101901320735072600','2112732556605182117'}  # 0403Z: EditHouse447 celebrity sex-compilation promo (sexual); likely paid (ShowCaseShabazz again, 26,894 followers: 431 likes and 4 replies on 549K views)
DESK_OVERRIDE_RUN.update({'2077167290085236927':'internet','2112238409070604456':'entertainment','2112614952074903772':'life','2112708041988587904':'justice','2111053358920253537':'medicine','2112422310670127576':'sports','2034650099067048142':'entertainment','2112596062972088544':'business','2016354863207391344':'sports','2112725281245167981':'sports','2112733191404675253':'sports'})  # 0403Z desk fixes
skip_nsfw |= {'2112729819599327258','2112366584350261723','2112738079651827926','2096290810975109598','2089210792029605963'}  # 0507Z: TheBHentel Jared McCain post with a homophobic slur; 03nightz sexual joke with a racial slur; 30GotNext Shai post with a racial slur (as EVERYONEATHEEND in 2059Z); likely paid (caseofluv, 4,904 followers: 241 likes and 0 replies on 1.45M views); QuietPremise close-up ingrown-hair extraction video (graphic, when in doubt left out)
EXTRA_PRIVATE |= {'2112659261096640710'}  # 0507Z: PopBase post of the Ramaswamy campaign statement on the ad featuring Amy Acton's mother (public status unclear, as in 1200Z/1401Z/1502Z)
DESK_OVERRIDE_RUN.update({'2038480087637475739':'offbeat','2111766741563175139':'offbeat','2112204122216685905':'world','2055499046488342878':'offbeat','2112491642552987698':'music','2052289520708784548':'sports','2082359699324674381':'offbeat','2093280390693691680':'offbeat','2112346780163563909':'justice','2108561739822588126':'sports','2112340434551013382':'politics','1841073101443899652':'gaming'})  # 0507Z desk fixes
EXTRA_PRIVATE |= {'2079268143520780461'}  # 0004Z: dollyp2025 clip of a couple and a boyfriend at a door (people shown are not public figures)
DESK_OVERRIDE_RUN.update({'2112309016617439286':'internet','2112202242048528540':'ai','2112242023805964327':'ai','2111985934589645266':'ai','2112206764024463679':'sports','2111975720184361157':'life','2112216349393232083':'internet'})  # 0004Z
skip_nsfw |= {'1981893109425311959','2112449011181584433'}  # 0559Z: archmovies Shameless wedding clip (likely paid: 1,672 likes and 6 replies on 2.7M views); Abhishek060722 'Elon Musk's daughter' video, preview shows a young woman of unclear age posing in underwear (left out under the minors rule as a precaution)
EXTRA_PRIVATE |= {'2112450284081356969','2026687145964962174'}  # 0559Z: stoneoreye ultrasound-room clip of a nurse and patient; wildfreakouts livestream clip of a woman punched by her boyfriend (neither public figures)
DESK_OVERRIDE_RUN.update({'2111798615844810801':'tech','2054402101728408039':'entertainment','2112116180232106134':'entertainment','2112572559325585704':'life','2112406293092987169':'offbeat','2112420242660147537':'world','2026687145964962174':'internet','2112407664516796898':'internet','2112616840635773183':'world','2112277713595617775':'life','2112193568186224900':'internet','2111837668958978519':'tech','2111667264105693577':'tech','2112493706268012831':'life','2112746994909294744':'sports','2112450284081356969':'internet'})  # 0559Z
skip_nsfw |= {'2112210483533008965'}  # 0705Z: mask_robot anime character art (Eldreda Sunbringer, #zzzero); media not returned by X and possibly_sensitive not set, so it could not be screened
EXTRA_PRIVATE |= {'2111572549612253296'}  # 0705Z: Madximilian clip mocking a rally attendee in a red cap (not a public figure)
DESK_OVERRIDE_RUN.update({'2112592653774704788':'sports','2110841224986812828':'tech','2112336168784134484':'tech','2102425012435071386':'tech','2112712984644784534':'ai','2112603916076781778':'ai','2111572549612253296':'politics','2112574343280529490':'sports','2112654591674175702':'sports','2112210483533008965':'gaming'})  # 0705Z desk fixes
skip_nsfw |= {'2112537545536061803','1699985421940252753','2042983726959689970'}  # 0804Z: gothicornate_ 'standing nude contortionist' sculpture (nudity; media not returned, so it could not be screened); milk4ufag 'Boys night' 2023 video (sexualised account name; media not returned, so it could not be screened); Ssuzzie 'This movie is rated 9/10' clip (likely paid: 1,029 likes and 69 replies on 1.41M views)
EXTRA_PRIVATE |= {'2112638556900356129','2112618691409883444'}  # 0804Z: its_The_Dr video of people caught destroying a Trump sign (private people); allchronology clip of a cameraman stopping a man (private people; media not returned)
DESK_OVERRIDE_RUN.update({'2112618691409883444':'offbeat','2112506169608871943':'internet','2112660966072590389':'disaster','2112520560018338170':'gaming','2112253657647599684':'internet','2112461424651911634':'internet','2112755758106611943':'music','2112125500990902690':'internet','2112189152343081468':'world','2112229044171456900':'music','2112591515566371199':'ai','2112638556900356129':'politics'})  # 0804Z desk fixes
skip_nsfw |= {'2074182250699051029','2109651609076764858','2112749792871002588','2105616451902333358','2112698713281855610'}  # 0906Z: likely paid (Rssaill Arabic exorcism clip, Jul 2026: 64 likes and 5 replies on 4.5M views, as the Rssaill origin left out in 1303Z); likely paid (SteelersFC, 3,187 followers: 165 likes and 0 replies on 1.16M views); likely paid (ShowCaseShabazz Aday Mara clip: 961 likes and 2 replies on 661K views, as its Wemby clip left out in 0802Z); likely paid or bait (onlygirll8 'possessive girlfriend' clip, Oct 1: 15,408 likes and 0 replies on 311K views); promotion (PumpfunEco trading-platform promo)
DESK_OVERRIDE_RUN.update({'2112732230124818891':'ai','2112638276389790102':'business','2112781132387529005':'business','2112499101312942227':'gaming','2112516066563829882':'ai','2111860967508181222':'world','2112723908520460339':'entertainment'})  # 0906Z desk fixes

skip_nsfw |= {'2112583515787182563','2089680490743673085','2071696172583186707','2112658581027770650'}  # 1007Z: sexual text (ria_reigns); likely paid (ashercrw link-only post, Aug 2026: 20 likes and 2 replies on 779K views; PlayoffVJ77 link-only video reply, Jun 2026: 104 likes and 0 replies on 368K views; FlowParisien, 42 followers: 46 likes and 1 reply on 570K views)
EXTRA_PRIVATE |= {'2112159826885156896','2112485928682025335'}  # 1007Z: Proudofthisland Tesco video accusing a man of shoplifting (not a public figure); allchronology clip of hecklers at a Trump event (private people)
DESK_OVERRIDE_RUN.update({'2112834288056144037':'sports','2112526775523619161':'music','2112566334013726858':'music','2112159826885156896':'world','2112678925394739684':'politics','2112760990513193240':'politics','2112637394654822514':'business','2112732678680449341':'sports','2112295219765137570':'ai','2112238714516607211':'entertainment','2112223631249990039':'internet'})  # 1007Z desk fixes
skip_nsfw |= {'2112167551711215876'}  # 1107Z: sexual text (hot____ewa reply)
skip_nsfw |= {'2110662276244242842','2086121837403177141','2086061596972056700'}  # 1107Z: likely paid (Tanj5iro, 7,224 followers: 25,018 likes and 18 replies on 983K views, 6,274 likes and 13 replies on 1.2M views; Othayarukitta: 1,143 likes and 26 replies on 597K views), suggestive Jenna Ortega kiss clips
skip_nsfw |= {'2112565308003414185','2084540473059000322'}  # 1107Z: pornographic text (jakipziio, reached through the quote stream); likely paid suggestive Jenna Ortega clip (Tanj5iro, as above)
skip_nsfw |= {'2106476456268403186'}  # 1107Z: likely promoted (KalshiSports betting-market post, Sept 2026: 244 likes and 17 replies on 348K views)
DESK_OVERRIDE_RUN.update({'2112680671260938277':'sports','2112736030302617699':'business'})  # 1107Z
DESK_OVERRIDE_RUN.update({'2112812380413366397':'entertainment'})  # 1107Z: GMMTV Scarlet Heart Thailand live
DESK_OVERRIDE_RUN.update({'2112349020454559771':None,'2111979523080093815':'life','2112620704424202343':'gaming','2112755217418813909':'music','2111019315780538856':'music','2111864426257146047':'world','2112625951586800119':'entertainment','2112536817488572645':'offbeat'})  # 1107Z desk fixes
skip_nsfw |= {'2112632806077800585'}  # 1204Z: mark_slapinski post alleging sexual abuse of a 13-year-old girl, left out under the minors rule as in 0004Z, 0906Z and 1007Z
EXTRA_PRIVATE |= {'2112655761843380287'}  # 1204Z: RabbiJeffx asks Grok for the ethnicity of a victim and a perpetrator in an attached image the reads did not return (people likely not public figures; precaution)
DESK_OVERRIDE_RUN.update({'2112844429052830042':'sports','2112655761843380287':'justice','2112549171336987027':'sports','2112651162835185926':'tech','2112754017386553547':'politics','2112649803888807983':'entertainment','2112407555628741042':'internet','2042821091316392368':'internet','2112574563796009333':'entertainment','2112549706588889126':'sports','2067636354121666996':'politics','2112181044330070274':'internet','2112375662317347258':'music','2112661108834353419':'sports'})  # 1204Z desk fixes: FabrizioRomano Dembele injury and buzor042_ Super Ballon d'Or posts are sports (were ai/entertainment by keyword); RabbiJeffx crime-ethnicity question is justice; IntCyberDigest eMudhra certificate post is tech; EndWokeness Ilhan Omar post is politics; DiscussingFilm Marvel x Star Wars comic and dunemovie tickets are entertainment; IanCarrollShow Shawn Ryan episode post, dykemedla Saucy Santana reaction clip and DoobieCartoonie clip are internet; MySportsUpdate Titans release and BleacherReport Pistons comeback are sports; Acyn Vance clip is politics; britmebaby duo clip is music
skip_nsfw |= {'2099730026434605130'}  # 1302Z: axisrobotics token 'Community Sale' pre-registration post (promotion; old origin reached through a reference)
EXTRA_PRIVATE |= {'2112824660677038339','2112817908745400493'}  # 1302Z: notdokun quote post of screenshots of Justwandyy's replies to her own 'talking stage' question, and the Justwandyy post itself (pile-on on a person who is not a public figure)
EXTRA_PRIVATE |= {'2112478401911046477'}  # 1302Z: RyanAFournier post on the ad featuring Amy Acton's mother (public status unclear, as in 1200Z/1401Z/1502Z/0507Z)
DESK_OVERRIDE_RUN.update({'2112680269475897600':'gaming','2112716513153028296':'sports','2112819774573179175':'tech','2112618021122605272':'life','2112871277690011719':'world','2112528073316831326':'tech','2082455586633859387':'music','2112824660677038339':'internet','2112817908745400493':'internet','2112656247589904420':'tech'})  # 1302Z desk fixes: PlayStation Crimson Desert DLC to gaming; NBA Jaylen Brown clip to sports; Unitree H2-X robot to tech; theshawnyboy relationship post to life; Osint613 Witkoff clip to world, as the other Witkoff and Hubbard posts; VigilantFox Rogan on Meta scam ads to tech; nitigrande Tyla video to music; notdokun and Justwandyy to internet; firesidealpha SpaceX casting-shop post to tech
skip_nsfw |= {'2112520751291277589','2112665847642894714','2112666167357968556'}  # 1402Z: likely paid (haterseraa, 1,924 followers: 6,980 likes and 1 reply on 5.3M views; ElonMuskAOC EAGLE-4 promotional copy in the paid EAGLE-4 campaign seen in 0705Z: 1,169 likes and 22 replies on 150K views; BoardManKLaw, 1,115 followers: 22,176 likes and 7 replies on 462K views)
EXTRA_PRIVATE |= {'2112476861733433463'}  # 1402Z: mico332 photo of an unnamed man urinating at Shibuya coin lockers (private person, racially framed caption)
skip_nsfw |= {'2100285201381458105','2112229078648668601'}  # 1500Z: Lustykittu66 video whose preview is pornographic (old origin reached through a reference); transleytanked post of photos dug up of Chappell Roan's old friends, relatives and ex-boyfriends (private family information)
EXTRA_PRIVATE |= {'2112109505622294555','2112414831928127854'}  # 1500Z: Rakgadi_EM and LilithBlack25 copies of a video of an unnamed tall South Sudanese wrestler (not a public figure; Rakgadi_EM caption is a 'cross breed' joke about him)
skip_nsfw |= {'2105038102788264444'}  # 1604Z: ProudPatriots1 'Trump Elf' pre-order sales post (product promotion, likely paid; old origin reached through a reference)
EXTRA_PRIVATE |= {'2112691087697469456','2110765728601387261','2112702665033486747'}  # 1604Z: okayaleiah memorial post for her mother (private family grief); donttouchxanax clip of unnamed stream guests kissing; ItsKingSlime video of Coco Jones and an unnamed man insulting her (precaution for the unnamed people)
skip_nsfw |= {'2112218918777753774','2044505156033610205'}  # 1709Z: AmericanExpress NBA card-perk post (ad, 23M views on 2,336 likes); UTD_Pa 'Mom and Daughter' video whose preview is suggestive (sexual bait, old origin reached through a reference)
EXTRA_PRIVATE |= {'2112550132231414060'}  # 1709Z: BenStanton77 video mocking an unnamed man's skin (pile-on against a private person)
skip_nsfw |= {'2112949405565215180','2112949611438448689'}  # 1808Z: likely paid (Omr_USL, 18 followers: 32 likes and 1 reply on 748K views, video removed on a copyright report; ottawatopys, 163 followers: 24 likes and 0 replies on 690K views, link-only video)
EXTRA_PRIVATE |= {'2112457542454690262','2112725484396286201','2112776429108707630','2112810844161520073','2112603318778474970','2112113925181591984'}  # 1808Z: unnamed people in an arena concourse confrontation (godsoncatalina video and the dijoni repost of it); funeral of the executed Bangladeshi couple with their young daughter, and the couple at the Kaaba (yirmiucderece, private family); unnamed man in the blue_sapphire9 clip and the Ichanpyaari couple video it reuses (precaution)
OLD_VIA_CHAIN.add('2029872548347814380')  # 1808Z: March 2026 post reached through a reply chain from an October post read this run
skip_nsfw |= {'2112954705634902429','2112963173666185655','2112529278449443285','2112944865575379443','1752463675234144346','2090808404688183652','2074257214219371005','1813789890418766264','2112285949287669885'}  # 1900Z: likely promoted (KanekoaTheGreat Talarico clip compilation: 1,405 likes and 141 replies on 9.1M views, as the 1803Z KanekoaTheGreat post; BrianRoemmele Grok Bot credit-repair post with a sign-up link: 198 likes on 938K views; LAIKAStudios Wildwood ticket trailer: 12,319 likes on 2.3M views from 82K followers; PrimeVideo Rings of Power trailer: 1,193 likes on 715K views; FilmUpdates Jan 2024 question post: 2,370 likes on 21.7M views); likely paid (acervobelissimo Aug 2026 prank clip: 3,268 likes and 30 replies on 14.6M views); likely paid keyword-stuffed reaction-meme clips (burnerbwoireact, Jul 2026: 760 likes and 1 reply on 2.9M views; DeviantReaction, Jul 2024: 599 likes and 0 replies on 833K views); reply bait on suicide (jjmmgg23, 91 followers: 1,740 replies on 2.7M views)
skip_nsfw |= {'2112864653143429380'}  # 1900Z: ImtiazMadmood video whose preview shows a boy swinging a strap at a girl in a madrasa classroom full of children (minors rule: abuse of a minor)
DESK_OVERRIDE_RUN.update({'2112964322192408813':'politics','2112958301344264310':'politics','2112876909134811262':'entertainment','2112491349492867300':'offbeat','2112642154581381131':'internet'})  # 1900Z desk fixes: elonmusk Talarico posts are politics; gleeofficial reboot post is entertainment; AliceHooll caterpillar clip is offbeat; N1NETY6S racist-past quote is internet
skip_nsfw |= {'2112172521797898683','2112582820350607718','1917242256828076477'}  # 2008Z: sexual text (Tretuahissobac 'carnally' post on two cartoon characters); sexyIoserr post with a racial slur (as the earlier slur skips); likely promoted (blckriflecoffee brand post of May 2025: 626 likes on 1.5M views)
EXTRA_PRIVATE |= {'2112079104577347745','2112434981473509456','2112607367363735651'}  # 2008Z: mosque CCTV video of an unnamed man dying during prayer (JMNewsNetwork_ and joemiano30 posts of it) and the realMaalouf pile-on against the worshippers (people who are not public figures)
DESK_OVERRIDE_RUN.update({'1851665635513950434':'gaming','2111849880088183197':'gaming','2112079104577347745':'life','2112434981473509456':'life','2112607367363735651':'life','2111787628710314044':'offbeat','2112464810084630997':'internet','2112595237746921848':'sports','1920858904075935818':'world','2112594574145163355':'music','2107014125482131523':'internet'})  # 2008Z desk fixes: Grummz Dragon Age and the Deltarune clip are gaming; the mosque video and posts on it are life; the cat and green beans post is offbeat; Adrien Broner on a DeenTheGreat stream is internet; Adam Silver on SGA is sports; RadioGenoa Macron clip is world; Slayyyter statement is music; mrvediyebirisi wafer joke is internet
DESK_OVERRIDE_RUN.update({'2112538789922894245':'world','2112510803912138835':'politics','2112672106349494582':'politics','2112732783890337837':'justice','2112743701046849575':'music','2112853707784118403':'world','2112831255913881932':'music','2112487884917964806':'internet','2112476861733433463':'internet','2112630446563512675':'politics','1969763112149479860':'entertainment'})  # 1402Z desk fixes: PolitlcsUK Jenrick clip and bradlander IDF detention to world; StateDept Rubio, ethanclynne Ramaswamy and GrageDustin Tad Jude ad to politics; DailyLoud Charlotte police to justice; godmitzu JIHYO and LNGSHOT4sho to music; ben_1225 and mico332 to internet; ficcnucc film clip to entertainment
skip_nsfw |= {'2111722552011722928','2112253338121355471'}  # 2203Z: Ale_Fever1400 link-only animated clip from a 156-follower account in a neon room with a cage and chains (suggestive, when in doubt left out); BoltAndBeer Madison Beer selfie video framed with no clothing visible (suggestive, when in doubt left out)
DESK_OVERRIDE_RUN.update({'2112981920741310695':'world','2112916637494002024':'politics','2112880329031618645':'world','2112880919316967802':'politics','2112777988706111905':'internet','1617638952852402177':'entertainment','2112687433578160169':'internet','2112544460676780506':'music','2112555986561228872':'music','2112120017689125099':'internet','2111411340032282744':'internet'})  # 2203Z desk fixes: Bukele message to the Haitian gangs holding Salvadoran aviation technicians is world; Bill Clinton on Muslims is politics; Reuters migrant caravan is world; FoxNews Ilhan Omar is politics; Lamborghini husband clip and blocked-accounts screenshot are internet; Drag Race Snatch Game clip is entertainment; Anok Yai and Jennie comparison posts are music; French post on Japanese protest tweets is internet; Charlie Kirk song clip is internet
skip_nsfw |= {'2112927934134575522','2105760490064384012','2112986757696229505','2112362626995122671'}  # 2301Z: KiwiFarmsDotNet post on a livestreamed self-immolation with photos (graphic, left out); TELLMELOCOM 'Join now' post from a 208-follower account (likely promoted); TheBHentel racial slur; Real_JFK_Jr_ 'Epstein File Video' clip of a man handling a person lying down (possible abuse content, when in doubt left out)
EXTRA_PRIVATE |= {'2035382073649741876','2035377927001362847','2112517629504090361'}  # 2301Z: EhisOjeks photos with his mother (not a public figure); visegrad24 post naming a man as the Limoges town hall arsonist (precaution)
DESK_OVERRIDE_RUN.update({'2065166390605017152':'sports'})  # 2301Z: World Cup red card clip is sports
skip_nsfw |= {'2112730449319735449','2083393317757231307','2112979321233224062','2111291861767971069'}  # 0001Z: ashtonpittman leaked bodycam of the police shooting that killed a 1-year-old (graphic, minor); Erogetism 'molested by my iPod Touch' (sexual text); HariomK61498 Martina Hingis photo pair framed on her cleavage (suggestive, when in doubt left out); TheCinesthetic text-only question with 204 likes on 1.4M views (likely promoted)
DESK_OVERRIDE_RUN.update({'2112921648252719420':'tech','2112879349443518975':'internet','2112594903616328012':'entertainment','2112887540831395864':'entertainment'})  # 0001Z: FBI PHP vulnerability alert is tech; Wicked 'What Is This Feeling' joke is internet; Karen Gillan Highlander and Doctor Who posts are entertainment
skip_nsfw |= {'2107213637136056390','2112615417797882242','2112125519315755288'}  # 0103Z: kwiHuub 'HotelsexVol.1 full movie on my link' (sexual text and spam link, Oct 5 origin); MrParleG 'Transgenders atrocities in Gummidipoondi SIPCOT' video (hostile framing of a group, private people); Askandtask 'My anime ranking' (637 followers: 943 likes and 538 replies on 1.3M views; likely promoted)
skip_nsfw |= {'2112646712812548265','2112972552729473330'}  # 0206Z: cinemaclt 2009 Ibiza paparazzi swimsuit photos of Ana de Armas with an unnamed older man (suggestive, private person, when in doubt left out); SaveJxn 'FAFO ALERT' video of police stopping a 16-year-old with a pistol (minors rule)
DESK_OVERRIDE_RUN.update({'2113021834702823905':'sports','2112894970499629563':'gaming'})  # 0206Z: NBA Haliburton return is sports; Vanoss Crew GTA 6 mansion is gaming
EXTRA_PRIVATE |= {'2112582739492803050'}  # 0300Z: rewanayman79 Arabic post with an Instagram-story video of a woman, framed as Egyptian men chasing transgender people (private person, when in doubt)
DESK_OVERRIDE_RUN.update({'2052783544720605639':'music','2112582739492803050':'internet','2113081289570127971':'politics','2103250168338686288':'politics','2092682411792380191':'entertainment','2111980188103848032':'music','2045152451372716103':'internet','2112987147900977290':'sports','2112233954782625850':'internet','2112596149706121363':'life','2103541377166446901':'politics','2112572837773140286':'entertainment','2112885364977238210':'politics','2112853606776869335':'world'})  # 0300Z: PinkPantheress and Latto are music; Talarico, RNCResearch, El-Sayed and Hillary-NASA meme are politics; Macron is world; JD Vance with Bengals players is sports; Ramayana is entertainment
skip_nsfw |= {'2113008540629774789','1980994929364287797','1664325945963216901','2069721883260375097'}  # 0408Z: sexual text (hoIysaintwest 'laugh dick first'); likely paid (MidiaAleatoria link-only video, Oct 2025: 6 likes on 1.6M views; elenacute01 copy of the Crazymoments01 tent clip with an added link, as the elenacute01 clip left out in 1410Z); likely promoted old question post (PopCrave 'favorite queer anthem', Jun 2023: 2,311 likes on 15.3M views)
EXTRA_PRIVATE |= {'2112957209701396922'}  # 0408Z: jwdongkcwing post on an unnamed streamer claiming to be Choi Soobin's boyfriend, with livestream screenshots (private person, when in doubt)
DESK_OVERRIDE_RUN.update({'2112965425164411132':'gaming','2112519623203492296':'entertainment','2112629887269789963':'entertainment','2112957209701396922':'music','2112911869136482802':'entertainment','2113042914771415095':'sports','2112998543065600047':'business','2113071511107944654':'politics','2112982970869170553':'politics','2112984169735139816':'gaming','1947923895987671210':'gaming','1667612864255868928':'entertainment'})  # 0408Z: Battlefront 3, WARDOGS server regions and the GTA 4 voice actor are gaming; Heat 2 audition, press-junket clips and the Suki Waterhouse photo are entertainment; TXT Soobin is music; Barkley on the Heat is sports; Tesla Q3 is business; Omar and the bullet train are politics
skip_nsfw |= {'1897022771919774128','2113090829955084405','2105833572217081989'}  # 0502Z: ThinJen82 suggestive video framed on a woman's body ('Who wants to feel it'; reached through the it repost stream); likely paid (moonball30 link-free clip, 26 followers, 50 likes and 0 replies on 362K views; onelostmedia Oct 2 clip, 888 likes and 20 replies on 12.1M views)
DESK_OVERRIDE_RUN.update({'2103534482930491441':'ai','2102801274173587569':'ai','2112483997762863187':'gaming','2113045722744717360':'tech','2113061182265290843':'politics','2111910794447507956':'entertainment','2112696641165668399':'internet','2112439103858073986':'internet','2033747120210260436':'music','2033775089590931896':'music','1856496905984827411':'internet','2110129088514195489':'sports'})  # 0502Z: Opus 5.5 prompt videos are ai; cricket 07 browser game is gaming; PHP bugs is tech; Talarico is politics; You Can See Everything is entertainment; K-pop stage clips are music; Alysa Liu gala is sports
skip_nsfw |= {'2112775545566200183'}  # 0607Z: seduhtehnya post on a former employee of Aijing's parents' company with photos of her 2-year-old baby's bruised feet and heart condition (private family and medical information about a minor)
EXTRA_PRIVATE |= {'2112915092375556550','2112238148327719131'}  # 0607Z: fujikaize photos of Chloe Lim, named as a Sampoerna heir (not a public figure, when in doubt); kebirungilydi video compilation of unnamed shop workers in Guangzhou imitating African customers (private people)
DESK_OVERRIDE_RUN.update({'1874599446958539258':'offbeat','2112671730800189555':'offbeat','2112868798458192349':'offbeat','2111407030628233483':'sports','2111402302234079256':'sports','2112976702557278542':'sports','2112948272570503631':'world','2112915092375556550':'internet','2112238148327719131':'internet','2112789486459380116':'internet'})  # 0607Z: toy-car clip and pink dolphin posts are offbeat; Ferrari F1 and Packers posts are sports; Irish hugging advert is world; Chloe Lim, Guangzhou shop and rebranding clips are internet
TREND_OFF = {'Warriors': {'2112959155925299672'}}  # 0706Z: Gerashchenko_en post on Ukrainian soldiers matches the word, not the Golden State Warriors trend
TREND_OFF['Swift'] = _SWIFT_OFF  # 0059Z
skip_nsfw |= {'2113070784751321106'}  # 0706Z: sponsored post (Lakers, @ToyotaSoCal x #LakeShow)
skip_nsfw |= {'2048400464450855362'}  # 0706Z: sexual text (BrandtsBoys porn promo, Apr 2026)
skip_nsfw |= {'2113097021909324203','2113107473494049074','2113107506138648845','1937345223023059110','2058966356230369390'}  # 0706Z: likely paid (JEJTron link-only video: 27 likes and 1 reply on 861K views; F0RGIAT0 Luka half-court clip: 129 likes and 0 replies on 945K views; MindOfBron same clip: 240 likes and 5 replies on 773K views; acervoclassicos SpongeBob compilation, Jun 2025: 2,786 likes on 34.0M views; dykemedla reaction video of private people, May 2026: 266 likes and 1 reply on 723K views)
DESK_OVERRIDE_RUN.update({'2113001073019662481':'science','2112964113856938265':'sports','2113079352682570051':'tech','2112807649922122044':'world','2112959155925299672':'world','1906348644070002881':'sports','2112937949654606260':'sports','2112750015592739254':'sports'})  # 0706Z: Marathon Fusion isotope post is science; Man United All or Nothing post is sports; Cloudflare php2shell stats are tech; Abia State governor video is world (Nigeria); Ukrainian 65th Brigade post is world (not the Golden State Warriors); Aiyuk bonus, Giants QB and travel clip are sports
DESK_OVERRIDE_RUN.update({'2112917851354849344':'world'})  # 0800Z: RT_Visual_on_X Filipino land-dispute underwater contest deaths (not sports)
EXTRA_PRIVATE |= {'2112953780090310851'}  # 0800Z: OgLakyn post on a TikTok dry cleaner (not a public figure)
skip_nsfw |= {'2112975589267169468'}  # 0904Z: isaacrrr7 post describing the public rape of a teenage girl in Pakistan (sexual violence involving a minor, left out under the minors rule)
skip_nsfw |= {'1901718057002668208','2112767440971252126'}  # 0904Z: racial slur in the text (legendz_prod 'leaked audio' Banchero/Jerome clip, Mar 2025, reached through the Ty Jerome stream; thyesteanAseity quote-stream origin), as the earlier slur skips
skip_nsfw |= {'1957279864949772310','2039709209605136544'}  # 0904Z: likely paid (MadsFCB10, 1,477 followers: 527 likes and 11 replies on 15.7M views, Aug 2025; palmtop_taigaa: 513 likes and 7 replies on 1.65M views, Apr 2026)
skip_nsfw |= {'2014760041224577536','2112962964081021156'}  # 1007Z: explicit sexual text and video (FaceFuckFiend, Jan 2026 origin reached through a reference); mattxiv post about a candidate's rape by her stepfather (sexual violence involving a minor, left out under the minors rule)
skip_nsfw |= {'2103644527810503139','2113107557871235265','2113106174543528388'}  # 1007Z: likely paid (30CookBron, Sep 26: 434 likes and 33 replies on 2.35M views; ShowCaseShabazz Luka clip: 360 likes and 3 replies on 624K views; MindOfBron Luka clip: 118 likes and 0 replies on 623K views)
skip_nsfw |= {'2112923731769360511'}  # 1107Z: dopetimist ranking of adult film actresses (sexual content)
skip_nsfw |= {'2112934185661026349','2054727454443388978','2109367589508194699'}  # 1201Z: racial slur as the whole text (park_geon10723, as the slur posts left out in 0904Z); sexual subject (feinmadeit 'G*ON bait' Twitch streamer post, May 2026 origin); likely paid (pahrduve link-only video, Oct 11: 43 likes on 1.7M views)
EXTRA_PRIVATE |= {'2111220437623660651'}  # 1201Z: viafication 'such a barbie' video of an unnamed woman (when in doubt)
skip_nsfw |= {'1994988475356254674','2112807462722265344'}  # 1307Z: sexual subject (Piggy0o captive-sub post, Nov 2025 origin; harrysone9 'one-minute man' post)
EXTRA_PRIVATE |= {'2112974943772086406','2113036859328573853','2112941335355215876'}  # 1307Z: sarrah_bellus names a nursing student (private person); LoneStar_PAC names an 11-year-old child performer; desi0re screenshot of a friend's message (when in doubt)
skip_nsfw |= {'2113270793933349007','2113273841401159713','2113275713470054540','2113277806046056541','2113283101711577250'}  # 1501Z: Lindsey Graham escort posts that describe one of the men as 17 or a minor (minors rule)
skip_nsfw |= {'2112097522793505098','2112598541373788189','2112187582855401644'}  # 1501Z: likely paid (st0ic_09, 4,524 followers, '#challenge' video: 1,673 likes and 16 replies on 1.3M views; SegunOruku, 5,331 followers, 'Watch full episode' video: 3,011 likes and 35 replies on 863K views); Dani_X0X6 'Postpartum looks so good on you' body-focused video whose media was not returned, so it could not be screened
EXTRA_PRIVATE |= {'2112567142520607016'}  # 1501Z: polo_kimanii post mocking an unnamed CRE teacher from Kitui (private person)
DESK_OVERRIDE_RUN.update({'2112899243312586875':'entertainment','2112842130163114298':'music','2113226701622681897':'defense','2113240052461613212':'defense','2112268806852620683':'internet','2112540700730376318':'entertainment','2112634019460354300':'entertainment','2112180899718561886':'ideas','2113112076038373722':'world','2112962128781140118':'entertainment','2113251043173683683':'ai','2112567142520607016':'world','2113021567987060955':'entertainment'})  # 1501Z desk fixes
skip_nsfw |= {'2113125779156709827'}  # 1409Z: sexual subject (cokebby11 drug-and-sex question)
EXTRA_PRIVATE |= {'2112653835403673891'}  # 1409Z: PeakClipsMedia store CCTV clip calling an unnamed woman a 'honey trap' and asking for her arrest (private people, when in doubt)
DESK_OVERRIDE_RUN.update({'2112244067140882538':'entertainment','2113042527947211104':'entertainment','2113058108482445418':'sports','2113151750530023708':'sports','2112968196001296537':'gaming','2112579643261829453':'gaming','2111768262757261553':'internet','2112653835403673891':'internet'})  # 1409Z desk fixes: Ron Koslow (TV writer) obituary; Janice Dean on Megyn Kelly; Harry Kane goal kick; Yaxel Lendeborg; Xbox Cloud Gaming pricing; GTA 6 day off; Priest_king2 meme video; PeakClipsMedia CCTV clip
skip_nsfw |= {'2064635430624964971'}  # 1612Z: sexual subject (urauntiesnudes necrophilia joke from a nudes-named account, old origin)
skip_nsfw |= {'2113336264175079586','2109000277626089888'}  # 1902Z: pornographic posts in the Panamá trend stream (sexual, not captured)
skip_nsfw |= {'2112987152912974068','2112585676688445857'}  # 1902Z: blowseason2 sexual question (sexual text); _malenurse 'send this picture to your crush' engagement bait
EXTRA_PRIVATE |= {'2113030688492404846'}  # 1902Z: heavensentl0ver story about a classmate and his girlfriend (private people, when in doubt)
DESK_OVERRIDE_RUN.update({'2113319277092642942':'politics','2113316775291142572':'politics','2091189233654624544':'politics','2091596080429342855':'politics','2112956889004679566':'world'})  # 1902Z desk fixes
skip_nsfw |= {'2113272829794046318'}  # 2107Z: micah_erfan Lindsey Graham escort-allegation post saying one of the men was a minor (left out, as the 1501Z posts mentioning a minor)
EXTRA_PRIVATE |= {'2113339143073792321','2113353494321074451','2113347644643004565','2113017481807700148'}  # 2107Z: EndWokeness, EricLDaugh and Milajoy name the man arrested over the Iwo Jima statue at Quantico (a private person named in an arrest; when in doubt, flag); PeakClipsMedia clip of a man spitting on a streamer and knocked out (private people)
skip_nsfw |= {'2112905268367380718','2044414274123046993','2113158536033403375'}  # 2201Z: dfwsammy1 school-fight clip of a bullied kid (minors, private people); inndigold 'isn\'t she gorgeous?' old photo post (bait); Stake boosted-odds UFC post (paid gambling ad, T&Cs apply)
EXTRA_PRIVATE |= {'2113038620663894179'}  # 2201Z: FightStorage clip of streamer Sneako knocked out by an unnamed passer-by (private person; as PeakClipsMedia in 2107Z)
DESK_OVERRIDE_RUN.update({'2113324631100920279':'ai'})  # 2201Z: nima_owji post on handing tasks to an AI agent is ai, not sports
skip_nsfw |= {'2113290153955328444','2113343520929136862'}  # 2307Z: adamscochran and cenkuygur Lindsey Graham escort-allegation posts saying one of the men was a minor (left out, as the 1501Z and 2107Z posts mentioning a minor)
skip_nsfw |= {'2113006593503809616'}  # 2305Z: ploukipower paid adult-video promo ("Subscribe to unlock the full video")
skip_nsfw |= {'2113042253740650640','2113221200898150624','2113130971629527128'}  # 2305Z: small-account sexual insults/jokes (cryplutoski and harbents quote of it, bypluvia "slut" post)
EXTRA_PRIVATE |= {'2113712485647696330','2113679139622244405','2113733909699805355'}  # 2305Z: Byron Donalds clip; the unnamed transgender person he calls "sir" and onlookers (private people)
EXTRA_PRIVATE |= {'2113629889568125216'}  # 2305Z: Polymarket post about an unnamed 15-year-old boy arrested in the UK (private minor)
skip_nsfw |= {'2089196330795106457','2113178154525196426'}  # 2307Z: itsmemphishxe 'HxesOnly at streamer pool party' (sexual bait); NkamaBright crude sexual bait line
DESK_OVERRIDE_RUN.update({'2113342518943179172':'politics','2113325263157395456':'tech'})  # 2307Z: VanityFair Kushner excerpt is politics, not sports; JasonDClinton security-leaders post is tech, not science
skip_nsfw |= {'2061920303832260723','2113143833588613393'}  # 0002Z: KingKylieTS porn link post; shutupari_ 'best school uniform? 👀🔥' image of schoolgirls (minors, bait)
EXTRA_PRIVATE |= {'2112357859510137082','2112228163510239232'}  # 0002Z: _Punjabi_Dude_ post on a couple accused of adultery in a Saudi mosque, and the post it quotes (private people)
skip_nsfw |= {'2113200448026902941'}  # 0205Z: akazuann fan-art image with a sexualized adult character holding a child (sexual framing, minors rule, when in doubt)
skip_nsfw |= {'2113134414293049715','2112866758893928700'}  # 0959Z: antislave1 post alleging a streamer's sexual abuse of 14 and 15 year olds (minors rule); likely paid or promoted (OfficialECFC goal clip: 1,661 likes and 16 reposts on 845K views)
skip_nsfw |= {'2113310713712365940'}  # 1107Z: NikkiAArt2 Fat Albert stream post whose text jokes about a character who 'diddled kids' (child sexual abuse reference; left out as a precaution)
skip_nsfw |= {'1736213383530119464'}  # 0059Z: THESPECTORFILES 'i should just kill myself' gun-to-head reaction meme (self-harm)
skip_nsfw |= {'2112886820119707868'}  # 1804Z: mattvanswol post naming a private woman, her street and her children (private information, not captured)
skip_nsfw |= {'1787216385451708501'}  # 1706Z: CollinRugg May 2024 post naming a 17-year-old student charged with crimes (a minor's name and charges; private information, not captured)
EXTRA_PRIVATE |= {'2112648428492619900'}  # 1706Z: mymixtapez post on the 20-year-old who pistol-whipped Rick Ross' son (private people, when in doubt)
skip_nsfw |= {'2106079698648469858','2113621713481007266','2113552164409004489'}  # 1401Z: #FridayVibes stream sexual posts ('Who's being bad with me' bait image; 'Fuck me friday' NSFW tags; crossdress lingerie post)
skip_nsfw |= {'2113317017272889764','2113265746528903455','2113536500373872994'}  # 1401Z: Jiniferl5hv 'Show me your dick'; CrazyWooat69 incest-fetish post; ChromeCrumpet lingerie bait photo
EXTRA_PRIVATE |= {'1906435490221301834'}  # 1401Z: peleasclub before-and-after photos of a person using crack (private person)
skip_nsfw |= {'2106809221270339977','2071960640554500525','2113573701828354463','2113337678087536822'}  # 1459Z: likely paid (dykemedla old HBO clip: 267 likes and 0 replies on 2.48M views, as the dykemedla post left out in 1600Z); sexual bait (Proffesor_9576 'Flat as a board' body post); child sexual abuse allegation against a named person (DocIainDarcy, minors rule, left out as a precaution); likely graphic combat footage (War_footageX, video preview not returned, could not be screened)
EXTRA_PRIVATE |= {'2113586333457518842','2113012452883612099'}  # 1459Z: SnarkingIsLegal photo showing the woman described as Ethan Klein's mistress (public status unclear); WildMediaOnly video of a confrontation between people who are not public figures
skip_nsfw |= {'2112887810600390889','1730251958387122662','2113594639223787818'}  # 1602Z: likely paid (SteveReinharz $AITX stock post: 59 likes and 3 replies on 599K views); likely promoted (NFSCSpeak, Nov 2023: 837 likes on 794K views); willchamberlain post on the marriage certificate of Ilhan Omar's sister naming their father (private family information)
EXTRA_PRIVATE |= {'2113309328686109019','2113348710797037977','2113435917834739975'}  # 1602Z: Excalibyy video of a father and his daughter described as a bully (minor, private family); MPUniversityUS clip of a non-public voter questioning AOC; addisuncain TikTok screenshot of a non-public creator
skip_nsfw |= {'2051528578387558738','2112977615065895377'}  # 1659Z: WomenReadWomen quotes of a 2018 post with sexual content; Family59110 Chinese-language rumor post promising a face-reveal video in a sexual-scandal rumor about a named K-pop idol (likely sexual)
EXTRA_PRIVATE |= {'2113404346247602244'}  # 1659Z: DwightSinghS video of a non-public student accused of scamming food banks
EXTRA_PRIVATE |= {'2113521362207670273'}  # 1808Z: Ethan Klein meme post naming and showing the woman described as his mistress (public status unclear, as in 1459Z)
DESK_OVERRIDE_RUN.update({'2096207075386786042':'ideas','2090044055484833934':'ideas','2113017110536597504':'tech','2113314032778383848':'world','2113367493423313191':'entertainment','2113588025175507323':'internet','1823462923248730619':'internet'})  # 1459Z
EXTRA_PRIVATE |= {'2113316378187104344','2112743668314444083','2112946769604829415','2113366981600555304','2113363733598654664'}  # 1303Z: Plomoterap30 before-and-after video of a person using crack; RadioGenoa 'Future European doctors' video of unnamed people mocked; DrClownPhD video of people in the France riots; realmuckraker undercover videos of Arizona canvassers (none public figures)
DESK_OVERRIDE_RUN.update({'2113170142716666169':'offbeat','2113118985189302489':'politics','2112610011188703483':'politics','2113217413189861490':'entertainment','2112876805539659947':'entertainment','2113231476233744783':'music','2109230390514704591':'music','2113194919229829559':'music','2112810391474520090':'gaming','1672357498571857927':'sports','2035408417314189661':'sports'})  # 1612Z: VehicleTracker8 dashcam hijack satire (golf-ball wording, not sports); Candace Owens on Turning Point USA rumor; Erika Kirk Halloween; Christopher Lloyd 88th birthday; Glee reboot; AI K-pop group; ATEEZ Yunho; NCT Park Jisung; osu! ban; Mason Mount transfer; Alysa Liu skating

EXTRA_PRIVATE |= {'2031592313777172838','2107127083734552874','2113438767738655076'}  # 1905Z: Honest_Cric_fan video of two unnamed boys in a hotel washroom; visegrad24 video of an unnamed high-school student (likely a minor) at a Paris riot; NarongAccord Thai near-miss video with an unnamed truck driver and riders
DESK_OVERRIDE_RUN.update({'2113680701770068067':'ai','2113678299394142433':'politics','2113667772211421244':'politics','2113636993179513337':'politics','2113445064194085176':'politics','2107127083734552874':'world','2113115576558358720':'entertainment','2113267166153936899':'entertainment','2113692448300097708':'ideas','2034473089321607237':'ideas'})  # 1905Z
skip_nsfw |= {'2099079137981800577','2113310763850862881','2113707163105308852','2113520320590365107','2113281707709186138','2113362436371702059','2113464244377473190','2113458457844101316'}  # 2107Z: sexual posts that use the word bulls (six: Seductive/BBC accounts), a like-and-RT giveaway (Haddzy mystery bonuses) and a crypto pump reply, all from the Bulls trend stream
EXTRA_PRIVATE |= {'2113639685683581139'}  # 2107Z: atrupar video of an unnamed college student in line at a Trump rally (not a public figure)
DESK_OVERRIDE_RUN.update({'2113696003069280585':'entertainment','2113662289949901139':'internet'})  # 2107Z: Shanemgillis Kalshi sketch is comedy, not science; rowanfornow Halloween joke is internet
EXTRA_PRIVATE |= {'2113651413020512745','2113303395368935813','2112392213196148818'}  # 0704Z: BulwarkClips and factpostnews posts on the Ramaswamy ad featuring Amy Acton's estranged mother (her family; precaution, as in 2107Z); EcEssie clip mocking an unnamed man on the Tube
DESK_OVERRIDE_RUN.update({'2113820303952650534':'politics','2113386372287623679':'world','2112945193267945682':'world','2113146003343962307':'world','2112625621486682410':'world','2113237332220330125':'world'})  # 0602Z: Musk Talarico post is politics, not science; South Korea mosque and immigration posts are world
skip_nsfw |= {'2045592694072737958'}  # 2005Z: likely paid (NEPOPHOBIA, 822 followers: 1,043 likes and 4 replies on 8.8M views, Apr 2026 clip)
EXTRA_PRIVATE |= {'2112706890799141327','2113522920207339627','2101723123749908875'}  # 2005Z: enklgl reply by a 62-follower account (non-public author of a viral reply); Salvo1st rumor naming h3 podcast staffer Tamara as the woman in the Klein divorce (public status unclear, as in 1808Z); StreetFightsHQ video of an unnamed woman's funeral and family
DESK_OVERRIDE_RUN.update({'2113498867543245258':'offbeat','2113701145138876532':'sports','2113717544817426676':'sports','2113696043854401828':'sports','2113718262211264524':'sports'})  # 2005Z: AjitYadav260 banana-worm video is offbeat, not ai (it only tags @grok); 247Sports Jesse Legree and the Skye Blakely world all-around posts are sports
skip_nsfw |= {'2112758989306094060','2113291850127696073','2113488169983410507','2113688372212580862'}  # 0000Z: numehamiris photos of a private person and the post quoting them about her sexual preferences (sexual, private person); likely promoted (FallonTonight: 4,458 likes and 38 replies on 6.3M views; FischerKing64: 630 likes on 661K views)
DESK_OVERRIDE_RUN.update({'2113764536100798527':'sports','2113697902916751661':'ai','2113718797505036665':'ai'})  # 0000Z: chicagobulls first win is sports; jack Dessa speech model and OpenAI training-security post are ai
skip_nsfw |= {'2113322517636997578','2110417671586263300','1978299241928818738','2113130466979295292'}  # 0103Z: 6iixfoot post about a performer's erotic movie scenes (sexual); likely promoted (Gotimehomie series post: 18 likes on 1.6M views; loveisembrrsing Yamamoto clip: 267 likes on 2.8M views; konchacortez 'video trend watch': 311 likes on 768K views)
skip_nsfw |= {'2070281545819234425','2113432308175061205'}  # 0200Z: likely promoted (foxone FOX One sign-up ad, Jun 2026 origin: 2,688 likes and 0 replies on 3.9M views); suicide wording (twinturbowank 'i could just commit suicide' joke post, left out as the suicide-wording posts in 0203Z and 1900Z)
DESK_OVERRIDE_RUN.update({'2113798038586282014':'entertainment'})  # 0200Z: DiscussingFilm Avengers: Doomsday teaser is entertainment, not markets
DESK_OVERRIDE_RUN.update({'2113386066199945633':'politics','2112891818480218468':'internet','2112199762296684598':'world','2015180028623851750':'politics'})  # 0400Z: MHTruthUltra Kushner post is politics, not sports; Omgemeraldddd old-internet post is internet; D_Tarczynski Poland post is world; Hegseth ICE post is politics
skip_nsfw |= {'2113792950673293351'}  # 0303Z: 30GotNext Giannis post with a racial slur (as the 2207Z BronGotGame Tatum post)
skip_nsfw |= {'2113646634144010437','2113045645376327917','2113106524276920628','2096570562625655088','2110732066585530537'}  # 0303Z: likely promoted (america Talarico clip: 2,403 likes and 545 replies on 31.0M views); likely paid (zavanchy Angel Reese clip: 8,584 likes and 2 replies on 1.8M views; SMHighlights1 Ty Lue clip: 270 likes and 5 replies on 1.17M views; LunarResearcher link-only post, Sep 2026: 700 likes and 19 replies on 1.4M views; ThroawayLeMain, 196 followers: 3,246 likes and 34 replies on 1.43M views)
skip_nsfw |= {'2113899296663744854','2113825577383903344'}  # 0804Z: JalisaAvari hashtag-stuffed 'get monetized and paid on X' promo in the #CulturalCreditMatters stream (spam); likely promoted (kevinnbass Talarico clip compilation: 555 likes and 42 replies on 417K views, as the KanekoaTheGreat Talarico posts left out in 1807Z and 1803Z)
DESK_OVERRIDE_RUN.update({'2113474211968659757':'entertainment'})  # 0804Z: Perp338 Emma Watson and JK Rowling post is entertainment, not sports
skip_nsfw |= {'2066020254225150298','2113677291674820992','2113668379353534473','2093986240433402191','2113635362702508145'}  # 0905Z: InNudemovie 'nude sex scenes' post in the Thompson stream (sexual); MessiahYaniss16 joke sexualizing a minor; nigerianprynce post with a racial slur; likely promoted (Real_jaeflex movie-scene question: 65 likes on 15.2M views; cityoftoronto speed-limit notice: 924 likes on 2.9M views)
EXTRA_PRIVATE |= {'2113783957494075795'}  # 0905Z: Neutral_OC clip of a father leaving two children at a door (private people)
skip_nsfw |= {'2111388791663661126','1690385777945939968','2113888297122488826','2090511693579211126','2111018613159199143','2113861688370073898','2113643042045612161','2099497286208262326'}  # 1003Z: THROATBREAKER69 sexual text; DaneHardon 'Have a good Saturday' adult-performer clip and Stephan47616460 'Good saturday with @imevesweet' (sexual, in the Good Saturday stream); likely paid or promoted (LOS1OgGgCLgTDTW link-only video: 55 likes on 3.1M views; zee_zhu_ movie question: 51 likes on 659K views; Teslaconomics Grok Bot finances post: 326 likes on 636K views, as the earlier Teslaconomics posts; KalshiSports Man City odds post: 720 likes on 801K views; ArmedMaidan drone raffle fundraiser: 330 likes on 669K views)
EXTRA_PRIVATE |= {'2113610780490997947'}  # 1003Z: fforcejs screenshot of an Instagram message request from a private account (itscandy.ke, 206 followers), shown by handle
skip_nsfw |= {'2113851868673937537','2046150707611644240','2113170669877997889','2112803655694925886'}  # 1105Z: likely paid or promoted: OBOROCK Marugame udon text (737 likes and 5 reposts on 1.07M views); 7ikm33 fire-detector clip, April origin (3,399 likes on 11.0M views); gauravsbuilding Fastlane ad-product launch (product promo, 1,341 likes on 824K views); FABIOTHEBARB link-only photo (4,266 likes on 4.4M views)
DESK_OVERRIDE_RUN.update({'2113643573338046654':'sports','2113261462990766535':'world'})  # 1105Z desk fixes: FabrizioRomano Ronaldo 982nd goal is sports; easydigita APC post is Nigerian politics, not the Warriors game
skip_nsfw |= {'2113733487375077458','2113833301081571541'}  # 1204Z: likely paid or promoted: icreatelife 'here's my little team' bot-product post (198 likes and 25 reposts on 535K views); ClownWorld '$260 a month ... @bot' product plug (1,084 likes on 552K views)
EXTRA_PRIVATE |= {'2113868946960986257'}  # 1204Z: 75secondes post about a newborn baby (private person)
DESK_OVERRIDE_RUN.update({'2113675605451456873':'business','2096265762948383174':'sports','2113868946960986257':'offbeat'})  # 1204Z desk fixes: LeadingReport Musk CNN/CBS stake is business; UTDCJ_ Mateus Fernandes away record is sports; 75secondes baby story is offbeat
skip_nsfw |= {'2113503182387335439','2113784407421263977','2113946746493534671'}  # 1307Z: sexual content: dee_elleea sex question (quote stream); DefundNintendo explicit sexual reply; fOx1257067 'Good Saturday' post about Sydney Sweeney lingerie photos
skip_nsfw |= {'2112574886421901822'}  # 1307Z: likely paid or promoted: unicodef1wn 'one guide ... Save it' bot-setup guide plug (561 likes and 61 replies on 982K views)
DESK_OVERRIDE_RUN.update({'2113730310047437083':'politics','2113354752935522420':'world','2113688428348948784':'sports','2113665255088017698':'offbeat','2113750562042769432':'gaming','2113797331212546251':'entertainment'})  # 1307Z desk fixes: kingkapoor72 London attack claim is politics; KalendarNews Sofia journalist attack is world; Messi award is sports; cat photo is offbeat; Sweeney/Valve AI-disclosure is gaming; Avengers Doomsday look is entertainment
skip_nsfw |= {'2099471623564796101','2110707984137335151'}  # 1404Z: sexual content: masterchris_of adult-creator clip ('Full vid (no ppv)'); Oceanbreeze473 sign-language interpreter for 'WAP' (explicit lyrics)
EXTRA_PRIVATE |= {'2113678119903313986','2112530523583140226','1920564365792510240','2113843714472714391','2113416412471677099'}  # 1404Z: SeeRacists Queens broker and couple (private people, pile-on); Hoint1967 two strangers seated together; reactions_es man in meme clip; AkademiksTV Ray J's friend's house; missconceitedxx 17-follower clip of a private person
skip_nsfw |= {'2113860764264227015'}  # 1505Z: likely paid or promoted: tetsuoai 'Super intelligent Beauty' AI-character video (1,589 likes and 171 replies on 673K views)
EXTRA_PRIVATE |= {'2113307573482934521','2113854786709987366'}  # 1505Z: lesbianlotuss TikTok screenshots of private users (a dress post and its comments, with usernames); viewsceo brawl video with an unnamed man accused of being a predator (private person, pile-on)
skip_nsfw |= {'2099820757110899127','2113819491226333412','2098854910670573983','2113631561635491920'}  # 1604Z: likely paid or promoted: real_jfkjr01 'BOMB IN THE WHITE HOUSE' clickbait video (2,079 followers; 1,812 likes on 3.5M views) and the real_MAGAFOX copy carrying the same video (208 likes on 339K views); LoneStar_PAC attack video on Talarico (PAC ad; 733 likes on 1.2M views); CodyBrownBets 'Tight End Day prep' photo (betting account; 1,632 likes on 756K views)
skip_nsfw |= {'2098423452768284880'}  # 1700Z: likely paid (ccxxrree__1 'Trend + Viral Videos & photos' post, Sep 11: 41 likes and 9 replies on 8.0M views)
skip_nsfw |= {'2113854387122848178','2088642671304712455'}  # 1907Z: graphic description of the rape of a child (zip99900 Cho Doo-soon post); likely paid (Talhaa10_ link-only post, Aug 15: 498 likes on 6.16M views)
DESK_OVERRIDE_RUN.update({'2113831337652265060':'sports','2113913307849785855':'world','2114055025161064570':'gaming','2113796696790700541':'music'})  # 1907Z desk fixes: FabrizioRomano Xabi Alonso Chelsea quote is sports; europa Eagle's Nest fire is world; Fortnite post is gaming; Chuu show post is music
EXTRA_PRIVATE |= {'2113737667540345288','2113761509436240274'}  # 1700Z: its__Scarlettt video of an unnamed father and daughter (private people); hoesluvkweku video of an unnamed couple ('Darnell', private people)
DESK_OVERRIDE_RUN.update({'2113763920716668992':'politics','2113938616204644772':'gaming','2113690702181773650':'justice','2114050872045138051':'sports','2114026169813414022':'politics'})  # 1807Z desk fixes: WesternLensman Bulwark/Musk clip is politics; NIKKE_en PV is gaming; KAMCNews fentanyl sentencing is justice; stoolpresidente Michigan halftime is sports; elonmusk Talarico post is politics
skip_nsfw |= {'2114022773651832927','2006631169497120772','2073114607930188243','2011001552996040751'}  # 2007Z: sexual text (_everybodystype used-condoms post); slur against immigrants (Jukkamakko65792 'matuja' post); likely paid (WCLegendKyks link-only post: 10 likes and 0 replies on 1.7M views; dykemedla Susana Vieira video, Jan 12: 289 likes and 1 reply on 1.3M views)
EXTRA_PRIVATE |= {'2113728312644075932'}  # 2007Z: 2eviltwerp video mocking an unnamed high-school student (private person, likely a minor)
DESK_OVERRIDE_RUN.update({'2113684608370057655':'business','2113957614417502631':'sports','2063655005559648507':'sports','2114064620411666919':'politics','2113209811638870291':'life','2113217974173905092':'life'})  # 2007Z desk fixes: Polymarket Airbnb hosts business; amjushere Aston Villa sports; shanethecnfsr Kimi Antonelli F1 sports; elonmusk tribal politics post politics; UltraLinx old-car post life; literarrium hangout-space post life
skip_nsfw |= {'2113617662886433166','2113616948810461216','2101507510406709599','2113894984705573345'}  # 2103Z: dehumanizing language about immigrants and a call to identify children (TRobinsonNewEra 'Invader youth ... Make these rats famous' Belfast park video; freedomdad73 posts the same video of children being attacked, 'attack on our kids by foreigners'); likely paid (theepunisher11 link-only video, Sep 20: 6 likes on 825K views, 4 followers; Katheri23760769 link-only listicle 'Why Professional Chefs Avoid Nonstick Pans', 979 likes on 609K views)
EXTRA_PRIVATE |= {'2114046541912523141'}  # 2103Z: iswiminnachos display name says the account holder is a minor
skip_nsfw |= {'2113224606656155854'}  # 2300Z: likely paid (sevenart_ai AI short-drama product pitch: 1,142 followers, 1,610 likes on 4.5M views)
EXTRA_PRIVATE |= {'2113835066078196167','2112631426705400283'}  # 2300Z: OliLondonTV post about an Afghan man not named as a public figure; Nayainshambles asks whether people were 'this racist at 15/16' over an attached photo (likely a teenager; precaution)
DESK_OVERRIDE_RUN.update({'2112645157799776667':'politics','2114019665043190046':'politics','2113382389837599053':'entertainment','2114008816522318227':'sports','1961882403196309858':'sports','2112094450461859967':'defense','2113778747782685160':'defense','2113759884760297642':'world','2113835066078196167':'world','2113726579486364059':None})  # 2300Z: Iowa-trend early-voting and campaign-ad posts are politics; desk fixes for new posts
skip_nsfw |= {'2093036949129077044','2026352105251025234','2112895167497703665','2113847834667807117','2114129731952210402','2112325287665176717'}  # 0003Z: likely paid (OHIO811 utility ad: 498 likes on 1.49M views; Schwarzenegger fiber product pitch: 3,007 likes on 759K views; starmexxx bare link: 183 likes on 724K views; ShowCaseShabazz: 610 likes on 722K views, flagged likely paid before in 0308Z; gmannVOLS clip: 117 likes on 401K views in about an hour; barstoolsports Oct 19 clip: 306 likes on 287K views)
skip_nsfw |= {'2036790852677165308'}  # 0003Z: graphic (hippyygoat video post describing a burnt and nailed baby)
EXTRA_PRIVATE |= {'2099518798931824679','2113717222732685468','2114080240431755588'}  # 0003Z: furqrahim (100 followers) post about his mother; bourne_beth2345 video at a girls' high school volleyball game (students; precaution); ChuksEricE clip of a guest not named as a public figure at a convention in Benin
DESK_OVERRIDE_RUN.update({'2113636527972536714':'politics','2113717222732685468':'politics','2113856400174764258':'politics','2099134058265542859':'politics','2113643164510966194':'politics','2113559586003132913':'gaming','2113762242327892456':'tech','2113956172055081028':'entertainment','2114080240431755588':'internet'})  # 0003Z: Stella Parton Tennessee voting machine (Tennessee trend); Beth Bourne and Brandi Kruse women's-sports protests; Babylon Bee clip; Epstein files; Kyedae/TenZ; Samsung TV microphones; Peller; Benin convention
DESK_OVERRIDE_RUN.update({'2110049870337716393':'politics','2113418071792906455':'politics','2114010276295320028':'world','1859677023075213356':'sports','2113982676436992413':'internet','2113633752383373374':'world'})  # 2103Z desk fixes: libsoftiktok Indiana council candidate politics; realDonaldTrump Indiana early voting politics; lazarorosa25 Lula Copacabana world; acdmma_ Oliveira/Chandler sports; Anomali210830 Pythagorean Theorem Day internet; Le_Crapaud47 French post on communists and Islam world
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
    _refby2 = [q2 for q in _refby for q2 in posts_by_id.values() if q['id'] in [r['id'] for r in (q2.get('referenced_tweets') or [])] + list((q2.get('attachments') or {}).get('media_source_tweet_id') or [])]
    _old_ref = any((snowflake_ts(q['id']) - snowflake_ts(pid)) > 7*86400 for q in _refby + _refby2)
    if (age_d > 7 and (ref_counts.get(pid,0) >= 1 or _old_ref)) or 'old_content' in (prior_meta.get(pid,{}).get('flags') or []):
        flags.append('old_content')
    if pid in OLD_VIA_CHAIN and 'old_content' not in flags:
        flags.append('old_content')  # reached through a reference chain from a post read this run more than 7 days newer
    if 'giamanco' in (text or '').lower() and 'private_individual' not in flags:
        flags.append('private_individual')
    if pid in private_ids or pid in EXTRA_PRIVATE:
        flags.append('private_individual')
    flags = list(dict.fromkeys(flags))
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
    if pid in DESK_OVERRIDE_RUN:
        rec['desk'] = DESK_OVERRIDE_RUN[pid]
    elif pid in DESK_OVERRIDE_1807:
        rec['desk'] = DESK_OVERRIDE_1807[pid]
    elif pid in DESK_OVERRIDE:
        rec['desk'] = DESK_OVERRIDE[pid]
    elif pid in PRIOR_DESK and PRIOR_DESK[pid] in desk_floor:
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
        if s.startswith('trend.') and not s.endswith('.media'):
            trend_posts[s.split('.',1)[1]].append(pid)

# one event aliases
for a,b in [('Niners','Commanders'),('Commanders','Niners'),('Niners','49ers'),('Commanders','49ers'),('Rays','Junior Caminero'),('Rays','#WorldSeries'),('#WorldSeries','Rays'),('49ers','Niners'),('Mike Evans','49ers'),('Rays','Yandy Diaz'),('Jayden Daniels','Dan Quinn'),('Dan Quinn','Jayden Daniels'),('Monday Night Football','Kittle'),('Kittle','Monday Night Football'),('Bronny','Knecht'),('Knecht','Bronny'),('Bronny','Dalton Knecht'),('Dalton Knecht','Bronny'),('New Mexico','New America'),('#COYS','Tottenham'),('Ryan Day','Ohio State'),('Jeremiah Smith','Ohio State'),('Sayin','Julian Sayin'),('Sayin','Ohio State'),('Jeremiah Smith','Julian Sayin'),('Arch Manning','Gators'),('Sark','Gators'),('Arch Manning','#HookEm'),('Sark','#HookEm'),('Sark','Arch Manning'),('Arch Manning','Sark'),('Ryan Day','Indiana'),('Arthur Smith','Ohio State'),('Betis','Lamine'),('Isak','Munoz'),('Munoz','Isak'),('Isak','Brentford'),('Munoz','Brentford'),('#MrFanboyEP8','MR FANBOY CHAPTER 8'),('Everton','Pedro Neto'),('Everton','#EVECHE'),('#CORTIS_NOLFest2026','IDEA BANK'),('#CORTIS_NOLFest2026','JAMES THE ULTIMATE PHENOMENON'),('#EVECHE', 'Everton'), ('#EVECHE', 'Pedro Neto'), ('#EVECHE', 'Caicedo'), ('#EVECHE', 'Hato'), ('#EVECHE', 'Paul Tierney'), ('Everton', '#EVECHE'), ('Everton', 'Pedro Neto'), ('Everton', 'Caicedo'), ('Everton', 'Hato'), ('Everton', 'Paul Tierney'), ('Pedro Neto', '#EVECHE'), ('Pedro Neto', 'Everton'), ('Pedro Neto', 'Caicedo'), ('Pedro Neto', 'Hato'), ('Pedro Neto', 'Paul Tierney'), ('Caicedo', '#EVECHE'), ('Caicedo', 'Everton'), ('Caicedo', 'Pedro Neto'), ('Caicedo', 'Hato'), ('Caicedo', 'Paul Tierney'), ('Hato', '#EVECHE'), ('Hato', 'Everton'), ('Hato', 'Pedro Neto'), ('Hato', 'Caicedo'), ('Hato', 'Paul Tierney'), ('Paul Tierney', '#EVECHE'), ('Paul Tierney', 'Everton'), ('Paul Tierney', 'Pedro Neto'), ('Paul Tierney', 'Caicedo'), ('Paul Tierney', 'Hato')] + [('JAMES THE ULTIMATE PHENOMENON', '#JAMESUnparalleled'), ('JAMES THE ULTIMATE PHENOMENON', 'IDEA BANK'), ('JAMES THE ULTIMATE PHENOMENON', 'CHAOWESOME'), ('JAMES THE ULTIMATE PHENOMENON', '#CORTIS_NOLFest2026'), ('JAMES THE ULTIMATE PHENOMENON', 'NOL Festival'), ('JAMES THE ULTIMATE PHENOMENON', 'KEONHO CAPTIVATES THE LENS'), ('JAMES THE ULTIMATE PHENOMENON', 'IKEONIC'), ('JAMES THE ULTIMATE PHENOMENON', 'ACEKEON MAKNAE'), ('JAMES THE ULTIMATE PHENOMENON', '5TH GEN IT BOY'), ('JAMES THE ULTIMATE PHENOMENON', 'HOGAN EFFECT'), ('#JAMESUnparalleled', 'JAMES THE ULTIMATE PHENOMENON'), ('#JAMESUnparalleled', 'IDEA BANK'), ('#JAMESUnparalleled', 'CHAOWESOME'), ('#JAMESUnparalleled', '#CORTIS_NOLFest2026'), ('#JAMESUnparalleled', 'NOL Festival'), ('#JAMESUnparalleled', 'KEONHO CAPTIVATES THE LENS'), ('#JAMESUnparalleled', 'IKEONIC'), ('#JAMESUnparalleled', 'ACEKEON MAKNAE'), ('#JAMESUnparalleled', '5TH GEN IT BOY'), ('#JAMESUnparalleled', 'HOGAN EFFECT'), ('IDEA BANK', 'JAMES THE ULTIMATE PHENOMENON'), ('IDEA BANK', '#JAMESUnparalleled'), ('IDEA BANK', 'CHAOWESOME'), ('IDEA BANK', '#CORTIS_NOLFest2026'), ('IDEA BANK', 'NOL Festival'), ('IDEA BANK', 'KEONHO CAPTIVATES THE LENS'), ('IDEA BANK', 'IKEONIC'), ('IDEA BANK', 'ACEKEON MAKNAE'), ('IDEA BANK', '5TH GEN IT BOY'), ('IDEA BANK', 'HOGAN EFFECT'), ('CHAOWESOME', 'JAMES THE ULTIMATE PHENOMENON'), ('CHAOWESOME', '#JAMESUnparalleled'), ('CHAOWESOME', 'IDEA BANK'), ('CHAOWESOME', '#CORTIS_NOLFest2026'), ('CHAOWESOME', 'NOL Festival'), ('CHAOWESOME', 'KEONHO CAPTIVATES THE LENS'), ('CHAOWESOME', 'IKEONIC'), ('CHAOWESOME', 'ACEKEON MAKNAE'), ('CHAOWESOME', '5TH GEN IT BOY'), ('CHAOWESOME', 'HOGAN EFFECT'), ('#CORTIS_NOLFest2026', 'JAMES THE ULTIMATE PHENOMENON'), ('#CORTIS_NOLFest2026', '#JAMESUnparalleled'), ('#CORTIS_NOLFest2026', 'IDEA BANK'), ('#CORTIS_NOLFest2026', 'CHAOWESOME'), ('#CORTIS_NOLFest2026', 'NOL Festival'), ('#CORTIS_NOLFest2026', 'KEONHO CAPTIVATES THE LENS'), ('#CORTIS_NOLFest2026', 'IKEONIC'), ('#CORTIS_NOLFest2026', 'ACEKEON MAKNAE'), ('#CORTIS_NOLFest2026', '5TH GEN IT BOY'), ('#CORTIS_NOLFest2026', 'HOGAN EFFECT'), ('NOL Festival', 'JAMES THE ULTIMATE PHENOMENON'), ('NOL Festival', '#JAMESUnparalleled'), ('NOL Festival', 'IDEA BANK'), ('NOL Festival', 'CHAOWESOME'), ('NOL Festival', '#CORTIS_NOLFest2026'), ('NOL Festival', 'KEONHO CAPTIVATES THE LENS'), ('NOL Festival', 'IKEONIC'), ('NOL Festival', 'ACEKEON MAKNAE'), ('NOL Festival', '5TH GEN IT BOY'), ('NOL Festival', 'HOGAN EFFECT'), ('KEONHO CAPTIVATES THE LENS', 'JAMES THE ULTIMATE PHENOMENON'), ('KEONHO CAPTIVATES THE LENS', '#JAMESUnparalleled'), ('KEONHO CAPTIVATES THE LENS', 'IDEA BANK'), ('KEONHO CAPTIVATES THE LENS', 'CHAOWESOME'), ('KEONHO CAPTIVATES THE LENS', '#CORTIS_NOLFest2026'), ('KEONHO CAPTIVATES THE LENS', 'NOL Festival'), ('KEONHO CAPTIVATES THE LENS', 'IKEONIC'), ('KEONHO CAPTIVATES THE LENS', 'ACEKEON MAKNAE'), ('KEONHO CAPTIVATES THE LENS', '5TH GEN IT BOY'), ('KEONHO CAPTIVATES THE LENS', 'HOGAN EFFECT'), ('IKEONIC', 'JAMES THE ULTIMATE PHENOMENON'), ('IKEONIC', '#JAMESUnparalleled'), ('IKEONIC', 'IDEA BANK'), ('IKEONIC', 'CHAOWESOME'), ('IKEONIC', '#CORTIS_NOLFest2026'), ('IKEONIC', 'NOL Festival'), ('IKEONIC', 'KEONHO CAPTIVATES THE LENS'), ('IKEONIC', 'ACEKEON MAKNAE'), ('IKEONIC', '5TH GEN IT BOY'), ('IKEONIC', 'HOGAN EFFECT'), ('ACEKEON MAKNAE', 'JAMES THE ULTIMATE PHENOMENON'), ('ACEKEON MAKNAE', '#JAMESUnparalleled'), ('ACEKEON MAKNAE', 'IDEA BANK'), ('ACEKEON MAKNAE', 'CHAOWESOME'), ('ACEKEON MAKNAE', '#CORTIS_NOLFest2026'), ('ACEKEON MAKNAE', 'NOL Festival'), ('ACEKEON MAKNAE', 'KEONHO CAPTIVATES THE LENS'), ('ACEKEON MAKNAE', 'IKEONIC'), ('ACEKEON MAKNAE', '5TH GEN IT BOY'), ('ACEKEON MAKNAE', 'HOGAN EFFECT'), ('5TH GEN IT BOY', 'JAMES THE ULTIMATE PHENOMENON'), ('5TH GEN IT BOY', '#JAMESUnparalleled'), ('5TH GEN IT BOY', 'IDEA BANK'), ('5TH GEN IT BOY', 'CHAOWESOME'), ('5TH GEN IT BOY', '#CORTIS_NOLFest2026'), ('5TH GEN IT BOY', 'NOL Festival'), ('5TH GEN IT BOY', 'KEONHO CAPTIVATES THE LENS'), ('5TH GEN IT BOY', 'IKEONIC'), ('5TH GEN IT BOY', 'ACEKEON MAKNAE'), ('5TH GEN IT BOY', 'HOGAN EFFECT'), ('HOGAN EFFECT', 'JAMES THE ULTIMATE PHENOMENON'), ('HOGAN EFFECT', '#JAMESUnparalleled'), ('HOGAN EFFECT', 'IDEA BANK'), ('HOGAN EFFECT', 'CHAOWESOME'), ('HOGAN EFFECT', '#CORTIS_NOLFest2026'), ('HOGAN EFFECT', 'NOL Festival'), ('HOGAN EFFECT', 'KEONHO CAPTIVATES THE LENS'), ('HOGAN EFFECT', 'IKEONIC'), ('HOGAN EFFECT', 'ACEKEON MAKNAE'), ('HOGAN EFFECT', '5TH GEN IT BOY')] + [('KEONHO CAPTIVATES THE LENS', 'NOL Festival'), ('KEONHO CAPTIVATES THE LENS', 'IKEONIC'), ('KEONHO CAPTIVATES THE LENS', 'ACEKEON MAKNAE'), ('KEONHO CAPTIVATES THE LENS', '5TH GEN IT BOY'), ('KEONHO CAPTIVATES THE LENS', 'HOGAN EFFECT'), ('NOL Festival', 'KEONHO CAPTIVATES THE LENS'), ('NOL Festival', 'IKEONIC'), ('NOL Festival', 'ACEKEON MAKNAE'), ('NOL Festival', '5TH GEN IT BOY'), ('NOL Festival', 'HOGAN EFFECT'), ('IKEONIC', 'KEONHO CAPTIVATES THE LENS'), ('IKEONIC', 'NOL Festival'), ('IKEONIC', 'ACEKEON MAKNAE'), ('IKEONIC', '5TH GEN IT BOY'), ('IKEONIC', 'HOGAN EFFECT'), ('ACEKEON MAKNAE', 'KEONHO CAPTIVATES THE LENS'), ('ACEKEON MAKNAE', 'NOL Festival'), ('ACEKEON MAKNAE', 'IKEONIC'), ('ACEKEON MAKNAE', '5TH GEN IT BOY'), ('ACEKEON MAKNAE', 'HOGAN EFFECT'), ('5TH GEN IT BOY', 'KEONHO CAPTIVATES THE LENS'), ('5TH GEN IT BOY', 'NOL Festival'), ('5TH GEN IT BOY', 'IKEONIC'), ('5TH GEN IT BOY', 'ACEKEON MAKNAE'), ('5TH GEN IT BOY', 'HOGAN EFFECT'), ('HOGAN EFFECT', 'KEONHO CAPTIVATES THE LENS'), ('HOGAN EFFECT', 'NOL Festival'), ('HOGAN EFFECT', 'IKEONIC'), ('HOGAN EFFECT', 'ACEKEON MAKNAE'), ('HOGAN EFFECT', '5TH GEN IT BOY'),('#LingOrmBetweenUsConcertD1','THE WORLD BETWEEN LINGORM D1'),('THE WORLD BETWEEN LINGORM D1','#LingOrmBetweenUsConcertD1'),('Kimmel','Johnny Carson'),('Johnny Carson','Kimmel'),('PERTHSANTA LOST IN LOVE','#PerthSantaFMinMacau'),('#PerthSantaFMinMacau','PERTHSANTA LOST IN LOVE'),('Mamu','Kessler'),('Kessler','Mamu'),('YK Osiris','Deshae'),('Deshae','YK Osiris'),('YK Osiris','ash trevino'),('YK Osiris','Adin Ross'),('ash trevino','Adin Ross'),('Adin Ross','ash trevino'),('Memphis','Marcus Stokes'),('Marcus Stokes','Memphis'),('Memphis','Tulane'),('Tulane','Memphis'),('Baron Corbin','#SmackDown'),('#SmackDown','Baron Corbin'),('#SmackDown','Nikki Bella'),('Nikki Bella','#SmackDown'),('San Clemente','Norte Fire'),('Norte Fire','San Clemente'),('#NorteFire','San Clemente'),('San Clemente','#NorteFire'),('Scaramucci','Press Secretary'),('Scaramucci','Katie Zacharia'),('#The24thBloomOfPor','POR 24TH BIRTHDAY'),('Good Friday','Remember Everyone Deployed'),('Good Friday','RED Friday'),('RED Friday','Remember Everyone Deployed'),('Julian Sayin','Hoover'),('Hoover','Julian Sayin'),('Julian Sayin','Ohio State'),('Ohio State','Julian Sayin'),('Hoover','Ohio State'),('Ohio State','Hoover'),('Julian Sayin','#GoBucks'),('Julian Sayin','#iufb'),('Hoover','#iufb'),('Hoover','#GoBucks'),('Indiana','Ohio State'),('Indiana','Sayin'),('Indiana','Jeremiah Smith'),('Indiana','Hoover'),('Indiana','Ryan Day'),('Indiana','#GoBucks'),('Indiana','#iufb'),('Texas','Arch Manning'),('Texas','Gators'),('Texas','#HookEm'),('Texas','Sark'),('Nick Marsh','Michigan State'),('Fahey','NHL'),('Macron','Paris'),('Macron','The French'),('Arch Manning','Arch'),('Nick Marsh','Marsh'),('Auburn','Gunner'),('Auburn','Georgia'),('Georgia','Gunner'),('Georgia','WAR DAMN EAGLE'),('Georgia','War Eagle'),('Bryce Underwood','Tommy Carr'),('Tommy Carr','Bryce Underwood'),('Bryce Underwood','Michigan'),('Tommy Carr','Michigan'),('Rhyne','#WNBAfinals'),('Rocco Becht','Tennessee'),('Macron','The French'),('The French','Macron'),('The French','Paris'),('Grubb','DeBoer'),('Auburn','War Eagle'),('War Eagle','Auburn'),('Auburn','War Damn Eagle'),('War Eagle','War Damn Eagle'),('Tennessee','Go Vols'),('Tennessee','DeBoer'),('Tennessee','Grubb'),('Florida State','Miami'),('Florida State','Mensah'),('Florida State','Malachi Toney'),('Miami','Malachi Toney'),('Mensah','Malachi Toney'),('Miami','Mensah'),('Mateer','Oklahoma'),('Buckley','Alabama'),('Notre Dame','CJ Carr'),('CJ Carr','Notre Dame'),('Notre Dame','Provo'),('Provo','Notre Dame'),('CJ Carr','Provo'),('Provo','CJ Carr'),('Kentucky','Mateer'),('Mateer','Kentucky'),('Stein','Kentucky'),('Kentucky','Stein'),('Clockwork Carnage','#AEWWrestleDream'),('#AEWWrestleDream','Clockwork Carnage'),('Clockwork Carnage','Ospreay'),('Utah','Big 12'),('Miami','Florida State'),('Brock Thomas','Dan Lanning'),('Dan Lanning','Brock Thomas'),('Brock Thomas','Raiola'),('Dan Lanning','Raiola'),('#LingOrmBetweenUsConcertD2','THE WORLD BETWEEN LINGORM D2'),('THE WORLD BETWEEN LINGORM D2','#LingOrmBetweenUsConcertD2'),('OH MY BEST DAY WITH FOURTH','#FourthConcertD3'),('#FourthConcertD3','OH MY BEST DAY WITH FOURTH'),('#YaoRunhaoRuinsPapergames','#BladeRunnerStandsWithAbuser'),('#BladeRunnerStandsWithAbuser','#YaoRunhaoRuinsPapergames'),('#YaoRunhaoRuinsPapergames','#全球请辞中国叠纸姚润昊'),('Nico Collins','#HTownMade')]:
    if trend_posts.get(a):
        trend_posts[b] = list(dict.fromkeys((trend_posts.get(b) or []) + trend_posts[a]))
        trend_posts[a] = list(dict.fromkeys((trend_posts.get(a) or []) + trend_posts[b]))

for _n in ('Julian Sayin','Ohio State','#GoBucks','#iufb'):
    trend_posts[_n] = [x for x in (trend_posts.get(_n) or []) if x != '2110789095257747679']  # 1706Z: a vacuum-cleaner joke from the Hoover stream, not the Ohio State v Indiana game

trend_posts['Beck'] = [x for x in (trend_posts.get('Beck') or []) if x != '2113461868312637891']  # 2159Z: NEWSMAX Glenn Beck clip, not Jason Beck in Indiana v Michigan

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
        if region == 'WW' and name in ('緊急地震速報','M9.9','マグニチュード9.9'):
            for pid in best_for_trend(name, 5):
                if pid in posts_by_sel and pid not in pids:
                    pids.append(pid)
                if len(pids) >= 3:
                    break
        if region == 'US':
            candidates_t = best_for_trend(name, 5)
            # for event clusters, also try related
            for pid in candidates_t:
                if pid in posts_by_sel and pid not in TREND_OFF.get(name, ()):
                    pids.append(pid)
                if len(pids) >= 3:
                    break
            # also from trend stream source
            for pid in (trend_posts.get(name) or []):
                if pid in posts_by_sel and pid not in pids and pid not in TREND_OFF.get(name, ()):
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

trends = parse_trends(raw['trends_us'], 'US')

def sweep(id_, kind, desk, method, window, status, reason, post_ids):
    return {
        'id': id_, 'kind': kind, 'desk': desk, 'method': method,
        'window_hours': window, 'status': status, 'reason': reason,
        'post_ids': post_ids or []
    }

watch_ordered = []
seenw=set()
for batch in ('watch0','watch1','watch2','watch3'):
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
SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}
sweeps.append(sweep('watch','watch',None,
    f'get_posts_by_ids of requests/watch.json ({len(watch_json)} ids), every post first captured in the last 6 hours and under 24 hours old, posts first captured 6 to 24 hours ago that gained at least 2 percent between their last two readings, then the {len(ADDED_STORY)} ids cited in pulse/current.json or in published stories (moments/) that were not otherwise on the list, (this 00Z run is a fourth hour, so the rest of the last 24 hours was added, slowest-growing last; with every pulse- and story-cited post placed right after the watch.json ids, then the six-hour, still-gaining and rest-of-24-hour tiers, the list was 602 long, so the 400 cap left out the 40 last six-hour posts, the 133 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post); {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 4 reads; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id,referenced_tweets.id.author_id',
    None,'ok',None, watch_ordered))
sweeps.append(sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max 20',None,'ok',None,[]))
sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20: not read this run (budget)',None,'skipped','not read this run to keep to about 20 reads; last read in 2026-10-23T0002Z',[]))
sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed one hop from every post read (and a second hop), including attachments.media_source_tweet_id; sensors news/money/science (one read each); trend names "Tennessee", "Big 12" and "Dan Lanning" ("<name> lang:en is:retweet", newest first, 25 each; three of the top-ten US names with no posts attached in 2300Z: "Tennessee" (second; South Carolina beat No. 11 Tennessee on a field goal with no time left; "South Carolina" (third), "Heupel" (ninth) and "David Smith" are the same game), "Big 12" (fifth; UCF beat No. 2 BYU in double overtime and Cincinnati beat Texas Tech; "2 BYU" (sixth) and "#BYUvsUCF" (eighth) are the same game as "Scott Frost" (first, attached in 2300Z)) and "Dan Lanning" (tenth; Oregon lost to Illinois); "Iowa" (fourth) and "Cheesecake Factory" (seventh) were attached in 2300Z); quote/repost words is/you + and (quoted); hourly desks politics/entertainment/sports/internet; two screening reads by id (100 unread referenced posts, most pointed-at first, then the 20 second-hop and remaining posts in the second read); story clusters not read for the budget; screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '2 quote pages + 1 repost page (budget), common words "is", "you" and "and", each quoted so X does not reject a bare stopword: ("is" lang:en is:quote -is:retweet), ("you" lang:en is:quote -is:retweet), ("and" lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
for g in ['news','money','science','culture','sports','online']:
    if g in SENSOR_READ:
        sweeps.append(sweep(f'sensors.{g}','discovery',None,
            f'search_posts_all {SENSOR_Q[g]} newest first, 25 results; reposts followed to origin; screened by global floor/pace',
            6,'ok',None, sensor_posts.get(f'sensors.{g}') or []))
    else:
        _last = '2026-10-24T2300Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science read this run; kept to about 20 reads to pace the daily budget); last read in {_last}',6,'skipped',f'not in this run rotation of three groups (kept to about 20 reads to pace the daily budget); last read in {_last}',[]))
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
        reason = 'four-hour desk due since 07:08Z on 2026-10-20 (last ok 2026-10-20T0308Z) but cut for the one hundred and tenth run (kept to about 20 reads to pace the daily budget in the 12:00-05:00 UTC band, up to 42; four-hour desks are cut first)' if d in ('defense','disaster','business','science','ideas','life') else 'two-hour desk due since 06:00Z (last ok 2026-10-20T0400Z) but cut for the one hundred and twelfth run (kept to about 20 reads to pace the daily budget in the 12:00-05:00 UTC band, up to 42)'
        sweeps.append(sweep(f'desk.{d}','desk',d, DESK_Q.get(d) or d, 24,'skipped', reason, []))
sweeps.append(sweep('context.top','context',None,'cut for the read budget (kept to about 20 reads to pace the daily budget in the 12:00-05:00 UTC band, up to 42)',None,'skipped','cut for the read budget',[]))
open_reqs = json.load(open(f'{REPO}/requests/open.json'))['requests']
REQ_Q = {
    'r-2026-10-23-01': 'search_posts_all Talarico ("voter ID" OR "voter IDs" OR "photo ID" OR "ID laws" OR clip OR video OR interview) -is:retweet -is:reply, start_time 2026-10-22T00:00:00Z, relevancy, 25 results; the clip post 2113317694367748316 itself is re-read in watch',
    'r-2026-10-23-02': 'search_posts_all Oleshky (ceasefire OR truce OR humanitarian) (Zelensky OR Ukrainian OR Ukraine OR "General Staff" OR "Southern Defense Forces" OR Pletenchuk OR Yermak OR Sybiha OR "27 October" OR "29 October" OR "October 27" OR "October 29") -is:retweet -is:reply, start_time 2026-10-23T12:00:00Z, relevancy, 25 results (1808Z re-read after the ask was rewritten; 1659Z used a narrower query from 2026-10-22T12:00Z); posts showing or naming residents not kept',
    'r-2026-10-20-01': 'two search_posts_all reads, start_time 2026-10-19T07:50:00Z, relevancy, 25 results each: ("SpaceX shares" OR "SpaceX share" OR "SpaceX stock") (kids OR kid OR children OR "Trump Accounts" OR "Trump Account" OR Treasury OR eligible OR eligibility) -is:retweet -is:reply; and (from:SpaceX OR from:USTreasury OR from:SecScottBessent OR from:TrumpAccounts OR from:elonmusk) (shares OR share OR kids OR children OR "Trump Accounts" OR account OR eligible) -is:retweet',
    'r-2026-10-18-02': 'two search_posts_all reads, start_time 2026-10-17T12:00:00Z, relevancy, 25 results each: Omar (search OR searched OR raid OR citizenship OR FBI OR DOJ OR "Justice Department" OR DHS OR denaturalization) -is:retweet -is:reply; and (from:nottspolice OR (Nottingham (officer OR police OR policeman) (shot OR shooting))) -is:retweet -is:reply',
    'r-2026-10-18-01': 'search_posts_all (Wainwright (explosion OR casualties OR killed OR injured OR cause)) OR (Wichita Stryker (crash OR truck OR police)) -is:retweet -is:reply, start_time 2026-10-17T12:00:00Z, relevancy, 25 results; plus posts on both events reached through the other sweeps this run',
    'r-2026-10-16-01': 'search_posts_all ("Norte Fire" OR #NorteFire) (acres OR containment OR contained OR homes OR structures OR destroyed OR cause) -is:retweet -is:reply, start_time 2026-10-16T00:00:00Z, relevancy, 25 results; plus OCFA and KTLA originals reached through the #NorteFire trend-name stream this run',
    'r-2026-10-10-01': 'search_posts_all ("intelligence sharing" OR "new president") Ukraine (refinery OR refineries OR Trump OR Zelensky) lang:en -is:retweet -is:reply, start_time 2026-10-09T00:00:00Z, relevancy, 25 results',
    'r-2026-10-09-12': 'search_posts_all "Marble Hill" (ICE OR DHS OR NYPD OR shooting OR shot) -is:retweet -is:reply, start_time 2026-10-08T00:00:00Z, relevancy, 25 results',
    'r-2026-10-09-13': 'search_posts_all (PERM OR "labor certification") (Microsoft OR Adobe OR Infosys OR Tata OR Wipro OR HCL OR Cognizant OR Capgemini OR "Labor Department" OR "Department of Labor") -is:retweet -is:reply, start_time 2026-10-08T00:00:00Z, relevancy, 25 results',
}
ANSWERED_EARLIER = {'r-2026-10-23-02':'2026-10-23T1808Z','r-2026-10-23-01':'2026-10-23T1659Z','r-2026-10-20-01':'2026-10-20T0308Z','r-2026-10-18-02':'2026-10-18T2203Z','r-2026-10-18-01':'2026-10-18T1807Z','r-2026-10-16-01':'2026-10-16T2303Z','r-2026-10-15-01':'2026-10-15T2059Z','r-2026-10-10-01':'2026-10-15T2200Z','r-2026-10-09-12':'2026-10-15T2200Z','r-2026-10-09-13':'2026-10-15T2200Z','r-2026-10-09-05':'2026-10-09T0629Z','r-2026-10-09-08':'2026-10-09T0629Z','r-2026-10-09-09':'2026-10-09T0629Z','r-2026-10-09-10':'2026-10-09T0629Z'}
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

_here = {p['id'] for p in posts_out}
ANSWERS = []
capture = {
    'schema': 'mts.capture/1',
    'run': {
        'id': RUN_ID,
        'started_at': STARTED,
        'finished_at': FINISHED,
        'status': 'partial',
        'reason': (
            f'Evening run (8:03 PM ET Oct 24 / 00:03 UTC Oct 25, the 00Z slot and the first run of the new UTC day; 12:00-05:00 UTC band, up to 42, kept to about 20 to keep usage minimal): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; the X day reset at 00:00 UTC, and 2300Z ended the old day at 510), parallel batches of up to 13, no 429 refusals. '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 00Z is a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour, still-gaining and rest-of-24-hour tiers; 602 ids, so the 400 cap left out the 40 last six-hour posts, the 133 slowest-growing still-gaining posts and 29 rest-of-24-hour posts, and no cited post; 4 reads); trends US (1 read; worldwide not read for the budget); '
            f'trend names "Tennessee", "Big 12" and "Dan Lanning" (3 reads; "<name> lang:en is:retweet", newest first, 25; three of the top-ten US names with no posts attached in 2300Z: "Tennessee" (second; South Carolina beat No. 11 Tennessee on a field goal with no time left; "South Carolina" (third), "Heupel" (ninth) and "David Smith" are the same game), "Big 12" (fifth; UCF beat No. 2 BYU in double overtime and Cincinnati beat Texas Tech; "2 BYU" (sixth) and "#BYUvsUCF" (eighth) are the same game as "Scott Frost" (first, attached in 2300Z)) and "Dan Lanning" (tenth; Oregon lost to Illinois); "Iowa" (fourth) and "Cheesecake Factory" (seventh) were attached in 2300Z); '
            f'quote/repost words is/you + and (3 reads, each word quoted); sensors news/money/science (3 reads; culture/sports/online last read 2300Z, so news/money/science were next in rotation); '
            f'4 desk reads: hourly politics, entertainment, sports, internet; the two-hour desks (last ok 2026-10-20T0400Z, due 06:00Z) cut for the one hundred and fourteenth run and the four-hour desks (last ok 2026-10-20T0308Z, due since 2026-10-20T07:08Z) cut for the one hundred and twelfth run, both for the budget; '
            f'two screening reads by id: 100 unread referenced, reply-parent and media-source posts, most pointed-at first, then 20 in the second read (the 1 left from the first list, 2108062331095908717, and the 19 second-hop posts the first read led to; ids left out earlier as likely paid or sexual were not read again; 2108062331095908717 was Not Found again in the second read, as in 1105Z through 2300Z; 8 third-hop ids left unread); story clusters (search_news) not read for the budget. '
            f'No new request: requests/open.json changed only its updated_at since 2300Z (watch.json dropped 2113498434431025427, read here in screening, and gained 2113990281322221932, read in watch); r-2026-10-23-02 was answered in 1659Z and 1808Z and r-2026-10-23-01 in 1659Z; earlier requests were answered in earlier captures; none was read again. '
            f'Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). '
            f'{EXTRA_NOTE} '
            f'Skipped sexual or graphic ids are in exclude_ids.json in the work folder.'
        ),
        'grabber': {
            'agent': 'grokbot',
            'model': None,
            'method': 'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid, search_news)'
        },
        'requests_rev': REQUESTS_REV,
    },
    'sweeps': sweeps,
    'trends': trends,
    'posts': posts_out,
    'observations': obs_ids_order,
    'context': [],
    'answers': ANSWERS,
}

out_path = os.environ.get('OUT') or f'{REPO}/capture/2026/10/25/0003Z.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
json.dump(capture, open(out_path,'w'), indent=2, ensure_ascii=False)
open(out_path,'a').write('\n')
print('wrote', out_path)
print('posts', len(posts_out), 'obs', len(obs_ids_order))
print("skipped_nsfw", len(set(skipped_nsfw)), sorted(set(skipped_nsfw)))
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
