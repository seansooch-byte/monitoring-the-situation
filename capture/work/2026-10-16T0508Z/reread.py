import json,glob
from datetime import datetime,timezone
REPO='/workspace/monitoring-the-situation'
NOW=datetime.now(timezone.utc)
watch=json.load(open(f'{REPO}/requests/watch.json'))['post_ids']
caps=sorted(glob.glob(f'{REPO}/capture/2026/10/1[0-6]/*.json'))
first={}; obs={}; unavail=set()
for c in caps:
  d=json.load(open(c))
  st=datetime.fromisoformat(d['run']['started_at'].replace('Z','+00:00'))
  for p in d['posts']:
    if p['id'] not in first: first[p['id']]=(st,p.get('created_at'))
  for o in d['observations']:
    obs.setdefault(o['id'],[]).append(o)
    if o.get('state')=='unavailable': unavail.add(o['id'])
def age(created):
  return (NOW-datetime.fromisoformat(created.replace('Z','+00:00'))).total_seconds()/3600
tier2=[];tier3=[];tier4=[]
def growth(i):
  v=[o['views'] for o in obs.get(i,[]) if o.get('views')]
  return (v[-1]-v[-2])/v[-2] if len(v)>=2 and v[-2] else 0
for i,(st,cr) in first.items():
  if not cr or i in unavail: continue
  if age(cr)>=24: continue
  h=(NOW-st).total_seconds()/3600
  if h<=6: tier2.append(i)
  elif h<=24:
    if growth(i)>=0.02: tier3.append(i)
    else: tier4.append(i)
tier4.sort(key=lambda i:growth(i))  # slowest growing last (ascending growth)
FOURTH=False  # 05Z is not a fourth hour
ids=list(dict.fromkeys(watch+tier2+tier3+(tier4 if FOURTH else [])))
print('watch',len(watch),'tier2',len(tier2),'tier3',len(tier3),'tier4',len(tier4),'before_cap',len(ids),'FOURTH',FOURTH)
left_out=max(0,len(ids)-400)
ids=ids[:400]
print('total',len(ids),'left_out_by_cap',left_out)
open('reread_ids.txt','w').write('\n'.join(ids))
for k in range(0,len(ids),100):
  open(f'watch_ids_{k//100}.txt','w').write(','.join(ids[k:k+100]))
print('batches', (len(ids)+99)//100)
