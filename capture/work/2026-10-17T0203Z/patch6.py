s=open('build_capture.py').read()
a="for a,b in [('#SmackDown','Nikki Bella'),"
assert a in s
s=s.replace(a,"for a,b in [('Memphis','Marcus Stokes'),('Marcus Stokes','Memphis'),('Memphis','Tulane'),('Tulane','Memphis'),('Baron Corbin','#SmackDown'),('#SmackDown','Baron Corbin'),('#SmackDown','Nikki Bella'),",1)
open('build_capture.py','w').write(s); print('ok')
