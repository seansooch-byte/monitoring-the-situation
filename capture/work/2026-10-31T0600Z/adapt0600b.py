s=open('build_capture.py').read()
a=s.index("DESK_OVERRIDE_RUN.update({'2116121773469061256':'music'"); b=s.index("\n",a)
add = """
skip_nsfw |= {'2116152635917246821'}  # 0600Z: makidogang 'Solgaleo in grave' hypnosis animation promo ('Full movie by P-site'), likely sexual fan content; left out
EXTRA_PRIVATE |= {'2116281350219076025'}  # 0600Z: gapjilreborn clip of an unnamed man stuck in a tennis racket (private person; when in doubt, flag)
DESK_OVERRIDE_RUN.update({'2116281350219076025':'offbeat','2114061035804000612':'entertainment','2108668953023410555':'gaming','2116287873918140737':'tech','2115890118561288264':'internet','2063626504773202321':'sports','2116294330638074103':'politics'})  # 0600Z desk fixes: tennis-racket clip is offbeat; Georgie & Mandy scene is entertainment, not sports; PlayStation podcast is gaming; elonmusk Tesla self-driving clip is tech; Atrioc deepfake post is internet; EnjoyBBall birthday-shooting post is sports; 'Voted in Texas for Paxton' is politics"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
