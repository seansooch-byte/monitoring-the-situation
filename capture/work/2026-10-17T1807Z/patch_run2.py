s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2097000940230324589','2111189343826251874','2110600760459452670','2106591559252660621','2111497864559943944','2111225205053919390'}  # 1807Z: likely paid (wdtalwutdo Portuguese celebrity-moment question: 1,941 likes on 112M views); likely paid (NikhatPraw70799 'watch till the end' clip: 9,887 likes on 19.2M views); likely paid (chalkalaana question: 282 likes and 20 replies on 11.4M views); likely paid (THEOVOSZALEGACY pineapple clip: 273 likes on 3.4M views); likely paid (MediaPLi2, 192 followers, link-only video: 255 likes and 8 replies on 2.9M views); sexual text (Will442232)\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2111210261197533605',")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2111037738879218043':'life','2099543565777195438':'music','2109271552378220789':'tech','2109116746753880192':'tech','2110635620330811758':'life','2111328130069889351':'life','2111076953382150189':'politics','2111319909594718624':'entertainment','2110862266593677675':'world','2111027214011519094':'world',\n")
open('build_capture.py','w').write(s); print('ok')
