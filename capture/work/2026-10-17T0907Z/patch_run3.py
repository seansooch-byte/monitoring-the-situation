s=open('build_capture.py').read()
a="EXTRA_PRIVATE = {'2003125806332280920',"
assert s.count(a)==1
s=s.replace(a,"EXTRA_PRIVATE = {'2003125806332280920','2110781018214895722',")
open('build_capture.py','w').write(s); print('ok')
