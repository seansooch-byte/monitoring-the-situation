s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2079893972512641218','2110966188943765965'}  # 1108Z: sexual text (old origin); likely promoted engagement-bait question (28 likes and 7 replies on 1.46M views)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2110400241317085592','2055340102935593423','2111099194878603366',")
open('build_capture.py','w').write(s); print('ok')
