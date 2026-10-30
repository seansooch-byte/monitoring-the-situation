s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2096757842435084301','2040357643416375371','2109928937975648440','2110883752306151819'}  # 0703Z: likely promoted A24 trailer-announcement post from Sept 7 (79K likes, 1.6K replies on 60M views); likely paid (1,399 likes, 30 replies on 7.2M views); sexual caption; likely paid Kick brand promo (928 likes on 808K views)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2110768423282069760','2110944984408989792','2111093562452639905','2111171825527103889',")
open('build_capture.py','w').write(s); print('ok')
