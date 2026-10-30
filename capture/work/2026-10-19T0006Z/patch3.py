s=open('build_capture.py').read()
a="SEX_WORDS = ("
assert s.count(a)==1
s=s.replace(a,"skip_nsfw |= {'2110789320869089345','2111607977576673607','2111834756220694619','2110960974324801623','2111683170257293481','2111929432575250845','2111814936104260042','2111388055982518381'}  # 0006Z: likely promoted (BBQChiefs Brittany Mahomes photo set: 4,322 likes on 11.8M views; pahrduve link-only videos: 1 like on 2.86M views and 26 likes on 1.61M views); slur as the whole text (Himbruh02); graphic injury video (intel_nova Alamodome rappelling fall, as the MLFootball clip left out in 0400Z); sexual text (p1cass00 Herbert post); sponsored betting picks (HoldThe_Phone, @BetMGM); off-topic in the Raiders stream (Shnyatheninja ARC Raiders game clip)\n"+a,1)
a="DESK_OVERRIDE_RUN.update({'2111564441380864468':'sports'"
assert s.count(a)==1
i=s.index(a); j=s.index('\n',i)
s=s[:j+1]+"DESK_OVERRIDE_RUN.update({'2111092458109231403':'internet','2111081082128838830':'internet','2111469998489415739':'internet','2111724384620830784':'sports','2111642809769832950':'sports','2111277510176416027':'medicine','2111515371031113817':'world','2111853238353793404':'world'})  # 0006Z: 'just say you're gay' exchange and the edit of it are internet; Duke Kimari Robinson posts are sports; RFK Jr. measles clip is medicine; Paris Republique clip and Albania Supreme Court fire are world\nEXTRA_PRIVATE |= {'2111724384620830784','2111642809769832950'}  # 0006Z: Duke medical staff member shoved by a player (not a public figure) and the player himself (college athlete, public status unclear)\n"+s[j+1:]
open('build_capture.py','w').write(s); print('ok')
