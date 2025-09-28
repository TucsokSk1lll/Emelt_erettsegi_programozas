import math
#print('1.feladat')
file = 'konnyu.txt'
sor = 1
oszlop = 1

#print('2.feladat')
lst = open(f'Informatika\\2021_oktober\\{file}','r').read().split('\n')
lst.pop()

for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
    
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = int(lst[i][j])    

lepesek = []

for i in lst:
    if len(i) == 3:
        lepesek.append(i)
        
for i in range(len(lepesek)):
    lst.pop()
        
print(lepesek)
print(lst)

print('3.feladat')
print(f'A megadott helyen szereplo szam: {lst[sor-1][oszlop-1]}')

def hely(sor,oszlop): 
    sor = math.ceil(sor/3)
    oszlop = math.ceil(oszlop/3)
    
    if sor == 1 and oszlop == 1:
        return 1
    elif sor == 1 and oszlop == 2:
        return 2
    elif sor == 1 and oszlop == 3:
        return 3
    elif sor == 2 and oszlop == 1:
        return 4
    elif sor == 2 and oszlop == 2:
        return 5
    elif sor == 2 and oszlop == 3:
        return 6
    elif sor == 3 and oszlop == 1:
        return 7
    elif sor == 3 and oszlop == 2:
        return 8
    elif sor == 3 and oszlop == 3:
        return 9
    
print(f'A hely a(z) {hely(sor,oszlop)} resztablazathoz tartozik.')

print('4.feladat')
nulla = 0

for i in lst:
    for j in i:
        if j == 0:
            nulla += 1
    
print(f'Az ures helyek aranya: {round(nulla/81*100,1)}%')

print('5.feladat')
for i in lepesek:
    sor = i[1]
    oszlop = i[2]
    szam = i[0]
    cella = hely(sor,oszlop)
    hiba = False
    
    print(f'A kivalasztott sor: {sor} oszlop: {oszlop} a szam: {szam}')
    
    if lst[sor-1][oszlop-1] != 0:
        hiba = True
        print('A helyet mar kitoltottek.\n')
        
    
    for j in lst[sor-1]:
        if j == szam:
            if hiba == False: 
                hiba = True
                print('Az adott sorban mar szerepel a szam\n')
                
    for j in lst:
        if j[oszlop-1] == szam:
            if hiba == False: 
                hiba = True
                print('Az adott oszlopban mar szerepel a szam\n')
                
    cella_szamok = []
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if hely(i+1,j+1) == cella:
                if lst[i][j] != 0:
                    cella_szamok.append(lst[i][j])
                
    if szam in cella_szamok:
        if hiba == False: 
            hiba = True
            print('Az adott resztablazatban mar szerepel a szam.\n')
            
    if hiba == False:
        print('A lepes megteheto.\n')