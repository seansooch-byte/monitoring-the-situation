s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'1868856351373639713','2070884053935350077'}  # 1906Z: likely paid (hellostarr_, 718 followers: 6,769 likes and 6 replies on 6.3M views); likely paid (ced_jayy: 411 likes and 140 replies on 2.1M views)\nskipped_nsfw = []\n")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2111072036089131094':'sports','1604764832754171905':'music','2110462362343866599':'sports','2111506579128480242':'sports','2071357848861147244':None,\n")
open('build_capture.py','w').write(s); print('ok')
