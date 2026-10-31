s=open('build_capture.py').read()
a="skip_nsfw |= {'2116421086980276267'}"
i=s.index(a); j=s.index("\n",i)+1
s=s[:j]+"""DESK_OVERRIDE_RUN.update({'2116259094856360313':'politics','2116514747281490237':'politics','2116344876564726052':'politics','2116576272016892083':'entertainment','1699147798732476809':'sports','2116402408343617868':'internet'})  # 1802Z: desk fixes (FoxNews Trump garbage-truck anniversary in Green Bay, AaronRegunberg Francesca Hong post and GOP 'Kansas and Iowa are up next' rally post are politics, not the Wisconsin/Iowa games; DiscussingFilm Avengers: Doomsday drone show is entertainment, not medicine; TomBradyDaily Patriots clip is sports, not gaming; Rioriotalk hair post asking grok is internet, not ai)
"""+s[j:]
open('build_capture.py','w').write(s);print('ok')
