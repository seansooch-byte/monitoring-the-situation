s=open('build_capture.py').read()
a=s.index("skip_nsfw |= {'2115731138249412793','2115902565376241837'}"); b=s.index("\n",a)
add = """
DESK_OVERRIDE_RUN.update({'2116046885559414996':'politics','2116043113747902737':'politics','2115821848873017777':'politics','2116035373361230325':'tech'})  # 0805Z desk fixes: elonmusk quotes of tyler 'vote Republican' and the Babylon Bee Minnesota turnout post, and as400495 voter-fraud reporting post, are politics; elonmusk Terafab post is tech (they came via the money sensor, which defaults to markets)
skip_nsfw |= {'2115748000123216353','2115979672651505837','2115597836259889310'}  # 0805Z: sexual: 12gee_man Riley Reid adult-film anecdote; Rjw6996 #AHS13 'sexy moments ... not a single cheek' clip (399 followers); carverfomo Blueface stream clip of women in cop costumes taking over the camera (video preview not returned, left out when in doubt)"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
