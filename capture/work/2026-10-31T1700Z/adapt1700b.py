s=open('build_capture.py').read()
a="skip_nsfw |= {'2116209329556922392','2116279098259513364','2116316436209828169'}"
i=s.index(a); j=s.index("\n",i)+1
s=s[:j]+"""DESK_OVERRIDE_RUN.update({'2116187307506057283':'defense','2116441855655035248':'life','2116215956686954499':'offbeat','2116195183331012609':'offbeat','2116394236161781871':'internet','2116119786157642069':'politics','2116511508918050971':'sports','2116510970650493269':'internet'})  # 1700Z: desk fixes (OccupyDemocrats Hegseth/Navy sailor post is defense, not the Notre Dame-Navy game; navy satin heels post is life; retired Navy admiral UFO claim is offbeat; RabbiJeffx Chernobyl turbine post is offbeat; kazegogogo 'iPhone DUO' cosplay clip is internet; golub White House Halloween photo is politics; Carra23 apology to Aston Villa is sports; supern0va_08 manga coloured in by a niece is internet)
"""+s[j:]
open('build_capture.py','w').write(s);print('ok')
