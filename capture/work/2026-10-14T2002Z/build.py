import json, os, re
from datetime import datetime, timezone
from collections import Counter

WORK='/workspace/monitoring-the-situation/capture/work/2026-10-14T2002Z'
REPO='/workspace/monitoring-the-situation'
NOW=datetime(2026,10,14,20,5,tzinfo=timezone.utc)
RUN_ID='2026-10-14T2002Z'
AT='2026-10-14T20:05:00Z'
STARTED='2026-10-14T20:02:00Z'
FINISHED=__import__('datetime').datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00Z')
REQ_REV=open(f'{WORK}/requests_rev.txt').read().strip()
READS_START=780
READS_END=757

def load_x(path):
  raw=open(path).read()
  if 'X reads left' in raw:
    raw=raw[:raw.rfind('X reads left')]
  raw=re.sub(r'</?cursor_untrusted_data[^>]*>','',raw)
  start=raw.find('{'); end=raw.rfind('}')+1
  return json.loads(raw[start:end])

def verified_of(u):
  vt=(u.get('verified_type') or '').lower()
  if vt in ('blue','business','government','organization'):
    return 'blue' if vt=='blue' else vt
  if u.get('verified') is True:
    return 'blue'
  return 'none'

def metrics(t):
  pm=t.get('public_metrics') or {}
  return {
    'views': pm.get('impression_count'),
    'likes': pm.get('like_count'),
    'reposts': pm.get('retweet_count', pm.get('repost_count')),
    'quotes': pm.get('quote_count'),
    'replies': pm.get('reply_count'),
    'bookmarks': pm.get('bookmark_count'),
  }

def media_list(t, media_by_key):
  out=[]
  keys=(t.get('attachments') or {}).get('media_keys') or []
  ents=t.get('entities') or {}
  for mk in keys:
    m=media_by_key.get(mk)
    if not m: continue
    typ=m.get('type')
    if typ=='animated_gif': typ='gif'
    elif typ=='image': typ='photo'
    else: typ=typ or 'photo'
    dur=m.get('duration_ms')
    out.append({
      'type': typ,
      'description': None,
      'alt': m.get('alt_text'),
      'duration_s': (dur/1000.0) if dur else None,
      'link_url': None,
      'link_title': None,
    })
  if not out:
    urls=ents.get('urls') or []
    for u in reversed(urls):
      eu=u.get('expanded_url') or u.get('unwound_url') or ''
      if 'x.com' in eu or 'twitter.com' in eu: continue
      out.append({
        'type':'link','description': None,'alt': None,'duration_s': None,
        'link_url': u.get('unwound_url') or eu,
        'link_title': u.get('title'),
      })
      break
  return out

def reply_quote(t):
  reply=None; quotes=None
  for r in t.get('referenced_tweets') or []:
    if r.get('type')=='replied_to': reply=r['id']
    if r.get('type')=='quoted': quotes=r['id']
  return reply, quotes

def text_of(t):
  note=t.get('note_tweet')
  if isinstance(note, dict) and note.get('text'):
    return note['text']
  return t.get('text') or ''

EXCLUDE_IDS=set(json.load(open(f'{WORK}/exclude_ids.json'))) | set([
  '2092675679880089981',  # Starlink promo ad
  '2110223317416423775',  # prior Starlink promo

  '2108124415762592123','2107389692018622901','2108366539439411593',
  '2107759105586921862','2107898516836073615','2107914086675788263',
  '2107913429990166804','2108289854974951548','2108325927872803119',
  '2108511541351837778','2108378335512293747','2108437202543800337',
  '2105144159715643542','2107407108446790049',
  '2108531741883560072','2107219727701746162','2108211566034440579',
  '2108148098182836497','2107950433654235262','1883242684762255643',
  '2108573302612504596','2100889316075651135','2108591066077118717',
  '2108368510816596206','2108538963732414892','2105701698513567928',
  '2108264549707329662','2108327411746255354','2108599428894642631',
  '2108620753218252866','2109011084795584706','2108812467568865699',
  '2107834547752816718',
])
EXCLUDE_SUBSTR=['hentai','porn','pussy','masturbat','getting laid','raped a','9-year-old','9 year old','onlyfans','#mom #mommy #stepmom','ass-to-mouth','fleshlight','sex slave','stolas ass','cockyboys','creamy pussy','tiny tits','sissy','help me cum','prostate massager','oral sex','Ladyboy','Shemale','#nsfw','#hentai','penetrators','face fuck','AI girlfriend','sexy, witty','fursuit','#FursuitFriday','fearedbuck private','finished inside','fuck her','manhandled','onlyfans']

def bad_text(s):
  sl=(s or '').lower()
  return any(x in sl for x in EXCLUDE_SUBSTR)

all_tweets={}; all_users={}; all_media={}
watch_docs=[]
for name in ['watch1.json','watch2.json','watch3.json']:
  p=f'{WORK}/{name}'
  if os.path.exists(p):
    try: watch_docs.append(load_x(p))
    except Exception as e: print('skip watch', name, e)

screen_docs=[]
for name in ['quote1.json','quote2.json','quote3.json','repost.json',
             'sensors_culture.json','sensors_sports.json','sensors_online.json',
             'desk_politics.json','desk_entertainment.json','desk_sports.json','desk_internet.json',
             'trend_mcipsg.json','trend_roma.json','trend_dudus.json','trend_widedeceiver.json','trend_realmadrid.json',
             'screen0.json','screen1.json','screen2.json']:
  p=f'{WORK}/{name}'
  if os.path.exists(p):
    try: screen_docs.append(load_x(p))
    except Exception as e: print('skip', name, e)

for doc in watch_docs+screen_docs:
  for u in (doc.get('includes') or {}).get('users') or []:
    all_users[u['id']]=u
  for m in (doc.get('includes') or {}).get('media') or []:
    all_media[m['media_key']]=m
  for t in (doc.get('includes') or {}).get('tweets') or []:
    all_tweets[t['id']]=t
  for t in (doc.get('includes') or {}).get('posts') or []:
    all_tweets[t['id']]=t
  for t in doc.get('data') or []:
    all_tweets[t['id']]=t

watch_ids=json.load(open(f'{REPO}/requests/watch.json'))['post_ids']
observations=[]; seen_obs=set()

def add_obs(tid, t, at=AT):
  if tid in seen_obs: return
  tw=t or all_tweets.get(tid)
  if not tw: return
  m=metrics(tw)
  if m['views'] is None and m['likes'] is None:
    observations.append({'id':tid,'at':at,'state':'unavailable','views':None,'likes':None,'reposts':None,'quotes':None,'replies':None,'bookmarks':None,'approx':False})
  else:
    observations.append({'id':tid,'at':at,'state':'live','views':m['views'],'likes':m['likes'],'reposts':m['reposts'],'quotes':m['quotes'],'replies':m['replies'],'bookmarks':m['bookmarks'],'approx':False})
  seen_obs.add(tid)

watch_returned=set()
for doc in watch_docs:
  for t in doc.get('data') or []:
    watch_returned.add(t['id'])
    add_obs(t['id'], t)
for wid in list(dict.fromkeys(watch_ids+open(f'{WORK}/reread_ids.txt').read().split())):
  if wid not in watch_returned and wid not in seen_obs:
    observations.append({'id':wid,'at':AT,'state':'unavailable','views':None,'likes':None,'reposts':None,'quotes':None,'replies':None,'bookmarks':None,'approx':False})
    seen_obs.add(wid)

def age_hours(created):
  if not created: return None
  ct=datetime.fromisoformat(created.replace('Z','+00:00').replace('.000',''))
  return (NOW-ct).total_seconds()/3600.0

def clears_global(m, age_h, kind):
  views=m['views'] or 0; likes=m['likes'] or 0
  if kind=='news':
    return views>=100000 or likes>=2000
  if age_h is not None and age_h < 0.25:
    return False
  if age_h is not None and 0.25 <= age_h < 3:
    return (views/age_h)>=25000 and views>=10000
  return views>=100000 or likes>=2000

def clears_desk(m, age_h, kind, floor_views=50000, floor_likes=1000):
  views=m['views'] or 0; likes=m['likes'] or 0
  if kind=='news':
    return views>=floor_views or likes>=floor_likes
  if age_h is not None and age_h < 0.25:
    return False
  if age_h is not None and 0.25 <= age_h < 3:
    return (views/age_h)>=(floor_views/4) and views>=(floor_views/10)
  return views>=floor_views or likes>=floor_likes

def assign_desk(text):
  tl=(text or '').lower()
  # crypto retired: map market/company tokens, else null via markets/business
  cryptoish=any(w in tl for w in ['bitcoin','btc','ethereum','crypto','memecoin','solana','$btc','token launch'])
  if any(w in tl for w in ['cpi','inflation','rate cut','treasury yield']): return 'markets'
  if any(w in tl for w in ['hurricane','isaias','storm surge','landfall','earthquake']): return 'disaster'
  if any(w in tl for w in ['pope','vatican']): return 'world'
  if any(w in tl for w in ['mcipsg','#ucl','psg','mbappe','mbappé','mourinho','donnarumma','dembele','vinicius','ballon d','barça','barca','manchester united','champions league','lamine yamal','real madrid','lisandro','hansi flick','manchester','ronaldo']): return 'sports'
  if any(w in tl for w in ['ps5','playstation','resident evil','windows 7 on']): return 'gaming'
  if any(w in tl for w in ['panama','panamá','putin','zelensky','nobel','pillay','icc','starlink','ambani','israel','gaza','ukraine','nato','penta','wwe','wrestling']): return 'world' if 'penta' not in tl and 'wwe' not in tl and 'wrestling' not in tl else ('sports' if any(x in tl for x in ['penta','wwe','wrestling','mitb','money in the bank']) else 'world')
  if any(w in tl for w in ['penta','#mitb','money in the bank','la knight','wwe']): return 'sports'
  if any(w in tl for w in ['trump','democrat','republican','congress','senate','election','governor','white house','supreme court','charlie kirk','execution','endwokeness','hegseth','jd vance','rubio','katie zacharia','press secretary']): return 'politics'
  if any(w in tl for w in ['ditka','bears','nfl','nba','mlb','f1','soccer','touchdown','kelce','cowboys','bucs','wnba','ufc','schefter','super bowl','premier league','mcbride','caitlin clark','bama','alabama','georgia','oklahoma','oregon','sark','gunner stockton','gavin williams','arch manning']): return 'sports'
  if any(w in tl for w in ['anime','movie','trailer','actor','actress','netflix','episode','season','celebrity','film','avatar','marvel','sinners','emmy']): return 'entertainment'
  if cryptoish:
    if any(w in tl for w in ['sec','etf','nasdaq','stocks','fed ','market']): return 'markets'
    if any(w in tl for w in ['coinbase','binance','company','ceo']): return 'business'
    return None
  if any(w in tl for w in ['stocks','nasdaq','fed ','s&p','dow ']): return 'markets'
  if any(w in tl for w in ['openai','anthropic','chatgpt','gemini','grok','llm',' ai ' ,'math papers','stargate']): return 'ai'
  if any(w in tl for w in ['vaccine','hhs','kennedy','nih','mold','fungal']): return 'medicine'
  if any(w in tl for w in ['meme','tiktok','streamer','twitch','youtube','fandom','kick ']): return 'internet'
  return 'internet'

NEWS_HANDLES=set(h.lower() for h in ['Reuters','BBCBreaking','SkyNews','nytimes','cnnbrk','cnni','NobelPrize','PTI_News','WFLA','MeidasTouch','LeadingReport','visegrad24','CNN','BBCWorld','FoxNews','weatherchannel','BNONews','MyRadarWX','Forbes','AP','NFL','MLB','SportsCenter','BleacherReport','rawsalerts'])

def kind_of_user(u):
  un=(u.get('username') or '')
  if un.lower() in NEWS_HANDLES:
    return 'news'
  unl=un.lower()
  if any(x in unl for x in ['nytimes','reuters','bbc','pti_news','nobelprize','cnn','foxnews','weather','forbes']):
    return 'news'
  vt=(u.get('verified_type') or '').lower()
  if vt=='government':
    return 'official'
  if vt=='business':
    return 'org'
  return 'unknown'

DESK_OVERRIDE={**json.load(open(f'{WORK}/desk_override.json')),'2110368165985493137':'justice','2110349602918445087':'justice','2110322650442768768':'justice','2110385901297709079':'justice','2110223317416423775':'tech','2110355411144675696':'sports','2110340342071672911':'sports','2110393055039623260':'gaming','2110354053108543736':'music','2110355310120755259':'music','2110354955089633770':'music','2110080227854688323':'music','2110390540294636019':'entertainment','2110296578514928116':'entertainment','2110230614158848350':'entertainment','2110350212317270407':'entertainment','2110062933816611208':'world','2110067869287661838':'business','2110165104713183485':'tech','2110016190617911553':'science','2110091703419871393':'ai','2110092821571027310':'gaming','2110207594484642084':'gaming','2110057477236789447':'sports','2110313050423095339':'world'}
FLAG_ADD={'2110117870743195940':['private_individual'],'2110323971266908578':['private_individual'],'2110333415895826662':['private_individual'],'2110118705317233129':['private_individual'],'2106169354878321043':['private_individual'],'2110109803305656826':['private_individual'],'2110076763799986523':['private_individual'],'2110077784148316301':['private_individual'],'2110228564717015082':['private_individual'],'2110295825859420526':['private_individual'],'2110050933283668252':['private_individual'],'2110041731949576244':['private_individual'],'2110066955634012367':['private_individual'],'2008193557673488846':['private_individual'],'2110135850361291059':['private_individual'],'2110057477236789447':['private_individual']}
REREAD_SET=set(open(f'{WORK}/reread_ids.txt').read().split())
posts=[]; viral_ids=[]; rising_ids=[]
desk_map={k:[] for k in ['politics','entertainment','sports','internet','world','markets','ai','disaster','medicine','tech','science','business','music','gaming','ideas','life','offbeat','defense','justice']}
TREND_NAMES=['#MCIPSG','Roma','Dudus','Wide Deceiver','Real Madrid']
trend_top={}
TREND_FILE={
  '#MCIPSG':'trend_mcipsg_top3.txt',
  'Roma':'trend_roma_top3.txt',
  'Dudus':'trend_dudus_top3.txt',
  'Wide Deceiver':'trend_widedeceiver_top3.txt',
  'Real Madrid':'trend_realmadrid_top3.txt',
}
for _n in TREND_NAMES:
  _fp=f"{WORK}/{TREND_FILE[_n]}"
  _ids=[x for x in open(_fp).read().splitlines() if x] if __import__('os').path.exists(_fp) else []
  trend_top[_n]=_ids
press_keep=[]
trend_of={}
for _n in TREND_NAMES:
  for _i in trend_top[_n]:
    press_keep.append(_i); trend_of[_i]=_n
trend_keep=set(press_keep)
def TREND_LEAD(n):
  if n=='#MCIPSG': return 'trend context for #MCIPSG (one event with Donnarumma, Doue, Dembele: Manchester City v PSG, Champions League); no floor'
  if n=='Roma': return 'trend context for Roma (one event with Real Madrid, Valverde, Tchouameni: Roma v Real Madrid, Champions League); no floor'
  if n=='Dudus': return 'trend context for Dudus (one event with Diddy: reported prison fight); no floor'
  if n=='Wide Deceiver': return 'trend context for Wide Deceiver (Netflix Untold documentary title); no floor'
  if n=='Real Madrid': return 'trend context for Real Madrid (one event with Roma, Valverde, Tchouameni: Roma v Real Madrid, Champions League); no floor'
  return 'trend context for %s; no floor' % n

tally_lead={}
try:
  tally=json.load(open(f'{REPO}/capture/TALLY.json'))
  c=Counter()
  for run in tally.get('runs') or []:
    for o in run.get('origins') or []:
      c[o]+=1
  tally_lead=dict(c)
except Exception:
  pass

quote_origins=open(f'{WORK}/quote_origins_all.txt').read().splitlines()
repost_origins=open(f'{WORK}/repost_origins_all.txt').read().splitlines()
this_stream=set(quote_origins+repost_origins)

pointed=Counter()
try:
  rc=json.load(open(f'{WORK}/ref_counts.json'))
  if isinstance(rc, list):
    pointed.update(dict(rc))
  elif isinstance(rc, dict) and 'ref_counts' in rc:
    pointed.update(rc['ref_counts'])
  else:
    pointed.update(rc)
except Exception:
  pass

screen_tweets=[]
for doc in screen_docs:
  for t in doc.get('data') or []:
    refs=t.get('referenced_tweets') or []
    if any(r.get('type')=='retweeted' for r in refs) and (t.get('text') or '').startswith('RT @'):
      continue
    screen_tweets.append(t)
  for t in (doc.get('includes') or {}).get('tweets') or []:
    screen_tweets.append(t)
  for t in (doc.get('includes') or {}).get('posts') or []:
    screen_tweets.append(t)

seen_screen=set(); screen_unique=[]
for t in screen_tweets:
  if t['id'] in seen_screen: continue
  seen_screen.add(t['id']); screen_unique.append(t)

skipped_sensitive=[]
for t in screen_unique:
  tid=t['id']
  if tid in EXCLUDE_IDS: continue
  if tid in watch_ids or tid in REREAD_SET: continue
  txt=text_of(t)
  if bad_text(txt):
    skipped_sensitive.append(tid); continue
  if t.get('possibly_sensitive'):
    skipped_sensitive.append(tid); continue
  u=all_users.get(t.get('author_id'),{})
  m=metrics(t)
  age=age_hours(t.get('created_at'))
  akind=kind_of_user(u)
  flags=[]
  if age is not None and age > 24*7:
    flags.append('old_content')
  if age is not None and age > 24 and 'old_content' not in flags and tid not in trend_keep:
    continue
  desk=DESK_OVERRIDE.get(tid,assign_desk(txt))
  flags+=FLAG_ADD.get(tid,[])
  ok=clears_desk(m, age, akind) or clears_global(m, age, akind)
  lead=None
  if tid in press_keep:
    ok=True
    lead=TREND_LEAD(trend_of[tid])
  if tid in this_stream:
    n=tally_lead.get(tid,0)+1
    extra='seen in the quote or repost stream in %d of the last 6 runs' % min(n,6)
    lead=(lead+'; '+extra) if lead else extra
  if pointed.get(tid,0) >= 2:
    extra='pointed at by %d posts read this run' % pointed[tid]
    lead=(lead+'; '+extra) if lead else extra
  # credits
  for pat in [r'via @(\w+)', r'📽️ @(\w+)', r'🎥 @(\w+)']:
    mm=re.search(pat, txt)
    if mm:
      extra='credits @%s' % mm.group(1)
      lead=(lead+'; '+extra) if lead else extra
      break
  if not ok: continue
  handle=u.get('username')
  if not handle:
    continue
  if age is not None and 0.25<=age<3 and (m['views'] or 0) < 100000:
    pace=int((m['views'] or 0)/age) if age else 0
    extra='pace about %d views/hour at read' % pace
    lead=(lead+'; '+extra) if lead else extra
  created=(t.get('created_at') or '').replace('.000Z','Z')
  if created.endswith('+00:00'): created=created.replace('+00:00','Z')
  reply, quotes = reply_quote(t)
  post={
    'id': tid,
    'url': 'https://x.com/%s/status/%s' % (handle, tid),
    'created_at': created,
    'lang': t.get('lang') or 'en',
    'text': txt,
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
  posts.append(post)
  if clears_global(m, age, akind) or tid in trend_keep:
    viral_ids.append(tid)
  if age is not None and age < 6:
    rising_ids.append(tid)
  if desk and desk in desk_map:
    desk_map[desk].append(tid)

seenp=set(); posts2=[]
for p in posts:
  if p['id'] in seenp: continue
  seenp.add(p['id']); posts2.append(p)

def views_of(pid):
  tw=all_tweets.get(pid) or {}
  return (tw.get('public_metrics') or {}).get('impression_count') or 0

posts2.sort(key=lambda p: -views_of(p['id']))

# author cap: at most 3 new posts per account
author_counts=Counter(); capped=[]; dropped_by_author=Counter()
for p in posts2:
  h=p['author']['handle'].lower()
  if author_counts[h] >= 3:
    dropped_by_author[h]+=1
    continue
  author_counts[h]+=1
  capped.append(p)
_trend_ok=[x for x in press_keep if x in all_tweets and not bad_text(text_of(all_tweets[x])) and not all_tweets[x].get('possibly_sensitive')]
posts=[p for p in capped if p['id'] not in trend_keep][:40]
kept=set(p['id'] for p in posts)
for p in posts:
  add_obs(p['id'], all_tweets.get(p['id']))
viral_ids=[i for i in viral_ids if i in kept][:40]
rising_ids=[i for i in rising_ids if i in kept][:30]
for k in desk_map:
  desk_map[k]=[i for i in desk_map[k] if i in kept][:10]

# Ensure press trend posts are in posts even if below floor
for mid in press_keep:
  if not mid or mid in kept or mid in EXCLUDE_IDS or mid in REREAD_SET: continue
  t=all_tweets.get(mid)
  if not t: continue
  u=all_users.get(t.get('author_id'),{})
  handle=u.get('username')
  if not handle: continue
  txt=text_of(t)
  if bad_text(txt) or t.get('possibly_sensitive'): continue
  created=(t.get('created_at') or '').replace('.000Z','Z')
  reply, quotes = reply_quote(t)
  posts.append({
    'id': mid,
    'url': 'https://x.com/%s/status/%s' % (handle, mid),
    'created_at': created,
    'lang': t.get('lang') or 'en',
    'text': txt,
    'author': {
      'handle': handle,
      'name': u.get('name') or handle,
      'followers': (u.get('public_metrics') or {}).get('followers_count'),
      'verified': verified_of(u),
      'kind': kind_of_user(u),
    },
    'media': media_list(t, all_media),
    'reply_to': reply,
    'quotes': quotes,
    'note': None,
    'flags': FLAG_ADD.get(mid,[]),
    'desk': DESK_OVERRIDE.get(mid,assign_desk(txt)),
    'beat': None,
    'topic': None,
    'lead': TREND_LEAD(trend_of[mid]),
  })
  add_obs(mid, t)
  kept.add(mid)
  if mid not in viral_ids: viral_ids.append(mid)
  d=DESK_OVERRIDE.get(mid,assign_desk(txt))
  if d: desk_map.setdefault(d, []).append(mid)
MEDIA_DESC=json.load(open(f'{WORK}/media_desc.json'))
for p in posts:
  if p['id'] in MEDIA_DESC and p['media']:
    p['media'][0]['description']=MEDIA_DESC[p['id']]
posts=posts[:60]
# corrected records: watched posts whose stored text was the first 280 characters of a long post
import glob as _g
_rec={}
for _c in sorted(_g.glob(f'{REPO}/capture/2026/10/*/*.json')):
  if _c.endswith('/14/2002Z.json'): continue
  for _p in json.load(open(_c))['posts']: _rec[_p['id']]=(_p,_c.split('/capture/')[1])
RECORRECTED=[]
for _d in watch_docs:
  for _t in _d.get('data') or []:
    _i=_t['id']
    if _i in kept or _i not in _rec: continue
    _txt=text_of(_t)
    _old,_src=_rec[_i]
    if _old['text']==_txt: continue
    _p=json.loads(json.dumps(_old))
    _p['text']=_txt
    _u=all_users.get(_t.get('author_id'),{})
    if _u.get('username'):
      _p['author']['followers']=(_u.get('public_metrics') or {}).get('followers_count')
    _note='re-recorded: X returned the full long-post text (note_tweet) this run; the record in capture/%s held %d characters, now %d' % (_src,len(_old['text']),len(_txt))
    _p['lead']=(_p.get('lead')+'; '+_note) if _p.get('lead') else _note
    posts.append(_p); RECORRECTED.append(_i)
print('recorrected', RECORRECTED)
kept=set(p['id'] for p in posts)
press_ids=[i for i in press_keep if i and i in kept]
viral_ids=[i for i in viral_ids if i in kept][:40]
rising_ids=[i for i in rising_ids if i in kept][:30]
for k in desk_map:
  desk_map[k]=[i for i in desk_map[k] if i in kept][:10]

GROUPS=['culture','sports','online']
sensor_kept={g:[] for g in GROUPS}
for g in GROUPS:
  p=f'{WORK}/sensor_{g}_top.txt'
  if os.path.exists(p):
    for pid in open(p).read().splitlines():
      if not pid: continue
      if pid in kept or pid in watch_returned:
        if pid not in sensor_kept[g]:
          sensor_kept[g].append(pid)
for g in sensor_kept:
  sensor_kept[g]=sensor_kept[g][:15]

us=json.load(open(f'{WORK}/trends_us_clean.json'))['data']
ww=json.load(open(f'{WORK}/trends_ww_clean.json'))['data']
trends=[]
for i,t in enumerate(us[:20],1):
  name=t['trend_name']
  pids=[]
  if name in TREND_NAMES:
    pids=[x for x in trend_top[name] if x in kept or x in watch_returned][:3]
  trends.append({'region':'US','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})
for i,t in enumerate(ww[:20],1):
  name=t['trend_name']
  pids=[]
  if name in TREND_NAMES:
    pids=[x for x in trend_top[name] if x in kept or x in watch_returned][:3]
  trends.append({'region':'WW','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})

reread=open(f'{WORK}/reread_ids.txt').read().splitlines()
watch_post_ids=[]; seenw=set()
for i in watch_ids+reread:
  if i not in seenw and i in seen_obs:
    watch_post_ids.append(i); seenw.add(i)
watch_post_ids=watch_post_ids[:400]

sweeps=[]
def sweep(sid, kind, desk, method, window, status, reason, pids):
  sweeps.append({'id':sid,'kind':kind,'desk':desk,'method':method,'window_hours':window,'status':status,'reason':reason,'post_ids':pids})

n_watch_planned=len(set(reread))
n_watch_ret=len([i for i in set(reread) if i in watch_returned])
sweep('watch','watch',None,'get_posts_by_ids of requests/watch.json (57 ids), every post first captured in the last 6 hours and under 24 hours old (captures 2026-10-14T1406Z through 1902Z), posts first captured 6 to 24 hours ago that gained at least 2 percent between their last two readings, and (fourth hour) the rest of the last 24 hours slowest growing last: %d unique ids, %d returned, 3 reads; 2110417903740973149 Not Found; fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id'%(n_watch_planned,n_watch_ret),None,'ok',None,watch_post_ids)
sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max_trends 20',None,'ok',None,[])
sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max_trends 20',None,'ok',None,[])
sweep('viral.global','discovery',None,'sources: references followed two hops from every post read, including attachments.media_source_tweet_id (origins carried in includes.tweets with expansion referenced_tweets.id and referenced_tweets.id.author_id; second-hop, reply-parent and media-source ids screened in two get_posts_by_ids reads of 117 ids); sensors culture/sports/online; trend names "\\"#MCIPSG\\" lang:en is:retweet", "\\"Roma\\" lang:en is:retweet", "\\"Dudus\\" lang:en is:retweet", "\\"Wide Deceiver\\" lang:en is:retweet", "\\"Real Madrid\\" lang:en is:retweet"; quote streams "this lang:en is:quote -is:retweet", "is lang:en is:quote -is:retweet", "you lang:en is:quote -is:retweet" and repost stream "\\"and\\" lang:en is:retweet" (newest first, 25 each); desk repost streams. Global floor 100,000 views or 2,000 likes under 24 hours, pace rule for 15 min to 3 h',24,'ok',None,viral_ids)
sweep('rising.global','discovery',None,'3 quote pages + 1 repost page, common words "this", "is", "you" and "and": "this lang:en is:quote -is:retweet", "is lang:en is:quote -is:retweet", "you lang:en is:quote -is:retweet", "\\"and\\" lang:en is:retweet", newest first, 25 each; originals screened',6,'ok',None,rising_ids)
SQ={g:open(f'{WORK}/sensor_query_{g}.txt').read().strip() for g in GROUPS}
for g in GROUPS:
  sweep('sensors.%s'%g,'discovery',None,'search_posts_all %s newest first, 25 results; reposts and quotes followed to the origin'%SQ[g],6,'ok',None,sensor_kept.get(g,[]))
for g in ['news','money','science']:
  sweep('sensors.%s'%g,'discovery',None,'rotation: culture/sports/online this run',6,'skipped','sensor rotation; news/money/science were read in 2026-10-14T1902Z',[])
DESKS_SWEPT=['politics','entertainment','sports','internet']
for desk in DESKS_SWEPT:
  q=open(f'{WORK}/desk_query_{desk}.txt').read().strip()
  extra=''
  sweep('desk.%s'%desk,'desk',desk,'search_posts_all %s newest first, 25 results; reposted originals screened by the desk floor and pace rule (contract/desks.json)%s'%(q,extra),24,'ok',None,desk_map.get(desk,[])[:5])
for desk in ['world','defense','justice','disaster','markets','business','ai','tech','science','medicine','music','gaming','ideas','life','offbeat']:
  sweep('desk.%s'%desk,'desk',desk,'not due',24,'skipped','not due at 20:02Z: world/justice/markets/ai/tech/medicine/music (2-hour) swept ok at 18:07Z in 2026-10-14T1807Z; ideas/life (4-hour) swept at 18:07Z; gaming/offbeat (2-hour) swept ok in 2026-10-14T1902Z; defense/disaster/business/science (4-hour) swept ok at 17:04Z in 2026-10-14T1704Z',[])
sweep('context.top','context',None,'not run',None,'skipped','cut for time this run',[])
answers=[]
for r in json.load(open(f'{REPO}/requests/open.json'))['requests']:
  sweep('request.%s'%r['id'],'request',None,'open request deferred',None,'skipped','deferred this run for time; watched ids re-read in watch',[])

reason=('4:02 PM ET run (20 UTC Oct 14): %d X reads (%d to %d left today). Watch %d of %d ids returned (watch.json plus the posts first captured in 2026-10-14T1406Z through 1902Z, the 6-to-24-hour posts still gaining 2 percent, and the fourth-hour rest of the last 24 hours; 2110417903740973149 Not Found, recorded unavailable); trends US+WW; trend names #MCIPSG (one event with Donnarumma, Doue, Dembele: Manchester City v PSG), Roma and Real Madrid (one event with Valverde, Tchouameni: Roma v Real Madrid), Dudus (one event with Diddy), Wide Deceiver; Starlink had posts attached in 1902Z, LASK left as a continuing match name; quote/repost words "this", "is", "you", "and" (3+1); sensors culture/sports/online; desks politics, entertainment, sports, internet (the 2-hour desks were 1 h 55 min from their last sweep, not due); two screening reads by id of 117 second-hop, reply-parent and media-source posts. No volume, story clusters, context.top or media descriptions; x_stories omitted; open requests deferred. Skipped sexual or graphic ids are in exclude_ids.json and build_meta.json in the work folder.' % (READS_START-READS_END, READS_START, READS_END, n_watch_ret, n_watch_planned))

doc={
  'schema':'mts.capture/1',
  'run':{
    'id':RUN_ID,
    'started_at':STARTED,
    'finished_at':FINISHED,
    'status':'partial',
    'reason':reason,
    'grabber':{'agent':'grokbot','model':None,'method':'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid)'},
    'requests_rev':REQ_REV,
  },
  'sweeps':sweeps,
  'trends':trends,
  'posts':posts,
  'observations':observations,
  'context':[],
  'answers':answers,
}
os.makedirs(f'{REPO}/capture/2026/10/14',exist_ok=True)
out=f'{REPO}/capture/2026/10/14/2002Z.json'
open(out,'w').write(json.dumps(doc, indent=2, ensure_ascii=False)+'\n')
print('wrote', out, 'posts', len(posts), 'obs', len(observations), 'sweeps', len(sweeps))
print('viral', len(viral_ids), 'rising', len(rising_ids))
print('top posts', [(p['id'], p['author']['handle'], views_of(p['id']), p['desk']) for p in posts[:10]])
print('press_ids', press_ids)
print('author drops', dict(dropped_by_author))
print('skipped_sensitive', len(set(skipped_sensitive)))

# update TALLY
tally_path=f'{REPO}/capture/TALLY.json'
tally=json.load(open(tally_path))
origins=list(dict.fromkeys([o for o in quote_origins+repost_origins if o]))
runs=[r for r in (tally.get('runs') or []) if r.get('run')!=RUN_ID]
seen_runs=set(); cleaned=[]
for r in runs:
  if r.get('run') in seen_runs: continue
  seen_runs.add(r.get('run')); cleaned.append(r)
cleaned.append({'run':RUN_ID,'origins':origins})
tally['runs']=cleaned[-6:]
open(tally_path,'w').write(json.dumps(tally, indent=2, ensure_ascii=False)+'\n')
print('tally runs', [r['run'] for r in tally['runs']], 'origins', len(origins))

# notes line
note_extra=''
if dropped_by_author:
  note_extra=' Author-cap dropped: '+', '.join('%s x%d'%(h,n) for h,n in dropped_by_author.most_common())
open(f'{WORK}/build_meta.json','w').write(json.dumps({
  'posts':len(posts),'obs':len(observations),'author_drops':dict(dropped_by_author),
  'skipped_sensitive':sorted(set(skipped_sensitive))[:20],
  'note_extra':note_extra,
}, indent=2))
