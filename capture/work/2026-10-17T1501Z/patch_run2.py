s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'1723440854189183278','2111114854170013865','2109439700641481075','2110718810496147750'}  # 1501Z: sexual text (guess-what's-in-my-ass bait, old origin); sexual text (ArguablyAnna, 119,911 likes on 1.3M views); likely paid (Kartbro48 Knights of Guinevere clip: 13,934 likes and 18 replies on 664K views); likely paid (JaceValen TikTok repost of a dad and child: 711 likes on 1.35M views, 5,532 followers)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2111448883217694956','2008340922518344140','2111246923751452853','2111317409831481367',")
open('build_capture.py','w').write(s); print('ok')
