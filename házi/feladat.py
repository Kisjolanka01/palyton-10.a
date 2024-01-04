import random

# 1. Feladat
lista = []

n = int(input("Add meg a lista elemszámét [30...60]: "))

while (n < 30 or n > 60):
    print("hibás adatbevitel! Próbáld meg újra...")
    n = int(input("Add meg a lista elemszámét [30...60]: "))

for i in range(n):
    lista.append(random.randint(-100, 100))

# 2. Feladat
start = int(input(f"Add meg a kezdő sorszámot [1...{n}]: "))
while (start < 1 or start > n):
    print("Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...")
    start = int(input(f"Add meg a kezdő sorszámot [1...{n}]: "))

end = int(input(f"Add meg a befejező sorszámot [1...{n}]: "))
while (end < 1 or end > n or end < start):
    print("Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...")
    end = int(input(f"Add meg a befejező sorszámot [1...{n}]: "))

lista2feladat = []

for i in range(start, end + 1):
    lista2feladat.append(lista[i])
    print(f"{i}. elem: {lista[i]}")

# 3. Feladat
osszeg = 0
for elem in lista2feladat:
    osszeg += elem

print(f"A lista {start}. és {end}. közötti elemeinek összege: {osszeg}")

                             #lista2feladat[lista2feladat.length - 1]
szorzat = lista2feladat[0] * lista2feladat[-1]

print(f"A lista első és utolsó elemének szorzata: {lista2feladat[0]} * {lista2feladat[-1]} = {szorzat}")

if(osszeg > szorzat):
    print(f"A lista {start}. és {end}. közötti elemeinek összege a nagyobb.")
else:
    print(f"A lista első és utolsó elemének szorzata a nagyobb.")

# 4. Feladat
min = lista[0]
max = lista[0]

for elem in lista:
    if elem < min:
        min = elem
    if elem > max:
        max = elem

print(f"A listában található legkisebb szám: {min}")
print(f"A listában található legnagyobb szám: {max}")

vanBenne = False

for elem in lista2feladat:
    if(min == elem):
        vanBenne = True

if(vanBenne):
    print(f"A legkisebb szám megtalálható a(z) {start}. és a(z) {end}. sorszámú elemek között.")
else:
    print(f"A legkisebb szám nem megtalálható a(z) {start}. és a(z) {end}. sorszámú elemek között.")

vanBenne = False

for elem in lista2feladat:
    if(max == elem):
        vanBenne = True

if(vanBenne):
    print(f"A legnagyobb szám megtalálható a(z) {start}. és a(z) {end}. sorszámú elemek között.")
else:
    print(f"A legnagyobb szám nem megtalálható a(z) {start}. és a(z) {end}. sorszámú elemek között.")

# 5. Feladat
min = lista2feladat[0]

for elem in lista2feladat:
    if elem < min:
        min = elem

print(f"A lista {start}. és {end}. elemei között található legkisebb szám: {min}")

db = 0
for elem in lista:
    if(elem == min):
        db += 1

print(f"Előfordulások száma a teljes listában: {db}db")

# 6. Feladat
min = lista[0]

for elem in lista:
    if(elem < min):
        min = elem

vanNegativ = False
maxIndex = 0
max = min

for i in range(len(lista)):
    elem = lista[i]
    if(elem < 0):
        vanNegativ = True
        if(elem > max):
            max = elem
            maxIndex = i

if(vanNegativ):
    print(f"A listában található legnagyobb negatív szám: {max}, helye: {maxIndex} pozíció.")
else:
    print(f"A listában nincs negatív szám.")