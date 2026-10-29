import json,glob,sys,statistics
from datetime import datetime
runs=sys.argv[1].split(',')
files=[f'capture/2026/10/29/{r}.json' for r in runs]
views={};first={};fam={}
def ts(s): return datetime.fromisoformat(s.replace('Z','+00:00'))
for f in files:
  c=json.load(open(f)); st=ts(c['run']['started_at'])
  ids={p['id'] for p in c['posts']}
  for p in c['posts']:
    if p['id'] not in first: first[p['id']]=(ts(p['created_at']),st)
  for o in c['observations']:
    if o['id'] in ids or o['id'] in views: 
      if o.get('views') is not None: views[o['id']]=o['views']
  def add(i,k):
    if i in ids: fam.setdefault(k,set()).add(i)
  for s in c['sweeps']:
    k={'viral':'viral.global','sensors':'sensors','rising':'rising','desk':'desk'}.get(s['id'].split('.')[0])
    if k:
      for i in s['post_ids']: add(i,k)
  for t in c.get('trends') or []:
    for i in t.get('post_ids') or []: add(i,'trend names')
P=[i for i in first]
v=[views.get(i,0) for i in P]
age=[(first[i][1]-first[i][0]).total_seconds()/3600 for i in P]
print(len(P),sum(x>1e6 for x in v),sum(x>5e6 for x in v),sum(x>1e7 for x in v),max(v),int(statistics.median(v)),round(statistics.median(age),2))
for k in ['viral.global','sensors','trend names','rising','desk']:
  vv=[views.get(i,0) for i in fam.get(k,())]; print(k, (max(vv), int(statistics.median(vv))) if vv else "n/a")
