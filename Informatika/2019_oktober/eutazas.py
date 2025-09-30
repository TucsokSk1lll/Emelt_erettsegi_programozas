import datetime
lst = open('Informatika\\2019_oktober\\utasadat.txt','r').read().split('\n')
lst.pop()
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
    
print(lst)

print('2.feldat')
print(f'A buszra {len(lst)} utas akart felszallni.')

print('3.feladat')
nemxd = 0

for i in lst:
    if i[-1] == '0':
        nemxd += 1
    elif i[3] != 'JGY':
        if datetime.datetime(int(i[1][0:4]),int(i[1][4:6]),int(i[1][6:8])) > datetime.datetime(int(i[-1][0:4]),int(i[-1][4:6]),int(i[-1][6:8])):
            nemxd += 1
        
print(f'A buszra {nemxd} utas nem szallhatott fel.')

print('4.feladat')
allomasok = {}

for i in lst:
    if i[0] not in allomasok:
        allomasok.update({i[0]:1})
    else:
        allomasok[i[0]] += 1
        
legnagyobb = '0'
for i in allomasok:
    if int(allomasok[i]) > allomasok[legnagyobb]:
        legnagyobb = i

print(f'A legtobb utas ({allomasok[legnagyobb]} fo) a {legnagyobb}. megalloban probalt felszallni.')

print('5.feladat')
ingyen = 0
kedvezmeny = 0

for i in lst:
    if i[3] == 'TAB' or i[3] == 'NYB':
        kedvezmeny += 1
    elif i[3] == 'NYP' or i[3] == 'RVS' or i[3] == 'GYK':
        ingyen += 1
        
print(f'Ingyenesen utazok szama {ingyen} fo.')
print(f'A kedvezmennyel utazok szama: {kedvezmeny} fo.')

#print('6.feladat')
def naposzama(e1,h1,n1,e2,h2,n2):
	h1 = (h1 + 9) % 12 
	e1 = e1 - h1 // 10 
	d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1 
	h2 = (h2 + 9) % 12 
	e2 = e2 - h2 // 10 
	d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1 
	return d2-d1

#print('7.feladat')
