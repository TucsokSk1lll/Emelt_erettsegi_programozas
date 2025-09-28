x = open(file='2018.majus\\fogado.txt',mode='r')
x = x.read()
x = x.split('\n')

lst = []

for i in range(len(x)):
    for j in range(len(x[i])):
        lst2 = []
        if x[i][j].isdigit() == True:
            lst2.append(x[i][0:(j-1)])
            lst2.append(x[i][(j):(j+5)])
            lst2.append(x[i][(j+5):(j+10)])
            lst2.append(x[i][(j+11):(j+13)])
            lst2.append(x[i][(j+14):(j+16)])
            lst2.append(x[i][(j+17):(j+22)])
            lst.append(lst2)
            break
    
print(lst)

print('2. feladat \n')
print(len(lst))

print('3.feladat \n')
nev = 'Nagy Ferenc'
db = 0

for i in range(len(lst)):
    if lst[i][0] == nev:
        db += 1

print(db)

print('4.feladat \n')
idopont = '17:40'
lst3 = []

for i in range(len(lst)):
    if lst[i][1] == idopont:
        lst3.append(lst[i][0])

lst3.sort()
print(lst3)

print('5.feladat \n')
legkorabb = ['Csorba Ede', '16:30', ' 2017', '10', '28', '18:48']

for i in range(1,len(lst)):
    if lst[i][2] < legkorabb[2]:
        legkorabb = lst[i]
    elif lst[i][2] == legkorabb[2]:
        if lst[i][3] < legkorabb[3]:
            legkorabb = lst[i]
        elif lst[i][3] == legkorabb[3]:
            if lst[i][4] < legkorabb[4]:
                legkorabb = lst[i]
            elif lst[i][4] == legkorabb[4]:
                if lst[i][5] < legkorabb[5]:
                    legkorabb = lst[i]

print(legkorabb)

print('6.feladat \n')
lst4 = ['16:00','16:10','16:20','16:30','16:40','16:50',
        '17:00','17:10','17:20','17:30','17:40','17:50']

for i in range(len(lst)):
    if lst[i][0] == 'Barna Eszter' and lst[i][1] in lst4:
        lst4.remove(lst[i][1])

print(lst4)

for i in range(1,len(lst4)):
    if int(lst4[int(len(lst4)-i)][0:2]) == int(lst4[int(len(lst4)-i-1)][0:2]) and int(lst4[int(len(lst4)-i)][3:5]) == int(lst4[int(len(lst4)-i-1)][3:5]) +10:
        pass
    else:
        print(lst4[len(lst4)-i])
        break
#if int(lst4[3:4])