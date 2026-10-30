s=open('build_capture.py').read()
a=s.index("EXTRA_PRIVATE |= {'2115909558757462435'}"); b=s.index("\n",a)
add = """
DESK_OVERRIDE_RUN.update({'2116049311163122143':'politics','2115810408670048669':'politics','2115877985610011015':'politics','2115958112653852888':'politics','2116010037243937148':'politics','2115876323336057074':'politics','2115903476093849937':'internet','2115944930250310001':'offbeat','2115889565982716054':'offbeat'})  # 1004Z desk fixes: elonmusk voter-fraud post and his reposts of GabsClark5, FreeAndWhiskey, BrookeLRollins and america (Vance in Texas) are politics; EricLDaugh Trump-rally golfers post is politics, not sports; grok Tyson-lisp reply is internet; sciencegirl dogs and art posts are offbeat (all came via the science/news sensors)"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
