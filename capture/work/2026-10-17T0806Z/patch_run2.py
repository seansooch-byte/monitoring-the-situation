s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skip_nsfw |= {'2111365980270256455'}  # 0806Z: follower-boost spam in the #PFLChicago stream\n",
    "skip_nsfw |= {'2111365980270256455','2110022872689512536','1743247058801459706','2044907793929412626','2111116853762281500'}  # 0806Z: follower-boost spam in the #PFLChicago stream; likely paid Bollywood promo (71 replies, 9 quotes on 1.9M views); likely paid keyword-stuffed reaction clips (439 likes and 1 reply on 1.25M views; 21 likes and 0 replies on 499K views); media not returned, could not be screened (caption describes threats against women)\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2110702236632248608',")
open('build_capture.py','w').write(s); print('ok')
