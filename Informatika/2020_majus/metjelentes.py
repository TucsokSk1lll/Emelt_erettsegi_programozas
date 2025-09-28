import math
x = open('Informatika\\2020_majus\\tavirathu13.txt','r').read().split('\n')
x.pop()

for i in range(len(x)):
    x[i] = x[i].split(' ')
    
#print(x)

lst = []

for i in x:
    dic = {
		'Telepules': i[0],
		'Ido': {'Ora':int(i[1][0:2]),'Perc':int(i[1][2:5])},
		'Szel': {'Irany':i[2][0:3],'Ero':int(i[2][3:5])},
		'Ho': int(i[3])
	}
    lst.append(dic)
    
#print(lst)

print('2.feladat')
Telepules = 'SM'

for i in range(len(lst)-1,0,-1):
	if lst[i]['Telepules'] == Telepules:
		print(f'Az tolso meresi adat a megadott telepulesrol {lst[i]['Ido']['Ora']}:{lst[i]['Ido']['Perc']}-kor erkezett.')
		break

print('3.feladat')
Szelso_ertekek = {
	'Legkisebb': {'Telepules': 'SN', 'Ido': {'Ora': '06', 'perc': '45'}, 'Szel': {'Irany': '320', 'Ero': '06'}, 'Ho': 20},
	'Legnagyobb': {'Telepules': 'SN', 'Ido': {'Ora': '06', 'perc': '45'}, 'Szel': {'Irany': '320', 'Ero': '06'}, 'Ho': 20}
}


for i in lst:
    if i['Ho'] < Szelso_ertekek['Legkisebb']['Ho']:
        Szelso_ertekek['Legkisebb'] = i
    if i['Ho'] > Szelso_ertekek['Legnagyobb']['Ho']:
        Szelso_ertekek['Legnagyobb'] = i 
        
print(f'A legalacsonyabb homerseklet: {Szelso_ertekek["Legkisebb"]['Telepules']} {Szelso_ertekek["Legkisebb"]['Ido']['Ora']}:{Szelso_ertekek["Legkisebb"]['Ido']['Perc']} {Szelso_ertekek["Legkisebb"]['Ho']} fok.')
print(f'A legmagasabb homerseklet: {Szelso_ertekek["Legnagyobb"]['Telepules']} {Szelso_ertekek["Legnagyobb"]['Ido']['Ora']}:{Szelso_ertekek["Legnagyobb"]['Ido']['Perc']} {Szelso_ertekek["Legnagyobb"]['Ho']} fok.')

print('4.feladat')
Szelcsend = []

for i in lst:
    if i['Szel']['Irany'] == '000':
        Szelcsend.append(i)
        
if i != []:
    for i in Szelcsend:
        print(f'{i['Telepules']} {i['Ido']['Ora']}:{i['Ido']['Perc']}')
else:
    print('Nem volt szelcsend a meresek idejen.')
    
print('5.feladat')
Ertekek = {}

for i in lst:
    if i['Telepules'] not in Ertekek:
        Ertekek.update({i['Telepules']:{'Eredmenyek':{'Kozephomerseklet':'Na','Hoingas':'Na'},'Ertekek':{'Kozephomerseklet':{1:[],7:[],13:[],19:[]},'Hoingas':{'Legkisebb':100,'Legnagyobb':0}}}})
        
for i in lst:
	if i['Ido']['Ora'] == 1 or i['Ido']['Ora'] == 7 or i['Ido']['Ora'] == 13 or i['Ido']['Ora'] == 19:
		Ertekek[i['Telepules']]['Ertekek']['Kozephomerseklet'][i['Ido']['Ora']].append(i['Ho'])
	if i['Ho'] > Ertekek[i['Telepules']]['Ertekek']['Hoingas']['Legnagyobb']:
		Ertekek[i['Telepules']]['Ertekek']['Hoingas']['Legnagyobb'] = i['Ho']
	if i['Ho'] < Ertekek[i['Telepules']]['Ertekek']['Hoingas']['Legkisebb']:
		Ertekek[i['Telepules']]['Ertekek']['Hoingas']['Legkisebb'] = i['Ho']



for i in Ertekek:
	osszeg = 0
	szamok = 0
	for j in Ertekek[i]['Ertekek']['Kozephomerseklet']:
		if Ertekek[i]['Ertekek']['Kozephomerseklet'][j] != []:
			for k in Ertekek[i]['Ertekek']['Kozephomerseklet'][j]:
				osszeg += k
				szamok += 1
		else:
			break

	for j in Ertekek[i]['Ertekek']['Kozephomerseklet']:
		if Ertekek[i]['Ertekek']['Kozephomerseklet'][j] == []:
			osszeg = 0
   
	if osszeg != 0:
		Ertekek[i]['Eredmenyek']['Kozephomerseklet'] = round(osszeg/szamok)
	Ertekek[i]['Eredmenyek']['Hoingas'] = Ertekek[i]['Ertekek']['Hoingas']['Legnagyobb'] - Ertekek[i]['Ertekek']['Hoingas']['Legkisebb']
    
#print(Ertekek)

for i in Ertekek:
	if Ertekek[i]['Eredmenyek']['Kozephomerseklet'] != 'Na':
		print(f'{i} kozephomerseklet: {Ertekek[i]['Eredmenyek']['Kozephomerseklet']}; Homerseklet-ingadozas: {Ertekek[i]['Eredmenyek']['Hoingas']}')
	else: 
		print(f'{i} {Ertekek[i]['Eredmenyek']['Kozephomerseklet']}; Homerseklet-ingadozas: {Ertekek[i]['Eredmenyek']['Hoingas']}')
  
print('6.feladat')
Ertekek = {}

for i in lst:
    if i['Telepules'] not in Ertekek:
        Ertekek.update({i['Telepules']:{}})
        
for i in lst:
    Ertekek[i['Telepules']].update({f'{i['Ido']['Ora']}:{i['Ido']['Perc']}': i['Szel']['Ero']})

for i in Ertekek:
    file = open(f'Informatika\\2020_majus\\{i}.txt','w')
    file.write(f'{i}\n')
    for j in Ertekek[i]:
        file.write(f'{j} {Ertekek[i][j]*'#'}\n')

#print(Ertekek)