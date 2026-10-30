import json, os
from datetime import datetime, timezone

WORK='/workspace/monitoring-the-situation/capture/work/2026-10-09T1212Z'
REPO='/workspace/monitoring-the-situation'
NOW=datetime(2026,10,9,12,20,tzinfo=timezone.utc)
RUN_ID='2026-10-09T1212Z'
AT='2026-10-09T12:20:00Z'
STARTED='2026-10-09T12:12:00Z'
FINISHED='2026-10-09T12:22:00Z'
REQ_REV='be899e747ba385d0d7316b9965799591c197b0c2'
READS_START=770
READS_END=748

def load_x(path):
  raw=open(path).read()
  if 'X reads left' in raw:
    raw=raw[:raw.rfind('X reads left')]
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
    if typ=='photo': typ='photo'
    elif typ=='animated_gif': typ='gif'
    elif typ=='video': typ='video'
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
  '2108511541351837778',  # sexual Good Friday
  '2108378335512293747','2108437202543800337',
])
EXCLUDE_SUBSTR=['hentai','porn','pussy','masturbat','getting laid','raped a','9-year-old','9 year old','onlyfans','#mom #mommy #stepmom']

def bad_text(s):
  sl=(s or '').lower()
  return any(x in sl for x in EXCLUDE_SUBSTR)

all_tweets={}; all_users={}; all_media={}
watch_docs=[]
for i in range(0,4):
  p=f'{WORK}/watch_{i}.json'
  if os.path.exists(p):
    watch_docs.append(load_x(p))

screen_docs=[]
for name in ['screen.json','screen2.json']:
  p=f'{WORK}/{name}'
  if os.path.exists(p):
    screen_docs.append(load_x(p))

# also ingest desk includes for author coverage
for name in ['desk_entertainment.json','desk_sports.json','desk_internet.json','quote_just_p2.json','quote_just_p3.json','repost_just.json']:
  p=f'{WORK}/{name}'
  if os.path.exists(p):
    try:
      screen_docs.append(load_x(p))
    except Exception as e:
      print('skip', name, e)

for doc in watch_docs+screen_docs:
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
  if any(w in tl for w in ['trump','democrat','republican','congress','senate','election','governor','white house','supreme court']): return 'politics'
  if any(w in tl for w in ['nfl','nba','mlb','f1','soccer','touchdown','kelce','cowboys','bucs','wnba','ufc']): return 'sports'
  if any(w in tl for w in ['anime','movie','trailer','actor','actress','netflix','episode','season','celebrity','film']): return 'entertainment'
  if any(w in tl for w in ['bitcoin','crypto','stocks','nasdaq','fed ','mortgage']): return 'markets'
  if any(w in tl for w in ['openai','anthropic','chatgpt','gemini','grok','llm','ai ']): return 'ai'
  if any(w in tl for w in ['meme','tiktok','streamer','twitch','youtube','fandom']): return 'internet'
  return 'internet'

NEWS_HANDLES=set('reuters bbcbreaking skynews nytimes cnnbrk cnni nobelprize ptinews wfla meidastouch leadingreport visegrad24'.lower().split() if False else [])
NEWS_HANDLES=set(h.lower() for h in ['Reuters','BBCBreaking','SkyNews','nytimes','cnnbrk','cnni','NobelPrize','PTI_News','WFLA','MeidasTouch','LeadingReport','visegrad24','CNN','BBCWorld'])

def kind_of_user(u):
  un=(u.get('username') or '')
  if un in NEWS_HANDLES or un.lower() in {x.lower() for x in NEWS_HANDLES}:
    return 'news'
  unl=un.lower()
  if any(x in unl for x in ['nytimes','reuters','bbc','pti_news','nobelprize','cnn']):
    return 'news'
  if unl.endswith('news') or 'news' in unl:
    return 'news'
  vt=(u.get('verified_type') or '').lower()
  if vt=='government':
    return 'official'
  if vt=='business':
    return 'org'
  return 'unknown'

posts=[]; viral_ids=[]; rising_ids=[]
desk_map={k:[] for k in ['politics','entertainment','sports','internet','world','markets','ai']}
navi_keep=['2108482846449189371','2108486729426698548','2108486031528149149']
gf_keep=open(f'{WORK}/trend_goodfriday_top3.txt').read().splitlines()
tally_lead={}

# load tally for lead notes
try:
  tally=json.load(open(f'{REPO}/capture/TALLY.json'))
  from collections import Counter
  c=Counter()
  for run in tally.get('runs') or []:
    for o in run.get('origins') or []:
      c[o]+=1
  tally_lead=dict(c)
except Exception:
  pass

# quote/repost origins this run for tally update
quote_origins=open(f'{WORK}/quote_origins_all.txt').read().splitlines()
repost_origins=open(f'{WORK}/repost_origins_all.txt').read().splitlines()
this_stream=set(quote_origins+repost_origins)

screen_tweets=[]
for doc in screen_docs:
  for t in doc.get('data') or []:
    screen_tweets.append(t)

seen_screen=set(); screen_unique=[]
for t in screen_tweets:
  if t['id'] in seen_screen: continue
  seen_screen.add(t['id']); screen_unique.append(t)

for t in screen_unique:
  tid=t['id']
  if tid in EXCLUDE_IDS: continue
  if tid in watch_ids: continue  # watch is observations only unless new record needed - actually watch posts that are new-ish can be in posts from prior; we only add NEW posts from screening
  txt=text_of(t)
  if bad_text(txt): continue
  if t.get('possibly_sensitive'): continue
  u=all_users.get(t.get('author_id'),{})
  m=metrics(t)
  age=age_hours(t.get('created_at'))
  akind=kind_of_user(u)
  flags=[]
  # old origin rule: >7 days older than "now" roughly - use age > 7 days from NOW as old_content when from reference
  if age is not None and age > 24*7:
    flags.append('old_content')
  # keep under ~48h unless trend context or old_content
  if age is not None and age > 48 and 'old_content' not in flags and tid not in navi_keep:
    continue
  desk=assign_desk(txt)
  ok=clears_desk(m, age, akind) or clears_global(m, age, akind)
  lead=None
  if tid in navi_keep:
    ok=True
    lead='trend context for Navi Pillay / Nobel Peace Prize; no floor'
  if tid in gf_keep:
    ok=True
    lead=(lead+'; ') if lead else ''
    lead+='trend context for Good Friday; no floor'
  if tid in this_stream:
    n=tally_lead.get(tid,0)+1
    extra='seen in the quote or repost stream in %d of the last 6 runs' % min(n,6)
    lead=(lead+'; '+extra) if lead else extra
  if not ok: continue
  handle=u.get('username')
  if not handle: continue
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
  # obs added after truncation so every obs has a posts[] record
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
# sort by views desc
posts2.sort(key=lambda p: -((next((o['views'] or 0 for o in observations if o['id']==p['id']),0))))
posts=posts2[:40]
kept=set(p['id'] for p in posts)
for p in posts:
  add_obs(p['id'], all_tweets.get(p['id']))
viral_ids=[i for i in viral_ids if i in kept][:40]
rising_ids=[i for i in rising_ids if i in kept][:30]
for k in desk_map:
  desk_map[k]=[i for i in desk_map[k] if i in kept][:10]
navi_ids=[i for i in navi_keep if i in kept]
gf_ids=[i for i in gf_keep if i in kept]

# sensor kept posts: those from sensor origin lists that cleared
sensor_kept={g:[] for g in ['news','money','science']}
for g, fname in [('news','sensor_news_refs.txt'),('money','sensor_money_refs.txt'),('science','sensor_science_refs.txt')]:
  for pid in open(f'{WORK}/{fname}').read().splitlines():
    if pid in kept:
      sensor_kept[g].append(pid)
  for pid in open(f'{WORK}/sensor_{g}_ids.txt').read().splitlines():
    if pid in kept and pid not in sensor_kept[g]:
      sensor_kept[g].append(pid)
  sensor_kept[g]=sensor_kept[g][:15]

us=json.load(open(f'{WORK}/trends_us.json'))['data']
ww=json.load(open(f'{WORK}/trends_ww.json'))['data']
trends=[]
for i,t in enumerate(us[:20],1):
  name=t['trend_name']
  pids=[]
  if name in ('Navi Pillay','Navanethem "Navi" Pillay','Nobel Peace Prize'):
    pids=navi_ids[:3]
  elif name=='Good Friday':
    pids=gf_ids[:3]
  trends.append({'region':'US','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})
for i,t in enumerate(ww[:20],1):
  name=t['trend_name']
  pids=navi_ids[:3] if name=='Navi Pillay' else []
  trends.append({'region':'WW','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})

reread=open(f'{WORK}/reread_ids.txt').read().splitlines()
watch_post_ids=[]
seenw=set()
for i in watch_ids+reread:
  if i not in seenw and i in seen_obs:
    watch_post_ids.append(i); seenw.add(i)
watch_post_ids=watch_post_ids[:400]

sweeps=[]
def sweep(sid, kind, desk, method, window, status, reason, pids):
  sweeps.append({'id':sid,'kind':kind,'desk':desk,'method':method,'window_hours':window,'status':status,'reason':reason,'post_ids':pids})

sweep('watch','watch',None,'get_posts_by_ids of requests/watch.json plus posts first captured in last 6h and gaining (400 ids, 4 calls); fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id',None,'ok',None,watch_post_ids)
sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max 20',None,'ok',None,[])
sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[])
sweep('viral.global','discovery',None,'quote/repost stream word "just" plus sensors news/money/science, trend names, hourly desks; screened by id; global floor/pace',24,'ok',None,viral_ids)
sweep('rising.global','discovery',None,'3 quote pages + 1 repost page: just lang:en is:quote -is:retweet / is:retweet, newest first, 25 each',6,'ok',None,rising_ids)
for g in ['news','money','science']:
  sweep('sensors.%s'%g,'discovery',None,'(from:sensor accounts in capture/SENSORS.md %s group) -is:reply newest 25; origins followed'%g,6,'ok',None,sensor_kept[g])
for g in ['culture','sports','online']:
  sweep('sensors.%s'%g,'discovery',None,'rotation: news/money/science this run',6,'skipped','sensor rotation; next run',[])
for desk in ['politics','entertainment','sports','internet']:
  sweep('desk.%s'%desk,'desk',desk,'standing query from CAPABILITIES.md lang:en is:retweet -is:reply newest 25; origins screened by pace/floor',24,'ok',None,desk_map.get(desk,[]))
for desk in ['world','defense','justice','disaster','markets','business','crypto','ai','tech','science','medicine','music','gaming','ideas','life','offbeat']:
  sweep('desk.%s'%desk,'desk',desk,'due but cut for budget',24,'skipped','cut order: non-hourly desks after hourly; day budget 45',[])
sweep('context.top','context',None,'skipped to leave budget for watch/sensors/desks',None,'skipped','budget: cut context',[])
# requests: answer notice r-11 if not already; others skipped with reason
answers=[]
for r in json.load(open(f'{REPO}/requests/open.json'))['requests']:
  if r['id']=='r-2026-10-09-11':
    sweep('request.%s'%r['id'],'request',None,'notice acknowledged in prior overnight runs; re-ack',None,'ok',None,[])
    answers.append({'request_id':r['id'],'status':'ok','post_ids':[],'note':'acknowledged: pace floor 15m + tenth views + news totals-only; x_stories optional; 20-minute reaction windows; per-post quote/reply series in rotation; editor briefs noted'})
  else:
    sweep('request.%s'%r['id'],'request',None,'open request deferred',None,'skipped','answered once previously or deferred this hour for budget',[])

reason=('daytime run at 8 AM ET (12 UTC): %d X reads (%d to %d left today). Watch 400; trends US+WW; quote/repost word \"just\" (3+1); sensors news/money/science; hourly desks politics/entertainment/sports/internet; trend streams Good Friday + Navi Pillay/Nobel Peace Prize; screen 100 by id. No volume, story clusters, context.top, or media descriptions; x_stories omitted. Excluded NSFW/sexual ids including Good Friday Labonitas. Non-hourly desks skipped after cut order. Started ~%d left after overnight runs.' % (READS_START-READS_END, READS_START, READS_END, READS_START))

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
out=f'{REPO}/capture/2026/10/09/1212Z.json'
open(out,'w').write(json.dumps(doc, indent=2, ensure_ascii=False)+'\n')
print('wrote', out, 'posts', len(posts), 'obs', len(observations), 'sweeps', len(sweeps), 'answers', len(answers))

# update TALLY.json keep last 6
tally_path=f'{REPO}/capture/TALLY.json'
tally=json.load(open(tally_path))
origins=list(dict.fromkeys(quote_origins+repost_origins))
tally['runs']= (tally.get('runs') or []) + [{'run':RUN_ID,'origins':origins}]
tally['runs']=tally['runs'][-6:]
open(tally_path,'w').write(json.dumps(tally, indent=2, ensure_ascii=False)+'\n')
print('tally runs', len(tally['runs']), 'origins this run', len(origins))
