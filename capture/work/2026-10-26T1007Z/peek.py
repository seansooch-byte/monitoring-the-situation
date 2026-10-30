import sys,json;sys.path.insert(0,'.')
from loadx import load_x
for f in sys.argv[1:]:
  j=load_x(f); inc=j.get('includes') or {}
  users={u['id']:u['username'] for u in inc.get('users') or []}
  tw={t['id']:t for t in (inc.get('tweets') or [])}
  print('=====',f)
  seen=set()
  for t in j.get('data') or []:
    o=t
    for r in t.get('referenced_tweets') or []:
      if r['type'] in('retweeted','quoted') and r['id'] in tw: o=tw[r['id']]
    if o['id'] in seen: continue
    seen.add(o['id'])
    pm=o.get('public_metrics',{})
    print(o['id'],users.get(o.get('author_id')),pm.get('impression_count'),pm.get('like_count'),o.get('created_at','')[:16],(o.get('note_tweet',{}).get('text') or o.get('text',''))[:110].replace('\n',' '))
