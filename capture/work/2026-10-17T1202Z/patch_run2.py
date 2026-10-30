s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2109993106494112203'}  # 1202Z: likely paid (A2OLITE_PICS chart-update video: 738 likes and 4 replies on 1.6M views)\nskipped_nsfw = []\n")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2111148091378409488':'tech','2111297643754275002':'world','2015835655012508016':'world','1993051980982632828':'politics','2110694702747934965':'sports','2110739170041991379':'sports','2110639247744975208':'music','2111354746548433173':'tech','2111354696854114702':'tech','2110805296662614448':'world','2110536137961771506':'world','2111081480822940046':'entertainment','2111000798972846279':'entertainment',\n")
open('build_capture.py','w').write(s); print('ok')
