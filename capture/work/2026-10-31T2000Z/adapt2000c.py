s=open('build_capture.py').read()
i=s.index("skip_nsfw |= {'2116521901652840938','2116525727487230398'}  # 1909Z"); j=s.index("\n",i)+1
add = """skip_nsfw |= {'2116019534608126427','2116568095615856711'}  # 2000Z: sexual text (evilboyfren sex joke; AhhHaaaIWon quote of the context post about a child sexual abuse accusation)
skip_nsfw |= {'2097207090012152009','2114865710451278191','2116404078268109271'}  # 2000Z: likely paid (jobescape_ai 'Full Claude Course' promo, 5,191 likes on 17.5M views; CSVC2026 campaign ad, 185 followers, 442 likes on 1.03M views; janeswaan bare 'satisfying' video, 1,592 followers, 413 likes on 390K views)
DESK_OVERRIDE_RUN.update({_x:'politics' for _x in ['2116564175208018186']+CTXR+CTXQ})  # 2000Z: NICKIMINAJ post on a politician's anger and its context replies and quotes are politics
DESK_OVERRIDE_RUN.update({'2116213004337369370':'markets','1998453138857099684':'politics','2116534303735656486':'politics','2116448800156033501':'internet','2116370021467214201':'world','1960380408316530729':'politics','2116574052903251969':'gaming','2116551882219090231':'business','2116323594292842666':'internet'})  # 2000Z: desk fixes (gannwyck 2029 crash chart is markets; elonmusk immigration post and AlexToughTakes pride-flag post are politics; SimpPolice911 texting joke and rejectedhannah movie clip are internet; DariuszMatecki Poland tribunal post is world; disclosetv Trump Warp Speed clip is politics; SkyRaiderG7 Persona 1 leak post is gaming; elonmusk Tesla/SpaceX employee wealth post is business)
"""
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s); print('ok')
