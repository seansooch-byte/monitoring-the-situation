s=open('build_capture.py').read()
anchor="# 1802Z: DiscussingFilm Dune popcorn bucket"
j=s.index("\n",s.index(anchor))+1
add=("skip_nsfw |= {'2115668034924781701','1922842809129656632'}  # 1802Z: sexual text (paygoddesslilly 'face sitting' post; makeyabitchnutt sexual post about an influencer)\n"
"skip_nsfw |= {'2086794573297361074','1971897954387874111','2115475466257596516'}  # 1802Z: likely paid (kotakneo trading ad copy, 5,813 likes on 72.5M views; loonapilld bare video post, 3,615 likes and 29 replies on 17.3M views; sunra_ai API launch from a 10.7K-follower account, 3,930 likes on 4.4M views)\n"
"EXTRA_PRIVATE |= {'2115454670990868837','2115557948525060580','1947381281660010703','2108425973318418541'}  # 1802Z: Crazymoments01 shelter story naming a private man (Glen, 50, a teacher); IShowSpeedHQ clip of a 'random guy' at a rhythm game; therecount clip of an unnamed woman at a town hall about her OB-GYN; ChaosTV video of an unnamed man at a mental health clinic (private people, when in doubt)\n"
"TREND_OFF.setdefault('Burton', set()).update({'2115139787745095797','2115785873367371976','2115539117333254440'})  # 1802Z: Givenchy 'Sarah Burton' dress post, a missing-person post and another post match the word, not the WNBA Finals Veronica Burton trend\n"
"DESK_OVERRIDE_RUN.update({'2115139787745095797':'entertainment','2115601695933603881':'gaming','2115813444083490867':'internet'})  # 1802Z: Givenchy Celine Dion dress is entertainment, not sports; DiscussingFilm GTA 6 police post is gaming; Dexerto YouTuber thumbnails post is internet\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s);print('ok')
