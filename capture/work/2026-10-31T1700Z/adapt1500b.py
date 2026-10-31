s=open('build_capture.py').read()
a="DESK_OVERRIDE_RUN.update({'1752815271692116273':'music'"
i=s.index(a); j=s.index("\n",i)+1
s=s[:j]+"""EXTRA_PRIVATE |= {'2116281888868577778','2094806325637046319','2116180636826567075'}  # 1500Z: srkntnyldz clip of an unnamed woman punched by a stranger in Canada; nujhayhne_ and finegirlveeee reaction clips of unnamed people (none public figures)
DESK_OVERRIDE_RUN.update({'2116534734763458792':'sports','2114644678461288828':'music','2116379802655740322':'sports','2114380123864469742':'sports','2112968708058501406':'sports','1803848427844845579':'sports','2116183357310788036':'music','2116498894397780218':'entertainment','2116076783984685158':'entertainment','2116235812547277043':'life','2096230981002748041':'offbeat'})  # 1500Z: Fabrizio Romano Man United run is sports; ILLIT 'you're under arrest' is music; Curry/Luka and Man United jokes and Neal Maupay are sports; TREASURE teaser is music; Marvel drone show and Rajkumar posts are entertainment; parenting post is life; flatmate beer clip is offbeat
"""+s[j:]
a="skip_nsfw |= {'2115670530359521388'}  # 1400Z: sexual (Uber story post)\n"
assert a in s
s=s.replace(a,a+"skip_nsfw |= {'2116343317600329969'}  # 1500Z: sexual (hentaihavenx)\n")
open('build_capture.py','w').write(s);print('ok')
