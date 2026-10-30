import json,sys,statistics as st
from datetime import datetime
R='/workspace/monitoring-the-situation/capture/2026/10/17/'
files=sys.argv[1:]
first={}; created={}; last={}; fam={}
def t(s): return datetime.fromisoformat(s.replace('Z','+00:00'))
for f in files:
    d=json.load(open(R+f))
    stt=t(d['run']['started_at'])
    for p in d['posts']:
        created.setdefault(p['id'],p['created_at'])
        first.setdefault(p['id'],stt)
    for o in d['observations']:
        if o.get('views') is not None: last[o['id']]=o['views']
    kept={p['id'] for p in d['posts']}
    for s in d['sweeps']:
        k=s['id']
        g='viral.global' if k=='viral.global' else 'sensors' if k.startswith('sensors.') else 'rising' if k=='rising.global' else 'desk' if k.startswith('desk.') else None
        if g:
            for i in s['post_ids']:
                if i in kept: fam.setdefault(g,set()).add(i)
    for tr in d['trends']:
        for i in tr['post_ids']:
            if i in kept: fam.setdefault('trend',set()).add(i)
ids=list(first)
v=[last.get(i) for i in ids if last.get(i) is not None]
ages=[(first[i]-t(created[i])).total_seconds()/3600 for i in ids if created.get(i)]
def lm(s):
    x=[last[i] for i in s if last.get(i) is not None]
    return f'{max(x)} / {int(st.median(x))}' if x else 'n/a'
print(len(ids),sum(x>1e6 for x in v),sum(x>5e6 for x in v),sum(x>1e7 for x in v),max(v),int(st.median(v)),round(st.median(ages),2))
print('viral.global:',lm(fam.get('viral.global',[])),'; sensors:',lm(fam.get('sensors',[])),'; trend names:',lm(fam.get('trend',[])),'; rising:',lm(fam.get('rising',[])),'; desk:',lm(fam.get('desk',[])))
