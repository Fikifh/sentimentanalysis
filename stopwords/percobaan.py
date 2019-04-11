import json
T = '{"nama":"udin", "umur":27}'
alay = ['sy', 'tp']
baku = ['saya','tapi']
data = json.loads(T)
h = 'perkenalkan nama sy fiki firmansyah dn sy suka sekali mie, tp sy jg punya keinginan utk tnya'

token = h.split()
for s in alay:
    baru = h.replace(s, baku)    
print(baru)
print(data['nama'], data['umur'])