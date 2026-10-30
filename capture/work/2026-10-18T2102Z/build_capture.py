#!/usr/bin/env python3
"""Build capture/2026/10/18/2102Z.json from saved X outputs."""
import json, re, os, time
from collections import Counter, defaultdict
from datetime import datetime, timezone

W = '/workspace/monitoring-the-situation/capture/work/2026-10-18T2102Z'
REPO = '/workspace/monitoring-the-situation'
RUN_ID = '2026-10-18T2102Z'
STARTED = '2026-10-18T21:02:00Z'
FINISHED = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
OBS_AT = '2026-10-18T21:03:00Z'
REQUESTS_REV = open(f'{W}/requests_rev.txt').read().strip()
READS_BEFORE = 413
READS_AFTER = int(open(f'{W}/reads_after.txt').read().strip())
READS_USED = READS_BEFORE - READS_AFTER
FORCE_REREC = set()
NO_REREC = {'2111143320311243129'}
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
    at_ts = at_ts or datetime(2026,10,18,21,4,tzinfo=timezone.utc).timestamp()
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
    'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt',
    'quote_is': 'quote_is.txt', 'quote_it': 'quote_it.txt', 'quote_that': 'quote_that.txt',
    'repost_what': 'repost_what.txt',
    'trend_jjmccarthy': 'trend_jjmccarthy.txt', 'trend_giants': 'trend_giants.txt', 'trend_kylergordon': 'trend_kylergordon.txt', 'trend_ajbrown': 'trend_ajbrown.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',
    'screen0': 'screen0.txt', 'screen1': 'screen1.txt', 'screen2': 'screen2.txt',
    'trends_us': 'trends_us.txt', 'trends_ww': 'trends_ww.txt',
}
DUE = [d['id'] for d in json.load(open(f'{REPO}/contract/desks.json'))['desks'] if d['id'] in ('politics','entertainment','sports','internet','ai','tech','medicine','defense','disaster','business')]
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
    ('quote_is','quote'),('quote_it','quote'),('quote_that','quote'),('repost_what','repost'),
    ('trend_jjmccarthy','trend.JJ McCarthy'),('trend_giants','trend.Giants'),('trend_kylergordon','trend.Kyler Gordon'),('trend_ajbrown','trend.AJ Brown'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),
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
        if str(_x) in ('trend.World Series','trend.David Hamilton','trend.Dodgers','trend.Brewers','trend.Bo Nix'): return 'sports'
        if str(_x) in ('trend.Seahawks','trend.Sam Darnold','trend.Shaheed'): return 'sports'
        if str(_x) in ('trend.Tesla Roadster','trend.Tesla'): return 'tech'
        if str(_x)=='trend.#OlandriaxWWW20': return 'life'
        if str(_x) in ('trend.RED Friday','trend.Good Friday'): return 'life'
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
SEX_WORDS = ('onlyfans','blowjob','would you fuck','want to fuck','be my pillow',' nsfw','porn','xxx ')

REQ_PICKS = {}
REQ_FILES = {}
REQ_ONLY = set()
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
EXTRA_PRIVATE = {'2111544142979604538','2111578605062861177','2111471845517963621','2049207819858039098','2111205736575549755','2111219056468480460','2111489219046641980','2111468596069126626','2111210261197533605','2111037738879218043','2110314961687707934','2110855499990384953','2111177307905995079','2111071770010673497','2069666093640417401','2040888913531662627','2111448883217694956','2008340922518344140','2111246923751452853','2111317409831481367','2111227821074845951','2109855328175317022','2111186315215560982','2111083403701338434','2110838225925189879','2111130582855962999','2110400241317085592','2055340102935593423','2111099194878603366','2109647068252004643','2111084566551363601','2003125806332280920','2110781018214895722','2110702236632248608','2029755078291415424','2110768423282069760','2110944984408989792','2111093562452639905','2111171825527103889','2110402979681771963','2110318389441044630','2111194862087479702','2111277181502398722','2111282491784864232','2111272038887547269','2111285508256977324','2111275019427074166','2110819912331702288','2110951046042579249','2111265332232933394','2111272639733916145','2111177447731560712','2111090671700287537','2110863058029474257','2111110833086283790','2089842388508287245','2081963206797615298','2092890946790646264','2110616551762141223','2110868572071407618','2109642635719950597','2111053432136278396','2110555022505198020','2110331635392471307','2041802128994275586','2110879358852411634','2110453086166929581','2110714998616150280','2110467314785349871','2110855697436979238','2111077078695387195','2110896741641838713','2110772234717397000','2110698695477829780','2110651029482074556','2086317046493520240','2110808191126892978','2110626732269289912','2110009515290599884','2110324218655076676','2110736011320025241','2110740447568056363'}
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
DESK_OVERRIDE_RUN.update({'2111917989562032173':'sports','2111433132331217153':None})  # 2102Z: PFF JJ McCarthy fourth-quarter passing stat is sports; Naaadeey candy-tasting clip is not a disaster post
EXTRA_PRIVATE |= {'2111198620187804119','2111546670559449421','2111302593183969363'}  # 1904Z: nypost photo of the dead college student (private person); BradBeringer video of a woman in her family's store in France (same video as 2111544142979604538, flagged earlier)
OLD_VIA_CHAIN |= {'2038807290422370479'}  # 1904Z: March 31 axios post reached through a March 31 quote and reply chain from a post read this run
DESK_OVERRIDE_1807 = {'2111856962044416268':'sports','2111734532483207284':'justice','2111525848310521868':'world','2111562104784519183':'world','2111683964721037767':'tech','2111842588126818619':'tech','2111278766152700208':'ai','2111503434008731795':'gaming','2111180818542698889':'sports','2111624429474136101':'music','2111751793386438949':'sports','2111578871921274962':'justice','2111861770444739018':'defense','2111652303854076191':'defense','2111689401051103636':'defense'}
import glob as _glob
PRIOR_DESK = {}
for _c in sorted(_glob.glob(f'{REPO}/capture/2026/10/*/*.json')):
    if _c.endswith('2102Z.json') and '/18/' in _c: continue
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
for a,b in [('Ryan Day','Ohio State'),('Jeremiah Smith','Ohio State'),('Sayin','Julian Sayin'),('Sayin','Ohio State'),('Jeremiah Smith','Julian Sayin'),('Arch Manning','Gators'),('Sark','Gators'),('Arch Manning','#HookEm'),('Sark','#HookEm'),('Sark','Arch Manning'),('Arch Manning','Sark'),('Ryan Day','Indiana'),('Arthur Smith','Ohio State'),('Betis','Lamine'),('Isak','Munoz'),('Munoz','Isak'),('Isak','Brentford'),('Munoz','Brentford'),('#MrFanboyEP8','MR FANBOY CHAPTER 8'),('Everton','Pedro Neto'),('Everton','#EVECHE'),('#CORTIS_NOLFest2026','IDEA BANK'),('#CORTIS_NOLFest2026','JAMES THE ULTIMATE PHENOMENON'),('#EVECHE', 'Everton'), ('#EVECHE', 'Pedro Neto'), ('#EVECHE', 'Caicedo'), ('#EVECHE', 'Hato'), ('#EVECHE', 'Paul Tierney'), ('Everton', '#EVECHE'), ('Everton', 'Pedro Neto'), ('Everton', 'Caicedo'), ('Everton', 'Hato'), ('Everton', 'Paul Tierney'), ('Pedro Neto', '#EVECHE'), ('Pedro Neto', 'Everton'), ('Pedro Neto', 'Caicedo'), ('Pedro Neto', 'Hato'), ('Pedro Neto', 'Paul Tierney'), ('Caicedo', '#EVECHE'), ('Caicedo', 'Everton'), ('Caicedo', 'Pedro Neto'), ('Caicedo', 'Hato'), ('Caicedo', 'Paul Tierney'), ('Hato', '#EVECHE'), ('Hato', 'Everton'), ('Hato', 'Pedro Neto'), ('Hato', 'Caicedo'), ('Hato', 'Paul Tierney'), ('Paul Tierney', '#EVECHE'), ('Paul Tierney', 'Everton'), ('Paul Tierney', 'Pedro Neto'), ('Paul Tierney', 'Caicedo'), ('Paul Tierney', 'Hato')] + [('JAMES THE ULTIMATE PHENOMENON', '#JAMESUnparalleled'), ('JAMES THE ULTIMATE PHENOMENON', 'IDEA BANK'), ('JAMES THE ULTIMATE PHENOMENON', 'CHAOWESOME'), ('JAMES THE ULTIMATE PHENOMENON', '#CORTIS_NOLFest2026'), ('JAMES THE ULTIMATE PHENOMENON', 'NOL Festival'), ('JAMES THE ULTIMATE PHENOMENON', 'KEONHO CAPTIVATES THE LENS'), ('JAMES THE ULTIMATE PHENOMENON', 'IKEONIC'), ('JAMES THE ULTIMATE PHENOMENON', 'ACEKEON MAKNAE'), ('JAMES THE ULTIMATE PHENOMENON', '5TH GEN IT BOY'), ('JAMES THE ULTIMATE PHENOMENON', 'HOGAN EFFECT'), ('#JAMESUnparalleled', 'JAMES THE ULTIMATE PHENOMENON'), ('#JAMESUnparalleled', 'IDEA BANK'), ('#JAMESUnparalleled', 'CHAOWESOME'), ('#JAMESUnparalleled', '#CORTIS_NOLFest2026'), ('#JAMESUnparalleled', 'NOL Festival'), ('#JAMESUnparalleled', 'KEONHO CAPTIVATES THE LENS'), ('#JAMESUnparalleled', 'IKEONIC'), ('#JAMESUnparalleled', 'ACEKEON MAKNAE'), ('#JAMESUnparalleled', '5TH GEN IT BOY'), ('#JAMESUnparalleled', 'HOGAN EFFECT'), ('IDEA BANK', 'JAMES THE ULTIMATE PHENOMENON'), ('IDEA BANK', '#JAMESUnparalleled'), ('IDEA BANK', 'CHAOWESOME'), ('IDEA BANK', '#CORTIS_NOLFest2026'), ('IDEA BANK', 'NOL Festival'), ('IDEA BANK', 'KEONHO CAPTIVATES THE LENS'), ('IDEA BANK', 'IKEONIC'), ('IDEA BANK', 'ACEKEON MAKNAE'), ('IDEA BANK', '5TH GEN IT BOY'), ('IDEA BANK', 'HOGAN EFFECT'), ('CHAOWESOME', 'JAMES THE ULTIMATE PHENOMENON'), ('CHAOWESOME', '#JAMESUnparalleled'), ('CHAOWESOME', 'IDEA BANK'), ('CHAOWESOME', '#CORTIS_NOLFest2026'), ('CHAOWESOME', 'NOL Festival'), ('CHAOWESOME', 'KEONHO CAPTIVATES THE LENS'), ('CHAOWESOME', 'IKEONIC'), ('CHAOWESOME', 'ACEKEON MAKNAE'), ('CHAOWESOME', '5TH GEN IT BOY'), ('CHAOWESOME', 'HOGAN EFFECT'), ('#CORTIS_NOLFest2026', 'JAMES THE ULTIMATE PHENOMENON'), ('#CORTIS_NOLFest2026', '#JAMESUnparalleled'), ('#CORTIS_NOLFest2026', 'IDEA BANK'), ('#CORTIS_NOLFest2026', 'CHAOWESOME'), ('#CORTIS_NOLFest2026', 'NOL Festival'), ('#CORTIS_NOLFest2026', 'KEONHO CAPTIVATES THE LENS'), ('#CORTIS_NOLFest2026', 'IKEONIC'), ('#CORTIS_NOLFest2026', 'ACEKEON MAKNAE'), ('#CORTIS_NOLFest2026', '5TH GEN IT BOY'), ('#CORTIS_NOLFest2026', 'HOGAN EFFECT'), ('NOL Festival', 'JAMES THE ULTIMATE PHENOMENON'), ('NOL Festival', '#JAMESUnparalleled'), ('NOL Festival', 'IDEA BANK'), ('NOL Festival', 'CHAOWESOME'), ('NOL Festival', '#CORTIS_NOLFest2026'), ('NOL Festival', 'KEONHO CAPTIVATES THE LENS'), ('NOL Festival', 'IKEONIC'), ('NOL Festival', 'ACEKEON MAKNAE'), ('NOL Festival', '5TH GEN IT BOY'), ('NOL Festival', 'HOGAN EFFECT'), ('KEONHO CAPTIVATES THE LENS', 'JAMES THE ULTIMATE PHENOMENON'), ('KEONHO CAPTIVATES THE LENS', '#JAMESUnparalleled'), ('KEONHO CAPTIVATES THE LENS', 'IDEA BANK'), ('KEONHO CAPTIVATES THE LENS', 'CHAOWESOME'), ('KEONHO CAPTIVATES THE LENS', '#CORTIS_NOLFest2026'), ('KEONHO CAPTIVATES THE LENS', 'NOL Festival'), ('KEONHO CAPTIVATES THE LENS', 'IKEONIC'), ('KEONHO CAPTIVATES THE LENS', 'ACEKEON MAKNAE'), ('KEONHO CAPTIVATES THE LENS', '5TH GEN IT BOY'), ('KEONHO CAPTIVATES THE LENS', 'HOGAN EFFECT'), ('IKEONIC', 'JAMES THE ULTIMATE PHENOMENON'), ('IKEONIC', '#JAMESUnparalleled'), ('IKEONIC', 'IDEA BANK'), ('IKEONIC', 'CHAOWESOME'), ('IKEONIC', '#CORTIS_NOLFest2026'), ('IKEONIC', 'NOL Festival'), ('IKEONIC', 'KEONHO CAPTIVATES THE LENS'), ('IKEONIC', 'ACEKEON MAKNAE'), ('IKEONIC', '5TH GEN IT BOY'), ('IKEONIC', 'HOGAN EFFECT'), ('ACEKEON MAKNAE', 'JAMES THE ULTIMATE PHENOMENON'), ('ACEKEON MAKNAE', '#JAMESUnparalleled'), ('ACEKEON MAKNAE', 'IDEA BANK'), ('ACEKEON MAKNAE', 'CHAOWESOME'), ('ACEKEON MAKNAE', '#CORTIS_NOLFest2026'), ('ACEKEON MAKNAE', 'NOL Festival'), ('ACEKEON MAKNAE', 'KEONHO CAPTIVATES THE LENS'), ('ACEKEON MAKNAE', 'IKEONIC'), ('ACEKEON MAKNAE', '5TH GEN IT BOY'), ('ACEKEON MAKNAE', 'HOGAN EFFECT'), ('5TH GEN IT BOY', 'JAMES THE ULTIMATE PHENOMENON'), ('5TH GEN IT BOY', '#JAMESUnparalleled'), ('5TH GEN IT BOY', 'IDEA BANK'), ('5TH GEN IT BOY', 'CHAOWESOME'), ('5TH GEN IT BOY', '#CORTIS_NOLFest2026'), ('5TH GEN IT BOY', 'NOL Festival'), ('5TH GEN IT BOY', 'KEONHO CAPTIVATES THE LENS'), ('5TH GEN IT BOY', 'IKEONIC'), ('5TH GEN IT BOY', 'ACEKEON MAKNAE'), ('5TH GEN IT BOY', 'HOGAN EFFECT'), ('HOGAN EFFECT', 'JAMES THE ULTIMATE PHENOMENON'), ('HOGAN EFFECT', '#JAMESUnparalleled'), ('HOGAN EFFECT', 'IDEA BANK'), ('HOGAN EFFECT', 'CHAOWESOME'), ('HOGAN EFFECT', '#CORTIS_NOLFest2026'), ('HOGAN EFFECT', 'NOL Festival'), ('HOGAN EFFECT', 'KEONHO CAPTIVATES THE LENS'), ('HOGAN EFFECT', 'IKEONIC'), ('HOGAN EFFECT', 'ACEKEON MAKNAE'), ('HOGAN EFFECT', '5TH GEN IT BOY')] + [('KEONHO CAPTIVATES THE LENS', 'NOL Festival'), ('KEONHO CAPTIVATES THE LENS', 'IKEONIC'), ('KEONHO CAPTIVATES THE LENS', 'ACEKEON MAKNAE'), ('KEONHO CAPTIVATES THE LENS', '5TH GEN IT BOY'), ('KEONHO CAPTIVATES THE LENS', 'HOGAN EFFECT'), ('NOL Festival', 'KEONHO CAPTIVATES THE LENS'), ('NOL Festival', 'IKEONIC'), ('NOL Festival', 'ACEKEON MAKNAE'), ('NOL Festival', '5TH GEN IT BOY'), ('NOL Festival', 'HOGAN EFFECT'), ('IKEONIC', 'KEONHO CAPTIVATES THE LENS'), ('IKEONIC', 'NOL Festival'), ('IKEONIC', 'ACEKEON MAKNAE'), ('IKEONIC', '5TH GEN IT BOY'), ('IKEONIC', 'HOGAN EFFECT'), ('ACEKEON MAKNAE', 'KEONHO CAPTIVATES THE LENS'), ('ACEKEON MAKNAE', 'NOL Festival'), ('ACEKEON MAKNAE', 'IKEONIC'), ('ACEKEON MAKNAE', '5TH GEN IT BOY'), ('ACEKEON MAKNAE', 'HOGAN EFFECT'), ('5TH GEN IT BOY', 'KEONHO CAPTIVATES THE LENS'), ('5TH GEN IT BOY', 'NOL Festival'), ('5TH GEN IT BOY', 'IKEONIC'), ('5TH GEN IT BOY', 'ACEKEON MAKNAE'), ('5TH GEN IT BOY', 'HOGAN EFFECT'), ('HOGAN EFFECT', 'KEONHO CAPTIVATES THE LENS'), ('HOGAN EFFECT', 'NOL Festival'), ('HOGAN EFFECT', 'IKEONIC'), ('HOGAN EFFECT', 'ACEKEON MAKNAE'), ('HOGAN EFFECT', '5TH GEN IT BOY'),('#LingOrmBetweenUsConcertD1','THE WORLD BETWEEN LINGORM D1'),('THE WORLD BETWEEN LINGORM D1','#LingOrmBetweenUsConcertD1'),('Kimmel','Johnny Carson'),('Johnny Carson','Kimmel'),('PERTHSANTA LOST IN LOVE','#PerthSantaFMinMacau'),('#PerthSantaFMinMacau','PERTHSANTA LOST IN LOVE'),('Mamu','Kessler'),('Kessler','Mamu'),('YK Osiris','Deshae'),('Deshae','YK Osiris'),('YK Osiris','ash trevino'),('YK Osiris','Adin Ross'),('ash trevino','Adin Ross'),('Adin Ross','ash trevino'),('Memphis','Marcus Stokes'),('Marcus Stokes','Memphis'),('Memphis','Tulane'),('Tulane','Memphis'),('Baron Corbin','#SmackDown'),('#SmackDown','Baron Corbin'),('#SmackDown','Nikki Bella'),('Nikki Bella','#SmackDown'),('San Clemente','Norte Fire'),('Norte Fire','San Clemente'),('#NorteFire','San Clemente'),('San Clemente','#NorteFire'),('Scaramucci','Press Secretary'),('Scaramucci','Katie Zacharia'),('#The24thBloomOfPor','POR 24TH BIRTHDAY'),('Good Friday','Remember Everyone Deployed'),('Good Friday','RED Friday'),('RED Friday','Remember Everyone Deployed'),('Julian Sayin','Hoover'),('Hoover','Julian Sayin'),('Julian Sayin','Ohio State'),('Ohio State','Julian Sayin'),('Hoover','Ohio State'),('Ohio State','Hoover'),('Julian Sayin','#GoBucks'),('Julian Sayin','#iufb'),('Hoover','#iufb'),('Hoover','#GoBucks'),('Indiana','Ohio State'),('Indiana','Sayin'),('Indiana','Jeremiah Smith'),('Indiana','Hoover'),('Indiana','Ryan Day'),('Indiana','#GoBucks'),('Indiana','#iufb'),('Texas','Arch Manning'),('Texas','Gators'),('Texas','#HookEm'),('Texas','Sark'),('Nick Marsh','Michigan State'),('Fahey','NHL'),('Macron','Paris'),('Macron','The French'),('Arch Manning','Arch'),('Nick Marsh','Marsh'),('Auburn','Gunner'),('Auburn','Georgia'),('Georgia','Gunner'),('Georgia','WAR DAMN EAGLE'),('Georgia','War Eagle'),('Bryce Underwood','Tommy Carr'),('Tommy Carr','Bryce Underwood'),('Bryce Underwood','Michigan'),('Tommy Carr','Michigan'),('Rhyne','#WNBAfinals'),('Rocco Becht','Tennessee'),('Macron','The French'),('The French','Macron'),('The French','Paris'),('Grubb','DeBoer'),('Auburn','War Eagle'),('War Eagle','Auburn'),('Auburn','War Damn Eagle'),('War Eagle','War Damn Eagle'),('Tennessee','Go Vols'),('Tennessee','DeBoer'),('Tennessee','Grubb'),('Florida State','Miami'),('Florida State','Mensah'),('Florida State','Malachi Toney'),('Miami','Malachi Toney'),('Mensah','Malachi Toney'),('Miami','Mensah'),('Mateer','Oklahoma'),('Buckley','Alabama'),('Notre Dame','CJ Carr'),('CJ Carr','Notre Dame'),('Notre Dame','Provo'),('Provo','Notre Dame'),('CJ Carr','Provo'),('Provo','CJ Carr'),('Kentucky','Mateer'),('Mateer','Kentucky'),('Stein','Kentucky'),('Kentucky','Stein'),('Clockwork Carnage','#AEWWrestleDream'),('#AEWWrestleDream','Clockwork Carnage'),('Clockwork Carnage','Ospreay'),('Utah','Big 12'),('Miami','Florida State'),('Brock Thomas','Dan Lanning'),('Dan Lanning','Brock Thomas'),('Brock Thomas','Raiola'),('Dan Lanning','Raiola'),('#LingOrmBetweenUsConcertD2','THE WORLD BETWEEN LINGORM D2'),('THE WORLD BETWEEN LINGORM D2','#LingOrmBetweenUsConcertD2'),('OH MY BEST DAY WITH FOURTH','#FourthConcertD3'),('#FourthConcertD3','OH MY BEST DAY WITH FOURTH'),('#YaoRunhaoRuinsPapergames','#BladeRunnerStandsWithAbuser'),('#BladeRunnerStandsWithAbuser','#YaoRunhaoRuinsPapergames'),('#YaoRunhaoRuinsPapergames','#全球请辞中国叠纸姚润昊'),('Nico Collins','#HTownMade')]:
    if trend_posts.get(a):
        trend_posts[b] = list(dict.fromkeys((trend_posts.get(b) or []) + trend_posts[a]))
        trend_posts[a] = list(dict.fromkeys((trend_posts.get(a) or []) + trend_posts[b]))

for _n in ('Julian Sayin','Ohio State','#GoBucks','#iufb'):
    trend_posts[_n] = [x for x in (trend_posts.get(_n) or []) if x != '2110789095257747679']  # 1706Z: a vacuum-cleaner joke from the Hoover stream, not the Ohio State v Indiana game

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
SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}
sweeps.append(sweep('watch','watch',None,
    f'get_posts_by_ids of requests/watch.json ({len(watch_json)} ids), every post first captured in the last 6 hours and under 24 hours old, posts first captured 6 to 24 hours ago that gained at least 2 percent between their last two readings, (21Z is not a fourth hour, so the rest of the last 24 hours was not added); {len(watch_ids)} ids, under the 400 cap, none left out; {len(watch_ids)} ids read, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 3 reads; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id,referenced_tweets.id.author_id',
    None,'ok',None, watch_ordered))
sweeps.append(sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max 20',None,'ok',None,[]))
sweeps.append(sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[]))
sweeps.append(sweep('viral.global','discovery',None,
    'sources: references followed two hops from every post read, including attachments.media_source_tweet_id; trend names "JJ McCarthy", Giants, "Kyler Gordon", "AJ Brown" (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2005Z; Steelers, Browns, Colts, Titans, Falcons and Saints already had posts from 2005Z and were not read again; only four names qualified; all are NFL Sunday names); quote/repost words is/it/that + what; sensors culture/sports/online; desks politics/entertainment/sports/internet/ai/tech/medicine/defense/disaster/business; three screening reads by id of unread referenced posts (two first-hop, one second-hop); search_news viral (story clusters; x_stories omitted); screened by id with global floor/pace',
    24,'ok',None, viral_core))
sweeps.append(sweep('rising.global','discovery',None,
    '3 quote pages + 1 repost page, common words "is", "it", "that" and "what": (is lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:quote -is:retweet), (what lang:en is:retweet), newest first, 25 each',
    6,'ok',None, rising_ids[:30]))
for g in ['news','money','science','culture','sports','online']:
    if g in SENSOR_READ:
        sweeps.append(sweep(f'sensors.{g}','discovery',None,
            f'search_posts_all {SENSOR_Q[g]} newest first, 25 results; reposts followed to origin; screened by global floor/pace',
            6,'ok',None, sensor_posts.get(f'sensors.{g}') or []))
    else:
        _last = '2026-10-18T2005Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped',f'rotation: culture/sports/online read this run (last read in 1904Z); news/money/science last read in {_last}, next run',[]))
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
        if d in ('music','gaming','offbeat','world','justice','markets'):
            reason = 'not due this run (two-hour desk, read in 2005Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, read in 1904Z)'
        else:
            reason = 'not due this run'
        sweeps.append(sweep(f'desk.{d}','desk',d, DESK_Q.get(d) or d, 24,'skipped', reason, []))
sweeps.append(sweep('context.top','context',None,'cut for the read budget',None,'skipped','cut for the read budget',[]))
open_reqs = json.load(open(f'{REPO}/requests/open.json'))['requests']
REQ_Q = {
    'r-2026-10-18-01': 'search_posts_all (Wainwright (explosion OR casualties OR killed OR injured OR cause)) OR (Wichita Stryker (crash OR truck OR police)) -is:retweet -is:reply, start_time 2026-10-17T12:00:00Z, relevancy, 25 results; plus posts on both events reached through the other sweeps this run',
    'r-2026-10-16-01': 'search_posts_all ("Norte Fire" OR #NorteFire) (acres OR containment OR contained OR homes OR structures OR destroyed OR cause) -is:retweet -is:reply, start_time 2026-10-16T00:00:00Z, relevancy, 25 results; plus OCFA and KTLA originals reached through the #NorteFire trend-name stream this run',
    'r-2026-10-10-01': 'search_posts_all ("intelligence sharing" OR "new president") Ukraine (refinery OR refineries OR Trump OR Zelensky) lang:en -is:retweet -is:reply, start_time 2026-10-09T00:00:00Z, relevancy, 25 results',
    'r-2026-10-09-12': 'search_posts_all "Marble Hill" (ICE OR DHS OR NYPD OR shooting OR shot) -is:retweet -is:reply, start_time 2026-10-08T00:00:00Z, relevancy, 25 results',
    'r-2026-10-09-13': 'search_posts_all (PERM OR "labor certification") (Microsoft OR Adobe OR Infosys OR Tata OR Wipro OR HCL OR Cognizant OR Capgemini OR "Labor Department" OR "Department of Labor") -is:retweet -is:reply, start_time 2026-10-08T00:00:00Z, relevancy, 25 results',
}
ANSWERED_EARLIER = {'r-2026-10-18-01':'2026-10-18T1807Z','r-2026-10-16-01':'2026-10-16T2303Z','r-2026-10-15-01':'2026-10-15T2059Z','r-2026-10-10-01':'2026-10-15T2200Z','r-2026-10-09-12':'2026-10-15T2200Z','r-2026-10-09-13':'2026-10-15T2200Z','r-2026-10-09-05':'2026-10-09T0629Z','r-2026-10-09-08':'2026-10-09T0629Z','r-2026-10-09-09':'2026-10-09T0629Z','r-2026-10-09-10':'2026-10-09T0629Z'}
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
            f'Daytime run at 5:02 PM ET (21:02 UTC Oct 18; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2005Z run ended at 413, so no reads were used elsewhere between the runs). '
            f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 21Z is not a fourth hour; under the 400 cap, none left out; 3 reads); trends US+WW (2 reads); '
            f'trend names "JJ McCarthy", Giants, "Kyler Gordon", "AJ Brown" (4 reads; each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; of the current top-ten US names these had no posts attached in 2005Z; Steelers, Browns, Colts, Titans, Falcons and Saints already had posts and were not read again; all are NFL Sunday names); quote/repost words is/it/that + what (3+1); '
            f'sensors culture/sports/online (3 reads); 10 desks due (hourly politics, entertainment, sports, internet; two-hour ai, tech, medicine last read 1807Z; four-hour defense, disaster, business last read 1709Z, coming due at 21:09Z); music/gaming/offbeat/world/justice/markets (2005Z) and four-hour science/ideas/life (1904Z) not due; '
            f'three screening reads by id: {len(open(f"{W}/screen_ids.txt").read().split())} unread first-hop and {len(open(f"{W}/screen_ids_hop2.txt").read().split())} second-hop referenced, reply-parent and media-source posts; search_news viral (1 read; x_stories omitted, result file saved). '
            f'No new request: every open request was answered in an earlier capture (r-2026-10-18-01 in 1807Z) and was not read again. '
            f'Not read for the budget: volume, context.top, media descriptions; news/money/science sensors next rotation. '
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

out_path = f'{REPO}/capture/2026/10/18/2102Z.json'
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
