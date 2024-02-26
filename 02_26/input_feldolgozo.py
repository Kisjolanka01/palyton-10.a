#1 feladat

file = open("02_26/input1.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg/len(szamok)
print(f'Az elso fajl atlaga: {atlag}')

#2 fajl

file = open("02_26/input2.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(2, len(sorok)):
    szamok.append(int(sorok[i].strip()))

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg/len(szamok)
print(f'Az masodik fajl atlaga: {atlag}')

#3 fajl

file = open("02_26/input3.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(1, len(sorok)-1):
    szamok.append(int(sorok[i].strip()))

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg/len(szamok)
print(f'Az harmadik fajl atlaga: {atlag}')

#4 fajl

file = open("02_26/input4.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg/len(szamok)
print(f'Az negyedik fajl atlaga: {atlag}')

#5 fajl

file = open("02_26/input5.txt", encoding='utf-8')
sorok = file.readlines()
file.close()

szamok = []
for i in range(2,len(sorok)-1):
    szamok.append(int(sorok[i].strip()))

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg/len(szamok)
print(f'Az otodik fajl atlaga: {atlag}')
