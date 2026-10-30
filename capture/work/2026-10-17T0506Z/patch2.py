s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2080387237829640397','2102428582127579567','2110486695275790551'}  # 0506Z: likely paid (952 likes, 31 replies on 9.3M views; wild dogs attacking a kudu); product ad video (window film, with a product disclaimer); likely paid movie promo (1,057 likes, 17 replies on 1.2M views)\nskipped_nsfw = []\n")
rep("        if str(_x)=='trend.YK Osiris': return 'music'\n","        if str(_x)=='trend.YK Osiris': return 'internet'\n")
rep("'trend.YK Osiris':'music',","'trend.YK Osiris':'internet',")
rep("for a,b in [('Mamu','Kessler'),('Kessler','Mamu'),","for a,b in [('Mamu','Kessler'),('Kessler','Mamu'),('YK Osiris','Deshae'),('Deshae','YK Osiris'),('YK Osiris','ash trevino'),('YK Osiris','Adin Ross'),")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2111075443176825233':'world','2110511855731159239':'tech','2110483188174946476':'tech','2110942875290935307':'disaster','2111279949336179053':'sports','2111262985360740675':'internet','2111304230162329908':'internet',\n")
old='YK Osiris is the rapper;'
new='YK Osiris (and Deshae) is the Deshae Frost vs YK Osiris fight at Adin Ross\'s Brand Risk boxing event, the same event as ash trevino and Adin Ross in 0403Z;'
assert s.count(old)==2; s=s.replace(old,new)
open('build_capture.py','w').write(s); print('ok')
