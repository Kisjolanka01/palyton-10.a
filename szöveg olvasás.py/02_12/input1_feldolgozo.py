file= open("szöveg olvasás/02_12/input1.txt")
sorok=file.readlines()
file.close

szamok=0
osszeg=0
for i in range(len(szamok)):
    osszeg+=szamok[i]
print(osszeg)

