import json,re,glob
from collections import Counter
def load_x(p):
  raw=open(p).read()
  if 'X reads left' in raw: raw=raw[:raw.rfind('X reads left')]
  raw=re.sub(r'</?cursor_untrusted_data[^>]*>','',raw)
  return json.loads(raw[raw.find('{'):raw.rfind('}')+1])
tw={}; docs={}
skip=('missing_refs.json','ref_counts.json','exclude_ids.json','build_meta.json','desk_override.json','media_desc.json')
for n in sorted(glob.glob('*.json')):
  if n.startswith('trends') or n in skip: continue
  d=load_x(n); docs[n]=d
  for t in (d.get('data') or [])+((d.get('includes') or {}).get('tweets') or []): tw.setdefault(t['id'],t)
def views(i): return ((tw.get(i) or {}).get('public_metrics') or {}).get('impression_count') or 0
def origins(d, kinds=('retweeted','quoted')):
  out=[]
  for t in d.get('data') or []:
    for r in t.get('referenced_tweets') or []:
      if r['type'] in kinds: out.append(r['id'])
  return out
q=[]
for n in ['quote1.json','quote2.json','quote3.json']: q+=origins(docs[n],('quoted',))
r=origins(docs['repost.json'],('retweeted',))
open('quote_origins_all.txt','w').write('\n'.join(dict.fromkeys(q)))
open('repost_origins_all.txt','w').write('\n'.join(dict.fromkeys(r)))
print('quote origins',len(set(q)),'repost origins',len(set(r)))
names={'Endrick':'trend_endrick.json','Espi':'trend_espi.json','Starlink':'trend_starlink.json','Mourinho':'trend_mourinho.json','Semenyo':'trend_semenyo.json'}
for name,f in names.items():
  c=set(origins(docs[f]))
  for i,t in tw.items():
    if re.search(r'(?<![\w#])'+re.escape(name)+r'(?!\w)',(t.get('text') or ''),re.I) and not (t.get('text') or '').startswith('RT @'): c.add(i)
  top=sorted(c,key=lambda i:-views(i))[:3]
  key=name.lower().replace('#','').replace(' ','')
  open(f'trend_{key}_top3.txt','w').write('\n'.join(top))
  print(name,[(i,views(i),(tw[i].get('text') or '')[:90].replace('\n',' ')) for i in top])
for g in ['news','money','science']:
  d=docs[f'sensors_{g}.json']; ids=[]
  for t in d.get('data') or []:
    refs=[x['id'] for x in t.get('referenced_tweets') or [] if x['type'] in ('retweeted','quoted')]
    if (t.get('text') or '').startswith('RT @') and refs: ids+=refs
    else: ids.append(t['id']); ids+=refs
    ids+=(t.get('attachments') or {}).get('media_source_tweet_id') or []
  ids=sorted(dict.fromkeys(ids),key=lambda i:-views(i))
  open(f'sensor_{g}_top.txt','w').write('\n'.join(ids))
  print(g,[(i,views(i)) for i in ids[:6]])
# references: count pointers across all posts read, find unread
pointers=Counter(); unread=set()
for i,t in tw.items():
  refs=[x['id'] for x in t.get('referenced_tweets') or [] if x['type'] in ('retweeted','quoted','replied_to')]
  refs+=(t.get('attachments') or {}).get('media_source_tweet_id') or []
  for ref in set(refs):
    if ref==i: continue
    pointers[ref]+=1
    if ref not in tw: unread.add(ref)
json.dump(dict(pointers),open('ref_counts.json','w'))
excl=set(json.load(open('exclude_ids.json')))
reread=set(open('reread_ids.txt').read().split())
miss=[i for i in sorted(unread,key=lambda i:-pointers[i]) if i not in excl and i not in reread]
print('unread refs',len(miss),'top pointed',[(i,pointers[i]) for i in miss[:10]])
open('missing_refs.txt','w').write('\n'.join(miss))
print('pointed>=2 total',sum(1 for v in pointers.values() if v>=2))
