import json, os
from datetime import datetime, timezone

WORK='/workspace/monitoring-the-situation/capture/work/2026-10-09T1011Z'
REPO='/workspace/monitoring-the-situation'
NOW=datetime(2026,10,9,10,15,tzinfo=timezone.utc)
RUN_ID='2026-10-09T1011Z'
AT='2026-10-09T10:15:00Z'
STARTED='2026-10-09T10:11:00Z'
FINISHED='2026-10-09T10:18:00Z'
REQ_REV='be899e747ba385d0d7316b9965799591c197b0c2'

def load_x(path):
  raw=open(path).read()
  if 'X reads left' in raw:
    raw=raw[:raw.rfind('X reads left')]
  start=raw.find('{'); end=raw.rfind('}')+1
  return json.loads(raw[start:end])

def verified_of(u):
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
    if typ=='photo': typ='image'
    elif typ=='animated_gif': typ='gif'
    elif typ=='video': typ='video'
    else: typ=typ or 'image'
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
        'type':'link',
        'description': None,
        'alt': None,
        'duration_s': None,
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

EXCLUDE_IDS=set([
  '2108124415762592123','2107389692018622901','2108366539439411593',
  '2107759105586921862','2107898516836073615','2107914086675788263',
  '2107913429990166804','2108289854974951548','2108325927872803119',
])
EXCLUDE_SUBSTR=['hentai','porn','pussy','masturbat','getting laid','raped a','9-year-old','9 year old']

def bad_text(s):
  sl=(s or '').lower()
  return any(x in sl for x in EXCLUDE_SUBSTR)

watch_docs=[]
for i in range(1,5):
  p=f'{WORK}/watch_{i}.json'
  if os.path.exists(p):
    watch_docs.append(load_x(p))

screen=load_x(f'{WORK}/screen.json')
navi=json.load(open(f'{WORK}/navi_posts.json'))

all_tweets={}; all_users={}; all_media={}
for doc in watch_docs+[screen,navi]:
  for u in (doc.get('includes') or {}).get('users') or []:
    all_users[u['id']]=u
  for m in (doc.get('includes') or {}).get('media') or []:
    all_media[m['media_key']]=m
  for t in (doc.get('includes') or {}).get('tweets') or []:
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
for wid in watch_ids:
  if wid not in watch_returned:
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
  if 'nobel' in tl or 'pillay' in tl: return 'world'
  if any(w in tl for w in ['trump','democrat','republican','congress','senate','election','governor','white house']): return 'politics'
  if any(w in tl for w in ['nfl','nba','mlb','f1','soccer','touchdown','kelce','cowboys','bucs']): return 'sports'
  if any(w in tl for w in ['anime','movie','trailer','actor','actress','netflix','episode','season','cuphead']): return 'entertainment'
  if any(w in tl for w in ['meme','tiktok','streamer','twitch','ai ','code ','slop']): return 'internet'
  if any(w in tl for w in ['gas','gallon','california']): return 'markets'
  return 'internet'

def kind_of_user(u):
  un=(u.get('username') or '').lower()
  if any(x in un for x in ['nytimes','reuters','bbc','pti_news','nobelprize']):
    return 'news'
  if un.endswith('news') or 'news' in un:
    return 'news'
  return 'unknown'

posts=[]; viral_ids=[]; rising_ids=[]
desk_map={k:[] for k in ['politics','entertainment','sports','internet','world','markets']}
navi_keep=['2108482846449189371','2108486031528149149','2108488145348038702']

for t in (screen.get('data') or []) + (navi.get('data') or []):
  tid=t['id']
  if tid in EXCLUDE_IDS: continue
  txt=text_of(t)
  if bad_text(txt): continue
  if t.get('possibly_sensitive'): continue
  u=all_users.get(t.get('author_id'),{})
  m=metrics(t)
  age=age_hours(t.get('created_at'))
  akind=kind_of_user(u)
  flags=[]
  if age is not None and age > 24*7:
    flags.append('old_content')
  if age is not None and age > 48 and 'old_content' not in flags:
    continue
  desk=assign_desk(txt)
  ok=clears_desk(m, age, akind) or clears_global(m, age, akind)
  lead=None
  if tid in navi_keep:
    ok=True
    lead='trend context for Navi Pillay / Nobel Peace Prize; no floor'
  if not ok: continue
  handle=u.get('username')
  if not handle: continue
  if age is not None and 0.25<=age<3 and (m['views'] or 0) < 100000:
    pace=int((m['views'] or 0)/age) if age else 0
    extra='pace about %d views/hour at read' % pace
    lead=(lead+'; '+extra) if lead else extra
  created=(t.get('created_at') or '').replace('.000Z','Z').replace('+00:00','Z')
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
  add_obs(tid, t)
  if clears_global(m, age, akind) or tid in navi_keep:
    viral_ids.append(tid)
  if age is not None and age < 6:
    rising_ids.append(tid)
  if desk in desk_map:
    desk_map[desk].append(tid)

seenp=set(); posts2=[]
for p in posts:
  if p['id'] in seenp: continue
  seenp.add(p['id']); posts2.append(p)
posts=posts2[:40]
kept=set(p['id'] for p in posts)
viral_ids=[i for i in viral_ids if i in kept][:40]
rising_ids=[i for i in rising_ids if i in kept][:30]
for k in desk_map:
  desk_map[k]=[i for i in desk_map[k] if i in kept][:10]
navi_ids=[i for i in navi_keep if i in kept]

us=json.load(open(f'{WORK}/trends_us.json'))['data']
ww=json.load(open(f'{WORK}/trends_ww.json'))['data']
trends=[]
for i,t in enumerate(us[:20],1):
  name=t['trend_name']
  pids=navi_ids[:3] if name=='Navi Pillay' else []
  trends.append({'region':'US','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})
for i,t in enumerate(ww[:20],1):
  trends.append({'region':'WW','rank':i,'name':t['trend_name'],'post_count':None,'story':None,'post_ids':[]})

watch_post_ids=list(watch_ids)+[i for i in open(f'{WORK}/reread_ids.txt').read().split() if i not in watch_ids]
watch_post_ids=[i for i in watch_post_ids if i in seen_obs][:400]

sweeps=[]
def sweep(sid, kind, desk, method, window, status, reason, pids):
  sweeps.append({'id':sid,'kind':kind,'desk':desk,'method':method,'window_hours':window,'status':status,'reason':reason,'post_ids':pids})

sweep('watch','watch',None,'get_posts_by_ids of requests/watch.json plus posts first captured in last 6h (400 ids, 4 calls); fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id',None,'ok',None,watch_post_ids)
sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max 20',None,'ok',None,[])
sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[])
sweep('viral.global','discovery',None,'quote/repost stream word "it" plus desk origins screened by id; global floor/pace',24,'partial','overnight lean: streams+desks only; sensors/story clusters skipped',viral_ids)
sweep('rising.global','discovery',None,'quote stream and repost stream with word "it" (quoted), newest first, 25 each; 1 quote page and 1 repost page',6,'ok',None,rising_ids)
for g in ['news','money','science','culture','sports','online']:
  sweep('sensors.%s'%g,'discovery',None,'skipped overnight budget',6,'skipped','overnight lean (06-11 UTC budget)',[])
for desk in ['politics','entertainment','sports','internet']:
  sweep('desk.%s'%desk,'desk',desk,'standing query lang:en is:retweet -is:reply newest 25; origins screened',24,'ok',None,desk_map.get(desk,[]))
for desk in ['world','defense','justice','disaster','markets','business','crypto','ai','tech','science','medicine','music','gaming','ideas','life','offbeat']:
  sweep('desk.%s'%desk,'desk',desk,'skipped',24,'skipped','overnight: hourly desks only',[])
sweep('context.top','context',None,'skipped overnight',None,'skipped','overnight lean',[])
for r in json.load(open(f'{REPO}/requests/open.json'))['requests']:
  sweep('request.%s'%r['id'],'request',None,'skipped overnight',None,'skipped','overnight lean budget',[])

doc={
  'schema':'mts.capture/1',
  'run':{
    'id':RUN_ID,
    'started_at':STARTED,
    'finished_at':FINISHED,
    'status':'partial',
    'reason':'overnight-lean run at 6 AM ET (10 UTC): 15 X reads (806 to 791 left today). Watch 400; trends US+WW; quote/repost word "it"; hourly desks politics/entertainment/sports/internet; trend stream Navi Pillay; screen 35+5 by id. No volume, story clusters, sensors, context.top, or media descriptions; x_stories omitted. Excluded NSFW/sexual/minor/piracy ids. Started with 806 left after 0901Z.',
    'grabber':{'agent':'grokbot','model':None,'method':'x MCP namespace (get_posts_by_ids, search_posts_all, get_trends_by_woeid)'},
    'requests_rev':REQ_REV,
  },
  'sweeps':sweeps,
  'trends':trends,
  'posts':posts,
  'observations':observations,
  'context':[],
  'answers':[],
}
out=f'{REPO}/capture/2026/10/09/1011Z.json'
open(out,'w').write(json.dumps(doc, indent=2, ensure_ascii=False)+'\n')
print('wrote', out, 'posts', len(posts), 'obs', len(observations), 'sweeps', len(sweeps))
