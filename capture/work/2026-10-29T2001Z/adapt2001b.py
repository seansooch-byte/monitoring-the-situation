s=open('build_capture.py').read()
a="skip_nsfw = set(json.load(open(f'{W}/exclude_ids.json')))\n"
assert s.count(a)==1
s=s.replace(a,a+"skip_nsfw |= {'2115610206881169877','2115796777546953166'}  # 2001Z: sexual text (MLFootball Charles Haley locker-room claim; CenobiteAQ claim about a 16-year-old)\n")
a="DESK_OVERRIDE_RUN.update({'2115893413233016885':'entertainment'"
i=s.index(a); j=s.index("\n",i)+1
s=s[:j]+"DESK_OVERRIDE_RUN.update({'2115607373448610186':'gaming','2115630283211116631':'entertainment','2115848262481768576':'entertainment','2115805894336536741':'gaming','2115657810205974849':'politics'})  # 2001Z desk fixes: Mario Kart Tour apk is gaming; Spider-Man deleted scene and Chris Pratt are entertainment; The Duskbloods delay is gaming; Medicare / 32-hour week post is politics\n"+s[j:]
open('build_capture.py','w').write(s);print('ok')
