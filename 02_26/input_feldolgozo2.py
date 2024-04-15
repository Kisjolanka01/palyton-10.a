file= open("02_26/input92.txt")
sorok=file.readlines()
file.close

szamok=0
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip))
 
osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg/len(szamok)
print(f'Az elso fajl atlaga: {atlag}')