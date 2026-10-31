s=open('build_capture.py').read()
lines=s.split('\n')
mine=[l for l in lines if l.startswith("skip_nsfw |=") and ('suckle' in l or 'AiWithIqra' in l)]
assert len(mine)==2
lines=[l for l in lines if l not in mine]
i=[k for k,l in enumerate(lines) if l.startswith("skip_nsfw |= {'2113877508382744677'")][0]
lines[i+1:i+1]=mine
open('build_capture.py','w').write('\n'.join(lines)); print('ok')
