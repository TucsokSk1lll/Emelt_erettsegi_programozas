x = open('Digitalis_kultura\\2023_majus\\taborok.txt','r').read().split('\n')
x.pop()
#print(x)

lst = []

for i in range(len(x)):
    lst.append(x[i].split('\t'))
print(lst)

print('2.feladat')
print(f'Az adatsorok szama: {len(lst)}')

print('3.feladat')

taborok = []

for i in range(len(lst)):
    if lst[i][5] == 'zenei':
        taborok.append(lst[i])

if len(taborok) > 0:
    for i in taborok:
        print(f'Zenei tabor kezdodik {i[0]}. ho {i[1]}. napjan. ')
else:
    print('Nem volt zenei tábor.')

print('4.feladat')
legnepszerubbek = []

legtobb = 0

for i in range(len(lst)):
    if len(lst[i][4]) > legtobb:
        legtobb = len(lst[i][4])

for i in range(len(lst)):
    if len(lst[i][4]) == legtobb:
        legnepszerubbek.append(lst[i])

for i in range(len(legnepszerubbek)):
    print(f'{legnepszerubbek[i][0]} {legnepszerubbek[i][1]} {legnepszerubbek[i][5]}')

#print('5.feladat')

def sorszam(honap,nap):
    napok = 0
    if honap == 6:
        napok += 0
        napok += nap-15
    if honap == 7:
        napok += 30-15
        napok += nap
    if honap == 8:
        napok += 30-15+31
        napok += nap
    return napok

print('6.feladat')
ho = 8
nap = 1

tart = 0

for i in range(len(lst)):
    #print(sorszam(lst[i][0],lst[i][1]) , sorszam(ho,nap) , sorszam(lst[i][2],lst[i][3]) , sorszam(ho,nap))
    if sorszam(int(lst[i][0]),int(lst[i][1])) < sorszam(ho,nap) and sorszam(int(lst[i][2]),int(lst[i][3])) > sorszam(ho,nap):
        tart += 1

print(f'Ekkor eppen {tart} tabor tart.')

print('7.feladat')
betu = 'L'

erdeklodott = []

for i in range(len(lst)):
    if betu in lst[i][4]:
        erdeklodott.append(lst[i])

erdeklodott_sorted = []
datumok = []

for i in range(len(erdeklodott)):
    #print(int(erdeklodott[i][0]),int(erdeklodott[i][1]))
    datumok.append(sorszam(int(erdeklodott[i][0]),int(erdeklodott[i][1])))
datumok.sort()

#print(datumok)
#print(erdeklodott)

for j in range(len(datumok)):
    for i in range(len(erdeklodott)):
        if sorszam(int(erdeklodott[i][0]),int(erdeklodott[i][1])) == datumok[j] and erdeklodott[i] not in erdeklodott_sorted:
            erdeklodott_sorted.append(erdeklodott[i])

print(erdeklodott_sorted)

elmehet = True

for i in range(len(erdeklodott_sorted)):
    for j in range(len(erdeklodott_sorted)):
        print(sorszam(erdeklodott_sorted[i][0],erdeklodott_sorted[i][1]),sorszam(erdeklodott_sorted[j][0],erdeklodott_sorted[j][1]))
        if (sorszam(int(erdeklodott_sorted[i][0]),int(erdeklodott_sorted[i][1])) < sorszam(int(erdeklodott_sorted[j][0]),int(erdeklodott_sorted[j][1])) and sorszam(int(erdeklodott_sorted[i][2]),int(erdeklodott_sorted[i][3])) < sorszam(int(erdeklodott_sorted[j][2]),int(erdeklodott_sorted[j][3]))) or (int(sorszam(int(erdeklodott_sorted[i][0])),int(erdeklodott_sorted[i][1])) > sorszam(int(erdeklodott_sorted[j][0]),int(erdeklodott_sorted[j][1])) and sorszam(int(erdeklodott_sorted[i][2]),int(erdeklodott_sorted[i][3])) > sorszam(int(erdeklodott_sorted[j][2]),int(erdeklodott_sorted[j][3]))):
            pass
        else:
            elmehet = False

if elmehet == True:
    print('Nem mehet el mindegyik taborba.')
else:
    print('Elmehet mindegyik taborba.')