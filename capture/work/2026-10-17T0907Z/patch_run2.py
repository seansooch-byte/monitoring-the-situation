s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("skip_nsfw |= {'2111207821769327038'}  # 0907Z: pornographic spam text in the Mónica stream\n",
    "skip_nsfw |= {'2111207821769327038','2111132564882678237','2089353664120889482','2107521708379054547','2091539538183082256','2086834114389303500'}  # 0907Z: pornographic spam text in the Mónica stream; sexual-innuendo clip naming an adult performer (Mónica stream); likely paid (608 likes and 1 reply on 18.9M views; 139 likes and 3 replies on 1.5M views); likely paid link-promo account Emeraldmovies3 (1,607 likes on 5.7M views; 3,320 likes on 1.8M views, both with outbound links)\n")
rep("EXTRA_PRIVATE = {","EXTRA_PRIVATE = {'2003125806332280920',")
rep("DESK_OVERRIDE = {\n","DESK_OVERRIDE = {\n    '2056835812772196578':'sports',\n")
open('build_capture.py','w').write(s); print('ok')
