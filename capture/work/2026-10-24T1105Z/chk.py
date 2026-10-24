import sys,re; sys.path.insert(0,'.')
from loadx import load_x
for i in sys.argv[1:]:
  j=load_x(f'watch{i}.txt'); req=open(f'watch_ids_{i}.txt').read().strip().split(',')
  got={t['id'] for t in j.get('data') or []}; err={str(e.get('resource_id') or e.get('value')):e.get('title') for e in j.get('errors') or [] if e.get('parameter')=='ids' or 'resource_id' in e}
  miss=[x for x in req if x not in got]
  print(i,len(req),'got',len(got),'missing',[(m,err.get(m)) for m in miss], 'extra',[x for x in got if x not in req])
  print(re.findall(r'X reads left.*',open(f'watch{i}.txt').read())[-1:])
