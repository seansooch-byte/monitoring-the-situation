s=open('build_capture.py').read()
a="skip_nsfw |= {'2111117490612736161','2071910961682772388'"
assert a in s
s=s.replace(a,"skip_nsfw |= {'2034391848064889041','2112189047607337405'}  # 0906Z: posts alleging sexual abuse of a minor (PamphletsY March clip and GPC_Globall post of the same Rep. Goldman remark), left out under the minors rule as in 0004Z\n"+a,1)
b="EXTRA_PRIVATE |= {'2111684930644390323','2112041190707388581'}  # 0801Z"
assert b in s
s=s.replace(b,"DESK_OVERRIDE_RUN.update({'2111933887622582513':'entertainment','2111940251526762889':'gaming','2112276675996024870':'internet','2112160305635897609':'sports','2112116545295986960':'tech','2111881742034608303':'entertainment','2112214060192190692':'music','2112323704822636895':'music','2112190389943722435':'internet','2112246067739984319':'justice','2112361800335565107':'life'})  # 0906Z desk fixes: South Park clip and Premalu 2 post to entertainment; game-piracy post to gaming; conversation and win memes to internet; figure skating post to sports; casino fish-tank hack to tech; Tim McGraw and carterefe music video to music; Atlanta Technical College shooting to justice; Indonesian compliment story to life\n"+b,1)
open('build_capture.py','w').write(s); print('ok')
