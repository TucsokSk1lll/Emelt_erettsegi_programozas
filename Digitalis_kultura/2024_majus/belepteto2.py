lst = open('Digitalis_kultura\\2024_majus\\bedat.txt','r').read().split('\n')
lst.pop()
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
for i in range(len(lst)):
    lst[i][1] = lst[i][1].split(':')
#print(lst)

print('2.feladat')
print(f'Az elso tanulo {lst[0][1][0]}:{lst[0][1][1]}-kor lepett be a fokapun.')
print(f'Az utolso tanulo {lst[-1][1][0]}:{lst[-1][1][1]}-kor lepett ki a fokapun.')

#print('3.feladat')
kesok2 = open('Digitalis_kultura\\2024_majus\\kesok2.txt','w')

for i in lst:
    if i[2] == '1' and ((int(i[1][0]) == 7 and int(i[1][1]) > 50) or (int(i[1][0]) == 8 and int(i[1][1]) < 15)):
        kesok2.write(f'{i[1][0]}:{i[1][1]} {i[0]}\n')
        
print('4.feladat')
ebedelt = 0

for i in lst:
    if i[2] == '3':
        ebedelt += 1
print(f'A menzan aznap {ebedelt} tanulo ebedelt.')

print('5.feladat')
kolcsonzott = 0
xd = []

for i in lst:
    if i[2] == '4' and i[0] not in xd:
        kolcsonzott += 1
        xd.append(i[0])
print(f'A menzan aznap {kolcsonzott} tanulo kolcsonzott a konyvtarban.')

if kolcsonzott > ebedelt:
    print('Tobben voltak mint a menzan.')
else:
    print('Nem voltak tobben mint a menzan.')

print('6.feladat')
lul = []

for i in lst:
    if i[0] not in lul and i[2] == '1':
        lul.append(i[0]) 
    elif i[0] in lul and i[2] == '2':
        lul.remove(i[0]) 
    elif i[0] in lul and i[2] == '1' and (i[1][0] == '10' and int(i[1][1]) > 45):
        print(i[0],end=' ')
print('\n7.feladat')
azonosito = 'ZOOM'

elso = ['17','59']
utolso = ['8','09']

for i in lst:
	if i[0] == azonosito:
		if int(i[1][0]) < int(elso[0]):
			elso = i[1]
		elif int(i[1][0]) == int(elso[0]) and int(i[1][1]) < int(elso[1]):
			elso = i[1]
			
		if int(i[1][0]) > int(utolso[0]):
			utolso = i[1]
		elif int(i[1][0]) == int(utolso[0]) and int(i[1][1]) > int(utolso[1]):
			utolso = i[1]

percek_belepes = int(elso[0])*60 + int(elso[1])
percek_kilepes = int(utolso[0])*60 + int(utolso[1])

#print(elso,utolso)
eltelt = percek_kilepes-percek_belepes
if elso[0] != '17':
    print(f'A tanulo erkezese es tavozasa kozott {eltelt//60} ora {eltelt%60} perc telt el.')
else:
    print('Ilyen azonositoju tanulo aznap nem volt az iskolaban.')