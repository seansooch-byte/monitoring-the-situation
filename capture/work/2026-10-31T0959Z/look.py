import sys,json,glob;sys.path.insert(0,'.')
from loadx import load_x
T={};U={};M={};S={}
for f in glob.glob('*.txt'):
  if f.endswith('_q.txt') or f.startswith('trends_') or f.startswith('volume_'): continue
  try: j=load_x(f)
  except Exception: continue
  if not isinstance(j,dict): continue
  inc=j.get('includes') or {}
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and 'id' in t: T.setdefault(t['id'],t); S.setdefault(t['id'],set()).add(f)
  for u in inc.get('users') or []: U[u['id']]=u
  for m in inc.get('media') or []: M[m['media_key']]=m
for i in sys.argv[1:]:
  t=T.get(i); 
  if not t: print(i,'NOT FOUND'); continue
  u=U.get(t.get('author_id'),{})
  print('==',i,u.get('username'),u.get('public_metrics',{}).get('followers_count'),u.get('verified_type'),'|',(u.get('description') or '')[:120].replace('\n',' '))
  print('  ',t.get('public_metrics'),t.get('created_at'),'sens',t.get('possibly_sensitive'),sorted(S[i])[:4])
  print('  ',(t.get('note_tweet',{}).get('text') or t.get('text'))[:400].replace('\n',' '))
  for r in t.get('referenced_tweets') or []: print('   ref',r)
  for k in (t.get('attachments') or {}).get('media_keys') or []: m=M.get(k,{}); print('   media',m.get('type'),m.get('alt_text'),m.get('url') or m.get('preview_image_url'))
