s=open('build_capture.py').read()
a="SEX_WORDS = ("
assert s.count(a)==1
s=s.replace(a,"skip_nsfw |= {'2110463946851303621','2111492207655948756','2111677004516905318','2111341625050013904','2111906181199630763'}  # 2203Z: sexual subject (welmnop Corinna Kopf dress clip); private teenager filmed bathing from a bucket, mocked as how South Africans bathe (Invaluablemoi video and the TundeOkafor1 quote of it); media not returned, could not be screened (BugZapper231 'I fixed it' reply); sexual-word joke (MLFootball Jahdae Walker ejection post)\n"+a,1)
a="DESK_OVERRIDE_RUN.update({'2111917989562032173':'sports'"
assert s.count(a)==1
i=s.index(a); j=s.index('\n',i)
s=s[:j+1]+"DESK_OVERRIDE_RUN.update({'2111921324247671171':'sports','2111821497434046875':'entertainment','1616763196940980228':'sports','2000921779997696064':'entertainment'})  # 2203Z: NFL Jalen Ramsey 'calls game' is sports; Game of Thrones quote is entertainment; Skip Bayless clip is sports; mimiscatalog music-video clip is entertainment\n"+s[j+1:]
a="EXTRA_PRIVATE = {"
i=s.index(a); j=s.index('\n',i)
s=s[:j+1]+"EXTRA_PRIVATE |= {'1790425730653863945'}  # 2203Z: poptime clip mocking a man's face after cosmetic procedures\n"+s[j+1:]
open('build_capture.py','w').write(s); print('ok')
