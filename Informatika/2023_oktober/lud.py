import math
dobasok = open('Informatika\\2023_oktober\dobasok.txt','r').read().split(' ')
dobasok[-1] = dobasok[-1][0]
for i in range(len(dobasok)):
    dobasok[i] = int(dobasok[i])
#print(dobasok)

x = open('Informatika\\2023_oktober\osvenyek.txt','r').read().split('\n')
x.pop()
#print(x)

osvenyek = []

for i in range(len(x)):
    lst = []
    for j in range(len(x[i])):
        lst.append(x[i][j])
    osvenyek.append(lst)
#print(osvenyek)

print('2.feladat')
print(f'A dobások száma: {len(dobasok)}')
print(f'Az ösvények száma: {len(osvenyek)}')

print('3.feladat')
leghoszabb = [69,0]

for i in range(len(osvenyek)):
    if len(osvenyek[i]) > leghoszabb[1]:
        leghoszabb = [i+1,len(osvenyek[i])]
        
print(f'Az egyik leghosszabb a(z) {leghoszabb[0]}. ösvény, hossza: {leghoszabb[1]}')

print('4.feladat')
sorszam = 9
jatekosok = 5

print('5.feladat')
tipusok = {
	'M': 0,
	'V': 0,
	'E': 0
}

for i in osvenyek[sorszam-1]:
    tipusok[i] += 1
print(tipusok)

print('6.feladat')
kulonleges = open('Informatika\\2023_oktober\\kulonleges.txt','w')

for i in range(len(osvenyek[sorszam-1])):
    if osvenyek[sorszam-1][i] != 'M':
        kulonleges.write(f'{i}\t{osvenyek[sorszam-1][i]}\n')
        
print('7.feladat')
allas = {}

for i in range(jatekosok):
    allas.update({i: 0})

for i in range(len(dobasok)):
	allas[i%jatekosok] += dobasok[i]
	if i%jatekosok == 0:
		if allas[0] >= len(osvenyek[sorszam-1]):
			print(f'A játék a(z) {math.ceil(i/5)}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {1}')
			break
		if allas[1] >= len(osvenyek[sorszam-1]):
			print(f'A játék a(z) {math.ceil(i/5)}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {2}')
			break
		if allas[2] >= len(osvenyek[sorszam-1]):
			print(f'A játék a(z) {math.ceil(i/5)}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {3}')
			break
		if allas[3] >= len(osvenyek[sorszam-1]):
			print(f'A játék a(z) {math.ceil(i/5)}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {4}')
			break
		if allas[4] >= len(osvenyek[sorszam-1]):
			print(f'A játék a(z) {math.ceil(i/5)}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {5}')
			break
print(allas)

print('8.feladat')
allas = {}

for i in range(jatekosok):
    allas.update({i+1: 0})
    
nyert = []    
    
for i in range(0,len(dobasok),jatekosok):
	for j in range(jatekosok):
		#print(allas)
		if allas[1+j]+dobasok[i+j] < len(osvenyek[sorszam-1]):
			if osvenyek[sorszam-1][allas[1+j]+dobasok[i+j]-1] == 'M':
				allas[(i%jatekosok)+1+j] += dobasok[i+j]
			elif osvenyek[sorszam-1][allas[1+j]+dobasok[i+j]-1] == 'E':
				allas[(i%jatekosok)+1+j] += dobasok[i+j]*2
			elif osvenyek[sorszam-1][allas[1+j]+dobasok[i+j]-1] == 'V':
				pass
		else:
			#print(allas)
			nyert.append((i%jatekosok)+1+j)
	if nyert != []:
		break
print(nyert)
print(allas)