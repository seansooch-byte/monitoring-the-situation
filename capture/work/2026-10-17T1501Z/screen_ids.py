import sys,glob,json; sys.path.insert(0,'.')
from loadx import load_x,left
from collections import Counter
files=[f for f in sorted(glob.glob('*.txt')) if not f.endswith('_q.txt') and f.split('.')[0].startswith(('watch','sensor_','quote_','repost_','trend_','desk_','screen')) and not f.startswith(('watch_ids','desk_q','sensor_q','x_q','watch_json','screen_batch','screen_ids'))]
have={}; refs=Counter()
for f in files:
  j=load_x(f)
  inc=j.get('includes') or {}
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and 'id' in t and t.get('public_metrics'): have[t['id']]=t
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if not isinstance(t,dict): continue
    for rt in t.get('referenced_tweets') or []: refs[rt['id']]+=1
    for m in (t.get('attachments') or {}).get('media_source_tweet_id') or []: refs[m]+=1
excl=set(json.load(open('exclude_ids.json')))
need=[i for i,c in refs.most_common() if i not in have and i not in excl]
print(len(files),len(have),len(refs),'need',len(need))
json.dump(dict(refs.most_common()),open('ref_counts.json','w'))
for k in range(0,min(len(need),200),100):
  open(f'screen_batch_{k//100}_ids.txt','w').write(','.join(need[k:k+100]))
  print(f'== {k//100}'); print(','.join(need[k:k+100]))
for f in files[-7:]: print(f,left(f))
