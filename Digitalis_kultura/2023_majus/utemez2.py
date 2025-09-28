import datetime
lst = open('Digitalis_kultura\\2023_majus\\taborok.txt','r').read().split('\n')
lst.pop()
for i in range(len(lst)):
    lst[i] = lst[i].split('\t')
    for j in range(4):
        lst[i][j] = int(lst[i][j])
    betuk = lst[i][4]
    lst[i][4] = []
    for j in range(len(betuk)):
        lst[i][4].append(betuk[j]) 
#print(lst)

print('2.feladat')
print(f'Az adatsorok szama: {len(lst)}.')
print(f'Az elso rogzitett tabor temaja: {lst[0][5]}.')
print(f'Az utolso rogzitett tabor temaja: {lst[-1][5]}.')

print('3.feladat')
zenei_taborok = []

for i in lst:
    if i[5] == 'zenei':
        zenei_taborok.append(i)
        
if len(zenei_taborok) > 0:
    for i in zenei_taborok:
        print(f'Zenei tabor kezdodik {i[0]}. honap {i[1]}. napjan.')
else:
    print('Nem volt zenei tabor.')
        
print('4.feladat')
legtobben = [[69,69,69,69,['xd','kek'],'anyukad']]

for i in lst:
    if len(i[4]) > len(legtobben[0][4]):
        legtobben = [i]
    elif len(i[4]) == len(legtobben[0][4]):
        legtobben.append(i)

print('Legnepszerubbek: ')
for i in legtobben:     
	print(i[0],i[1],i[5])

print('6.feladat')
ho = 8
nap = 1

tartanak = []

for i in lst:
	if (i[0] < ho or (i[0] == ho and i[1] < nap)) and (i[2] > ho or (i[2] == ho and i[3] > nap)):
		tartanak.append(i)

print(f'Ekkor eppen {len(tartanak)} tabor tart.')

print('7.feladat')
jel = 'L'
taborok = []

for i in lst:
    if jel in i[4]:
        taborok.append(i)
        
#print(taborok)

elmehet = True
for i in range(len(taborok)):
	for j in range(i+1,len(taborok)):
		i_eleje = datetime.datetime(2025, taborok[i][0], taborok[i][1])
		i_vege = datetime.datetime(2025, taborok[i][2], taborok[i][3])
		j_eleje = datetime.datetime(2025, taborok[j][0], taborok[j][1])
		j_vege = datetime.datetime(2025, taborok[j][2], taborok[j][3])

		if (i_eleje < j_eleje and i_vege < j_eleje) or (i_eleje > j_vege and i_vege > j_vege):
			pass
		else:
			#print(i_eleje,i_vege,j_eleje,j_vege)
			elmehet = False
   
if elmehet == False:
    print('Nem mehet el mindegyik taborba.')
else:
    print('Elmehet mindegyik taborba.')
    
egytanulo = open('Digitalis_kultura\\2023_majus\\egytanulo2.txt','w')

legkisebb = [12,12,69,69,['xd','kek'],'anyukad']
while taborok != []:
	for i in taborok:
		if datetime.datetime(2025,i[0],i[1]) < datetime.datetime(2025,legkisebb[0],legkisebb[1]):
			legkisebb = i

	egytanulo.write(f'{legkisebb[0]}.{legkisebb[1]}:{legkisebb[2]}:{legkisebb[3]}. {legkisebb[5]}\n')
	taborok.remove(legkisebb)
	legkisebb = [12,12,69,69,['xd','kek'],'anyukad']