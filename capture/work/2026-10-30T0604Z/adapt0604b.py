s=open('build_capture.py').read()
a=s.index("DESK_OVERRIDE_RUN.update({'2115139787745095797'"); b=s.index("\n",a)
add = """
DESK_OVERRIDE_RUN.update({'2115878416423784939':'medicine','2116037732845957434':'politics','2115911629422342197':'politics'})  # 0604Z desk fixes: Neuralink speech-restoration study participant post is medicine, not sports; elonmusk 'I voted early today in Texas' and the Babylon Bee Minnesota voter-turnout satire are politics, not science
EXTRA_PRIVATE |= {'2115952763750203711','2115938524130365898','2115955817794928753'}  # 0604Z: B1Gsad post on the Red Baron worker's hours, kids and bills; RT_com and EricLDaugh posts on the Red Baron worker (private individual, as flagged since 2109Z)"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
