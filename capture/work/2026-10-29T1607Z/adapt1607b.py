s=open('build_capture.py').read()
anchor="DESK_OVERRIDE_RUN.update({'2115811294951710978'"
i=s.index(anchor); j=s.index("\n",i)+1
add=("skip_nsfw |= {'2115327474687201556','2115591387882123406','2069962103432028377'}  # 1607Z: sexual text (GordFT robot joke, a prostate-exam joke); sexual innuendo caption on a concert clip (Oct 2025 origin)\n"
"EXTRA_PRIVATE |= {'2115496186614251902'}  # 1607Z: rae_chloe133 'why can't all men be like this' video of a man not named as a public figure (media not described, when in doubt)\n"
"DESK_OVERRIDE_RUN.update({'2115523333089354033':'entertainment','2115823011399938182':'markets','2115783934298526179':'entertainment','2115651643031290246':'ideas','2115792124998209842':'entertainment','2115603773699903748':'politics','2115593564478415011':'politics','2115779934136545373':'ai','2115827957386056068':'markets','2115827775810445764':'markets','2115827789404271054':'markets'})  # 1607Z desk fixes: K-drama murder-scene clip is entertainment; Elon Musk 'Interesting' on Druckenmiller's Hyperliquid post and its context replies and quotes are markets; Kris Jenner granddaughter post is entertainment; Einstein letter question is ideas; James Gunn Suicide Squad podcast is entertainment; Tim Walz on Trump and Bikers for Trump rally post are politics; employers pulling back on AI is ai\n")
s=s[:j]+add+s[j:]
open('build_capture.py','w').write(s); print('ok')
