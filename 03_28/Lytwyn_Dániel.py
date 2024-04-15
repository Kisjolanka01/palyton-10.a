file = open("adat.txt", "r", encoding="UTF-8")
lista = []
for sor in file:
    lista.append(sor.replace("\n", "").strip().split())
file.close()

for i in range(len(lista)):
    for j in range(0, len(lista[i]), 4):
            lista[i][j] = int(lista[i][j])

print("2. feladat")
print(f"A fájlban található tranzakciók (eladások) száma: {len(lista)}")

darab = 0
for i in range(len(lista)):
    for j in range(4, len(lista[i]), 4):
        darab += lista[i][j]
print("3. feladat")
print(f"Összes eladott termék száma: {darab} db")

print("4. feladat")
while True:
    nap = int(input("Add meg a nap sorszámát [1...28]: "))
    if 1 <= nap <= 28:
        break
    print("Hibás adatbevitel! Próbáld újra...")

forgalom = False
for i in range(len(lista)):
    if lista[i][0] == nap:
        for j in range(1, len(lista[i])):
            print(lista[i][j], end=" ")
            forgalom = True
        print()
if forgalom == False:
    print("A megadott napon nem volt forgalma a cégnek.")

termekek = [600, 750, 550, 650, 450]
maximumertek = 0
maxertekmunkas = ""
print("5. feladat")
print("Az egyes munkatársak által generált bevételek:")
for i in range(1, 6):
    munkasbevetel = 0
    munkaskod = "M"+str(i)
    for j in range(len(lista)):
        for k in range(len(lista[j])):
            if lista[j][k] == munkaskod:
                munkasbevetel += lista[j][k - 3] * termekek[int(lista[j][k + 1].replace("T", "")) - 1]
                munkas = munkaskod
    if munkasbevetel > maximumertek:
        maximumertek = munkasbevetel
        maxertekmunkas = munkas
    print(f"{munkas}: {munkasbevetel} Ft")
print(f"A legtöbb bevételt az {maxertekmunkas} kódú munkatárs generálta.")