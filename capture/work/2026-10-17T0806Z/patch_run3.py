s=open('build_capture.py').read()
a="'2111116853762281500'}  # 0806Z:"
assert s.count(a)==1
s=s.replace(a,"'2111116853762281500','2110506851083374805','2111321307170107887','2111142484239896728'}  # 0806Z (also: 4-follower account with 4 likes and 0 replies on 434K views, likely paid; two posts whose media was not returned, a Blue Archive pool clip and a caption about a singer's partner, so they could not be screened):")
open('build_capture.py','w').write(s); print('ok')
