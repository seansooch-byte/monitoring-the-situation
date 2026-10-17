s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2111058578266013805'}  # 0959Z: likely promoted (Daily_Express tiger video: 44 likes and 10 replies on 1.1M views)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2109647068252004643','2111084566551363601',")
open('build_capture.py','w').write(s); print('ok')
