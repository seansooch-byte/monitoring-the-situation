s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2111295582895808806','2095686426306269242'}  # 1403Z: sexualised ring-walk video (bikini, Kick event); likely paid (28,098 likes and 38 replies on 6.7M views, 1,302 followers)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2111227821074845951','2109855328175317022','2111186315215560982',")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2111375640717033777':'ai','2111142161584628060':'ai','2111080152197476739':'gaming','2110803630022422950':'entertainment','2110349551022248244':'gaming','2111295582895808806':'internet','2111207677527310645':'ideas','2111360445642596678':'tech','2110977536897528137':'music','1895010422689866009':'entertainment','2111227821074845951':'life','2111091095258169786':'entertainment','2110924190362595396':'internet','2110796301420159124':'politics','2074167715460165757':'ai','2110752082399555799':'politics',\n")
open('build_capture.py','w').write(s); print('ok')
