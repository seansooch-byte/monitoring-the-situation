import sys,glob,json;sys.path.insert(0,'.')
from loadx import load_x
P={};U={};M={}
refby={}
for f in sorted(glob.glob('*.txt')):
  if f.endswith('_q.txt') or 'ids' in f or f in('reads_after.txt','extra_note.txt','known_posts.txt','private_ids.txt','pulse_ids.txt','story_ids.txt','requests_rev.txt','reread_ids.txt'): continue
  try: j=load_x(f)
  except Exception as e: continue
  inc=j.get('includes') or {}
  for u in inc.get('users') or []: U[u['id']]=u
  for m in inc.get('media') or []: M[m['media_key']]=m
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and 'id' in t:
      if t.get('text') and (i:=t['id']) not in P or (t.get('public_metrics') and not P[t['id']].get('public_metrics')): P[t['id']]=t
      for r in t.get('referenced_tweets') or []: refby.setdefault(r['id'],set()).add((t['id'],r['type'],f))
      for ms in (t.get('attachments') or {}).get('media_source_tweet_id') or []: refby.setdefault(ms,set()).add((t['id'],'media',f))
for i in sys.argv[1:]:
  t=P.get(i) or {}; u=U.get(t.get('author_id'),{})
  txt=(t.get('note_tweet') or {}).get('text') or t.get('text') or ''
  print('==',i,u.get('username'),u.get('public_metrics',{}).get('followers_count'),t.get('created_at'),t.get('public_metrics'),'refs',t.get('referenced_tweets'),'ms',(t.get('attachments') or {}).get('media_source_tweet_id'))
  print('  text:',txt[:500].replace('\n',' '))
  print('  refby:',sorted(refby.get(i,[]))[:6])
  for k in (t.get('attachments') or {}).get('media_keys') or []:
    m=M.get(k,{}); print('  media',m.get('type'),m.get('duration_ms'),m.get('preview_image_url') or m.get('url'), (m.get('alt_text') or '')[:100])
