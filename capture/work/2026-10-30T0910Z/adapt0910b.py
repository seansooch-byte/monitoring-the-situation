s=open('build_capture.py').read()
a=s.index("skip_nsfw |= {'2115748000123216353','2115979672651505837','2115597836259889310'}"); b=s.index("\n",a)
add = """
DESK_OVERRIDE_RUN.update({'2116077674364031247':'gaming'})  # 0910Z desk fix: Nintendo Japan sale-page post (lists NBA 2K27 among games) is gaming, not sports
EXTRA_PRIVATE |= {'2115909558757462435'}  # 0910Z: 0880elvis0880 reply to FabrizioRomano by a 564-follower account (non-public author of a viral reply)"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
