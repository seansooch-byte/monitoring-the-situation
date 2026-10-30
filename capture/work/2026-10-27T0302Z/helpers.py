import json,glob
REPO='/workspace/monitoring-the-situation'
prior={}; private=set()
for c in sorted(glob.glob(f'{REPO}/capture/2026/10/*/*.json')):
  d=json.load(open(c))
  for p in d['posts']:
    prior[p['id']]={'text':p.get('text'),'handle':(p.get('author') or {}).get('handle'),'flags':p.get('flags') or []}
    if 'private_individual' in (p.get('flags') or []): private.add(p['id'])
json.dump(prior,open('prior_posts.json','w'))
open('known_posts.txt','w').write('\n'.join(prior))
open('private_ids.txt','w').write('\n'.join(sorted(private)))
pc=json.load(open(f'{REPO}/pulse/current.json'))
pids=[]
for it in pc['items']:
  pids.append(it['id']); pids+=it.get('also') or []
open('pulse_ids.txt','w').write('\n'.join(dict.fromkeys(pids)))
sids=[]
for m in glob.glob(f'{REPO}/moments/**/*.json',recursive=True):
  d=json.load(open(m))
  for p in d.get('posts') or []:
    sids.append(p['id'] if isinstance(p,dict) else p)
open('story_ids.txt','w').write('\n'.join(sorted(set(sids))))
w=json.load(open(f'{REPO}/requests/watch.json'))['post_ids']
open('watch_json_ids.txt','w').write('\n'.join(w))
print(len(prior),len(private),len(set(pids)),len(set(sids)),len(w))
