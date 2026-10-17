s=open('build_capture.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60]); s=s.replace(a,b)
rep("    from_trend = any(s.startswith('trend.') for s in srcs)","    from_trend = any(s.startswith('trend.') and not s.endswith('.media') for s in srcs)  # 0703Z: media-source posts reached through a trend stream are screened on the global floor, not taken as trend context")
rep("    _tn = sorted({str(x).replace('.media','') for x in row[6] if str(x).startswith('trend.')})","    _tn = sorted({str(x) for x in row[6] if str(x).startswith('trend.') and not str(x).endswith('.media')})")
rep("        if s.startswith('trend.'):\n            trend_posts[","        if s.startswith('trend.') and not s.endswith('.media'):\n            trend_posts[")
open('build_capture.py','w').write(s); print('ok')
