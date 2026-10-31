s=open('build_capture.py').read()
a="skip_nsfw |= {'2116168243333206264','2116336503647605183'}  # 1303Z"
assert s.count(a)==1
s=s.replace(a,"skip_nsfw |= {'2115670530359521388'}  # 1400Z: sexual (Uber story post)\n"+a)
a="EXTRA_PRIVATE |= {'2116343018777448539'}  # 1303Z"
assert s.count(a)==1
s=s.replace(a,"EXTRA_PRIVATE |= {'2116281350219076025','2116251139792634111','2116197708209799251'}  # 1400Z: video of a man stuck in a tennis racket; photo of people in homemade Halloween costumes; unnamed college student in a Joshua Haymes campus video (none public figures)\nDESK_OVERRIDE_RUN.update({'1752815271692116273':'music','2115850437244944478':'world','2116405414921384099':'tech','2115415755109937276':'tech'})  # 1400Z: Katy Perry video is music; Spain train collision survivor is world; X multi-account switching and Tesla self-driving are tech\n"+a)
open('build_capture.py','w').write(s)
