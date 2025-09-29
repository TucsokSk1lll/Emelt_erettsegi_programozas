lst = open('Digitalis_kultura\\2023_oktober\\rendel.txt','r').read().split('\n')
#lst.pop()

for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
    lst[i][0] = int(lst[i][0])
    lst[i][2] = int(lst[i][2])
#print(lst)
print(lst[0])

print('2.feladat')
print(f'A rendelesek szama: {len(lst)}.')

print('3.feladat')
nap = 9
szam = 0

for i in lst:
    if i[0] == nap:
        szam += 1
        
print(f'Rendelesek szama a napon {szam}.')

print('4.feladat')
nem_volt = 0
napok = {}

for i in range(30):
    napok.update({i+1:False})

for i in lst:
    if i[1] == 'NR':
        napok[i[0]] = True
        
for i in napok:
    if napok[i] == False:
        nem_volt += 1
   
if nem_volt > 0:     
	print(f'{nem_volt} nap nem volt a reklamban nem erintett varosbol rendeles.')
 
print('5.feladat')
legnagyobb = [69,0]

for i in lst:
    if i[2] > legnagyobb[1]:
        legnagyobb = [i[0],i[2]]
        
print(f'A legnagyobb darabszam: {legnagyobb[1]}, a rendeles napja: {legnagyobb[0]}.')

#print('6.feladat')
def osszes(nap,varos):
    darab = 0
    for i in lst:
        if i[0] == nap and i[1] == varos:
            darab += i[2]
    return darab

print('7.feladat')
varosok = {'PL':0,'TV':0,'NR':0}

for i in lst:
    if i[0] == 21:
    	varosok[i[1]] += i[2]
	
print(f'A rendel termekek darabszama a 21. napon: ',end='')

for i in varosok:
    print(f'{i}: {varosok[i]} ',end='')
print('\n',end='')

print('8.feladat')
eredmeny = {'PL':{},'TV':{},'NR':{}}

for i in eredmeny:
	for j in range(30):
		eredmeny[i].update({j+1:0})
  
for i in lst:
    eredmeny[i[1]][i[0]] += 1

print('Napok\t1..10\t11...20\t21...30')
print('PL\t',end='')
for i in range(3):
	kecske = 0
	for j in range(i*10,i*10+10):
		kecske += list(eredmeny.items())[0][1][j+1]
	print(f'{kecske}\t',end='')
print('\n',end='')

print('TV\t',end='')
for i in range(3):
	kecske = 0
	for j in range(i*10,i*10+10):
		kecske += list(eredmeny.items())[1][1][j+1]
	print(f'{kecske}\t',end='')
print('\n',end='')

print('NR\t',end='')
for i in range(3):
	kecske = 0
	for j in range(i*10,i*10+10):
		kecske += list(eredmeny.items())[2][1][j+1]
	print(f'{kecske}\t',end='')