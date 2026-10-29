import sys,json
from loadx import load_x,left
for i in sys.argv[1:]:
  d=load_x(f'watch{i}.txt'); want=open(f'watch_ids_{i}.txt').read().strip().split(',')
  got={p['id'] for p in d.get('data',[])}
  errs={e.get('value') or e.get('resource_id'):e.get('title') for e in d.get('errors',[])}
  unk=[x for x in got|set(errs) if x not in want]
  print(i,len(got),errs,'missing',[w for w in want if w not in got and w not in errs],'unexpected',unk,'left',left(f'watch{i}.txt'))
