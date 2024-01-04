import random

# 1. Feladat
lista = []

while True:
    szam = int(input("Add meg a lista elemszámát [30...60]: "))
    if szam >= 30 and szam <= 60:
        break
    print("Hibás adatbevitel! Próbáld meg újra...")

for i in range(szam):
    lista.append(random.randint(-100, 100))

# 2. Feladat
kezdo = int(input(f"Add meg a kezdő sorszámot [1...{szam}]: "))
while (kezdo < 1 or kezdo > szam):
    print("Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...")
    kezdo = int(input(f"Add meg a kezdő sorszámot [1...{szam}]: "))

befejezo = int(input(f"Add meg a befejező sorszámot [1...{szam}]: "))
while (befejezo < 1 or befejezo > szam or befejezo < kezdo):
    print("Hibás adatbevitel! Próbáld meg újra...")
    befejezo = int(input(f"Add meg a befejező sorszámot [1...{szam}]: "))

for i in range(kezdo - 1, befejezo):
    print(f"{i + 1}. elem: {lista[i]}")

# 3. Feladat
osszeg = 0
for e in lista:
    osszeg = osszeg + e

print(f"A lista {kezdo}. és {befejezo}. közötti elemeinek összege: {osszeg}")

szorzat = lista[0] * lista[-1]

print(f"A lista első és utolsó elemének szorzata: {lista[0]} * {lista[-1]} = {szorzat}")

if (osszeg > szorzat):
    print(f"A lista {kezdo}. és {befejezo}. közötti elemeinek összege a nagyobb.")
else:
    print(f"A lista első és utolsó elemének szorzata a nagyobb.")

# 4. Feladat
minErtek = lista[0]
maxErtek = lista[0]

for elem in lista:
    if elem < minErtek:
        minErtek = elem
    if elem > maxErtek:
        maxErtek = elem

print(f"A listában található legkisebb szám: {minErtek}")
print(f"A listában található legnagyobb szám: {maxErtek}")

van = False

for e in lista:
    if minErtek == e:
        van = True

if van:
    print(f"A legkisebb szám megtalálható a(z) {kezdo}. és a(z) {befejezo}. sorszámú elemek között.")
else:
    print(f"A legkisebb szám nem megtalálható a(z) {kezdo}. és a(z) {befejezo}. sorszámú elemek között.")

van = False
for e in lista:
    if maxErtek == e:
        van = True

if van:
    print(f"A legnagyobb szám megtalálható a(z) {kezdo}. és a(z) {befejezo}. sorszámú elemek között.")
else:
    print(f"A legnagyobb szám nem megtalálható a(z) {kezdo}. és a(z) {befejezo}. sorszámú elemek között.")

# 5. Feladat
minErtek = lista[0]

for e in lista:
    if e < minErtek:
        minErtek = e

print(f"A lista {kezdo}. és {befejezo}. elemei között található legkisebb szám: {minErtek}")

db = 0
for e in lista:
    if e == minErtek:
        db += 1

print(f"Előfordulások száma a teljes listában: {db} db")

# 6. Feladat
minErtek = lista[0]
for e in lista:
    if e < minErtek:
        minErtek = e

van = False
maxIndex = 0
maxErtek = minErtek
for i in range(len(lista)):
    if lista[i] < 0:
        van = True
        if lista[i] > maxErtek:
            maxErtek = lista[i]
            maxIndex = i

if van:
    print(f"A listában található legnagyobb negatív szám: {maxErtek}, helye: {maxIndex} pozíció.")
else:
    print(f"A listában nincs negatív szám.")