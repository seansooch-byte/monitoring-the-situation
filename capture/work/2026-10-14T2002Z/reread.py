import json,glob
from datetime import datetime,timezone
REPO='/workspace/monitoring-the-situation'
NOW=datetime.now(timezone.utc)
watch=json.load(open(f'{REPO}/requests/watch.json'))['post_ids']
caps=sorted(glob.glob(f'{REPO}/capture/2026/10/1[0-4]/*.json'))
first={}; obs={}
for c in caps:
  d=json.load(open(c))
  st=datetime.fromisoformat(d['run']['started_at'].replace('Z','+00:00'))
  for p in d['posts']:
    if p['id'] not in first: first[p['id']]=(st,p.get('created_at'))
  for o in d['observations']:
    obs.setdefault(o['id'],[]).append(o)
def age(created):
  return (NOW-datetime.fromisoformat(created.replace('Z','+00:00'))).total_seconds()/3600
tier2=[];tier3=[]
for i,(st,cr) in first.items():
  if not cr: continue
  if age(cr)>=24: continue
  h=(NOW-st).total_seconds()/3600
  if h<=6: tier2.append(i)
  elif h<=24:
    v=[o['views'] for o in obs.get(i,[]) if o.get('views')]
    if len(v)>=2 and v[-2] and (v[-1]-v[-2])/v[-2]>=0.02: tier3.append(i)
ids=list(dict.fromkeys(watch+tier2+tier3))
print('watch',len(watch),'tier2',len(tier2),'tier3',len(tier3),'total',len(ids))
ids=ids[:400]
open('reread_ids.txt','w').write('\n'.join(ids))
for k in range(0,len(ids),100):
  open(f'watch_ids_{k//100+1}.txt','w').write(','.join(ids[k:k+100]))
