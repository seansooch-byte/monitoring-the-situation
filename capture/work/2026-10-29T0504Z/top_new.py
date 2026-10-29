import sys,glob,json;sys.path.insert(0,'.');from loadx import load_x
known=set(open('known_posts.txt').read().split()); ex=set(json.load(open('exclude_ids.json')))
posts={};users={}
for f in glob.glob('*.txt'):
  if f.endswith('_q.txt') or not f.startswith(('desk_','sensor_','trend_','quote_','repost_','screen','watch')) or f.startswith(('watch_ids','watch_json')): continue
  try: j=load_x(f)
  except Exception as e: print('bad',f); continue
  inc=j.get('includes') or {}
  for u in inc.get('users') or []: users[u['id']]=u['username']
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and t.get('public_metrics'): posts[t['id']]=t
new=[t for i,t in posts.items() if i not in known and i not in ex and t['created_at']>'2026-10-28T01' and not any(r['type']=='retweeted' for r in t.get('referenced_tweets') or [])]
new.sort(key=lambda t:-t['public_metrics']['impression_count'])
for t in new[:int(sys.argv[1]) if len(sys.argv)>1 else 25]: print(t['id'],users.get(t['author_id']),t['public_metrics']['impression_count'],t['public_metrics']['like_count'],t['created_at'][:16],t.get('possibly_sensitive'),(t.get('note_tweet',{}).get('text') or t['text'])[:100].replace('\n',' '))
