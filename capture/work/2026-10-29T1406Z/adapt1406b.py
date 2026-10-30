s=open('build_capture.py').read()
a="skip_nsfw |= {'2106939299849519434','2114736437782585850','2114601360544903466'}  # 1259Z"
assert s.count(a)==1
i=s.index(a); j=s.index('\n',i)+1
add=("skip_nsfw |= {'2113596029907939750','2102414260576076287','1893938998747205976'}  # 1406Z: graphic precaution (sxmmie_z 'Was this guy stabbing her?' video of a possible stabbing); likely paid (massivebrains00 Massive SEO ad copy; MeggieEliseVA 'officially sponsored' ZZZ animation)\n"
     "EXTRA_PRIVATE |= {'2114618787047608732'}  # 1406Z: OgbajiIfeanyi wedding post naming and showing a private bride (precaution)\n"
     "DESK_OVERRIDE_RUN.update({'2115611693078241734':'sports','2115802311997931713':'sports','2115802269329375574':'sports','2115802315378528356':'sports','2115314582659141981':'entertainment','2115549729790533982':'entertainment','2114618787047608732':'offbeat'})  # 1406Z desk fixes: MLS Suárez goal and the Cristiano Ballon d'Or reply/quotes to sports; Doctor Strange AI post and Chicago Fire clip to entertainment; Nigerian 'Jim Brown' wedding (not the football player) to offbeat\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s);print('ok')
