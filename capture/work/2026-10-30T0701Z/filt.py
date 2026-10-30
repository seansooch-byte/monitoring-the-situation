import re,json,sys
s=open('build_capture.py').read()
ex=set(json.load(open('exclude_ids.json')))
for l in s.split('\n'):
  if l.lstrip().startswith('skip_nsfw |='): ex|=set(re.findall(r"'(\d{15,20})'",l.split('#')[0]))
refs=json.load(open('ref_counts.json'))
import sys; sys.path.insert(0,'.')
from loadx import load_x
import glob
have=set()
for f in glob.glob('*.txt'):
  if f.endswith('_q.txt') or f.startswith(('watch_ids','screen_batch','known','private','pulse','story','watch_json','reread','added','requests','started','reads_')): continue
  try: j=load_x(f)
  except Exception: continue
  inc=j.get('includes') or {}
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and t.get('public_metrics'): have.add(t['id'])
need=[i for i in refs if i not in have and i not in ex]
print(len(need))
for k in range(0,len(need),100): print('==',k//100); print(','.join(need[k:k+100]))
