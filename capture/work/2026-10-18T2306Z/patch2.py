s=open('build_capture.py').read()
a="SEX_WORDS = ("
assert s.count(a)==1
s=s.replace(a,"skip_nsfw |= {'2100349873094541761','2093272806125429196','2111495426339750185'}  # 2306Z: likely promoted (M7DMEN video: 740 likes and 3 replies on 6.7M views; 0xNextCore link-only post: 116 likes on 2.1M views; versivald link-only post: 121 likes and 0 replies on 1.67M views)\n"+a,1)
a="DESK_OVERRIDE_RUN.update({'2111921324247671171':'sports'"
assert s.count(a)==1
i=s.index(a); j=s.index('\n',i)
s=s[:j+1]+"DESK_OVERRIDE_RUN.update({'2111564441380864468':'sports','2111907213891792958':'entertainment','2111649350963417576':'entertainment','2111659833980284946':'entertainment','2111769606117363893':'internet','2110837502281986281':'internet','2111797185838813599':'justice','2111583733836857454':'politics','2111585327307710888':'world'})  # 2306Z: Hansi Flick quote is sports; Bigfoot hoax documentary, Hunter Schafer gala clip and RDJ Doom post are entertainment; burn-survivor and fic-writer posts are internet; Pilar Sanders court record is justice; Epstein reply is politics; Paris riots photo is world\n"+s[j+1:]
open('build_capture.py','w').write(s); print('ok')
