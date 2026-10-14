import json,re,glob
def load_x(p):
  raw=open(p).read()
  if 'X reads left' in raw: raw=raw[:raw.rfind('X reads left')]
  raw=re.sub(r'</?cursor_untrusted_data[^>]*>','',raw)
  return json.loads(raw[raw.find('{'):raw.rfind('}')+1])
tw={}
docs={}
for n in sorted(glob.glob('*.json')):
  if n.startswith('trends') or n in ('missing_refs.json','ref_counts.json','exclude_ids.json','build_meta.json','desk_override.json','media_desc.json','build_meta.json'): continue
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
names={'Starlink':'trend_starlink.json','Dudus':'trend_dudus.json','Gold Glove':'trend_gold_glove.json','Happy Birthday Charlie':'trend_happy_birthday_charlie.json','Greenland':'trend_greenland.json'}
for name,f in names.items():
  c=set(origins(docs[f]))
  for i,t in tw.items():
    if name.lower() in (t.get('text') or '').lower() and not (t.get('text') or '').startswith('RT @'): c.add(i)
  top=sorted(c,key=lambda i:-views(i))[:3]
  key=name.lower().replace('#','').replace(' ','_')
  open(f'trend_{key}_top3.txt','w').write('\n'.join(top))
  print(name,[(i,views(i),(tw[i].get('text') or '')[:70].replace('\n',' ')) for i in top])
for g in ['news','money','science']:
  d=docs[f'sensors_{g}.json']; ids=[]
  for t in d.get('data') or []:
    refs=[x['id'] for x in t.get('referenced_tweets') or [] if x['type'] in ('retweeted','quoted')]
    if (t.get('text') or '').startswith('RT @') and refs: ids+=refs
    else: ids.append(t['id']); ids+=refs
    ms=(t.get('attachments') or {}).get('media_source_tweet_id') or []
    ids+=ms
  ids=sorted(dict.fromkeys(ids),key=lambda i:-views(i))
  open(f'sensor_{g}_top.txt','w').write('\n'.join(ids))
  print(g,[(i,views(i)) for i in ids[:6]])
