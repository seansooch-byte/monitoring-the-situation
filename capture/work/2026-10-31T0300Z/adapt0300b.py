s=open('build_capture.py').read()
a="skip_nsfw = set(json.load(open(f'{W}/exclude_ids.json')))\n"
assert s.count(a)==1
s=s.replace(a,a+"skip_nsfw |= {'2113877508382744677','2115607352137437370'}  # 0300Z: sexual (HIZZYJOE06 clip framed on a woman's backside; StepbackMelo Gobert/Magic Johnson sex joke)\n")
b="EXTRA_PRIVATE |= {'2115359902617256247'}  # 0202Z:"
assert s.count(b)==1
s=s.replace(b,"EXTRA_PRIVATE |= {'2116339657151811806','2116340976817959323'}  # 0300Z: BrickCenter_ and TheNBACentel crude jokes about the female referee in the Knicks game (unnamed; in doubt whether a public figure)\n"+b)
open('build_capture.py','w').write(s); print('ok')
