s=open('build_capture.py').read()
anchor="DESK_OVERRIDE_RUN.update({'2116343266081640792'"
i=s.index(anchor); j=s.index("\n",i)+1
add=("DESK_OVERRIDE_RUN.update({'2116363443871850645':'sports','2116414789194789254':'politics','2116386027552096613':'politics','2116240553620783328':'markets','2116176184757096758':'politics','2116200444276178966':'tech','2116398208725483797':'tech'})  # 0800Z desk fixes: Gerard Pique on Barcelona and Pacho is sports; Musk and Bill Maher on James Talarico (Texas Senate race) are politics; Intel/Reddit/Roblox stock drops are markets; ZeekArkham on liberals and conservatives is politics; Tesla and Robotaxi brand clips are tech\n"
     "TREND_OFF.setdefault('gerard', set()).add('2116363443871850645')  # 0800Z: FullTime90X Gerard Pique post matches the word, not the My Chemical Romance (Gerard Way) trend\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s);print('ok')
