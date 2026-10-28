p='build_capture.py'; s=open(p).read()
a="skip_nsfw |= {'2115346310043713979'}  # 1904Z: sexual (speedgump explicit post about minions)\n"
assert s.count(a)==1
s=s.replace(a,a+"""skip_nsfw |= {'1955618802609029363','2115221740393497044'}  # 2004Z: FightCent fight video captioned 'ends up dead' (footage of a death, Aug 2025 origin); Nino_Billz sexual text about Doja Cat
skip_nsfw |= {'2114918487089192967','2115323302986084405','2114788232042807740'}  # 2004Z: likely paid (TiaraSmith1989, 142 followers: 256 likes and 0 replies on 1.54M views; Rabi_musaa 'greatest movie of all time' clip, 3,150 followers: 2,401 likes and 60 replies on 683K views); likely promoted (Substack 'Tap your state' election guide: 351 likes on 575K views)
DESK_OVERRIDE_RUN.update({'2115423937299697713':'music','2115318710907134325':'music','2115272829356982428':'world','2115481622862811285':'sports','2115477831081926848':'sports','2114932523507782083':'internet','2115064971167957343':'internet','2115124663018000791':'politics','2115137270282101183':'tech','2115433746748809491':'world','2115501119296463056':'tech','2115447957843821013':'tech'})  # 2004Z desk fixes: IVE Wonyoung/Bvlgari clip and K/DA Vogue China are music; Mbappe-Mao storm is world; Josh Downs trade posts are sports; mac n cheese photo and dating quip are internet; BillboardChris vote post is politics; FSD post and Tesla robotaxi/chipmunk posts are tech; Peter Obi post is world
""")
open(p,'w').write(s); print('ok')
