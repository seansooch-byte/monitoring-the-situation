p='build_capture.py'; s=open(p).read()
k="skip_nsfw |= {'2100349873094541761','2093272806125429196','2111495426339750185'}"
a=s.index(k); b=s.index('\n',a)
s=s[:b+1]+"skip_nsfw |= {'2114341207514259697','2043105295468019765','2115246964199883101','2115236397892145271','2115594563918106683','2115423405076004969','2115595864811163998'}  # 0001Z: sexual text or paid adult promos in the it repost and my quote streams (nananyanbabe, AvaVenom, smc429, girlderping, Alexatsbaby, GAYGOMHAR, hntddoII)\nskip_nsfw |= {'2115320798307025327','2115460252246151446','2115320581528998211','2115199705244213405','2115268804578050073','2115264150284689456'}  # 0001Z: likely paid (F0RGIAT0 Lillard clip: 36 likes on 599K views; MisoginLabsInc link-only: 17 likes on 584K; wokdior Ja Morant clip: 50 likes on 404K; canadaicekw link-only: 5 likes on 387K; notpardonmymeme link-only: 7 likes on 279K; ShowCaseShabazz Mikel Brown clip: 139 likes on 270K)\n"+s[b+1:]
open(p,'w').write(s); print('ok')
