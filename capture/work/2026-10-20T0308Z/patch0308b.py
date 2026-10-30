s=open('build_capture.py').read()
a="skip_nsfw |= {'2112211153480831163'}  # 0200Z"
assert a in s
s=s.replace(a,"skip_nsfw |= {'2112348898379346131','2068937071277089226'}  # 0308Z: likely paid (FollowZeroChill, 106 followers, link-only video: 9 likes and 0 replies on 804k views; allreactvids keyword-stuffed reaction clip: 0 replies on 1.1M views)\n"+a,1)
b="EXTRA_PRIVATE |= {'2079268143520780461'}  # 0004Z"
assert b in s
s=s.replace(b,"EXTRA_PRIVATE |= {'2112085314256720355','2111918884857020567'}  # 0308Z: TrendingEx post naming two Bangladeshi nationals reported executed in Saudi Arabia (private people); AryanBundles post mocking an unnamed man in photos (private person)\nDESK_OVERRIDE_RUN.update({'2112085314256720355':'world','2111804709074043369':'world','2112214366737010864':'world','2109559502840508514':'entertainment','2111942044222419453':'entertainment','2111918884857020567':'internet','2112102322507534767':'offbeat','2112323120380129562':'politics','2112286669508694289':'politics','2112256359022362891':'politics','2112227716183277635':'business','2112211740884975910':'business'})  # 0308Z desk fixes: Saudi executions, Paris photos and Kim Jong Un rumour to world; Allu Arjun film update and Little Witch Academia post to entertainment; Goku-shirt man post to internet; survival clip to offbeat; Trump Accounts request posts to politics and business\n"+b,1)
open('build_capture.py','w').write(s); print('ok')
