import random

# 1. feladat
ervenyes_bevitel = False
while not ervenyes_bevitel:
    n_str = input("Add meg a lista elemszámát [30...60]: ")
    if n_str.isdigit() and 30 <= int(n_str) <= 60:
        elemszam = int(n_str)
        ervenyes_bevitel = True
    else:
        print("Hibás adatbevitel! Próbáld meg újra...")

# Lista létrehozása
szamok = [random.randint(-100, 100) for _ in range(elemszam)]

# 2. feladat
ervenyes_intervalum = False
while not ervenyes_intervalum:
    kezdo_str = input(f"Add meg a kezdő sorszámot [1...{elemszam}]: ")
    vegso_str = input(f"Add meg a befejező sorszámot [1...{elemszam}]: ")
    
    if kezdo_str.isdigit() and vegso_str.isdigit():
        kezdo = int(kezdo_str)
        vegso = int(vegso_str)
        
        if 1 <= kezdo <= elemszam and 1 <= vegso <= elemszam:
            ervenyes_intervalum = True
        else:
            print("Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...")
    else:
        print("Hibás adatbevitel! Próbáld meg újra...")

# 3. feladat
osszeg = 0
szorzat = 1
for i in range(kezdo - 1, vegso):
    osszeg += szamok[i]
    szorzat *= szamok[i]

if osszeg > szorzat:
    print("A lista elemeinek összege nagyobb.")
else:
    print("A lista első és utolsó elemeinek szorzata nagyobb.")

# 4. feladat
min_szam = szamok[0]
max_szam = szamok[0]

for i in range(1, elemszam):
    if szamok[i] < min_szam:
        min_szam = szamok[i]
    if szamok[i] > max_szam:
        max_szam = szamok[i]

if min_szam in szamok[kezdo - 1:vegso] and max_szam in szamok[kezdo - 1:vegso]:
    print("A legkisebb és legnagyobb szám megtalálható az intervallumban.")
else:
    print("A legkisebb és legnagyobb szám nem található meg az intervallumban.")

# 5. feladat
legkisebb_elem = min(szamok[kezdo - 1:vegso])
elofordulasok_szama = szamok.count(legkisebb_elem)

print(f"A lista {kezdo}. és {vegso}. elemei között található legkisebb szám: {legkisebb_elem}")
print(f"Előfordulások száma a teljes listában: {elofordulasok_szama}db")

# 6. feladat
negativ_szamok = [szam for szam in szamok if szam < 0]

if negativ_szamok:
    legnagyobb_negativ = max(negativ_szamok)
    pozicio = szamok.index(legnagyobb_negativ) + 1
    print(f"A listában található legnagyobb negatív szám: {legnagyobb_negativ}, helye: {pozicio}. pozíció")
else:
    print("A listában nincs negatív szám.")
