s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2105999488515186699','2099688684295745806','2110764910011384002','2111224226808311906','2110819145118007485','2111026544856494158','2110583372460458444','2111135963116085559','2111073230907670715'}  # 0600Z: thirst-account gym clip (sexualised framing); post naming an adult performer; likely paid (7,624 likes, 3 replies on 1.3M views); free-pizza giveaway promo; likely paid (171 followers, 167 likes on 877K views); likely paid Netflix India promo (26 replies on 962K views); likely paid Hulu episode promo; likely paid (19 replies on 897K views); post naming a five-year-old shooting victim\nskipped_nsfw = []\n")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2110402979681771963':None,'2111045153565626645':'gaming','2111162211318067638':'politics','2111189453880406301':'entertainment','2110903725116014610':'tech','2110441463599542506':'politics','2110398367201145273':'politics','2110803056606720218':'internet','2111058554878853430':'sports','2111276969690038485':'politics',\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2110402979681771963',")
open('build_capture.py','w').write(s); print('ok')
