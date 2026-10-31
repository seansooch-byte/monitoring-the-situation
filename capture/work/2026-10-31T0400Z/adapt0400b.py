s=open('build_capture.py').read()
def R(a,b,n=None):
    global s
    c=s.count(a); assert c>=1 and (n is None or c==n),(a[:80],c); s=s.replace(a,b)
R('CTXHANDLE','tiyora__'); R('CTXID','2116222771000963266'); R('CTXDESK','offbeat')
R('CTXSTART','2026-10-30T17:36:00Z'); R('CTXEND','2026-10-30T17:56:00Z')
R('CTXWHAT','tiyora__ "This is animal abuse" quote post, 2.7M views, the biggest new post under 24 hours once likely-paid posts are left out; the post it quotes was not returned')
R('CTXRESULT','1 reply and no quotes in the window')
R("CTX_IDS = ['2116222771000963266'] + CTX_REPLIES + CTX_QUOTES  # 0400Z: the context post itself","CTX_IDS = ['2116222771000963266'] + CTX_REPLIES + CTX_QUOTES  # 0400Z: the context post itself; 1 reply, the quote read returned nothing")
R("(2 reads). '\n            f'Screen: cut","(2 reads; 1 reply and no quotes in the 20-minute window). '\n            f'Screen: cut",1)
add = """
skip_nsfw |= {'2116175894318371010'}  # 0400Z: sexual text (santosvenganza 'suckle that baby dick' quote post)
skip_nsfw |= {'2103199796378939448','2116126609233400041','1841856218073030691','2115509421333700780'}  # 0400Z: likely paid (AppleTV Ted Lasso Season 4 ad copy, Sept 24: 1,991 likes on 18.0M views; AiWithIqra seedance 2.5 AI video, bio offers paid collabs: 2,449 likes on 4.18M views; PlayStation Chroma accessories pre-order post from Oct 2024: 5,699 likes on 750K views; GhostSoldierMov ticket promo, 995 followers: 539 likes on 620K views)
DESK_OVERRIDE_RUN.update({'2116134803770864023':'markets','2116261080406356000':'markets','2116306579779731464':'ai','2112921864406229367':'music','2115914525304107502':'music','2115657879675900404':'music','2116058504842928179':'music','2116277485524717825':'medicine','2115921052979405005':'internet','2116217692931924007':'business','2116246241528951011':'world','2115955402814697933':'politics','2116353467472380247':'gaming'})  # 0400Z desk fixes: lil_ahga Samsung Electronics chart meme and WatcherGuru $1.8T market loss are markets; elonmusk 'Cool' on the Grok phone feature is ai; BIGHIT TXT teaser, FUCCl Destin Conrad, PopBase Eminem/Rihanna and btschartsxdaily BTS MMA nominations are music; BillGates Alzheimer's is medicine; Pastor_Gabe Sour Patch Kids joke is internet; elonmusk on Gates's short position is business; JackPosobiec reply to Donald Tusk is world; MikeNellis on Ken Paxton is politics; FF_XIV_EN Evercold date is gaming
"""
R("DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116222771000963266']+CTXR+CTXQ})  # 0400Z: the context post and its context replies and quotes share its desk",
  "DESK_OVERRIDE_RUN.update({_x:'offbeat' for _x in ['2116222771000963266']+CTXR+CTXQ})  # 0400Z: the context post and its context replies and quotes share its desk"+add.rstrip('\n'),1)
open('build_capture.py','w').write(s); print('ok')
