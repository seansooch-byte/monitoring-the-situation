from loadx import *
import glob,json
from collections import Counter
tw={}
files=sorted(glob.glob('*.txt'))
skipf=('trends_','watch_ids','reread','requests_rev','post_fields','exp.','screen_ids','missing')
for f in files:
  if f.startswith(skipf): continue
  try: d=load_x(f)
  except Exception as e: print('skip',f,e); continue
  for t in (d.get('data') or [])+((d.get('includes') or {}).get('tweets') or [])+((d.get('includes') or {}).get('posts') or []): tw.setdefault(t['id'],t)
  print(f,len(d.get('data') or []),left(f))
pointers=Counter(); unread=set()
for i,t in tw.items():
  refs=[x['id'] for x in t.get('referenced_tweets') or []]
  refs+=(t.get('attachments') or {}).get('media_source_tweet_id') or []
  for r in set(refs):
    if r==i: continue
    pointers[r]+=1
    if r not in tw: unread.add(r)
miss=sorted(unread,key=lambda i:-pointers[i])
print('tweets',len(tw),'unread refs',len(miss),[(i,pointers[i]) for i in miss[:10]])
json.dump(dict(pointers),open('ref_counts.json','w'))
open('missing_refs.txt','w').write('\n'.join(miss))
