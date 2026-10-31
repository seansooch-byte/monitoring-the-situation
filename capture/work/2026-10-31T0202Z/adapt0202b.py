s=open('build_capture.py').read()
a="DESK_OVERRIDE_RUN.update({_x:'entertainment' for _x in ['2116059923759133013']+CTXR+CTXQ})  # 0202Z: Mangaaposts anime clip is entertainment"
assert s.count(a)==1
s=s.replace(a,a+"\nDESK_OVERRIDE_RUN.update({'2116114302855708700':'sports','2116012548570992893':'sports','2115992053515727191':'world'})  # 0202Z: desk fixes: Kevin Garnett NBA story and Christian Watson clip are sports, not gaming/medicine; the unverified Netanyahu election claim is world, not ai")
b="EXTRA_PRIVATE |= {'2115965600069452153','2116022244954771889'}  # 0102Z:"
assert s.count(b)==1
s=s.replace(b,"EXTRA_PRIVATE |= {'2115359902617256247'}  # 0202Z: mmahokei2 video of a woman fainting (who she is is not given; may be a private person)\n"+b)
open('build_capture.py','w').write(s); print('ok')
