import sys,glob,re
from loadx import load_x
b=open('build_capture.py').read()
P={}
for f in glob.glob('*.txt'):
  try: j=load_x(f)
  except Exception: continue
  if not isinstance(j,dict): continue
  inc=j.get('includes') or {}
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and 'id' in t: P.setdefault(t['id'],t)
for i in sys.argv[1:]:
  t=P.get(i); 
  if not t: print(i,'??');continue
  print('==',i,'sens',t.get('possibly_sensitive'),'flagged' if i in b else '', (t.get('note_tweet',{}) or {}).get('text') or t.get('text'))
