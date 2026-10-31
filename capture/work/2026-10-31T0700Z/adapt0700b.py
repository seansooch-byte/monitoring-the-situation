s=open('build_capture.py').read()
a=s.index("DESK_OVERRIDE_RUN.update({'2116281350219076025':'offbeat'"); b=s.index("\n",a)
add = """
DESK_OVERRIDE_RUN.update({'2116343266081640792':'justice','2116410020879274006':'justice','2116418160299839892':'science','2116364549569843512':'internet','2116385675381703063':'music'})  # 0700Z desk fixes: Florida sex-crimes sting arrests (Disney workers) is justice; Fairfield, California mall shooting is justice; NASA restoring contact with Voyager 1 is science; streamer RaKai's Halloween maid costume is internet; WILLOW's birthday post is music"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
