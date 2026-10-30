s=open('build_capture.py').read()
a="SEX_WORDS = ("
assert s.count(a)==1
s=s.replace(a,"skip_nsfw |= {'2111897013847552081'}  # 0106Z: likely promoted (pahrduve link-only video: 4 likes on 1.03M views, as the pahrduve videos left out in 0006Z)\n"+a,1)
a="DESK_OVERRIDE_RUN.update({'2111092458109231403':'internet'"
assert s.count(a)==1
i=s.index(a); j=s.index('\n',i)
s=s[:j+1]+"DESK_OVERRIDE_RUN.update({'2111871188381430023':'life','2111593216784916859':'world'})  # 0106Z: inherited-house story is life; Ted Cruz Paris post is world, as the other Paris posts\n"+s[j+1:]
open('build_capture.py','w').write(s); print('ok')
