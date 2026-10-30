import json,glob,sys,statistics as st
from datetime import datetime
files=sorted(glob.glob('capture/2026/10/25/*.json'))
if len(sys.argv)>1: files=[f for f in files if f.split('/')[-1] in sys.argv[1:]]
last={};first_age={};src={}
for f in files:
  d=json.load(open(f)); stt=datetime.fromisoformat(d['run']['started_at'].replace('Z','+00:00'))
  for p in d['posts']:
    if p['id'] not in first_age and p.get('created_at'):
      first_age[p['id']]=(stt-datetime.fromisoformat(p['created_at'].replace('Z','+00:00'))).total_seconds()/3600
  for o in d['observations']:
    if o.get('views') is not None: last[o['id']]=o['views']
  for s in d['sweeps']:
    fam=s['id'].split('.')[0]
    if fam=='trends': fam='trend names'
    if fam=='sensors': fam='sensors'
    if fam=='rising': fam='rising'
    if fam=='viral': fam='viral.global'
    for i in s.get('post_ids') or []: src.setdefault(fam,set()).add(i)
  for t in d.get('trends') or []:
    for i in t.get('post_ids') or []: src.setdefault('trend names',set()).add(i)
posts=set()
for f in files: posts|={p['id'] for p in json.load(open(f))['posts']}
v=[last.get(i,0) for i in posts]
print(len(files),len(posts),sum(x>1e6 for x in v),sum(x>5e6 for x in v),sum(x>1e7 for x in v),max(v),int(st.median(v)),round(st.median([first_age[i] for i in posts if i in first_age]),2))
for k in ['viral.global','sensors','trend names','rising','desk']:
  vv=[last.get(i,0) for i in src.get(k,set()) if i in posts]
  print(k, max(vv) if vv else None, int(st.median(vv)) if vv else None)
