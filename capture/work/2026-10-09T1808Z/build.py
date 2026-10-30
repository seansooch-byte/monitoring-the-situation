import json, os
from datetime import datetime, timezone
from collections import Counter

WORK='/workspace/monitoring-the-situation/capture/work/2026-10-09T1808Z'
REPO='/workspace/monitoring-the-situation'
NOW=datetime(2026,10,9,18,13,tzinfo=timezone.utc)
RUN_ID='2026-10-09T1808Z'
AT='2026-10-09T18:13:00Z'
STARTED='2026-10-09T18:08:00Z'
FINISHED='2026-10-09T18:15:00Z'
REQ_REV=open(f'{WORK}/requests_rev.txt').read().strip()
READS_START=659
READS_END=642

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

EXCLUDE_IDS=set([
  '2108124415762592123','2107389692018622901','2108366539439411593',
  '2107759105586921862','2107898516836073615','2107914086675788263',
  '2107913429990166804','2108289854974951548','2108325927872803119',
  '2108511541351837778','2108378335512293747','2108437202543800337',
  '2105144159715643542','210200681','2107407108446790049',
  '2108531741883560072','2107219727701746162','2108211566034440579',
  '2108148098182836497','2107950433654235262','1883242684762255643',
  '2108573302612504596','2100889316075651135','2108591066077118717',
  '2108368510816596206','2108538963732414892','2105701698513567928',
  '2108264549707329662','2108327411746255354','2108599428894642631',
  '2108620753218252866',
])
EXCLUDE_SUBSTR=['hentai','porn','pussy','masturbat','getting laid','raped a','9-year-old','9 year old','onlyfans','#mom #mommy #stepmom','ass-to-mouth','cockyboys','creamy pussy','tiny tits','sissy','help me cum','prostate massager','oral sex','Ladyboy','Shemale','#nsfw','#hentai','penetrators','face fuck','AI girlfriend','sexy, witty']

def bad_text(s):
  sl=(s or '').lower()
  return any(x in sl for x in EXCLUDE_SUBSTR)

all_tweets={}; all_users={}; all_media={}
watch_docs=[]
for i in range(0,3):
  p=f'{WORK}/watch_{i}.json'
  if os.path.exists(p):
    watch_docs.append(load_x(p))

screen_docs=[]
for name in ['screen.json','sensor_money.json','repost_0.json','quote_1.json','desk_internet.json','trend_mcbride.json']:
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
  for err in doc.get('errors') or []:
    # unavailable ids
    rid=err.get('resource_id') or err.get('value')
    if rid and rid not in watch_returned:
      pass
for wid in watch_ids:
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
  if any(w in tl for w in ['hurricane','isaias','storm surge','landfall','earthquake']): return 'disaster'
  if 'nobel' in tl or 'pillay' in tl or 'icc' in tl or 'starlink' in tl or 'ambani' in tl: return 'world'
  if any(w in tl for w in ['trump','democrat','republican','congress','senate','election','governor','white house','supreme court','charlie kirk','execution','endwokeness','hegseth','jd vance','rubio']): return 'politics'
  if any(w in tl for w in ['ditka','bears','nfl','nba','mlb','f1','soccer','touchdown','kelce','cowboys','bucs','wnba','ufc','schefter','super bowl','premier league','mcbride','caitlin clark']): return 'sports'
  if any(w in tl for w in ['anime','movie','trailer','actor','actress','netflix','episode','season','celebrity','film','avatar','marvel','sinners','emmy']): return 'entertainment'
  if any(w in tl for w in ['bitcoin','crypto','stocks','nasdaq','fed ']): return 'markets'
  if any(w in tl for w in ['openai','anthropic','chatgpt','gemini','grok','llm','ai ' ,'math papers']): return 'ai'
  if any(w in tl for w in ['vaccine','hhs','kennedy','nih','mold','fungal']): return 'medicine'
  if any(w in tl for w in ['meme','tiktok','streamer','twitch','youtube','fandom','kick ']): return 'internet'
  return 'internet'

NEWS_HANDLES=set(h.lower() for h in ['Reuters','BBCBreaking','SkyNews','nytimes','cnnbrk','cnni','NobelPrize','PTI_News','WFLA','MeidasTouch','LeadingReport','visegrad24','CNN','BBCWorld','FoxNews','weatherchannel','BNONews','MyRadarWX','Forbes','AP'])

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

posts=[]; viral_ids=[]; rising_ids=[]
desk_map={k:[] for k in ['politics','entertainment','sports','internet','world','markets','ai','disaster','medicine']}
mcbride_keep=open(f'{WORK}/trend_mcbride_top3.txt').read().splitlines()
trend_keep=set(mcbride_keep)
ditka_keep=['2108575881996210210','2108584126420844732','2108596213046210970']
trend_keep |= set(ditka_keep)
kirk_keep=['2108532428482433526','2108426931364401393','2108535196601700564']
trend_keep |= set(kirk_keep)

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

# Prefer screen.json data as primary new posts; also includes from stream files for metrics
screen_tweets=[]
for doc in screen_docs:
  for t in doc.get('data') or []:
    # skip pure RTs without being origins - for screen.json data are originals
    refs=t.get('referenced_tweets') or []
    if any(r.get('type')=='retweeted' for r in refs) and 'RT @' in (t.get('text') or '')[:5]:
      continue
    screen_tweets.append(t)
  for t in (doc.get('includes') or {}).get('tweets') or []:
    screen_tweets.append(t)

seen_screen=set(); screen_unique=[]
for t in screen_tweets:
  if t['id'] in seen_screen: continue
  seen_screen.add(t['id']); screen_unique.append(t)

for t in screen_unique:
  tid=t['id']
  if tid in EXCLUDE_IDS: continue
  if tid in watch_ids: continue
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
  if age is not None and age > 48 and 'old_content' not in flags and tid not in trend_keep:
    continue
  desk=assign_desk(txt)
  ok=clears_desk(m, age, akind) or clears_global(m, age, akind)
  lead=None
  if tid in mcbride_keep:
    ok=True
    lead='trend context for McBride; no floor'
  if tid in ditka_keep:
    ok=True
    lead = (lead + '; trend context for Mike Ditka') if lead else 'trend context for Mike Ditka; no floor'
  if tid in kirk_keep:
    ok=True
    lead = (lead + '; trend context for Charlie Kirk') if lead else 'trend context for Charlie Kirk; no floor'
  if tid in this_stream:
    n=tally_lead.get(tid,0)+1
    extra='seen in the quote or repost stream in %d of the last 6 runs' % min(n,6)
    lead=(lead+'; '+extra) if lead else extra
  if not ok: continue
  handle=u.get('username')
  if not handle:
    # try to keep if we have author_id but missing user - skip
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
  if desk in desk_map:
    desk_map[desk].append(tid)

seenp=set(); posts2=[]
for p in posts:
  if p['id'] in seenp: continue
  seenp.add(p['id']); posts2.append(p)

def views_of(pid):
  tw=all_tweets.get(pid) or {}
  return (tw.get('public_metrics') or {}).get('impression_count') or 0

posts2.sort(key=lambda p: -views_of(p['id']))
posts=posts2[:40]
kept=set(p['id'] for p in posts)
for p in posts:
  add_obs(p['id'], all_tweets.get(p['id']))
viral_ids=[i for i in viral_ids if i in kept][:40]
rising_ids=[i for i in rising_ids if i in kept][:30]
for k in desk_map:
  desk_map[k]=[i for i in desk_map[k] if i in kept][:10]
mcbride_ids=[i for i in mcbride_keep if i in kept or i in all_tweets]
ditka_ids=[i for i in ditka_keep if i in kept or i in watch_returned]
kirk_ids=[i for i in kirk_keep if i in kept or i in watch_returned]

# Ensure McBride trend posts are in posts even if low views
for mid in mcbride_keep:
  if mid in kept: continue
  t=all_tweets.get(mid)
  if not t: continue
  u=all_users.get(t.get('author_id'),{})
  handle=u.get('username')
  if not handle: continue
  txt=text_of(t)
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
    'flags': [],
    'desk': 'sports',
    'beat': None,
    'topic': None,
    'lead': 'trend context for McBride; no floor',
  })
  add_obs(mid, t)
  kept.add(mid)
  if mid not in viral_ids: viral_ids.append(mid)
  desk_map['sports'].append(mid)
posts=posts[:40]
kept=set(p['id'] for p in posts)
mcbride_ids=[i for i in mcbride_keep if i in kept]

sensor_kept={g:[] for g in ['news','money','science']}
for g,fn in [('news','sensor_news_top.txt'),('money','sensor_money_top.txt'),('science','sensor_science_top.txt')]:
  p=f'{WORK}/{fn}'
  if os.path.exists(p):
    for pid in open(p).read().splitlines():
      if not pid: continue
      if (pid in kept or pid in watch_returned) and pid not in sensor_kept[g]:
        sensor_kept[g].append(pid)
for g in sensor_kept:
  sensor_kept[g]=sensor_kept[g][:15]

us=json.load(open(f'{WORK}/trends_us.json'))['data']
ww=json.load(open(f'{WORK}/trends_ww.json'))['data']
trends=[]
for i,t in enumerate(us[:20],1):
  name=t['trend_name']
  pids=[]
  if name=='Mike Ditka':
    pids=ditka_ids[:3]
  elif name in ('Da Bears','Chicago Bears','RIP Legend','85 Bears') and ditka_ids:
    pids=ditka_ids[:2]
  elif name=='Charlie Kirk':
    pids=kirk_ids[:3]
  elif name=='McBride':
    pids=mcbride_ids[:3]
  trends.append({'region':'US','rank':i,'name':name,'post_count':None,'story':None,'post_ids':pids})
for i,t in enumerate(ww[:20],1):
  name=t['trend_name']
  pids=[]
  if name=='Mike Ditka' and ditka_ids:
    pids=ditka_ids[:3]
  elif name=='Da Bears' and ditka_ids:
    pids=ditka_ids[:1]
  elif name=='Da Coach' and ditka_ids:
    pids=ditka_ids[:1]
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

n_watch_planned=len(reread)
n_watch_ret=len(watch_returned)
sweep('watch','watch',None,'get_posts_by_ids of requests/watch.json plus recent capture posts (%d ids planned, %d returned in 3 saved batches); fields created_at,public_metrics,author_id,referenced_tweets,attachments,entities,lang,note_tweet,conversation_id,edit_history_tweet_ids,possibly_sensitive; expansions author_id,attachments.media_keys,attachments.media_source_tweet_id,referenced_tweets.id'%(n_watch_planned,n_watch_ret),None,'ok',None,watch_post_ids)
sweep('trends.us','trends',None,'get_trends_by_woeid 23424977 max 20',None,'ok',None,[])
sweep('trends.ww','trends',None,'get_trends_by_woeid 1 max 20',None,'ok',None,[])
sweep('viral.global','discovery',None,'quote/repost stream word "and" (2 quote pages + 1 repost) plus sensors news/money/science, trend name McBride, hourly desks; screened by id; global floor/pace',24,'ok',None,viral_ids)
sweep('rising.global','discovery',None,'2 quote pages + 1 repost page: "and" lang:en is:quote -is:retweet / is:retweet, newest first, 25 each',6,'ok',None,rising_ids)
for g in ['news','money','science']:
  method='(from:sensor accounts in capture/SENSORS.md %s group) -is:reply newest 25; origins followed'%g
  sweep('sensors.%s'%g,'discovery',None,method,6,'ok',None,sensor_kept[g])
for g in ['culture','sports','online']:
  sweep('sensors.%s'%g,'discovery',None,'rotation: news/money/science this run',6,'skipped','sensor rotation; next run',[])
for desk in ['politics','entertainment','sports','internet']:
  sweep('desk.%s'%desk,'desk',desk,'standing query from CAPABILITIES.md lang:en is:retweet -is:reply newest 25; origins screened by pace/floor',24,'ok',None,desk_map.get(desk,[]))
other_skip=['world','defense','justice','disaster','markets','business','crypto','ai','tech','science','medicine','music','gaming','ideas','life','offbeat']
for desk in other_skip:
  sweep('desk.%s'%desk,'desk',desk,'due but cut for budget',24,'skipped','cut order: non-hourly desks after hourly; day budget',[])
sweep('context.top','context',None,'skipped to leave budget for watch/sensors/desks',None,'skipped','budget: cut context',[])
answers=[]
for r in json.load(open(f'{REPO}/requests/open.json'))['requests']:
  sweep('request.%s'%r['id'],'request',None,'open request deferred',None,'skipped','deferred this hour for budget; watch includes related ids where applicable',[])

reason=('daytime run at 2:08 PM ET (18 UTC): %d X reads (%d to %d left today). Watch %d; trends US+WW; quote/repost word "and" (2+1); sensors news/money/science; hourly desks politics/entertainment/sports/internet; trend stream McBride; screen 35 by id. No volume, story clusters, context.top, or media descriptions; x_stories omitted. Non-hourly desks skipped after cut order. SKIP/SKIP_ALL absent on pipeline.' % (READS_START-READS_END, READS_START, READS_END, n_watch_ret))

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
out=f'{REPO}/capture/2026/10/09/1808Z.json'
open(out,'w').write(json.dumps(doc, indent=2, ensure_ascii=False)+'\n')
print('wrote', out, 'posts', len(posts), 'obs', len(observations), 'sweeps', len(sweeps))

tally_path=f'{REPO}/capture/TALLY.json'
tally=json.load(open(tally_path))
origins=list(dict.fromkeys(quote_origins+repost_origins))
runs=[r for r in (tally.get('runs') or []) if r.get('run')!=RUN_ID]
seen_runs=set(); cleaned=[]
for r in runs:
  if r.get('run') in seen_runs: continue
  seen_runs.add(r.get('run')); cleaned.append(r)
cleaned.append({'run':RUN_ID,'origins':origins})
tally['runs']=cleaned[-6:]
open(tally_path,'w').write(json.dumps(tally, indent=2, ensure_ascii=False)+'\n')
print('tally runs', [r['run'] for r in tally['runs']], 'origins', len(origins))
print('viral', len(viral_ids), 'rising', len(rising_ids), 'desks', {k:len(v) for k,v in desk_map.items() if v})
