import random

# 1. feladat
while True:
    try:
        elemszam = int(input("Add meg a lista elemszámát [30...60]: "))
        if 30 <= elemszam <= 60:
            break
        else:
            print("Hibás adatbevitel! Próbáld meg újra...")
    except ValueError:
        print("Hibás adatbevitel! Próbáld meg újra...")

szamok = [random.randint(-100, 100) for _ in range(elemszam)]

# 2. feladat
while True:
    try:
        kezdo_sorszam = int(input("Add meg a kezdő sorszámot [1...{}]: ".format(elemszam)))
        if 1 <= kezdo_sorszam <= elemszam:
            break
        else:
            print("Hibás adatbevitel! Próbáld meg újra...")
    except ValueError:
        print("Hibás adatbevitel! Próbáld meg újra...")

while True:
    try:
        befejezo_sorszam = int(input("Add meg a befejező sorszámot [1...{}]: ".format(elemszam)))
        if 1 <= befejezo_sorszam <= elemszam and befejezo_sorszam >= kezdo_sorszam:
            break
        else:
            print("Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...")
    except ValueError:
        print("Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...")

kivalasztott_terulet = szamok[kezdo_sorszam - 1:befejezo_sorszam]

# 3. feladat
osszeg = 0
szorzat = szamok[0] * szamok[-1]

for szam in kivalasztott_terulet:
    osszeg += szam

if osszeg > szorzat:
    print("A lista {} és {} közötti elemeinek összege: {}".format(kezdo_sorszam, befejezo_sorszam, osszeg))
    print("A lista első és utolsó elemének szorzata: {} * {} = {}".format(szamok[0], szamok[-1], szorzat))
    print("A lista első és utolsó elemének szorzata nagyobb.")
else:
    print("A lista {} és {} közötti elemeinek összege: {}".format(kezdo_sorszam, befejezo_sorszam, osszeg))
    print("A lista első és utolsó elemének szorzata: {} * {} = {}".format(szamok[0], szamok[-1], szorzat))
    print("A lista {} és {} közötti elemeinek összege vagy a lista első és utolsó elemének szorzata nagyobb.".format(kezdo_sorszam, befejezo_sorszam))

# 4. feladat
legkisebb = min(szamok)
legnagyobb = max(szamok)

if legkisebb >= kivalasztott_terulet[0] and legnagyobb <= kivalasztott_terulet[-1]:
    print("A listában található legkisebb szám: {}".format(legkisebb))
    print("A listában található legnagyobb szám: {}".format(legnagyobb))
    print("A legkisebb elem megtalálható a(z) {} és a(z) {} sorszámú elemek között.".format(kezdo_sorszam, befejezo_sorszam))
    print("A legnagyobb elem megtalálható a(z) {} és a(z) {} sorszámú elemek között.".format(kezdo_sorszam, befejezo_sorszam))
else:
    print("A legkisebb elem nem található meg a(z) {} és a(z) {} sorszámú elemek között.".format(kezdo_sorszam, befejezo_sorszam))
    print("A legnagyobb elem megtalálható a(z) {} és a(z) {} sorszámú elemek között.".format(kezdo_sorszam, befejezo_sorszam))

# 5. feladat
legkisebb_elem_teruleten = min(kivalasztott_terulet)
elofordulasok_szama = szamok.count(legkisebb_elem_teruleten)

print("A lista {} és {} közötti elemei között található legkisebb szám: {}".format(kezdo_sorszam, befejezo_sorszam, legkisebb_elem_teruleten))
print("Előfordulások száma a teljes listában: {} db".format(elofordulasok_szama))

# 6. feladat
legnagyobb_negativ = None
legnagyobb_negativ_index = -1

for i, szam in enumerate(szamok):
    if szam < 0 and (legnagyobb_negativ is None or szam > legnagyobb_negativ):
        legnagyobb_negativ = szam
        legnagyobb_negativ_index = i

if legnagyobb_negativ is not None:
    print("A listában található legnagyobb negatív szám: {}, helye: {}.".format(legnagyobb_negativ, legnagyobb_negativ_index + 1))
else:
    print("A listában nincs negatív szám.")
