x = open(file='Digitalis_kultura\\2024_majus\\bedat.txt',mode='r',encoding='utf-8').read().split('\n')
x.pop()
#print(x)

lst = []

for i in range(len(x)):
    lst.append(x[i].split(' '))

print(lst)

print('2. feladat')

belepes = None
kilepes = None

for i in range(len(lst)):
    if lst[i][2] == '1':
        belepes = lst[i][1]
        break

for i in reversed(range(len(lst))):
    if lst[i][2] == '2':
        kilepes = lst[i][1]
        break

print(belepes)
print(kilepes)

#print('3. feladat')

kesok = open(file='Digitalis_kultura\\2024_majus\kesok.txt',mode='w+',encoding='utf-8')

for i in range(len(lst)):
    if int(lst[i][1][0:2]) == 7 and int(lst[i][1][3:5]) > 50 and int(lst[i][2]) == 1:
        kesok.write(lst[i][1] + ' ' +lst[i][0] + '\n')
    elif int(lst[i][1][0:2]) == 8 and int(lst[i][1][3:5]) <= 15 and int(lst[i][2]) == 1:
        kesok.write(lst[i][1] + ' ' +lst[i][0] + '\n')

print('4. feladat')
menza = 0

for i in range(len(lst)):
    if int(lst[i][2]) == 3:
        menza += 1

print(menza)

print('5. feladat')
konyvtar = 0
xdbro = []

for i in range(len(lst)):
    if int(lst[i][2]) == 4 and lst[i][0] not in xdbro:
        konyvtar += 1
        xdbro.append(lst[i][0])

print(konyvtar)

if konyvtar > menza:
    print('A konyvtarba tobben jartak be.')
else:
    print('A menzaba tobben jartak be.')

print('6. feladat')

belepok = []
duplan_beleopk = []

for i in range(len(lst)):
    #print(lst[i][1][0:2],lst[i][1][3:6])
    if lst[i][0] not in belepok and lst[i][2] == '1':
        belepok.append(lst[i][0])
    elif lst[i][0] in belepok and lst[i][2] == '2':
        belepok.remove(lst[i][0])
    elif lst[i][0] in belepok and lst[i][2] == '1' and ((int(lst[i][1][0:2]) == 10 and int(lst[i][1][3:6]) > 50) or (int(lst[i][1][0:2]) == 11 and int(lst[i][1][3:6]) == 0)):
        duplan_beleopk.append(lst[i][0])

#print(belepok)
print(duplan_beleopk)

print('7. feladat')

azonosto = 'ZOOM'

belepes = []
kilepes = []

for i in range(len(lst)):
    if lst[i][0] == azonosto and lst[i][2] == '1':
        belepes.append(lst[i][1])
    if lst[i][0] == azonosto and lst[i][2] == '2':
        kilepes.append(lst[i][1])

idoxd = []

idoxd.append(int(kilepes[len(kilepes)-1][0:2]) - int(belepes[len(belepes)-1][0:2]))
if int(kilepes[len(kilepes)-1][3:5]) < int(belepes[len(belepes)-1][3:5]):
    idoxd[0] -= 1
    #print(kilepes[len(kilepes)-1])
    kilepes[len(kilepes)-1] =  str(kilepes[len(kilepes)-1][0:2]) + ':' + str(int(kilepes[len(kilepes)-1][3:5]) + 60)
    #print(kilepes[len(kilepes)-1])
idoxd.append(int(kilepes[len(kilepes)-1][3:5]) - int(belepes[len(belepes)-1][3:5]))


#print(belepes,kilepes)
#print(idoxd)
print(str(idoxd[0]) + ' ora ' + str(idoxd[1]) + ' perc ')

