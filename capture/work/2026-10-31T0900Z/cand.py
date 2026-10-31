import sys,glob,json;sys.path.insert(0,'.');from loadx import load_x
known=set(open('known_posts.txt').read().split()); ex=set(json.load(open('exclude_ids.json')))
posts={};users={}
for f in glob.glob('*.txt'):
  if f.endswith('_q.txt') or not f.startswith(('desk_','sensor_','trend_','quote_','repost_','screen','watch')) or f.startswith(('watch_ids','watch_json','screen_batch')): continue
  j=load_x(f); inc=j.get('includes') or {}
  for u in inc.get('users') or []: users[u['id']]=u
  for t in (j.get('data') or [])+(inc.get('tweets') or []):
    if isinstance(t,dict) and t.get('public_metrics'): posts[t['id']]=t
new=[t for i,t in posts.items() if i not in known and i not in ex and t['created_at']>'2026-10-30T01' and not any(r['type']=='retweeted' for r in t.get('referenced_tweets') or [])]
new=[t for t in new if t['public_metrics']['impression_count']>=100000 or t['public_metrics']['like_count']>=2000]
new.sort(key=lambda t:-t['public_metrics']['impression_count'])
for t in new:
  u=users.get(t['author_id'],{}); pm=t['public_metrics']
  print(t['id'],u.get('username'),u.get('public_metrics',{}).get('followers_count'),pm['impression_count'],pm['like_count'],round(1000*pm['like_count']/max(pm['impression_count'],1),1),t['created_at'][5:16],t.get('possibly_sensitive'),(t.get('note_tweet',{}).get('text') or t['text'])[:90].replace('\n',' '))
print(len(new))
