s=open('build_capture.py').read().split('\n')
k=[i for i,l in enumerate(s) if l.startswith("DESK_OVERRIDE_RUN.update({'2114147669987766603'")][0]
add=[
"skip_nsfw |= {'2113590120091660385','2114149831883268132','2107492885570490562'}  # 0301Z: likely paid (CHQMarkets Explee product pitch with a '$30 free' offer: 295 likes on 2.0M views; F0RGIAT0, 850 followers, Cam Coleman clip: 32 likes and 1 reply on 754K views; hungcesca, 43 followers, keyword-stuffed Hunger Games reaction video: 1,317 likes and 3 replies on 3.8M views)",
"EXTRA_PRIVATE |= {'2114007529168736396','2113793061147050245'}  # 0301Z: dudeitsokay livestream clip of an unnamed man taking a phone (private person); Brandons__1 funeral of a 1-year-old with children carrying the coffin (private family and children; precaution)",
"DESK_OVERRIDE_RUN.update({'2113827225418285081':'politics','2113809139759472874':'politics','2112556531225158088':'politics','2113808119562207548':'politics','2113737403449975076':'medicine','2114144918448840873':'entertainment','1765935471971213816':'entertainment','1879923986924224921':'sports','1912094476782428358':'music','2074923172483268651':'music','2114007529168736396':'internet','2113793061147050245':'justice'})  # 0301Z: Wisconsin-trend posts on the Wisconsin governor race, a ballot lawsuit and SNAP cards are politics, as is the MikeLevin Forbes Trump crypto post; NicHulscher Bill Gates pandemic clip medicine; Avengers: Doomsday and the Dragon Ball notice entertainment; Bob Uecker supercut sports; Taylor Swift and song posts music; livestream phone clip internet; Kohen Wiley funeral (police shooting) justice",
]
s[k+1:k+1]=add
open('build_capture.py','w').write('\n'.join(s))
