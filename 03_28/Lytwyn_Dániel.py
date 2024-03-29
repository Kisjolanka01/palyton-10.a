# 1. feladat

file = open("adat.txt", "r", encoding="UTF-8")
lista = []
for sor in file:
    lista.append(sor.replace("\n", "").strip().split())
file.close()

for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == 0:
            lista[i][j] = int(lista[i][j])
        if j == 4:
            lista[i][j] = int(lista[i][j])

# 2. feladat
eladasok = 0
for i in range(len(lista)):
    eladasok += 1
print(f"2. feladat\nA fájlban található tranzakciók (eladások) száma: {eladasok}")

# 3. feladat
darab = 0
for i in range(len(lista)):
    for j in range(len(lista)):
        if j == 4:
            darab += lista[i][j]
print(f"3. feladat\nÖsszes eladott termék száma: {darab} db")

# 4. feladat
print("4. feladat")
while True:
    nap = int(input("Add meg a nap sorszámát [1...28]: "))
    if nap > 0 and nap < 29:
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

# 5. feladat
termekek = [600, 750, 550, 650, 450]
maximumertek = 0
legtobb_erteku_munkas =  ""
print("5. feladat\nAz egyes munkatársak által generált bevételek:")
for i in range(1, 6):
    munkasbevetel = 0
    munkas =  ""
    for j in range(len(lista)):
        for k in range(len(lista[j])):
            if lista[j][k] == f"M{i}":
                munkasbevetel += lista[j][k - 3] * termekek[int(lista[j][k + 1].replace("T", "")) - 1]
                munkas = f"M{i}"
    if munkasbevetel > maxertek:
        maxertek = munkasbevetel
        legtobb_erteku_munkas = munkas
    print(f"{munkas}: {munkasbevetel} Ft")
print(f"A legtöbb bevételt az {legtobb_erteku_munkas} kódú munkatárs generálta.")
# 6. feladat