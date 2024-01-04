import random

# 1. feladat - Lista létrehozása
elemszam = 0

while not (30 <= elemszam <= 60):
    elemszam_input = input("Add meg a lista elemszámát [30...60]: ")

    if elemszam_input and 30 <= int(elemszam_input) <= 60:
        elemszam = int(elemszam_input)
    else:
        print("Hibás adatbevitel! Próbáld meg újra...")

szamok = [random.randint(-100, 100) for _ in range(elemszam)]

# 2. feladat - Tartalom kiírása
kezdo_sorszam, befejezo_sorszam = 0, 0

while not (1 <= kezdo_sorszam <= elemszam) or not (1 <= befejezo_sorszam <= elemszam and befejezo_sorszam >= kezdo_sorszam):
    kezdo_sorszam_input = input("Add meg a kezdő sorszámot [1...{}]: ".format(elemszam))
    befejezo_sorszam_input = input("Add meg a befejező sorszámot [1...{}]: ".format(elemszam))

    if kezdo_sorszam_input and befejezo_sorszam_input:
        kezdo_sorszam, befejezo_sorszam = int(kezdo_sorszam_input), int(befejezo_sorszam_input)

    if not (1 <= kezdo_sorszam <= elemszam) or not (1 <= befejezo_sorszam <= elemszam and befejezo_sorszam >= kezdo_sorszam):
        print("Hibás adatbevitel! Próbáld meg újra...")

kivalasztott_terulet = szamok[kezdo_sorszam - 1:befejezo_sorszam]
print("Kiválasztott terület: ", kivalasztott_terulet)

# 3. feladat - Összegzés vagy szorzás
osszeg = 0
szorzat = 1

for szam in kivalasztott_terulet:
    osszeg += szam
    szorzat *= szam

print("A lista kiválasztott területének összege:", osszeg)
print("A lista első és utolsó elemének szorzata:", szorzat)

# 4. feladat - Minimum és maximum keresés
legkisebb, legnagyobb = 101, -101

for szam in szamok:
    if kezdo_sorszam <= szam <= befejezo_sorszam:
        legkisebb = min(legkisebb, szam)
        legnagyobb = max(legnagyobb, szam)

if legkisebb == 101:
    print("A legkisebb elem nem található meg a kiválasztott területen.")
else:
    print("A listában található legkisebb szám a kiválasztott területen:", legkisebb)

if legnagyobb == -101:
    print("A legnagyobb elem nem található meg a kiválasztott területen.")
else:
    print("A listában található legnagyobb szám a kiválasztott területen:", legnagyobb)

# 5. feladat - Előfordulások száma
legkisebb_elofordulasok = kivalasztott_terulet.count(legkisebb)
print("A legkisebb elem előfordulásainak száma a teljes listában:", legkisebb_elofordulasok)

# 6. feladat - Legnagyobb negatív szám pozíciója
legnagyobb_negativ = max((szam, index + 1) for index, szam in enumerate(szamok) if szam < 0)
if legnagyobb_negativ[0] >= 0:
    print("A listában nincs negatív szám.")
else:
    print("A listában található legnagyobb negatív szám: {}, helye: {}."(legnagyobb_negativ[0], legnagyobb_negativ[1]))
