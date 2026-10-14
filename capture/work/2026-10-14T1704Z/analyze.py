import json,re,glob,os
from collections import Counter
from datetime import datetime,timezone
W='/workspace/monitoring-the-situation/capture/work/2026-10-14T1704Z'
NOW=datetime.now(timezone.utc)
def load_x(p):
  raw=open(p).read()
  if 'X reads left' in raw: raw=raw[:raw.rfind('X reads left')]
  raw=re.sub(r'</?cursor_untrusted_data[^>]*>','',raw)
  return json.loads(raw[raw.find('{'):raw.rfind('}')+1])
tw={};users={};pointed=Counter();src={}
reads={}
for p in sorted(glob.glob(W+'/*.json')):
  n=os.path.basename(p)
  if n.startswith('trends') or n in('build_meta.json','ref_counts.json','tally_origins.json','missing_refs.json','exclude_ids.json','desk_override.json','media_desc.json'): continue
  d=load_x(p)
  m=re.findall(r'(\d+) of 1000 today',open(p).read()); reads[n]=m[-1] if m else None
  for u in (d.get('includes') or {}).get('users') or []: users[u['id']]=u
  allt=(d.get('data') or [])+((d.get('includes') or {}).get('tweets') or [])
  for t in allt:
    tw.setdefault(t['id'],t)
    src.setdefault(t['id'],set()).add(n)
  for t in d.get('data') or []:
    for r in t.get('referenced_tweets') or []:
      pointed[r['id']]+=1
    for ms in set((t.get('attachments') or {}).get('media_source_tweet_id') or []):
      if ms!=t['id']: pointed[ms]+=1
missing=set()
for t in list(tw.values()):
  for r in t.get('referenced_tweets') or []:
    if r['id'] not in tw: missing.add(r['id'])
  for ms in set((t.get('attachments') or {}).get('media_source_tweet_id') or []):
    if ms not in tw: missing.add(ms)
print('reads',reads)
print('tweets',len(tw),'missing refs',len(missing))
def age(t):
  c=datetime.fromisoformat(t['created_at'].replace('Z','+00:00'));return (NOW-c).total_seconds()/3600
cands=[]
for i,t in tw.items():
  if (t.get('text') or '').startswith('RT @'): continue
  pm=t.get('public_metrics') or {}
  v=pm.get('impression_count') or 0; l=pm.get('like_count') or 0
  a=age(t)
  cands.append((v,l,a,i,(users.get(t.get('author_id')) or {}).get('username'),(t.get('text') or '')[:90].replace('\n',' '),sorted(src[i])[0], pointed.get(i,0)))
cands.sort(reverse=True)
for c in cands[:90]:
  print('%10d %7d %6.1fh %s @%s [%s] p%d | %s'%(c[0],c[1],c[2],c[3],c[4],c[6],c[7],c[5]))
json.dump(sorted(missing),open(W+'/missing_refs.json','w'))
json.dump(dict(pointed),open(W+'/ref_counts.json','w'))
