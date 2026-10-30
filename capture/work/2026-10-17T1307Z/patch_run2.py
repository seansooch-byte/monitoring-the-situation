s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2111047798908948837','2050617645821567122','2102939077293293814','1842995992003850486'}  # 1307Z: paid hotel-furniture ad (31 likes on 4.2M views); likely paid copy of the yoga-fall video (335 likes and 10 replies on 2.2M views); likely paid (10,272 likes and 4 replies on 2.0M views); likely promoted 2024 question post (952 likes on 44.6M views)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2111083403701338434','2110838225925189879','2111130582855962999',")
open('build_capture.py','w').write(s); print('ok')
