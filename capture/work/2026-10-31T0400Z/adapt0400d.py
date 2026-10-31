s=open('build_capture.py').read()
a="skip_nsfw |= {'2116175894318371010'}  # 0400Z: sexual text (santosvenganza 'suckle that baby dick' quote post)"
assert s.count(a)==1
s=s.replace(a,"skip_nsfw |= {'2116175894318371010','2113841553311707617'}  # 0400Z: sexual text (santosvenganza 'suckle that baby dick' quote post); sexual AI-girlfriend promo, likely paid (BrokenHeartGifs 'Create your perfect AI girlfriend—sexy' with a sign-up link)")
b="DESK_OVERRIDE_RUN.update({'2116134803770864023':'markets',"
assert s.count(b)==1
s=s.replace(b,"EXTRA_PRIVATE |= {'2115879591206174852'}  # 0400Z: nypost story on an Instagram prank on a grocery vendor (private person)\nDESK_OVERRIDE_RUN.update({'2116157255171150273':'politics','2115879591206174852':'offbeat'})  # 0400Z: WhiteHouse fraud Halloween video is politics; nypost grocery-vendor prank fundraiser is offbeat\n"+b)
open('build_capture.py','w').write(s);print('ok')
