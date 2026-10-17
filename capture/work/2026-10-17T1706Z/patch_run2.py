s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skipped_nsfw = []\n","skip_nsfw |= {'2104571188424913143','2096945421310718384','2032613478792323531','2036346370458788269'}  # 1600Z: likely paid (Chinasa7v32 'Movie recommendation': 26 likes and 4 replies on 3.7M views); crypto-trading ad (Delta_Exchange: 497 likes and 16 replies on 1.4M views); likely paid (dykemedla Natalie Nunn reaction clip: 2,840 likes and 8 replies on 3.8M views); engagement-bait photo (Jesii_ca_M, four women labelled A to D, 'who looks perfect?')\nskipped_nsfw = []\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2111071770010673497','2069666093640417401','2040888913531662627',")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2110960095597142265':None,'2111209208012210409':'ai','2111131677351432197':'tech','2111087026330374516':'entertainment','2111094888033132859':'gaming','2111449904984056138':'world','2111462671878918556':'music','2110752265846091881':'politics','2111008131501170884':'life','2110703535423922663':'entertainment','2111136203496116704':'internet','2110744206952075514':'music','2111071770010673497':'world',\n")
open('build_capture.py','w').write(s); print('ok')
