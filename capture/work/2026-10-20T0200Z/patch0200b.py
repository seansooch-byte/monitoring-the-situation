s=open('build_capture.py').read()
a="skip_nsfw |= {'2112334072492196126','2112332726116462711','2112322316256309442'}  # 0004Z"
assert a in s
s=s.replace(a,"skip_nsfw |= {'2112211153480831163'}  # 0200Z: GoatDeehere sexual text question about celebrities\n"+a,1)
b="EXTRA_PRIVATE |= {'2079268143520780461'}  # 0004Z"
assert b in s
s=s.replace(b,"EXTRA_PRIVATE |= {'2111894582413898065','2109652649763033227','2110482968766460280','2112281537475453336','2112200010146492818','2112262193496383617'}  # 0200Z: InsaneContext video of a pit bull attacking a toddler and a bystander; BVoltaire and posttmodern videos of a French police officer beaten by high school students; instablog9ja woman crying over a seat swap; mattvanswol Italian woman shouting at police; atrupar protester behind Vance (none public figures)\nDESK_OVERRIDE_RUN.update({'2109652649763033227':'world','2110482968766460280':'world','2112200010146492818':'world','2112196290645832062':'sports','1876753074091638809':'politics','2112262193496383617':'politics','2054805910636351522':'offbeat','2108251074637213843':'internet'})  # 0200Z: France and Italy police videos to world; Eagles medical staff joke to sports; Watters Canada clip and Vance protester to politics; cats chattering to offbeat; waist meme to internet\n"+b,1)
open('build_capture.py','w').write(s); print('ok')
