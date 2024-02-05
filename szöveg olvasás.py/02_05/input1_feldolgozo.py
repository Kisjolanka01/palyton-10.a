file= open("szöveg olvasás/02_05/input1.txt")
sorok=file.readlines()
file.close
print(sorok)

szamok=[]
for i in range(len(sorok)):
    szam_str=sorok[i].strip()
    #print(szam_str)
    szam=int(szam_str)
    #print(szam_str)
    szamok.append(szam)

print(szamok)

osszeg=0
for i in range(len(szamok)):
    osszeg+=szamok[i]
print(osszeg)


file= open("szöveg olvasás/02_05/input1.txt")
sorok=file.readlines()
file.close

szamok=0
for i in range(len(sorok)):
    szam=int(sorok[i].strip())
    szamok.append()
print(szamok)


szamok=0
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)

